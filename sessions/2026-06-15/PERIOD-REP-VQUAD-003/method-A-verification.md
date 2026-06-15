# Sub-problem C / Stage 4 — Method A: differential-equation verification

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 4 (Method A) · **Date:** 2026-06-15
**Status:** COMPLETE — **PASS**
**Script:** `scripts/stage4a_methodA_v2.py` → `scripts/stage4_methodA_results.json`

> **Claim.** The parameter-deformed integral I_γ(z) = ∫_γ e^{−ξ/z} B̂(ξ) dξ satisfies the
> **same** differential equation L_φ whose Stokes multiplier (at the irregular point) is the
> connection coefficient C. Both sides of C = ∫_γ e^ξ B̂ dξ are governed by L_φ via
> Borel–Laplace duality. **Verified at the operator level.**

---

## 1. The Borel–Laplace operator duality

The Borel sum of V_quad is φ(z) = a₀ + ∫₀^∞ e^{−ξ/z} B̂(ξ) dξ, with kernel **e^{−ξ/z}**
(this kernel is forced by the convention b_m = a_{m+1}/m!, since
a_{m+1} = b_m·m! = b_m ∫₀^∞ e^{−t} t^m dt). Along any contour where the boundary terms
vanish (the rapid-decay thimble γ qualifies, Stage 1.2), the transform
𝓛[f](z) = ∫ e^{−ξ/z} f(ξ) dξ obeys

> **D_ξ ↦ +1/z,  ξ ↦ +z² D_z.**

(Derivation: ∂_z e^{−ξ/z} = (ξ/z²)e^{−ξ/z} ⟹ 𝓛[ξf] = z² D_z 𝓛[f]; and
∫ e^{−ξ/z} f′ dξ = (1/z) 𝓛[f] after integrating by parts with vanishing boundary.)

The thimble integral is the **difference of the two lateral Borel sums**, which cancels the
analytic a₀-part; hence the difference I_γ(z) satisfies the **homogeneous** equation.

## 2. Dualizing L_V → an order-2 operator M, and M = h(z)·L_φ

Writing L_V = Σ_{k,a} c_{k,a} ξ^a D_ξ^k (c_{k,a} = coeff of ξ^a in p_k), the duality maps it
to the operator M = Σ_{k,a} c_{k,a} (z² D_z)^a (1/z)^k acting on I_γ(z). Because max_k deg_ξ p_k
= 2, **M has order 2**. Computed symbolically over ℚ(√3):

> **M = h(z)·L_φ,  h(z) = 27(649 + 30√3) / (418501·z²·(2√3 − 3)).**

The three operator-coefficient ratios coincide exactly:
M-coeff(D²)/q₂ = M-coeff(D¹)/q₁ = M-coeff(D⁰)/q₀ = h(z).

**Convention check (anti-fluke).** All four kernel-sign conventions (±1/z, ±z²D_z) were
tested; **only** the correct Borel-sum convention (D_ξ↦+1/z, ξ↦+z²D_z) yields a proportional
operator. The other three fail. This rules out an accidental match.

Therefore I_γ(z) is annihilated by L_φ: it is a genuine solution of the V_quad linear
equation.

## 3. Identification of the connection coefficient

I_γ(z) is the Stokes jump (difference of lateral sums), hence the **subdominant solution** of
L_φ at the irregular point z=0: as z → 0⁺ its leading behaviour is
I_γ(z) ~ (const)·e^{−ξ₀/z}·z^{·}, and that constant is, by definition of the Stokes
phenomenon, the **Stokes multiplier = the connection coefficient C** (up to the normalisation
fixed in Stage 1.4: leading period = S·e^{−ξ₀}, C = (|Γ(β)|/2π)·S). The initial-condition /
normalisation match is the content of Method B (Hankel) and Method C (Stokes), which pin the
constant numerically to ~46 digits.

## 4. What this method establishes (task 4.A.1–4.A.3)

* **(4.A.1)** LHS (C as Stokes multiplier of L_φ) and RHS (I_γ(z)=∫_γ e^{−ξ/z}B̂ dξ) satisfy
  the same differential structure: I_γ solves L_φ, proved by M = h(z)·L_φ (Borel–Laplace
  duality, exact over ℚ(√3)). ✓
* **(4.A.2)** Initial conditions match: I_γ is the subdominant L_φ-solution whose leading
  small-z coefficient is C; numerically fixed by Stage 1.4 / Methods B, C. ✓
* **(4.A.3)** This deliverable. ✓

## 5. Sourcing

* L_V, L_φ coefficients: VQUAD-002 `operator-verification.md` §4.0a,b.
* M = h(z)·L_φ, four-convention test: this slot `stage4a_methodA_v2.py` + JSON.
* Borel–Laplace duality, Stokes multiplier = subdominant coefficient: van der Put–Singer
  *Galois Theory of Linear Differential Equations* Ch. 7; Loday-Richaud, *Divergent Series,
  Summability and Resurgence II* (Lect. Notes Math. 2154), Ch. 5–6.
* Normalisation leading period = S·e^{−ξ₀}: this slot `numerical-integral.md` (Stage 1.4).

**Method A verdict: PASS.** I_γ(z) solves L_φ (operator duality M = h(z)·L_φ, exact); C is
its subdominant Stokes coefficient. The two sides share the L_φ differential structure.
