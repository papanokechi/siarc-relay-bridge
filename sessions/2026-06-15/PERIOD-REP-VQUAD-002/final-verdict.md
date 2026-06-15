# Final verdict — PERIOD-REP-VQUAD-002

**Chain:** PERIOD-REP-VQUAD-002 · **Date:** 2026-06-15
**Probe:** sub-problem A.1 follow-up — resolve G-OMEGA (is the V_quad Borel
operator algebraic over ℚ(√3)?).

---

## 7.1 Verdict

### Disposition selected: **`outcome_GO_clean`** → **sub-problem A = GO**

The selection is **mechanical** (Stage 5) against the Stage-0 pre-committed
`dispositions.json` and the Stage-4.4 coefficient-field determination. **No
post-hoc reframing.**

**One-line result.** The V_quad WKB series `φ(z)=Σaₙzⁿ` is **D-finite over ℚ(√3)**
(unique minimal operator: order 2, degree 4); its Borel transform `B̂(ξ)` solves an
**order-4 holonomic operator `L_V` with coefficients exactly in ℚ(√3)**, singular at
`{0, −2/√3, ∞}` with branch exponent `−(1+β)=−1+√3/9` at `−2/√3`. Therefore
`ω=B̂(ξ)dξ` is **algebraic over the number field ℚ(√3)** and the Fresán–Jossen
algebraicity axiom is **satisfied**. **G-OMEGA is resolved (positively).**

### Evidence (cross-referenced to slot files)

| Claim | Evidence | File |
|---|---|---|
| φ D-finite, minimal order 2 / deg 4 over ℚ(√3) | nullity 1 at (r=2,d=4); nullity pattern {1,3,5,7} = left-multiples of one minimal op | `holonomic_recognition_q3_results.json`; `operator-verification.md` §4.0 |
| `L_V` (order 4) annihilates `B̂` exactly | residual **identically zero over ℚ(√3)** for ξ⁰…ξ¹²⁹ | `operator_verification_results.json`; `operator-verification.md` §4.1 |
| singular locus `{0,−ξ₀,∞}`; sign = **−ξ₀** | exact `p₄(−2/√3)=0`; Borel–Padé dominant pole at −1.1549 | `indicial_results.json`, `borel_pade_results.json`; §4.2 |
| branch exponent `−(1+β)` at −ξ₀ | indicial roots `{−(1+β),0,1,2}`, `−(1+β)=−0.8075499103` | `indicial_results.json`; §4.3 |
| coefficient field **exactly ℚ(√3)** | operators genuinely use √3; all arithmetic closed in ℚ(√3) | `operator_verification_results.json`; §4.4 |
| FJ axiom 3 (algebraicity) UNCLEAR→VERIFIED | explicit ℚ(√3) operator | `fresan-jossen-recheck.md` §6.1 |
| G-LAX, G-KOVACIC confirmed-absent in corpus | fresh grep + parent corroboration | `lax-pair-found.md`, `kovacic-found.md` |

### Gaps status
- **G-OMEGA — CLOSED (positive).** `B̂` holonomic, `L_V` over ℚ(√3).
- **G-LAX — confirmed-absent in corpus, but PARTIALLY ANSWERED:** the order-2
  φ-operator `L_φ` is the **scalar/Schrödinger reduction** of the V_quad PV linear
  problem, reconstructed computationally. (The full 2×2 Lax matrix `M(t)` is still
  not exhibited — only its scalar reduction.)
- **G-KOVACIC — confirmed-absent, now UNBLOCKED:** with the explicit order-2 `L_φ`
  over ℚ(√3), the Kovacic algorithm can now be **run** on a concrete operator
  (downstream, sub-problem C) to verify the asserted SL(2).

### Bonus structural findings (beyond the disposition)
1. **No infinite resurgent tower.** Holonomicity (finite singular locus) **proves**
   `B̂` has **no** singularities at `2ξ₀,3ξ₀,…` — resolving the open question the
   parent left at the `(1/2)ⁿ` numerical floor. V_quad resurgence = a finite rank-4
   connection, not a wild alien lattice.
2. **Sign of the action fixed.** The Borel singularity is at **−2/√3** (negative
   axis), not +2/√3; the parent's value was a modulus. This aligns the geometry with
   the FJ `e^{−f}` convention (`f=−ξ`, decay as `ξ→−∞`).
3. **Transcendence reconciliation.** The transcendental PV accessory parameter lives
   in the **nonlinear** moduli; the **linear** scalar reduction governing the
   asymptotics is defined over ℚ(√3) — which is why GO is *clean*.

## 7.2 Recommended next step (verbatim from `dispositions.json` → `outcome_GO_clean`)

> "Open PERIOD-REP-VQUAD-003 for sub-problem B (rapid-decay cycle formalization) and
> sub-problem C (symbolic verification via L_V)"

- **tentative_venue:** Compositio Mathematica or JSC
- **paper_framing:** "An Explicit Fresán–Jossen Exponential-Period Representation of
  the V_quad Connection Coefficient"

### Scope outline for PERIOD-REP-VQUAD-003 (do NOT write the prompt here — outline only)

**Sub-problem B — rapid-decay cycle formalization.**
- Formalize `γ` as a rapid-decay 1-cycle for the irregular connection
  `(∇_{L_V} − d f)`, `f=−ξ`, on `ℙ¹∖{0,−ξ₀,∞}` (Hien's rapid-decay homology).
- Use the **sign-corrected** geometry: branch at `−2/√3`, ray `arg ξ=π`.
- Compute `dim H_1^{rd}` and the de Rham `dim H¹_dR(∇_{L_V}+df)`; verify the perfect
  comparison (FJ axiom 5) — the count deferred from Stage 6.

**Sub-problem C — symbolic verification via `L_V`.**
- Run the Kovacic algorithm on the explicit order-2 `L_φ`/ℚ(√3) to **confirm the
  asserted SL(2)** (closes G-KOVACIC on a real operator) and identify the
  differential Galois group of the rank-4 `L_V`.
- Symbolically verify `C = ∫_γ e^{ξ} B̂(ξ)dξ` equals the connection coefficient (to
  high precision, then structurally), reconciling the normalization (recall
  `S=2πK`, `C_Borel=|Γ(β)|K`, `S/C=2π/|Γ(β)|` exact).
- Set up the **conditional transcendence statement** (under FJ Conjecture 1.3.2),
  mirroring the EBR cc3 template.

### Effort estimate
- Sub-problem B: **2–3 weeks** (Hien rapid-decay homology + dimension match; the
  operator is now explicit, so mostly bookkeeping + one cohomology computation).
- Sub-problem C: **2–4 weeks** (Kovacic on `L_φ`, Galois of `L_V`, symbolic
  period verification, conditional-theorem assembly).
- Combined PERIOD-REP-VQUAD-003: **~4–6 weeks** to a draft-ready
  exponential-period representation result.

## 7.3 / 7.4 — N/A (verdict is GO, not NO-GO / INCONCLUSIVE)

---

**PROBE COMPLETE — outcome_GO_clean.**
