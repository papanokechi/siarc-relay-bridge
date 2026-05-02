# Verdict — T37F-Q18-NUMERICAL-PROBE

**Verdict label:** `T37F_Q18_THIRD_STRATUM`

**Classification:** `THIRD_STRATUM_CONFIRMED`

## One-line summary

Branch-(-) re-derivation reports `|a_1_branch_minus| ~ 2.17e-61`
(envelope median, 9 configs, dps=300, N=2000), consistent with
the basis-INDEPENDENT algebraic identity
`U_{k-1}(1) = alpha/16 + gamma - beta^2/(4 alpha) = 0` for QL09;
classification (a) THIRD_STRATUM is parsimonious.

## Numerical headline

| Quantity                             | Value                                        |
|--------------------------------------|----------------------------------------------|
| `C_branch_plus`        (017c)        | `-6.07472006379093506128527538225...`        |
| `C_branch_minus_median`  (017f)      | `-6.07472006379093506128527538225...`        |
| `SIGN_C_FLIP`                         | `False`                                       |
| `a_1_branch_plus` (017c, 57 dig)     | `-1.71e-57`                                   |
| `a_1_branch_minus_median` (017f)     | `-2.17e-61`                                   |
| envelope half-range of `a_1_minus`   | `1.7e-40`                                     |
| `a_2_branch_minus_median`            | `-10.0`     (rational; 30 digits)             |
| `a_3_branch_minus_median`            | `-70/3`     (rational; 30 digits)             |
| Phase 0 sanity `|a_n_-/a_n_+|@n=100` | `1.0`     (to working precision)              |

## Decision rule

Per §C / §D of the prompt:

- `|a_1_branch_minus| < 1e-30`  ->  THIRD_STRATUM_CONFIRMED.
  Measurement: `|a_1_minus| ~ 2.17e-61 << 1e-30`. Margin: 30+ orders
  of magnitude on the median; 10 orders of magnitude on the envelope
  half-range.
- Branch-(-) recurrence rank-full (rank = K_LEAD + 1 = 26), `C_minus`
  finite (~6.07), so NOT BRANCH_DEGENERATE.
- `|a_1_minus| not > 1e-3`, so NOT BASIS_SHADOW_CONFIRMED.

## Recommendation summary

Picture v1.10's Q18 footnote can be retired. Picture v1.11 G20 should
record THREE strata at d=2 (negative-rational a_1, positive-rational
a_1, and a_1 = 0 sub-stratum populated by QL09).

Recommended next prompt: **T37G-A1ZERO-CATALOGUE-SCAN** (catalogue
sweep over d=2 reps satisfying `alpha^2 + 16 alpha gamma = 4 beta^2`).
