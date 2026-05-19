"""K_X-perp basis and saturation analysis for cycle 2 of R1-ROUTE-F.

Task: R1-ROUTE-F-K-PERP-BASIS (cycle 2 of 3).
Predecessor: R1-ROUTE-F-SAKAI-NONGEN (bridge commit 53efe94),
which fixed the canonical Sakai-convention KNY embedding
`d6_affine_simple_roots_kny()` per KNY 2017 sec.8.2.19 eq (8.101).
The Pic intersection form is the (configuration-independent)
standard 8-point blow-up form per KNY 2017 sec.3.3 eq (3.26).

Goal of this module
-------------------
Decide whether the rank-7 sublattice L_delta = Z<delta_0,...,delta_6>
is SATURATED inside the rank-9 orthogonal complement
K_X^perp = { v in Pic(X) : <v, -K_X> = 0 }
under the Pic bilinear form.

Algorithm
---------
1. Compute K_X^perp as the kernel of the integer linear functional
   f(v) = <v, -K_X>_Pic. Since -K_X = (2, 2, -1, -1, ..., -1) and
   G(-K_X) = (2, 2, 1, 1, ..., 1) (with G = Pic form), f is the
   functional with content gcd = 1, hence ker(f) is a primitive
   rank-9 sublattice of Z^10 = Pic(X).

2. Pick the explicit Z-basis of K_X^perp:

       b_1 = H_1 - 2 E_1            (free param: H_1 coord)
       b_2 = H_2 - 2 E_1            (free param: H_2 coord)
       b_{3+k} = E_{2+k} - E_1      (free param: E_{2+k} coord, k = 0..6)

   with the constraint that E_1 = -2 v_H1 - 2 v_H2 - sum_{j=2..8} v_Ej.

3. Express each KNY delta_i as a Z-linear combination of {b_1..b_9}.
   This gives a 7x9 integer matrix M whose rows are the
   K_X^perp-coordinates of delta_0..delta_6.

4. Compute the Smith Normal Form of M. The resulting diagonal
   elementary divisors d_1, ..., d_7 determine the structure of
   K_X^perp / L_delta:

       K_X^perp / L_delta = (Z / d_1 Z) (+) ... (+) (Z / d_7 Z) (+) Z^{9-7}

   The TORSION part has order prod(d_i). L_delta is SATURATED in
   K_X^perp iff this torsion is trivial iff all d_i = 1.

5. If all d_i = 1 -> SATURATED_AT_RANK_7.
   Otherwise, the saturation closure L_delta^sat is the preimage
   of the torsion under the quotient map; we compute its
   generators and the index [L_delta^sat : L_delta] = prod(d_i).

References
----------
- Sakai 2001, "Rational surfaces associated with affine root
  systems and geometry of the Painleve equations",
  Comm. Math. Phys. 220, 165-229 (doi: 10.1007/s002200100393).
- KNY 2017 = Kajiwara-Noumi-Yamada, "Geometric Aspects of Painleve
  Equations", J. Phys. A 50 (2017) 073001 (arXiv:1509.08186v8),
  sec.3.3 eq (3.26) and sec.8.2.19 eq (8.101).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

import numpy as np
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    anti_canonical,
    d6_affine_simple_roots_kny,
    intersect,
    intersection_form_sakai_nongen,
)

# Rank of K_X^perp: -K_X is primitive in Pic, so ker(<-, -K_X>) is
# a primitive rank (10 - 1) = 9 sublattice.
RANK_K_PERP = 9
RANK_KNY = 7


def _functional_K_perp() -> np.ndarray:
    """The 1x10 row vector representing the integer linear functional
    f(v) = <v, -K_X>_Pic = (G v) . (-K_X).

    Returns the 10-vector whose dot product with any v in Pic(X)
    (in canonical coordinates) yields <v, -K_X>.
    """
    return GRAM_PIC @ anti_canonical()


def k_perp_basis() -> np.ndarray:
    """Explicit Z-basis for K_X^perp as a 9x10 integer matrix.

    Each row is one basis vector expressed in the canonical Pic(X)
    basis (H_1, H_2, E_1, E_2, ..., E_8). The construction
    parametrises the kernel of f(v) = 2 v_{H_1} + 2 v_{H_2}
    + sum_{j=1..8} v_{E_j} = 0 by free coordinates
    (v_{H_1}, v_{H_2}, v_{E_2}, ..., v_{E_8}) with
    v_{E_1} = - 2 v_{H_1} - 2 v_{H_2} - sum_{j=2..8} v_{E_j}.
    """
    basis = np.zeros((RANK_K_PERP, DIM_PIC), dtype=np.int64)
    # b_1 = H_1 - 2 E_1
    basis[0, 0] = 1
    basis[0, 2] = -2
    # b_2 = H_2 - 2 E_1
    basis[1, 1] = 1
    basis[1, 2] = -2
    # b_{3+k} = E_{2+k} - E_1 for k = 0..6 (i.e. E_2..E_8 minus E_1)
    for k in range(7):
        basis[2 + k, 2] = -1
        basis[2 + k, 3 + k] = 1
    return basis


# Cache: 9x10 integer matrix.
K_PERP_BASIS = k_perp_basis()


def verify_k_perp_basis_orthogonal_to_canonical() -> bool:
    """Each row of `k_perp_basis()` is orthogonal to -K_X."""
    k_anti = anti_canonical()
    for v in K_PERP_BASIS:
        if intersect(v, k_anti) != 0:
            return False
    return True


def verify_k_perp_basis_rank_is_9() -> bool:
    """The 9 vectors are Z-linearly independent (full row rank over Z).

    Sufficient: the matrix has a 9x9 minor with nonzero determinant.
    """
    rank_q = np.linalg.matrix_rank(K_PERP_BASIS.astype(np.float64))
    return int(rank_q) == RANK_K_PERP


def _solve_kny_in_k_perp_basis() -> np.ndarray:
    """Compute integer coordinates of each KNY delta_i in K_X^perp basis.

    Returns the 7x9 integer matrix M with M @ K_PERP_BASIS equal to
    the 7x10 KNY simple-root matrix. Computed by selecting the 9
    free coordinates (H_1, H_2, E_2, ..., E_8) of each delta_i and
    reading them off directly (this gives the K_X^perp coordinates
    by construction).
    """
    delta = d6_affine_simple_roots_kny()  # 7 x 10
    # Free coords of K_X^perp basis are indices:
    #   index 0 (H_1), index 1 (H_2), index 3..9 (E_2..E_8).
    free_idx = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    M = delta[:, free_idx].astype(np.int64).copy()
    return M


def kny_in_k_perp_coords() -> np.ndarray:
    """Public alias for `_solve_kny_in_k_perp_basis`."""
    return _solve_kny_in_k_perp_basis()


def verify_reconstruction() -> bool:
    """Sanity: M @ K_PERP_BASIS == d6_affine_simple_roots_kny()."""
    M = kny_in_k_perp_coords()
    reconstructed = M @ K_PERP_BASIS
    return np.array_equal(reconstructed, d6_affine_simple_roots_kny())


def verify_every_kny_delta_orthogonal_to_canonical() -> bool:
    """Defensive: each KNY delta_i is in K_X^perp (already a cycle-1
    invariant, re-checked here for halt-condition safety)."""
    k_anti = anti_canonical()
    for v in d6_affine_simple_roots_kny():
        if intersect(v, k_anti) != 0:
            return False
    return True


def smith_normal_form_of_kny() -> Matrix:
    """Smith Normal Form of the 7x9 matrix `kny_in_k_perp_coords`."""
    M = kny_in_k_perp_coords()
    return smith_normal_form(Matrix(M.tolist()))


def elementary_divisors() -> list[int]:
    """Return the 7 elementary divisors d_1 <= d_2 <= ... <= d_7
    (each d_i divides d_{i+1}). For a 7x9 SNF the divisors live on
    the diagonal positions (i, i) for i = 0..6; trailing columns
    are zero columns.
    """
    snf = smith_normal_form_of_kny()
    divs: list[int] = []
    for i in range(min(snf.rows, snf.cols)):
        if i < RANK_KNY:
            divs.append(int(snf[i, i]))
    return divs[:RANK_KNY]


def saturation_index() -> int:
    """The index [L_delta^sat : L_delta] = product of elementary
    divisors (over the nonzero ones). For a saturated sublattice
    the index is 1.
    """
    divs = elementary_divisors()
    idx = 1
    for d in divs:
        if d == 0:
            # Rank deficit: would indicate the rows are not Z-linearly
            # independent. Defensive return -1 so callers can halt.
            return -1
        idx *= d
    return idx


def verify_snf_has_exactly_seven_nonzero_elementary_divisors() -> bool:
    """Defensive: all 7 elementary divisors are nonzero (i.e. the
    KNY embedding has full Z-rank 7)."""
    divs = elementary_divisors()
    if len(divs) != RANK_KNY:
        return False
    return all(d != 0 for d in divs)


def verdict_saturation() -> str:
    """Resolve to exactly one of:
      - "SATURATED_AT_RANK_7" if all elementary divisors are 1;
      - f"NOT_SATURATED_WITH_INDEX_{k}" otherwise, where k = prod d_i.
    """
    idx = saturation_index()
    if idx == 1:
        return "SATURATED_AT_RANK_7"
    return f"NOT_SATURATED_WITH_INDEX_{idx}"


def saturation_closure_generators() -> list[list[int]]:
    """If L_delta is not saturated, return Z-generators of L_delta^sat
    in K_X^perp coordinates (9-vectors). If saturated, return an
    empty list.

    Uses SymPy's Smith Normal Form decomposition: the unimodular
    column transformation V satisfies M V = D (D = SNF). The
    columns of V corresponding to nonzero d_i, divided by d_i,
    give the L_delta^sat generators in the *transformed* basis;
    pulling back gives the closure in the original K_perp basis.
    """
    M = kny_in_k_perp_coords()
    if saturation_index() == 1:
        return []
    # When the index > 1, recompute SNF in the "with transforms"
    # form: there exist unimodular U (7x7), V (9x9) such that
    # U M V = D. We need V to back-transform. SymPy's
    # smith_normal_form_with_transforms is in
    # sympy.matrices.normalforms (1.11+).
    from sympy.matrices.normalforms import (
        smith_normal_decomp,  # type: ignore[attr-defined]
    )

    D, U, V = smith_normal_decomp(Matrix(M.tolist()))
    closure: list[list[int]] = []
    for i in range(RANK_KNY):
        d_i = int(D[i, i])
        if d_i > 1:
            # The (i-th column of V) / d_i is a candidate closure
            # element in the V-transformed basis; pulling back to
            # K_perp coords requires V^{-1}, but actually the closure
            # in K_perp coords is precisely the (i-th column of V)
            # divided by d_i AFTER expressing it as a 9-vector in
            # K_perp basis directly.
            col = [int(V[j, i]) for j in range(9)]
            # The generator of the closure is col / d_i (must be integer
            # by construction of SNF).
            gen = [c // d_i for c in col]  # exact in Z by SNF property
            closure.append(gen)
    return closure


# ---------------------------------------------------------------------------
# Aggregate report
# ---------------------------------------------------------------------------


def verify_report() -> dict:
    """Aggregate every cycle-2 verification flag and the verdict."""
    divs = elementary_divisors()
    idx = saturation_index()
    verdict = verdict_saturation()
    closure_gens = saturation_closure_generators() if idx not in (1, -1) else []
    return {
        "k_perp_rank": int(np.linalg.matrix_rank(K_PERP_BASIS.astype(np.float64))),
        "k_perp_basis_has_rank_9": verify_k_perp_basis_rank_is_9(),
        "k_perp_basis_orthogonal_to_canonical": verify_k_perp_basis_orthogonal_to_canonical(),
        "kny_orthogonal_to_canonical": verify_every_kny_delta_orthogonal_to_canonical(),
        "reconstruction_kny_from_k_perp_coords": verify_reconstruction(),
        "snf_seven_nonzero_elementary_divisors": verify_snf_has_exactly_seven_nonzero_elementary_divisors(),
        "elementary_divisors": divs,
        "saturation_index": idx,
        "cycle2_verdict": verdict,
        "n_closure_generators": len(closure_gens),
    }


def _main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Print the cycle-2 verification report as JSON to stdout.",
    )
    args = parser.parse_args()
    if not args.analyze:
        parser.print_help()
        return 2

    rep = verify_report()
    sys.stdout.write(json.dumps(rep, indent=2, sort_keys=True))
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Halt-condition gate: all defensive flags must be true; verdict
    # must be one of the two named branches; saturation_index in
    # [1, 6] per the pre-registered halt condition.
    flags_ok = (
        rep["k_perp_basis_has_rank_9"]
        and rep["k_perp_basis_orthogonal_to_canonical"]
        and rep["kny_orthogonal_to_canonical"]
        and rep["reconstruction_kny_from_k_perp_coords"]
        and rep["snf_seven_nonzero_elementary_divisors"]
        and rep["k_perp_rank"] == RANK_K_PERP
        and rep["saturation_index"] >= 1
        and rep["saturation_index"] <= 6
        and (
            rep["cycle2_verdict"] == "SATURATED_AT_RANK_7"
            or rep["cycle2_verdict"].startswith("NOT_SATURATED_WITH_INDEX_")
        )
    )
    return 0 if flags_ok else 1


if __name__ == "__main__":
    sys.exit(_main())
