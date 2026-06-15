# Stage 7 — Paper outline

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 7 · **Date:** 2026-06-15
**Status:** COMPLETE (outline only — paper drafting is a SEPARATE downstream task)
**Working title:** *An Explicit Exponential-Period Representation of the V_quad Connection
Coefficient*
**Target length:** 20–25 pp.

> This is a sketch for an eventual paper. **No paper is drafted from this slot** (probe DO-NOT
> rule). Venue decision is deferred to a separate VENUE-RELAY chain.

---

## Abstract (draft)

We prove that the connection coefficient C of the V_quad PCF transcendent — the n = 1
standalone closure on the Sakai surface PV/D₅⁽¹⁾ — admits an explicit exponential-period
representation C = (|Γ(β)|/2π)∫_γ e^{ξ} B̂(ξ) dξ, where B̂ is the Borel transform of V_quad's
asymptotic series (holonomic over ℚ(√3), order-4 operator L_V), γ is an explicit Hankel
rapid-decay cycle on (−∞,−2/√3], and β = −1/(3√3). We give three independent verifications
(differential-equation/operator duality, Borel–Laplace/Hankel, and Stokes-data) agreeing to
46 digits, an exact differential-Galois computation (SL(2) by Kovacic for the order-2 operator
L_φ; the dual group G_V for L_V), and, conditional on the Fresán–Jossen period conjecture for
exponential motives, deduce that C is transcendental over ℚ̄.

## §1 Introduction (3 pp)
* V_quad and the PCF transcendence program; the Sakai stratification context (Zenodo, June
  2026). The connection coefficient C = |Γ(β)|·K and the Stokes constant S = 2πK.
* Open problem OP1/G1: explicit period representation of C. Direction-2 strategy
  (exponential motives).
* **Main results**, stated up front: (i) the explicit integral identity; (ii) the three
  verifications; (iii) the exact Galois data; (iv) conditional transcendence.
* **CAS / SOTA context paragraph** (AAECC Item-40 lesson, mandatory): position relative to
  `ore_algebra`/`gfun` holonomic-guessing, Maple `DEtools`/`DifferentialGaloisGroup`, Kovacic
  implementations, and resurgence/Borel-summation software; state precisely what is and is not
  automatable here (the operator recognition is, the motivic interpretation is not).

## §2 The differential operators L_φ and L_V (4 pp)
* φ(z) = Σ aₙ zⁿ is D-finite over **exactly ℚ(√3)**; minimal operator L_φ (order 2, deg 4),
  explicit coefficients.
* Borel transform B̂(ξ); operator L_V (order 4, deg 2) via Borel/Laplace duality, residual
  identically zero. Singular locus {0 apparent, −2/√3 branch, ∞ irregular slope 1}; branch
  exponent −(1+β) = −1+√3/9.
* Algebraicity over ℚ(√3) ⟹ the FJ algebraicity axiom for ω = B̂ dξ.
* Appendix pointer for the full coefficient lists.

## §3 The rapid-decay cycle γ (3 pp)
* Hankel thimble γ = γ_below + γ_loop + γ_above; formal Fresán–Jossen relative-homology
  description H₁^{rd}(𝔸¹, M).
* Rapid-decay verification: e^{+ξ}→0 at −∞; integrable branch singularity −(1+β) > −1.
* FJ rapid-decay class compatibility (C1/C2/C3).

## §4 The main theorem (3 pp)
* **Theorem 1.** C = (|Γ(β)|/2π)∫_γ e^{ξ} B̂(ξ) dξ (= |Γ(β)|·K). Statement, normalisation,
  the raw-vs-normalised period bookkeeping (leading period = S·e^{−ξ₀}).
* The bridge identity S/C = 2π/|Γ(β)| (exact).

## §5 Three verifications (4 pp)
* **§5.1 Differential-equation (Method A).** Operator Borel–Laplace duality: I_γ(z)=∫_γ
  e^{−ξ/z}B̂ dξ solves L_φ; M = h(z)·L_φ exactly over ℚ(√3); C = subdominant Stokes coefficient.
* **§5.2 Borel–Laplace (Method B).** Hankel branch integral ∮_H e^η η^{−(1+β)}dη = 2πi/Γ(1+β);
  Γ-factor of C; leading period S·e^{−ξ₀} to 46 digits.
* **§5.3 Stokes-data (Method C).** S_mult = 2πi·A/Γ(1+β), |S_mult| = 2πK; tightest, no
  γ-integration.
* **§5.4 Cross-consistency.** Independence of inputs; 46-digit agreement; VERIFIED.

## §6 Differential Galois and conditional transcendence (3 pp)
* **§6.1** Kovacic on L_φ ⟹ SL(2) (two methods); algorithmic certificate.
* **§6.2** G_V for L_V: 𝔾_m (irrational branch) × SL(2)-dual/Stokes at ∞; C as
  Galois-equivariant pairing.
* **§6.3** Fresán–Jossen application; **Theorem 2 (conditional):** C transcendental over ℚ̄.
  Honest statement of the motivic-comparison gap (G-MOTGALOIS).

## §7 Discussion (2 pp)
* Relation to the Sakai stratification: upgrade of Part (ii)(a) from STRUCTURAL to VERIFIED for
  d = 2 (V_quad) as the paradigm case.
* The d ≥ 3 case: why the present method (finite Borel locus, single branch) does **not** obviously
  extend; open problem.
* CAS reproducibility statement.

## §8 Appendix (3–4 pp)
* A. Explicit L_φ, L_V coefficients over ℚ(√3).
* B. Numerical verification logs (Stage 1.4 Hankel period; Methods B/C; ~46-digit tables).
* C. CAS sessions: holonomic recognition, Kovacic, operator-duality M = h(z)L_φ, Frobenius
  exponents.

---

## Venue priority (decision DEFERRED to VENUE-RELAY)
| Priority | Venue | Condition |
|---|---|---|
| a | **Compositio Mathematica** | all three methods verify cleanly (current state ✓) |
| b | **Mathematische Annalen** | if only PARTIALLY VERIFIED |
| c | **Journal of Symbolic Computation** | always-available backup; strongest CAS-context fit |

**Note (memory: AAECC desk-reject, Lecerf criteria).** For JSC or any CAS-adjacent venue the
§1 CAS/SOTA paragraph and §7 reproducibility statement are mandatory; define every central
object (L_φ, L_V, γ, B̂, the motive M) in-paper, not by citation to prior preprints; frame
significance against external state-of-the-art (holonomic guessing, differential-Galois
packages), not only within the SIARC program.

## Sourcing
All section content is backed by this slot's deliverables (`cycle-formal-definition.md`,
`rapid-decay-verification.md`, `fj-cycle-compatibility.md`, `numerical-integral.md`,
`kovacic-verification.md`, `galois-LV-verification.md`, `method-A/B/C-verification.md`,
`cross-verification.md`, `fj-application.md`) and VQUAD-001/002 (`operator-verification.md`,
`numerical-check.md`, `fresan-jossen-axioms.md`).
