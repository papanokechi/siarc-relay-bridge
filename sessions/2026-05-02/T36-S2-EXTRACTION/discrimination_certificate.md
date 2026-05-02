# T36-S2-EXTRACTION discrimination certificate (HALT state)

**Date:** 2026-05-02   **Verdict:** `HALT_T36_S2_RICHARDSON_DIVERGED`
(secondary halt key: `T36_S2_CROSSMETHOD_MISMATCH`).

S_2 was NOT extracted.  The G6b discrimination test at the second
Stokes-multiplier scale therefore remains OPEN; structural-pattern
analyses (|S_2|, arg(S_2), R := S_2/S_1^2, residual beta_R) cannot be
populated.  This certificate documents the halt cause and the
diagnostic measurement that we DID obtain in its place.

## Halt cause: polynomial-in-1/n corrections to the leading Birkhoff term

Convention check `a_n / (C * Gamma(n) * zeta_*^(-n)) -> 1` measured at
n in {1500, 1700, 1900} for the cached T35 dps=250 / N=2000 series.
Prompt 016 §2 Phase B requires >= 60-digit agreement; we measure ~3
digits (i.e. the ratio decays like 1 + a_1/n with a_1 of O(1)).

| rep    | side | n=1500 ratio  | n=1700 ratio  | n=1900 ratio  | agree-with-1 digits (max over n) |
|--------|------|---------------|---------------|---------------|----------------------------------|
| V_quad | neg  | 0.999019      | 0.999134      | 0.999225      | 3.111                            |
| QL15   | neg  | 0.998353      | 0.998547      | 0.998699      | 2.886                            |
| QL05   | pos  | 1.005176      | 1.004566      | 1.004085      | 2.389                            |
| QL09   | pos  | 0.999996      | 0.999997      | 0.999997      | 5.557                            |

The 1/n decay (rather than the predicted exponential `(1/2)^n` decay
toward 1) means the d=2 PCF Birkhoff series carries non-trivial
polynomial-in-1/n corrections to the leading amplitude.  Phase C's
extraction
`R_n := r_n * (2 zeta_*)^n / Gamma(n) -> S_2 / (2 pi i)`
therefore amplifies the polynomial residual exponentially (`R_n` grows
like `2^n / n^k`) rather than converging.  Cross-method digit agreement
between Richardson order-30 and LSQ-in-(1/n) at the top window is
~10^-15 digits across all four reps — manifestly noise.

## What we extracted instead: the first polynomial correction a_1

Endpoint estimator on `s_n := n * (a_n / a_n_lead - 1)` (Richardson
order-40 over n in [200, 1500); endpoint sanity values at n=1500 and
n=1900 used as cross-checks).  Source: `extract_a1.py`,
output `a1_polynomial_corrections.csv`.

| rep    | side | A_pred | Delta_b | a_1 (3-4 digits)         | s(1500) vs s(1900) agreement digits |
|--------|------|--------|---------|--------------------------|--------------------------------------|
| V_quad | neg  | 3      | -11     | -1.47165 ...             | 3.987                                |
| QL15   | neg  | 3      | -20     | -2.47108 ...             | 3.911                                |
| QL05   | pos  | 4      | +8      | +7.76157 ...             | 3.402                                |
| QL09   | pos  | 4      | +1      | -0.00527 ...             | 2.852                                |

Observations (we report; we do not interpret):
- Within the neg side, both reps have negative a_1 of order -1 to -2.5
  (V_quad ~ -1.47, QL15 ~ -2.47).
- Within the pos side, the two reps have a_1 of opposite sign and
  vastly different magnitude (+7.76 vs ~ -0.005).
- QL09's a_1 is anomalously close to zero (~ 5e-3); this matches the
  prior T35 anomaly that QL09's leading C is negative while the other
  three reps' C is positive (Q18 territory).
- a_1 does NOT cleanly partition by side at this 3-digit precision.

## Convention check (literal prompt-016 vs T35-consistent)

Prompt 016 §2 Phase B literally writes
`a_n_lead = (C / 2pi) * Gamma(n) * zeta_*^(-n)`.
Under that literal reading the convention check would yield
`a_n / a_n_lead -> 2 pi`, falsifying T35's V_quad amplitude (which
matches CC-MEDIAN-RESURGENCE-EXECUTE to 49 displayed digits).  We
adopted the T35-consistent convention `a_n_lead = C * Gamma(n) *
zeta_*^(-n)` so that the test could be informative.  The deviation
is documented in `rubber_duck_critique.md`.

## What this means for G6b and Q19

- **G6b** (S_2 cluster-by-side): cannot be evaluated at this dps with
  the prompt's leading-only ansatz.  Recommended Prompt 018 strategy:
  joint-fit (a_1, ..., a_K) with C via constrained-LSQ, then peel and
  apply Richardson at the 2 zeta_* scale.
- **Q19** ("beta_R = 0 universal at d=2 implies no Gamma-shift in the
  resurgence ladder"): T36 does not contradict Q19, but does sharpen
  it.  beta_R = 0 characterises the leading Gamma argument; it does
  NOT imply that the polynomial-in-1/n coefficients of the leading
  amplitude vanish.  The four measured a_1 values above are direct
  evidence of non-zero polynomial corrections.

## AEAL claims

11 entries in `claims.jsonl` (4 convention-check failures, 1 phase-C
divergence diagnostic, 4 a_1 endpoint measurements, 1 structural
finding, 1 verdict).
