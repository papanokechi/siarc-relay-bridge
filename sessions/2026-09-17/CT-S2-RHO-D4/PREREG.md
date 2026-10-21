# PREREG — CT-S2-RHO-D4

Written **before** any computation was run. Thresholds below are frozen.

## Hypothesis

For `b(n) = Σ_{k=0..d} β_k n^k` with β_d ≠ 0, and
`Q_n = b(n) Q_{n-1} + Q_{n-2}`, `Q_{-1} = 0`, `Q_0 = 1`:

> **H1 (growth law).** `Q_n / Γ(dn+1) = K · (β_d/d^d)^n · n^s · (1 + O(1/n))`
> with `s = β_{d-1}/β_d + (d-1)/2`, whenever
> `r_∞ := lim_n Q_n / ∏_{k≤n} b(k) ≠ 0`.

Focus of this session: **d = 4**, on the 8 representatives of Phase Q1-3.

## Observable

`s_measured`, extracted from `log c_n` where

```
log c_n = log|Q_n| - logΓ(dn+1) + n·log(d^d/β_d)
```

which under H1 satisfies `log c_n = s·log n + C + a₁/n + a₂/n² + …`.

Estimator: `t(n) = (log c_n - log c_{n/2}) / log 2`, which has an asymptotic
expansion in `1/n` with limit `s`. Richardson-extrapolate `t` on the geometric
ladder `n ∈ {1250, 2500, 5000, 10000, 20000}` (ratio 2), giving **4 Richardson
levels** (spec requires ≥ 3). Working precision **dps = 80** (spec requires ≥ 60),
`N_max = 20000` (spec requires ≥ 20000).

`s_predicted = β_{d-1}/β_d + (d-1)/2`.

Residual reported is `|s_measured - s_predicted|` at the deepest Richardson level,
together with the level-to-level drift `|A₃ - A₄|` as the internal error estimate.

## Falsifier (frozen)

> **F1.** For any representative with `r_∞ ≠ 0`:
> `|s_measured - s_predicted| > 1e-6` after Richardson extrapolation.

If F1 fires, HALT and report; do not retune the estimator, the ladder, the
precision, or the threshold.

Secondary halt conditions (from P0): ambiguous convention, missing data,
runtime > 3× budget.

## Vacuity pre-check (run before the main table is believed)

The observable must actually move when the data the hypothesis is about moves.

- **(i) Insensitivity arm.** Hold `β_4` and `β_3` fixed; vary the *lower*
  coefficients `β_2, β_1, β_0` over a grid. H1 predicts `s` does **not** depend
  on them. PASS if the spread of `s_measured` across the grid stays within the
  fit error (taken as `1e-6`, the F1 scale).
- **(ii) Sensitivity arm.** Vary `β_3` with `β_4` fixed. H1 predicts
  `s` moves by exactly `Δβ_3/β_4`. PASS if `s_measured` tracks the prediction to
  within `1e-6`, i.e. the observable genuinely responds.

> **If arm (ii) fails, the observable is not sensitive to the hypothesis and the
> session HALTS.** A pass on arm (i) alone would be vacuous.

Grid, fixed in advance:
- arm (i): `β_4 = 1`, `β_3 = -3`, `(β_2, β_1, β_0) ∈ {-3,0,1,5} × {-3,1} × {-3,1}`
  (16 points).
- arm (ii): `β_4 = 1`, `β_3 ∈ {-4,-3,-2,-1,0,1,2,3,4}`, `(β_2,β_1,β_0) = (-3,1,1)`
  (9 points), plus `β_4 = 7`, `β_3 ∈ {0,1,7,14}` to test the `β_3/β_4` ratio
  rather than `β_3` alone (4 points).

## Minimality / `r_∞` check

`Q_n` must not be the minimal solution, else the growth law is about the wrong
solution. Compute

```
r_n = r_{n-1} + r_{n-2} / (b(n)·b(n-1)),   r_0 = 1/b(1)·b(1) normalisation per script
```

and confirm convergence to a nonzero limit. Report `r_∞` per representative.
A representative with `r_∞ = 0` (or indistinguishable from 0) is **excluded from
F1** but reported.

Precondition checked first: `b(k) ≠ 0` for all integers `k ≥ 1`, and no root of
`b` is a positive integer. If violated → HALT for that representative.

At least **two sign-changing** `b` must be in the tested set.

## Convention map (symbolic, no threshold)

Derive the map between the exponent stored by PCF2-SESSION-Q1 and
`ρ_d = -s - 1 = -(d+1)/2 - β_{d-1}/β_d`.

**Known before running (from CT-S0-INVENTORY):** PCF2-SESSION-Q1 stores **no ρ**
at d = 4. It stores `ξ₀ = d/β_d^{1/d}` and WKB fit exponents `A, α, β, γ`. The
only stored ρ in the relevant corpus is the **d = 2** value for V_quad,
`ρ = -11/6`, in `sessions/2026-05-01/CC-PIPELINE-G/results_vquad.json`.
The convention map will therefore be anchored at d = 2 and labelled
**STRUCTURAL**, or **CONJECTURED** if the d = 2 definition proves ambiguous.
This is recorded here, before running, so it cannot be presented later as a
result.

## Outputs

- `s_table.json` — the main table, hashed.
- `vacuity.json` — both arms, hashed.
- `claims.jsonl` — one line per claim.
- `REPORT.md`.
