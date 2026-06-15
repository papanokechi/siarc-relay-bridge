# Sub-problem B / Stage 1.1 — Formal definition of the rapid-decay cycle γ

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 1.1 · **Date:** 2026-06-15
**Status:** COMPLETE

---

## 0. Object and conventions

We work with the Borel transform of the V_quad formal solution,

> **B̂(ξ) = Σ_{m≥0} b_m ξ^m,  b_m = a_{m+1}/m!,**

holonomic over **exactly ℚ(√3)**, annihilated by the order-4 operator **L_V**
(PERIOD-REP-VQUAD-002 `operator-verification.md` §4.0(b); residual identically 0).
Its singular locus is

> **Sing(L_V) = { 0 (apparent), −ξ₀ (regular-singular branch point), ∞ (irregular, slope 1) },
> ξ₀ = 2/√3.**

The dominant Borel singularity sits on the **negative** real axis at −ξ₀
(VQUAD-002 sign correction; stored repository memory), with local exponent the
indicial root **−(1+β)** of L_V at −ξ₀,

> **β = −1/(3√3) = −0.19245008972987525…,  −(1+β) = −1 + √3/9 = −0.80754991027…**

so locally **B̂(ξ) ~ A·(ξ+ξ₀)^{−(1+β)}**, A = (S/2πi)·Γ(1+β) the alien/branch amplitude
(VQUAD-001 `numerical-check.md`; this stage 1.4 confirms |A| = K·Γ(1+β) to 46 digits).

**Fresán–Jossen sign convention.** FJ write the integrand as **e^{−f} ω**.
Here f = −ξ (so e^{−f} = e^{+ξ}) and ω = B̂(ξ) dξ. The task body fixes this convention
(`candidate-data.md`: f_task = −f_FJ). Rapid decay is therefore decay of **e^{+ξ}** as
Re ξ → −∞, which is exactly the direction in which the cut (−∞, −ξ₀] runs. This is the
structural reason the corrected (negative-axis) geometry is the FJ-natural one.

---

## 1. The Hankel thimble γ

γ is the **Hankel thimble** wrapping the branch cut of B̂ that emanates from −ξ₀ along
the negative real axis to −∞. Decompose

> **γ = γ_below + γ_loop + γ_above**

with a small parameter ε → 0⁺:

| piece | description | parametrisation |
|---|---|---|
| **γ_below** | ray on the **lower** lip of the cut, incoming from −∞ to −ξ₀ | ξ(s) = −s − iε, s: +∞ → ξ₀ |
| **γ_loop**  | small **clockwise** circle around the branch point −ξ₀ | ξ(θ) = −ξ₀ + ε e^{iθ}, θ: −π → +π |
| **γ_above** | ray on the **upper** lip of the cut, outgoing from −ξ₀ to −∞ | ξ(s) = −s + iε, s: ξ₀ → +∞ |

Orientation: γ is traversed so that the branch point is encircled once clockwise
(standard Hankel orientation matching the Laplace inversion ∫_0^∞ → wrapped contour).
The limit ε → 0⁺ is taken in the distributional (boundary-value) sense, the two lips
carrying the two determinations (ξ+ξ₀)^{−(1+β)}_± differing by the monodromy factor
e^{∓2πi(1+β)}.

---

## 2. Fresán–Jossen relative-homology description

FJ realise an exponential period as a pairing of a **rapid-decay homology** class with a
de Rham (algebraic) class. The data (`fresan-jossen-axioms.md`, FJ "Exponential motives",
arXiv:1511.xxxxx / book *expmot.pdf*):

* **X** = the affine line 𝔸¹_ξ over ℚ(√3) (coordinate ξ); the potential **f = −ξ ∈ 𝒪(X)**
  is regular, with no finite critical points (df = −dξ ≠ 0), so the only "critical value"
  contribution is the irregular direction at ∞.
* The relevant **D-module** is M = (𝒪_X[ξ]-module defined by L_V) ⊗ E^{−f}, where
  E^{−f} = (𝒪_X, ∇ = d − df) is the exponential connection. ω = B̂(ξ) dξ is a global
  algebraic section of the de Rham complex of M (algebraicity over ℚ(√3): VQUAD-002 GO_clean).
* The cycle γ is a class in the **rapid-decay homology**
  **H₁^{rd}(X, M) = H₁(X, Z; rd)** where Z = {−ξ₀} is the locus where ω is singular and
  "rd" prescribes the allowed behaviour at ∞: a chain must decay faster than any power of
  e^{−f} = e^{ξ} permits along its non-compact ends — i.e. the ends must run into the half
  plane Re ξ → −∞ where e^{+ξ} → 0.

Concretely, in FJ's notation for a thimble at a regular-singular point of M sitting over a
cut to the rapid-decay direction,

> **[γ] = ⟨ −ξ₀ ; (−∞·e^{iπ}) ⟩_{rd} ∈ H₁^{rd}(𝔸¹, M),**

the "moderate" endpoint being the branch point −ξ₀ (finite, governed by exponent −(1+β) > −1
⇒ integrable) and the "rapid-decay" endpoint being the ray to −∞ along arg ξ = π.
The exponential period is then the canonical pairing

> **∫_γ e^{ξ} B̂(ξ) dξ = ⟨ [γ]_{rd},  [e^{ξ} B̂ dξ]_{dR} ⟩.**

---

## 3. Two normalisations (recorded honestly)

The branch point sits at −ξ₀ ≠ 0, so the action e^{−f} = e^{ξ} contributes the constant
factor **e^{−ξ₀}** at the dominant point. Two FJ-equivalent presentations:

1. **f = −ξ** (used above). Then the leading thimble value is
   **∫_γ e^{ξ} B̂ dξ |_lead = S·e^{−ξ₀}** (Stage 1.4 closed-form collapse).
2. **f = −(ξ+ξ₀)** (re-centre the potential on the singularity, an FJ-admissible
    𝔾_a-translation). Then the action factor is absorbed and the period is exactly **S**.

The connection coefficient is the same datum reweighted by the branch Γ-factor:

> **C = (|Γ(β)|/2π)·S = |A|/|β|,  |A| = K·Γ(1+β)** (all verified to 46 digits, Stage 1.4).

Both normalisations are recorded; the paper will fix convention (2) so the headline
identity reads ∫_γ e^{ξ+ξ₀} B̂ dξ = S, with C the algebraic-Γ reweighting. This is the
"explicit normalization factor documented honestly" required by the probe plan — the raw
∫_γ e^{ξ} B̂ dξ is **not** numerically equal to |Γ(β)|·K; it equals S·e^{−ξ₀} at leading
order, and C is recovered by the explicit factor above.

---

## 4. Sourcing

* L_V, singular locus, branch exponent −(1+β): VQUAD-002 `operator-verification.md` §4.0(b), §4.2.
* Negative-axis sign, ξ₀ = 2/√3: VQUAD-002 sign correction; stored repo memory "Borel singularity sign".
* K, S, C, β numerics and bridge identity S/C = 2π/|Γ(β)|: VQUAD-001 `numerical-check.md` T1.
* FJ rapid-decay homology framework: `fresan-jossen-axioms.md` (this slot, Stage-2 carryover from VQUAD-001) and FJ *Exponential Motives* monograph.
* |A| = K·Γ(1+β), C = |A|/|β|, leading period = S·e^{−ξ₀}: this slot `scripts/stage1_hankel_period.py` → `stage1_hankel_results.json` (worst rel. err 8.8e-46).

**Verdict 1.1: γ formally defined as a rapid-decay Hankel thimble class in
H₁^{rd}(𝔸¹, M), with explicit three-piece chain and explicit FJ relative-homology label.**
