# Handoff — T2C-PRECISION-ESCALATION-MONITOR
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~15 minutes
**Status:** COMPLETE (with UNEXPECTED FINDING; not halted)

## What was accomplished
Built and ran the Layer-5 Precision Escalation Monitor on 24 reference
Trans `-2/9` families (the F1-TRANS-STRUCTURE catalogue) plus 6 controls
(3 Log at ratio `-1/36`/`-1/49`, 3 simple Alg). For every family we
computed `L` at `dps ∈ {50,100,150,200,250,300}`, ran PSLQ at each level
against `{L, √2, √3, √5, √17, π, log2, ζ(3), 1}` with the phantom-hit
rule, fit `slope(log10(r), dps)`, and ran an additional dps=300 sweep
against the extended basis `{L, L², √17, π, log2, ζ(3), e, γ, 1}`. All
deliverables (scripts, JSON results, report, claims) are in
`t2c/` and copied here.

## Key numerical findings
- Slope is uniformly `-1.0` across all 30 families (Trans mean −0.999999,
  Log/Alg mean −1.0). Separation gap (min Trans − max Log) = 0.0.
  → **slope alone is NOT a reliable Trans-hard discriminator** on this
  training set; it is dominated by the residual floor `10^-dps`.
  Script: `t2c/precision_escalation.py`, dps≤300.
- The PSLQ-acceptance-pattern across dps IS a reliable discriminator:
  20 / 24 Trans families produced no L-bearing relation at any dps
  (Trans-hard signature); 4 / 24 produced the same relation at all dps.
- **dps=300 extended-basis sweep: 4 hits / 24** (prompt expected 0).
  Closed forms (verified at all six dps levels):
  - T08_130101 (a=[-2,-1,1], b=[0,-3,-3]): `L = -(π+2)/2`
  - T11_130117 (a=[-2,-1,1], b=[0, 3, 3]): `L =  (π+2)/2`
  - T14_143931 (a=[-2, 1,3], b=[0,-3,-3]): `L = -(3π+4)/4`
  - T21_143951 (a=[-2, 1,3], b=[0, 3, 3]): `L =  (3π+4)/4`
  Script: `t2c/pslq_sweep_300.py`. All four still transcendental
  via Lindemann–Weierstrass; Trans `-2/9` stratum unchanged.

## Judgment calls made
- Replaced the prompt's suggested 24-family construction (varying
  `b1 ∈ {4..12}`, `a2 = -2*b1²/9`, integer-approximated) with the
  **24 reference Trans `-2/9` families verified in F1-TRANS-STRUCTURE**
  (24 of 24 with exact ratio `a2/b1² ∈ {-2/9, +1/4}`). Reason: that set
  is already the canonical Trans `-2/9` reference, has known
  Lindemann–Weierstrass status, and contains exactly the integer
  `(a2,b1)` solutions to `9 a2 + 2 b1² = 0` for `|b1| ≤ 3` plus the
  Apéry-cousin `(1, ±2)` pair. Constructing fresh integer
  approximations to `-2/9` for `b1 ∈ {4..12}` would either reproduce
  these same solutions (`b1 = 3k`) or land off-ratio.
- Residual is **clipped from below at `10^-dps`** (not `10^-(2dps)`).
  This keeps the slope statistic bounded at −1 from below and
  isolates SPURIOUS as `slope ≈ 0` exactly per the prompt's intended
  semantics.
- Alg controls use `b1 = 0` (not the deg-(2,1) family) so the limits
  are simple algebraic numbers detectable by linear PSLQ in `B`.

## Anomalies and open questions
**(MOST IMPORTANT — flagged for Claude review.)**

1. **Four reference Trans families are closed forms in `(1/2)·Q(π)`.**
   T08, T11, T14, T21 produce identical PSLQ-accepted relations at
   every dps tested (50–300). These are NOT phantoms (residuals
   genuinely shrink with dps; relations stable at every precision).
   The Trans `-2/9` stratum-membership conjecture is unaffected (all
   four are L–W transcendental), but this contradicts the implicit
   assumption in the prompt that every reference Trans family is
   "Trans-hard" against `{1, π, log2, ζ(3), √-rationals}`. See
   `unexpected_finds.json` (severity: INFORMATIONAL).
2. **Slope is degenerate on this 30-family training set.** Every
   slope ≈ −1.0, including Alg controls. The prompt's design assumes
   spurious near-hits will produce slope ≈ 0; none appeared. The
   monitor as a slope-only test does not separate strata. The joint
   statistic `(slope, accept_pattern)` is what actually
   discriminates.
3. **Open question for Claude:** Are the closed forms for T08/T11/
   T14/T21 the only ones in the broader 585k Trans `-2/9` corpus, or
   the tip of a larger sub-family? A targeted PSLQ sweep over all
   ~24-200 known Trans `-2/9` families against `{1, π, π², L, L²}`
   would answer this in minutes and could refine the manuscript's
   structural claim.
4. **Why these four and not the others?** All four share `b0 = b1`
   (i.e. `b(n) = b1·(n+1)`). The other 20 families do not. This is
   suggestive of a closed-form sub-stratum keyed on `b0 = b1`.
   Worth confirming.

## What would have been asked (if bidirectional)
- Should the Layer-5 protocol be defined by slope alone, by
  acceptance-pattern alone, or jointly? (We chose joint and report
  both.)
- Are the `b0 = b1` closed forms already known in the literature
  (Apéry-like, Brouncker-like, etc.)? If yes, cite; if no, this is a
  small new identification result.
- Should the four closed-form families be removed from future
  Trans-hard enumerations, or retained with a "closed-form" flag?

## Recommended next step
**T2C-CLOSED-FORM-SWEEP** — restrict to the 585k Trans `-2/9` corpus
with `b0 = b1` (and the sign-flipped twin), run PSLQ at dps=200
against `{1, π, π², L}` only. Time budget ≈ 15 minutes. Goal: confirm
that the 4 closed forms are an isolated sub-stratum (size ≤ ~50) and
that the rest of Trans `-2/9` is genuinely Trans-hard against `Q(π)`.
This delivers a clean appendix table for Output B.

## Files committed
- precision_escalation.py
- precision_escalation_results.json
- precision_escalation.log
- pslq_sweep_300.py
- pslq_sweep_300.json
- pslq_sweep_300.log
- t2c_report.md
- claims.jsonl
- unexpected_finds.json
- halt_log.json   (empty — no halt triggered)
- discrepancy_log.json   (empty)
- handoff.md   (this file)

## AEAL claim count
4 entries written to claims.jsonl this session.
