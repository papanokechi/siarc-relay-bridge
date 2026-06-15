# Stage 6 — Fresán–Jossen compatibility check

**Chain:** PERIOD-REP-VQUAD-001 · **Stage:** 6 · **Date:** 2026-06-15

Candidate (Stage 4): `X = 𝔾_m,ξ`, `f = ξ`, `ω = B[φ](ξ)dξ`, `γ =` Hankel thimble
on `[ξ₀,∞)`, `ξ₀ = 2/√3`, branch exponent `β = −1/(3√3)`. Axioms as numbered in
`fresan-jossen-axioms.md` §2.5.

Legend: **VERIFIED** / **VERIFIED-BUT-NEEDS-CARE** / **UNCLEAR** / **FAILS**.

---

| # | FJ axiom | status | justification |
|---|----------|--------|---------------|
| 1 | `X` smooth, `k ⊆ ℚ̄` | **VERIFIED** | `X = 𝔾_m` is smooth affine, defined `/ℚ`. (The *base-field* algebraicity of the **whole datum** is axiom 3.) |
| 2 | `f : X→𝔸¹` regular | **VERIFIED** | `f = ξ` is a regular function on `𝔾_m`, `/ℚ`. Its only "infinity" behaviour is the rank-1 irregular direction `arg ξ=0`, the required rapid-decay direction. |
| 3 | **`ω` algebraic `d_f`-class, `k ⊆ ℚ̄`** | **UNCLEAR** | `ω = B[φ]dξ` is Bessel/Kummer-*flavoured* (not visibly rational), and — decisively — **no explicit algebraic Borel operator for V_quad exists** (gap G-OMEGA) and the Painlevé-V **accessory parameter is transcendental** (EBR-II §5). Stage-5 T2 (single isolated branch at the algebraic point `ξ₀`, Nilsson type) is *necessary* support but **not** a proof of algebraicity. **This is the load-bearing axiom and it is genuinely UNCLEAR.** |
| 4 | `γ ∈ H_n^{rd}` rapid-decay | **VERIFIED** | The Hankel thimble on `[ξ₀,∞)` runs to `∞` only where `Re(f)=Re(ξ)→+∞`, so `|e^{−f}|=e^{−Re ξ}` decays super-polynomially ⇒ absolutely convergent (FJ Def. 3.1.1.1 / eq 1.1.2.1). Its defining ray is numerically pinned to `ξ₀` at 95.6 digits (Stage 5 T2). |
| 5 | perfect comparison / `dim H^n_dR = dim H_n^{rd}` | **VERIFIED-BUT-NEEDS-CARE** | The PV linear problem is rank 2 and the EBR sibling realised a `2×2` period matrix with basis `{[Φ],[θΦ]}` and cycles `γ±` via Hien; the V_quad analogue is expected `2×2`. **But** the V_quad rapid-decay and de Rham dimensions have **not been computed explicitly** (no Lax pair in corpus, gap G-LAX) — the dimension match is *expected*, not *verified*. |
| 6 | motive `/` number field; `G_M` for Conjecture 1.3.2 | **UNCLEAR** | The transcendence payload needs `M` over a number field and an *identified* motivic Galois group `G_M`. We have only the **differential** (Picard–Vessiot) group `SL(2)` (asserted, gap G-KOVACIC) — which is **not** `G_M`. And "M over a number field" itself depends on resolving axiom 3 (base-field algebraicity). So both the hypothesis and the group are UNCLEAR. |

### Special-attention items (Stage 6.3)

- **Rapid-decay condition** (axiom 4): ✅ the clean part. The candidate `γ` has
  exactly the right asymptotic behaviour; this is the strongest leg of the
  candidate and is independently confirmed numerically.
- **Algebraicity of `ω` / coefficient field** (axiom 3): ❓ the **central
  unknown.** The honest statement is that the field of definition of `ω` is *not
  yet identified* — it is `ℚ(√3)` *iff* `B[φ]` solves an algebraic operator over
  `ℚ(√3)`, which is unproven and is exactly gap G-OMEGA. The transcendental
  accessory parameter is a concrete reason it might **fail** `k ⊆ ℚ̄`.
- **Hodge-/motivic-cohomological conditions** (axiom 6): ❓ untouched. No
  irregular-Hodge filtration or `G_M` computation has been attempted; this is
  downstream (sub-problem C territory), but it means the motivic reading is
  currently unsupported beyond the differential-Galois analogy.

---

## Stage 6 verdict

**Two axioms are UNCLEAR (3 and 6), one needs care (5); the rest VERIFIED.**

The candidate is **shape-compatible** with Fresán–Jossen — `X, f, γ` and the
singular geometry sit cleanly inside the framework (indeed inside the Bessel
template Ex. 1.1.5) — **but the load-bearing algebraicity axiom (3) is UNCLEAR**,
and the motivic/transcendence axiom (6) is UNCLEAR and partly *contingent* on (3).

**Governance consequence (task DO-NOT rule):** *"do not declare GO if any
Fresán–Jossen axiom is UNCLEAR; downgrade to GO-WITH-COMPLICATION or
NEEDS-MORE-PROBE."* Axiom 3 is not a minor caveat but the **definitional**
requirement for "exponential period," and it is **blocking** for sub-problems
B/C/D (all of which take an algebraic `ω` as input). ⇒ the verdict cannot be GO,
and because the unresolved item is a *single well-defined sub-step* rather than a
documented-risk-to-carry, the indicated classification is **NEEDS-MORE-PROBE**
(see `verdict.md`).
