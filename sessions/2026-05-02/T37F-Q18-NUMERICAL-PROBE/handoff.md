# Handoff — T37F-Q18-NUMERICAL-PROBE
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

Closed Q18 (sign-of-C / branch-of-c basis ambiguity) numerically by
re-deriving the QL09 Birkhoff recurrence in the opposite dominant-
balance branch (`c = -2/sqrt(alpha)`) at dps=300 N=2000, refitting
(C, a_1, a_2, a_3, D) under the same protocol as 017c
(T37-S2-EXTRACTION-POLYNOMIAL-AWARE), and comparing branch (+) vs
branch (-) invariants. The classification is THIRD_STRATUM_CONFIRMED
(verdict label `T37F_Q18_THIRD_STRATUM`): QL09's a_1 = 0 is a
structural, basis-INDEPENDENT vanishing, not a convention shadow.

## Key numerical findings

- Phase 0 sanity at n=100: `|a_n_minus / a_n_plus| = 1.0` to working
  precision (dps=300; `t37f_runner.py`).
- Stage1 (K_lead=25, W1=[400,1900], dps=300):
  - `C_branch_minus_median = -6.07472006379093506128527538225` (30 dig)
  - `a_1_branch_minus_median = -2.17e-61` (envelope median across 9
    configs); half-range = 1.7e-40 (both far below the 1e-30 THIRD_
    STRATUM threshold).
  - `a_2_branch_minus_median = -10.0` to 30 digits
  - `a_3_branch_minus_median = -23.3333333333... (-70/3)` to 30 digits
  (`t37f_runner.py`, `invariant_comparison.json`).
- Phase 0 algebraic identity: for QL09 the bracket
  `alpha/16 + gamma - beta^2/(4 alpha) = 1/8 + 1 - 9/8 = 0`,
  which is c-INDEPENDENT (`derive_recurrence_QL09_opposite_branch.py`).
- Branch identity (Unexpected Find #1): in the recurrence form used
  by T35/017c, `a_n(branch -) = (-1)^n * a_n(branch +)`, hence
  `T_n` with signed `zeta_signed = 2c` is literally identical across
  branches.

## Judgment calls made

- The "signed dominant action" convention `zeta_signed = 2c` (as
  opposed to `|2c|`) was chosen for branch (-) so that T_n converges
  to a real C rather than oscillating. Documented in
  `phase_0_branch_pinning.json` §branch_minus.rationale. This is the
  natural choice; the alternative `|2c|` would just absorb the
  per-n sign into a (-1)^n factor and yield numerically identical
  fit results.
- Stage 2 (next-rung) `D` extraction: 017c reported D for QL09 as
  BLOCKED (D_half_range/|D_median| ~10^11). Both 017f's branch-(+)
  recomputation and branch-(-) measurement of D are therefore
  noise-floor and not directly comparable. The Phase D
  classification was driven by |a_1| only, NOT by D ratios. Logged
  in `discrepancy_log.json`.
- The PSLQ probe was conditional on `|a_1_minus| > 1e-3`. Since
  |a_1_minus| ~ 2e-61 << 1e-3, PSLQ was not invoked (both
  tol=1e-8 and tol=1e-12 entries in claims.jsonl record `None`).
  This is the right behaviour: PSLQ on a numerically-zero value
  would only return spurious relations.

## Anomalies and open questions

- **Branch identity (Unexpected Find #1).** The empirical observation
  that the two branches give literally identical T_n is structurally
  explained by `a_n(-c) = (-1)^n a_n(+c)` plus `zeta_signed_minus =
  -zeta_signed_plus`. This is a general d=2 PCF result, not specific
  to QL09. **Implication for picture v1.10's Q18 footnote:** the
  branch convention is provably not a degree of freedom at the level
  of T_n with signed-zeta. Worth amending the footnote to reflect
  this, and to record that the QL09 a_1 = 0 stratum is therefore
  structural with no possible "shadow" reading.
- **a_1 = 0 stratum membership predicate.** Phase 0 identifies the
  bracket `alpha^2 + 16 alpha gamma - 4 beta^2 = 0` as the predicate
  selecting QL09-like reps. Worth a follow-on prompt to scan the d=2
  catalogue for additional members of this sub-stratum (rapid arithmetic
  filter; potentially extends Picture v1.11 G20 stratification).
- **a_2, a_3 rationality.** Both branches return what look like clean
  rationals: a_2 = -10, a_3 = -70/3 (Unexpected Find #2). The (a_2,
  a_3) values across V_quad / QL15 / QL05 / QL09 might admit a finer
  Galois-aware classification — finer than the a_1 partition that
  017c established. Out-of-scope here.
- **D extraction remains noisy.** A future T37 retry at dps=400 / N=5000
  would resolve the D blockage and let us also test whether
  `|D_minus| = |D_plus|` is itself an invariant (Phase C.1 expectation).

## What would have been asked (if bidirectional)

- Should Picture v1.10's Q18 footnote be retired entirely (replaced
  by the structural-vanishing fact), or kept with a note that the
  question is settled in favour of the structural reading?
- Is the predicate `alpha^2 + 16 alpha gamma = 4 beta^2` worth a
  full-catalogue scan immediately (small extra prompt), or should it
  wait until G20 stratification is reviewed?

## Recommended next step

A short follow-on prompt **T37G-A1ZERO-CATALOGUE-SCAN**:

> Scan the d=2 (alpha, beta, gamma, delta, epsilon) catalogue (T3
> output) for representatives satisfying
> `alpha^2 + 16 alpha gamma = 4 beta^2`. For each match, compute
> (alpha, beta, gamma, delta, epsilon, A_pred, Delta_b) and the
> 017c-style a_2, a_3 rationals at dps=200 N=1500 (one branch
> only, since 017f shows branches are equivalent at the T_n level).
> Tabulate and identify any that share QL09's (Delta_b > 0,
> a_1 = 0) signature. Output: a JSON sub-stratum table for picture
> v1.11 G20 amendment.

## Files committed

- `derive_recurrence_QL09_opposite_branch.py`
- `derive_recurrence_branch_check.json`
- `derive_recurrence.log`
- `t37f_runner.py`
- `t37f_run.log`
- `runner.stdout.log`
- `a_n_QL09_opposite_dps300_N2000.csv`
- `phase_0_branch_pinning.json`
- `invariant_comparison.json`
- `q18_numerical_certificate.md`
- `verdict.json`
- `halt_log.json`
- `discrepancy_log.json`
- `unexpected_finds.json`
- `claims.jsonl`
- `rubber_duck_critique.md`
- `handoff.md`

## AEAL claim count

17 entries written to `claims.jsonl` this session (>= 16 required).

## Picture v1.10 vs v1.11 recommendation

Classification: **THIRD_STRATUM_CONFIRMED**.

Recommendation: amend Picture v1.11 G20 to record THREE strata at
d=2:
  (i) Delta_b<0 negative-rational a_1 (V_quad: -53/36; QL15: -89/36),
  (ii) Delta_b>0 positive-rational a_1 (QL05: +31/4),
  (iii) Delta_b>0 a_1 = 0 sub-stratum (QL09; predicate
        alpha^2 + 16 alpha gamma = 4 beta^2).
Picture v1.10's Q18 footnote can be retired; the branch-convention
ambiguity is provably not a real degree of freedom at the T_n level
(Unexpected Find #1).
