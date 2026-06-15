# Sub-problem C / Stage 4 — Method B: Borel–Laplace duality (Hankel closed form)

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 4 (Method B) · **Date:** 2026-06-15
**Status:** COMPLETE — **PASS**
**Script:** `scripts/stage4_methods.py` (Method B block) → `scripts/stage4_methods_results.json`

> **Claim.** Deforming the Borel-sum ray to the Hankel thimble γ around the branch point
> −ξ₀ produces the connection coefficient via the branch (Γ-factor) integral, and the
> Γ(β) in C = |Γ(β)|·K arises **exactly** from Hankel's formula. **Verified in closed form,
> confirmed to ~46 digits.**

---

## 1. The Borel–Laplace statement (task 4.B.1)

For the Gevrey-1 series φ(z)=Σ a_n z^n with Borel transform B̂(ξ)=Σ b_m ξ^m (b_m=a_{m+1}/m!),
the Borel sum is φ_sum(z) = a₀ + ∫₀^∞ e^{−ξ/z} B̂(ξ) dξ in the right half-plane. The
connection coefficient C is read off from the Stokes phenomenon across the ray pointing at
the dominant Borel singularity, here at **−ξ₀ = −2/√3** (negative axis; VQUAD-002 sign).

## 2. Contour deformation to the thimble (task 4.B.2)

Deforming the lateral Borel sums to the Hankel thimble γ = γ_below+γ_loop+γ_above wrapping
the cut (−∞,−ξ₀] gives the Stokes jump as the branch integral of B̂. Near −ξ₀,
B̂(ξ) ~ A·(ξ+ξ₀)^{−(1+β)} with A = (S/2πi)·Γ(1+β) (Stage 1.4). With η = ξ+ξ₀ the leading
thimble contribution is

> **∫_γ e^{ξ} A(ξ+ξ₀)^{−(1+β)} dξ = A·e^{−ξ₀} ∮_H e^{η} η^{−(1+β)} dη.**

## 3. The Γ-factor from Hankel's formula (task 4.B.3)

Hankel's representation of the reciprocal Gamma function,

> **(1/2πi) ∮_H e^{η} η^{−s} dη = 1/Γ(s),**

(H the Hankel contour wrapping the negative real axis) gives, with s = 1+β,

> **∮_H e^{η} η^{−(1+β)} dη = 2πi / Γ(1+β).**

Numerically (dps 60): ∮_H = 5.43596955395471573394…·i, exactly 2πi/Γ(1+β). Hence the leading
thimble value is

> **A·e^{−ξ₀}·(2πi/Γ(1+β)) = [(S/2πi)Γ(1+β)]·e^{−ξ₀}·(2πi/Γ(1+β)) = S·e^{−ξ₀},**

the Γ(1+β) cancelling **exactly**. The branch integral has manufactured the Γ-factor, and

> **|leading period| = S·e^{−ξ₀}  (rel. err 8.8·10⁻⁴⁶).**

The connection coefficient is the action-stripped, β-reweighted datum:
C = (|Γ(β)|/2π)·S = (|Γ(1+β)|/(2π|β|))·S = |A|/|β| (Stage 1.4: rel. err ~10⁻⁴⁶). The
**|Γ(β)|** of C = |Γ(β)|·K is precisely Γ(1+β)/|β| from this branch integral.

## 4. Cross-check with Method-A picture

Method B uses the negative-axis thimble (kernel e^{+ξ}, FJ convention f=−ξ); Method A uses
the Borel-sum kernel e^{−ξ/z} and proves the parameter integral solves L_φ. They are the two
faces of the same Borel–Laplace duality: A establishes the **differential** identity (same
ODE), B establishes the **analytic/closed-form** value (Hankel Γ-factor). They agree on the
normalisation leading period = S·e^{−ξ₀}.

## 5. Sourcing

* B̂ amplitude A, |A|=K·Γ(1+β), branch exponent −(1+β): Stage 1.4 (`numerical-integral.md`),
  VQUAD-002 `operator-verification.md` §4.2.
* Hankel's formula 1/Γ(s) = (1/2πi)∮_H e^η η^{−s} dη: standard (Whittaker–Watson §12.22;
  NIST DLMF 5.9.2).
* Numerics: this slot `stage4_methods.py` (Method B block), `stage4_methods_results.json`.

**Method B verdict: PASS.** The Hankel branch integral produces 2πi/Γ(1+β); the leading
thimble period equals S·e^{−ξ₀} in closed form (rel. err 8.8·10⁻⁴⁶), and the Γ(β)-factor of
C = |Γ(β)|·K is exactly this branch Γ-factor.
