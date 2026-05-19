"""Cycle 3a (R1-ROUTE-F-EFFECTIVITY) verification tests.

Pre-registered expected verdicts for each KNY simple root delta_i.
Declared at the TOP of this file (before any computation runs)
so that the assertions are falsifiable per AEAL discipline.

If any computed verdict differs from the pre-registered table, the
corresponding test will fail and the cycle's `unexpected_finds.json`
will record the divergence prominently.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    H,
    E,
    anti_canonical,
    d6_affine_simple_roots_kny,
    intersect,
)
from sakai_d6.effectivity import (
    IRREDUCIBLE_BASIS_DETERMINANT,
    IRREDUCIBLE_BASIS_MATRIX,
    IRREDUCIBLE_COMPONENT_NAMES,
    classify_kny_root,
    classify_kny_roots,
    effective_decomposition,
    irreducible_components_kny,
    is_effective,
    try_weyl_moves_for_effectivity,
    verify_effective_decomposition_lattice_consistent,
    verify_report,
    weyl_reflection,
)


# ---------------------------------------------------------------------------
# Pre-registered expected verdicts (declared BEFORE computing)
# ---------------------------------------------------------------------------
#
# Per the synthesizer's cycle-3a brief and verified against the
# actual `d6_affine_simple_roots_kny()` source:
#
#     delta_0 = E_1 - E_2          -> effective (strict transform, chain {1,2})
#     delta_1 = E_3 - E_4          -> effective (strict transform, chain {3,4})
#     delta_2 = H_1 - E_1 - E_3    -> effective (H_1 fiber through chains
#                                                {1,2} and {3,4})
#     delta_3 = H_2 - E_5 - E_6    -> effective (H_2 fiber through chain
#                                                {5,6,7,8})
#     delta_4 = E_6 - E_7          -> effective (strict transform, chain
#                                                {5,6,7,8})
#     delta_5 = E_5 - E_6          -> effective (strict transform, chain
#                                                {5,6,7,8})
#     delta_6 = E_7 - E_8          -> effective (strict transform, chain
#                                                {5,6,7,8})

PREREGISTERED_VERDICTS = {
    0: "effective",
    1: "effective",
    2: "effective",
    3: "effective",
    4: "effective",
    5: "effective",
    6: "effective",
}

# Pre-registered expected explicit decompositions (when effective).
# Each delta_i should decompose as itself with multiplicity 1, since
# the seven delta_i are themselves the (-2)-component basis.
PREREGISTERED_DECOMPOSITIONS = {
    i: {**{name: 0 for name in (
        "delta_0", "delta_1", "delta_2", "delta_3",
        "delta_4", "delta_5", "delta_6", "E_2", "E_4", "E_8",
    )}, **{f"delta_{i}": 1}}
    for i in range(7)
}


# ---------------------------------------------------------------------------
# Irreducible-component basis structural tests
# ---------------------------------------------------------------------------


class TestIrreducibleComponentBasis:
    def test_ten_components(self):
        comps = irreducible_components_kny()
        assert len(comps) == 10

    def test_names_in_canonical_order(self):
        comps = irreducible_components_kny()
        names = [c[0] for c in comps]
        assert names == [
            "delta_0", "delta_1", "delta_2", "delta_3",
            "delta_4", "delta_5", "delta_6",
            "E_2", "E_4", "E_8",
        ]

    def test_basis_matrix_shape(self):
        assert IRREDUCIBLE_BASIS_MATRIX.shape == (10, 10)

    def test_basis_matrix_integer_dtype(self):
        assert np.issubdtype(IRREDUCIBLE_BASIS_MATRIX.dtype, np.integer)

    def test_basis_is_unimodular(self):
        """The 10 irreducible components form a Z-basis of Pic(X)."""
        assert abs(IRREDUCIBLE_BASIS_DETERMINANT) == 1

    def test_e2_e4_e8_self_intersection_minus_one(self):
        """The chain-tip (-1)-curves have self-intersection -1."""
        for tip in (E(2), E(4), E(8)):
            assert intersect(tip, tip) == -1

    def test_delta_i_self_intersection_minus_two(self):
        """The seven (-2)-curves have self-intersection -2."""
        delta = d6_affine_simple_roots_kny()
        for i in range(7):
            assert intersect(delta[i], delta[i]) == -2


# ---------------------------------------------------------------------------
# Per-delta-i effectivity tests (one per i, against pre-registered table)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("i", list(range(7)))
class TestEffectivityPerDelta:
    def test_verdict_matches_pre_registered(self, i):
        record = classify_kny_root(i)
        expected = PREREGISTERED_VERDICTS[i]
        assert record["verdict"] == expected, (
            f"delta_{i} pre-registered as {expected!r} but classified "
            f"as {record['verdict']!r}; record={record}"
        )

    def test_decomposition_matches_pre_registered(self, i):
        record = classify_kny_root(i)
        if record["verdict"] != "effective":
            pytest.skip(
                f"delta_{i} verdict is {record['verdict']!r}, "
                "decomposition pin only applies when 'effective'"
            )
        expected = PREREGISTERED_DECOMPOSITIONS[i]
        assert record["decomposition"] == expected

    def test_decomposition_reconstructs(self, i):
        record = classify_kny_root(i)
        if record["verdict"] != "effective":
            pytest.skip("only applies when 'effective'")
        delta = d6_affine_simple_roots_kny()
        decomp = record["decomposition"]  # type: ignore[assignment]
        assert verify_effective_decomposition_lattice_consistent(
            delta[i], decomp  # type: ignore[arg-type]
        )

    def test_decomposition_intersection_form_consistent(self, i):
        """Lattice-level consistency: every effective delta_i must
        have self-intersection -2 and pair to 0 with -K_X. (This is
        already established in cycles 1-2 but pinning here ties the
        decomposition to those properties.)
        """
        record = classify_kny_root(i)
        if record["verdict"] != "effective":
            pytest.skip("only applies when 'effective'")
        assert record["self_intersection"] == -2
        assert record["intersection_with_anti_canonical"] == 0


# ---------------------------------------------------------------------------
# Weyl reflection structural tests
# ---------------------------------------------------------------------------


class TestWeylReflection:
    def test_weyl_reflection_returns_integer_array(self):
        delta = d6_affine_simple_roots_kny()
        v = anti_canonical()
        for j in range(7):
            r = weyl_reflection(v, delta[j])
            assert isinstance(r, np.ndarray)
            assert np.issubdtype(r.dtype, np.integer)
            assert r.shape == (DIM_PIC,)

    def test_weyl_reflection_is_involution(self):
        """r_alpha o r_alpha = identity."""
        delta = d6_affine_simple_roots_kny()
        test_battery = [anti_canonical(), H(1), H(2), E(1), E(5), E(8)]
        for v in test_battery:
            for j in range(7):
                rv = weyl_reflection(v, delta[j])
                rrv = weyl_reflection(rv, delta[j])
                assert np.array_equal(rrv, v), (
                    f"r_delta_{j} not an involution on {v}"
                )

    def test_weyl_reflection_sends_root_to_negative(self):
        """r_alpha(alpha) = -alpha for any (-2)-root alpha."""
        delta = d6_affine_simple_roots_kny()
        for j in range(7):
            rj = weyl_reflection(delta[j], delta[j])
            assert np.array_equal(rj, -delta[j])

    def test_weyl_reflection_is_isometry(self):
        """<r(v), r(w)> = <v, w> for all v, w and any (-2)-root."""
        delta = d6_affine_simple_roots_kny()
        rng = np.random.default_rng(20260520)
        # Deterministic test battery + a few pseudo-random integer
        # Pic vectors. Seed is fixed for reproducibility.
        test_battery = [
            anti_canonical(),
            H(1), H(2),
            E(1), E(3), E(5), E(7), E(8),
            E(1) + E(2) - E(3),
        ]
        for _ in range(5):
            test_battery.append(
                rng.integers(low=-3, high=4, size=DIM_PIC, dtype=np.int64)
            )
        for v in test_battery:
            for w in test_battery:
                for j in range(7):
                    rv = weyl_reflection(v, delta[j])
                    rw = weyl_reflection(w, delta[j])
                    assert intersect(rv, rw) == intersect(v, w), (
                        f"isometry fails on (v,w)=({v},{w}) under "
                        f"r_delta_{j}"
                    )

    def test_weyl_reflection_preserves_K_X(self):
        """r_alpha(-K_X) = -K_X for any alpha orthogonal to -K_X."""
        delta = d6_affine_simple_roots_kny()
        k_anti = anti_canonical()
        for j in range(7):
            r = weyl_reflection(k_anti, delta[j])
            assert np.array_equal(r, k_anti), (
                f"r_delta_{j} does not fix -K_X"
            )

    def test_weyl_reflection_preserves_K_perp_setwise(self):
        """For any v in K_X^perp and any KNY simple root delta_j,
        r_{delta_j}(v) is also in K_X^perp.
        """
        delta = d6_affine_simple_roots_kny()
        k_anti = anti_canonical()
        # Build a small battery of vectors in K_X^perp:
        # the seven delta_i are in K_X^perp; -K_X itself is in
        # K_X^perp (cycle 2); some integer combinations too.
        battery = [delta[i] for i in range(7)] + [
            k_anti,
            delta[0] + 2 * delta[2],
            3 * delta[3] - delta[5],
        ]
        for v in battery:
            assert intersect(v, k_anti) == 0  # battery sanity check
            for j in range(7):
                r = weyl_reflection(v, delta[j])
                assert intersect(r, k_anti) == 0, (
                    f"r_delta_{j}(v) leaves K_X^perp; v={v}"
                )


# ---------------------------------------------------------------------------
# Classification pipeline + verifier
# ---------------------------------------------------------------------------


class TestClassificationPipeline:
    def test_classify_kny_roots_returns_seven_records(self):
        results = classify_kny_roots()
        assert len(results) == 7

    def test_every_verdict_in_allowed_branches(self):
        results = classify_kny_roots()
        allowed = {
            "effective",
            "not_effective",
            "effective_after_named_Weyl_move",
        }
        for r in results:
            assert r["verdict"] in allowed

    def test_all_seven_effective_matches_pre_registration(self):
        """The pre-registered table expects all seven 'effective';
        this test ASSERTS that. If a delta_i ever lands non-effective
        under the canonical KNY embedding, this assertion fails and
        the cycle records an unexpected_finds entry.
        """
        results = classify_kny_roots()
        verdicts = [r["verdict"] for r in results]
        assert verdicts == ["effective"] * 7

    def test_verify_report_all_flags_true(self):
        report = verify_report()
        flags = report["flags"]  # type: ignore[index]
        assert all(flags.values()), f"some flag is false: {flags}"


# ---------------------------------------------------------------------------
# Cross-cycle consistency: cycle-2 saturation + cycle-3a effectivity
# ---------------------------------------------------------------------------


class TestCycleConsistency:
    def test_irreducible_components_lie_in_Pic_with_correct_squared_lengths(self):
        comps = irreducible_components_kny()
        for name, vec in comps:
            if name.startswith("delta"):
                assert intersect(vec, vec) == -2, (
                    f"{name} should be a (-2)-curve, got {intersect(vec, vec)}"
                )
            else:
                assert intersect(vec, vec) == -1, (
                    f"{name} should be a (-1)-curve, got {intersect(vec, vec)}"
                )

    def test_minus_K_X_decomposes_with_affine_marks(self):
        """The cycle-2 imaginary-root identity
            sum_i a_i delta_i = -K_X
        with affine D_6^{(1)} marks (1, 1, 2, 2, 2, 1, 1).

        Pinning this here under the effectivity-module imports
        guarantees the cycle-3a code agrees with cycle-2's substrate.
        (-K_X)'s effective decomposition over the 10-component basis,
        however, includes the chain-tip E_2, E_4, E_8 to absorb the
        non-affine-root content; verified separately below.
        """
        delta = d6_affine_simple_roots_kny()
        marks = np.array([1, 1, 2, 2, 2, 1, 1], dtype=np.int64)
        s = sum(int(marks[i]) * delta[i] for i in range(7))
        assert np.array_equal(s, anti_canonical())

    def test_minus_K_X_is_effective_with_extended_decomposition(self):
        """-K_X is effective on the surface with a known explicit
        decomposition into the 10 irreducible components.
        """
        k_anti = anti_canonical()
        decomp = effective_decomposition(k_anti)
        assert decomp is not None, "-K_X should be effective"
        # Reconstruction must reproduce -K_X exactly.
        assert verify_effective_decomposition_lattice_consistent(
            k_anti, decomp
        )

    def test_three_chain_tip_e_classes_are_effective(self):
        """E_2, E_4, E_8 are (-1)-curves on the surface (each is itself
        an irreducible component). They are effective via the trivial
        decomposition.
        """
        for tip_class in (E(2), E(4), E(8)):
            assert is_effective(tip_class)
            decomp = effective_decomposition(tip_class)
            assert decomp is not None
            assert all(c >= 0 for c in decomp.values())


# ---------------------------------------------------------------------------
# JSON artefact: written so the bridge captures the classification table
# ---------------------------------------------------------------------------


PROJECT_ROOT = Path(__file__).resolve().parents[2]


class TestArtefacts:
    def test_writes_effectivity_table_artefact(self, tmp_path):
        out_path = PROJECT_ROOT / "effectivity_table.json"
        report = verify_report()
        out_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
        # Round-trip
        loaded = json.loads(out_path.read_text(encoding="utf-8"))
        assert loaded == report

    def test_writes_irreducible_components_artefact(self):
        out_path = PROJECT_ROOT / "irreducible_components_kny.json"
        comps = irreducible_components_kny()
        payload = {
            "basis_determinant": int(IRREDUCIBLE_BASIS_DETERMINANT),
            "ordered_component_names": IRREDUCIBLE_COMPONENT_NAMES,
            "components": {name: vec.tolist() for name, vec in comps},
            "basis_matrix_pic_columns_are_components": (
                IRREDUCIBLE_BASIS_MATRIX.tolist()
            ),
            "pic_basis_order_rows": [
                "H_1", "H_2",
                "E_1", "E_2", "E_3", "E_4",
                "E_5", "E_6", "E_7", "E_8",
            ],
        }
        out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        loaded = json.loads(out_path.read_text(encoding="utf-8"))
        assert loaded["basis_determinant"] == int(IRREDUCIBLE_BASIS_DETERMINANT)
