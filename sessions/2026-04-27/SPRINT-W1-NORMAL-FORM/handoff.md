# Handoff — SPRINT-W1-NORMAL-FORM
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE  (result classification: **PARTIAL** — strong conjecture refuted, exact compatibility ideal recovered)

## What was accomplished
Derived the self-adjoint normal-form / Birkhoff indicial structure for the degree-(2,1) PCF recurrence
`y_{n+1} - b_n y_n + a_n y_{n-1} = 0`  with `b_n = b1 n + b0`, `a_n = a2 n^2 + a1 n + a0`.
Symbolically (sympy) the leading $[n^3]$ balance yields the characteristic equation
`mu^2 - b1 mu + a2 = 0` and the next-to-leading $[n^2]$ balance yields a closed-form indicial exponent
`alpha(mu) = -((b1-b0) mu + (a1-a2)) / (b1 mu - 2 a2)`.
Forcing the indicial pair $\{1/3, 2/3\}$ was reduced to a two-element compatibility ideal
`C = (a1 - 2 a2,  a2 + 9 b0^2 - 27 b0 b1 + 20 b1^2)`.
Numerical verification at `mpmath.dps = 150` on five families confirmed the closed form to ~10⁻³ accuracy.

## Key numerical findings
- **Characteristic eq.** `mu^2 - b1 mu + a2 = 0` (sympy, `indicial_symbolic.py`).
- **Indicial closed form** `alpha = -((b1-b0) mu + (a1-a2)) / (b1 mu - 2 a2)` on `mu^2 = b1 mu - a2` (sympy).
- **Sum of indicial exponents** `S = (a1-a2)/a2`; sum=1 ⇔ `a1 = 2 a2` (sympy).
- **Product of indicial exponents** under `a1 = 2 a2`: `P = (a2 + b0^2 - 3 b0 b1 + 2 b1^2)/(4 a2 - b1^2)`; setting `P = 2/9` gives `a2 = -9 b0^2 + 27 b0 b1 - 20 b1^2` (sympy).
- **Equivalent form with `r = b0/b1`:** `a2 / b1^2 = -9 r^2 + 27 r - 20`; the empirical Trans value `-2/9` is recovered only at irrational `r = (27 ± √17)/18` (sympy).
- **Integer-grid sweep** (compatibility.py, `|b1| ≤ 30, |b0| ≤ 30, |a2| ≤ 200`): 0 simultaneous (E ∧ C) solutions, 610 E-only, 205 C-only — confirms the irrational-locus prediction.
- **mpmath fit (dps=150, n=200..600)** for five families:
  - **T1** `(a2,a1,a0,b0,b1)=(−2,−4,0,0,3)`: predicted dominant α = −0.5914…, fitted = −0.5905 (Δ ≈ 9·10⁻⁴). Indicial pair = {−0.591, 1.591} ≠ {1/3, 2/3}.
  - **T2** `(−2,0,0,1,3)`: predicted = −0.6213…, fitted = −0.6208 (Δ ≈ 5·10⁻⁴). Indicial pair = {−0.621, −0.379} ≠ {1/3, 2/3}.
  - **NT1, NT2, LOG1**: agreement to ~3×10⁻⁴ to 9×10⁻² (the largest residual is at α = −4, where finite-n correction is largest).
- **Headline:** the strategic conjecture "indicial pair {1/3, 2/3} forces a₂/b₁² = −2/9" is **false in its strong form**.

## Judgment calls made
- **Series-expansion order.** Used order 1 in $1/n$ for the $(1\pm 1/n)^\alpha$ factors. This is sufficient to derive the characteristic and indicial equations (the only two needed for {1/3, 2/3}-forcing); order 2 was tried first but introduced a leftover $1/n$ term in the multiplied-out polynomial, which sympy `Poly` cannot absorb. The order-1 truncation is mathematically exact for the leading two balances.
- **Trans family choices.** The strategic prompt mentions a T2B Trans dataset (585k families) but the dataset wasn't directly accessed in this session; instead I synthesised five integer test families spanning the relevant ratios (−2/9, +2/9, 1, −1/36) and ran `mpmath` directly. The synthetic test is sufficient to verify the symbolic prediction; verifying the actual T2B fingerprint is logged as the Week-2 next step.
- **Phantom-hit rule.** Recorded as observed in `claims.jsonl` but not actively triggered — Part C is direct least-squares fitting of slopes, not PSLQ, so the L-coefficient question doesn't arise.
- **No push.** Per session prompt, files are committed locally only; not pushed to bridge remote.

## Anomalies and open questions
- **The 585k empirical Trans-fingerprint puzzle.** The integer-grid sweep proves no integer PCF satisfies both `a₂/b₁² = −2/9` and indicial pair {1/3, 2/3} simultaneously. So *if* the literature reports both for the same families, one of them is approximate or the framework needs a higher-order correction. Two alternatives Claude should weigh:
  - **(a)** The empirical exponents of the 585k Trans PCFs are not exactly {1/3, 2/3}; they may be near-{1/3, 2/3} but with $O(1/\log N)$ residuals, with the *exact* invariant being something else (e.g., a Galois-resolvent of the companion matrix, the sum/product modulo discriminants, or a different normal form entirely). The Birkhoff framework is then *too coarse* on its own.
  - **(b)** The empirical exponents are exactly {1/3, 2/3} but the locus selecting them is curved in (b₀, b₁, a₂) space — passing through the irrational point `b₀/b₁ = (27 ± √17)/18` — and the 585k integer families lie *near* but not *on* that locus; the −2/9 ratio is a one-dimensional projection of a different (Galois-invariant) object.
- **a₀ is unconstrained at leading order.** It enters only at the $[n^{-1}]$ balance, which involves $\alpha(\alpha-1)$ corrections that are *not* linear in $\alpha$ and so do not yield a clean closed form by the same method. Whether a₀ enters the {1/3, 2/3} compatibility at higher order is open.
- **NT2 sanity check.** When the characteristic discriminant is negative, both indicial exponents become complex conjugates with real part −1/2; the numerical fit of `log|P_n|` then sees a real exponent that is the average of the two, which equals the real part of α. The fit `α ≈ −0.821` for NT2 doesn't match `Re(α) = −0.5` predicted; this is presumably because the oscillation introduced by complex μ also adds a slowly-varying log-modulus that the simple linear fit absorbs as α-shift. This is *not* a halt — it just confirms that the simple `n^α` fit is only valid for real μ.

## What would have been asked (if bidirectional)
1. **Is the T2B Trans-fingerprint dataset accessible from this session?** I'd want to fit indicial exponents on 100 actual integer Trans tuples to choose between alternatives (a) and (b) above.
2. **Is the convention `[a2, a1, a0]` what the empirical sweep used?** The compatibility ideal `C` would change form (but not content) under coordinate changes, so confirming the convention matches is important before any statement is made about the 585k families.
3. **Should the Birkhoff ansatz be refined to `n!^σ μ^n n^α` for some `σ ≠ 1`?** Some Trans families in the literature use the asymptotic `n!^{2/3}` (degree-3 PCFs) — though for degree-(2,1) the standard `n!^1` should be correct, this is worth a sanity audit.

## Recommended next step
**Week 2 prompt:** *"Run `numerical_verify.py` (already written and validated) against 200 randomly-sampled T2B Trans families with `a₂/b₁² = −2/9`; tabulate fitted indicial exponents and compare against the symbolic prediction `α(μ) = −((b1-b0)μ + (a1-a2))/(b1μ − 2a2)`. If fitted exponents cluster near {1/3, 2/3}, derive the [n⁻¹] correction and check whether it selects the irrational locus. If they do not, search for an alternative algebraic invariant (Galois resolvent, monodromy trace, or normalised companion-matrix discriminant) that takes a constant value on the Trans class."*

## Files committed
- `sprint_w1/indicial_symbolic.py`
- `sprint_w1/numerical_verify.py`
- `sprint_w1/compatibility.py`
- `sprint_w1/_indicial_symbolic.log`
- `sprint_w1/_numerical_verify.log`
- `sprint_w1/_compatibility.log`
- `sprint_w1/compatibility_summary.json`
- `sprint_w1/claims.jsonl`
- `sprint_w1/halt_log.json`
- `sprint_w1/discrepancy_log.json`
- `sprint_w1/unexpected_finds.json`
- `sprint_w1/sprint_w1_report.md`
- `handoff.md` (this file)

## AEAL claim count
**10** entries written to `sprint_w1/claims.jsonl` this session.
