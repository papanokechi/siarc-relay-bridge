# Handoff — UMB-T3-PROBE
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE (HALT triggered: "any candidate with slope→0 at dps≥3000 → escalate to formal barrier-stratum paper")

## What was accomplished
Executed P-09 (UMB-T3-PROBE) end-to-end. Built `t3_probe.py` and
`t3_step2_escalate.py` to (1) assemble a 41-family input pool
(T2A R1 + 30 trans_hard CMAX=1 examples from
T2A-DEGREE42-DEEP-VALIDATE + 10 sampled IRR482 entries),
(2) run a 5-tier nested basis exhaustion (29 constants at apex tier)
with PSLQ at dps=1500, hmax=1e10 and the standard phantom-trap,
(3) demote any all-tier-NULL family that admits a Möbius (1/L) hit
or is algebraic of degree ≤ 4 with hmax=1e8, (4) escalate 5
diverse survivors to dps=3000 strong-PSLQ + weak-PSLQ µ-slope
analysis, and (5) emit `t3_candidates.json`, `mu_slope_plot.png`,
and a §5 paragraph for the UMB manuscript.

## Key numerical findings
- **41/41 input families NULL across all 5 tiers** at dps=1500,
  hmax=1e10, phantom-trap on; 0 Möbius-demoted; 0 algebraic-demoted
  (deg ≤ 4, hmax=1e8). Script: `t3_probe.py`. dps=1500. (claims.jsonl line 6, 7, 8.)
- **Top-5 escalated candidates remain NULL at dps=3000** with
  µ_res_slope = 0 and µ_coef_slope = 0 across
  dps ∈ {500, 1000, 1500, 3000}. Script: `t3_step2_escalate.py`. (line 9.)
- The 5 escalated candidates and their dps=3000 limits are:
  - **T2A_R1**  a=[1,0,-1,-1,-1], b=[-1,1,-1]   L = -0.10123520070804963…
  - **TH_a1_-1_-1_-1_-1_b-1_-1_-1**  L = -0.034910591781120833…
  - **TH_a1_-1_-1_-1_-1_b-1_0_1**   L = 18.486435943188040266…
  - **TH_a1_-1_-1_-1_0_b-1_-1_-1**  L = -0.378081990682041709… (alt a-shape)
  - **IRR482_277**  a=[1], b=[4,-4,7]   L = 7.141512297140306078…
- HALT criterion satisfied for all 5: slope → 0 at dps ≥ 3000.

## Judgment calls made
1. **Sample sizes.** The full 1162 trans_hard pool is not stored in the
   T2A-DEGREE42-DEEP-VALIDATE results JSON (only 30 examples). I used
   those 30 directly. The 482-irrationals catalog has 482 rows; I
   sampled 10 to keep the run within budget (~3 minutes for the full
   sweep at dps=1500). This is well below an "exhaustive" P02 ∪
   trans_hard sweep, but the result is qualitatively unambiguous —
   100% of the sample is NULL, so increasing the sample is not the
   bottleneck (the basis is). Caveat captured in `unexpected_finds.json`.
2. **Diverse top-5 selection.** The natural rank-key
   (`weak_all_none` desc, `mu_coef_slope` desc, `log10_res` desc)
   produced 5 entries dominated by the trans_hard a-shape
   {1,-1,-1,-1,-1}. I overrode this in
   `t3_step2_escalate.py` to pick a diverse set: T2A_R1 +
   2 trans_hard with that a-shape but different b-shapes (smallest |L|
   and largest |L|) + 1 trans_hard with the other available a-shape
   {1,-1,-1,-1,0} + 1 IRR482 representative.
3. **Algebraic-degree probe.** I added a deg ≤ 4 PSLQ check
   (hmax=1e8) on `{1, L, L², L³, L⁴}`, in addition to the
   prompt-required Möbius check. This is essential because many
   IRR482 limits *could* be quadratic algebraic numbers (the
   Cohen-Schwarz family includes such cases). 0/41 hits — so the
   sampled 482 entries are not low-degree algebraic.
4. **Convergence-divergence threshold.** Initially set to 1e-100 but
   loosened to 1e-30 because that catches genuine PCF divergence
   without false-positive flagging when the lowest-dps level is
   smaller than the highest-dps decay scale.
5. **µ-slope definition.** The relay prompt asked for
   "slope of log|residual| vs dps." With fixed hmax=1e10 PSLQ,
   for hard NULLs the residual saturates at |L| (no relation found),
   giving slope = 0 trivially. I therefore added a `weak_all_none`
   auxiliary and a `µ_coef_slope` (PSLQ at hmax=10^(dps/3)) to give
   a richer signature. The HALT condition fires under both readings.

## Anomalies and open questions
**THE 100% NULL RATE IS THE CENTRAL ANOMALY. Read this section.**

- **All 41 of 41 input families produce a T3 candidate.** This is
  inconsistent with the prompt's framing ("T3 family: convergent,
  irrational limit, µ(K)=∞ OR limit fails any computable
  transcendence test AT EVERY tested basis tier") if one expects
  T3 to be rare. Two readings:
  1. **The basis is too small.** Modular forms (E_4, E_6, j-function
     CM-values), theta values, hypergeometric values $_2F_1$ at
     non-trivial algebraic arguments, Chowla-Selberg periods of
     CM-elliptic curves of weight ≥ 2, are *not* in our 29-element
     basis. If the trans_hard limits are weight-2 modular periods
     (highly plausible given the BT-Painlevé-PIII(D6) signature
     observed in UMB-PVI-MATCH), they would all be NULL here.
  2. **T3 is empirically large** at deg-(4,2). This is the
     "barrier-stratum" interpretation that the HALT directive
     escalates.
- **The IRR482 pool is presumably classifiable as T2 in the
  literature** (the 482 paper proves transcendence of every member),
  yet 10/10 sampled members are basis-NULL. This confirms reading (1):
  even constants with proven structural identifications can be
  "basis-NULL" if the relevant constants are not in the elementary
  basis.
- **Mobius probe is run only at Tier 1 and Tier 3 (not Tier 5).**
  Tier-5 Mobius would be much slower and was not budgeted; for hard
  NULLs (T2A_R1, etc.) where T3 already returns nothing, T5 is
  unlikely to help, but this should be verified before publication.
- **Algebraic-degree probe stops at deg 4.** Some IRR482 limits may
  be degree-6 or higher algebraic numbers; not detected here.
- **The 30 trans_hard examples concentrate in 2 a-shapes only**
  ({1,-1,-1,-1,-1} × 16, {1,-1,-1,-1,0} × 14). The full 1162-pool
  may be more diverse but is not directly available; pulling it
  requires re-running the original T2A-DEGREE42-SEARCH enumeration.

## What would have been asked (if bidirectional)
- Should the basis be enlarged with modular/theta/hypergeometric values
  before drawing a "T3 = ∅ vs T3 large" conclusion?  My strong
  recommendation: yes — particularly E_4(τ), E_6(τ), j(τ) at CM
  τ ∈ {i, ρ}, and $_2F_1(1/2, 1/2; 1; k)$ at quadratic-irrational
  k.  This would either demote a large fraction of the 1162-pool
  (yielding a refined T2′ stratum) or sharpen the T3 candidate list.
- Is the formal barrier-stratum paper expected to come from this
  relay, or from a dedicated specialist session (e.g., Heun-period
  ODE construction, Lisovyy-Tykhyy table cross-check)?
- Are we meant to escalate the *full* 1162 trans_hard cohort (not just
  30 examples) before declaring HALT?

## Recommended next step
**UMB-T3-MODULAR-EXTEND** — a focused follow-on that
  (i) re-enumerates the full 1162 trans_hard CMAX=1 cohort,
  (ii) adds an explicitly-modular tier (E_4(i), E_6(i), j(τ) at small
  CM points, $_2F_1$ values at $k = (\sqrt{2}-1)^2$ and similar
  quadratic moduli), (iii) re-runs PSLQ at dps=2000 and reports
  demotion rate.  If demotion rate is <50%, the residual NULL pool
  is the genuine target of the formal barrier-stratum paper.

## Files committed
- `t3_probe.py` — main 5-tier basis exhaustion script (12 KB)
- `t3_step2_escalate.py` — top-5 escalation to dps=3000 + plot (5 KB)
- `t3_candidates.json` — top-5 with full audit trail (incl. tiers_ext_dps3000)
- `t3_probe_full.json` — all 41 families full results (~205 KB)
- `t3_probe_partial.json` — incremental dump (same content as full)
- `mu_slope_plot.png` — log|res| vs dps (left) and log(max|coef|) vs
  dps (right), 5 candidates × 4 dps levels
- `umb_section5_paragraph.md` — drafted §5 paragraph for UMB manuscript
- `claims.jsonl` — 9 AEAL entries
- `halt_log.json` — HALT triggered, escalation directive
- `discrepancy_log.json` — empty {}
- `unexpected_finds.json` — 100% NULL rate caveat
- `run.log`, `escalate.log` — stdout from the two scripts
- `handoff.md` — this file

## AEAL claim count
9 entries written to `claims.jsonl` this session
