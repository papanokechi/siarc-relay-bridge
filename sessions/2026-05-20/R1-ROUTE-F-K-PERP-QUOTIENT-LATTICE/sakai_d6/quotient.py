"""Rank-2 quotient lattice Q := K_X^perp / L_delta on the PIII(D_6)
Sakai surface (canonical KNY 2017 sec.8.2.19 simple-root convention).

Cycle 3b of the R1-ROUTE-F program (split by synthesizer dispatch
from the original three-cycle brief). Predecessors:

  - Cycle 1 (R1-ROUTE-F-SAKAI-NONGEN, bridge commit 53efe94)
    fixed the canonical KNY embedding `d6_affine_simple_roots_kny()`.
  - Cycle 2 (R1-ROUTE-F-K-PERP-BASIS, bridge commit 139fa8b)
    proved L_delta is SATURATED at rank 7 inside K_X^perp (all
    elementary divisors = 1, saturation index 1).
  - Cycle 3a (R1-ROUTE-F-EFFECTIVITY, bridge commit baf650a)
    classified all 7 KNY delta_i as `effective` with trivial
    decompositions in the 10-component irreducible basis.

Scope (per synthesizer cycle-3b brief)
--------------------------------------
Compute the rank-2 quotient lattice Q := K_X^perp / L_delta where:

  - K_X^perp is rank 9 (cycle-2 substrate, `k_perp_basis()`).
  - L_delta = Z<delta_0, ..., delta_6> is rank 7, saturated inside
    K_X^perp (cycle-2 verdict SATURATED_AT_RANK_7).

Therefore Q is a torsion-free rank-2 abelian group, i.e. Z^2 as an
abelian group. We compute:

  1. An explicit Z-basis (q_1, q_2) of Q lifted to K_X^perp (and
     hence Pic) coordinates.
  2. The 2x2 integer Gram matrix of (q_1, q_2) under the restriction
     of the Pic intersection form (well-defined modulo L_delta when
     the lifts are chosen consistently, but the Gram of the lifted
     representatives suffices since L_delta lies in the radical of
     the form-on-quotient projection along -K_X --- see verify
     `verify_minus_K_X_projects_to_zero`).
  3. The discriminant disc(Q) = det(Gram).
  4. The exact signature (p, n, z) of Gram over Q ⊗ Q (integer
     2x2: classified by det and trace).
  5. The verdict branch: exactly one of
       - Q_DEFINITE_NEGATIVE  (det > 0, trace < 0)
       - Q_DEFINITE_POSITIVE  (det > 0, trace > 0)
       - Q_LORENTZIAN         (det < 0)
       - Q_DEGENERATE_WITH_ISOTROPIC_LINE  (det == 0, Gram != 0)
       - Q_TOTALLY_ISOTROPIC  (det == 0, Gram == 0)

Algorithm
---------
Let M be the 7x9 integer matrix `kny_in_k_perp_coords()` whose row
i gives delta_i in K_X^perp basis coordinates. Equivalently
L_delta = row-span of M inside Z^9.

Let A := M^T (9 x 7); columns of A are the delta_i in K_X^perp
coordinates. The Smith Normal Form `smith_normal_decomp` of A
returns (D, U, V) with U (9x9) and V (7x7) unimodular and
U @ A @ V = D. D is 9x7 with diagonal entries d_1, ..., d_7 (the
elementary divisors of A) and trailing zero rows 7 and 8.

Since cycle 2 established d_1 = ... = d_7 = 1 (saturation), the
column-span of A in Z^9 is precisely the kernel of the projection
Z^9 -> Z^9 / col(A), and U maps col(A) onto Z^7 x {0}^2.
Therefore U^{-1}(e_7) and U^{-1}(e_8) are Z-generators of a
complementary direct summand of col(A) inside Z^9, i.e. they lift
a Z-basis of Q = (Z^9 / col(A)) to Z^9. Their primitivity (i.e.
that they generate a SATURATED rank-2 sublattice in Z^9) follows
from U being unimodular.

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

import numpy as np
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_decomp

from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    anti_canonical,
    intersect,
)
from sakai_d6.saturation import (
    K_PERP_BASIS,
    RANK_K_PERP,
    RANK_KNY,
    kny_in_k_perp_coords,
)


RANK_Q = 2
RANK_L_DELTA = RANK_KNY  # 7
EXPECTED_DIVISORS_FROM_CYCLE2 = (1, 1, 1, 1, 1, 1, 1)


# ---------------------------------------------------------------------------
# SNF decomposition (cached)
# ---------------------------------------------------------------------------

_SNF_CACHE: tuple[Matrix, Matrix, Matrix, Matrix] | None = None


def _snf_decomposition() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    """Return (D, U, V, U_inv) for A = (kny_in_k_perp_coords())^T.

    A is 9x7 with columns equal to delta_i in K_X^perp coords.
    U is 9x9 unimodular, V is 7x7 unimodular, D is 9x7 with
    U @ A @ V == D. By cycle-2 saturation, the diagonal entries
    of D are all 1.

    U_inv (= U^{-1}) is the integer 9x9 matrix whose last 2
    columns lift a Z-basis of the quotient Q = Z^9 / col(A) to Z^9.
    """
    global _SNF_CACHE
    if _SNF_CACHE is None:
        M_np = kny_in_k_perp_coords()  # 7 x 9
        A = Matrix(M_np.T.tolist())  # 9 x 7
        D, U, V = smith_normal_decomp(A)
        U_inv = U.inv()
        _SNF_CACHE = (D, U, V, U_inv)
    return _SNF_CACHE


# ---------------------------------------------------------------------------
# Quotient basis
# ---------------------------------------------------------------------------


def k_perp_quotient_basis() -> np.ndarray:
    """Z-basis (q_1, q_2) of the rank-2 quotient Q in K_X^perp coords.

    Returns a 2x9 integer matrix; row k is q_k expressed in the
    K_X^perp basis (b_1, ..., b_9) of `saturation.K_PERP_BASIS`.

    The lift is constructed from the last two columns of U^{-1},
    where (D, U, V) = smith_normal_decomp(A) for A = M^T (9x7).
    This is a SATURATED Z-lift (primitive in Z^9) because U is
    unimodular.
    """
    _D, _U, _V, U_inv = _snf_decomposition()
    q1 = np.array([int(U_inv[i, RANK_KNY]) for i in range(RANK_K_PERP)], dtype=np.int64)
    q2 = np.array([int(U_inv[i, RANK_KNY + 1]) for i in range(RANK_K_PERP)], dtype=np.int64)
    return np.stack([q1, q2], axis=0)


def quotient_basis_in_pic_coords() -> np.ndarray:
    """The Z-basis (q_1, q_2) expressed in canonical Pic(X) coords.

    Returns a 2x10 integer matrix.
    """
    Q_kperp = k_perp_quotient_basis()  # 2 x 9
    return (Q_kperp @ K_PERP_BASIS).astype(np.int64)


# ---------------------------------------------------------------------------
# Gram matrix, discriminant, signature
# ---------------------------------------------------------------------------


def quotient_gram_matrix() -> np.ndarray:
    """The 2x2 integer Gram matrix of (q_1, q_2) under the Pic form."""
    Q_pic = quotient_basis_in_pic_coords()  # 2 x 10
    G = (Q_pic @ GRAM_PIC @ Q_pic.T).astype(np.int64)
    return G


def quotient_discriminant() -> int:
    """The discriminant disc(Q) = det(Gram(Q))."""
    G = quotient_gram_matrix()
    return int(G[0, 0]) * int(G[1, 1]) - int(G[0, 1]) * int(G[1, 0])


def quotient_signature() -> tuple[int, int, int]:
    """The signature (p, n, z) of the 2x2 integer Gram matrix.

    Computed by EXACT integer logic (no eigenvalue tolerance is
    needed for 2x2): let G = [[a, b], [b, c]], det = ac - b^2,
    trace = a + c. Then:

      - det > 0 and trace > 0  -> (2, 0, 0)
      - det > 0 and trace < 0  -> (0, 2, 0)
      - det > 0 and trace == 0 -> impossible for 2x2 symmetric
        with real entries (would mean a + c = 0 and ac > b^2;
        but then a, c have opposite signs and ac <= 0, contradiction).
      - det < 0                -> (1, 1, 0)
      - det == 0 and G != 0    -> (1, 0, 1) if trace > 0
                                  (0, 1, 1) if trace < 0
                                  (cannot have trace == 0 with G != 0
                                  unless a == c == 0 and b != 0, in
                                  which case the form is [0 b; b 0]
                                  which has signature (1, 1, 0) -- but
                                  det == -b^2 < 0, contradicting det == 0;
                                  so this branch unreachable when det == 0)
      - det == 0 and G == 0    -> (0, 0, 2)

    Returns (p, n, z) with p + n + z == 2.
    """
    G = quotient_gram_matrix()
    a = int(G[0, 0])
    b = int(G[0, 1])
    c = int(G[1, 1])
    det = a * c - b * b
    trace = a + c

    if G[0, 0] == 0 and G[0, 1] == 0 and G[1, 1] == 0:
        return (0, 0, 2)

    if det > 0:
        if trace > 0:
            return (2, 0, 0)
        if trace < 0:
            return (0, 2, 0)
        # det > 0, trace == 0: impossible per docstring.
        raise ValueError(
            f"Numerically inconsistent 2x2 Gram: det={det}>0 yet trace==0 "
            f"(Gram={G.tolist()}). Possible substrate corruption."
        )
    if det < 0:
        return (1, 1, 0)
    # det == 0, G != 0: one eigenvalue is 0, the other is trace.
    if trace > 0:
        return (1, 0, 1)
    if trace < 0:
        return (0, 1, 1)
    # det == 0, trace == 0, G != 0: would require a = -c and ac = b^2.
    # Then ac = -a^2 <= 0 forces b == 0 and a == 0, hence c == 0,
    # contradicting G != 0. Unreachable.
    raise ValueError(
        f"Numerically inconsistent 2x2 Gram: det==0, trace==0, but G != 0 "
        f"(Gram={G.tolist()}). Possible substrate corruption."
    )


def quotient_classification() -> str:
    """Resolve the verdict to exactly one of the five branches."""
    G = quotient_gram_matrix()
    a = int(G[0, 0])
    b = int(G[0, 1])
    c = int(G[1, 1])
    det = a * c - b * b
    trace = a + c

    if det > 0:
        if trace > 0:
            return "Q_DEFINITE_POSITIVE"
        if trace < 0:
            return "Q_DEFINITE_NEGATIVE"
        # det > 0 with trace == 0 unreachable for real 2x2 symmetric.
        raise ValueError(
            f"Inconsistent verdict: det={det}>0, trace==0 (Gram={G.tolist()})."
        )
    if det < 0:
        return "Q_LORENTZIAN"
    # det == 0.
    if a == 0 and b == 0 and c == 0:
        return "Q_TOTALLY_ISOTROPIC"
    return "Q_DEGENERATE_WITH_ISOTROPIC_LINE"


# ---------------------------------------------------------------------------
# Verification flags
# ---------------------------------------------------------------------------


def verify_quotient_basis_is_in_k_perp() -> bool:
    """Each q_k (in Pic coords) pairs with -K_X to zero."""
    k_anti = anti_canonical()
    Q_pic = quotient_basis_in_pic_coords()
    for v in Q_pic:
        if intersect(v.astype(np.int64), k_anti) != 0:
            return False
    return True


def verify_quotient_basis_is_primitive() -> bool:
    """The 2x9 K-perp coord matrix has unimodular 2x2 minor structure.

    For a saturated rank-2 sublattice of Z^9, the gcd of the 2x2
    minors of the 2x9 matrix must equal 1. (Equivalently the SNF
    of the 2x9 matrix has elementary divisors (1, 1).)
    """
    Q_kperp = k_perp_quotient_basis()
    snf_q = Matrix(Q_kperp.tolist())
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(snf_q)
    # D is 2x9; check the two diagonal entries are 1.
    return int(D[0, 0]) == 1 and int(D[1, 1]) == 1


def verify_minus_K_X_projects_to_zero() -> bool:
    """-K_X (in K_X^perp coords) has zero image in Q.

    Equivalent: writing kfree = (-K_X)_{K_perp coords} as a 9-vector
    and applying U, the last two entries of U @ kfree must vanish.
    This is the defining condition that -K_X lies in col(A) =
    L_delta inside K_X^perp.
    """
    _D, U, _V, _U_inv = _snf_decomposition()
    free_idx = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    kfree = anti_canonical()[free_idx].astype(np.int64)
    Uk = U * Matrix(kfree.tolist())  # 9 x 1
    last_two = (int(Uk[RANK_KNY, 0]), int(Uk[RANK_KNY + 1, 0]))
    return last_two == (0, 0)


def verify_elementary_divisors_match_cycle2() -> bool:
    """The 7 elementary divisors of A = M^T are all 1, matching
    cycle-2 saturation. This is a halt-safety re-check."""
    D, _U, _V, _U_inv = _snf_decomposition()
    for i in range(RANK_KNY):
        if int(D[i, i]) != 1:
            return False
    return True


def verify_snf_decomp_holds() -> bool:
    """U @ A @ V == D (sympy SNF contract sanity)."""
    M_np = kny_in_k_perp_coords()
    A = Matrix(M_np.T.tolist())
    D, U, V, _U_inv = _snf_decomposition()
    return U * A * V == D


def verify_gram_is_symmetric() -> bool:
    G = quotient_gram_matrix()
    return int(G[0, 1]) == int(G[1, 0])


def verify_signature_within_pic_envelope() -> bool:
    """The Pic form has signature (1, 9); the rank-2 quotient's
    signature must therefore satisfy p in {0, 1} and n in {0, 1, 2}.
    """
    p, n, _z = quotient_signature()
    return p in (0, 1) and n in (0, 1, 2)


# ---------------------------------------------------------------------------
# Aggregate report
# ---------------------------------------------------------------------------


def verify_report() -> dict:
    """Aggregate every cycle-3b verification flag and the verdict."""
    G = quotient_gram_matrix()
    p, n, z = quotient_signature()
    disc = quotient_discriminant()
    Q_kperp = k_perp_quotient_basis().tolist()
    Q_pic = quotient_basis_in_pic_coords().tolist()
    verdict = quotient_classification()
    return {
        "rank_q": RANK_Q,
        "rank_l_delta": RANK_L_DELTA,
        "rank_k_perp": RANK_K_PERP,
        "quotient_basis_in_k_perp_coords": Q_kperp,
        "quotient_basis_in_pic_coords": Q_pic,
        "gram_matrix": [
            [int(G[0, 0]), int(G[0, 1])],
            [int(G[1, 0]), int(G[1, 1])],
        ],
        "discriminant": disc,
        "signature_p_n_z": [int(p), int(n), int(z)],
        "verdict": verdict,
        "snf_decomp_holds": verify_snf_decomp_holds(),
        "elementary_divisors_match_cycle2": verify_elementary_divisors_match_cycle2(),
        "quotient_basis_is_in_k_perp": verify_quotient_basis_is_in_k_perp(),
        "quotient_basis_is_primitive": verify_quotient_basis_is_primitive(),
        "minus_K_X_projects_to_zero": verify_minus_K_X_projects_to_zero(),
        "gram_is_symmetric": verify_gram_is_symmetric(),
        "signature_within_pic_envelope": verify_signature_within_pic_envelope(),
    }


# ---------------------------------------------------------------------------
# Artefact emission
# ---------------------------------------------------------------------------


def _write_artefacts(rep: dict, out_dir: Path) -> None:
    """Write quotient_verdict.json and quotient_basis_provenance.json."""
    out_dir.mkdir(parents=True, exist_ok=True)
    verdict_artefact = {
        "verdict": rep["verdict"],
        "rank_q": rep["rank_q"],
        "gram_matrix": rep["gram_matrix"],
        "discriminant": rep["discriminant"],
        "signature_p_n_z": rep["signature_p_n_z"],
        "all_flags_ok": all(
            rep[k] for k in (
                "snf_decomp_holds",
                "elementary_divisors_match_cycle2",
                "quotient_basis_is_in_k_perp",
                "quotient_basis_is_primitive",
                "minus_K_X_projects_to_zero",
                "gram_is_symmetric",
                "signature_within_pic_envelope",
            )
        ),
    }
    provenance = {
        "k_perp_basis_shape": [RANK_K_PERP, DIM_PIC],
        "kny_in_k_perp_coords_shape": [RANK_KNY, RANK_K_PERP],
        "A_shape": [RANK_K_PERP, RANK_KNY],
        "elementary_divisors_of_A": list(EXPECTED_DIVISORS_FROM_CYCLE2),
        "lift_construction": (
            "Z-basis (q_1, q_2) of Q = Z^9 / col(A) is taken as columns "
            "7 and 8 (zero-indexed) of U^{-1}, where (D, U, V) = "
            "smith_normal_decomp(A) with U @ A @ V == D and U unimodular."
        ),
        "quotient_basis_in_k_perp_coords": rep["quotient_basis_in_k_perp_coords"],
        "quotient_basis_in_pic_coords": rep["quotient_basis_in_pic_coords"],
        "predecessor_cycle2_commit": "139fa8b",
        "predecessor_cycle3a_commit": "baf650a",
    }
    (out_dir / "quotient_verdict.json").write_text(
        json.dumps(verdict_artefact, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "quotient_basis_provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n"
    )


def _main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Print the cycle-3b verification report as JSON to stdout.",
    )
    parser.add_argument(
        "--write-artefacts",
        type=str,
        default=None,
        help="If set, write quotient_verdict.json and "
        "quotient_basis_provenance.json into the given directory.",
    )
    args = parser.parse_args()
    if not args.analyze and args.write_artefacts is None:
        parser.print_help()
        return 2

    rep = verify_report()
    if args.analyze:
        sys.stdout.write(json.dumps(rep, indent=2, sort_keys=True))
        sys.stdout.write("\n")
        sys.stdout.flush()

    if args.write_artefacts is not None:
        _write_artefacts(rep, Path(args.write_artefacts))

    # Halt-condition gate: every defensive flag must be true, and the
    # verdict must be one of the five allowed branches.
    flags_ok = (
        rep["snf_decomp_holds"]
        and rep["elementary_divisors_match_cycle2"]
        and rep["quotient_basis_is_in_k_perp"]
        and rep["quotient_basis_is_primitive"]
        and rep["minus_K_X_projects_to_zero"]
        and rep["gram_is_symmetric"]
        and rep["signature_within_pic_envelope"]
        and rep["verdict"] in {
            "Q_DEFINITE_NEGATIVE",
            "Q_DEFINITE_POSITIVE",
            "Q_LORENTZIAN",
            "Q_DEGENERATE_WITH_ISOTROPIC_LINE",
            "Q_TOTALLY_ISOTROPIC",
        }
    )
    return 0 if flags_ok else 1


if __name__ == "__main__":
    sys.exit(_main())
