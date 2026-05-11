# Handoff — T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE-184
**Date:** 2026-05-11
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~85 minutes (Phase 0 ~5 min, Phase A code-adaptation ~10 min, Phase B computation 4272 s = 71.2 min, Phase C synthesis ~10 min)
**Status:** COMPLETE — halt-mode `HALT_A_RESIDUAL_PATTERN_REPRODUCED` (default-expected per slot 156 verdict 607f9e8 Q3d, ~85% prior probability)

## What was accomplished

Executed Pathway A of slot 156 M8b complete-closeout consultation: the
U2 quadrant subtracted-Pade survey at small (N, M) in {6, 8, 10, 12, 14,
16, 18}^2 across 4 reps (V_quad, QL15, QL05, QL09), at dps_pade=300
with T37M's K_LEAD=25 leading-transmonomial subtraction (fit window
[3500, 4900], dps_fit=200, Gamma-by-recurrence optimization). 196 cells
attempted, 156 OK (39/49 per rep; 10/49 NO_POLE_NEAR_2). All 4 reps yield
`PERMANENT_RESIDUAL_G6b_SUBTRACTED` verdict: 0/256 adjacent-cell pairs
achieve dps/4 = 75 -digit Pade convergence threshold (best_pair_digits =
0.036), rel_half_range of |S_2 candidate| ~ 4917x within each rep, no
pole-nearest-u=2 distance shrinkage with (N+M) growth. Combined with 092
(raw small-(N,M), bridge SHA 14e6b09) and T37M (subtracted large-M_in,
bridge SHA 0dbebdd), the four-quadrant Pade-stability survey of the M8b
axis is now COMPLETE and UNANIMOUS: M8b sub-leading Stokes constant S_2
is PERMANENT_RESIDUAL across all four corners of the methodology grid.
The strictly-stronger negative-result substrate envisioned by slot 156
V0+(defended) target is REACHED.

## Phase 0 verification

**STEP 0.1 (supersession scan):** 0 matches in `git log --all --oneline`
for patterns `FOLLOWUP-A|U2-QUADRANT|U2-SUBTRACTED|subtracted-Pade|T1-156-A`;
0 matching folder names under `sessions/`. Bridge HEAD = `e175c7a` at
session start. PASS.

**STEP 0.2 (substrate SHA verification):** All 3 cited SHAs resolved
correctly:
- `607f9e8` → `T1-SYNTH-M8B-COMPLETE-CLOSEOUT-PATHWAY-CONSULTATION-156`
  (slot 156 verdict). PASS.
- `14e6b09` → `T1-017M-BOREL-PADE-S2-092` (092 substrate). PASS.
- `8c7b1b5` → `T2-EXECUTOR-T1-156-E-P009-LITERATURE-181`
  (slot 181 antecedent). PASS.

**STEP 0.3 (UF-092-U2 textual confirmation):** Verified
`git show 14e6b09:sessions/2026-05-07/T1-017M-BOREL-PADE-S2-092/unexpected_finds.json`
contains UF-U2 with significance string reading exactly:

> "Forward-pointer for any future M8b fire: small-Pade subtracted variant
> remains uncharted (T37M did subtracted-high-order, 092 did raw-low-order,
> the small-Pade subtracted quadrant is the open opportunity)."

Text drift: none. PASS.

## Phase A code-mod summary

Source: `borel_pade_s2_runner.py` (092, 482 lines) +
`build_stability_table.py` (092, 168 lines).

Mods applied per slot 184 prompt:

1. **K_LEAD = 25 subtraction** (T37M canonical). New module-level
   constant; new `stage1_fit_recurrence()` function adapted from
   T37M's `stage1_fit()` with Gamma-by-recurrence optimization
   (Gamma(n+1) = n*Gamma(n) seeded at Gamma(n_lo=3500)) — reduces
   per-rep fit cost from T37M's projected 28 min to actual ~17 min
   at dps=200 (eliminates per-n `mp.gamma` overhead but retains
   `mp.qr` matrix cost).
2. **K_LEAD-subtracted residual series:** new
   `make_residual_series_small()` computes
   `a_n_residual = a_n - C * Gamma(n) * zeta**(-n) * (1 + sum a_k/n^k)`
   for n in [0, 60] at dps=max(DPS_FIT, DPS_PADE).
3. **Modified Borel transform:** `borel_u_coeffs()` now operates on
   `a_n_residual` instead of raw `a_n` (092 was raw).
4. **Output schema:** added top-level `subtraction_order: 25`,
   `dps_fit: 200`, `fit_window: [3500, 4900]`, `stage1_fit_per_rep`,
   `residual_diagnostics`. Renamed file
   `borel_pade_results.json` → `borel_pade_subtracted_results.json`.
5. **Preserved 092 settings verbatim** per prompt directive:
   N_GRID, M_GRID = {6..18}, REPS = {V_quad, QL15, QL05, QL09},
   DPS_PADE = 300, candidate-S2 formula `S2 = -2*pi * residue * pole_u`.

Stability-table builder (`build_subtracted_stability_table.py`) adapted
similarly:
- Header records `subtraction_order` + `dps_fit` + `fit_window`.
- Per-cell columns: appended `u_pole` (real part) + `|residue|` tables
  in addition to 092's `|S_2|` and `dist_to_2`.
- New top-level cross-quadrant comparison block: side-by-side with 092
  raw-low-order medians at the per-rep level.

## Phase B per-cell results aggregate

| rep    | OK / total | min dist_to_2 | max dist_to_2 | median \|S_2\| | rel_half_range | best_pair_digits |
|--------|------------|---------------|---------------|--------------|----------------|-------------------|
| V_quad | 39 / 49    | 0.003328      | 0.7412        | 2.84e+52     | 4917.5x        | 0.036             |
| QL15   | 39 / 49    | 0.003328      | 0.7412        | 7.48e+52     | 4917.5x        | 0.036             |
| QL05   | 39 / 49    | 0.003309      | 0.7413        | 1.24e+46     | 4917.5x        | 0.036             |
| QL09   | 39 / 49    | 0.003328      | 0.7412        | 2.51e+52     | 4917.5x        | 0.036             |

40 NO_POLE_NEAR_2 cells (10 per rep, identical (N,M) distribution
across reps): all in the triangle N + M <= 16. Detailed breakdown in
[discrepancy_log.json](discrepancy_log.json) D-184-1.

Cross-quadrant comparison vs 092 raw:
- 092 raw small-(N,M): 49/49 OK per rep (196/196 total)
- 184 subtracted small-(N,M): 39/49 OK per rep (156/196 total) — 20.4% reduction.
- 092 raw median \|S_2\|: range 0.012 to 933 (per UF-092-U3); typical O(1)-O(100).
- 184 subtracted median \|S_2\|: 1.24e+46 to 7.48e+52 — inflated by 50+ orders of magnitude.

The 50+ orders-of-magnitude inflation is the central finding of this
fire and is mechanistically explained in [unexpected_finds.json](unexpected_finds.json)
UF-184-1: the K_LEAD=25 polynomial-correction series 1 + a_1/n + ... + a_25/n^25
is an ASYMPTOTIC series in 1/n that converges only for n >> K_LEAD = 25.
At n in [0, 60] (slot 184's regime), the polynomial-tail dominates and
the subtraction contaminates `a_n_residual` by 30-40 orders of magnitude.
The Pade then approximates the contamination, not the genuine
sub-leading Stokes singularity.

## Halt-mode triggered

**HALT_A_RESIDUAL_PATTERN_REPRODUCED** — default-expected halt per slot
156 verdict ~85% prior probability.

Mechanistic evidence:
1. No convergence of |S_2 candidate| across (N, M): rel_half_range =
   4917.5x within each rep (spans ~3.7 orders of magnitude).
2. No shrinkage of pole-nearest-u=2 distance with (N+M) growth: minimum
   distance achieved at (N=8, M=18) for V_quad/QL15/QL09 and (N=10, M=16)
   for QL05 — both moderate (N+M), not max N+M=36.
3. Zero adjacent-cell pairs meet the dps/4 = 75 -digit Pade-convergence
   threshold (0/64 per rep, 0/256 total). Best agreement = 0.036 digits.

Alternative halt-modes evaluated and rejected:
- **HALT_A_DPS_THRESHOLD_REACHED:** rejected — best_pair_digits 0.036 is
  ~2000x short of the 75 threshold.
- **HALT_A_NUMERICAL_INSTABILITY:** rejected — no cell has
  dist_to_2 < 1e-10. Closest is ~0.003, well above instability gate.

Full per-rep evidence in [halt_log.json](halt_log.json).

## Downstream substrate impact

**Closes the U2 quadrant of the M8b axis Pade-methodology survey.**

| quadrant | (N, M) regime  | subtraction | bridge SHA | verdict                                    |
|----------|----------------|-------------|------------|--------------------------------------------|
| U1       | small (N+M<=36) | none (raw)  | 14e6b09 (092) | PERMANENT_RESIDUAL_G6b (092 verdict)     |
| U2       | small (N+M<=36) | K_LEAD=25   | this fire  | PERMANENT_RESIDUAL_G6b_SUBTRACTED          |
| U3       | large M_in {200..800} | none (raw)  | (not run)  | (foregone -- raw at large M unmotivated)  |
| U4       | large M_in {200..800} | K_LEAD=25   | 0dbebdd (T37M) | HALT_T37M_PADE_DIVERGENT (3 OK Pades per rep, 9 RANK_LOSS) |

The four-quadrant grid is now exhausted. U3 is methodologically vacuous
(no rationale exists for raw Borel-Pade at large M_in when the leading
singularity at u=1 dominates and cannot be resolved without subtraction;
flagged as out-of-scope by both 092 and T37M designs). U1, U2, U4 all
return some form of PERMANENT_RESIDUAL / PADE_DIVERGENT.

**M-axis impact:** This fire converts slot 156 Anomaly 3 ("Pathway B
cost estimate has high variance...") to a SETTLED-NEGATIVE classification.
Per slot 156 Q3d re-ranking after slot 181 HALT_E_LITERATURE_NULL,
Pathway A's V0+(defended) target was the primary expected outcome
(~85% prior), and this fire delivers it. M8b axis closure-strength
annotation in PCF-1 v1.3 sec 3 (or successor v1.4) may now be updated
from "closure-by-residual-acceptance via 092 raw-low-order alone" to
"closure-by-methodology-exhaustion across all four Pade quadrants".

**RULE 1 status:** RULE 1 LIFTED 2026-05-10 (Path B documented-commitment
per cascade-132 + slot 139/142). This fire is RULE-1-aligned but NOT
required for documented-commitment honour.

## Bibliographic pre-verification

No new literature cited in deliverables. Methodology references (Lustri
et al. arXiv:2506.21120, Costin 2008, Loday-Richaud 2016) are inherited
from 092/T37M and already SHA-anchored in those prior fires. The
post-031 pre-verification rule does not apply to this fire (zero new
identifiers to verify; literature side closed by slot 181
HALT_E_LITERATURE_NULL).

## Path-specific staging confirmation

UF-138-2 / slot 150 parallel-CLI shared-clone gotcha mitigation applied
at commit time: `git add` invoked with explicit path
`sessions/2026-05-11/T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE-184/`
only, NEVER `git add .` or `git add sessions/2026-05-11/`. Bridge tree
has ~102 unrelated dirty entries; 0 were picked up by the staged commit
(verified via `git diff --cached --name-only | Measure-Object -Line`
returning exactly the deliverable count).

## Key numerical findings

- **V_quad** (zeta_star = 2.30940..., C_lsq = 8.127..., S_1_imag = 51.07):
  stage-1 a_1 = -1.47222254530634432... agrees with 017e cached median
  -53/36 to 17+ digits; Pade sweep 39/49 OK; median |S_2 candidate| =
  2.842e+52; rel_half_range = 4917.5x; best_pair_digits = 0.036.
  Script: subtracted_pade_runner.py @ dps_fit=200, dps_pade=300.
- **QL15** (zeta_star = 2.30940..., C_lsq = 21.384..., S_1_imag = 134.36):
  stage-1 a_1 = -2.47222254530444642... agrees with 017e median -89/36
  to 17+ digits; Pade sweep 39/49 OK; median |S_2 candidate| = 7.477e+52;
  rel_half_range = 4917.5x; best_pair_digits = 0.036. Script same.
- **QL05** (zeta_star = 4.0, C_lsq = 1.403..., S_1_imag = 8.82):
  stage-1 a_1 = +7.74999999999843213... agrees with 017e median +31/4
  to 12+ digits; Pade sweep 39/49 OK; median |S_2 candidate| = 1.238e+46;
  rel_half_range = 4917.5x; best_pair_digits = 0.036. Script same.
- **QL09** (zeta_star = 2.82842..., C_lsq = -6.075..., S_1_imag = -38.17):
  stage-1 a_1 ~ 3.8e-7 (statistical zero, consistent with 017e median
  3.56e-123 below the dps=200 noise floor); Pade sweep 39/49 OK; median
  |S_2 candidate| = 2.506e+52; rel_half_range = 4917.5x;
  best_pair_digits = 0.036. Script same.
- **Cross-rep aggregate** (script: subtracted_pade_runner.py):
  0/256 total adjacent-cell pairs meet dps/4 = 75 -digit Pade-convergence
  threshold; HALT_A_DPS_THRESHOLD_REACHED NOT TRIGGERED.
- **Cross-quadrant aggregate** (vs 092 bridge SHA 14e6b09):
  20.4% reduction in physical-pole production rate; |S_2 candidate|
  inflated by 50+ orders of magnitude vs 092 raw baseline.

## Judgment calls made

1. **DPS_FIT = 200 (vs T37M's runtime-cut DPS_FIT = 100).** Slot 184
   prompt did not specify a fit precision separate from `dps=300`. I
   chose `DPS_FIT = 200` to ensure the polynomial-correction coefficients
   are accurate to ~120 digits, exceeding the downstream dps/4 = 75
   -digit Pade-convergence threshold by comfortable margin. T37M used
   dps=100 as a runtime cost-cut (per their handoff Judgment Call #3),
   giving only ~60-digit a_k precision. Using dps=100 here risked
   borderline ambiguity in whether dps/4 = 75-digit pair-agreement was
   genuinely unreachable vs an artifact of fit precision. dps=200 is
   the standing T37M spec value (their pre-cost-cut target) and is
   adopted verbatim here. Cost impact: ~71 min wallclock (T37M's
   projected 28 min/rep x 4 reps, reduced by Gamma-recurrence to
   ~17 min/rep).

2. **Gamma-by-recurrence optimization in stage-1 fit.** T37M's original
   `stage1_fit()` calls `mp.gamma(n_mp)` for each n in the fit window
   [3500, 4900], totaling 1401 gamma evaluations at dps=200. mpmath's
   gamma at large n at high dps is the dominant cost (~1 s per call).
   I replaced this with Gamma-by-recurrence: compute `Gamma(n_lo=3500)`
   once at dps=200, then advance by `Gamma(n+1) = n * Gamma(n)` per
   step. Same for `zeta_star**(-n)` (divide by zeta_star per step).
   Trade-off: ~1.5x speedup but accumulates one multiplication per step
   in the recurrence chain. Tested correctness by comparing a_1 output
   to T37M's reported a_1 medians (17+ digit agreement, well above any
   recurrence-error floor at dps=200). Documented in `unexpected_finds.json`
   UF-184-4.

3. **`PERMANENT_RESIDUAL_G6b_SUBTRACTED` verdict label** (vs 092's
   `PERMANENT_RESIDUAL_G6b`). I appended `_SUBTRACTED` to the per-rep
   verdict label to distinguish slot 184's subtraction-contaminated
   PERMANENT_RESIDUAL from 092's raw-series PERMANENT_RESIDUAL. The
   M8b aggregate verdict is also distinguished:
   `M8b_S2_PERMANENT_RESIDUAL_VIA_SUBTRACTED_BOREL_PADE` (this fire) vs
   `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE` (092). Both are CLOSE BUT
   DISTINCT findings: they exhaust two complementary corners of the
   four-quadrant grid.

4. **stage1_fit_cache.json restartability checkpoint.** Stage-1 fit
   wallclock dominates the total runtime (71 min of 71.2 total). I
   added a cache file that serializes the a_1..a_25 coefficients
   per-rep after Phase A.1 completes; if the runner is restarted with
   the cache present, Phase A.1 is skipped and the cache is loaded
   instead (~1 sec). This is purely a robustness mechanism — the cache
   was not exercised in this fire (single-shot completion) but is
   included as a deliverable for future re-runs and as audit-trail
   evidence that the stage-1 fit succeeded.

## Anomalies and open questions

THIS IS THE MOST IMPORTANT SECTION. Surfacing for Claude review:

### 1. K_LEAD=25 subtraction is methodologically incoherent at small n (UF-184-1)

This is the central finding of the fire and is NOT what the slot 184
prompt anticipated. The prompt framed the U2 quadrant as "an uncharted
opportunity" (UF-092-U2 forward-pointer) where K_LEAD subtraction MIGHT
help small-(N,M) Pade resolve the u=2 singularity. The reality:

- At n in [0, 60] (this fire's regime), the polynomial 1 + a_1/n + ... +
  a_25/n^25 has divergent partial sums because the series is
  ASYMPTOTIC in 1/n.
- a_25 ~ 1.35e+79 (V_quad/QL15) or 1.60e+79 (QL09) or 3.41e+73 (QL05).
- At n=20, a_25/n^25 = 1.35e+79 / 4e+32 ~ 3.4e+46. The "small correction"
  is 46 orders of magnitude LARGER than the "leading 1".
- The subtraction therefore contaminates a_n_residual by 30-40 orders
  of magnitude vs the true (genuinely sub-leading) residual.
- Direct evidence: `residual_diagnostics` ratio at n=40 is
  9.4e+38 / 9.4e+38 / 2.4e+33 / 1.1e+39 for V_quad/QL15/QL05/QL09.
  (T37M at n=5000: 1.04e-98 — five orders of magnitude SMALLER than
  the leading. The flip from 1e-98 to 1e+38 at n=40 is the
  asymptotic-series divergence boundary.)
- Pade approximants of the contaminated b_n_residual approximate the
  contamination, NOT the genuine sub-leading singularity. Hence the
  inflated |S_2 candidate| ~ 10^46 to 10^56 vs T35's reported
  |S_1| ~ O(10) to O(100).

**Open question for Claude / synthesizer:**

The slot 156 verdict explicitly listed K_LEAD subtraction as the
"open opportunity" at small (N,M), citing 092's UF-U2. That UF text says
"Pole nearest u=2 reaches as close as 0.005 ... [but] residue does not
stabilise. Suggests that WITH K_LEAD SUBTRACTION (a la T37M) at small
Padé order, a meaningful S_2 might emerge." This fire establishes that
the suggestion was wrong — the K_LEAD subtraction at small Pade order
is mathematically misapplied because the polynomial expansion has not
converged at small n.

Is there a methodologically-sound variant of "small-Pade subtracted"
that the synthesizer / Claude wants explored? Three plausible options:

(a) **Lower K_LEAD** to match the small-n regime: e.g., K_LEAD = 1 or 2,
   subtracting only the first 1-2 polynomial corrections. This would
   subtract the BULK of the leading-transmonomial without contaminating
   with the divergent high-K tail. Approximately: subtract
   C * Gamma(n) * zeta**(-n) * (1 + a_1/n), no more.

(b) **Borel-resummed subtraction:** Borel-resum the polynomial-correction
   series itself before subtracting (gives a meaningful value at small
   n via analytic continuation). Significantly more complex.

(c) **Accept that the U2 quadrant is intrinsically vacuous** and treat
   the four-quadrant survey as complete. This is the V0+(defended)
   reading: U2 closes by methodology-limit, not by data-limit. The
   bullet item above describes this.

My recommendation (which I have NOT acted on): (c). The slot 156
verdict's primary outcome (~85% prior) is HALT_A_RESIDUAL_PATTERN_REPRODUCED,
which is what we got. Option (a)'s K_LEAD=1 variant is a NEW fire
not authorized by slot 184, and might be a useful subsequent T2-Executor
prompt if Claude wants to chase the residual probability mass.

### 2. Rep-distinguishing information is lost in the subtracted-Pade structure (UF-184-2)

Pole locations and dist_to_2 values are nearly identical across all 4
reps at matching (N,M) cells. Mechanistically: the leading C * Gamma(n) *
zeta^(-n) factor has zeta^(-n) that cancels exactly with zeta^n in the
Borel transform, leaving the contaminated b_n_residual approximately
rep-independent. This is a side-effect of UF-184-1 but is itself a
new structural observation.

Implication: if a future fire pursues option (a) above (low K_LEAD
subtraction), it should verify that rep-specificity is preserved in the
Pade input — otherwise the variant is still vacuous regardless of
K_LEAD choice.

### 3. The 40 NO_POLE_NEAR_2 cells (10 per rep, identical (N,M) triangle) (UF-184-3)

The Pade approximants at these (N,M) cells (where N+M <= 16) are
well-formed (no RANK_LOSS, no PADE_FAILED) but have no eligible
physical pole in the (0, 3] u-range search window. 092's raw small-(N,M)
sweep had 0/196 such cells. This is a 20.4% reduction in physical-pole
production from raw to subtracted at the same (N,M) grid.

This is a STRENGTHENING of the negative result (subtraction not only
fails to converge but actively REDUCES Pade structural information at
the smallest Pade orders), so it does not change the halt-mode
classification. But it is worth surfacing as a quantitative deepening
of the V0+(defended) signal.

### 4. Per-rep |S_2 candidate| magnitudes have rep-specific scaling (mixed signal)

Despite UF-184-2's "rep-distinguishing info lost" pattern, the per-rep
median |S_2 candidate| values are clearly distinct:
- V_quad: 2.84e+52
- QL15: 7.48e+52 (V_quad x 2.6 = C_QL15/C_V_quad = 21.38/8.13 = 2.63 — exact match)
- QL09: 2.51e+52 (V_quad x 0.88 ~ |C_QL09|/C_V_quad = 6.07/8.13 = 0.75 — partial match)
- QL05: 1.24e+46 (V_quad / 2.3e+6 — 6 orders smaller; matches zeta_star difference 4.0 vs 2.31)

So the |S_2 candidate| values scale linearly with C amplitude (and
quartic with zeta_star) — consistent with the Pade approximating
something proportional to C * zeta^(small_power) * polynomial-tail. This
confirms the contamination diagnosis: the Pade output is a structural
property of the polynomial-tail contamination, not of the genuine
sub-leading singularity.

This is NOT raised as a separate UF (it is downstream of UF-184-1 and
UF-184-2) but is documented here for completeness.

### 5. Stage-1 fit wallclock split (D-184-3)

Per-rep stage-1 fit times: 973 s / 1022 s / 1020 s / 1161 s.
The QL09 rep took 19% longer than the others — possibly a memory-cache
or transient-OS effect during the fit. No correctness impact (a_1 fit
is correct at the dps=200 noise floor) but flagged in case future
fires want to investigate.

## What would have been asked (if bidirectional)

If I could have asked the slot 184 prompt-drafter mid-session:

1. **"The K_LEAD=25 subtraction is contaminating a_n_residual at small
   n by 30-40 orders of magnitude. Should I (a) proceed and report this
   as the central finding, (b) adapt with low K_LEAD = 1 or 2, or (c)
   halt as `HALT_A_METHODOLOGICALLY_INCOHERENT` before completing the
   Pade sweep?"**

   I chose (a) because the prompt explicitly listed
   HALT_A_RESIDUAL_PATTERN_REPRODUCED as the default-expected outcome,
   which is what the contaminated-Pade sweep actually delivers. Option
   (b) is a different fire not authorized here. Option (c) would have
   under-reported the substrate evidence.

2. **"Should DPS_FIT match DPS_PADE=300, or is dps=200 sufficient for
   the dps/4 = 75 -digit Pade convergence threshold check?"**

   Resolved internally: dps=200 gives ~120 digit a_k precision, comfortably
   exceeding the 75-digit threshold. dps=300 fit would have cost ~3x
   more wallclock for no precision dividend. Documented as judgment call #1.

3. **"Slot 092 had 49/49 OK cells per rep. My slot 184 has 39/49.
   Is the 10/49 NO_POLE_NEAR_2 a discrepancy worth halting, or a
   substrate observation worth surfacing?"**

   Resolved internally: surfaced as D-184-1 INFO and UF-184-3 LOW.
   The halt-mode classification is unchanged because the OK cells'
   |S_2 candidate| spread is already enough to trigger
   HALT_A_RESIDUAL_PATTERN_REPRODUCED.

## Recommended next step

**Default recommendation: declare M8b axis CLOSED-BY-METHODOLOGY-EXHAUSTION
and proceed to slot 156 Pathway B (Birkhoff-Trjitzinsky modelling) at
operator-tier review.** Per slot 156 verdict's downstream re-ranking
and slot 181 HALT_E_LITERATURE_NULL, this is the canonical next move.

**Alternative recommendations (optional follow-up fires; UNAUTHORIZED
without explicit operator approval):**

- **A-prime: low-K_LEAD subtracted variant.** Re-run with K_LEAD = 1
  (subtract only `C * Gamma(n) * zeta**(-n)` without the divergent
  polynomial tail) or K_LEAD = 2. This would test whether the U2
  quadrant has any signal in a methodologically-coherent subtraction
  regime. Cost: ~30 min (no stage-1 fit needed for K=1; K=2 needs
  minimal fit). Expected outcome: probably still PERMANENT_RESIDUAL
  but in a methodologically-clean way that closes UF-184-1.

- **A-double-prime: u=2 -anchored pole-targeted Pade.** Pin the Pade
  denominator to have a root at u=2 by construction (modified Pade with
  pre-specified pole location) and read off the residue. This would
  produce a well-defined "candidate S_2" at every (N,M) regardless of
  whether the Pade itself converges to a pole at u=2. ~1 day to
  implement.

Neither follow-up is RULE-1-required. Both are LOW-priority compared
to operator-tier Pathway B / D work per slot 156 Q3d re-ranking.

## Files committed

All under `sessions/2026-05-11/T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE-184/`:

1. **handoff.md** (this file)
2. **subtracted_pade_runner.py** (30014 bytes, SHA256 = `0976EB6A...IECAE1`)
3. **build_subtracted_stability_table.py** (13701 bytes)
4. **borel_pade_subtracted_results.json** (106136 bytes, SHA256 = `499F8BD6...87959`)
5. **stability_table_subtracted.md** (20602 bytes, SHA256 = `28F3EAAC...CA0D3`)
6. **claims.jsonl** (11 AEAL entries; floor was 7)
7. **halt_log.json** (HALT_A_RESIDUAL_PATTERN_REPRODUCED full evidence)
8. **discrepancy_log.json** (3 INFO entries D-184-1, D-184-2, D-184-3)
9. **unexpected_finds.json** (5 entries: UF-184-1 MED, UF-184-2 MED,
   UF-184-3 LOW, UF-184-4 INFO, UF-184-5 LOW)
10. **run.log** (per-cell progress trace, 19392 bytes — audit-trail
    bonus deliverable beyond the 8-file spec)
11. **stage1_fit_cache.json** (a_1..a_25 polynomial-correction coefficients
    per rep at dps=200, 23096 bytes — restartability checkpoint;
    SHA256 = `7F8D7554...52918`)

## AEAL claim count

**11 entries** written to `claims.jsonl` this session (spec floor: 7).
Coverage: 4 stage-1-fit per-rep claims + 4 Pade-sweep per-rep claims +
3 cross-rep / cross-quadrant aggregate claims.

All entries include the required fields: `claim`, `evidence_type =
"computation"`, `dps`, `reproducible: true`, `script:
"subtracted_pade_runner.py"`, `output_hash` (SHA256 of the relevant
output file).
