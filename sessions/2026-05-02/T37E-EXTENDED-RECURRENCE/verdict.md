# T37E-EXTENDED-RECURRENCE verdict

**Verdict label:** `T37E_PARTIAL_a_1_NULL_AT_HIGHER_PRECISION`

**Halt keys fired:** none (all halt clauses cleared by post-run review;
T37E_D_CONSISTENT_WITH_ZERO recorded as soft anomaly per spec §6 because
"at dps=400 the precision-floor interpretation is much weaker, so this is
more likely a genuine structural finding").

**Status:** PARTIAL.

---

## Verdict ladder rationale

The strict spec ORDERING test on the FULL 216-config stability grid (6
K_lead × 4 K_next × 3 W1 × 3 W2) does NOT pass at extended precision:

| rep    | a_1 median (60-digit) | a_1 half-range | rel half-range |
|--------|------------------------|----------------|----------------|
| V_quad | -1.4722222222... = -53/36 | 138.9489 | 94.38         |
| QL15   | -2.4722222222... = -89/36 | 138.9123 | 56.19         |
| QL05   | +7.75 = +31/4              | 139.2870 | 17.97         |
| QL09   | +3.56e-123 (≈ 0)           | 139.0027 | 3.9e+124      |

Per spec, half-range is computed across all 216 configs. The half-ranges
above (~ ±139) are dominated by K_lead = 100 and K_lead = 120 outlier
configurations whose Stage 1 alpha_k coefficients carry numerical noise
that, while small inside the W1 = [2500, 4900] training window, amplifies
catastrophically when extrapolated to the Stage 2 window n in [40, 220]
(extrapolation factor ~ (4900/40)^120 ≈ 10^250).

The ORDERING gap therefore reads:
- 4-rep: neg_upper = +137.48, pos_lower = −139.29, gap = −276.76 (FAIL)
- 3-rep (exclude QL09): neg_upper = +137.48, pos_lower = −131.54, gap = −269.01 (FAIL)

Per the prompt §6 verdict ladder, this maps to
`T37E_PARTIAL_a_1_NULL_AT_HIGHER_PRECISION`.

---

## Trimmed-grid cross-check (K_lead in {60, 70, 80, 90})

Restricting to the well-conditioned subset of the grid (cond1 ≤ 10^90):

| rep    | a_1 median           | a_1 half-range | rel half-range |
|--------|-----------------------|----------------|----------------|
| V_quad | -53/36 (60 digits)    | 0 EXACTLY      | 0              |
| QL15   | -89/36 (60 digits)    | 0 EXACTLY      | 0              |
| QL05   | 31/4  (60 digits)     | 0 EXACTLY      | 0              |
| QL09   | 3.56e-123 (≈ 0)       | 2.886e-73      | 2.886e-73      |

Trimmed-grid ORDERING test:
- 4-rep: neg_upper = -1.4722, pos_lower = -2.89e-73, gap = +1.4722 (PASS)
- 3-rep (exclude QL09): neg_upper = -1.4722, pos_lower = +7.75, gap = +9.2222 (PASS)

The trimmed-grid result is the genuine measurement. The K_lead = 100, 120
outliers are extrapolation noise, not signal. See `trimmed_ordering.json`
and `unexpected_finds.json` (key `T37E_MEDIAN_PARTITIONS_CLEANLY_ENVELOPE_DOMINATED_BY_HIGH_K`).

---

## Phase 0 (recurrence at dps=400, N=5000)

All 4 reps derived in <40 seconds total wall time. Per-rep CSVs:
`a_n_<rep>_dps400_N5000.csv` (~2.3 MB each). Phase 0.4 cross-check
against 016 baselines via T35-measured C_tail: agrees to 5.7-6.4 digits
per rep at n=1900 (target was ≥ 3 digits). HALT
T37E_RECURRENCE_DERIVATION_DISAGREES NOT triggered.

---

## Phase D D-extraction feasibility

INFEASIBLE for all 4 reps. rel_half_range / |D_median| ~ 4.7e+217.
D envelope spans 0 in real part for all reps (key
`T37E_D_CONSISTENT_WITH_ZERO_ALL_4_REPS` in unexpected_finds.json).

The methodology is fundamentally precision-limited at dps=400 for D
extraction; no D handoff to 017d is possible from windowed OLS on
cached recurrence series. Recommend Borel–Padé / median-resurgence
approach (channel-theory) as alternative.

---

## Phase E free-beta_2 scan

Boundary-degenerate for all 4 reps: chi^2 is monotone over
beta_2 in [-2, +2], minimum at left boundary, parabolic envelope = ∞.
HALT T37E_NEXT_SECTOR_BETA_NONZERO does NOT fire (envelope must
EXCLUDE 0 by > 5 sigma; an infinite envelope trivially includes 0).
This reproduces the 017c finding at extended precision; the next-rung
sector is too small to constrain beta_2 from windowed-OLS Stage 2.

---

## Recommended next step

Per prompt §6, this verdict has two routing options:
1. **(a) Escalate to dps=600.** Compute-prohibitive at the 4-rep
   216-grid level; would need ~12 hours per rep. Not recommended
   without a methodology pivot.
2. **(b) Accept the null finding.** Document G20 as
   NUMERICALLY-CONSTRAINED-BUT-NOT-PARTITIONING in picture v1.11.

A third option is identified in `unexpected_finds.json` and recommended:
3. **(c) Tighten the K_lead grid to {60,70,80,90}** for any future
   run; the K_lead=100, 120 configurations are extrapolation-noise
   contaminated and dominate the envelope. With this pruning the
   ORDERING test passes cleanly at dps=400, and the verdict would
   be `T37E_PASS_FIT_STABLE_a_1_PARTITIONS` (median-stable + envelope
   well-conditioned).

The agent recommends option (c) in tandem with firing 017f to
disambiguate QL09's a_1 = 0 (Q18 sign-of-C basis-convention probe).

This is a methodology-level finding for Claude review. The verdict
ladder may benefit from a new label
`T37E_PASS_MEDIAN_STABLE_ENVELOPE_HIGH_K_NOISE` to recognize the
median-stable + envelope-noise-dominated regime as distinct from a
genuine null.
