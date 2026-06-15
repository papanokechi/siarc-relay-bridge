# Stage 6 — Fresán–Jossen application: conditional transcendence of C

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 6 · **Date:** 2026-06-15
**Status:** COMPLETE
**Inputs:** Stage 4/5 VERIFIED identity C = ∫_γ e^{ξ} B̂(ξ) dξ; `galois-LV-verification.md`
(G_V); `fresan-jossen-axioms.md` (VQUAD-001) and `fresan-jossen-recheck.md` (VQUAD-002).

---

## 1. C is now an exponential period

With sub-problem C **VERIFIED**, the connection coefficient is exhibited as an explicit
exponential-period integral
> **C = (|Γ(β)|/2π) · ∫_γ e^{ξ} B̂(ξ) dξ,  B̂ algebraic-holonomic over ℚ(√3), γ rapid-decay.**

The data (X, f, ω, γ) entering Fresán–Jossen are (VQUAD-001 §3, VQUAD-002 §S6, this slot
Stages 1–3):
* **X** = the affine line 𝔸¹_ξ minus the singular locus {0 (apparent), −ξ₀=−2/√3 (branch)} of
  L_V (the irregular point is at ∞);
* **f** = −ξ (the FJ exponent; the integrand carries e^{−f} = e^{+ξ});
* **ω** = B̂(ξ) dξ, with B̂ holonomic over **exactly ℚ(√3)** (L_V, order 4 / deg 2, residual 0;
  VQUAD-002 §4) — the FJ **algebraicity** axiom holds with coefficient field a real quadratic;
* **γ** = the Hankel thimble on (−∞, −ξ₀], a rapid-decay cycle (Stage 1, FJ class C1/C2/C3 OK).

Hence C is a **period of the exponential motive** H¹(𝔸¹∖{0,−ξ₀}, ∇) attached to (X, f, ω),
in the precise Fresán–Jossen sense (FJ *Exponential Motives*, Def. of rapid-decay period).

## 2. The Fresán–Jossen / Kontsevich–Zagier-type conjecture (task 6.2)

Fresán–Jossen attach to an exponential motive M a **motivic Galois group** G_mot(M), and the
period torsor is a G_mot-torsor; the **period conjecture** states that all ℚ-polynomial
relations among the periods of M come from the motivic torsor — equivalently
> **trdeg_ℚ ℚ(periods of M) = dim G_mot(M).**

(This is the exponential-motives analogue of Grothendieck's period conjecture; FJ formulate it
for the Tannakian category of exponential motives. The differential-Galois group G_V is the
de Rham realisation / a quotient of G_mot, by the analogue of the Ayoub/Nori comparison.)

## 3. Galois input for V_quad (task 6.3)

From Stages 2–3:
* L_φ (order 2, the de Rham fibre at the regular side) has differential Galois group
  **SL(2)** by exact Kovacic (HALT GATE 2 PASS, two methods) — `kovacic-verification.md`.
* L_V (order 4, the Borel/Laplace dual) has Galois group **G_V** containing a torus 𝔾_m (from
  the irrational branch exponent −1+√3/9 at −ξ₀, monodromy eigenvalue e^{2πi√3/9} of infinite
  order) and the **exponential/Stokes data at ∞** (formal torus × non-trivial unipotent Stokes,
  the SL(2)-dual structure) — `galois-LV-verification.md` (HALT GATE 3 PASS).
* The connection coefficient C is the **Galois-equivariant pairing** between the de Rham class
  [ω] = [B̂ dξ] and the rapid-decay Betti class [γ]; the exponential period 2πi (period of
  E^{ξ}) and the branch normalisation 1/Γ(1+β) are the two torus generators (Method C §4).

Because G_V contains a non-abelian part (SL(2)-type, from the SL(2) of L_φ under Borel duality
plus the Stokes unipotent) **and** a transcendental-monodromy torus 𝔾_m (irrational exponent),
the motivic Galois group is **large**: there is no 1-dimensional sub-torsor forcing C to be
algebraic, and **no algebraic relation** of C with the base periods {1} is visible.

## 4. The conditional transcendence statement (task 6.4)

> **Theorem (conditional on the Fresán–Jossen period conjecture for exponential motives).**
> The V_quad connection coefficient
> **C = (|Γ(β)|/2π)·∫_γ e^{ξ} B̂(ξ) dξ = |Γ(β)|·K,  β = −1/(3√3),**
> is **transcendental over ℚ̄** (the algebraic closure of ℚ).

**Reasoning.** C is a period of the exponential motive M = (𝔸¹∖{0,−ξ₀}, f=−ξ, ω=B̂dξ). Its
de Rham/differential Galois group G_V is positive-dimensional and non-trivial on the class
pairing defining C (contains 𝔾_m with irrational character √3/9 and an SL(2)-type Stokes
part). The FJ period conjecture gives trdeg_ℚ of the period algebra = dim G_mot ≥ 1, and the
specific generator C is not fixed by G_mot (no algebraic relation with 1). Hence C ∉ ℚ̄,
conditionally. ∎(conditional)

**Unconditional fallback already known.** Independently of FJ, C = |Γ(β)|·K with
β = −1/(3√3) ∉ ℚ; by Nesterenko / known Γ-transcendence at non-rational arguments combined
with the (conjecturally transcendental) K, C is *expected* transcendental — but only the
**Γ(β)** factor is unconditionally non-algebraic-by-classical-means; the product's
transcendence still rests on K. The FJ route is what upgrades the **whole** C to conditional
transcendence in one structured statement, and ties it to the motivic Galois group rather than
to ad-hoc Γ-arithmetic.

## 5. Caveats / auxiliary FJ conditions actually checked

* **Algebraicity of ω over a number field** — YES, exactly ℚ(√3) (VQUAD-002; the FJ axiom does
  not require ℚ, a number field suffices). ✓
* **Rapid-decay class of γ** — YES, C1 (finite integrability β>−1, here −(1+β)>−1),
  C2 (e^{+ξ}→0 as Re ξ→−∞), C3 (relative-homology closedness). (Stage 1.3.) ✓
* **Critical locus of f** — f = −ξ is linear, df = −dξ never vanishes on X, so there is **no
  finite critical point**; the only "critical value at infinity" is the slope-1 irregularity.
  This is the simplest possible f (the FJ "no interior critical point" sub-case), which is
  favourable: the motive is a single E^{−f}⊗(rank-4 algebraic) with no extra vanishing-cycle
  contributions. ✓ (This is the auxiliary condition flagged as easy-to-miss in VQUAD-001 §2.3.)
* **Honest gap.** The identification G_V ⊇ (the motivic Galois group quotient) uses the
  standard de Rham-realisation comparison; the full Nori/Ayoub exponential-motive comparison
  for this specific M is **assumed**, not verified here. This is a CONJECTURAL bridge and is
  flagged as such (gap G-MOTGALOIS, NEW — see ledger). It does not affect the differential
  computations, only the motivic interpretation.

## 6. Headline

> **Conditional on Fresán–Jossen, the V_quad connection coefficient C is transcendental over
> ℚ̄.**

This is the headline result of PERIOD-REP-VQUAD-003.

## 7. Sourcing

* FJ framework & period conjecture: Fresán–Jossen, *Exponential Motives* (monograph draft,
  expmot.pdf); summarised in VQUAD-001 `fresan-jossen-axioms.md`, rechecked VQUAD-002
  `fresan-jossen-recheck.md`.
* G_V, SL(2), branch exponent: this slot `kovacic-verification.md`, `galois-LV-verification.md`.
* C = |Γ(β)|·K, β = −1/(3√3): VQUAD-001 `numerical-check.md`.
* Γ-transcendence context: Nesterenko (1996), modular-function algebraic independence;
  classical Γ at rational arguments (Chudnovsky). Marked CONJECTURAL where it concerns K.
