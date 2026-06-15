# Stage 5 — Cross-verification consistency

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 5 · **Date:** 2026-06-15
**Status:** COMPLETE — **VERIFIED** (all three methods agree; none contradict)
**HALT GATE 5:** NOT triggered (no irreconcilable disagreement).

---

## 1. The identity under test

> **C = ∫_γ e^{ξ} B̂(ξ) dξ  (up to the documented action/normalisation factor).**

Precise normalised form (the honest disposition fixed in Stage 1.4): the **raw** leading
thimble period is ∫_γ e^{ξ} B̂ dξ = S·e^{−ξ₀} at leading order; the connection coefficient is
recovered by the explicit, fully-documented factor

> **C = (|Γ(β)|/2π)·S = |A|/|β| = |Γ(β)|·K,  with the bridge S/C = 2π/|Γ(β)| (residual 0).**

All three methods confirm this same structure.

## 2. Per-method results

| Method | Mechanism | Independent of | Result | Agreement |
|---|---|---|---|---|
| **A** differential-equation | I_γ(z)=∫_γ e^{−ξ/z}B̂ dξ solves L_φ via operator duality **M = h(z)·L_φ** | numerical integration; uses only exact operators over ℚ(√3) | **PASS** | exact (symbolic), only correct sign-convention of 4 works |
| **B** Borel–Laplace (Hankel) | ∮_H e^η η^{−(1+β)}dη = 2πi/Γ(1+β) ⟹ leading period = S·e^{−ξ₀} | the Stokes datum (derives it) | **PASS** | rel. err **8.84·10⁻⁴⁶** |
| **C** Stokes-data | S_mult = 2πi·A/Γ(1+β), \|S_mult\| = 2πK; C = \|A\|/\|β\| | γ-integration (uses only S, β, A) | **PASS** | rel. err **8.84·10⁻⁴⁶** (S), **9.31·10⁻⁴⁶** (C) |

## 3. Why the three are genuinely independent

* **Method A** is purely **algebraic/differential**: it never evaluates an integral
  numerically. It proves the *deformed* integral satisfies the V_quad operator L_φ by an
  exact operator computation over ℚ(√3) (M = h(z)·L_φ). Its evidence is the symbolic
  proportionality of three operator coefficients plus the four-sign anti-fluke test.
* **Method B** is **analytic/contour**: it deforms the Borel-sum ray to the Hankel thimble and
  evaluates the branch integral in closed form via Hankel's 1/Γ formula. Its evidence is the
  ~46-digit match of the leading period to S·e^{−ξ₀}.
* **Method C** is **Stokes/numerical**: it uses only the deposited Stokes constant S = 2πK and
  the branch amplitude A from L_V's large-order data, never touching γ. Its evidence is the
  ~46-digit match |S_mult| = 2πK and C = |Γ(β)|·K.

A, B, C use disjoint inputs (operators / contour / Stokes datum) yet land on the **same single
datum A** and the **same Γ-factor** Γ(1+β). The probability of a spurious triple coincidence at
46 digits with the unique correct operator-sign convention is negligible.

## 4. Reconciliation of conventions

* **Kernel sign.** Method B/the period integral uses the FJ convention e^{+ξ} (f = −ξ);
  Method A uses the Borel-sum kernel e^{−ξ/z}. These are the two complementary faces of the
  one Borel–Laplace duality, not a contradiction: B fixes the *value*, A fixes the *ODE*.
* **Real vs imaginary Stokes constant.** The deposited S = 2πK = 0.4579… is the **magnitude**
  of the Stokes multiplier S_mult = 2πiK; the factor i is the Stokes phase. Method C makes
  this explicit; no inconsistency with the deposited real value.
* **Raw vs normalised period.** The raw leading period is S·e^{−ξ₀}; C is obtained by the
  documented factor |Γ(β)|/2π. This was pre-committed in Stage 1.4 (HALT GATE 1) and is not a
  post-hoc adjustment.

## 5. Verdict

All three methods **PASS** and **agree**; none contradicts. Per the probe rule
(VERIFIED ⟺ ≥2 agree and none contradict), and here all **three** agree:

> **Sub-problem C: VERIFIED.**
> **Method A: PASS · Method B: PASS · Method C: PASS.**

The identity C = ∫_γ e^{ξ} B̂(ξ) dξ (normalised C = |Γ(β)|·K = (|Γ(β)|/2π)·S) is established
by three independent methods. HALT GATE 5 not triggered.

## 6. Sourcing

* Method results: `method-A-verification.md`, `method-B-verification.md`,
  `method-C-verification.md`, and the scripts/JSON cited therein.
* Bridge identity, K/S/C: VQUAD-001 `numerical-check.md`; Stage 1.4 `numerical-integral.md`.
