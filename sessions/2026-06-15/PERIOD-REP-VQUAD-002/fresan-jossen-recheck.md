# Stage 6 — Fresán–Jossen compatibility recheck (against the explicit operator)

**Chain:** PERIOD-REP-VQUAD-002 · **Stage:** 6 · **Date:** 2026-06-15
**Trigger:** outcome = GO ⇒ this stage runs.

Re-run of PERIOD-REP-VQUAD-001 Stage 6, now with the **explicit holonomic operator
`L_V`** (order 4, coefficients exactly in ℚ(√3)) in hand. The parent left axiom 3
(the load-bearing algebraicity axiom) **UNCLEAR**; this is the axiom the probe
resolves.

**Datum, sign-corrected (Stage 4.2):**
`X = 𝔾_{m,ξ} ∖ {−ξ₀} = ℙ¹∖{0, −ξ₀, ∞}`, `f = −ξ`, `ω = B̂(ξ)·dξ`,
`γ =` Hankel thimble around the branch at `−ξ₀ = −2/√3` along the ray `arg ξ = π`.
(`e^{−f} = e^{ξ} → 0` as `Re ξ → −∞`: the negative-axis singularity found in
Stage 4 is **exactly** the FJ rapid-decay direction.)

---

## 6.1 Axiom-by-axiom recheck

| # | FJ axiom | parent status | **this probe** | justification |
|---|----------|---------------|----------------|---------------|
| 1 | `X` smooth, `k⊆ℚ̄` | VERIFIED | **VERIFIED** | `ℙ¹∖{0,−ξ₀,∞}` smooth affine; the removed branch point `−ξ₀=−2/√3` is **ℚ(√3)-rational** (Stage 4.2, exact). Datum defined over the number field ℚ(√3). |
| 2 | `f:X→𝔸¹` regular | VERIFIED | **VERIFIED** | `f=−ξ` regular on `𝔾_m`, `/ℚ`. The irregular direction at `∞` (slope 1) supplies the `e^{ξ}` exponential — the "exponential" of the exponential motive. |
| 3 | **`ω` algebraic `d_f`-class, `k⊆ℚ̄`** | **UNCLEAR** | **✅ VERIFIED (resolved)** | `ω=B̂(ξ)dξ`: `B̂` is annihilated by the **order-4 operator `L_V` with coefficients exactly in ℚ(√3)⊆ℚ̄**, residual **identically zero over ℚ(√3)** (Stage 4.1). `ω` is a section of the ℚ(√3)-algebraic meromorphic connection `(𝒪^4, ∇_{L_V})`. **This is the G-OMEGA resolution.** |
| 4 | `γ∈H_n^{rd}` rapid-decay | VERIFIED | **VERIFIED (sharpened)** | thimble on `arg ξ=π` to `−∞`; `|e^{−f}|=e^{Re ξ}→0`. The defining ray/branch is now an **exact algebraic point** `−2/√3∈ℚ(√3)` (was a 95.6-digit modulus). |
| 5 | perfect comparison / `dim H^n_dR = dim H_n^{rd}` | VERIFIED-BUT-NEEDS-CARE (no operator) | **VERIFIED-PENDING-EXPLICIT-COUNT (now computable)** | The blocker ("no Lax pair / operator in corpus") is **removed**: the φ-operator (order 2) and `L_V` (order 4) give a concrete finite connection whose de Rham/rapid-decay dimensions are a finite computation (rank ≤ 4). Exact dimension match deferred to sub-problem C, but **no longer obstructed**. |
| 6 | motive `/`number field; `G_M` (Conj. 1.3.2) | UNCLEAR (contingent on 3) | **HYPOTHESIS NOW MET; payload conditional (by design)** | With axiom 3 resolved, the motive `M` is defined over the **number field ℚ(√3)** — so the hypothesis "M over a number field" of Conjecture 1.3.2 is **satisfied**. `G_M` itself still needs identification (sub-problem C/D); the **unconditional** transcendence of `C` stays conjectural — exactly the EBR cc3 template's *conditional transcendence theorem under the FJ period conjecture*. |

## 6.2 The decisive reconciliation (transcendental accessory parameter)

The parent flagged the **transcendental Painlevé-V accessory parameter** (EBR-II §5)
as "a concrete reason `ω` might **fail** `k⊆ℚ̄`." **This probe refutes that fear for
this datum:**

- The accessory parameter is transcendental in the **nonlinear** Painlevé-V moduli
  (the transcendent `y(t)` is genuinely non-holonomic — that is the Painlevé property).
- But the **WKB/Borel scalar reduction** of the *specific* V_quad solution is a
  **linear** order-2 ODE (`L_φ`), hence `φ` is D-finite and `B̂` holonomic, with
  operator coefficients in **ℚ(√3)** — no transcendental constant appears in `L_V`.
- I.e. the transcendence lives upstairs (nonlinear isomonodromy moduli), while the
  **linear connection governing the asymptotics is defined over ℚ(√3)**. The
  exponential-period datum `(X,f,ω,γ)` only sees the linear connection ⇒ algebraic.

This is the structural reason GO is clean rather than complicated.

## 6.3 Special-attention items (FJ auxiliary conditions, axioms-easy-to-miss)

- **Regularity of `ω` at the finite singular points.** At `ξ=0`, `L_V` exponents
  `{−1,0,1,2}` are all integers ⇒ **apparent** singularity (`B̂` analytic there);
  `ω` has at worst a pole, an algebraic (meromorphic) form — admissible. At `−ξ₀`,
  the branch exponent is `−(1+β)=−1+√3/9` (Stage 4.3): `ω` has a regular-singular
  (Nilsson-class, moderate-growth) point — the FJ-admissible type. ✓
- **Rapid decay vs `f` at `∞`.** `f=−ξ`, irregular slope 1 at `∞`: the thimble's two
  ends both go to `Re ξ→−∞`, `e^{ξ}` super-polynomially small ⇒ the pairing
  `∫_γ e^{−f}ω` converges absolutely (FJ Def. 3.1.1.1). ✓
- **Number-field of definition.** Everything (`X`, `f`, `ω`, the branch point) is
  defined over **ℚ(√3)**; FJ requires `k⊆ℚ̄`, satisfied. ✓
- **Irregular-Hodge / `G_M`.** Still untouched (sub-problem C/D); now a clean
  downstream computation rather than a blocked one.

---

## Stage 6 verdict

**Axioms 1–4 VERIFIED** (3 upgraded from UNCLEAR — the G-OMEGA resolution); **axiom 5
unblocked** (operator now explicit, count deferred to sub-problem C); **axiom 6
hypothesis now satisfied**, transcendence payload conditional **by design** (the
intended FJ-conjecture-conditional theorem). The candidate is **not merely
shape-compatible but algebraically compatible** with Fresán–Jossen: the
load-bearing algebraicity axiom is **met over ℚ(√3)**. Consistent with
**outcome_GO_clean**.
