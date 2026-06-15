# Stage 7 — Verdict and recommendation

**Chain:** PERIOD-REP-VQUAD-001 (sub-problem A) · **Date:** 2026-06-15

---

# VERDICT: **NEEDS-MORE-PROBE**  *(favourable)*

The probe **produced a candidate** `(X, f, ω, γ)` that is structurally identified,
Fresán–Jossen-shaped, and numerically consistent — so this is **not** NO-GO. But
**one well-defined sub-step is unresolved** (the algebraicity of the de Rham form
`ω = B[φ]dξ` over a number field), and that sub-step is the **definitional**
requirement for "exponential period" and is **blocking** for sub-problems B/C/D.
Per the task's own DO-NOT rule (no GO while any FJ axiom is UNCLEAR; downgrade),
the honest classification is **NEEDS-MORE-PROBE**, qualified **favourable**
because the Stage-5 evidence predicts the sub-step is likely to resolve *for* the
candidate.

> Compact candidate: `X = 𝔾_m,ξ`, `f = ξ`, `ω = B[φ](ξ)dξ`, `γ =` Hankel thimble
> on `[ξ₀,∞)`, `ξ₀ = 2/√3`, `β = −1/(3√3)`, giving `C = |Γ(β)|·K = 0.43770528…`.
> Numerical agreement: bridge `C=|Γ(β)|·K`, `S=2πK` exact; Borel singularity at
> `ξ₀=2/√3` to **95.6 digits**.

## 7.1 Why NEEDS-MORE-PROBE and not the neighbours

- **Not GO.** FJ axiom 3 (`ω` algebraic, `k ⊆ ℚ̄`) is **UNCLEAR**; axiom 6
  (motive `/`number field, `G_M`) is **UNCLEAR**. The task forbids GO while any
  axiom is UNCLEAR.
- **Not GO-WITH-COMPLICATION.** That class is for a candidate that *works* with a
  *documented risk* carried into B/C/D. Here the unresolved item is not a side
  risk — it is the **input** `ω` that B/C/D consume. You cannot "carry it as a
  risk"; it must be built first.
- **Not NO-GO.** Nothing falsified the candidate. On the contrary: `f, γ, X` and
  the singular geometry are CLEAN-ALGEBRAIC in `ℚ(√3)`; the proven EBR sibling
  shows the method terminates on a same-program PCF connection coefficient; and
  Stage-5 T2 shows a single isolated Borel branch at an algebraic point — the
  *shape* an algebraic `ω` would have.
- ⇒ **NEEDS-MORE-PROBE:** "candidate partially identified, a specific sub-step
  unresolved; propose a focused 1–2 week follow-up before commitment." Exact fit.

## 7.2 Evidence ledger (supporting the classification)

**For the candidate (positive):**
1. Bridge `C = |Γ(β)|·K`, `S = 2πK` exact; `S/C = 2π/|Γ(β)|` residual `0`
   (Stage 5 T1) — `C` has the rapid-decay-connection-coefficient skeleton
   `Γ(branch)·amplitude`.
2. Dominant Borel singularity at `ξ₀ = 2/√3` to **95.6 digits**, single isolated
   branch (drift `2.1e−5`) (Stage 5 T2) — necessary support for `ω` algebraic.
3. `f, γ`, and `ξ₀, β ∈ ℚ(√3)` are CLEAN-ALGEBRAIC (Stage 4.3).
4. Proven sibling: EBR cc3 realised `κ = Γ(4/3)·A₀` as a Hien rapid-decay period
   of an **algebraic order-4 Borel operator** — a worked template on the same
   program (`data-inventory.json` EBR-CC3-TEMPLATE).
5. Candidate matches FJ Bessel Ex. 1.1.5 shape (regular `0` + irregular-rank-1
   `∞`, rank 2).

**Against / open (the blocker):**
6. **No explicit algebraic Borel operator / de Rham model for V_quad** (gap
   G-OMEGA); `ω = B[φ]dξ`'s field of definition is unidentified.
7. The Painlevé-V **accessory parameter is transcendental** (EBR-II §5) — a
   concrete mechanism by which `ω` could *fail* `k ⊆ ℚ̄`.
8. No explicit V_quad Lax pair in corpus (gap G-LAX); `SL(2)` Galois asserted but
   not located (gap G-KOVACIC); `G_M ≠` differential group.
9. `C`/`S` known only to ~58/~41 digits (not 65 — the task's 65-digit figure is
   the **δ growth constant**, a different object; `data-inventory.json` C1).

## 7.3 Focused follow-up probe (the NEEDS-MORE-PROBE deliverable)

**PERIOD-REP-VQUAD-002 — "Construct the V_quad algebraic Borel/de-Rham model"**
(1–2 weeks). Resolve axiom 3 (and thereby unblock B/C/D).

- **G-OMEGA (primary).** Construct the explicit linear ODE / Borel operator `L_V`
  annihilating the V_quad Borel transform `B[φ]`, the analogue of EBR cc3's
  order-4 `L`. Decide whether `L_V` has **coefficients in `ℚ(√3)`** (⇒ `ω`
  algebraic, axiom 3 VERIFIED) or whether the transcendental accessory parameter
  is unavoidable (⇒ axiom 3 FAILS ⇒ flip to NO-GO for the *clean* form, and pivot
  to a "relative period over the accessory-parameter base" reformulation).
  - **Method:** Borel–Padé of `a_n/Γ(n)` (already have `a_n` to order 1500,
    dps 240) to locate **all** singularities of `B[φ]` (test the 2-instanton tower
    at `2ξ₀, 3ξ₀`); fit the local ODE; attempt holonomic/`G`-operator recognition
    (gfun/`ore_algebra`).
- **G-LAX / G-KOVACIC (supporting).** Write the explicit PV Lax pair from
  Jimbo–Miwa specialised to `(θ_∞=2/√3, α=1/6)`; redo Kovacic to source the
  `SL(2)` claim; identify the irregular-Hodge/`G_M` data needed for axiom 6.
- **Decision gate:** `L_V` algebraic `/ℚ(√3)` ⇒ **upgrade A to GO** and start B/C/D;
  `L_V` provably non-algebraic ⇒ **A becomes NO-GO (clean form)** and Direction 2
  pivots to the relative/family period (see 7.5).

## 7.4 If it upgrades to GO — eventual paper outline (one page)

1. **Intro.** V_quad connection coefficient `C`; statement: `C` is an exponential
   period; CAS/SOTA context (per the AAECC/Lecerf lesson — name what `gfun`,
   `ore_algebra`, `DEtools`, Magma differential-Galois do and where they stop).
2. **The V_quad linear problem.** Explicit PV Lax pair; singularities; `θ_∞=2/√3`.
3. **Borel/de-Rham model.** The operator `L_V`; `[B[φ]],[θB[φ]]` de Rham basis;
   algebraicity over `ℚ(√3)`.
4. **Rapid-decay homology & the period matrix.** Hien pairing; cycles `γ±`;
   `C = ∫_γ e^{−ξ}B[φ]dξ = Γ(β)·K`.
5. **FJ membership.** Verify axioms 1–5; the exponential motive `M=H^1(X,f)`.
6. **Transcendence corollary (conditional).** Under Conjecture 1.3.2, `dim G_M ⇒`
   transcendence/algebraic-independence statement for `C` (mirroring EBR cc3's
   conditional theorem).
7. **Numerics & reproducibility.** The 95.6-digit Borel-singularity check, the
   `Γ(β)·K` bridge, the closed-form nulls.

## 7.5 If it goes NO-GO — alternative direction suggested by the evidence

The evidence (transcendental accessory parameter, non-rigidity) would point to
**Direction "relative/family period"**: realise `C` not as a single exponential
period over `ℚ̄` but as a **period of the family** over the accessory-parameter
base (a relative exponential motive / variation), where the transcendence of the
parameter is absorbed into the base rather than the fibre. This keeps Direction 2
alive in a weaker form and connects to the parent program's variation-of-periods
theme. (Recorded as the fallback, not currently the recommendation.)

## 7.6 Effort estimate for B/C/D (given the candidate)

| sub-problem | description | precondition | estimate |
|-------------|-------------|--------------|----------|
| **A** (this) | scoping: candidate `(X,f,ω,γ)` | — | **done** → NEEDS-MORE-PROBE |
| **A′** = PERIOD-REP-VQUAD-002 | construct `L_V`, settle `ω` algebraicity | A | **1–2 weeks** (data already in hand) |
| **B** | explicit period matrix + Hien pairing for V_quad | A′ GO | 2–3 weeks |
| **C** | FJ motive `M`, `G_M`, conditional transcendence theorem | B | 3–4 weeks |
| **D** | write-up + CAS/SOTA section + reproducibility | C | 2–3 weeks |

**Realistic timeline to a submitted paper, *if* A′ resolves GO:** ~**10–14 weeks**
of focused work past A′ (i.e. ~3–3.5 months), dominated by C (the `G_M`
computation). The single largest schedule risk is A′ itself: if `L_V` is not
algebraic, the clean-form paper does not exist and the program pivots to 7.5.

---

### Closing
**NEEDS-MORE-PROBE (favourable).** The candidate skeleton is real, clean where it
can be, and numerically consistent to 95.6 digits on the one independent check
available; the single blocking sub-step (`ω` algebraicity via an explicit V_quad
Borel operator) is well-defined and cheap (1–2 weeks, data in hand). Recommend
authorising **PERIOD-REP-VQUAD-002** before committing to B/C/D.
