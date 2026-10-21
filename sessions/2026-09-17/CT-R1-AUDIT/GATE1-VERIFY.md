# GATE 1 — verification of the companion v1.3 notice against companion v1.2

**Gate:** *"Run a non-isolated check that every tuple, equation and remark
number quoted in the notice matches companion v1.2, reading page images as the
P0 rule requires."* (Operator review #5, gate 1.)

This is the check Packet B's reader could not perform, because that reader was
deliberately isolated from the companion PDF.

## Source

| | |
|---|---|
| File | `refs/vquad_resurgence_v1.2_zenodo-20481592.pdf` |
| sha256 | `a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85` |
| Pages | 12 |
| Locator script | `gate1_locate.py` → `gate1_locate.log` |
| Page images read | `coldpackets/companion_v12_p{2,3,5,6,7,9}.png`, rendered at 3× |

Text extraction was used **only to locate** the pages. Every quoted string below
was then confirmed against the rendered page image, per the P0 citation rule.

## Result: every quoted number and tuple matches. No defect found.

| # | Quoted in the notice | v1.2, verbatim | Page (PDF idx) | Verdict |
|---|---|---|---|---|
| 1 | Remark **2.2** is the apparency claim | "Remark 2.2 (PCF-derived ODEs and the `b(x) = a′(x)` structure)" | p. 4 (3) | **MATCH** |
| 2 | Remark 2.2 asserts the roots of `χ` are apparent | "the finite singularities of the ODE — the roots of χ — are **always apparent**" | p. 4 (3) | **MATCH**, verbatim |
| 3 | The ODE has the form `χ y'' + χ' y' + c y = 0` | "a continuum ODE of the form `χ(x) y′′ + χ′(x) y′ + c(x) y = 0`" | p. 4 (3) | **MATCH**, verbatim |
| 4 | Conjecture **4.1** is the PV classification | "Conjecture 4.1 (Painlevé V (D₅⁽¹⁾) classification)" | p. 6 (5) | **MATCH** |
| 5 | The tuple `(α, β, γ, δ) = (1/6, 0, 0, −1/2)` | "α = 1/6, β = 0, γ = 0, δ = −1/2" | p. 6 (5) | **MATCH** |
| 6 | `β = γ = 0` is derived from apparency | "The vanishing β = γ = 0 reflects the fact that both finite singularities are apparent"; and "determined by the WKB exponents (11) and the **apparent-singularity condition θ₁ = θ₂ = 0**" | p. 6 (5) | **MATCH** |
| 7 | `θ₁ = θ₂ = 0` | "two regular singularities with formal monodromy exponents θ₁ = θ₂ = 0 (apparent)" | p. 6 (5) | **MATCH** |
| 8 | `D̃₅` / `D₅⁽¹⁾` is the claimed surface type | "the Sakai rational surface of type D₅⁽¹⁾, with affine Weyl symmetry W(A₃⁽¹⁾) ≅ S̃₄" | p. 6 (5) | **MATCH** |
| 9 | `χ = 3x² + x + 1`, `χ' = 6x + 1`, `c = −x²` | Table 1: ODE leading coeff `a(x) = 3x²+x+1`; middle `b(x) = 6x+1 = a′(x)`; trailing `c(x) = −x²` | p. 4 (3) | **MATCH** |
| 10 | Two finite regular singular points at the roots of `χ` | "s₁,₂ = (−1 ± i√11)/6", "Both are regular singular points" | pp. 3–4 (2–3) | **MATCH** |
| 11 | Irregular singular point of Poincaré rank 1 at `∞` | "one irregular singular point of Poincaré rank 1 at x = ∞" | p. 3 (2) | **MATCH** |

**Gate 1 verdict: PASS.** No tuple, equation number or remark number quoted in
the draft notice is wrong.

## Two findings that strengthen the notice

Gate 1 was a check, not a search, but it turned up two things that make the
correction more robust. Both have been folded into **C2**.

### F1 — the companion states the scaling law we used, and applies it itself

Packet B's caveat was that our refutation might be convention-dependent. It is
not, and the reason is stronger than an independent re-derivation: **v1.2 states
the same transformation law and uses it**. From p. 6 (PDF idx 5), verbatim:

> "The canonical Painlevé V normalization fixes this coefficient to 1 by the
> rescaling `z ↦ √3 z`, under which the PV parameters transform as
> `(α, β, γ, δ) ↦ (α, β, cγ, c²δ)` with `c = √3`. This leaves `α = 1/6` and
> `β = γ = 0` invariant and sends `δ ↦ 3·(−1/6) = −1/2 ≠ 0`"

Three consequences:

1. The law `(α, β, γ, δ) ↦ (α, β, cγ, c²δ)` is **the companion's own**. The
   convention objection is closed by the paper's own text, with no appeal to
   our derivation at all.
2. The claim that the rescaling "leaves `γ = 0` invariant" is true **only
   because `γ` was taken to be `0`**. Under `γ ↦ cγ`, the correct value `γ = 1`
   maps to `√3`, not to `0`.
3. `δ = −1/2` is reached from `δ_raw = −1/6` by `c² = 3`. So `δ = −1/2` is the
   *canonical* normalisation, which is exactly the scale in which `γ` is pinned.

### F2 — the `γ` error does not depend on C1

The companion assigns `θ₁ = θ₂ = 0`, and **those values are correct**: the local
exponents at both finite points really are `0, 0`. Jimbo's dictionary then gives

```
    γ = 1 − θ₀ − θ_t = 1 − 0 − 0 = 1 ,
```

so `γ = 0` is unattainable **on the companion's own local data**, independently
of whether the points are apparent. C1 is therefore not load-bearing for the
`γ` contradiction; it is load-bearing for the *monodromy* statement (unipotent
and nontrivial, not trivial) and for Remark 2.2 itself.

This matters for the deposit: C2 now has two independent grounds, and the weaker
of them does not rely on a lemma proved in this run.

## Downstream passages (new section C5)

The full-text pass located every place in v1.2 that depends on apparency. These
are tabulated in **C5** of the draft notice. The substantive one is **§7.1
item 1**, which offers apparency as the first of four components of a "complete
explanation" for the identification obstruction; that component must be
withdrawn or re-argued. The other three components are unaffected — in
particular the degeneration of the Jimbo connection formula at `θ₁ = θ₂ = 0`
survives, because those exponent values are correct.

## Gate 3 (wording) — one defect found and fixed

* **"Necessary condition" language on every row match** — present. C4 carries it
  as numbered point 1, and points 2–4 reinforce it. **PASS.**
* **C3 exactly as drafted** — **FAILED, now fixed.** The drafted restatement
  names the object: *"System C has the local formal type of the PV/D̃₅
  family…"*. The notice had *"The operator has the local formal type…"*, which
  is precisely the ambiguity that C4 exists to forbid — and "operator" is also
  overloaded in this repository, where it denotes the human principal. Corrected
  to read "System C". **NOW PASS.**

## Labels

| Claim | Label | Review |
|---|---|---|
| Every tuple/equation/remark number in the notice matches v1.2 | INSPECTED | `self` — this is a non-isolated check by the session that drafted the notice; that is what the gate asked for |
| F1: v1.2 states and applies `(α,β,cγ,c²δ)` | INSPECTED | `self` |
| F2: `γ = 1 − θ₀ − θ_t = 1` on the companion's own `θ` values | PROVEN (exact arithmetic from a quoted dictionary) | `self` |

Per the R8 rule, these are absence/presence facts about file contents read at a
stated sha256, so they are **INSPECTED**, not PROVEN, except where the claim is
pure arithmetic.
