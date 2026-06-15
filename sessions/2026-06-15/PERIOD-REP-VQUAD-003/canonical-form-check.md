# Stage 0.2 — Canonical-form check on L_V coefficients

**Chain:** PERIOD-REP-VQUAD-003 · **Stage:** 0.2 (carryover spot-check) · **Date:** 2026-06-15
**Scripts:** `scripts/stage0_canonical_check.py` → `scripts/stage0_canonical_results.json`
**Engine:** sympy exact `Fraction`/`Rational` arithmetic (independent of VQUAD-002's Q3 class).

## Checks and results

**(1) md ↔ json consistency.** The hand-transcribed `L_V` (from
`operator-verification.md` §4.0(b)) matches the parent machine artifact
`PERIOD-REP-VQUAD-002/scripts/operator_verification_results.json`
(`L_V_operator.coeffs`) **exactly** — no drift between the human-readable note and
the computed operator. ✓

**(2) Reduced fractions.** Every coefficient pair `(p, q)` (for `p + q√3`) is a
**reduced** fraction (`gcd(numerator, denominator) = 1`). ✓

**(3) Denominators.** The distinct denominators are exactly **{1, 431, 418501}**.
Factorisation: **418501 = 431 × 971**, and **both 431 and 971 are prime**
(`sympy.factorint(418501) = {431:1, 971:1}`). So the common denominator of the
order-≥2 part is `431·971` and the `p₁` part has denominator `431`; the two share
the prime `431`. This is the exact-arithmetic fingerprint of the single
normalisation `p₀ ≡ 1` applied to the minimal null-vector. ✓

**(4) No common factor (primitivity).** Clearing to the primitive ℤ[√3] form by
multiplying through by `418501` gives **24 integer coefficients** whose overall
**content (gcd) is 1**. Hence the operator cannot be simplified by removing a common
scalar factor — it is in **primitive** form (equivalently, `p₀ ≡ 1` is a faithful
normalisation, not hiding a removable common factor). ✓

## Verdict
**CANONICAL-OK.** `L_V`'s coefficients are in canonical (reduced, primitive) form
over ℚ(√3); the denominators `431` and `418501 = 431·971` are correctly computed and
prime-factored; and the human-readable transcription agrees with the machine
artifact. **HALT GATE 0 (canonical form): PASS.**

> Combined with §0.1, **HALT GATE 0 is fully passed** — no error in the VQUAD-002
> operator; the probe proceeds to Stage 1.
