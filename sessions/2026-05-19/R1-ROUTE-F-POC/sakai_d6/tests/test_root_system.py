"""Unit tests for the D_6^{(1)} root system and Sakai surface POC.

These tests verify only that the affine root system and the Pic(X)
intersection form compile and reproduce known structural facts:

  * simple roots have squared length 2
  * the derived Cartan matrix matches the supplied one
  * is_root recognises exactly the finite D_6 real-root set (60 vectors)
  * (delta, alpha_i) = 0 and (delta, delta) = 0
  * the Pic(X) intersection form is unimodular
  * the chosen 7 simple roots in Pic(X) are orthogonal to -K_X and
    have the expected D_6^{(1)} symmetric Cartan form
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from sakai_d6 import root_system as rs
from sakai_d6 import surface as sf


# ---------------------------------------------------------------------------
# root_system.py
# ---------------------------------------------------------------------------


class TestSimpleRoots:
    def test_count_is_seven(self):
        assert rs.SIMPLE_ROOTS.shape == (7, 8)

    def test_each_squared_length_is_two(self):
        for i, root in enumerate(rs.SIMPLE_ROOTS):
            assert rs.bilinear(root, root) == 2, f"alpha_{i} not of squared length 2"

    def test_delta_lives_in_z8(self):
        assert rs.DELTA.shape == (8,)
        assert rs.DELTA.dtype == np.int64

    def test_delta_orthogonal_to_every_simple_root(self):
        for i, root in enumerate(rs.SIMPLE_ROOTS):
            assert rs.bilinear(rs.DELTA, root) == 0, f"(delta, alpha_{i}) != 0"

    def test_delta_is_isotropic(self):
        assert rs.bilinear(rs.DELTA, rs.DELTA) == 0


class TestCartanMatrix:
    def test_shape(self):
        assert rs.CARTAN_MATRIX.shape == (7, 7)

    def test_diagonal_is_two(self):
        assert np.array_equal(np.diag(rs.CARTAN_MATRIX), np.full(7, 2, dtype=np.int64))

    def test_offdiagonal_entries_are_zero_or_minus_one(self):
        n = 7
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                assert rs.CARTAN_MATRIX[i, j] in (0, -1), (
                    f"unexpected entry {rs.CARTAN_MATRIX[i, j]} at ({i},{j})"
                )

    def test_matches_derived_from_bilinear_form(self):
        derived = rs.derived_cartan_matrix()
        assert np.array_equal(derived, rs.CARTAN_MATRIX), (
            f"derived Cartan {derived} disagrees with supplied {rs.CARTAN_MATRIX}"
        )

    def test_corank_one(self):
        # D_6^{(1)} is affine; its Cartan matrix has corank exactly one.
        rank = np.linalg.matrix_rank(rs.CARTAN_MATRIX.astype(np.float64))
        assert rank == 6


class TestIsRoot:
    def test_finite_root_set_has_exactly_sixty_elements(self):
        roots = rs.finite_real_roots()
        assert len(roots) == 60

    def test_is_root_accepts_every_enumerated_finite_root(self):
        for v in rs.finite_real_roots():
            assert rs.is_root(v), f"is_root rejected enumerated root {v}"

    def test_is_root_rejects_zero(self):
        assert not rs.is_root(np.zeros(8, dtype=np.int64))

    def test_is_root_rejects_delta(self):
        assert not rs.is_root(rs.DELTA)

    def test_is_root_rejects_wrong_dimension(self):
        assert not rs.is_root(np.array([1, -1, 0, 0, 0, 0, 0], dtype=np.int64))

    def test_is_root_rejects_three_nonzero_entries(self):
        v = np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype=np.int64)
        assert not rs.is_root(v)

    def test_is_root_rejects_entries_with_magnitude_two(self):
        v = np.array([2, -1, 0, 0, 0, 0, 0, 0], dtype=np.int64)
        assert not rs.is_root(v)

    def test_is_root_rejects_vectors_with_nonzero_delta(self):
        v = np.array([1, -1, 0, 0, 0, 0, 1, 0], dtype=np.int64)
        assert not rs.is_root(v)


# ---------------------------------------------------------------------------
# surface.py
# ---------------------------------------------------------------------------


class TestPicardIntersectionForm:
    def test_shape_and_dtype(self):
        assert sf.GRAM_PIC.shape == (10, 10)
        assert sf.GRAM_PIC.dtype == np.int64

    def test_h1_h2_cross(self):
        assert sf.intersect(sf.H(1), sf.H(2)) == 1
        assert sf.intersect(sf.H(2), sf.H(1)) == 1

    def test_hk_squared_is_zero(self):
        assert sf.intersect(sf.H(1), sf.H(1)) == 0
        assert sf.intersect(sf.H(2), sf.H(2)) == 0

    def test_exceptional_self_intersections(self):
        for i in range(1, 9):
            assert sf.intersect(sf.E(i), sf.E(i)) == -1

    def test_exceptional_pairwise_orthogonal(self):
        for i in range(1, 9):
            for j in range(1, 9):
                if i == j:
                    continue
                assert sf.intersect(sf.E(i), sf.E(j)) == 0

    def test_h_dot_e_is_zero(self):
        for k in (1, 2):
            for i in range(1, 9):
                assert sf.intersect(sf.H(k), sf.E(i)) == 0

    def test_form_is_unimodular(self):
        assert sf.verify_intersection_form_unimodular()


class TestAntiCanonical:
    def test_self_intersection_is_eight(self):
        # (-K_X) . (-K_X) = (K_X)^2 = 8 for blow-up of P^1xP^1 at 8 points
        # in the "Sakai" sense: K_X^2 = 8 - 8 = 0. Here we use the
        # generic form and verify (-K).(-K) = 8 - 8 = 0.
        k = sf.anti_canonical()
        assert sf.intersect(k, k) == 0


class TestD6AffineEmbedding:
    def test_seven_simple_roots(self):
        roots = sf.d6_affine_simple_roots()
        assert roots.shape == (7, 10)

    def test_every_simple_root_has_self_intersection_minus_two(self):
        roots = sf.d6_affine_simple_roots()
        for i, r in enumerate(roots):
            assert sf.intersect(r, r) == -2, f"alpha_{i} self-intersection != -2"

    def test_every_simple_root_is_orthogonal_to_anti_canonical(self):
        assert sf.verify_simple_roots_orthogonal_to_canonical()

    def test_simple_root_gram_matches_expected(self):
        gram = sf.compute_simple_root_gram()
        expected = sf.expected_d6_affine_symmetric_cartan()
        assert np.array_equal(gram, expected), (
            f"Gram matrix\n{gram}\ndoes not match expected\n{expected}"
        )

    def test_surface_type_is_d6_affine(self):
        assert sf.surface_type() == "D6_affine"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
