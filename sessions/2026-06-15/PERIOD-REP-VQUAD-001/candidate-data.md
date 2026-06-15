# Stage 4 — Candidate exponential-motive data `(X, f, ω, γ)`

**Chain:** PERIOD-REP-VQUAD-001 · **Stage:** 4 · **Date:** 2026-06-15

**Construction principle.** Port the **proven EBR cc3 template** (the same parent
program, the sibling that *worked*) to the V_quad Borel plane, and match it to
the Fresán–Jossen canonical shapes (Ex. 1.1.4 gamma-values, Ex. 1.1.5 Bessel).
In cc3 the connection coefficient is realised as
`κ = Γ(4/3)·A₀ = ∫_{γ±} e^{−f} ω` for an **algebraic order-4 Borel operator `L`**
with de Rham basis `{[Φ],[θΦ]}` and Hien rapid-decay cycles `γ±`
(`data-inventory.json` → `EBR-CC3-TEMPLATE`). The V_quad analogue replaces the
holonomic `Φ` by the V_quad Borel transform `B[φ]`.

> **Sign reminder.** FJ pairing is `∫_γ e^{−f}ω`; the task's `e^{+f}` means
> `f_task = −f_FJ`. Below, `f` is the **FJ-sign** potential (`e^{−f}`).

---

## 4.1 The candidate (explicit)

The connection coefficient `C = C_Borel = |Γ(β)|·K` is realised as the
**Borel–Laplace (rapid-decay) period** of the V_quad Borel transform:

```
   C  ∝  ∫_γ  e^{−ξ}  B[φ](ξ)  dξ ,      with
```

| comp. | candidate | explicit formula | derives from |
|------|-----------|------------------|--------------|
| **X** | Borel `ξ`-curve | `X = 𝔾_m,ξ` (i.e. `𝔸¹_ξ ∖ {0}`); singular fibres of `B[φ]` at `ξ = 0` (origin of the Borel plane) and the branch point `ξ = ξ₀ = 2/√3`; irregular at `ξ = ∞` | scalar reduction of the PV system at `z=∞` (Stage 3 §3.1); Borel plane of `REPRODUCE_stokes_2piK.py` |
| **f** | Laplace phase | `f(ξ) = ξ` (linear); the rapid-decay direction is `arg ξ = 0`, the Stokes ray to `ξ₀` | Borel–Laplace sum `φ(t)=∫_0^∞ e^{−tξ}B[φ]dξ`, `t=1` (`MEMO`/`results.json` L7) |
| **ω** | Borel 1-form | `ω = B[φ](ξ) dξ`, where near `ξ₀`: `B[φ](ξ) ≈ (const)·(ξ₀−ξ)^{−β} + holo.`, `β = −1/(3√3)` | resurgence branch (`results.json` L6–7); large-order `a_n~(S/2πi)Γ(n+β)/ξ₀^{n+β}` |
| **γ** | rapid-decay thimble | `γ =` Hankel/steepest-descent contour wrapping the cut `[ξ₀, +∞)` along `arg ξ = 0`; on its unbounded part `Re(f)=Re(ξ)→+∞` so `e^{−f}` decays | Stokes ray of Stage 3 §3.3; FJ Def. 3.1.1.1 |

**Why this evaluates to `Γ(β)·K`.** Integrating the local branch
`(ξ₀−ξ)^{−β}` against `e^{−ξ}` over the Hankel thimble produces a **`Γ`-factor**
by the Hankel representation of the Gamma function (precisely the mechanism that
gives `Γ(j/n)` in FJ Ex. 1.1.4 and `Γ(4/3)` in EBR cc3): the branch exponent `β`
yields `Γ(β)`, and the local normalisation of `B[φ]` at `ξ₀` yields the
amplitude `K`. Hence `C ∝ Γ(β)·K` — **the bridge identity `C = |Γ(β)|·K`
verified to ~58 digits in Stage 5 is exactly this period’s skeleton.**

This is the **Bessel template (FJ Ex. 1.1.5)** with an extra modulus: rank-2,
**regular point at `ξ=0` + irregular rank-1 at `ξ=∞`**, but **non-rigid** (the
transcendental accessory parameter), so `B[φ]` is a Bessel/Kummer-*flavoured*
function with a continuous parameter rather than the rigid `J_n, H_n`.

## 4.2 Status of each component

| comp. | proven / conjectural | algebraicity / rationality |
|------|----------------------|----------------------------|
| **X = 𝔾_m** | CONJECTURAL-structural (the Borel curve is `𝔾_m` *if* `B[φ]` has exactly the singular set `{0, ξ₀, ∞}`; the `{0,ξ₀}` part is supported, `∞`/extra-singularity census is open) | defined `/ℚ` |
| **f = ξ** | the Laplace phase is forced by Borel–Laplace; the rapid-decay direction `arg ξ=0` is the Stage-5-confirmed singular ray | `/ℚ`; singular locus `ξ₀ = 2/√3 ∈ ℚ(√3)` algebraic |
| **ω = B[φ]dξ** | **CONJECTURAL; algebraicity UNPROVEN** — no explicit algebraic Borel operator for V_quad exists (gap G-OMEGA); the accessory parameter is transcendental (EBR-II §5) | **coefficient field UNCERTAIN** — the whole question |
| **γ = Hankel thimble** | PROVEN-structural (rapid decay by construction; the singular ray is Stage-5-confirmed) | `ℚ(√3)`-rational endpoint `ξ₀` |

## 4.3 Cleanliness assessment (Stage 4.3 schema)

- **`f` — CLEAN-ALGEBRAIC.** Linear, `f = ξ`, coefficients in `ℚ`; the rapid-decay
  ray and the singular location `ξ₀ = 2/√3 ∈ ℚ(√3)` are exact algebraic.
- **`γ` — CLEAN-CLASSICAL.** A Hankel/steepest-descent thimble — the canonical
  rapid-decay cycle of an irregular rank-1 connection (FJ Ex. 1.1.4–1.1.5). Its
  defining ray is numerically pinned to `ξ₀` at 95.6 digits (Stage 5).
- **`X` — CLEAN-ALGEBRAIC (provisional).** `𝔾_m / ℚ` *if* the singular set is
  `{0, ξ₀, ∞}`; the only un-pinned part is whether a 2-instanton tower adds
  further singular points (below the numerical floor; Stage 7 follow-up).
- **`ω` — HEDGED → UNCLEAN (the load-bearing component).** `ω = B[φ]dξ` is a
  *classical-special-function* form (Bessel/Kummer-flavoured), so it is **not**
  obviously rational; worse, **its algebraicity over a number field is unproven**
  because (i) no explicit algebraic Borel operator (the V_quad analogue of EBR's
  order-4 `L`) has been constructed, and (ii) the Painlevé-V accessory parameter
  it depends on is **transcendental**. Classification: **UNCLEAN** for the strict
  FJ `k ⊆ ℚ̄` requirement, **HEDGED** in the weaker "classical special function
  with continuous parameter" sense.

  **Per the Stage-4.3 rule this is a GO/NO-GO concern, *not* a stopper.** The
  positive Stage-5 evidence (single isolated branch of Nilsson type at an
  algebraic location) is *necessary* for `ω` algebraic and is encouraging, but it
  is **not sufficient**: it does not exhibit `B[φ]` as the period of an algebraic
  de Rham form.

---

### One-line summary
**Candidate:** `X = 𝔾_m,ξ`, `f = ξ`, `ω = B[φ](ξ)dξ`, `γ =` Hankel thimble on
`[ξ₀,∞)`, giving `C ∝ Γ(β)·K` (bridge-confirmed ~58 dig). **`f, γ` and the
singular geometry are CLEAN-ALGEBRAIC in `ℚ(√3)`; `X` is provisionally clean;
`ω = B[φ]dξ` is the one UNCLEAN component** — algebraicity over `ℚ̄` is unproven
pending an explicit V_quad algebraic Borel operator (gap G-OMEGA).
