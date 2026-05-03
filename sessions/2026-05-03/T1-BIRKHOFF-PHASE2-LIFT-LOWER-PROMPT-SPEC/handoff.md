# Handoff — T1-BIRKHOFF-PHASE2-LIFT-LOWER-PROMPT-SPEC

**Session:** spec-deposit (NOT relay execution)
**Date:** 2026-05-04 (JST)
**Pattern:** QS-2 / QS-3 (synthesizer-spec deposit ahead of relay agent
  firing; this instance is **post-hoc** because the relay fired before
  the parallel deposit landed)
**Source:** synthesizer chat 2026-05-03 (operator-side relay paste
  timestamp 2026-05-04T06:53:26.787+09:00)

## Scope

This deposit anchors the synthesizer-drafted **T1-BIRKHOFF-PHASE2-LIFT-LOWER**
prompt spec at deposit time. Phase 2 of T1 lifts the upper bound
`A ≤ 2d` for Conjecture B4 at d ≥ 3 via non-resonance / non-degeneracy
of the Birkhoff-Trjitzinsky reduction at irregular singularities of
fractional rank q. Anchors: D2-NOTE v2.1, A-01 verdict, B-T 1933 §§7-9,
Wasow §19 (Theorem 19.1, eq. 19.3), v1.15 strategic picture, T1 Phase 1
dossier (descendants synthesis matrix + gap proposition for d ≥ 3).

## Expected verdict ladder (synthesizer pre-fire estimate)

The synthesizer-drafted spec §6 OUTCOME LADDER lists:

- **UPGRADE_FULL_d_LE_d_max** — best case; M4 ✅ closes; M9 gating
  reduces from {M4, M6} to {M6 only}; H1 → PROVEN at d ≥ 3.
- **UPGRADE_PARTIAL_d_LE_d*** — d-range bounded; M4 partial.
- **UPGRADE_PARTIAL_PAGECOUNT** — Phase E build at non-canonical
  page range.
- **HALT_T1P2_*** (8 specific halts) — see spec §4.

## Actual verdict (post-fire, AEAL-honest)

The relay agent fired this spec **before** this deposit was committed.
Execution session: `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/`
(bridge commit `37c939f`, parent `62c917d`). Result:

- **Verdict:** `UPGRADE_PARTIAL_FORMAL_LEVEL`
- **Strategic implication:** M4 stays partial (EMPIRICAL d=3,4 + LIT
  BRACKET A ∈ [d, 2d] + FORMAL BASELINE A_naive ≤ d+1 + STRUCTURAL
  FRAMING of P2.1+P2.2+P2.3 lift); M9 gating remains {M4-partial, M6};
  H1 retains PHASE_2_GATED label.
- **Reason** (per execution session `phase_d_verdict.md`):
  Phase A naive Wimp-Zeilberger Newton-polygon analysis recovers the
  d=2 lower branch (A=3 = d+1, α-direction) matching PCF-1 v1.3 §6
  Theorem 5 lower branch (QL families) but does NOT recover V_quad
  upper branch (A=4=2d) nor empirical A=2d at d∈{3,4}. Phase B sweep
  d∈[3,8] confirms baseline. Phase C extracts B-T 1933 §§7-9 verbatim;
  4/4 sub-gates pass with structural caveat. The literature provides
  existence/factorization machinery (Theorem II §7, Fundamental
  Theorem §9, Theorem III §11) but does NOT identify A=2d for SIARC
  stratum specifically — that requires P2.1+P2.2 (algebraic
  identification of SIARC stratum as borderline/exceptional locus
  with `deg_a = 2 deg_b` of Wimp-Zeilberger 1985) + P2.3 (sectorial
  upgrade via Wasow §X.3 (Theorem 11.1) / Adams 1928 / Turrittin /
  Immink, all NIA or image-only this session).

The `UPGRADE_PARTIAL_FORMAL_LEVEL` verdict label is a sub-tier of the
spec's UPGRADE_PARTIAL ladder rung — the lift was achieved at the
formal Newton-polygon baseline level (lower bound of the bracket
recovered) but not at the proof-grade analytic level (upper bound
A=2d not closed).

## Strategic implication of UPGRADE_FULL (had it landed)

The spec §0 framed UPGRADE_FULL as the gate for:

- **M4** (Conjecture B4 at d ≥ 3 proof-grade) → ✅ CLOSED
- **M9 gating** {M4, M6} → {M6 only}
- **H1** PHASE_2_GATED → PROVEN at all d ≥ 3

The actual UPGRADE_PARTIAL_FORMAL_LEVEL outcome leaves all three
unchanged in substance, matching the rubber-duck pre-fire prediction
(β) and the v1.15 picture's PHASE_2_GATED label. The deferred
closure is the recommended **T1 Phase 3** task (Tier 2; v1.16 cycle).

## Recommended firing time (had spec not yet been fired)

- **Runtime:** ~3-5 hr autonomous CLI agent (no operator monitoring
  required after fire)
- **Compute:** medium-high (literature reading + symbolic derivation
  + verdict drafting)
- **Parallelism:** parallel-safe with any task NOT touching M4
  closure path
- **Pre-fire checks:**
  (i) literature PDFs SHA-verified at
      `tex/submitted/control center/literature/g3b_2026-05-03/`
      (4/4 verified — Birkhoff 1930, B-T 1933, Wasow 1965,
      Costin 2008)
  (ii) T1 Phase 1 dossier on bridge (already there, commit bbc905d
       amendment)
  (iii) A-01 verdict landed (already, 2026-05-03)
  (iv) v1.15 picture sealed (already, commit 62c917d)
  (v) D2-NOTE v2.1 deposited (Zenodo DOI 10.5281/zenodo.20015923,
      published 2026-05-04 ~07:00 JST — landed AFTER Phase 2 relay
      execution but BEFORE this deposit)

All pre-fire checks pass.

## Anchors

| Anchor | Path / DOI | Purpose |
|--------|-----------|---------|
| D2-NOTE v2.1 | Zenodo `10.5281/zenodo.20015923` | universality-radius result Phase 2 lift extends |
| A-01 verdict | `sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/handoff.md` | μ-units consistency Wasow/Birkhoff/B-T/Adams |
| B-T 1933 PDF | `literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf` SHA `dcd7e3c6...` | §§4-6 Borel summability + §§7-9 non-resonance |
| Wasow 1965 PDF | `literature/g3b_2026-05-03/04_wasow_1965_dover.pdf` SHA `f59d6835...` | §X.3 (Thm 11.1) + §19 (Thm 19.1, eq. 19.3) |
| T1 Phase 1 dossier | `sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/` | gap proposition + descendants synthesis matrix |
| v1.15 picture | `tex/submitted/control center/picture_revised_20260503.md` SHA `89B12CC9...` | strategic context for M4 / M9 / H1 |

## Note on QS-2 / QS-3 deposit pattern

QS-2 (D2-NOTE-V2-1-WASOW-FULL-CLOSURE) and QS-3 (subsequent QS-class
relay) established the convention of depositing a synthesizer-drafted
spec to bridge **before** firing. This anchors the spec at deposit
time independent of execution-session AEAL provenance. The chronology
this time is reversed (relay fired first; deposit landed second);
this handoff records that fact for AEAL honesty.

## Bridge anchors

- **Spec-deposit session (this):**
  `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER-PROMPT-SPEC/`
- **Execution session (already landed):**
  `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/`
  (bridge commit `37c939f`)
- **Related deposit pattern precedents:**
  - QS-2: `sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`
  - QS-3: (referenced by spec §0)
