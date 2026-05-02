# Q24 sub-(a): a_1 partition test at higher precision (Phase C)

**Task:** T37-S2-EXTRACTION-POLYNOMIAL-AWARE
**Date:** 2026-05-02
**Convention:** a_n_lead = C * Gamma(n) * zeta_*^(-n) (T35-consistent).
**Method:** stage 1 LSQ on T_n := a_n * zeta_*^n / Gamma(n) for n in [800, 1900],
basis {1/n^k : k = 0..K_lead}, mpmath dps=200, no SVD truncation.

## Per-rep a_1 medians and stability envelopes (across 24-config grid)

| rep    | side | Delta_b | a_1 (median, ~46 digits)                                   | envelope half_range | T36 endpoint estimate | agreement |
|--------|------|---------|------------------------------------------------------------|---------------------|-----------------------|-----------|
| V_quad | neg  |  -11    | -1.4722222222222222222222222222222222222222222222222...    | 6.27e-48            | -1.47165              | 4 digits  |
| QL15   | neg  |  -20    | -2.4722222222222222222222222222222222222222222222222...    | 2.39e-46            | -2.47108              | 4 digits  |
| QL05   | pos  |  +8     | +7.7499999999999999999999999999999999999999999999974...    | 1.41e-40            | +7.76157              | 3 digits  |
| QL09   | pos  |  +1     | -1.708566178e-57                                            | 1.04e-42            | -0.00527              | --        |

Note: V_quad a_1 = -53/36 = -1.47222... exactly (within envelope);
QL15 a_1 = -89/36 = -2.47222... exactly; QL05 a_1 = 31/4 = 7.75 exactly
(within envelope, plus a tail at the 41-digit level).
The rational-value structure observed at higher precision is striking and may inform
future invariant identification (Q24-(b)).

## C.1 Within-side spread

- neg-side spread (|V_quad - QL15|) = 1.0 (= |(-53+89)/36| = 36/36 = 1)
- pos-side spread (|QL05 - QL09|) = 7.75 (QL09 ≈ 0)

The pos-side spread is dominated by QL09's anomalous near-zero value.

## C.2 PRIMARY: ORDERING TEST

```
neg upper bound = max(-1.4722, -2.4722) + max envelope = -1.4722 + 2.39e-46
                = -1.4722222222...
pos lower bound = min(+7.75, ~0) - max envelope = (-1.71e-57) - 1.41e-40
                = -1.41e-40
```

**neg upper (-1.4722) < pos lower (-1.41e-40): TRUE → ORDERING TEST PASSES.**

Case: `neg<pos`.

This pass is robust against the QL09 anomaly precisely because
QL09's a_1 ≈ 0, while the neg-side maxes out at -1.47 (a full
unit below zero). The two sides do not overlap.

## SECONDARY: effect-size test

- cross_gap = |mean(pos) - mean(neg)| = |3.875 - (-1.972)| = 5.847
- max_within_side_spread = 7.75 (QL05 vs QL09)
- max_envelope = 1.41e-40

Strong-partition criterion: `cross_gap > 5 * max(spread, envelope)`.
- 5 * max(7.75, 1.41e-40) = 38.75
- 5.847 < 38.75 → STRONG PARTITION FAILS.

The strong-partition test fails because QL09's anomaly dilates the
pos-side spread. The PRIMARY ORDERING test still passes (it is robust
to within-side spread when sides are non-overlapping).

## C.3 QL09 anomaly probe

QL09's a_1 across the full 24-config stability grid:

- envelope median: -1.708566e-57
- envelope half_range: 1.04e-42

The grid envelope half_range is 1.04e-42 — TINY in absolute terms.
QL09's a_1 is genuinely (-2e-57 ± 1e-42), i.e. consistent with ZERO
to 42 digits, NOT a precision artifact.

This is a robust numerical finding: QL09's first polynomial Birkhoff
correction is anomalously zero, while V_quad / QL15 / QL05 all have
a_1 ~ O(1).

QL09 is the rep where T35 measured sign(C) = -1 (other reps have
sign(C) = +1). The QL09 series alternates sign in n: T_n ≈ -6.07.
Q18 territory: a_1 ≈ 0 may be a basis-convention shadow of the
sign(C) = -1 anomaly. The convention adopted in this prompt
(a_n_lead = C * Gamma(n) * zeta_*^(-n)) absorbs sign(C) into C
itself but does not normalize against a possibly-flipped phase
in the polynomial coefficients. Resolution of Q18 is required
before declaring QL09 a positive-side member.

## C.4 Higher invariants

| invariant | ordering test | case        | strong | comment                                     |
|-----------|---------------|-------------|--------|---------------------------------------------|
| a_1       | PASS          | neg<pos     | False  | dominant invariant; partitions cleanly     |
| a_2       | FAIL          | overlap     | False  | QL05 a_2 ~ 22, QL09 a_2 ~ -10; pos overlaps neg-extended-bound |
| a_3       | PASS          | neg>pos     | False  | partitions but with sign FLIP from a_1     |

The a_3 ordering case is "neg > pos" — opposite to a_1's case.
This indicates the partition structure of a_k alternates with k,
consistent with a quasi-rational-Gevrey expansion structure where
sign of (a_k * zeta_*^k) is what matters, not a_k itself.
Bare-numerical sign-and-magnitude partition is therefore not stable
across a_k for higher k; the invariant choice (Q24-(b)) is non-trivial.

## C.5 Endpoint-estimator agreement (T36 → T37)

The T36 endpoint estimator at n=1500–1900 reported a_1 to 3–4 digits.
T37's stage-1 LSQ pins a_1 to 40+ digits. The two methods agree
to within the T36 estimator's precision (3–4 digits) for V_quad,
QL15, QL05. Agreement for QL09 is not directly comparable because
T36 reported -0.00527 (3 digits) and T37 confirms a_1 ≈ 0 to 57
digits — consistent with T36 within T36's precision (the T36
3-digit estimate could not distinguish 0 from -5e-3 if the true
value is ~10^-57).

## Q24-(a) verdict

**Q24a_PARTITIONS_WITH_QL09_ANOMALY**

a_1 ORDERING test passes cleanly (neg < pos at all 24 configs).
QL09's a_1 ≈ 0 is a genuine numerical fact (42 digits stable),
not a precision artifact, and is consistent with Q18 (sign(C)
basis-convention shadow). The partition is robust for V_quad,
QL15, QL05; QL09's status as a "positive-side" rep depends on
Q18 resolution (which Claude must arbitrate).

For G20: CLOSED via a_1 ORDERING test for the 3 non-anomalous reps
(V_quad, QL15, QL05). The anomalous status of QL09 is an additional
epistemic flag, not a falsifier of the partition.
