# Phase D — Verdict Aggregation

**Task:** T1-BIRKHOFF-PHASE2-LIFT-LOWER, Phase D
**Date:** 2026-05-04 (JST)

## Phase signals (input to Phase D aggregation)

| Phase | Signal | Detail |
|-------|--------|--------|
| 0.0 | `PROVENANCE_WRITTEN` | `prompt_spec_used.md` on disk |
| 0.5 | `BIBKEY_PREFLIGHT_PASS` | All anchors (`BirkhoffTrjitzinsky1933`, `Wasow1965`, `Adams1928`, `Costin2008`, `Immink1984`, etc.) already exist in `bibliography_pass1.bib`; no new bibkeys introduced |
| A | `A_INDICIAL_BASELINE_RECOVERED_LOWER_BOUND_ONLY` | Naive Newton-polygon recovers d=2 lower branch (A=3) but NOT V_quad upper branch (A=4) nor d≥3 empirical (A=2d) |
| B | `B_BORDERLINE_NOT_MET_BY_NAIVE_ANSATZ` | Sweep d ∈ [3, 8] confirms baseline; SIARC stratum sits in NORMAL case, not BORDERLINE; lift to 2d structural |
| C | `C_LITERATURE_UNIFORM_AT_NORMAL_CASE` | All four C.2 sub-gates pass; B-T §§7–9 provide existence-and-factorization machinery; **do NOT identify A=2d for SIARC stratum specifically** |

## Verdict ladder mapping (per relay §2 Phase D)

The relay §2 Phase D maps:
- D.1 — A_VERIFIED + B_VERIFIED at d ∈ [3, d_max] + C_LITERATURE_UNIFORM
        → **UPGRADE_FULL_d_LE_d_max**
- D.2 — partial (e.g., B fails at d* > 3) → **UPGRADE_PARTIAL_d_LE_d*−1**
- D.3 — A halts → HALT_T1P2_INDICIAL_DRIFT
- D.4 — B halts → HALT_T1P2_NONRESONANCE_FAILS_GENERIC
- D.5 — C halts → HALT_T1P2_LITERATURE_NOT_LANDED or HALT_T1P2_LITERATURE_DISAGREES_WITH_012
- D.6 — all pass but d-range bounded → UPGRADE_PARTIAL

In our case:
- A and B both produce **structural-baseline** signals — not full
  verifications, not hard halts. The naive analysis recovers the LOWER
  bound A_naive ≤ d+1; the lift to A = 2d is the structural P2.1+P2.2+P2.3
  gap that Phase 1 already identified (cf. `gap_proposition_for_d_ge_3.md`
  Q1.e and `bt1933_theorem_extraction.md` lines 209–228).
- C produces `C_LITERATURE_UNIFORM_AT_NORMAL_CASE` — the literature
  machinery applies to the SIARC stratum at the existence / sectorial-
  realization level, but does NOT identify A = 2d.

This combination falls **between** D.1 (UPGRADE_FULL) and D.3/D.4 (HALT).
It is **UPGRADE_PARTIAL** at the *formal level*, with the lift from
formal A_naive to analytic A=2d structurally framed (not closed).

## Phase D verdict

> **VERDICT: `UPGRADE_PARTIAL_FORMAL_LEVEL`**
>
> Phase A + B establish the formal Newton-polygon baseline A_naive ≤ d+1
> (naive Wimp-Zeilberger normal case), recovering only the LOWER end of
> the literature bracket A ∈ [d, 2d]. The lift to **A = 2d** at d ≥ 3
> requires the SIARC PCF stratum to sit at the BORDERLINE case
> `deg_a = 2 deg_b` of Wimp-Zeilberger 1985 (equivalently, the anormal /
> fractional rank q ≥ 2 case of B-T 1933 §1) OR at an exceptional locus
> of the normal case where leading coefficients cancel.
>
> Phase C confirms B-T 1933 §§7–9 provide the existence / factorization /
> sectorial-realization machinery applicable to the SIARC stratum. The
> machinery does NOT identify A = 2d specifically — that requires:
>
> 1. **Identification (P2.1+P2.2):** algebraic argument that the SIARC
>    stratum at d ≥ 3 lies on the borderline / exceptional locus.
> 2. **Sectorial upgrade (P2.3):** formal-to-analytic lift via Wasow §X.3
>    (Theorem 11.1) / Adams 1928 / Turrittin 1955 / Immink 1984. **Wasow
>    PDF on disk is image-only (NO OCR), Adams 1928 NIA per A-01 verdict,
>    Turrittin/Immink not acquired.** This is a session-level limitation,
>    not a closed gap.
>
> Phase 2 of T1 is therefore **partially completed** at the AEAL-honest
> formal-symbol level: the Newton-polygon baseline + the structural
> declaration of where the lift to A = 2d sits. The full analytic-upgrade
> closure is **deferred** to a follow-on T1 phase (Phase 3) requiring
> primary literature acquisition for OCR-readable Wasow §X.3 and/or
> Adams 1928, or for a primary Turrittin / Immink reading.

## Strategic implication

| Element | Pre-Phase 2 | Post-Phase 2 |
|---------|------------|--------------|
| **M4** (Conjecture B4 at d ≥ 3 proof-grade) | EMPIRICAL d=3,4 + LIT BRACKET A ∈ [d, 2d] | **EMPIRICAL d=3,4 + LIT BRACKET A ∈ [d, 2d] + FORMAL BASELINE A_naive ≤ d+1 + STRUCTURAL FRAMING of P2.1+P2.2+P2.3 lift** |
| **M9** gating | {M4, M6} | {M4-partial, M6} (unchanged in gating substance) |
| **H1** label | PHASE_2_GATED | **PHASE_2_GATED** (unchanged; Phase 2 produces baseline + structural framing, NOT closure) |

The picture v1.15 PHASE_2_GATED label on H1 is **correct and retained**
post-Phase 2. The Phase 2 deliverable is a **sharpened structural
declaration of the gap**, not closure of the gap.

## Anomalies surfaced (for next-task recommendation)

1. **A-01 verdict + Phase A baseline coexistence is consistent**: A-01
   confirmed μ-units share across Wasow/Birkhoff/B-T/Adams (no factor-of-2
   ambiguity at *normalisation* level). Phase A then establishes
   A_naive = d+1 (α-direction) ≠ 2d at d ≥ 3. The factor-of-2 gap is
   NOT a normalisation issue (per A-01); it is a *case-distinction* issue
   (normal vs. borderline / anormal). This is consistent — A-01 does not
   close the case-distinction question.

2. **Phase 1 dossier `bt1933_theorem_extraction.md` Q1.e was correct**:
   "B-T proves A = 2d for SIARC at all d" is FALSE. Phase 2 confirms
   this with §§7–9 OCR-verbatim extracts.

3. **The empirical PCF-2 v1.3 R1.1 + R1.3 + Q1 result A_fit ≈ 2d at
   d=3,4** is unexplained by Phase A baseline. Two non-mutually-exclusive
   hypotheses for follow-on:
   (i)  SIARC stratum is at borderline (q=2 fractional rank). To verify,
        need to compute the explicit Q_j(x) in the s-series ansatz and
        check for fractional powers x^{1/2}.
   (ii) The empirical A_fit measures a different ratio than μ_dom − μ_sub
        (e.g., it could be the Stokes constant exponent on log Q_n
        instead of on n log n). To verify, need to read PCF-2 v1.3 source
        for the exact A_fit definition.

## Next-task recommendation

**Recommended follow-on: T1 Phase 3 (sectorial-upgrade closure)**
- Acquire OCR-readable Wasow §X.3 (Theorem 11.1) — currently image-only.
- Verify PCF-2 v1.3 A_fit definition (which expansion coefficient is
  being measured by the high-precision tail-window fit).
- If borderline-case identification (P2.1) holds: Phase 3 derives
  Q_j(x) = ±B x^{1/2} + lower; verifies B = √(c_a) (consistency with
  PCF-1 §6 Theorem 5 lower branch); shows A = 2d at the formal level.
- If exceptional-locus identification holds instead: Phase 3 derives
  the algebraic condition + verifies the SIARC stratum is on it.

This is **Tier 2 work** — defer to v1.16 cycle per relay §8.
