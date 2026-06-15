# Stage 3 — Riemann–Hilbert translation of the V_quad data

**Chain:** PERIOD-REP-VQUAD-001 · **Stage:** 3 · **Date:** 2026-06-15

**Goal.** Write down the rank-2 linear (isomonodromy) problem whose Painlevé-V
transcendent is V_quad, locate its singularities, and identify *which* Stokes
datum at the irregular point is the connection coefficient `C`, then cross-check
against the deposited Borel transform.

> **AEAL caveat (gap G-LAX).** **No explicit Lax pair / linear ODE for V_quad is
> present in the corpus.** EBR-II §5 (`files/EBR-II-paper.md` L59–61) describes it
> only in words: *"order-2 Heun type, four singular points (p=4), connection datum
> `σ_conn` transcendental in the accessory parameter, in its Painlevé-V Stokes
> data."* Everything in §3.1–§3.2 below is the **standard Jimbo–Miwa Painlevé-V
> linear problem** (literature), **specialised** to the V_quad exponents. It is
> **literature-derived / CONJECTURAL-for-V_quad**, not corpus-verified. Building
> the actual V_quad Lax pair is part of the recommended follow-up.

---

## 3.1 The associated linear problem (Painlevé V, Jimbo–Miwa form)

**Source.** M. Jimbo & T. Miwa, *Monodromy preserving deformation of linear
ordinary differential equations with rational coefficients. II*, Physica D **2**
(1981) 407–448 (DOI 10.1016/0167-2789(81)90021-X); standard PV Lax pair.

Painlevé V is the isomonodromic deformation of a **2×2 system**
```
        dΨ/dz  =  A(z; t) Ψ ,        A(z; t) =  A_0(t)/z  +  A_1(t)/(z−1)  +  (t/2) σ_3/?  ... 
```
more precisely, after the standard normalisation, a system with
```
   A(z) =  ( t/2 ) Θ_∞  +  A_0/z  +  A_1/(z−1) ,      Θ_∞ = diag(+1,−1)·(θ_∞/2 part),
```
having

| singularity | type | rank | exponents / data |
|-------------|------|------|------------------|
| `z = 0`   | **regular** (Fuchsian) | 0 | residue eigenvalues `± θ_0/2` |
| `z = 1`   | **regular** (Fuchsian) | 0 | residue eigenvalues `± θ_1/2` |
| `z = ∞`  | **irregular** | **Poincaré rank 1** | formal exponent `θ_∞`; Stokes structure |

- This is the **confluent-Heun / Whittaker–Kummer** rank-2 shape: **two regular
  points + one irregular rank-1 point**. (The "four singular points `p = 4`" of
  EBR-II §5 counts the irregular point at `∞` with multiplicity 2, i.e.
  `1 + 1 + 2 = 4`; equivalently the confluent Heun count.)
- The **scalar reduction** `y'' = Q(z;t) y` of this system is the Schrödinger /
  WKB form whose large-parameter expansion is the **V_quad WKB series**
  reproduced in `REPRODUCE_stokes_2piK.py` (seed `σ_rec = −1/√3`).

**V_quad specialisation of the parameters (from the Sakai/Galois data):**
- `θ_∞ = 2/√3` **exactly** (task; surface-type note). This is the formal exponent
  / irregular-point data carrying the Borel singularity.
- `α = θ_∞²/8 = 1/6` exactly — the Painlevé-V Hamiltonian parameter combination.
- The **accessory parameter** (equivalently the constant of motion fixing the
  particular V_quad transcendent / the residue `A_0`–`A_1` splitting) is the
  **non-rigid modulus**; per EBR-II §5 it is **transcendental**, and `σ_conn`
  depends transcendentally on it.
- Differential (Picard–Vessiot) Galois group of the *scalar* linear ODE: **SL(2)**
  by Kovacic (task assertion; gap G-KOVACIC — not located as a derivation in the
  corpus, but consistent with a non-Liouvillian rank-2 irregular connection).

## 3.2 Singularities, types, exponents (summary)

- **Regular singular points:** `z = 0`, `z = 1` (Fuchsian; local exponents
  algebraic in `θ_0, θ_1`). These are the points whose local solution data feed
  the algebraic form `ω` of the candidate (Stage 4).
- **Irregular singular point:** `z = ∞`, **Poincaré rank 1** (slope 1) — exactly
  the rank expected for Painlevé V, and exactly the irregular structure of the
  Bessel template (FJ Ex. 1.1.5). The formal solution at `∞` is
  `Ψ_formal ~ z^{Θ_∞} e^{(t/2) z σ_3} · (1 + O(1/z))`, an asymptotic (divergent,
  Gevrey-1) series — **the V_quad WKB series.**
- **Exponent carried to the resurgence side:** `θ_∞ = 2/√3` appears (i) as the
  formal monodromy exponent at `∞` and (ii), through the WKB action integral, as
  the **Borel singularity / instanton action** `A = ξ₀ = 2/√3`. The branch
  exponent `β = −1/(3√3)` is the corresponding sub-leading (one-loop) exponent.

## 3.3 Which Stokes datum is `C`? (Borel-sum picture)

- At the rank-1 irregular point `z = ∞`, the formal series `Ψ_formal` is Borel
  summable in sectors; crossing a **Stokes ray** multiplies the recessive
  solution by `(1 + s · dominant)`, with `s` a **Stokes multiplier**.
- The single active Stokes ray for the V_quad series is the one along the
  **instanton action direction `arg ξ = arg(2/√3) = 0`** (positive real axis in
  the Borel `ξ`-plane): the Borel transform `B[φ](ξ)` has its nearest singularity
  there, at `ξ₀ = 2/√3` (confirmed to **95.6 digits** in Stage 5).
- **The connection coefficient is this Stokes datum.** Writing the
  Borel–Laplace sum `φ(t) = ∫_0^∞ e^{−t ξ} B[φ](ξ) dξ`, the discontinuity of the
  lateral sums across `arg ξ = 0` is governed by the **alien derivative**
  `Δ_{ξ₀} φ`, whose coefficient is the Stokes constant. Concretely
  (`stokes_2piK_results.json` L7, L28, L31):
  ```
     a_n  ~  (S / 2πi) · Γ(n+β) / ξ₀^{n+β}          (large-order / resurgence)
     S    =  2π K                                    (Stokes constant)
     C    =  C_Borel  =  |Γ(β)| · K                  (Borel branch / connection coeff)
     ⇒    S / C  =  2π / |Γ(β)|       (exact; Stage 5 residual = 0)
  ```
  - **`S = 2πK`** is the Stokes multiplier in the "discontinuity" normalisation
    (the `2π` is the universal Cauchy/Borel–Laplace factor, problem-independent;
    repo memory *Stokes constant S*).
  - **`C = |Γ(β)|·K`** is the same datum in the **connection-coefficient
    normalisation** — carrying the `Γ(β)` of the branch `(ξ₀−ξ)^{...}` of
    `B[φ]`. **This is the object with the exponential-period skeleton**
    `Γ(branch exponent) × amplitude`, exactly as the proven EBR sibling has
    `κ = Γ(4/3)·A_0` (cc3 template, `data-inventory.json` EBR-CC3-TEMPLATE).
  - `K` is the V_quad-specific amplitude; the period integral, if it exists, must
    evaluate to (a number-field multiple of) `C` — **this `Γ(β)·amplitude` shape
    is the quantitative target of Stage 4–5.**

## 3.4 Borel-transform cross-check

- **Predicted** (PV irregular-point theory): `B[φ]` has its dominant singularity
  at the instanton action `ξ₀ = 2/√3`, of branch type `(ξ₀ − ξ)^{−β}` with
  `β = −1/(3√3)`.
- **Found** (Stage 5, `numcheck_period_rep_results.json` T2): the Borel radius
  `lim_n |a_n/a_{n+1}|·n = ξ₀ = 2/√3` to **95.6 digits**; the normalised
  amplitude `v_n → |C|` drifts only at the `O(1/n)` (algebraic) level over a
  decade of `n` (relative drift `2.1e−5`), with **no second geometric scale**
  detectable near `|ξ₀|`. ⇒ **CONSISTENT**: a single isolated dominant branch of
  the predicted location and type. (Whether a 2-instanton tower sits at `2ξ₀`,
  `3ξ₀` is below the numerical floor at `n ≤ 1500` and is *not* resolved — see
  Stage 4 ω-cleanliness and the Stage 7 follow-up.)
- **No inconsistency flagged.** The deposited Borel data matches the natural Borel
  transform of the formal solution at `z = ∞`.

---

### One-line summary
V_quad's linear problem is the standard **rank-2 Painlevé-V system** (regular
points `0,1`; **irregular rank-1 at `∞`**, `θ_∞ = 2/√3`); the connection
coefficient `C` is the **Stokes datum on the `arg ξ = 0` ray**, equal to
`|Γ(β)|·K` (`= (|Γ(β)|/2π)·S`), with `B[φ]` singular at `ξ₀ = 2/√3` (95.6-digit
confirmed) — but the explicit V_quad Lax pair is **not in the corpus** (gap
G-LAX) and the accessory parameter is **transcendental** (EBR-II §5).
