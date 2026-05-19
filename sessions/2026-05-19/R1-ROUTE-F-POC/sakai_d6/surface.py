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


def verify_report() -> dict:
    """Bundle the verification outcomes into a JSON-serializable dict."""
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
    }


def _main() -> int:
    parser = argparse.ArgumentParser(description="Sakai surface D_6^{(1)} POC verifier")
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
        )
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
