# Handoff — T1-BIRKHOFF-PHASE2-LIFT-LOWER

**Date:** 2026-05-04 (JST) / session opened 2026-05-03
**Agent:** GitHub Copilot (VS Code) — model: Claude Opus 4.7 (Extra high reasoning)
**Session duration:** ~3.5 h (incl. compaction recovery)
**Status:** **COMPLETE — verdict UPGRADE_PARTIAL_FORMAL_LEVEL**

## What was accomplished

Executed all six phases (0.0, 0.5, A, B, C, D, F) of the T1 Phase 2 relay
(Phase E intentionally skipped — see §Anomalies below). Phase A
established the formal Newton-polygon baseline `A_naive ≤ d+1` for the
SIARC PCF Wallis recurrence at d ∈ {2, 3, 4} via the standard Wimp-
Zeilberger normal-case ansatz `y(n) ~ Γ(n)^μ γ^n n^ρ S(1/n)`. Phase B
extended the sweep to d ∈ [3, 8] with the same conclusion. Phase C
extracted verbatim B-T 1933 §§7-9 statements from the SHA-verified OCR
dump and verified the four C.2 sub-gates (non-resonance match,
non-degeneracy match, d-range applicability, μ-units consistency per
A-01). Phase D aggregated to **`UPGRADE_PARTIAL_FORMAL_LEVEL`**: B-T's
existence-and-factorization machinery applies to the SIARC stratum at the
formal/sectorial-realization level, but does NOT identify A = 2d
specifically — that lift requires P2.1+P2.2 (algebraic identification of
SIARC stratum as borderline/exceptional locus) + P2.3 (formal-to-analytic
sectorial upgrade), with Wasow §X.3 (Theorem 11.1) image-only on disk
and Adams 1928 NIA per A-01.

## Key numerical findings

- **Phase A baseline at d=2 α-direction**: `μ_dom = 2, μ_sub = −1,
  A_naive = 3` ⟹ recovers PCF-1 v1.3 §6 Theorem 5 lower branch (QL01–QL26
  A=3); does NOT recover V_quad upper branch A=4=2d
  (`phase_a_symbolic_derivation.py`)
- **Phase A baseline at d=3 α-direction**: `A_naive = 4 = d+1` vs.
  empirical PCF-2 v1.3 R1.1 `A_fit ≈ 6 = 2d` — DRIFT by 2 confirmed
- **Phase A baseline at d=4 α-direction**: `A_naive = 5 = d+1` vs.
  empirical PCF-2 v1.3 `A_fit ≈ 7.954 ≈ 8 = 2d` (σ=3.7e-3) — DRIFT by 3
- **Phase B sweep d ∈ [3, 8]**: across all three conventions
  (α/symmetric/δ) the borderline condition `deg_a = 2 deg_b` is NEVER
  met; SIARC stratum is in NORMAL case but exhibits BORDERLINE-case
  asymptotic A — structural lift needed
- **Phase C C.2 gate results**: all four sub-gates pass (with structural
  caveat at borderline locus on C.2.1)

## Judgment calls made

1. **Phase E (D2-NOTE-style upgrade artifact) skipped.** The relay §2
   Phase E condition is "UPGRADE_FULL or UPGRADE_PARTIAL with d-range ≥ 4".
   Our verdict UPGRADE_PARTIAL_FORMAL_LEVEL is the *formal-level* baseline
   only — not strong enough to ground a deposit-grade upgrade artifact.
   Drafting a T2-NOTE / B4-NOTE v1.0 at this stage would conflate the
   formal Newton-polygon baseline with proof-grade closure; better to
   wait for T1 Phase 3 (Wasow §X.3 OCR + sectorial upgrade) before
   producing a citable artifact.

2. **No Adams 1928 acquisition surfaced.** Phase 2 did not depend on
   Adams's original argument beyond what was transitively covered by B-T
   1933; per A-01 verdict, this was expected. No `HALT_T1P2_ADAMS_GAP`.

3. **OCR mojibake in PowerShell display tolerated.** The Python script
   stdout under `cp1252` console produces visual mojibake but the file
   contents are valid UTF-8. Verified file SHA-256 matches and content
   is correct in editor. Did not invest in console encoding fixes
   (out-of-scope for math execution).

## Anomalies and open questions

1. **Phase E was conditionally skipped** (see Judgment Call #1).
   Operator decision: when T1 Phase 3 lands, can revisit drafting a
   T2-NOTE / B4-NOTE that combines Phase 2 baseline + Phase 3 sectorial
   upgrade.

2. **The empirical PCF-2 v1.3 R1.1 + R1.3 + Q1 result `A_fit ≈ 2d` at
   d=3,4 is unexplained by the Phase A naive baseline.** Two candidate
   explanations (non-mutually-exclusive):
   - (i) SIARC stratum is at borderline (q=2 fractional rank); to verify,
     need to compute Q_j(x) = ±B x^{1/2} + lower for the specific
     SIARC ansatz and check that the s-series matches.
   - (ii) The empirical A_fit measures something different from
     `μ_dom − μ_sub` (e.g., the Stokes constant exponent on log Q_n
     rather than n log n). To verify, need to read PCF-2 v1.3 §-of-fit
     for the exact A_fit definition.
   This open question is the critical input to T1 Phase 3.

3. **Phase A's analysis used the standard Wimp-Zeilberger 1985
   normal-case formula** without symbolically working through the
   borderline-case anormal ansatz. This is a deliberate scoping choice
   — the borderline-case symbolic derivation is itself the heart of P2.1
   and P2.2, and would require ≥4-6 h of symbolic work plus primary
   reading of B-T 1933 §1 anormal-case definition. Deferred to Phase 3.

4. **Internal literature consistency between A-01 verdict and Phase A
   baseline finding is OK.** A-01 verified μ-units share across
   Wasow/Birkhoff/B-T/Adams (no factor-of-2 ambiguity at *normalisation*
   level). Phase A factor-of-2 gap is a *case-distinction* gap (normal
   vs. borderline / anormal), not a normalisation gap. A-01 does not
   close the case-distinction question; Phase 2 surfaces it.

## What would have been asked (if bidirectional)

1. **Should Phase A attempt the two-layer ansatz** (rubber-duck
   pre-execution recommendation: edge characteristic for Q first, then
   indicial for ρ AFTER Q is fixed)? Default = no, ran naive baseline;
   the two-layer ansatz at borderline is exactly Phase 3 scope.

2. **Is the empirical A_fit = 2d at d=3,4 measuring the n log n
   coefficient or the log Q_n coefficient?** Affects which baseline
   match is the right comparison. Need PCF-2 v1.3 source-side reading.

3. **Should Phase E be drafted at this verdict level?** Defaulted to no
   (see Judgment Call #1).

## Recommended next step

**T1 Phase 3** — sectorial-upgrade closure. Tasks:
1. Read PCF-2 v1.3 R1.1+R1.3+Q1 source for exact A_fit definition.
2. Acquire OCR-readable Wasow §X.3 (Theorem 11.1) — current PDF image-only.
3. Symbolic borderline-case ansatz: derive Q_j(x) = ±B x^{1/2} + lower
   for SIARC stratum; verify B = √(c_a) (consistency with PCF-1 §6
   Theorem 5 lower-branch transition); identify exceptional locus where
   formal A bumps from d to 2d.
4. Sectorial upgrade via Wasow §X.3 (Theorem 11.1) — formal Borel
   transform convergence in sector of opening > π/(2d).

This is **Tier 2 work** per relay §8; defer scheduling to v1.16 cycle.

## Files committed

| File | SHA-256 | Size (B) |
|------|---------|---------|
| `prompt_spec_used.md` | `b8e806b1d080b4abcc1758af70d2dace92fab00c21b7c40e02b5b569c42d080b` | 4502 |
| `phase_a_symbolic_derivation.py` | `2fc6e39267768791912cc53aa59bc231c40483a1a93e92104b13f07809f16248` | 12329 |
| `phase_a_run_output.txt` | `732a0a82dccdc824db512b34ebb5eac37544c1801474eae1ebb76c3e24b64d25` | 13903 |
| `phase_a_findings.json` | `1c1038850da5a005d4078a276d4538fab894d44196450e557935816384a18b70` | 4561 |
| `phase_a_summary.md` | `71cac875c98a6ce8e0e2e161b3d4734741565a5119d4d0cafd6185b04fecf8ba` | 6266 |
| `phase_b_extended_sweep.py` | `39e98db607a5331686cf4ba4890bc50abc1232e8b533b80eeb2d4636c8e10175` | 6142 |
| `phase_b_run_output.txt` | `6556a069e3a8f1745a538a15500ba33afa98839ffe8a6f887a6e4fe840d9c6df` | 4438 |
| `phase_b_findings.json` | `a80a405901680f265d9de2f0d73f51a1d69627850b227159d43a1ab5381f2a03` | 7585 |
| `phase_c_literature_verification.md` | `c6cc2b1ac437647f2cad974b07462cc43422eaa71cc079f8a76e3cc32808ae93` | 9283 |
| `phase_d_verdict.md` | `7145a00d62b9716c735ed56b0d342c5a1d4cfa7c9da6bd675219b0ce662c65c5` | 6862 |
| `claims.jsonl` | (see file) | (see file) |
| `handoff.md` | this file | (this file) |

## AEAL claim count

**16 entries** written to `claims.jsonl` this session
(target was ≥ 14 per relay §3; achieved 16 = baseline + 2):

- Phase 0.0/0.5 provenance: 2 entries (P0_PROVENANCE, P05_BIBKEY_PREFLIGHT)
- Phase A: 3 entries (PA_DEG2_ALPHA_BASELINE, PA_DEG3_ALPHA_BASELINE,
  PA_DEG4_ALPHA_BASELINE)
- Phase B: 4 entries (PB_SWEEP_D3, PB_SWEEP_D4, PB_SWEEP_D5_TO_D8,
  PB_NONDEGENERACY_HOLDS)
- Phase C: 5 entries (PC_BT_SECTION_LOCATOR, PC_BT_THEOREM2_VERBATIM,
  PC_BT_FUNDAMENTAL_THEOREM_VERBATIM, PC_BT_SECT11_THEOREM3_VERBATIM,
  PC_GATES_C21_TO_C24)
- Phase D: 2 entries (PD_VERDICT_UPGRADE_PARTIAL_FORMAL_LEVEL,
  PD_STRATEGIC_IMPLICATION)

## Standing Final Step §H output

```
BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/

CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/handoff.md

VERDICT: UPGRADE_PARTIAL_FORMAL_LEVEL

ANOMALIES:
  1. Phase E skipped (verdict not strong enough for deposit-grade artifact)
  2. Empirical A_fit = 2d at d=3,4 unexplained by Phase A baseline; resolution
     candidates (borderline q=2 OR different A_fit definition) deferred to T1
     Phase 3
  3. Phase A used naive Wimp-Zeilberger normal case (not borderline two-layer
     ansatz); deliberate scoping choice
  4. Internal literature consistency A-01 vs Phase A is OK (case-distinction
     gap, not normalisation gap)

STRATEGIC_IMPLICATION:
  M4 → EMPIRICAL d=3,4 + LIT BRACKET A in [d, 2d] + FORMAL BASELINE A_naive ≤ d+1
       + STRUCTURAL FRAMING of P2.1+P2.2+P2.3 lift
  M9 gating → {M4-partial, M6} (unchanged in gating substance)
  H1 → PHASE_2_GATED RETAINED (Phase 2 produces baseline + structural framing,
       not closure)
```
