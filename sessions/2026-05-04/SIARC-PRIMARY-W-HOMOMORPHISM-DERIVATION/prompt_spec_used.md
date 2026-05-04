# prompt_spec_used.md

This session executed SIARC researcher prompt 033 issued
2026-05-04 ~15:35 JST.

## Task ID
   SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION

## Gate
Prompt 033 fires IFF prompt 031 (WITTE-FORRESTER-2010-ACQUISITION)
returns one of:
  - UPGRADE_WF10_ACQUIRED_W_HOMOMORPHISM_NOT_IN_WF10
  - UPGRADE_WF10_NIA_PAYWALL
  - HALT_WF10_*

**Gate satisfied** by:
  - Bridge commit (prompt 031): `WITTE-FORRESTER-2010-ACQUISITION -
    HALT_WF10_BIBLIOGRAPHIC_TARGET_NOT_FOUND` (terminal log,
    2026-05-04).
  - Bridge file: `sessions/2026-05-04/WITTE-FORRESTER-2010-ACQUISITION/handoff.md`
    line 5: `**Status:** PARTIAL (spec target halt; substitute
    probed; verdict reached)`.
  - The HALT_WF10_BIBLIOGRAPHIC_TARGET_NOT_FOUND verdict matches
    `HALT_WF10_*` in the gate.

Prompt 033 therefore proceeds (Path B = SIARC primary derivation).

## Goal (verbatim from §0)
Construct an explicit group homomorphism
   φ : W(B_2) → W((2A_1)^{(1)})
(or its inverse, depending on which direction is natural)
between the Okamoto 1987 W(B_2) framing and the Sakai 2001
W((2A_1)^{(1)}) framing of P_III(D_6^{(1)}), with full verification
and AEAL-honest provenance.

## Spec corrections in situ (see discrepancy_log.json)

The spec wrote `W(B_2)` (the finite Weyl group) but Okamoto 1987
§2.1 defines `G ≅ W^{aff}(B_2)` (affine), not `W(B_2)`. The
construction is reframed at the affine level. See
`construction_phase_B.md` §B.1 for the H_3* hypothesis.

## Phases
   - Phase A.1: Okamoto extraction → `extract_okamoto_BB2_generators.md`.
   - Phase A.2: Sakai extraction → `extract_sakai_2A1_generators.md`.
   - Phase B  : Construction + verification → `construction_phase_B.md` + `verify_homomorphism.py` + `verify_homomorphism.log`.
   - Phase C  : Kernel + classification → `kernel_classification.md`.
   - Phase D  : Cross-walk table → `crosswalk_table.md`.
   - Phase E  : Handoff → `handoff.md`.

## Halt conditions
None of the spec halt-conditions triggered:
  - HALT_W_HOMOMORPHISM_RELATION_FAILS: not triggered (all 6 relations pass; sympy log lines 24–35).
  - HALT_PARAMETER_ACTION_INCONSISTENT: not triggered (parameter map a_0=−v_1, a_1=1+v_1, b_0=−v_2, b_1=1+v_2 is bijective; all single-generator + length-2 actions commute, sympy log lines 11–22).
  - HALT_CONTRADICTS_KNY_2017: not triggered (cross-walk consistent with KNY 2017 §6 formulae per slot 14 readback in prompt 029).
  - HALT_CARTAN_ENTRY_DISAGREES_BETWEEN_PRIMARY_AND_SAGE: not triggered (no SAGE used; Cartan matrices computed by hand from primary verbatim quotes; B_2^{(1)} matrix in A.1, (2A_1)^{(1)} block-diagonal matrix in A.2).
  - HALT_SIARC_AUTHORSHIP_INCONSISTENCY: not triggered (no Tier-3 source surfaced in the audit; SIARC-primary authorship is preserved).

## Outcome
**CLOSED_M6_PHASE_B5_W_CROSSWALK_BY_SIARC_PRIMARY_DERIVATION** with
the qualifier that the bridge is an INDEX-2 EMBEDDING (not a strict
isomorphism). See `kernel_classification.md` §C.5 for three
operationally equivalent re-formulations and the recommended
phrasing for M6 Phase B.5 anchor + CT v1.4 §3.5.
