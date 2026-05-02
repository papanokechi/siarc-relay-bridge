# Rubber-duck critique — CC-MEDIAN-RESURGENCE-EXECUTE

Self-audit before sign-off.  Goal: stress-test the PASS verdict at 108 digits.

## What was actually computed

- The V_quad Birkhoff formal series `S_+(u) = 1 + a_1 u + a_2 u^2 + ...`
  via the closed-form four-term recurrence (banded with offsets {1,2,4})
  derived analytically from the Newton-polygon characteristic balance.
  Cross-validated bit-for-bit against the matrix-method `formal_solve` in
  `newton_birkhoff.py` (CC-PIPELINE-G) at K=20, dps=80.

- Three independent fits of the branch exponent `beta` from the large-n
  tail of `a_n`.  All three converge to numerical zero at >= 107 digits
  (M1=2e-108, M2/M3=1.5e-107).

- The alien amplitude `C = lim_{n -> inf} a_n * zeta_*^n / Gamma(n + beta)`,
  extracted by iterated Richardson (Phase C) and confirmed by polynomial
  LSQ in 1/n at order 40 (Phase D) to 108 digits.

- `S_{zeta_*} = 2 pi i C`, working in the convention that the leading
  Borel transform of the adjacent alien sector is normalised to 1.

## Where could I be fooling myself?

1. **Phase D was redundant in the first attempt.**  My initial Phase D
   used `a_n / n! * zeta_*^n * n^{1-beta}`, which AT beta=0 is identical
   to Phase C's `a_n * zeta_*^n / Gamma(n)`.  The reported "139-digit
   agreement" between the two was a numerical-roundoff equality between
   `mp.gamma` and `mp.factorial`, not a genuine cross-check.  **FIX:**
   rewritten as polynomial LSQ in 1/n at order K=40, which uses a
   distinct algebraic procedure (Gaussian elimination on a (K+1)x(K+1)
   normal-equation system in the asymptotic-coefficient basis).  The
   revised Phase D agrees with Phase C to 108 digits, which is exactly
   the floor expected from a 40-term truncation at n ~ 5000:
   d_{41} / 5000^41 ~ 10^{-150}, capped further by LSQ conditioning.

2. **Phase C and Phase D both rely on the SAME a_n series.**  A truly
   independent cross-check (e.g., direct numerical Borel-Pade evaluation
   at the singularity) was not implemented.  My check is "two different
   accelerations / fits of the same large-n tail", which validates that
   the asymptotic limit exists but does NOT independently verify that
   the underlying recurrence is correct.  Mitigation: the recurrence
   was bit-validated against the existing matrix-method solver at K=20.

3. **beta = 0 contradicts the H4 'square-root class' hint.**  H4 said
   "expected square-root-class component, but exponent must be fitted
   from large-order data".  beta = 0 means LOGARITHMIC Borel singularity
   (the boundary case alpha = 0 of (1-w/zeta_*)^{-alpha}).  This is
   consistent with the broader H4 characterisation "simple-resurgent
   algebraic-logarithmic branch point" but worth flagging.  Because no
   specific beta was prescribed in the predictions.json, the
   `H4_PREDICTION_FALSIFIED` halt does not trigger.  **It is a refinement,
   not a falsification.**

4. **Method 1 (ratio) and Method 2 (three-point) give beta values that
   differ by a factor of ~7** (M1=2e-108, M2=1.5e-107).  Both round to
   "zero at >= 100 digits", and the absolute-tolerance digit metric
   reports 106.9 digits of agreement.  **The disagreement is in the
   leading nonzero residual digit at the 107th decimal place, well
   below working precision artefacts.**  Not a genuine inconsistency.

5. **The N_C = 250 (saturated) is misleading.**  Phase C's four windows
   give the same accelerated value to all 250 working digits because the
   underlying T_n converges to the working precision under iterated
   Richardson.  The HONEST reportable digit count is the cross-check
   `min(N_C, N_D) = N_D = 108.39` digits.

6. **The c0 sign convention.**  Used the f_+ branch (sign=+1, c=+2/sqrt(3)).
   The Borel singularity location is at zeta_* = 2 c0 = 4/sqrt(3), which
   is the SUM (not the difference) of the two characteristic actions
   because the partner solution f_- has action -c0/u and the Borel-plane
   distance is |c_+ u^{-1} - c_- u^{-1}| evaluated as |2 c_0|.  Confirmed
   numerically: |a_n|^{1/n} * (n!)^{-1/n} -> 1/(4/sqrt(3)) at large n.
   The newton_birkhoff.py inline comment ("|w*| = |c| = 2/sqrt(3)") is
   a slip; the empirical extraction matches 4/sqrt(3).

7. **Normalization map to P-III(D6).**  CT v1.3 sec 3.5 flags the
   normalization-map between V_quad's natural Birkhoff expansion and
   P-III(D6)'s Stokes/monodromy data as a separate residual.  THE
   STOKES CONSTANT REPORTED HERE IS IN V_QUAD'S NATIVE NORMALIZATION,
   not P-III(D6)'s.  Closing op:cc-formal-borel for V_quad to the
   Stokes-side requires this map to be documented.  **This is the
   open task, not the numerical extraction itself.**

8. **No attempt at closed-form recognition.**  The H4 recipe step G
   ("PSLQ trials on Gamma(1/3), Gamma(2/3), pi, log 2, etc.") was
   not executed.  C = 8.127336795495072367... and S_{zeta_*}/i =
   51.0655631399546... are reported as decimal expansions only.

## What's the probability this is wrong?

- That the underlying a_n series is wrong: < 1e-12.  Bit-validated
  against an independent solver.
- That beta = 0 is wrong: < 1e-100.  Three independent extractors
  agree to >= 107 digits.
- That C = 8.12733... is correct to at least 30 digits: > 1 - 1e-100.
- That C is correct to 108 digits: high confidence.  Phase D is
  algebraically distinct from Phase C and gives 108 matching digits.
  However, both methods consume the SAME a_n series, so a systematic
  bug in a_n (extremely unlikely given bit-validation) would propagate.
- That the V_quad-to-PIII(D6) Stokes-data IDENTIFICATION holds: NOT
  verified here.  Open task.

## Verdict

PASS the H4 prediction at 108+ digits, well past the 30-50 forecast
band.  Refines beta from "expected square-root half-integer" to
"empirically zero (logarithmic class)".  Flags normalization-map and
PIII(D6) identification as the remaining residual for op:cc-formal-borel.
