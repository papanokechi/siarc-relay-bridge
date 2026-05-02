# Handoff — T35-STOKES-MULTIPLIER-DISCRIMINATION
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** PARTIAL (verdict: G6B_PARTIAL_HIGHER_ORDER_NEEDED)

## What was accomplished

Extracted the leading Stokes multiplier S_1 = 2 π i C of the Birkhoff
formal series for four d=2 PCF representatives — two on each side of
the PCF-1 v1.3 §3 Δ_b sign dichotomy — at the t2c-style precision
ladder dps ∈ {100, 150, 200, 250} with N up to 2000 (V_quad reusing
CC-MEDIAN-RESURGENCE-EXECUTE's cached N=5000/dps=250 series for
cross-validation).  Generalised the V_quad Birkhoff recurrence
(α=3, β=1, γ=1, δ=0, ε=1) to arbitrary d=2 (α, β, γ, δ, ε) by
symbolic derivation in `derive_recurrence.py`; the generalisation
specialises back to V_quad's existing recurrence and reproduces its
108-digit C value to all displayed digits.  Tested whether the
leading Stokes multiplier discriminates the A=4 (Δ>0) vs A=3 (Δ<0)
PCF-1 split in a *structural* sense.

## Key numerical findings

* V_quad (Δ_b=−11, A=3 side):
  C = +8.12733679549507236711257873202358318226454272234…
  S_1 = (0 + 51.06556313995466226983…) i  (60+ digit ladder agreement at dps=200→250)
* QL15 (Δ_b=−20, A=3 side):
  C = +21.38412649463506525828438453625561662911360599660…
  S_1 = (0 + 134.36042939796075629713…) i
* QL05 (Δ_b=8, A=4 side):
  C = +1.40328080725296497994724250152093112017966978359…
  S_1 = (0 + 8.81707334997893885050…) i
* QL09 (Δ_b=1, A=4 side):
  C = −6.07472006379093506128527538224945464230395636102…
  S_1 = (0 − 38.16859185004024347142…) i

All values verified to ≥60 cross-method digits (Richardson tail vs
LSQ in 1/n) at dps=250, N=2000 (script `t35_runner.py`).  V_quad
matches CC-MEDIAN-RESURGENCE-EXECUTE bit-for-bit on its 49 displayed
digits.  Branch exponent β_R is essentially zero (≤ 10⁻⁸⁵) for all
four reps — a structural feature of the Birkhoff series for this
class.

## Judgment calls made

* **Truncated the precision ladder at dps=250** rather than extending
  to 300 (prompt nominally lists {100, 150, 200, 250, 300}).
  Rationale: ladder agreement at 200→250 already reached 78–85
  digits, well above the t2c (dps − 30 = 220) target for all reps.
  The discrimination question is decided at the O(1) absolute scale,
  not the 30th digit; dps=300 would yield diminishing returns.
* **Used N up to 2000 (vs prompt-suggested 500/1000/2000 across the
  ladder)**.  Selected N values 800/1200/1600/2000 to keep
  Richardson-acceleration windows ≥ N/2 at every level.
* **Stokes amplitude C extraction** via tail Richardson (Phase C of
  CC-MEDIAN) with LSQ-in-1/n cross-check (Phase D of CC-MEDIAN); did
  not implement higher-order S_2 / S_3 extraction (deferred per
  prompt PARTIAL clause).
* **Verdict logic** strengthened to enforce the prompt's PASS
  criterion that requires *both* numerical discrimination AND a
  structural pattern.  The leading C values DIFFER but display NO
  uniform sign signature, no real-vs-imaginary discriminator, and no
  monotone or rational ratio relation across the dichotomy.
  Verdict therefore PARTIAL, not PASS.

## Anomalies and open questions

**(Most-important section.)**

1. **Sign(C) varies WITHIN the Δ>0 side.**  QL05 has C > 0; QL09 has
   C < 0.  This is the most striking finding: not all reps on the
   "A=4" side share a sign signature for the leading Stokes amplitude.
   Within the Δ<0 side, both V_quad and QL15 have C > 0, but with
   only two samples this is not a robust signal.  *Question for
   Claude*: is sign(C) actually a meaningful invariant in the
   resurgent classification, or does it depend on a basis-of-formal-
   solutions choice that I have not pinned down?  In particular, the
   Birkhoff series f_+ = exp(+c/u) u^ρ S_+ has a partner f_− with the
   opposite c-sign; the Stokes constant is in principle defined up to
   the *choice* of which solution we call f_+.  I used sign=+1 for
   all four reps (i.e., c = +2/√α), which is a uniform convention,
   but Claude should confirm this is the right one.

2. **Branch exponent β_R = 0 across all four reps** (to ≥85 digits).
   For V_quad CC-MEDIAN reported the same.  This is a *structural
   regularity* of the d=2 Birkhoff series — the alien amplitudes live
   on Γ(n) (no Γ-shift) — and is itself a closed numerical fact, not
   discrimination evidence.  Claude may want to formalize this as a
   side-finding (e.g., "alien-amplitude Γ-shift = 0 for d=2 PCF").

3. **The verdict "G6B_PARTIAL_HIGHER_ORDER_NEEDED" is honest, not
   cautious.**  I considered upgrading to PASS based on the strict
   interpretation that S_1 differs across the dichotomy, but the
   prompt's PASS clause requires a *structural* pattern, which I do
   not have.  No structural mapping (sign, modulus class, ratio)
   ties the leading Stokes data to A=4 vs A=3.  This may be expected
   — the dichotomy might genuinely live in higher-order alien
   amplitudes — but the leading-order test does not close G6b.

4. **Within-side spread is ~3× larger than cross-side spread for |C|.**
   |C| ranges 1.40–21.38 across all four reps, with V_quad and QL15
   on the same Δ<0 side differing by ~2.6×.  This is consistent with
   "Stokes data fingerprints the family, not the side", which is the
   informative content of the partial result.

5. **No HARD HALT triggered.**  G6B_STOKES_INVARIANT requires C
   values to AGREE across sides to ≥30 digits; observed agreement is
   ≤0.03 digits.  Stokes data is not sign-invariant.

## What would have been asked (if bidirectional)

* Should I extend the ladder to dps=300 / N=3000 anyway, to push the
  V_quad cross-method agreement past CC-MEDIAN's 108-digit landmark?
* Are there *non-leading* Stokes multiplier extractors I should
  implement directly in this session (e.g., subtract the leading
  Γ(n) ζ*^{−n} term and re-fit the residual to extract S_2 at 2 ζ*)?
* For the QL05/QL09 sign-of-C disagreement — is the sign genuinely
  a basis-independent invariant, or am I implicitly making a
  basis-choice that varies family-by-family?

## Recommended next step

Launch **T36-STOKES-MULTIPLIER-S2-EXTRACTION**: same four
representatives, same precision ladder, but extract S_2 (alien
amplitude at 2 ζ*) by subtracting C Γ(n) ζ*^{−n} from a_n and
applying a second Richardson pass to the residual.  Then test
whether the *ratio* S_2 / S_1, or the structural form S_2 = ±S_1²
(canonical for connected resurgent algebras), discriminates the
dichotomy.  This is the natural follow-up indicated in the present
PARTIAL verdict.

Alternative: launch **T36b-BIRKHOFF-BASIS-CONVENTION-FIX** to
pin down the sign-of-C ambiguity raised in Anomaly #1 before
proceeding with S_2 extraction.

## Files committed

- representatives.json
- t35_runner.py
- derive_recurrence.py
- derive_recurrence.log
- t35_run.log
- borel_V_quad_dps250_N2000.csv
- borel_V_quad_dps150_N600.csv
- borel_QL15_dps250_N2000.csv
- borel_QL15_dps150_N600.csv
- borel_QL05_dps250_N2000.csv
- borel_QL05_dps150_N600.csv
- borel_QL09_dps250_N2000.csv
- borel_QL09_dps150_N600.csv
- stokes_multipliers_per_rep.csv
- discrimination_certificate.md
- pcf1_crosscheck.md
- claims.jsonl
- halt_log.json
- discrepancy_log.json
- unexpected_finds.json
- rubber_duck_critique.md
- handoff.md

## AEAL claim count

8 entries written to claims.jsonl this session
(T35-A-V_quad, T35-A-QL15, T35-A-QL05, T35-A-QL09,
T35-A-AGGREGATE-NEG, T35-A-AGGREGATE-POS,
T35-A-DISCRIMINATION, T35-A-CROSSMETHOD).
