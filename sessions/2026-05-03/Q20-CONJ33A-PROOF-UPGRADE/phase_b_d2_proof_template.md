# Phase B.1 — d=2 proof template (D2-NOTE v1 + CT v1.3 cross-quote)

## B.1.a — D2-NOTE v1 Prop 3.3.A (Proposition `prop:xi0-d2`)

Source: `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/d2_note.tex`
lines 188–210.

> **Proposition (Universality of ξ_0, degree 2;
> [CT v1.3 Prop. 3.3.A]).**  For every degree-2 PCF
> `(1, b)` in scope with `b(n) = β_2 n² + β_1 n + β_0` and
> `β_2 > 0`, the leading Borel-plane singularity of the
> formal generating function `f(z) = Σ Q_n z^n` at `z = 0`
> is located at distance
>
> > ξ_0 = 2 / √β_2
>
> from the origin, and the secondary indicial exponent of
> the formal solution at the irregular singular point
> `u = √z = 0` is
>
> > ρ = −3/2 − β_1 / β_2.

> **Proof (sketch, after [CT v1.3 §3.3]).**  The Newton
> polygon of the homogeneous part of (eq:Lf) at `z = 0`,
> with `d = 2`, is read off from the lattice points
> `{(0,0),(1,0),(1,1),(1,2),(2,0)}` (weight = order of θ,
> height = order of z).  The lower convex hull has a
> single non-trivial edge `(0,0) → (1,2)` of slope 1/2 and
> multiplicity 2, corresponding to a Gevrey-2-in-z
> irregular singularity.  Substituting `z = u²` and
> `θ = (u/2) ∂_u`, the operator becomes Gevrey-1-in-u, and
> the level-1/u trans-series ansatz
>
> > f_±(u) = exp(c/u) · u^ρ · (1 + Σ_{k≥1} a_k u^k)
>
> produces the characteristic polynomial
>
> > χ(c) = 1 − (β_2/4) c²
>
> at leading order, whose two roots are `c = ±2/√β_2`.
> The positive root pins `ξ_0 = 2/√β_2`.  The u^1
> coefficient of the trans-series equation pins the
> indicial polynomial, giving `ρ = −3/2 − β_1/β_2`.  The
> Birkhoff recursion for the `a_k` then proceeds row-by-row
> in the `u^k` coefficient.  The full computation,
> including the worked V_quad example and the
> (α_1, α_0)-independence of ξ_0, is [CT v1.3 §3.3 Worked
> Example].  □

## B.1.b — CT v1.3 Prop 3.3.A (Proposition `prop:xi0`)

Source: `pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex`
lines 502–540.

> **Proposition (Universality of ξ_0, degree 2).**  For
> every degree-2 PCF `(1, b)` in scope with `b(n) = β_2 n²
> + β_1 n + β_0` and `β_2 > 0`, the leading Borel-plane
> singularity of the formal-series generating function
> `f(z) = Σ Q_n z^n` at `z = 0` is located at distance
> `ξ_0 = 2 / √β_2` from the origin, and the secondary
> exponent of the formal solution at the irregular singular
> point `u = √z = 0` is `ρ = −3/2 − β_1/β_2`.
>
> **Proof (Sketch).**  The Newton polygon of the homogeneous
> part of (eq:Lf-cc) at `z = 0` has a single slope-1/2 edge
> `(0,0)–(1,2)` of multiplicity 2, with characteristic
> polynomial `1 − (β_2/4) c²` (whose positive root is
> `ξ_0 = 2/√β_2`).  Substituting `z = u²` converts
> (eq:Lf-cc) to a Gevrey-1-in-u operator with a formal
> solution `f_±(u) = exp(±ξ_0/u) u^ρ (1 + Σ a_k u^k)`; the
> indicial polynomial at `u = 0` in the level 1/u
> trans-series ansatz pins `ρ = −3/2 − β_1/β_2`.
> Coefficients `a_k` are recursively determined and are
> exact rationals in the family parameters.  See
> [CC-PIPELINE-G], claims 1–4 and `newton_birkhoff.py`.  □

## B.2 — Cross-reference status

The D2-NOTE v1 statement and the CT v1.3 statement are
**identical at the proposition level** (both ξ_0 and ρ
formulas) and **identical at the proof-sketch level**
(slope-1/2 edge, characteristic polynomial `1 − (β_2/4) c²`,
trans-series ansatz `f_± = exp(c/u) u^ρ (1 + Σ a_k u^k)`,
indicial polynomial at u^1, Birkhoff recursion).  Both
documents cite **PCF-1 v1.3 §5 / Theorem 5** as the original
source of the d=2 statement (D2-NOTE bib key
`siarc_pcf1_v13`; CT v1.3 bib key `siarc_pcf1_v13`).

**Note on PCF-1 v1.3 §4/§5 source-drift check.** PCF-1 v1.3
itself is the operator's local TeX source; it is not
present under the bridge or under
`pcf-research/` in this workspace.  Per Q20 prompt §4 halt
condition `HALT_Q20_PHASE_B_TEMPLATE_DRIFT` we cannot
cross-quote against PCF-1 v1.3 directly.  However, both
D2-NOTE v1 (which ships in the same commit window as
PCF-1 v1.3) and CT v1.3 §3.3.A internally agree on the
statement and proof; we treat the D2-NOTE v1 + CT v1.3
pair as the canonical d=2 proof template and surface the
PCF-1 v1.3 source-drift check as a **partial-Phase-B
deferral** in the handoff.  The risk that PCF-1 v1.3 §5
disagrees with D2-NOTE v1 / CT v1.3 §3.3.A is low (the
SIARC v1.3 release window was joint), but is not formally
discharged here.
