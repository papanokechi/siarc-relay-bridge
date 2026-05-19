"""Sakai surface (blow-up of P^1 x P^1 at 8 points), POC scaffolding.

Scope of this module
--------------------
This module implements just enough of the Picard-lattice machinery
for a Sakai surface X = Bl_{8 pts}(P^1 x P^1) to support a
proof-of-concept check that the D_6^{(1)} affine root lattice embeds
into the orthogonal complement of the anti-canonical class in
Pic(X). It does NOT:

  * construct the V_quad parameter correspondence
  * derive the Stokes constant
  * make any claim about closing R1

The base points on P^1 x P^1 are exposed as configurable parameters
(``BASE_POINTS``) so that downstream sessions can iterate on
specific configurations. In this POC the base points are not used
by the lattice check itself: the check is combinatorial on Pic(X).

Pic(X) basis and intersection form
----------------------------------
We use the basis (H_1, H_2, E_1, ..., E_8) of Pic(X), 10 generators
total. Intersections for 8 points in general position:

    H_1 . H_1 = 0,   H_2 . H_2 = 0,   H_1 . H_2 = 1
    E_i . E_j = -delta_{ij},          H_k . E_i = 0

The anti-canonical class is

    -K_X = 2 H_1 + 2 H_2 - sum_{i=1..8} E_i.

The candidate D_6^{(1)} simple roots used here

    alpha_0 = E_1 - E_3
    alpha_1 = E_2 - E_4
    alpha_2 = H_1 - E_1 - E_2
    alpha_3 = H_2 - H_1
    alpha_4 = H_1 - E_5 - E_6
    alpha_5 = E_5 - E_7
    alpha_6 = E_6 - E_8

are seven (-2)-classes orthogonal to K_X whose pairwise intersection
matrix reproduces the D_6^{(1)} symmetric Cartan form. We verify
this explicitly. We do not claim the base points have any
particular geometric configuration; the seven classes above live in
Pic(X) by combinatorial fiat. The base points appear only as
parameters for downstream consumers.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

import numpy as np


# ---------------------------------------------------------------------------
# Pic(X) basis and intersection form
# ---------------------------------------------------------------------------
#
# Basis order: (H_1, H_2, E_1, E_2, E_3, E_4, E_5, E_6, E_7, E_8).

DIM_PIC = 10


def intersection_form() -> np.ndarray:
    """Return the 10x10 integer intersection matrix on Pic(X)."""
    g = np.zeros((DIM_PIC, DIM_PIC), dtype=np.int64)
    # H_1 . H_2 = H_2 . H_1 = 1
    g[0, 1] = 1
    g[1, 0] = 1
    # E_i . E_i = -1
    for i in range(2, DIM_PIC):
        g[i, i] = -1
    return g


GRAM_PIC = intersection_form()


def intersect(u: Sequence[int], v: Sequence[int]) -> int:
    """Intersection pairing on Pic(X) as an integer."""
    u_arr = np.asarray(u, dtype=np.int64)
    v_arr = np.asarray(v, dtype=np.int64)
    return int(u_arr @ GRAM_PIC @ v_arr)


# ---------------------------------------------------------------------------
# Distinguished classes
# ---------------------------------------------------------------------------


def H(k: int) -> np.ndarray:
    """H_k as a Pic(X) vector, k in {1, 2}."""
    if k not in (1, 2):
        raise ValueError("k must be 1 or 2")
    v = np.zeros(DIM_PIC, dtype=np.int64)
    v[k - 1] = 1
    return v


def E(i: int) -> np.ndarray:
    """E_i as a Pic(X) vector, i in {1, ..., 8}."""
    if not (1 <= i <= 8):
        raise ValueError("i must be in 1..8")
    v = np.zeros(DIM_PIC, dtype=np.int64)
    v[1 + i] = 1
    return v


def anti_canonical() -> np.ndarray:
    """The anti-canonical class -K_X = 2H_1 + 2H_2 - sum E_i."""
    v = 2 * H(1) + 2 * H(2)
    for i in range(1, 9):
        v = v - E(i)
    return v


# ---------------------------------------------------------------------------
# D_6^{(1)} simple-root embedding in Pic(X)
# ---------------------------------------------------------------------------
#
# See the module docstring for the choices. Ordered as
# [alpha_0, alpha_1, alpha_2, alpha_3, alpha_4, alpha_5, alpha_6].


def d6_affine_simple_roots() -> np.ndarray:
    """Return the 7x10 integer matrix of D_6^{(1)} simple roots in Pic(X)."""
    rows = [
        E(1) - E(3),                 # alpha_0
        E(2) - E(4),                 # alpha_1
        H(1) - E(1) - E(2),          # alpha_2
        H(2) - H(1),                 # alpha_3
        H(1) - E(5) - E(6),          # alpha_4
        E(5) - E(7),                 # alpha_5
        E(6) - E(8),                 # alpha_6
    ]
    return np.array(rows, dtype=np.int64)


def expected_d6_affine_symmetric_cartan() -> np.ndarray:
    """The expected symmetric matrix B_{ij} = (alpha_i, alpha_j) for D_6^{(1)}.

    All simple roots have self-intersection -2 in Pic(X) (equivalently
    (alpha_i, alpha_i) = -2 here, with the sign convention that the
    Cartan matrix has +2 on the diagonal). Off-diagonal entries are
    +1 on Dynkin-adjacent pairs and 0 otherwise.
    """
    b = np.zeros((7, 7), dtype=np.int64)
    for i in range(7):
        b[i, i] = -2
    # Adjacencies (i, j) with i < j in D_6^{(1)}
    adj = [(0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (4, 6)]
    for i, j in adj:
        b[i, j] = 1
        b[j, i] = 1
    return b


# ---------------------------------------------------------------------------
# Base points on P^1 x P^1 (configurable; not used by the lattice check)
# ---------------------------------------------------------------------------
#
# Each base point is a pair ((s : t), (u : v)) in P^1 x P^1, recorded
# here as affine ((s/t, u/v)) when finite. Any choice of 8 distinct
# points works for the rank-and-form computation; geometric
# configurations matching the Sakai PIII(D_6) layout are out of
# scope for this POC.

BASE_POINTS = [
    (0.0, 0.0),
    (1.0, 0.0),
    (0.0, 1.0),
    (1.0, 1.0),
    (2.0, 0.0),
    (0.0, 2.0),
    (2.0, 2.0),
    (3.0, 3.0),
]


# ---------------------------------------------------------------------------
# Verification entry points
# ---------------------------------------------------------------------------


def verify_intersection_form_unimodular() -> bool:
    """Check that the intersection form on Pic(X) is unimodular."""
    return int(round(np.linalg.det(GRAM_PIC.astype(np.float64)))) in (1, -1)


def verify_simple_roots_orthogonal_to_canonical() -> bool:
    """Check (alpha_i, -K_X) = 0 for every simple root."""
    roots = d6_affine_simple_roots()
    k_anti = anti_canonical()
    return all(intersect(r, k_anti) == 0 for r in roots)


def compute_simple_root_gram() -> np.ndarray:
    """Return the 7x7 matrix B_{ij} = (alpha_i, alpha_j) in Pic(X)."""
    roots = d6_affine_simple_roots()
    n = roots.shape[0]
    out = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            out[i, j] = intersect(roots[i], roots[j])
    return out


def surface_type() -> str:
    """Return ``"D6_affine"`` iff the chosen 7 simple roots in Pic(X)

    (a) are all orthogonal to the anti-canonical class, and
    (b) have pairwise intersection matrix equal to the expected
        D_6^{(1)} symmetric Cartan form.

    Otherwise return ``"unknown"``.
    """
    if not verify_simple_roots_orthogonal_to_canonical():
        return "unknown"
    if not np.array_equal(compute_simple_root_gram(), expected_d6_affine_symmetric_cartan()):
        return "unknown"
    return "D6_affine"


# ---------------------------------------------------------------------------
# Sakai non-generic configuration for PIII(D_6) -- cycle 1
# ---------------------------------------------------------------------------
#
# Primary source: Kajiwara-Noumi-Yamada, "Geometric Aspects of Painleve
# Equations", J. Phys. A 50 (2017) 073001 (arXiv:1509.08186v8).
#
# Important finding -- intersection form is CONFIGURATION-INDEPENDENT:
#
#   Per KNY 2017 sec.3.3 eq (3.26), the symmetric bilinear form on the
#   Picard lattice Lambda = ZH_1 (+) ZH_2 (+) ZE_1 (+) ... (+) ZE_8 is
#   defined by H_1.H_2=1, H_1.H_1=H_2.H_2=0, E_i.E_j=-delta_ij,
#   H_k.E_j=0, and the paper states explicitly:
#
#       "For any surface X obtained from P^1 x P^1 by eight blowing-ups,
#        Lambda is identified with the Picard lattice Pic X"
#
#   i.e. the Pic intersection form does not depend on whether the eight
#   blow-ups are at points in general position, at infinitely-near
#   towers, or at any other Sakai configuration. The non-genericity of
#   the PIII(D_6) configuration shows up in which CLASSES are the
#   components of the anti-canonical divisor (the surface-type simple
#   roots), not in the bilinear form.
#
# Consequently, `intersection_form_sakai_nongen()` returns the same
# 10x10 Gram matrix as the generic `intersection_form()`. The function
# is kept distinct (a) to make the convention-alignment explicit and
# (b) so downstream code can refer to the Sakai-form path without
# implying a numerical difference.
#
# PIII(D_6) eight-point configuration per KNY 2017 sec.8.2.19 eq (8.98)
# in (q, p) coordinates is:
#
#     P_12: (1/eps, 1 - a_1*eps) for eps -> 0, multiplicity 2
#           (a pair of infinitely near points at q = infinity)
#     P_34: (1/eps, -a_2*eps) for eps -> 0, multiplicity 2
#           (a second pair at q = infinity)
#     P_5678: (eps, -t/eps^2 + (1 - a_1 - a_2)/eps) for eps -> 0,
#           multiplicity 4 (a 4-fold tower at p = infinity)
#
# The seven D_6^{(1)} simple roots in Pic(X) per KNY 2017 sec.8.2.19
# eq (8.101) are:
#
#     delta_0 = E_1 - E_2          (left-fork pendant)
#     delta_1 = E_3 - E_4          (left-fork pendant)
#     delta_2 = H_1 - E_1 - E_3    (left-fork center)
#     delta_3 = H_2 - E_5 - E_6    (chain middle)
#     delta_4 = E_6 - E_7          (right-fork center)
#     delta_5 = E_5 - E_6          (right-fork pendant)
#     delta_6 = E_7 - E_8          (right-fork pendant)
#
# Dynkin adjacencies (KNY 2017 picture in eq (8.100)):
#
#     delta_0       delta_5
#         \        /
#       delta_2 - delta_3 - delta_4
#         /        \
#     delta_1       delta_6
#
# In particular delta_5 and delta_6 are BOTH attached to delta_4
# (degree-3 right-fork node), with delta_4 attached to delta_3, mirror
# image of the left fork. The agent verified by direct computation
# that delta_3.delta_5 = 0 (not delta_5 attached to delta_3).


def intersection_form_sakai_nongen() -> np.ndarray:
    """Return the 10x10 integer intersection matrix on Pic(X) under the
    Sakai PIII(D_6) non-generic configuration.

    Per Kajiwara-Noumi-Yamada (KNY) 2017 sec.3.3 eq (3.26) the Picard
    intersection form does NOT depend on the configuration of the eight
    blow-up points (generic vs infinitely-near vs Sakai-type). This
    function therefore returns the same 10x10 matrix as
    `intersection_form()`. It exists as a distinct entry point so
    that callers can document convention-alignment with the Sakai
    primary source, and so that any future change of convention is
    localized to a single function.
    """
    return intersection_form()


GRAM_PIC_SAKAI_NONGEN = intersection_form_sakai_nongen()


def signature_sakai_nongen(tol: float = 1e-9) -> tuple[int, int, int]:
    """Return (#positive, #zero, #negative) eigenvalues of the Sakai form.

    Eigenvalues are computed in float64 and compared against `tol`.
    Per KNY 2017 sec.3.3 (and direct inspection: U (+) (-I_8)), the
    Sakai form has signature (1, 9) -- one positive and nine negative
    eigenvalues, no zero eigenvalues.
    """
    eigvals = np.linalg.eigvalsh(GRAM_PIC_SAKAI_NONGEN.astype(np.float64))
    pos = int(np.sum(eigvals > tol))
    neg = int(np.sum(eigvals < -tol))
    zer = int(np.sum(np.abs(eigvals) <= tol))
    return (pos, zer, neg)


def d6_affine_simple_roots_kny() -> np.ndarray:
    """Return the 7x10 integer matrix of D_6^{(1)} simple roots
    delta_0, ..., delta_6 in Pic(X) per KNY 2017 sec.8.2.19 eq (8.101)
    for the PIII(D_6) surface type."""
    rows = [
        E(1) - E(2),                 # delta_0
        E(3) - E(4),                 # delta_1
        H(1) - E(1) - E(3),          # delta_2
        H(2) - E(5) - E(6),          # delta_3
        E(6) - E(7),                 # delta_4
        E(5) - E(6),                 # delta_5
        E(7) - E(8),                 # delta_6
    ]
    return np.array(rows, dtype=np.int64)


def expected_d6_affine_symmetric_cartan_kny() -> np.ndarray:
    """The expected symmetric matrix B_{ij} = (delta_i, delta_j) for
    D_6^{(1)} in the KNY 2017 sec.8.2.19 ordering.

    Diagonal -2 (self-intersection). Off-diagonals follow the Dynkin
    diagram drawn in KNY eq (8.100):

        delta_0 - delta_2 - delta_3 - delta_4 - delta_5
        delta_1 - delta_2                       delta_6 - delta_4
    """
    b = np.zeros((7, 7), dtype=np.int64)
    for i in range(7):
        b[i, i] = -2
    # Adjacencies (i, j) with i < j in KNY's labelling (8.101)
    adj_kny = [
        (0, 2),  # delta_0 -- delta_2
        (1, 2),  # delta_1 -- delta_2
        (2, 3),  # delta_2 -- delta_3
        (3, 4),  # delta_3 -- delta_4
        (4, 5),  # delta_4 -- delta_5
        (4, 6),  # delta_4 -- delta_6
    ]
    for i, j in adj_kny:
        b[i, j] = 1
        b[j, i] = 1
    return b


def compute_kny_root_gram() -> np.ndarray:
    """Return the 7x7 Gram matrix of the KNY simple roots under the
    Sakai non-generic form on Pic(X)."""
    roots = d6_affine_simple_roots_kny()
    n = roots.shape[0]
    out = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            u = roots[i].astype(np.int64)
            v = roots[j].astype(np.int64)
            out[i, j] = int(u @ GRAM_PIC_SAKAI_NONGEN @ v)
    return out


def verify_kny_embedding_orthogonal_to_canonical() -> bool:
    """Check (delta_i, -K_X) = 0 for every KNY simple root."""
    roots = d6_affine_simple_roots_kny()
    k_anti = anti_canonical()
    for r in roots:
        u = r.astype(np.int64)
        if int(u @ GRAM_PIC_SAKAI_NONGEN @ k_anti) != 0:
            return False
    return True


def verify_kny_embedding_self_intersection_minus_two() -> bool:
    """Check (delta_i, delta_i) = -2 for every KNY simple root."""
    gram = compute_kny_root_gram()
    return all(int(gram[i, i]) == -2 for i in range(gram.shape[0]))


def compute_poc_root_gram_under_sakai_form() -> np.ndarray:
    """Return the 7x7 Gram matrix of the predecessor (POC) simple roots
    under the Sakai non-generic form on Pic(X).

    Used to verify whether the predecessor cycle's alpha_0,...,alpha_6
    embedding satisfies the abstract D_6^{(1)} Cartan condition under
    the Sakai form (it does; the Pic form is unchanged from generic).
    """
    roots = d6_affine_simple_roots()
    n = roots.shape[0]
    out = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            u = roots[i].astype(np.int64)
            v = roots[j].astype(np.int64)
            out[i, j] = int(u @ GRAM_PIC_SAKAI_NONGEN @ v)
    return out


def verdict_sakai_nongen() -> str:
    """Return the cycle-1 verdict as one of:
      - SAKAI_FORM_PRESERVES_POC_EMBEDDING
      - SAKAI_FORM_REQUIRES_NEW_EMBEDDING
      - SAKAI_FORM_ADMITS_NO_INTEGER_EMBEDDING_AT_THIS_RANK

    Decision rule:
      - If the KNY embedding satisfies the D_6^{(1)} Cartan and is
        equal (as a set of integer vectors) to the POC embedding:
        PRESERVES.
      - Else if the KNY embedding satisfies the D_6^{(1)} Cartan but
        differs from the POC embedding: REQUIRES_NEW.
      - Else: NO_EMBEDDING.
    """
    poc = d6_affine_simple_roots()
    kny = d6_affine_simple_roots_kny()
    kny_ok = (
        verify_kny_embedding_self_intersection_minus_two()
        and verify_kny_embedding_orthogonal_to_canonical()
        and np.array_equal(compute_kny_root_gram(), expected_d6_affine_symmetric_cartan_kny())
    )
    if not kny_ok:
        return "SAKAI_FORM_ADMITS_NO_INTEGER_EMBEDDING_AT_THIS_RANK"
    # Compare embeddings as unordered sets of integer vectors
    poc_set = {tuple(int(x) for x in v) for v in poc}
    kny_set = {tuple(int(x) for x in v) for v in kny}
    if poc_set == kny_set:
        return "SAKAI_FORM_PRESERVES_POC_EMBEDDING"
    return "SAKAI_FORM_REQUIRES_NEW_EMBEDDING"


def verify_report() -> dict:
    """Bundle the verification outcomes into a JSON-serializable dict.

    Extended in cycle 1 (R1-ROUTE-F-SAKAI-NONGEN) to include the
    Sakai-non-generic checks and the cycle-1 verdict.
    """
    sig = signature_sakai_nongen()
    return {
        "pic_rank": int(DIM_PIC),
        "intersection_form_unimodular": bool(verify_intersection_form_unimodular()),
        "simple_roots_orthogonal_to_canonical": bool(verify_simple_roots_orthogonal_to_canonical()),
        "simple_root_gram_matches_expected": bool(
            np.array_equal(
                compute_simple_root_gram(),
                expected_d6_affine_symmetric_cartan(),
            )
        ),
        "surface_type": surface_type(),
        # Cycle-1 (R1-ROUTE-F-SAKAI-NONGEN) fields:
        "sakai_form_equals_generic_form": bool(
            np.array_equal(GRAM_PIC_SAKAI_NONGEN, GRAM_PIC)
        ),
        "sakai_form_unimodular": int(
            round(np.linalg.det(GRAM_PIC_SAKAI_NONGEN.astype(np.float64)))
        ) in (1, -1),
        "sakai_form_signature_positive": sig[0],
        "sakai_form_signature_zero": sig[1],
        "sakai_form_signature_negative": sig[2],
        "kny_embedding_self_intersection_minus_two": bool(
            verify_kny_embedding_self_intersection_minus_two()
        ),
        "kny_embedding_orthogonal_to_canonical": bool(
            verify_kny_embedding_orthogonal_to_canonical()
        ),
        "kny_embedding_gram_matches_expected": bool(
            np.array_equal(
                compute_kny_root_gram(),
                expected_d6_affine_symmetric_cartan_kny(),
            )
        ),
        "cycle1_verdict": verdict_sakai_nongen(),
    }


def _main() -> int:
    parser = argparse.ArgumentParser(description="Sakai surface D_6^{(1)} verifier")
    parser.add_argument(
        "--verify-lattice",
        action="store_true",
        help="Print the verification report as JSON and exit 0 iff all checks pass.",
    )
    args = parser.parse_args()

    report = verify_report()
    print(json.dumps(report, indent=2, sort_keys=True))

    if args.verify_lattice:
        ok = (
            report["intersection_form_unimodular"]
            and report["simple_roots_orthogonal_to_canonical"]
            and report["simple_root_gram_matches_expected"]
            and report["surface_type"] == "D6_affine"
            and report["sakai_form_equals_generic_form"]
            and report["sakai_form_unimodular"]
            and report["sakai_form_signature_positive"] == 1
            and report["sakai_form_signature_zero"] == 0
            and report["sakai_form_signature_negative"] == 9
            and report["kny_embedding_self_intersection_minus_two"]
            and report["kny_embedding_orthogonal_to_canonical"]
            and report["kny_embedding_gram_matches_expected"]
            and report["cycle1_verdict"] in (
                "SAKAI_FORM_PRESERVES_POC_EMBEDDING",
                "SAKAI_FORM_REQUIRES_NEW_EMBEDDING",
                "SAKAI_FORM_ADMITS_NO_INTEGER_EMBEDDING_AT_THIS_RANK",
            )
        )
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
