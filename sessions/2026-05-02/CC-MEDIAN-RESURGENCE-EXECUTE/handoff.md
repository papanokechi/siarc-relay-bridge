# Handoff — CC-MEDIAN-RESURGENCE-EXECUTE
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~120 minutes
**Status:** COMPLETE

## What was accomplished

Executed the median Écalle resurgence calculation that CT v1.3 §3.5
records as Theory-Fleet H4's HIGH-confidence theoretical prediction.
The V_quad Birkhoff formal series was extended to N=5000 coefficients
at mpmath dps=250, the branch exponent at the Borel singularity
ζ* = 4/√3 was fitted by three independent extractors, and the leading
alien amplitude `C` (and hence the Stokes constant `S_{ζ*} = 2 π i C`)
was extracted to >= 108 digits — well past the H4 forecast band of
30–50 (central 40). Verdict: **H4_EXECUTED_PASS_108_DIGITS**.

## Key numerical findings

- `a_n` series extended to n=5000 at dps=250 via a closed-form four-term
  recurrence derived from the Newton-polygon characteristic balance;
  bit-validated against the matrix-method `formal_solve` of CC-PIPELINE-G
  at K=20, dps=80. Hash:
  `0b9e656f08b5b1dae67ebaffa5456e3625594b8e4c1904b4d0b2487ab30687cd`
  (script: `median_resurgence.py`).
- Branch exponent **β = 0 to ≥ 107 digits** (M1 ratio = 2.19e-108,
  M2 three-point = 1.47e-107, M3 second-difference of log = 1.47e-107).
  Methods agree to 106.9 absolute digits — well past the 8-sig-fig
  consistency threshold (script: `median_resurgence.py`).
- Alien amplitude
  `C = 8.12733679549507236711257873202358318226454272233879...`
  via Phase C iterated Richardson on the deepest window
  `n ∈ [4495, 4995)` (script: `median_resurgence.py`).
- Cross-check via Phase D polynomial-LSQ in 1/n at order 40 (genuinely
  algebraically distinct from Phase C) agrees with C to **108.39 digits**
  (script: `median_resurgence.py`).
- Final Stokes constant
  `S_{ζ*} = 2 π i C ≈ 51.06556313995466226983167460994566... i`
  (purely imaginary; convention: leading B[Φ_{ζ*}] = 1).

## Judgment calls made

1. **Switched Phase D method.** The H4 recipe step 3 prescribes "local
   Borel singular-germ Padé-of-Padé fit". For β = 0 (log singularity),
   the natural local-germ ratio `b_n · ζ*^n · n^{1-β}` is identical
   (modulo Stirling) to Phase C's `a_n · ζ*^n / Γ(n+β)`, so the original
   formulation collapses to roundoff equality with Phase C and is NOT a
   genuine cross-check. Replaced with polynomial LSQ in 1/n at order 40
   (Gauss elimination on the (41×41) normal-equation system). This is a
   genuinely independent algebraic procedure; the 108-digit agreement is
   the HONEST cross-check digit count. Documented in
   `rubber_duck_critique.md` and `unexpected_finds.json`.
2. **Adopted M3 = second-difference-of-log instead of LSQ on log|a_n|.**
   The original LSQ M3 did not include 1/n correction terms and gave
   biased β estimates (~0.002) that did not accelerate to zero. Replaced
   with `β = 1/(exp(Δ² log a_n) - 1) - n + Richardson`, which is a clean
   third-order eliminator and converges to β = 0 at the working precision.
3. **Did NOT attempt closed-form recognition (PSLQ).** H4 recipe step G
   was deferred; outside the prompt 005 scope.
4. **Phase A used a direct banded recurrence** rather than the matrix
   method of CC-PIPELINE-G. The matrix method is O(K²) memory and would
   require ~50 GB at K=5000, dps=250. The recurrence is O(K) memory and
   completes in 0.2s; cross-validated bit-for-bit at K=20.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION.**

1. **Normalization map V_quad → P-III(D₆).** CT v1.3 §3.5 flags the
   normalization map between V_quad's native Birkhoff expansion and
   P-III(D₆)'s isomonodromic Stokes/monodromy data as a SEPARATE
   RESIDUAL of op:cc-formal-borel. The Stokes constant reported here
   (`S_{ζ*} ≈ 51.0655631399... i`) is in V_quad's native normalization,
   NOT P-III(D₆)'s. **Closing op:cc-formal-borel for V_quad to the
   Stokes-data side, which the prompt asserts the PASS verdict would
   accomplish, REQUIRES this map to be documented.** It is the remaining
   open residual.
2. **β = 0 (logarithmic), not the half-integer expected by H4.** H4's
   summary said "expected square-root class component, but exponent
   must be fitted". β = 0 is the boundary case of the algebraic class
   (α = 0 in `(1 - w/ζ*)^{-α}`), corresponding to a LOGARITHMIC Borel
   singularity, `B(w) ~ -C log(1 - w/ζ*) + analytic`. This is consistent
   with H4's broader "simple-resurgent algebraic-LOGARITHMIC branch
   point" characterisation but refines the half-integer expectation.
   The HALT condition `H4_PREDICTION_FALSIFIED` does not trigger
   because (a) achieved digits 108 >> threshold 10, and (b) no specific
   β was prescribed in `predictions.json` to compare against.
3. **108-digit cross-check far exceeds H4 forecast (30–50).** The H4
   forecast was based on Padé-Borel-Laplace global resummation. Direct
   Richardson on the large-n tail bypasses that route and saturates at
   working precision dps=250. Is this anomaly an artefact of the chosen
   acceleration or a genuine property of the V_quad coefficients? See
   `rubber_duck_critique.md` point 5.
4. **Phase C and Phase D both consume the SAME `a_n` series.** A truly
   independent cross-check via direct Borel-Padé evaluation at the
   singularity (the H4 recipe's strict reading) was NOT implemented.
   My cross-check is "two algorithmically distinct accelerations on
   the same large-n tail", validated against the matrix-method
   recurrence at K=20. **A direct Borel-Padé verification remains an
   open task** if Claude wants stronger algebraic independence.
5. **The three M1/M2/M3 fits of β resolved within tolerance but
   stretched it.** M1 = 2.19e-108 vs M2 = 1.47e-107 differ by a factor
   of 7 in the leading nonzero residual digit at the 107th decimal
   place. Absolute-tolerance digit count = 106.9 (passes the >= 8
   threshold by a wide margin), but the relative-tolerance metric
   would reject these as "completely disagreeing". The mixed metric
   (absolute when values are near zero) was adopted because β = 0
   exactly is consistent with all three methods at the working precision.

## What would have been asked (if bidirectional)

- "Should the Phase D cross-check be implemented as a direct Borel-Padé
  evaluation at ζ*, or does the polynomial-LSQ-in-1/n cross-check
  satisfy the prompt?"
- "Is it acceptable to declare PASS at 108 digits even though the
  H4-prescribed local-germ Padé-of-Padé fit was substituted with a
  numerically distinct procedure?"
- "Is the normalization map to P-III(D₆) within scope of this prompt
  or to be deferred to a follow-up prompt (op:cc-formal-borel residual)?"

## Recommended next step

Issue a follow-up prompt **CC-VQUAD-PIII-NORMALIZATION-MAP**:
1. Construct the explicit map between the V_quad Birkhoff formal series
   `S_+(u) = 1 + Σ a_k u^k` (with `c0 = 2/√3`, `ρ = -11/6`) and the
   P-III(D₆) Riemann-Hilbert normalisation at the relevant boundary
   condition.
2. Read off the P-III(D₆) Stokes/monodromy datum that should equal
   `S_{ζ*} ≈ 51.06556... i` after the map.
3. Match the two values to confirm op:cc-formal-borel can be flipped
   to DIAGNOSED. This is the key residual, not the numerical extraction.

Optionally, **CC-MEDIAN-RESURGENCE-PSLQ**: closed-form recognition of
C = 8.127336795... against `Γ(1/3), Γ(2/3), Γ(1/6), Γ(5/6), π, log 2,
log 3, √3` and elementary P-III(D₆) Stokes constants.

## Files committed

- `median_resurgence.py` — end-to-end executable script (Phases A–E),
  deterministic at dps=250.
- `Qn_5000_dps250.csv` — 5001 coefficients of `S_+(u)` at full
  dps=250 precision (1.3 MB).
- `phaseA_series.log` — Phase A timing/sanity log.
- `fit_branch_exponent.log` — Phase B raw output, four windows,
  three methods.
- `stokes_extraction.log` — Phase C raw output.
- `local_germ_crosscheck.log` — Phase D raw output.
- `S_zeta_star_digits.txt` — final S_{ζ*} value at full dps=250.
- `verdict.md` — H4_EXECUTED_PASS_108_DIGITS.
- `claims.jsonl` — 8 AEAL claims (H4-A1 through H4-A8).
- `halt_log.json` — empty `{}` (no halt triggered).
- `discrepancy_log.json` — empty `{}` (no internal discrepancy).
- `unexpected_finds.json` — three notable findings (β = 0 vs
  expected half-integer; digit count >> forecast; S_{ζ*} purely
  imaginary).
- `rubber_duck_critique.md` — self-audit before sign-off.
- `handoff.md` — this file.

## AEAL claim count

**8** entries written to `claims.jsonl` this session (H4-A1 through H4-A8).
