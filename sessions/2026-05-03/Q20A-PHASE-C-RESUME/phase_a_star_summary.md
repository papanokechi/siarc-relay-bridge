# Phase A* Summary — Q20A-PHASE-C-RESUME

**Verdict signal:** `A_DIRECT_IDENTITY_d10`

Extends Q20 Phase A's `A_DIRECT_IDENTITY` (which covered the
sanity range `d ∈ {2, 3, 4}`) to `d ∈ {2, 3, …, 10}` as a
stress test against any d-dependent symbolic instability.

## A*.1 — Q20 anchor script integrity

The Phase A* wrapper imports Q20's
`phase_a_symbolic_derivation.py` unchanged and asserts its
SHA-256 matches the value recorded in Q20's `claims.jsonl`.

| Field    | Value |
|----------|-------|
| Path     | `sessions/2026-05-03/Q20-CONJ33A-PROOF-UPGRADE/phase_a_symbolic_derivation.py` |
| SHA-256  | `8e6f9ebde933652e2581578d282163f0220091ea0ee4adbd6754bd53458f7496` |
| Match    | ✅ identical to Q20-recorded hash |

No script drift. The Phase A* sweep below uses Q20's exact
symbolic pipeline (`operator_points_general`,
`derive_at_concrete_d`, `_sanity_check`); only the d-range and
the β_d test points are extended.

## A*.1 — Extended sweep at d ∈ {2..10}

For each d, two β_d test points are run:
the **first** is the AEAL-cached or SIARC-conventional value
(β_2 = 3 for V_quad, β_d = 1 for d ≥ 3 per the cubic /
quartic / higher-d catalogues); the **second** is a coprime
stress value to exercise the `mpmath.polyroots` path on a
non-trivial radical.

| d  | β_d | computed max\|root\|                                          | rel_err   | match |
|----|-----|---------------------------------------------------------------|-----------|-------|
| 2  | 3   | 1.154700538379251529018297561                                  | 0         | ✅    |
| 2  | 7   | 0.755928946018454454429033072468                               | 0         | ✅    |
| 3  | 1   | 3.0                                                            | 0         | ✅    |
| 3  | 5   | 1.75441064292771963930407241608                                | 1.52e-51  | ✅    |
| 4  | 1   | 4.0                                                            | 0         | ✅    |
| 4  | 9   | 2.30940107675850305803659512201                                | 0         | ✅    |
| 5  | 1   | 5.0                                                            | 0         | ✅    |
| 5  | 11  | 3.09521960341922786443260685649                                | 1.73e-51  | ✅    |
| 6  | 1   | 6.0                                                            | 0         | ✅    |
| 6  | 13  | 3.91285743800967605994223485127                                | 0         | ✅    |
| 7  | 1   | 7.0                                                            | 0         | ✅    |
| 7  | 15  | 4.75428270822048742611863219756                                | 0         | ✅    |
| 8  | 1   | 8.0                                                            | 0         | ✅    |
| 8  | 17  | 5.61414818760147699187561645114                                | 0         | ✅    |
| 9  | 1   | 9.0                                                            | 0         | ✅    |
| 9  | 19  | 6.48871614570268011275830210887                                | 0         | ✅    |
| 10 | 1   | 10.0                                                           | 0         | ✅    |
| 10 | 23  | 7.30848258425932731110055681816                                | 0         | ✅    |

**18 / 18 pass** at the prompt's threshold `rel_err < 1e-15`
(mpmath dps = 50 inside `_sanity_check`, with `extraprec = 100`
on `polyroots`). The two non-zero rel_errors at d=3, β=5 and
d=5, β=11 (≈ 1.5e-51 and 1.7e-51) are well below the threshold
and reflect the radical-arithmetic precision floor at dps=50,
not a symbolic discrepancy.

No case split or symbolic failure appears at any d ∈ {5..10}.
The closed-form identity

> ξ_0(b) = d / β_d^{1/d}

reproduces in the same uniform way at every test point.

## A*.2 — AEAL cross-checks at d ∈ {2, 3, 4}

Independent verification that the Phase A* sweep's d ∈ {2,3,4}
results agree with the AEAL-anchored values from prior SIARC
sessions to ≥ 1e-15:

| d | β_d | expected ξ_0      | computed ξ_0      | rel_err | cached source |
|---|-----|-------------------|-------------------|---------|---------------|
| 2 | 3   | 2 / √3            | 2 / √3 (250 dig)  | 0       | PCF-1 v1.3 / Prompt 005 / CT v1.3 §3.3 |
| 3 | 1   | 3                 | 3.0               | 0       | Prompt 012 G2_CLOSED_AT_D3 (80 alg-digits) |
| 4 | 1   | 4                 | 4.0               | 0       | PCF2-SESSION-Q1 (spread = 0 across 8 reps, dps=80) |

**3 / 3 pass.** No `HALT_Q20A_REGRESSION_AT_PHASE_A`.

## Phase A* verdict

**`A_DIRECT_IDENTITY_d10`** — Q20's `A_DIRECT_IDENTITY` extends
cleanly from d ∈ {2, 3, 4} to d ∈ {2, …, 10} with no case
split, no symbolic instability, and no regression against
the AEAL-cached values at d ∈ {2, 3, 4}.

The Q20 closed-form identity ξ_0 = d / β_d^{1/d} is therefore
re-derived as a uniform algebraic identity over a 9-d window
without observed degree-induced pathology.

## Files

- `phase_a_star_extended_sweep.py` — wrapper; SHA-256 logged in `claims.jsonl`
- `phase_a_star_run.log` — run-time output
- `phase_a_star_results.json` — machine-readable summary
