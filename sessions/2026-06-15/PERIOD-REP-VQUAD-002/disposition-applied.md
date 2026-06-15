# Stage 5 — Disposition selection (MECHANICAL)

**Chain:** PERIOD-REP-VQUAD-002 · **Stage:** 5 · **Date:** 2026-06-15

> Per Strengthening Condition 2, the dispositions were committed in Stage 0
> (`dispositions.json`) **before any computation**. This selection is **mechanical**
> against the Stage-4.4 field determination. **No post-hoc reframing.**

## 5.1 The mechanical match

**Stage-4.4 result (the only input to this selection):**
> The coefficient field of the verified operator `L_V` (and of the φ-operator) is
> **exactly ℚ(√3)** — every coefficient lies in ℚ(√3), and the operators genuinely
> use √3 (not the proper subfield ℚ).
> *(Source: `operator-verification.md` §4.4; `scripts/operator_verification_results.json`
> `phi_op_uses_sqrt3=true`, `L_V_uses_sqrt3=true`.)*

**`dispositions.json` selection rule:**

| Rule (`_selection_rule`) | Field condition | Matches? |
|---|---|---|
| `GO_clean` | L_V coefficients in **ℚ(√3)** | ✅ **YES** |
| `GO_small_extension` | ℚ(√3,√−1), ℚ(√3,ζ_n) small, … | no |
| `GO_larger_field` | non-CM or rank ≥ 4 field | no |
| `NO_GO_clean` | no holonomic ODE + D-transcendence evidenced | no (holonomic ODE **found**) |
| `INCONCLUSIVE` | no holonomic ODE within budget | no |

The field is **exactly ℚ(√3)**, which is the verbatim condition for
**`outcome_GO_clean`**: *"L_V is algebraic over ℚ(√3) with coefficients in ℚ(√3)."*

The `_do_not` guard ("DO NOT declare GO_clean if the field is anything other than
ℚ(√3) — even ℚ(√3,√−1) is GO_small_extension") is **respected**: the field is
ℚ(√3) itself, with no imaginary or cyclotomic extension. ℚ(√3) is real quadratic,
rank 2 over ℚ.

## 5.2 Selected disposition: **`outcome_GO_clean`**

Taken verbatim from `dispositions.json`:

- **verdict_for_subproblem_A:** **GO**
- **next_step:** "Open PERIOD-REP-VQUAD-003 for sub-problem B (rapid-decay cycle
  formalization) and sub-problem C (symbolic verification via L_V)"
- **tentative_venue:** "Compositio Mathematica or JSC"
- **paper_framing:** "An Explicit Fresán–Jossen Exponential-Period Representation of
  the V_quad Connection Coefficient"

## 5.3 Evidence cross-reference (Stage 4.4 → this selection)

- Holonomic ODE **found** (not absent): `holonomic_recognition_q3_results.json`
  `holonomic_found=true`; minimal φ-operator order 2 / degree 4 (nullity 1).
- `L_V` annihilates `B̂` **exactly over ℚ(√3)** (`exact_residual_zero=true`).
- Field **exactly ℚ(√3)** (§4.4), neither smaller (ℚ) nor extended (no √−1, no ζ_n).
- ⇒ the single matching pre-committed outcome is **`outcome_GO_clean`**.

## 5.4 Caveat carried forward (does not change the selection)

The **sign of ξ₀** is negative (`−2/√3`, §4.2), refining the parent's `+2/√3`
(a modulus). This affects the cycle/`f` bookkeeping for sub-problem B but **not**
the coefficient field — so the mechanical selection is unaffected. It is recorded
as an explicit hand-off item, **not** as a reason to downgrade the disposition.

**Operator-review flag?** No. `dispositions.json` flags "holonomic ODE found but
operator structure unusable for the FJ application" for review. Here the structure
is **usable** (regular singular point at −ξ₀ with the expected branch exponent
−(1+β); irregular point at ∞ supplying `e^{ξ}`), so no review flag is raised. The
ξ₀-sign item is a routine refinement, handled in Stage 6/sub-problem B.

**STAGE 5 RESULT: outcome_GO_clean — verdict GO.**
