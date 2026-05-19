"""D_6^{(1)} affine root system, implemented over Z^8.

Scope of this module
--------------------
This module implements the affine root system of type D_6^{(1)} as
needed by the Sakai surface route-F proof-of-concept. It does not
claim anything about the Painleve III(D_6) transcendent or about
V_quad. It only provides:

  * the 7 simple roots alpha_0, ..., alpha_6 as integer vectors in Z^8
  * the affine null root delta as an integer vector in Z^8
  * the 7x7 generalized Cartan matrix of D_6^{(1)}
  * a predicate ``is_root(v)`` that decides membership in the finite
    real-root set { +/- e_i +/- e_j : 1 <= i < j <= 6 } of D_6

Conventions
-----------
We embed roots in Z^8 with the layout

    (x_1, x_2, x_3, x_4, x_5, x_6, m, p)

where x_1, ..., x_6 are coordinates in the standard epsilon-basis
of the ambient space of finite D_6, m is the coefficient of the
affine null root delta, and p is an unused padding slot reserved
for the level grading. The padding slot is always 0 for the simple
roots and for delta, but is carried to make Z^8 explicit (the brief
specifies Z^8 rather than Z^7).

The finite simple roots are the standard ones for D_6:

    alpha_1 = e_1 - e_2
    alpha_2 = e_2 - e_3
    alpha_3 = e_3 - e_4
    alpha_4 = e_4 - e_5
    alpha_5 = e_5 - e_6
    alpha_6 = e_5 + e_6

The highest finite root is

    theta = e_1 + e_2

and the affine simple root is

    alpha_0 = delta - theta = delta - e_1 - e_2.

The Cartan matrix below is the standard A(D_6^{(1)}) of Kac,
"Infinite-Dimensional Lie Algebras," Table Aff 1.
"""

from __future__ import annotations

import numpy as np

# ---------------------------------------------------------------------------
# Simple roots and null root
# ---------------------------------------------------------------------------

# Index convention: alpha_0 is the affine root; alpha_1..alpha_6 are the
# finite D_6 simple roots in the standard ordering above.
#
# Each row of SIMPLE_ROOTS has length 8: six epsilon-coordinates, then the
# delta coefficient, then the padding slot.

SIMPLE_ROOTS = np.array(
    [
        # alpha_0 = delta - e_1 - e_2
        [-1, -1, 0, 0, 0, 0, 1, 0],
        # alpha_1 = e_1 - e_2
        [1, -1, 0, 0, 0, 0, 0, 0],
        # alpha_2 = e_2 - e_3
        [0, 1, -1, 0, 0, 0, 0, 0],
        # alpha_3 = e_3 - e_4
        [0, 0, 1, -1, 0, 0, 0, 0],
        # alpha_4 = e_4 - e_5
        [0, 0, 0, 1, -1, 0, 0, 0],
        # alpha_5 = e_5 - e_6
        [0, 0, 0, 0, 1, -1, 0, 0],
        # alpha_6 = e_5 + e_6
        [0, 0, 0, 0, 1, 1, 0, 0],
    ],
    dtype=np.int64,
)

# Affine null root delta: lives entirely in the m-slot.
DELTA = np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=np.int64)


# ---------------------------------------------------------------------------
# Cartan matrix of D_6^{(1)}
# ---------------------------------------------------------------------------
#
# Standard generalized Cartan matrix for D_6^{(1)} (Kac, Table Aff 1).
# Rows / columns are indexed in the order [alpha_0, alpha_1, ..., alpha_6].
#
# Dynkin diagram of D_6^{(1)} (Kac Aff 1, n=6):
#
#       alpha_0           alpha_6
#           \            /
#   alpha_1 - alpha_2 - alpha_3 - alpha_4 - alpha_5
#
# i.e. alpha_0 attaches to alpha_2, alpha_6 attaches to alpha_4 (the
# fork at one end mirrors the fork at the other), and alpha_1..alpha_5
# form an A_5 string. With our chosen embedding, this is encoded by
# the matrix below; we verify a_{ij} = 2 (alpha_i, alpha_j) / (alpha_j,
# alpha_j) against the bilinear form in the unit tests.

CARTAN_MATRIX = np.array(
    [
        # a_0 a_1 a_2 a_3 a_4 a_5 a_6
        [2, 0, -1, 0, 0, 0, 0],   # alpha_0 attaches to alpha_2
        [0, 2, -1, 0, 0, 0, 0],   # alpha_1 attaches to alpha_2
        [-1, -1, 2, -1, 0, 0, 0], # alpha_2 trivalent: 0,1,3
        [0, 0, -1, 2, -1, 0, 0],  # alpha_3 attaches to 2,4
        [0, 0, 0, -1, 2, -1, -1], # alpha_4 trivalent: 3,5,6
        [0, 0, 0, 0, -1, 2, 0],   # alpha_5 attaches to alpha_4
        [0, 0, 0, 0, -1, 0, 2],   # alpha_6 attaches to alpha_4
    ],
    dtype=np.int64,
)


# ---------------------------------------------------------------------------
# Bilinear form
# ---------------------------------------------------------------------------
#
# We use the symmetric Z-bilinear form on Z^8 given by
#
#     (u, v) = sum_{i=1}^{6} u_i v_i + u_7 v_8 + u_8 v_7
#
# i.e. standard Euclidean on the first six (epsilon) coordinates, and
# a hyperbolic pairing between the delta-slot (index 7) and the level
# slot (index 8). Because the padding slot is 0 for every simple root
# and for delta, the hyperbolic term contributes nothing here, and we
# recover the standard affine extension where (delta, alpha_i) = 0
# for all simple roots and (delta, delta) = 0.

_GRAM = np.zeros((8, 8), dtype=np.int64)
for _i in range(6):
    _GRAM[_i, _i] = 1
_GRAM[6, 7] = 1
_GRAM[7, 6] = 1


def bilinear(u: np.ndarray, v: np.ndarray) -> int:
    """Symmetric Z-bilinear form on Z^8 used in this module."""
    u = np.asarray(u, dtype=np.int64)
    v = np.asarray(v, dtype=np.int64)
    return int(u @ _GRAM @ v)


# ---------------------------------------------------------------------------
# is_root: membership test for the finite D_6 real-root set
# ---------------------------------------------------------------------------
#
# The brief asks for a predicate that decides membership "on the finite
# set." We interpret this as the set of finite real roots of D_6, namely
#
#     { +/- e_i +/- e_j : 1 <= i < j <= 6 }
#
# embedded in Z^8 with delta-coefficient 0 and padding 0. There are
# 4 * C(6, 2) = 60 such vectors.


def is_root(v) -> bool:
    """Return True iff v is a finite D_6 real root in Z^8.

    The finite real roots of D_6 are the vectors of the form
    +/- e_i +/- e_j for 1 <= i < j <= 6, with delta-coefficient 0 and
    padding 0.
    """
    v = np.asarray(v, dtype=np.int64)
    if v.shape != (8,):
        return False
    if v[6] != 0 or v[7] != 0:
        return False
    finite = v[:6]
    # Exactly two non-zero entries, each +/-1
    nonzero_idx = np.flatnonzero(finite)
    if nonzero_idx.size != 2:
        return False
    return bool(np.all(np.abs(finite[nonzero_idx]) == 1))


def finite_real_roots() -> list[np.ndarray]:
    """Enumerate the 60 finite real roots of D_6 as Z^8 vectors."""
    roots: list[np.ndarray] = []
    for i in range(6):
        for j in range(i + 1, 6):
            for si in (1, -1):
                for sj in (1, -1):
                    v = np.zeros(8, dtype=np.int64)
                    v[i] = si
                    v[j] = sj
                    roots.append(v)
    return roots


# ---------------------------------------------------------------------------
# Self-consistency: derived Cartan matrix from the bilinear form
# ---------------------------------------------------------------------------


def derived_cartan_matrix() -> np.ndarray:
    """Compute a_{ij} = 2 (alpha_i, alpha_j) / (alpha_j, alpha_j).

    Every simple root in D_6^{(1)} has squared length 2, so the
    division is exact and the result is an integer matrix.
    """
    n = SIMPLE_ROOTS.shape[0]
    out = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            num = 2 * bilinear(SIMPLE_ROOTS[i], SIMPLE_ROOTS[j])
            den = bilinear(SIMPLE_ROOTS[j], SIMPLE_ROOTS[j])
            if den == 0:
                raise ValueError(
                    "simple root with squared length 0; this should not happen"
                )
            if num % den != 0:
                raise ValueError(
                    "non-integer Cartan entry; bilinear form inconsistent"
                )
            out[i, j] = num // den
    return out
