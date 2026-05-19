"""Cycle 1 (R1-ROUTE-F-SAKAI-NONGEN) tests.

Primary source for the Sakai PIII(D_6) configuration and the D_6^{(1)}
simple roots: Kajiwara-Noumi-Yamada (KNY) 2017, "Geometric Aspects of
Painleve Equations", J. Phys. A 50 (2017) 073001, arXiv:1509.08186v8,
sec.3.3 eq (3.26) and sec.8.2.19 eq (8.98), (8.100), (8.101).

Pre-registered AEAL claim: claims/claim-r1-sakai-nongen-001.json.

Key finding documented by this test module:
  The Pic(X) intersection form is configuration-independent (KNY
  sec.3.3 eq (3.26)); the PIII(D_6) non-genericity shows up in the
  CHOICE of seven simple roots delta_0,...,delta_6, not in the
  Gram matrix.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    GRAM_PIC_SAKAI_NONGEN,
    anti_canonical,
    compute_kny_root_gram,
    compute_poc_root_gram_under_sakai_form,
    d6_affine_simple_roots,
    d6_affine_simple_roots_kny,
    expected_d6_affine_symmetric_cartan,
    expected_d6_affine_symmetric_cartan_kny,
    intersection_form_sakai_nongen,
    signature_sakai_nongen,
    verdict_sakai_nongen,
    verify_kny_embedding_orthogonal_to_canonical,
    verify_kny_embedding_self_intersection_minus_two,
)


# ---------------------------------------------------------------------------
# Brief deliverables (1)-(3): the Sakai non-generic form
# ---------------------------------------------------------------------------


class TestSakaiNonGenForm:
    def test_returns_10x10_integer_matrix(self):
        g = intersection_form_sakai_nongen()
        assert g.shape == (DIM_PIC, DIM_PIC)
        assert g.dtype.kind == "i"

    def test_sakai_form_unimodularity(self):
        """KNY sec.3.3 eq (3.26): det = +/- 1."""
        det = int(round(np.linalg.det(GRAM_PIC_SAKAI_NONGEN.astype(np.float64))))
        assert det in (1, -1)

    def test_sakai_form_signature(self):
        """Sakai form is U (+) (-I_8), signature (1, 9), zero kernel."""
        pos, zero, neg = signature_sakai_nongen(tol=1e-9)
        assert (pos, zero, neg) == (1, 0, 9)

    def test_sakai_form_equals_generic_form_per_kny_3_26(self):
        """KNY 2017 sec.3.3 eq (3.26) finding: the Pic intersection form
        is configuration-independent. This test documents the discovery
        and is the canonical record that the two forms coincide.
        """
        assert np.array_equal(GRAM_PIC_SAKAI_NONGEN, GRAM_PIC)


# ---------------------------------------------------------------------------
# KNY 2017 sec.8.2.19 eq (8.101) -- the canonical Sakai simple roots
# ---------------------------------------------------------------------------


class TestKNYEmbedding:
    def test_kny_returns_7x10_matrix(self):
        m = d6_affine_simple_roots_kny()
        assert m.shape == (7, DIM_PIC)
        assert m.dtype.kind == "i"

    def test_kny_self_intersection_minus_two(self):
        assert verify_kny_embedding_self_intersection_minus_two()

    def test_kny_orthogonal_to_anti_canonical(self):
        assert verify_kny_embedding_orthogonal_to_canonical()

    def test_kny_gram_matches_d6_affine_cartan(self):
        gram = compute_kny_root_gram()
        expected = expected_d6_affine_symmetric_cartan_kny()
        assert np.array_equal(gram, expected)

    def test_kny_delta_3_not_adjacent_to_delta_5(self):
        """Discovered during implementation: in KNY's labelling,
        delta_5 = E_5 - E_6 is attached to delta_4, NOT to delta_3.
        Verify the agent's reading of the eq (8.100) diagram is correct.
        """
        roots = d6_affine_simple_roots_kny()
        d3, d5 = roots[3], roots[5]
        pairing = int(d3.astype(np.int64) @ GRAM_PIC_SAKAI_NONGEN @ d5.astype(np.int64))
        assert pairing == 0

    def test_kny_delta_4_has_three_neighbours(self):
        """delta_4 is the right-fork node and must connect to delta_3,
        delta_5, delta_6."""
        gram = compute_kny_root_gram()
        # row 4: off-diagonal +1s mark neighbours
        neighbours = [j for j in range(7) if j != 4 and gram[4, j] == 1]
        assert sorted(neighbours) == [3, 5, 6]

    def test_kny_delta_2_has_three_neighbours(self):
        """delta_2 is the left-fork node and must connect to delta_0,
        delta_1, delta_3."""
        gram = compute_kny_root_gram()
        neighbours = [j for j in range(7) if j != 2 and gram[2, j] == 1]
        assert sorted(neighbours) == [0, 1, 3]

    def test_kny_embedding_lives_in_Z(self):
        """All KNY simple roots are integer-coefficient vectors in Pic(X)."""
        roots = d6_affine_simple_roots_kny()
        assert np.all(roots == roots.astype(np.int64))


# ---------------------------------------------------------------------------
# Brief deliverable (4): the POC embedding under the Sakai form
# ---------------------------------------------------------------------------


class TestPOCEmbeddingUnderSakaiForm:
    def test_poc_embedding_satisfies_d6_affine_cartan_under_sakai_form(self):
        """The predecessor cycle's alpha_0,...,alpha_6 still satisfy the
        D_6^{(1)} Cartan condition under the Sakai non-generic form,
        because the form is unchanged from the generic case
        (KNY sec.3.3 eq (3.26)). This is the abstract algebraic check;
        it does NOT mean the POC embedding is the canonical Sakai one.
        See cycle1_verdict (SAKAI_FORM_REQUIRES_NEW_EMBEDDING) and the
        artefact poc_gram_under_sakai_form.json for the comparison.
        """
        gram = compute_poc_root_gram_under_sakai_form()
        expected = expected_d6_affine_symmetric_cartan()
        assert np.array_equal(gram, expected)

    def test_poc_gram_artefact_written(self, tmp_path):
        """Write the POC Gram matrix under the Sakai form to a JSON
        artefact for downstream inspection (matches the brief's
        deliverable (4))."""
        gram = compute_poc_root_gram_under_sakai_form()
        out_path = Path(__file__).resolve().parents[2] / "poc_gram_under_sakai_form.json"
        payload = {
            "source_paper": "KNY 2017 J.Phys.A 50 073001 (arXiv:1509.08186)",
            "section": "sec.3.3 eq (3.26) for the form; sec.8.2.19 eq (8.101) for the KNY delta_i",
            "predecessor_session": "R1-ROUTE-F-POC (bridge commit 0d7d20e)",
            "poc_alpha_under_sakai_form_gram": gram.tolist(),
            "matches_d6_affine_symmetric_cartan": bool(
                np.array_equal(gram, expected_d6_affine_symmetric_cartan())
            ),
        }
        out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        assert out_path.exists()
        assert payload["matches_d6_affine_symmetric_cartan"]


# ---------------------------------------------------------------------------
# Brief: verdict resolution to exactly one of three branches
# ---------------------------------------------------------------------------


class TestVerdict:
    def test_verdict_is_one_of_three_branches(self):
        v = verdict_sakai_nongen()
        assert v in (
            "SAKAI_FORM_PRESERVES_POC_EMBEDDING",
            "SAKAI_FORM_REQUIRES_NEW_EMBEDDING",
            "SAKAI_FORM_ADMITS_NO_INTEGER_EMBEDDING_AT_THIS_RANK",
        )

    def test_verdict_records_actual_branch_taken(self):
        """The agent records the actual branch as part of the AEAL
        claim (the brief says: "recorded as part of the claim, not
        pre-asserted"). The recorded value below is what the
        computation yields; this test pins it for reproducibility."""
        v = verdict_sakai_nongen()
        # The POC embedding (alpha_3 = H_2 - H_1, non-effective) does
        # not match KNY's canonical delta_3 = H_2 - E_5 - E_6. The
        # canonical Sakai-form embedding is therefore different from
        # the predecessor's. Branch 2.
        assert v == "SAKAI_FORM_REQUIRES_NEW_EMBEDDING"

    def test_verdict_artefact_written(self):
        """Persist the verdict, the two embeddings, and the source
        citation to a JSON artefact for downstream review (cycle 2
        will consume the validated KNY embedding)."""
        out_path = Path(__file__).resolve().parents[2] / "sakai_nongen_verdict.json"
        payload = {
            "task_id": "R1-ROUTE-F-SAKAI-NONGEN",
            "primary_source": "Kajiwara-Noumi-Yamada 2017, J.Phys.A 50 073001 (arXiv:1509.08186v8)",
            "primary_source_local_sha256_8mb_pdf": "see _tmp_lit/KNY2017.pdf",
            "form_finding": "Pic intersection form is configuration-independent (KNY sec.3.3 eq (3.26))",
            "verdict": verdict_sakai_nongen(),
            "poc_alpha_embedding": d6_affine_simple_roots().tolist(),
            "kny_delta_embedding_per_8_101": d6_affine_simple_roots_kny().tolist(),
            "kny_delta_gram_under_sakai_form": compute_kny_root_gram().tolist(),
            "kny_delta_dynkin_adjacencies": [
                [0, 2], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6]
            ],
        }
        out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        assert out_path.exists()
