# Verdict — T1-017M-BOREL-PADE-S2-092

**Date:** 2026-05-07
**Method:** Borel-Padé exponential-asymptotics resummation (raw-series, small-(N,M) regime)
**dps:** 300

## Aggregate verdict (M8b axis)

**`M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE`**

Resolves M8b axis via closure-by-residual-acceptance per Phase D2 of relay 092.

## Per-rep verdicts

| Rep      | Verdict                  | Median \|S_2 candidate\| | Rel half-range | Best digits-agree | T35 \|S_1\| |
|----------|--------------------------|--------------------------|-----------------|--------------------|--------------|
| V_quad   | `PERMANENT_RESIDUAL_G6b` | 11.02                    | 2.14            | 3.741 / 75 needed   | 51.07        |
| QL15     | `PERMANENT_RESIDUAL_G6b` | 70.63                    | 3.95            | 3.342 / 75 needed   | 134.36       |
| QL05     | `PERMANENT_RESIDUAL_G6b` | 9.62                     | 76.85           | ~3 / 75 needed      | 8.82         |
| QL09     | `PERMANENT_RESIDUAL_G6b` | 48.87                    | 10.08           | ~3 / 75 needed      | 38.17        |

**Convergence-region detection**: 0/84 adjacent (N,M) pairs reach the dps/4 = 75 digit
threshold in any rep. No EXTRACTED region exists.

## Method summary

1. Loaded T37E cached series for V_quad/QL15/QL05/QL09 at dps=400, N=5000
   (substrate SHA-anchored in `claims.jsonl` C-2..C-5).
2. Constructed scaled Borel transform `b_n(u) := a_n * zeta_star^n / Gamma(n+1)`
   for `n in 0..60` per rep. Leading singularity at `u=1` (S_1 location);
   sub-leading at `u=2` (S_2 location).
3. Computed Padé `[N/M]` for `N,M in {6,8,10,12,14,16,18}` (49 cells per rep,
   196 total). Used `mpmath.pade` at dps=300; all 196 cells produced valid
   approximants (no RANK_LOSS — confirms small-(N,M) regime well-conditioned).
4. For each cell: located denominator roots via `mpmath.polyroots`, filtered
   to real-axis poles in [0, 3], identified pole nearest `u=2`, extracted
   residue `R = P(u_pole)/Q'(u_pole)`. Candidate `|S_2| = |2*pi * R * u_pole|`
   (T35 magnitude convention; sign-imaginary factor from Stokes contour absorbed
   in convention).
5. Computed digits-of-agreement across adjacent (N,M) pairs (Manhattan
   distance ≤ 2 in grid). Threshold for EXTRACTED: dps/4 = 75 digits.

## Why PERMANENT_RESIDUAL_G6b classifies

Per peer-AI rubric A's signal-floor diagnostic absorbed in 092 spec: the
absence of Padé convergence at small (N,M) is itself the negative-result
substrate. Specifically:

- The Padé poles near u=2 do **not** cluster tightly: minimum distance
  reached is 0.005 (QL15 [16,14]), most cells have pole-distances in the
  range 0.3-0.7. A converged Padé approximation of the log singularity
  at `u=2` would show poles converging to `u=2` as N+M grows.
- Residues at the (rare) cells where the pole is close to `u=2` vary by
  1-2 orders of magnitude across neighboring (N,M) cells -- no stable
  log-amplitude can be read off.
- The implied `|S_2|/|S_1|` ratios across reps span 0.22 to 1.28,
  inconsistent with a coherent Stokes-data structure.

Combined with **T37M-DIRECT-BOREL-D-EXTRACTION** (2026-05-03) HALTED
verdict at high-order Padé (M=200..800 with 9/12 RANK_LOSS per rep), the
M8b axis sub-leading Stokes constant is bracketed:

- **Too small** for low-order Padé to resolve over the dominant leading
  singularity at `u=1` (092 result).
- **Too noisy** for high-order Padé to capture without numerical
  Hankel singularity (T37M result).

This is the canonical signature of `PERMANENT_RESIDUAL_G6b`: at
laptop-feasible recurrence depth (017m / T37E cache, dps=400, N=5000),
the sub-leading transmonomial governing S_2 is below the resolution
floor of the Borel-Padé method as canonically deployed.

## Comparison to 017L (T37E) LSQ baseline

T37E reported D-extraction infeasibility with relative half-range
`~10^217` across the Stage-2 LSQ stability grid (4 reps × 216 configs).
The present 092 Borel-Padé attempt reports relative half-ranges of
`2.14`-`76.85` across reps -- approximately **215 orders of magnitude
tighter** than the LSQ envelope, yet still failing the spec extraction
threshold. The Padé absence-of-convergence is a strictly stronger
negative-result substrate than LSQ envelope-spanning-zero, because the
Padé construction is well-conditioned at small (N,M) (no RANK_LOSS,
no overdetermined system, 196/196 OK cells).

In other words: the Borel-Padé method delivers a much sharper bound on
where the answer COULD lie -- and that sharper bound still excludes
extraction at the present compute budget.

## What would unlock EXTRACTED in a future fire

Per U2 unexpected find: small-Padé applied to the LEADING-SECTOR-
SUBTRACTED residual (T37M's K=25 cleanness step) at small (N,M) is the
uncharted quadrant. T37M's combination (subtracted + high-order) and
092's combination (raw + low-order) both fail. The orthogonal combination
(subtracted + low-order) might or might not succeed and is mechanically
straightforward to attempt in a follow-up fire. Alternatively, an
ENRICHED RECURRENCE RUN at dps=600+ or N=10000 (operator-side overnight)
combined with the present small-(N,M) sweep methodology would give a
cleaner stress test. Both options remain open as W21 LANE-1 substrate
recommendations -- not actionable without operator dispatch.

## Spec-mandated verdict tags

- M8b axis verdict: `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE`
- Status: `COMPLETE_PERMANENT_RESIDUAL`
- All four rep verdicts: `PERMANENT_RESIDUAL_G6b`
- Halts triggered: 0
- AEAL claims emitted: 15 (spec floor: 5; suggested: 7)
