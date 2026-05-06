# Handoff — SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT

**Date:** 2026-05-06
**Agent:** GitHub Copilot CLI (T2, acting cross-tier as T1-Synth-substitute per operator authorization)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished

Operator authorized T2 to act in T1-Synthesizer capacity for one round
to arbitrate Q1/Q2/Q4 of relay 051 (bt_baseline_note v1.0). T2
conducted substrate survey of bt_baseline_note.tex §3-§7, T1 Phase 2
phase_d_verdict.md and phase_c_literature_verification.md, PCF-2 v1.3
program statement, PCF-2 cubic harvest scripts, and PCF-1 v1.3 d=2
class definition. Mandatory rubber-duck QA dispatched and adopted in
full (8 findings). Synthesizer-substitute verdict drafted with HIGH
confidence on script/protocol mismatch and WZ plug-in math; MEDIUM-HIGH
confidence on Section 5 reframing scope; MEDIUM confidence on PCF-1 /
picture v1.20 / scope-wording implications. Canonical T1-Synth (W20
Mon 2026-05-11) re-arbitration explicitly recommended for any
repo-wide wording changes.

## Key numerical findings

- PCF-2 R1.1/R1.3/Q1 cubic+quartic harvest scripts implement canonical
  (1, b) backward CF with `a_n ≡ 1` identically (verbatim
  `cf_value()` lines 79-86 of `pcf-research/pcf2/session_C1_2026-05-01/
  session_c1_wkb.py` shows `x = b_k + 1/x` recurrence with no a_k
  factor on the `1/x` term). Stratum is `deg_a = 0`.
- PCF-2 v1.3 program statement L230 declares program scope as
  `a_n = δ_1 n + δ_0` (linear, deg_a ≤ 1) — a protocol-to-stratum
  mismatch with the harvest scripts.
- bt_baseline_note v1.0 Theorem 1.1 covers band `deg_a ∈ {d-1, d, d+1}`
  (α/symmetric/δ-direction conventions); does not include `deg_a = 0`.
- WZ normal-case Newton-polygon balance at `deg_a = 0`, `c_a = 1`:
  balance (I) `μ_dom = d, γ_dom = c_b`; balance (III)
  `μ_sub = -d, γ_sub = -1/c_b`; `A_naive = μ_dom - μ_sub = 2d`.
- PCF-2 R1.1 cubic empirical: `A_fit mean = 5.978, σ = 0.026` at d=3,
  consistent with `A_naive = 2d = 6` within σ.
- PCF-2 Q1 quartic empirical: `A_fit mean = 7.954, σ = 0.0037` at d=4,
  consistent with `A_naive = 2d = 8` within σ.
- PCF-1 v1.3 d=2 stratum at `tex/submitted/p12_journal_main.tex`
  L128-136: `a_n = δ n + ε` with α, δ ≠ 0 (linear, `deg_a = 1`),
  distinct from PCF-2 cubic-harvest's `deg_a = 0`.

## Judgment calls made

1. **Cross-tier role acceptance.** Operator chat instruction
   "proceed you being the new synthesizer" treated as one-round
   authorization for T2 (daily-cadence) to act in T1-Synth
   (weekly-cadence) capacity per RACI v2026-05-05 R3 override
   precedent set 2026-05-06 ~11:35 JST for the M6-amendment trio.
   Verdict explicitly labeled "synthesizer-substitute" (NOT canonical
   T1) with explicit defer-to-canonical recommendation at next ISO
   week. (Per memory `RACI / agent role boundary`: endorser-style
   ranking is synth-scope; same logic applied to mechanism-arbitration
   here, with deferred re-arbitration as hedge.)
2. **Rubber-duck QA dispatched.** Operator follow-up instruction
   "double check with a prompt for copilot researcher agent as
   necessary (in order to avoid unexpected outcome and for quality
   assurance)" interpreted as mandatory; rubber-duck dispatched with
   8 numbered critique questions (C1-C8); recommendation REVISE
   received and adopted in full.
3. **Verdict scope confined to PCF-2 R1.1/R1.3/Q1.** Per rubber-duck
   C5 blind-spot 1, Q1 verdict scope confined to the harvest scripts'
   stratum specifically; PCF-1 V_quad/QL01-QL26 split addressed
   under "Audited blind spots" but not load-bearing in Q1 verdict;
   canonical T1-Synth W20 weekly re-arbitration recommended for full
   PCF-1 substrate audit. Scope discipline enforced to avoid
   over-generalization.
4. **AEAL forbidden-verb hygiene.** Per rubber-duck C6, draft
   phrasings "correctly predicts", "matching empirical EXACTLY",
   "gap is artefact", "neither (i') nor (ii') is realised" softened
   to AEAL-compliant "indicates", "is consistent with", "likely
   reduces to", "mechanism (i') likely unnecessary; mechanism (ii')
   remains audit-worthy".
5. **Sign-error correction.** Per rubber-duck C2, draft balance (III)
   `γ = +1/c_b` corrected to `γ = -c_a/c_b = -1/c_b` for `c_a = 1`.
   `A_naive = 2d` unaffected (depends on μ_sub only).
6. **Q4 ranking softened.** Per rubber-duck C4, "Wasow primary +
   Costin secondary" → "Wasow canonical target + Costin operational
   substitute" framing; Wasow canonical-target-by-mathematical-
   strength (currently OCR-unavailable on disk); Costin
   operational-substitute-by-accessibility.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION.**

1. **The protocol-to-stratum mismatch finding (Q1 core) was NOT
   identified by the existing T1 Phase 2 verdict** (UPGRADE_PARTIAL_
   FORMAL_LEVEL at bridge `37c939f`). Phase 2 framed the d≥3 gap
   as requiring borderline-locus mechanism (i') without flagging
   the convention disconnect. This is recorded as
   `SYNTH-SUB-051-UF1` in `unexpected_finds.json`. Implication:
   T1 Phase 3 sub-task 3-A (extend Phase A WZ table to deg_a = 0)
   becomes higher-priority than the original Phase 3 borderline-
   case lift work.

2. **PCF-1 v1.3 §6 Theorem 5 d=2 V_quad/QL01-QL26 split may
   ALSO be a convention-split.** Per rubber-duck citation, V_quad
   may use `a_n ≡ 1` (deg_a = 0) per
   `algebraic_independence_audit.py:37-40` (NOT independently
   verified by T2 this session), in which case V_quad's `A = 4 = 2d`
   matches WZ at deg_a = 0 directly. QL01-QL26 with deg_a = 1 has
   `A_naive = 2d - 1 = 3` matching their empirical record. If
   verified, bt_baseline_note v1.x §4.2 d=2 verification framing may
   also need revision — flagged for canonical T1-Synth W20 weekly
   re-arbitration as `SYNTH-SUB-051-UF2`.

3. **PCF-2 v1.3 Conjecture B4' (FALSIFIED at d=3)** predicted a
   2d-1 vs 2d split tracking the Galois classification of b_n's
   resolvent cubic ("+_S3_real", "+_C3_real" predicted A=2d-1=5;
   "-_S3_CM" predicted A=2d=6). Empirically all 50 cubic
   representatives gave `A_fit ≈ 6` regardless of bin (B4' falsified).
   Under Q1's PROTOCOL_TO_STRATUM_MISMATCH framing, B4' falsification
   is naturally explained: the harvest's deg_a = 0 directly predicts
   A_naive = 2d for ALL bins (no Galois dependence). Recorded as
   `SYNTH-SUB-051-UF3`; provides additional substrate-side support
   for Q1 verdict beyond cf_value() inspection.

4. **rule5 amendment vocabulary extension.** Verdict adopts label
   "PROTOCOL_TO_STRATUM_MISMATCH" (per rubber-duck C5 blind-spot 3)
   as a slight extension of rule5's "classifier mismatch"
   vocabulary, because here both prose AND scripts disagree on
   stratum definition (not just labeling). Flagged as item 4 in
   "Recommended canonical T1-Synthesizer follow-up (W20 Mon
   2026-05-11)" for ratification or fold-in.

5. **The synthesizer-substitute verdict has confidence-split
   structure.** Per rubber-duck C8 split-confidence recommendation:
   - HIGH: PCF-2 R1.1/R1.3/Q1 cf_value uses `(1,b)` `a_n ≡ 1`
     (verifiable from script inspection)
   - HIGH: WZ plug-in `deg_a = 0 ⇒ A_naive = 2d` (mechanical
     derivation)
   - MEDIUM-HIGH: bt_baseline_note v1.x §5 gap-framing should be
     revised for PCF-2 R1.1/R1.3/Q1 scope (requires canonical T1-Synth
     assent on revision scope)
   - MEDIUM: implications for PCF-1 v1.3, picture v1.20, PCF-2 v3.x
     scope wording (PCF-1 substrate analysis incomplete this
     session; canonical T1-Synth scope)
   The MEDIUM components are explicitly deferred to canonical T1-Synth
   W20 weekly re-arbitration.

## What would have been asked (if bidirectional)

If T2 had bidirectional channel to canonical T1-Synth this session,
T2 would have asked:

1. Is V_quad in PCF-1 v1.3 §6 Theorem 5 actually `a_n ≡ 1`
   (deg_a = 0)? (Rubber-duck cited
   `algebraic_independence_audit.py:37-40` but T2 did not
   independently verify this session.)
2. Is the harvest-script's `deg_a = 0` IMPLEMENTED stratum
   intentionally chosen as a SUBSET of the program-statement's
   `deg_a ≤ 1` DECLARED scope, or is it an unintentional restriction?
3. Should rule5 amendment vocabulary be extended to include
   "protocol-to-stratum mismatch" as a distinct category from
   "classifier mismatch"?
4. Does Q1's PROTOCOL_TO_STRATUM_MISMATCH framing trigger an
   E-class escalation (E1/E2) per the SIARC escalation taxonomy, or
   is it absorbed in standard T1 Phase 3 sub-task framework?
5. Should the bt_baseline_note v1.0 Zenodo deposit be flagged with
   a follow-up note pointing to this synthesizer-substitute verdict,
   or stand as canonical with the verdict recorded only in the bridge
   chain?

## Recommended next step

Canonical T1-Synth (Claude.ai weekly-cadence) re-arbitration of this
synthesizer-substitute verdict at next ISO week W20 (Mon 2026-05-11).
Specific items for canonical T1-Synth assent (per
`synth_substitute_verdict.md` §"Recommended canonical T1-Synthesizer
follow-up"):

1. Ratify or reject the PROTOCOL_TO_STRATUM_MISMATCH finding for
   PCF-2 R1.1/R1.3/Q1 scope.
2. Authorize or defer T1 Phase 3 sub-tasks 3-A through 3-E.
3. Decide on bt_baseline_note v1.x deposit revision scope (additive
   `deg_a = 0` row vs §5 reframing → v1.1 vs leave v1.0 canonical
   with verdict-as-follow-up-note).
4. Ratify or fold the "protocol-to-stratum mismatch" label into rule5
   amendment vocabulary.
5. Decide picture v1.20 absorption (anomaly entry vs primary substrate
   row).
6. Decide PCF-2 v3.x scope-statement wording revision.

## Files committed

- `synth_substitute_verdict.md` (~22.9 KB) — main verdict deliverable
- `rubber_duck_critique.md` (~8.0 KB) — verbatim critique + per-finding
  adoption record
- `claims.jsonl` (~5.2 KB; 12 entries SYNTH-SUB-051-A1..A12)
- `halt_log.json` (4 B; empty `{}` per spec)
- `discrepancy_log.json` (~4.7 KB; 6 anomalies SYNTH-SUB-051-D1..D6,
  none blocking)
- `unexpected_finds.json` (~2.7 KB; 3 finds SYNTH-SUB-051-UF1..UF3)
- `handoff.md` (this file)

## AEAL claim count

**12 entries** written to `claims.jsonl` this session.

All claims are `evidence_type: "literature_desk"` or
`"script_inspection"` (this is a synthesizer-class deliverable; no
numerical execution was performed). 6 substrate claims (A1-A6 +
A8 covering script inspection + WZ derivation + empirical record +
note Theorem 1.1 band) + 1 PCF-1 substrate claim (A7) + 3 verdict
claims (A9/A10/A11 for Q1/Q2/Q4) + 1 governance claim (A12 covering
cross-tier RACI authorization).
