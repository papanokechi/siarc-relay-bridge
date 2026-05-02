# T36 rubber-duck critique

## Why we deviated from PROMPT 016 §2 Phase B literal text

Prompt 016 §2 Phase B literally writes

    a_n_lead := (C / 2pi) * Gamma(n) * zeta_*^(-n)

Under that literal reading, `a_n / a_n_lead -> 2 pi` (not 1), and the
prompt's own convention check would always trip
`T36_CONVENTION_MISMATCH`.  This would also falsify T35's reported
V_quad amplitude `C = 8.127336795...`, which matches
CC-MEDIAN-RESURGENCE-EXECUTE to 49 displayed digits.  We adopted the
T35-consistent convention

    a_n_lead := C * Gamma(n + beta_R) * zeta_*^(-n) ,   with beta_R = 0,

so that the convention check could be informative.  The connection
label `S_1 = 2 pi i C` does NOT introduce a `(2 pi)` factor in the
leading approximant under T35's amplitude definition; it is a
labelling convention on the connection coefficient, not on the
asymptotic series.

## What the 1/n decay of the convention-check ratio actually tells us

`a_n / a_n_lead -> 1` is observed at the **1/n rate**, not exponentially.
Concretely, `a_n / a_n_lead - 1 ≈ a_1 / n` with `a_1` of O(1) for three
of four reps (and ~ 0 for QL09).  This **falsifies the working
hypothesis** that the T35-measured `beta_R = 0` (G19 row) is enough to
characterise the leading asymptotic of the series — the asymptotic
expansion has the standard form

    a_n = C * Gamma(n) * zeta_*^(-n) * (1 + a_1/n + a_2/n^2 + ...)

with non-zero polynomial-in-1/n corrections that T35's beta_R = 0
finding did not address.

## Why Phase C diverged

Define `r_n := a_n - a_n_lead` and `R_n := r_n * (2 zeta_*)^n / Gamma(n)`.
If the residual were purely the next ladder rung at 2 zeta_*, then
`R_n -> S_2 / (2 pi i)` (bounded).  But

    r_n ≈ C * (a_1/n) * Gamma(n) * zeta_*^(-n)  +  S_2/(2 pi i) * Gamma(n) * (2 zeta_*)^(-n) + ...

so `R_n ≈ C * a_1 * 2^n / n + (S_2/(2 pi i)) + ...`.  The leading term
**diverges as `2^n / n`**.  The empirical `R_inf` reported by the
runner (~10^654) is precisely this divergence; it is **not** an S_2
estimate and we explicitly do not record it as one.

## Q18 (basis-convention) and Q19 (beta_R = 0)

- **Q18:** QL09's leading `C` is negative while V_quad/QL15/QL05 are
  positive.  We have NOT resolved Q18 in this session.  The optional
  Phase F probe (re-run QL09 with `c = -2/sqrt(alpha)`) was NOT
  performed — Phase C divergence consumed the budget and a basis
  flip alone would not bear on the polynomial-correction issue
  uncovered here.
- **Q19:** T35 measured `beta_R` consistent with 0 to >= 85 digits
  across all four reps, and we do NOT contradict that.  But the
  G19 manuscript-row interpretation as "no Gamma-shift in the
  resurgence ladder, full stop" needs sharpening: it pins down the
  leading Gamma argument only.  The polynomial-in-1/n coefficients
  `(a_1, a_2, ...)` are independent and we have measured `a_1` to
  3-4 digits per rep here.

## What Prompt 018 should do differently

1. Joint-fit `(a_1, ..., a_K)` with C via constrained-LSQ on
   `T_n = a_n * zeta_*^n / Gamma(n)` over a window where the
   polynomial decay dominates the next-ladder-rung signal.  K must be
   large enough that the polynomial residual at the inner window is
   below the dps-250 noise floor, i.e. K ~ 30-50.
2. Subtract the FULL polynomial-leading expansion to get a clean r_n.
3. Only then apply Richardson on R_n at the 2 zeta_* scale.

Alternative: extend the cached series at a higher dps (300-400) and
larger N (5000-10000), then revisit.  That is non-trivial compute
and was explicitly out of scope here.

## Forbidden-verb hygiene

The discrimination certificate and this critique have been grep'd
for "shows / confirms / proves / demonstrates / establishes" in
predictive contexts; no offending matches.  Where these words appear
in methodological prose ("we measure", "we report") they are
methodological, not epistemic.

## Verdict

`HALT_T36_S2_RICHARDSON_DIVERGED` (secondary key
`T36_S2_CROSSMETHOD_MISMATCH`).
