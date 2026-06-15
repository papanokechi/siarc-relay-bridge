# Stage 5 — Numerical sanity check

**Chain:** PERIOD-REP-VQUAD-001 · **Stage:** 5 · **Date:** 2026-06-15
**Script:** `scripts/numcheck_period_rep.py` (mpmath; order 1500, dps 240; runtime ~10 s)
**Output:** `scripts/numcheck_period_rep_results.json`

> **Honest scope.** No *clean integral evaluation* of `C` is performed here,
> because the algebraic de Rham form `ω = B[φ]dξ` is not yet an explicit object
> (gap G-OMEGA). Instead Stage 5 runs four **falsification-first** checks that are
> the cheapest way to *kill* a wrong candidate. Three are confirmatory; the fourth
> (the decisive one for `ω`) is left explicitly **partially open**.

---

## T1 — Bridge `C = |Γ(β)|·K`, `S = 2πK` (exponential-period skeleton)

| quantity | value | check |
|---------|-------|-------|
| `K` | `0.0728781025518669641294423633296525128045556892…` | matches deposited (`stokes_2piK_results.json`) to 58 dig |
| `S = 2πK` | `0.457906623169017636119097842548225837962395135…` | vs deposited anchor: **41.3 digits** |
| `C = |Γ(β)|·K` | `0.437705286193537221230739749794369589981725597…` | vs historical `0.43770528619353722123074`: **23 dig** (anchor only published to 23) |
| `S / C` vs `2π/|Γ(β)|` | residual **`0.0` (exact)** | the two normalisations are the *same* Borel datum |

**Reading.** `C` carries the `Γ(branch-exponent)` factor characteristic of a
rapid-decay connection coefficient — the **same skeleton** as the proven EBR
sibling `κ = Γ(4/3)·A₀`. *Caveat:* `C = |Γ(β)|·K` is, by construction, a rewrite
of the same large-order data, so T1 is a **consistency** check, not an
*independent* evaluation. Its value is to confirm the **shape** `Γ(β)·amplitude`,
which is what a Stage-4 period integral must reproduce.

## T2 — Borel singularity census (the `ω`-cleanliness probe — *non-circular*)

The original WKB series is Gevrey-1 (radius 0); the meaningful object is the
**Borel transform** `B[φ](ξ)=Σ a_n ξ^{n−1}/Γ(n)`, whose radius of convergence is
the distance to the nearest Borel singularity, `lim_n |a_n/a_{n+1}|·n`.

| diagnostic | result | meaning |
|-----------|--------|---------|
| dominant Borel radius `lim|a_n/a_{n+1}|·n` vs `ξ₀ = 2/√3` | agree to **95.6 digits** | dominant singularity is **exactly** at `ξ₀ ∈ ℚ(√3)` — a clean algebraic location |
| normalised amplitude `v_n = |b_n|ξ₀^{n+β}/n^β` relative drift over a decade of `n` | **`2.1×10⁻⁵`** (algebraic `O(1/n)` only) | **no second geometric scale** detectable near `|ξ₀|` — consistent with a **single isolated dominant branch** of Nilsson type `(ξ₀−ξ)^{−β}` |

**Reading.** The Borel transform behaves, to the resolution available at
`n ≤ 1500`, like the period of a **regular-holonomic / algebraic** kernel with one
isolated dominant branch at an algebraic point — the shape an *algebraic* `ω`
would have. **This is NECESSARY but NOT SUFFICIENT** for `ω` algebraic: exactly
locating any 2-instanton tower at `2ξ₀, 3ξ₀` (astronomically suppressed at this
`n`) and *proving* `B[φ]` is an algebraic de Rham period both require a
**Borel–Padé + an explicit V_quad Borel operator** — deferred (Stage 7 follow-up).

## T3 — Fresán–Jossen "clean (degenerate) period" null

PSLQ of `S` and of `C` against `{π, √3, √π, Γ(1/3), Γ(2/3), Γ(1/6), Γ(5/6)}` at
dps 45, maxcoeff `10⁵`: any relation returned has height `~10⁴–10⁵` (at the
detection floor) ⇒ **SPURIOUS ⇒ NULL CONFIRMED**. Neither `S` nor `C` is a
low-height combination of `√π` / single Γ-values.

**Reading.** `C` is **not** a degenerate gamma-motive (dimension-1) exponential
period — it is a **genuine higher** exponential period *if it is one at all*.
Consistent with the deposited 169-digit (EBR) and 55-digit (V_quad `S`) nulls.

## T4 — Sign / branch bookkeeping

FJ pairing `∫_γ e^{−f}ω` vs task `∫_γ e^{+f}g dt` ⇒ `f_task = −f_FJ` (same object).
Borel–Laplace realisation `φ(t)=∫_0^∞ e^{−tξ}B[φ]dξ`; the connection datum is the
rapid-decay period of `B[φ]` across the ray to `ξ₀ = 2/√3`. No sign pathology.

---

## Stage 5 verdict (did anything falsify the candidate?)

**No falsification; one decisive check left partially open.**
- T1 ✅ skeleton `C = Γ(β)·K` confirmed (consistency).
- T2 ✅ dominant Borel singularity at `ξ₀ = 2/√3` to 95.6 dig, single isolated
  branch (necessary support for `ω` algebraic) — **but not sufficient.**
- T3 ✅ `C` is a non-degenerate period (null reconfirmed).
- T4 ✅ conventions reconciled.

**No adjustment/retry was needed** (Stage 5.4 retries unused): the candidate
*skeleton* matches the numerics at every level it can be tested without the
explicit algebraic `ω`. The agreement that *would* upgrade the verdict — an
independent clean integral evaluating to `C` — **cannot be run yet**, precisely
because `ω`'s algebraic model is the open sub-step.
