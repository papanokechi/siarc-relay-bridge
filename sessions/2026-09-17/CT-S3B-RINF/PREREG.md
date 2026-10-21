# PREREG — CT-S3B-RINF

Written before the main computation. A single feasibility arithmetic
(§1 below) was evaluated first in order to write an honest pre-registration;
it is reported as a finding, not as a result.

**Prerequisite satisfied:** `sessions/2026-09-17/CT-S3A-ZETA-AUDIT/REPORT.md`
resolved the variable convention (classification (b): ζ* = 2ξ₀ is the action
difference; the Borel transform is `B(ζ) = Σ a_k ζ^k/k!` in `u = √z`).
Part C therefore runs.

## 1. Pre-registered threshold that is ill-posed (finding, declared up front)

P3 Part A step 2 says: *"Choose N so the tail bound `Σ_{k>N} |r|/|b(k)b(k-1)|` is
below 10^-3000."*

For V_quad, `b(n) = 3n² + n + 1`, so `|b(k)b(k-1)| ~ 9k⁴` and

```
Σ_{k>N} 1/(9k⁴)  ≈  1/(27 N³)
```

The tail decays **polynomially**, not geometrically. Requiring `< 1e-3000` gives

```
N > (10^3000/27)^(1/3) ≈ 10^999.5
```

which is unreachable by any computation. **The threshold as written cannot be
met at any N.** Per P0 ("If a threshold proves ill-posed, report that as a
finding") this is recorded as finding **S3B-F1** and the threshold is **not
silently replaced**.

**Substitute procedure, fixed here in advance:** obtain `r_∞` by Neville
polynomial extrapolation of `r_n` in the variable `x = 1/n` to `x = 0`, using
`L+1` nodes `n = N … N+L`. The convergence `r_∞ - r_n = O(n^-3)` makes this
legitimate. Report **only** the digits confirmed by the pre-registered
`N`-versus-`2N` agreement test, and report them as the achieved precision. Do
not claim 3000 digits.

## 2. Hypotheses and observables

- **A.** `r_∞ = lim Q_n / ∏_{k≤n} b(k)` exists and is nonzero for V_quad.
  Observable: `r_∞`, digits confirmed by N-vs-2N agreement.
- **B.** The leading amplitude in `Q_n/Γ(dn+1) ~ K (β_d/d^d)^n n^s` is

  ```
  K = r_∞ · (2π)^((d-1)/2) · d^(-1/2) / ∏_{i=1}^{d} Γ(1 - r_i)
  ```

  where `b(n) = β_d ∏_i (n - r_i)`. Observable: digits of agreement between this
  closed form and `Q_n/(Γ(dn+1)(β_d/d^d)^n n^s)` extrapolated to `n → ∞`.
- **C.** `r_∞` lies in the ℚ-span of a pre-registered constant basis.

## 3. Falsifiers (frozen)

- **F-A.** `r_∞` indistinguishable from 0, or N-vs-2N agreement < 20 digits.
- **F-B.** *(P3's own wording)* agreement between the closed form for `K` and the
  numerically extrapolated amplitude **below 20 digits**. Target ≥ 30 digits.
- **F-C.** No null. A null result is a valid outcome; report the excluded height
  bound.

## 4. Vacuity pre-check

The `K` formula must actually depend on the data it claims to depend on.
- **(i)** `K` must move when `r_∞` moves. Tested by evaluating both sides on
  **several different polynomials** `b` (not just V_quad), at `d = 2, 3, 4`. If
  the closed form matched the numerics for a `b` whose `r_∞` and roots were
  varied, while being insensitive to them, the test would be vacuous.
- **(ii)** The formula must fail when deliberately mis-specified. Control:
  evaluate `K` with the `∏Γ(1-r_i)` factor omitted and confirm the agreement
  collapses. If the control also "agrees", the observable is not discriminating
  and the session halts.

## 5. Part C — PSLQ basis, fixed before running

Basis, in this order:

```
1, π, √3, Γ(1/3), Γ(2/3), log 2, log 3, Γ(1-r₁), Γ(1-r₂)
```

where `r₁, r₂` are the roots of `3n²+n+1`. Bessel/hypergeometric values are
**excluded** unless a derivation motivates them; none does at prereg time.

Acceptance, all three required:
- identical relation at dps 500, 1000 and 2000;
- coefficient height ≤ 1e6;
- verifies at dps 3000.

A relation meeting all three is labelled **VERIFIED**, never PROVEN.

## 6. Precondition

No root of `b` may be a positive integer, else `Γ(1-r_i)` is singular. Checked
before anything else; violation → HALT for that polynomial.

## 7. Outputs

`rinf.json`, `amplitude.json`, `pslq.json`, `DERIVATION.md`, `claims.jsonl`,
`REPORT.md`. All numerical outputs hashed.
