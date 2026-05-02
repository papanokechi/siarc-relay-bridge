# Feasibility certificate — T37-S2-EXTRACTION-POLYNOMIAL-AWARE

**Verdict:** `T37_PARTIAL_a_1_PARTITIONS`

**Methodology validated; D extraction infeasible from cached series; a_1 partitions cleanly.**

## What this prompt established (positively)

1. The TWO-STAGE windowed-fit architecture (Stage 1 lead-only on
   high-n window with K_lead=25 in basis {1/n^k}; Stage 2 next-rung on
   residual at low-n window) is METHODOLOGICALLY VALID for stage 1.
   It cleanly recovers C and (a_1, ..., a_K) to 40+ digits across all
   four representatives, agreeing with T35's leading-amplitude
   measurement of C to 55–64 digits.

2. The first polynomial Birkhoff correction a_1 PARTITIONS the Delta_b
   sign dichotomy via the Phase C ORDERING test:
   - V_quad (Delta_b=-11, neg): a_1 = -1.4722222... (= -53/36) to 46 digits
   - QL15   (Delta_b=-20, neg): a_1 = -2.4722222... (= -89/36) to 46 digits
   - QL05   (Delta_b=+8,  pos): a_1 = +7.7499999... (= +31/4) to 41 digits
   - QL09   (Delta_b=+1,  pos): a_1 ≈ -1.7e-57 to 42 digits  (anomaly)
   neg upper -1.4722 < pos lower ~0; sides do not overlap.

3. QL09's a_1 ≈ 0 (to 42 digits) is a STABLE numerical finding,
   not noise — consistent with Q18 sign(C) basis-convention shadow.
   Reported as anomaly for Claude review but does NOT block partition.

## What this prompt established (negatively)

4. The next-rung amplitude D = beta_0 / 2 is NOT extractable from
   the cached dps=250/N=2000 series with the polynomial-aware fit
   architecture at K_next ∈ {4, 6} and windows ∈ {[40, 100], [60, 120]}.
   D varies 4-10 orders of magnitude across the 24-config grid for
   all 4 reps; envelope half_range / |median| > 10^4 in every case.
   Specifically:

   | rep    | D_median            | D_envelope_min | D_envelope_max | half_range / |median| |
   |--------|---------------------|----------------|----------------|------------------------|
   | V_quad | -1.13e-9            | -3.20e-1       | +1.03e+1       | 4.7e+9                 |
   | QL15   | +1.45e-9            | -1.42e+1       | +3.32e+1       | 1.6e+10                |
   | QL05   | +3.38e-5            | -3.55e+1       | +1.34e+6       | 2.0e+10                |
   | QL09   | +5.85e-2            | -6.65e-5       | +4.48e+4       | 3.8e+5                 |

   This triggers the soft halt T37_K_SENSITIVITY_DIVERGENT.
   D's envelope also straddles zero in all four cases, triggering
   T37_D_CONSISTENT_WITH_ZERO.

5. Phase B.6 free-beta_2 diagnostic is INCONCLUSIVE: residual
   decreases monotonically across the scanned beta_2 ∈ [-2, +2],
   with no local minimum. The reported beta_2 ≈ +2.10 for all four
   reps is a scan-boundary artifact, not a genuine next-sector
   exponent. The data-precision afforded by the cached series does
   NOT identify beta_2; the structural question (is beta_2 = 0 or
   nonzero?) remains open.

## Why D cannot be extracted from cached data

The fundamental obstruction is a basis/precision conflict:

- The leading-Birkhoff polynomial 1 + a_1/n + a_2/n^2 + ... is a
  divergent (Gevrey-1) asymptotic series with rate R = 2*zeta_*.
  Its TRUE coefficients grow factorially: |a_k| ~ k! / R^k.

- The CSV-cached series stores a_n at ~80 significant decimal
  digits (despite dps=250 internal at the time of the T35 run).
  This places a hard precision floor on T_n at ~10^-80 in the
  fit window.

- For the K_lead=25 polynomial fit on n in [800, 1900], the smallest
  basis function 1/800^25 ~ 10^-72 is just above the noise floor;
  K_lead = 25 is the upper edge of the well-conditioned regime.
  K_lead in {30, 40} (the original spec) overfits noise (probe_K.py
  shows that K=40 evaluated at n=40 produces values ~ -2e+50 because
  the noise-driven high-k coefficients amplify enormously when
  extrapolated). This is a CRITICAL methodological correction
  documented in rubber_duck_critique.md.

- At the chosen K_lead = 25, the polynomial extrapolation from
  [800, 1900] to [40, 100] is clean (truncation error ~ 10^-26),
  but the EXTRAPOLATION ITSELF dominates the next-rung 2^(-n) signal
  by a basis-dependent amount: the asymptotic-series tail at K_eff = 25
  is structurally entangled with the next-rung contribution at low n.

- Stage 2 fits a polynomial in 1/n times 2^(-n) to a residual that
  is ALREADY small (≤ 10^-26 at n=40); the fit absorbs the residual
  via large cancelling beta_k coefficients, and the b_0 coefficient
  (which we identify with D) varies wildly across (K_lead, K_next,
  windows) because of basis cancellation.

## What 017d would need to fire on cached data

For the next prompt (017d, full S_2 closure) to fire, the D-feasibility
gate must hold for at least some reps:
- D_envelope_half_range / |D_median| < 0.05
- D_envelope excludes 0
- Stage 2 residual within tolerance
- Cross-window holdout passes

NONE of these hold currently. 017d cannot fire on the dps=250/N=2000
cached data with the two-stage fit architecture. Two paths forward:

(A) **Extended-recurrence fallback (Phase F-style).** Re-run the
    Birkhoff recurrence at dps=400, N=5000 (~1 hr per rep on single
    laptop). With CSV noise floor at 10^-150 and K_lead extended
    to ~50, the polynomial extrapolation envelope will tighten and
    the next-rung 2^(-n) signal at n=200-300 (where 2^(-n) ~ 10^-90
    is now above noise) becomes measurable.

(B) **Methodology pivot to Borel/Padé.** Replace the polynomial-fit
    + extrapolation approach with a Borel transform / Padé approximant
    extraction of the alien amplitude. This is the standard resurgence
    method and avoids the basis-cancellation issue entirely.

Recommendation: (B) is more elegant but requires a separate prompt
to design and validate. (A) is a brute-force fallback that this
session DID NOT execute (Phase F was conditional and the verdict
ladder did not require it; the spec defers Phase F to a follow-up).

## What this prompt RECEIVES (D as preliminary input for Claude)

`d_extraction_feasibility.json` records per-rep:
- C_median (49+ digits agreement with T35)
- a_1 / a_2 / a_3 medians (40+ digits each)
- D_median, D_envelope_min, D_envelope_max, half_range
- S_2_provisional = 2*pi*i*D_median (PRELIMINARY ONLY; not a closure)
- feasibility flag (BLOCKED for all 4 reps)

The S_2_provisional values are NOT to be used as closure values
under any conditions. They are kept in the file as zero-cost
diagnostic data for cross-check against future extended-precision
runs.

## Gate status (operative)

- **G6b** (S_2 closure / Stokes-side discrimination at next-rung):
  PARTIAL+DEEPER. D extraction infeasible from cached data; awaits
  extended-recurrence run or Borel/Padé pivot.
- **G19** (residual beta_R / leading-amplitude pinning): UNCHANGED
  by this session; T35's beta_R = 0 measurement holds.
- **G20** (does first-polynomial-correction a_1 partition Delta_b
  sign?): CLOSED via a_1 ORDERING test for V_quad, QL15, QL05;
  QL09 sub-flagged as Q18 anomaly (a_1 ≈ 0 to 42 digits).
- **Q18** (sign(C) basis-convention): unresolved here; QL09's a_1
  anomaly is fresh evidence that may help Claude triangulate.
- **Q24-(a)**: ANSWERED EMPIRICALLY. ORDERING test passes;
  effect-size strong-partition fails due to QL09 dilation. Claude
  arbitrates the *interpretive* status (whether the partition
  "counts" given QL09).
- **Q24-(b)** (which invariant): a_3 also partitions but with sign
  FLIP from a_1; a_2 does not partition. Pattern suggests sign
  alternation across a_k; possibly the right invariant is
  (a_k * zeta_*^k) or similar dimensionful product.

## Status flag

`T37_PARTIAL_a_1_PARTITIONS`

Methodology validated; G20 closes (with QL09 sub-flag); G6b stays
PARTIAL+DEEPER. 017d cannot fire on cached data; recommend either
extended-recurrence fallback (Phase F) or Borel/Padé pivot for
future S_2-closure work.
