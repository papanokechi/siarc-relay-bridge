"""Effectivity classification of the canonical Sakai-convention
KNY 2017 sec.8.2.19 eq (8.101) D_6^{(1)} simple roots
delta_0, ..., delta_6 on the PIII(D_6) Sakai rational surface.

Cycle 3a of the R1-ROUTE-F program (split by synthesizer dispatch
from the original three-cycle brief). Predecessor: cycle 2
saturation result (bridge commit 139fa8b).

Scope (per synthesizer cycle-3a brief)
--------------------------------------
For each delta_i (i = 0..6), classify the Pic class as one of:

  - 'effective'                            : admits a non-negative
                                             integer decomposition
                                             into the irreducible
                                             components of the
                                             configuration.
  - 'not_effective'                        : no such decomposition.
  - 'effective_after_named_Weyl_move'      : becomes effective after
                                             a single Weyl reflection
                                             through one of the other
                                             six delta_j.

Irreducible components of the KNY configuration
-----------------------------------------------
The base-point configuration P_{12} + P_{34} + P_{5678}
(KNY eq 8.98) produces a Sakai surface X = Bl_{8 pts}(P^1 x P^1)
whose boundary at infinity consists of:

  - 7 (-2)-curves forming the D_6^{(1)} Dynkin pattern: these are
    exactly the seven delta_i themselves.
       delta_0 = E_1 - E_2  (strict transform of E_1 after P_2 blown up)
       delta_1 = E_3 - E_4  (strict transform of E_3 after P_4 blown up)
       delta_2 = H_1 - E_1 - E_3  (strict transform of the H_1 fiber
                                   through the heads of chains
                                   {1,2} and {3,4})
       delta_3 = H_2 - E_5 - E_6  (strict transform of the H_2 fiber
                                   through P_5 with P_6 inf-near)
       delta_4 = E_6 - E_7  (strict transform of E_6 after P_7 blown up)
       delta_5 = E_5 - E_6  (strict transform of E_5 after P_6 blown up)
       delta_6 = E_7 - E_8  (strict transform of E_7 after P_8 blown up)
  - 3 (-1)-curves at the chain tips:
       E_2 (last in chain {1,2})
       E_4 (last in chain {3,4})
       E_8 (last in chain {5,6,7,8})

Total: 10 irreducible components. They form a Z-basis of Pic(X)
(verified by unimodular determinant check); every Pic class
therefore has a UNIQUE integer decomposition in this basis, and
effectivity reduces to non-negativity of the unique coefficients.

Weyl reflection
---------------
For a (-2)-root alpha (intersection-form self-pairing -2), the
Weyl reflection is

    r_alpha(v) = v + <v, alpha> alpha

where <v, alpha> is the Picard intersection form. With alpha^2 = -2
this satisfies r_alpha(alpha) = -alpha and r_alpha is an isometry
of the form. Since each delta_i is orthogonal to -K_X, every
reflection r_{delta_i} fixes K_X and so preserves K_X^perp setwise.

Reference: KNY 2017 J. Phys. A 50 073001 = arXiv:1509.08186v8,
sec.3 (Sakai surfaces and root systems) and sec.8.2.19 (the
D_6^{(1)} case for PIII(D_6)).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import sympy as sp

from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    H,
    E,
    anti_canonical,
    d6_affine_simple_roots_kny,
    intersect,
)


# ---------------------------------------------------------------------------
# Irreducible-component basis
# ---------------------------------------------------------------------------


def irreducible_components_kny() -> List[Tuple[str, np.ndarray]]:
    """Return the 10 irreducible components of the KNY configuration
    P_{12} + P_{34} + P_{5678} as (name, Pic-vector) pairs in the
    fixed order:

        delta_0, ..., delta_6, E_2, E_4, E_8.

    These curves form a Z-basis of Pic(X) (det = +/- 1; verified by
    `irreducible_basis_determinant`).
    """
    delta = d6_affine_simple_roots_kny()
    components: List[Tuple[str, np.ndarray]] = []
    for i in range(7):
        components.append((f"delta_{i}", delta[i].astype(np.int64)))
    components.append(("E_2", E(2).astype(np.int64)))
    components.append(("E_4", E(4).astype(np.int64)))
    components.append(("E_8", E(8).astype(np.int64)))
    return components


def irreducible_basis_matrix() -> np.ndarray:
    """Return the 10x10 integer matrix whose columns are the 10
    irreducible components in the order of `irreducible_components_kny`.
    """
    comps = irreducible_components_kny()
    M = np.stack([c[1] for c in comps], axis=1).astype(np.int64)
    assert M.shape == (DIM_PIC, len(comps)) == (10, 10)
    return M


def irreducible_basis_determinant() -> int:
    """Return the integer determinant of the irreducible-component
    matrix. Must equal +/- 1 for the components to form a Z-basis
    of Pic(X).
    """
    M = irreducible_basis_matrix()
    return int(sp.Matrix(M.tolist()).det())


# Module constant (cached).
IRREDUCIBLE_BASIS_MATRIX = irreducible_basis_matrix()
IRREDUCIBLE_COMPONENT_NAMES = [c[0] for c in irreducible_components_kny()]
IRREDUCIBLE_BASIS_DETERMINANT = irreducible_basis_determinant()


# ---------------------------------------------------------------------------
# Effectivity by unique integer decomposition
# ---------------------------------------------------------------------------


def unique_integer_decomposition(
    class_vector: Sequence[int],
) -> Dict[str, int]:
    """Solve M x = v exactly over Z for x. Returns a dict mapping
    component name to integer coefficient.

    Pre-condition: |det M| = 1 (verified at module load).

    Raises ValueError if the determinant is not unimodular (would
    require integer linear programming instead of a simple solve).
    """
    if abs(IRREDUCIBLE_BASIS_DETERMINANT) != 1:
        raise ValueError(
            "irreducible components do not form a Z-basis "
            f"(det = {IRREDUCIBLE_BASIS_DETERMINANT})"
        )
    v = np.asarray(class_vector, dtype=np.int64)
    if v.shape != (DIM_PIC,):
        raise ValueError(f"class_vector must have shape ({DIM_PIC},), got {v.shape}")
    M_sp = sp.Matrix(IRREDUCIBLE_BASIS_MATRIX.tolist())
    b_sp = sp.Matrix(v.tolist())
    x_sp = M_sp.solve(b_sp)
    # x_sp entries must be integers (since det = +/- 1)
    coeffs: List[int] = []
    for entry in x_sp:
        as_rational = sp.Rational(entry)
        if as_rational.q != 1:
            raise ValueError(
                f"decomposition has non-integer entry {entry} "
                f"despite unimodular basis (numerical bug)"
            )
        coeffs.append(int(as_rational.p))
    return dict(zip(IRREDUCIBLE_COMPONENT_NAMES, coeffs))


def is_effective(class_vector: Sequence[int]) -> bool:
    """True iff the unique integer decomposition has all
    non-negative coefficients.
    """
    decomp = unique_integer_decomposition(class_vector)
    return all(c >= 0 for c in decomp.values())


def effective_decomposition(
    class_vector: Sequence[int],
) -> Optional[Dict[str, int]]:
    """Return the effective decomposition dict if `class_vector` is
    effective, else None.

    The returned dict maps EVERY component name to its coefficient
    (including zeros), for round-trip transparency.
    """
    decomp = unique_integer_decomposition(class_vector)
    if all(c >= 0 for c in decomp.values()):
        return decomp
    return None


# ---------------------------------------------------------------------------
# Weyl reflection in the (-2)-root sense
# ---------------------------------------------------------------------------


def weyl_reflection(
    class_vector: Sequence[int],
    reflecting_root: Sequence[int],
) -> np.ndarray:
    """Apply the Weyl reflection r_alpha to a Pic class:

        r_alpha(v) = v + <v, alpha> alpha

    where <,> is the Picard intersection form and alpha is a
    (-2)-root (alpha^2 = -2). Returns an integer ndarray of shape
    (DIM_PIC,).

    Sign convention: r_alpha(alpha) = -alpha (since <alpha, alpha>
    = -2 produces +(-2)*alpha = -alpha when added to alpha).
    """
    v = np.asarray(class_vector, dtype=np.int64)
    alpha = np.asarray(reflecting_root, dtype=np.int64)
    if v.shape != (DIM_PIC,) or alpha.shape != (DIM_PIC,):
        raise ValueError(
            f"both vectors must have shape ({DIM_PIC},); "
            f"got v={v.shape}, alpha={alpha.shape}"
        )
    pairing = int(v @ GRAM_PIC @ alpha)
    return v + pairing * alpha


def try_weyl_moves_for_effectivity(
    class_vector: Sequence[int],
    avoid_index: Optional[int] = None,
) -> Optional[Tuple[int, np.ndarray, Dict[str, int]]]:
    """For a class that is `not_effective`, try a single Weyl
    reflection through each of the seven KNY simple roots delta_j
    (j = 0..6), optionally skipping index `avoid_index`. Return the
    first (j, r_{delta_j}(v), decomposition) for which the
    reflection produces an effective class, else None.
    """
    delta = d6_affine_simple_roots_kny()
    for j in range(7):
        if avoid_index is not None and j == avoid_index:
            continue
        reflected = weyl_reflection(class_vector, delta[j])
        decomp = effective_decomposition(reflected)
        if decomp is not None:
            return (j, reflected, decomp)
    return None


# ---------------------------------------------------------------------------
# Full classification pipeline
# ---------------------------------------------------------------------------


def classify_kny_root(i: int) -> Dict[str, object]:
    """Classify delta_i and return a result record."""
    if not (0 <= i <= 6):
        raise ValueError(f"i must be in 0..6, got {i}")
    delta = d6_affine_simple_roots_kny()
    v = delta[i]
    record: Dict[str, object] = {
        "delta_index": i,
        "class_vector_pic": v.tolist(),
        "self_intersection": int(intersect(v, v)),
        "intersection_with_anti_canonical": int(intersect(v, anti_canonical())),
    }
    decomp = effective_decomposition(v)
    if decomp is not None:
        record["verdict"] = "effective"
        record["decomposition"] = decomp
        return record
    moved = try_weyl_moves_for_effectivity(v, avoid_index=i)
    if moved is not None:
        j, reflected, post_decomp = moved
        record["verdict"] = "effective_after_named_Weyl_move"
        record["weyl_move_reflecting_through_delta_index"] = j
        record["reflected_class_vector_pic"] = reflected.tolist()
        record["post_reflection_decomposition"] = post_decomp
        return record
    record["verdict"] = "not_effective"
    return record


def classify_kny_roots() -> List[Dict[str, object]]:
    """Run the classification pipeline for delta_0, ..., delta_6.
    Returns a 7-element list of result records.
    """
    return [classify_kny_root(i) for i in range(7)]


# ---------------------------------------------------------------------------
# Cross-consistency check: verify the lattice-level properties of each
# effective decomposition.
# ---------------------------------------------------------------------------


def verify_effective_decomposition_lattice_consistent(
    class_vector: Sequence[int],
    decomp: Dict[str, int],
) -> bool:
    """For an effective decomposition c = sum n_k C_k, verify:

        sum n_k C_k == class_vector  (reconstruction)

    The intersection-form facts (-2) and orthogonal to -K_X are
    asserted upstream on the class_vector itself in cycle 1's tests
    and the cycle 2 K_perp tests; this function just verifies
    reconstruction.
    """
    comps = irreducible_components_kny()
    name_to_vec = {n: v for n, v in comps}
    reconstructed = np.zeros(DIM_PIC, dtype=np.int64)
    for name, coeff in decomp.items():
        if name not in name_to_vec:
            return False
        reconstructed = reconstructed + int(coeff) * name_to_vec[name]
    return np.array_equal(reconstructed, np.asarray(class_vector, dtype=np.int64))


# ---------------------------------------------------------------------------
# Verifier / CLI
# ---------------------------------------------------------------------------


def verify_report() -> Dict[str, object]:
    """Aggregate verification flags + classification table for the
    AEAL-hashed verifier output.
    """
    classification = classify_kny_roots()

    # Top-level flags
    flags: Dict[str, object] = {}
    flags["irreducible_basis_determinant_is_unimodular"] = (
        abs(IRREDUCIBLE_BASIS_DETERMINANT) == 1
    )
    flags["all_seven_delta_classified"] = len(classification) == 7
    verdicts = [r["verdict"] for r in classification]
    flags["all_seven_delta_effective"] = all(v == "effective" for v in verdicts)
    flags["every_verdict_in_allowed_branches"] = all(
        v in ("effective", "not_effective", "effective_after_named_Weyl_move")
        for v in verdicts
    )

    # Reconstruction check for each effective decomposition
    delta = d6_affine_simple_roots_kny()
    recon_ok = True
    for i in range(7):
        rec = classification[i]
        if rec["verdict"] == "effective":
            ok = verify_effective_decomposition_lattice_consistent(
                delta[i], rec["decomposition"]  # type: ignore[arg-type]
            )
            if not ok:
                recon_ok = False
                break
        elif rec["verdict"] == "effective_after_named_Weyl_move":
            ok = verify_effective_decomposition_lattice_consistent(
                rec["reflected_class_vector_pic"],  # type: ignore[arg-type]
                rec["post_reflection_decomposition"],  # type: ignore[arg-type]
            )
            if not ok:
                recon_ok = False
                break
    flags["every_effective_decomposition_reconstructs"] = recon_ok

    return {
        "flags": flags,
        "irreducible_basis_determinant": int(IRREDUCIBLE_BASIS_DETERMINANT),
        "classification": classification,
    }


def _main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Effectivity classification of the KNY D_6^{(1)} simple roots."
    )
    parser.add_argument(
        "--classify",
        action="store_true",
        help="Run the full classification and emit JSON to stdout.",
    )
    args = parser.parse_args(list(argv))

    if args.classify:
        report = verify_report()
        print(json.dumps(report, indent=2, sort_keys=True))
        if not all(report["flags"].values()):  # type: ignore[arg-type]
            return 1
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
