"""Cycle 2 (R1-ROUTE-F-K-PERP-BASIS) tests.

Goal: verify the rank-9 K_X^perp basis construction and prove the
KNY canonical embedding L_delta = Z<delta_0,...,delta_6> is
saturated inside K_X^perp.

Primary source for inputs:
  - KNY 2017 sec.3.3 eq (3.26): the Pic intersection form
    (configuration-independent, validated in cycle 1).
  - KNY 2017 sec.8.2.19 eq (8.101): the canonical D_6^{(1)}
    simple roots delta_0..delta_6.

Predecessor: R1-ROUTE-F-SAKAI-NONGEN (bridge commit 53efe94).
Pre-registered claim: claims/claim-r1-k-perp-basis-001.json.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from sakai_d6.saturation import (
    K_PERP_BASIS,
    RANK_K_PERP,
    RANK_KNY,
    _functional_K_perp,
    elementary_divisors,
    k_perp_basis,
    kny_in_k_perp_coords,
    saturation_closure_generators,
    saturation_index,
    smith_normal_form_of_kny,
    verdict_saturation,
    verify_every_kny_delta_orthogonal_to_canonical,
    verify_k_perp_basis_orthogonal_to_canonical,
    verify_k_perp_basis_rank_is_9,
    verify_reconstruction,
    verify_snf_has_exactly_seven_nonzero_elementary_divisors,
)
from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    anti_canonical,
    d6_affine_simple_roots_kny,
    intersect,
)


# ---------------------------------------------------------------------------
# K_X^perp basis structure
# ---------------------------------------------------------------------------


class TestKPerpBasis:
    def test_returns_9x10_integer_matrix(self):
        b = k_perp_basis()
        assert b.shape == (RANK_K_PERP, DIM_PIC)
        assert b.dtype.kind == "i"

    def test_basis_has_full_row_rank_9_over_z(self):
        # Sufficient over Z: the 9x9 minor on the free coordinates
        # (H_1, H_2, E_2..E_8) is the identity, so det = +-1.
        b = K_PERP_BASIS
        free_cols = [0, 1, 3, 4, 5, 6, 7, 8, 9]
        sub = b[:, free_cols]
        det = int(round(np.linalg.det(sub.astype(np.float64))))
        assert det in (1, -1)

    def test_basis_has_full_row_rank_9_over_q(self):
        assert verify_k_perp_basis_rank_is_9()

    def test_every_basis_vector_orthogonal_to_anti_canonical(self):
        assert verify_k_perp_basis_orthogonal_to_canonical()

    def test_functional_recovers_anti_canonical_pairing(self):
        f = _functional_K_perp()
        # f . v == <v, -K_X>_Pic for every v in Pic(X).
        k = anti_canonical()
        for i in range(DIM_PIC):
            ei = np.zeros(DIM_PIC, dtype=np.int64)
            ei[i] = 1
            assert int(f @ ei) == intersect(ei, k)

    def test_basis_specific_first_two_vectors(self):
        b = K_PERP_BASIS
        # b_1 = H_1 - 2 E_1
        expected_b1 = np.array([1, 0, -2, 0, 0, 0, 0, 0, 0, 0], dtype=np.int64)
        assert np.array_equal(b[0], expected_b1)
        # b_2 = H_2 - 2 E_1
        expected_b2 = np.array([0, 1, -2, 0, 0, 0, 0, 0, 0, 0], dtype=np.int64)
        assert np.array_equal(b[1], expected_b2)

    def test_basis_exceptional_diff_vectors(self):
        b = K_PERP_BASIS
        # b_{3+k} = E_{2+k} - E_1 (i.e. coord -1 at idx 2, coord +1 at idx 3+k)
        for k in range(7):
            row = b[2 + k]
            assert int(row[2]) == -1
            assert int(row[3 + k]) == 1
            # All other entries are zero
            mask = np.ones(DIM_PIC, dtype=bool)
            mask[2] = False
            mask[3 + k] = False
            assert np.all(row[mask] == 0)


# ---------------------------------------------------------------------------
# KNY delta_i in K_perp coordinates and reconstruction
# ---------------------------------------------------------------------------


class TestKNYInKPerpCoords:
    def test_matrix_shape(self):
        M = kny_in_k_perp_coords()
        assert M.shape == (RANK_KNY, RANK_K_PERP)
        assert M.dtype.kind == "i"

    def test_reconstruction_M_times_basis_equals_kny_in_pic(self):
        assert verify_reconstruction()

    def test_kny_delta_i_all_in_k_perp(self):
        """Defensive: each KNY delta_i is orthogonal to -K_X."""
        assert verify_every_kny_delta_orthogonal_to_canonical()

    def test_specific_kny_coords_in_k_perp_basis(self):
        """Pin the K_perp coordinates of each delta_i.

        Derivation: delta_i in Pic coords -> free coords are the
        canonical Pic coords at indices (0, 1, 3..9).
        """
        M = kny_in_k_perp_coords()
        expected = np.array([
            [0, 0, -1,  0,  0,  0,  0,  0,  0],   # delta_0 = E_1 - E_2 -> -(E_2-E_1) = -b_3
            [0, 0,  0,  1, -1,  0,  0,  0,  0],   # delta_1 = E_3 - E_4 = b_4 - b_5
            [1, 0,  0, -1,  0,  0,  0,  0,  0],   # delta_2 = H_1 - E_1 - E_3 = b_1 - b_4
            [0, 1,  0,  0,  0, -1, -1,  0,  0],   # delta_3 = H_2 - E_5 - E_6 = b_2 - b_6 - b_7
            [0, 0,  0,  0,  0,  0,  1, -1,  0],   # delta_4 = E_6 - E_7 = b_7 - b_8
            [0, 0,  0,  0,  0,  1, -1,  0,  0],   # delta_5 = E_5 - E_6 = b_6 - b_7
            [0, 0,  0,  0,  0,  0,  0,  1, -1],   # delta_6 = E_7 - E_8 = b_8 - b_9
        ], dtype=np.int64)
        assert np.array_equal(M, expected)


# ---------------------------------------------------------------------------
# Smith Normal Form and saturation verdict
# ---------------------------------------------------------------------------


class TestSmithNormalFormAndVerdict:
    def test_snf_shape(self):
        snf = smith_normal_form_of_kny()
        assert (snf.rows, snf.cols) == (RANK_KNY, RANK_K_PERP)

    def test_seven_nonzero_elementary_divisors(self):
        assert verify_snf_has_exactly_seven_nonzero_elementary_divisors()

    def test_elementary_divisors_are_all_one(self):
        """The KNY embedding is saturated in K_X^perp; all d_i = 1.
        This is the core algebraic-geometry content of cycle 2.
        """
        divs = elementary_divisors()
        assert divs == [1, 1, 1, 1, 1, 1, 1]

    def test_elementary_divisors_divide_consecutively(self):
        """SNF invariant: d_i divides d_{i+1}. Trivially holds when
        all are 1, but pin the invariant for any future regression."""
        divs = elementary_divisors()
        for i in range(len(divs) - 1):
            assert divs[i + 1] % divs[i] == 0

    def test_saturation_index_is_one(self):
        assert saturation_index() == 1

    def test_verdict_is_saturated(self):
        assert verdict_saturation() == "SATURATED_AT_RANK_7"

    def test_verdict_is_one_of_two_branches(self):
        v = verdict_saturation()
        assert v == "SATURATED_AT_RANK_7" or v.startswith(
            "NOT_SATURATED_WITH_INDEX_"
        )

    def test_no_closure_generators_needed_for_saturated_case(self):
        gens = saturation_closure_generators()
        assert gens == []


# ---------------------------------------------------------------------------
# Cycle-1 / cycle-2 cross-consistency
# ---------------------------------------------------------------------------


class TestCycleConsistency:
    def test_sakai_form_is_same_as_generic_form(self):
        """Cycle-1 finding (KNY sec.3.3 eq 3.26): the form is
        configuration-independent. Pinned again here so cycle-2
        regressions surface immediately."""
        from sakai_d6.surface import intersection_form_sakai_nongen
        assert np.array_equal(intersection_form_sakai_nongen(), GRAM_PIC)

    def test_kny_imaginary_root_equals_anti_canonical(self):
        """Algebraic-geometry pin: the imaginary root of the D_6^{(1)}
        affine Cartan equals -K_X, with marks a = (1, 1, 2, 2, 2, 1, 1).

        delta_imag = a . delta = sum_i a_i delta_i = -K_X = K_anti.
        """
        delta = d6_affine_simple_roots_kny()
        a = np.array([1, 1, 2, 2, 2, 1, 1], dtype=np.int64)
        delta_imag = a @ delta  # shape (10,)
        assert np.array_equal(delta_imag, anti_canonical())

    def test_anti_canonical_self_intersection_is_zero(self):
        """(-K_X)^2 = K_X^2 = 8 - 8 = 0 for Bl_8(P^1 x P^1) (Halphen
        pencil / rational elliptic surface). This makes K_anti
        isotropic in the Pic form, hence K_anti is itself in K_X^perp.
        """
        k = anti_canonical()
        assert intersect(k, k) == 0

    def test_anti_canonical_is_in_k_perp(self):
        """Since K_anti is isotropic in the Pic form,
        K_anti . K_anti = 0, so K_anti in K_perp. Express it as
        Z-combo of the K_perp basis.
        """
        k = anti_canonical()
        # Solution: K_anti = 2 b_1 + 2 b_2 - b_3 - b_4 - ... - b_9.
        coeffs = np.array([2, 2, -1, -1, -1, -1, -1, -1, -1], dtype=np.int64)
        reconstructed = coeffs @ K_PERP_BASIS
        assert np.array_equal(reconstructed, k)


# ---------------------------------------------------------------------------
# JSON artefacts
# ---------------------------------------------------------------------------


class TestArtefacts:
    def test_writes_k_perp_basis_artefact(self):
        out_path = (
            Path(__file__).resolve().parents[2] / "k_perp_basis.json"
        )
        payload = {
            "source": "construction in sakai_d6/saturation.py; "
            "ker of integer functional <-, -K_X> = 2 v_H1 + 2 v_H2 + sum v_E",
            "rank": RANK_K_PERP,
            "ambient_rank": DIM_PIC,
            "basis_rows_in_pic_coords": K_PERP_BASIS.tolist(),
            "verified_every_row_orthogonal_to_canonical": True,
        }
        out_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
        )
        assert out_path.exists()

    def test_writes_kny_in_k_perp_coords_artefact(self):
        out_path = (
            Path(__file__).resolve().parents[2] / "kny_in_k_perp_coords.json"
        )
        payload = {
            "source": "d6_affine_simple_roots_kny() (KNY 2017 eq 8.101) "
            "expressed in the K_X^perp basis from saturation.py",
            "matrix_shape": "7 x 9",
            "rows_are_kny_delta_0_through_delta_6": True,
            "matrix": kny_in_k_perp_coords().tolist(),
        }
        out_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
        )
        assert out_path.exists()

    def test_writes_saturation_verdict_artefact(self):
        out_path = (
            Path(__file__).resolve().parents[2] / "saturation_verdict.json"
        )
        snf = smith_normal_form_of_kny()
        snf_list = [[int(snf[i, j]) for j in range(snf.cols)]
                    for i in range(snf.rows)]
        payload = {
            "task_id": "R1-ROUTE-F-K-PERP-BASIS",
            "cycle": "2 of 3",
            "predecessor": "R1-ROUTE-F-SAKAI-NONGEN (bridge commit 53efe94)",
            "primary_source": "KNY 2017 J.Phys.A 50 073001 (arXiv:1509.08186v8) "
            "sec.3.3 eq (3.26), sec.8.2.19 eq (8.101)",
            "verdict": verdict_saturation(),
            "elementary_divisors": elementary_divisors(),
            "saturation_index": saturation_index(),
            "smith_normal_form_diagonal": snf_list,
            "closure_generators_in_k_perp_coords": saturation_closure_generators(),
        }
        out_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
        )
        assert out_path.exists()
