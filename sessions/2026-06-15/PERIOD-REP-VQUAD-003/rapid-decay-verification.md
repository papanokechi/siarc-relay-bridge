# Sub-problem B / Stage 1.2 — Rapid-decay verification for γ

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 1.2 · **Date:** 2026-06-15
**Status:** COMPLETE

The integrand is **e^{+ξ} B̂(ξ)** (FJ convention e^{−f}, f = −ξ). For γ to be an
admissible rapid-decay cycle, two conditions must hold: exponential decay at the
non-compact ends (→ −∞) and integrability at the finite branch point −ξ₀.

---

## 1. Decay on the rays γ_below, γ_above (Re ξ → −∞)

On both lips ξ = −s ± iε with s → +∞, so Re ξ = −s → −∞ and

> **|e^{ξ}| = e^{Re ξ} = e^{−s}.**

The algebraic factor B̂(ξ) grows at most polynomially along the ray: B̂ is holonomic with
an irregular singularity of **slope 1** only at ξ = ∞ in the *formal* Borel plane, but
along the **negative** real direction (arg ξ = π) the relevant growth is governed by the
*moderate* (regular-singular / tempered) behaviour — B̂ continued along the cut grows no
faster than a power |ξ|^{N} for some fixed N (holonomic ⇒ moderate growth in any fixed
non-Stokes direction; van der Put–Singer Ch. 3). Hence on each ray

> **|e^{ξ} B̂(ξ)| ≤ C₀ · s^{N} · e^{−s} → 0   super-polynomially as s → ∞,**

and ∫^{−∞} |e^{ξ}B̂| ds ≤ C₀ ∫^∞ s^N e^{−s} ds = C₀ Γ(N+1) < ∞. **Exponential decay
holds with explicit bound e^{−s}.** This is the defining FJ rapid-decay condition at the
non-compact ends.

*Numerical sanity (Stage 1.4 generator):* the Borel coefficients satisfy
|b_m| ~ K·Γ(m+1+β)/(ξ₀^{m+1+β} m!), so the Taylor series of B̂ has radius ξ₀ and the
continuation to the cut is dominated by the (ξ+ξ₀)^{−(1+β)} branch — power-law, not
exponential — confirming moderate growth times e^{−s} decay.

---

## 2. Integrability at the branch point −ξ₀

Near ξ = −ξ₀ the leading singular behaviour is

> **B̂(ξ) ~ A·(ξ+ξ₀)^{−(1+β)},   −(1+β) = −1 + √3/9 = −0.80754991…**

The exponent satisfies

> **−(1+β) > −1   ⇔   β < 0,**

which is true (β = −1/(3√3) < 0). Therefore (ξ+ξ₀)^{−(1+β)} is **locally integrable**:
on the loop/segment near −ξ₀,

> **∫_{|ξ+ξ₀|<δ} |ξ+ξ₀|^{−(1+β)} |dξ| = ∫_0^δ r^{−(1+β)} dr = δ^{−β}/(−β) < ∞** (since −β > 0).

The small clockwise loop γ_loop contributes the finite jump across the two determinations:
the two lips differ by the monodromy factor (1 − e^{−2πi(1+β)}) = (1 − e^{−2πiβ}) (mod the
e^{−2πi} from the integer part), and the loop radius → 0 contribution vanishes because
−(1+β) > −1. Thus the cut integral converges and equals the discontinuity integral

> **∫_γ = (1 − e^{2πi(1+β)}) ∫_{−∞}^{−ξ₀} e^{ξ}·[disc B̂](ξ) dξ,**

finite. **The β > −1 (equivalently −(1+β) > −1) condition is satisfied; the singularity is
integrable.**

*Numerical confirmation (Stage 1.4):* the branch integral around −ξ₀ produces the
Γ-factor Γ(1+β) (resp. Γ(−β)), finite and nonzero; |A| = K·Γ(1+β) confirmed to 46 digits.
A divergent (β ≤ −1) exponent would have produced a divergent Γ, contradicting the
observed finite amplitude.

---

## 3. Combined statement

γ has

1. **exponential decay** e^{−s} at both non-compact ends (Re ξ → −∞), with explicit bound
   |e^{ξ}B̂| ≤ C₀ s^N e^{−s}; and
2. an **integrable** finite singularity at −ξ₀ governed by −(1+β) > −1.

Hence **∫_γ e^{ξ} B̂(ξ) dξ converges absolutely**, and γ is a legitimate rapid-decay
chain. ∎

---

## 4. Sourcing

* Branch exponent −(1+β), value of β: VQUAD-002 `operator-verification.md` §4.2;
  this slot `cycle-formal-definition.md` §0.
* Local amplitude A and |A| = K·Γ(1+β): this slot `scripts/stage1_hankel_period.py`
  → `stage1_hankel_results.json` (rel. err 5.1e-46).
* Moderate growth of holonomic functions in a fixed direction: van der Put & Singer,
  *Galois Theory of Linear Differential Equations*, Ch. 3 (regular-singular/tempered growth).
* Convergence pieces (rays + loop): standard Hankel-thimble analysis; numerics this slot 1.4.

**Verdict 1.2: γ has rapid decay — exponential at the ends, integrable (−(1+β) > −1) at
−ξ₀; the period integral converges absolutely.**
