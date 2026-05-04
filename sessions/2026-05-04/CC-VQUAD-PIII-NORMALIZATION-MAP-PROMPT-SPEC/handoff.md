# Handoff — CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC (M6 spec, pre-fire deposit)

**Date:** 2026-05-04 (JST)
**Agent:** GitHub Copilot CLI (operator-side; deposit session)
**Pattern:** QS-2 / QS-3 / T1P2-DEPOSIT (synthesizer-drafted
  prompt spec, AEAL-anchored at deposit time **before** the
  relay agent fires — in contrast to T1P2-DEPOSIT which was
  post-hoc-anchored)
**Source:** Operator chat 2026-05-04 (PRE-DRAFT-CC-VQUAD-PIII-
  NORMALIZATION-MAP-PROMPT spec) + Q35 ruling 2026-05-04 +
  R5-OKAMOTO-NUMDAM-RETRY `OUTCOME_R5RT_NUMDAM_ACQUIRED`
  (SCENARIO B confirmed) + v1.16 picture absorption +
  H4_PASS_108_DIGITS verdict + A-01 verdict
**Status:** COMPLETE (deposit drafted; awaiting synthesizer QA
  review; operator dispatches the relay-prompt body **after** QA)

---

## What was accomplished

Drafted the synthesizer-drafted prompt spec for the
**CC-VQUAD-PIII-NORMALIZATION-MAP** relay (M6 closure) and
deposited it to bridge **before** the relay agent fires, so
Claude (synthesizer) can perform critical-path QA review on the
spec content before operator dispatches the relay-prompt body
into a fresh Copilot CLI session.

The spec defines a 9-phase relay (0.0 / 0.5 / A / B / B.5 / C /
D / E / F) closing G15 + G22 + op:cc-formal-borel residual at
once, with the W(B_2) ↔ W(D_6) affine-Weyl cross-walk explicitly
embedded as Phase B.5 per Q35 ruling 2026-05-04.

This is a **pre-fire** deposit (in contrast to T1P2-DEPOSIT which
was post-hoc-anchored at 22 KB AFTER the relay landed
UPGRADE_PARTIAL_FORMAL_LEVEL); chronology note is captured at the
top of `prompt_spec.md`.

## Scope

This deposit (does NOT touch closure work itself):
  - Drafts spec body inside ` ``` ` code block (verbatim text
    intended for relay-agent dispatch)
  - Inlines synthesizer Notes 1–7 into the spec body itself per
    the QS-2 pattern (no separate notes document needed)
  - Provides QA review checklist for synthesizer
  - Lists bridge anchors / deposit pattern precedents
  - Computes SHA-256 + commits to bridge

This deposit (does NOT do):
  - Fire the relay (operator + synthesizer review first)
  - Modify any literature PDFs or SHA256SUMS.txt
  - Modify any artifact (CT v1.3 / CT v1.4 / D2-NOTE v2.1 /
    PCF-1 v1.3 / PCF-2 v1.3 / umbrella v2.0 / picture v1.16)

## Key spec features

  - **9 phases:** 0.0 (provenance write-out) + 0.5 (bibkey
    collision preflight) + A (formal Birkhoff series at z=0;
    cite ξ_0 ↔ H4 measurement) + B (canonical-form normalization
    map M = Φ_resc ∘ Φ_shift ∘ Φ_symp construction; sub-steps
    B.1–B.5) + B.5 (W cross-walk; sub-tasks B.5.1–B.5.4) + C
    (literature anchoring across slots 01/03/04/06/07/08; sub-
    anchors C.1–C.5) + D (verdict aggregation + numerical
    cross-check vs Barhoumi-Lisovyy 2024) + E (CC-NOTE v1.0
    citable artifact, conditional) + F (handoff + AEAL claims)

  - **8 halt codes:** HALT_M6_LITERATURE_NOT_LANDED +
    AFFINE_WEYL_MISMATCH + BIRKHOFF_SERIES_DRIFT +
    PHASE_B_CONSTRUCTION_INCOMPLETE + NORMALIZATION_INCONSISTENCY
    + LITERATURE_DISAGREES_WITH_H4 + STOKES_NUMERICAL_MISMATCH +
    BIBKEY_COLLISION (operator's 6 + 2 added during drafting:
    PHASE_B_CONSTRUCTION_INCOMPLETE for fundamental structural
    obstructions; STOKES_NUMERICAL_MISMATCH for Phase D.2
    cross-check failures)

  - **AEAL claims minimum:** ≥ 16 entries (= 14 prior T1-Phase-2
    baseline + 2 new for Phase B.5 sub-tasks per Q35)

  - **6 anchor PDFs verified:** all in
    `tex/submitted/control center/literature/g3b_2026-05-03/`
    with SHA prefixes recorded in spec §1:
      slot 01 Birkhoff 1930 — aeb5291e
      slot 03 Birkhoff-Trjitzinsky 1933 — dcd7e3c6
      slot 04 Wasow 1965 — f59d6835
      slot 06 Costin 2008 ch. 5 — 436c6c11
      slot 07 Okamoto 1987 FE 30 P_III — 65294fbc (newly acquired
        2026-05-04 via Kobe-U URL per R5-OKAMOTO-NUMDAM-RETRY)
      slot 08 Barhoumi-Lisovyy-Miller-Prokhorov 2024 — 96c49cdd

  - **Synthesizer rulings embedded:**
      Q35 (M6 fires next; parallel-safe with T1 Phase 3 / Wasow
        §X.3 OCR; Phase B.5 mandatory pre-step)
      R5 SCENARIO B (Costin substitutes Conte-Musette; no
        ethics-gate framing)
      A-01 (Wasow / Birkhoff / B-T / Adams μ-units consistent;
        no factor-of-2 ambiguity)
      H4_PASS_108_DIGITS (C = 8.127336795...; β = 0; values are
        V_QUAD NATIVE — canonical-form match floats at the
        precision floor Barhoumi-Lisovyy 2024 provides)

  - **Hygiene §5 carry-forward:** CT v1.4 / Q20a / T1 Phase 2
    rules forbidding "trivial / trivially / obvious / clearly /
    easily seen to / We claim / It is clear that"; "Wasow §X.3"
    DEPRECATED → use precise theorem citation; verbatim quotes
    ≤ 30 words; "shows / confirms / proves" forbidden in
    prediction-or-conjecture context

## Expected verdict ladder (post-fire)

The relay agent will produce one of:

  - **UPGRADE_V1_0_FULL** — best case; Phases A + B + B.5 + C +
    D all pass with full literature anchoring + numerical cross-
    check at the available precision floor. M6 ✅ closes; G15
    fully closed; G22 fully closed; op:cc-formal-borel residual
    fully resolved. M9 gating reduces from {M4-with-formal-
    baseline-+-structural-roadmap, M6} to {M4-only}.

  - **UPGRADE_V1_0_PARTIAL_NUMERICAL** — Phases A + B + B.5 + C
    pass structurally; Phase D.2 numerical cross-check
    unavailable (Barhoumi-Lisovyy 2024 provides only structural
    monodromy data without numerical Stokes constants for the
    specific parameter values). G15 fully closed; G22 partial
    (structural close, numerical unavailable); op:cc-formal-
    borel partial.

  - **UPGRADE_V1_0_PARTIAL_LITERATURE** — Phase C aggregate is
    C_LITERATURE_BOUNDED (anchor coverage partial). Refire
    path: acquire Conte-Musette ch. 7 OR extend Costin ch. 5
    reading.

  - **UPGRADE_V1_0_PARTIAL_PAGECOUNT** — Phase E build at non-
    canonical page range. Operator-side decision.

  - **HALT_M6_*** — see prompt_spec.md §4 for the 8 specific
    halt codes; each is actionable.

The most likely outcome is **UPGRADE_V1_0_FULL** given:
  - All 6 literature anchors verified
  - H4 measurement is at 108 digits (well in excess of any
    Stokes-data precision Barhoumi-Lisovyy 2024 will provide)
  - W(B_2) ↔ W(D_6) cross-walk is a known structural relationship
    (Sakai-classification quotient); Phase B.5 surfaces it
    explicitly rather than discovers it mid-flight
  - CT v1.3 §3.5 algebraic identity provides the V_quad ↔ P_III
    correspondence at the level needed for Phase A + Phase B map
    composition

The most likely partial outcome is
**UPGRADE_V1_0_PARTIAL_NUMERICAL** if Barhoumi-Lisovyy 2024
provides only structural Stokes-matrix data without explicit
numerical canonical-form Stokes constants. This is acceptable;
it still fully closes G15 and substantially advances G22.

## Strategic implication

If the post-fire verdict is **UPGRADE_V1_0_FULL**:
  - M6 closes ✅
  - G15 (Φ_symp residual) closes ✅
  - G22 (V_quad → P_III(D_6) canonical-form normalization map at
    108-digit canonical-form precision NOT written out) closes ✅
  - op:cc-formal-borel residual resolves ✅
  - M9 gating reduces from {M4-with-formal-baseline-+-structural-
    roadmap, M6} to {M4-only}
  - Once T1 Phase 3 lands (parallel-safe per Q35; closes M4 leg),
    M9 → {} and **SIARC-MASTER-V0 becomes announceable**
  - Picture v1.17 should be drafted to absorb both verdicts

If the post-fire verdict is **UPGRADE_V1_0_PARTIAL_NUMERICAL**:
  - M6 closes structurally (Phase E CC-NOTE v1.0 citable artifact
    drafted); G22 partial; op:cc-formal-borel partial
  - M9 gating remains {M4, M6-numerical-cross-check-residual} but
    the remaining residual is well-bounded and refire-able once
    additional Stokes-data literature is acquired

If the post-fire verdict is **HALT_M6_***:
  - M6 stays partial; H4 verdict remains in V_quad native form
    only
  - Specific structural gap surfaced; refire path identified
  - Picture v1.16 carries forward with M6 partial; v1.17 cycle
    delayed pending halt resolution

## Anomalies and open questions

**None at deposit time.** All anchor PDFs verified via SHA. All
synthesizer rulings explicitly embedded. All hygiene rules
consistent with prior cycles.

Carry-forward observations from R5-OKAMOTO-NUMDAM-RETRY (now
embedded in spec):
  - Okamoto 1987 (slot 07) uses **W(B_2) affine-Weyl** framework
    (3 generators); Barhoumi-Lisovyy 2024 (slot 08) uses **W(D_6)
    affine-Weyl** framework (7 generators per Sakai 2001 surface
    classification). These describe the same Painlevé III modulo
    a known type-correspondence. Phase B.5 is the explicit
    cross-walk, captured as a mandatory pre-step before Phase B's
    canonical-form map M is finalized. Without B.5, Phase B's
    map could be subtly inconsistent with the modern Sakai
    classification convention used throughout Phase C anchoring.

Note for synthesizer QA review:
  - Phase D.2 numerical cross-check has a "precision floor
    floats" framing (success threshold = "agreement at the
    precision floor Barhoumi-Lisovyy 2024 provides" rather than
    an absolute digit count). This avoids spurious
    HALT_M6_STOKES_NUMERICAL_MISMATCH triggers when the
    literature value is only known to N < 30 digits.
  - The precise digit count of agreement (Phase D.2) becomes
    the **NUMERICAL_CROSS_CHECK_DIGITS** field in the §7
    STANDING FINAL STEP output to chat — operator-readable, AEAL-
    auditable, distinct from the 108-digit V_quad native value.

## What would have been asked (if bidirectional)

  - "Should Phase D.2 use the H4 mpmath dps=250 cached value or
    re-run `median_resurgence.py` to a target precision?" → Spec
    answer: cite cached value at dps=250 (n=5000 closed-form
    recurrence already establishes the 108-digit measurement
    AEAL-honestly; no re-run needed for canonical-form match;
    re-run only triggered if HALT_M6_STOKES_NUMERICAL_MISMATCH
    surfaces and operator decides to pursue precision-floor
    diagnostic). Captured in Phase D.2.

  - "Should Phase E's CC-NOTE v1.0 deposit cite D2-NOTE v2.1's
    mpmath build-script provenance directly, or replicate from
    H4?" → Spec answer: cite D2-NOTE v2.1's existing extraction
    (it already carries 108-digit measurement provenance); H4
    handoff and verdict.md provide direct AEAL-auditable
    references. Captured in Phase E.4.

  - "Should the pre-fire deposit include a copy of the relay-
    prompt body at `prompt_spec_used.md` in the future execution
    session, OR rely on the relay agent to write that itself in
    Phase 0.0?" → Spec answer: relay agent writes Phase 0.0
    output at fire time; deposit's `prompt_spec.md` is the
    authoritative source. Captured in Phase 0.0.

## Recommended next step

**Operator + synthesizer QA review of `prompt_spec.md`** following
the QA review checklist at the bottom of the spec
(post-` ``` ` block). Expected outcomes:

  (i) **Synthesizer accepts spec as drafted** → operator
      dispatches the spec body into a fresh Copilot CLI session
      → relay agent runs ~2-4 hr → verdict landed at
      `sessions/<fire-date>/CC-VQUAD-PIII-NORMALIZATION-MAP/`
      handoff.md

  (ii) **Synthesizer requests amendments** → re-draft this
       deposit with v1.1 amendment block; commit + push v1.1;
       re-review

  (iii) **Synthesizer identifies critical gap** → spec returns to
        drafting (this is the "redraft from scratch" outcome;
        unlikely given Q35 + R5 + A-01 + H4 inputs are all
        explicit)

In parallel (per Q35 ruling, no operator monitoring required for
either):
  - Wasow §X.3 OCR (gates T1 Phase 3 if outcome A of QS-PCF2-
    AFIT)
  - QS-PCF2-AFIT readback (already filed; awaiting picture v1.17
    absorption)

## Files committed

  - `prompt_spec.md` — synthesizer-drafted spec body (verbatim
    relay-prompt code block) + Notes 1–7 inlined + QA review
    checklist + bridge anchors
  - `handoff.md` — this file
  - `README.md` — 1-paragraph framing pointing at prompt_spec.md
    and handoff.md (per QS-3 / T1P2-DEPOSIT pattern)

## AEAL claim count

**0 entries** appended to claims.jsonl this session.

This is a deposit session, not an execution session. AEAL claims
will accrue at relay-agent fire time (≥ 16 expected per spec §3
breakdown). Per AEAL-honest provenance rule:

  - This deposit anchors the spec content + pre-fire chronology
    in bridge git history (commit hash + timestamp = AEAL
    provenance for the spec text itself).
  - Numerical claims will accrue when Phases A-F run.
  - Spec-content claims (e.g., "spec contains 9 phases", "spec
    halt codes = 8") are bookkeeping, not numerical findings;
    bridge git history is sufficient provenance.

## Bridge anchors

  - **This deposit:**
    `siarc-relay-bridge/sessions/2026-05-04/CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC/`
  - **Future execution session (TO BE OPENED at fire time):**
    `siarc-relay-bridge/sessions/<fire-date>/CC-VQUAD-PIII-NORMALIZATION-MAP/`
  - **Pattern precedents:**
      - `sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`
        (QS-2; 75 KB; synthesizer-drafted spec; Note 1–N pattern)
      - `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER-PROMPT-SPEC/`
        (T1P2-DEPOSIT; 22 KB; QS-3 pattern; **post-hoc** anchored)
  - **Anchor execution sessions:**
      - `sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/`
        (H4 verdict source: C = 8.127336795..., β = 0)
      - `sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/`
        (A-01 verdict: μ-units consistency)
      - `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/`
        (R5 SCENARIO B disposition + Phase B.5 motivation)
