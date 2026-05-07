# Phase B — Chart-Map Required Form (the GAP side)

**Session:** 075 T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK
**Phase:** B
**Scope:** structural-form specification of the chart-map artefact
that 069r1 NO_GO_SUBSTRATE_INSUFFICIENT identifies as the open R1
substrate gap. SUBSTRATE-INVENTORY ONLY; no chart-map construction
is attempted; no R1-closure assertion is made.

---

## §B.1 — Verbatim quote of 069r1 A.1.5 chart-map block

(35 words; ≤ 50-word envelope ceiling PASS.)

Source: `sessions/2026-05-07/M6-CC-R1-CLOSURE-PREFLIGHT-069R1/phase_a_path_alpha.md`
SHA `c8dc5f4e9865a24d9a3fd623320257cd11de17762ecefc82ffa4566f73bb2e5`,
§1.5 "Required artefact" block (file lines L62-L72).

> "The envelope requires that the explicit map between the KNY 2017
> §8.5.17 $(a_{0}, a_{1}, a_{2})$ chart and the Okamoto 1987 §3
> four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$
> convention be cited verbatim from 058R + 069 substrate as four
> equations …"

(BT 1933-style display block from same file:)

> "$\alpha_{\infty} = f_{\alpha_{\infty}}(a_{0}, a_{1}, a_{2}),\;
>  \alpha_{0} = f_{\alpha_{0}}(a_{0}, a_{1}, a_{2}),$
>  $\beta_{\infty} = f_{\beta_{\infty}}(a_{0}, a_{1}, a_{2}),\;
>  \beta_{0} = f_{\beta_{0}}(a_{0}, a_{1}, a_{2}),$
>  with each $f_{\ast}$ a closed-form polynomial (or rational)
>  expression in $(a_{0}, a_{1}, a_{2})$." (29 words.)

Verbatim 058R anchor (cited downstream by 069r1):

Source: `sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/phase_b_canonical_map.md`
SHA `f831f9bd58d1f3064873dfdeab14c003bf441cbb3832e02b6cdddc94a91ff8bb3`,
file lines L136-L140.

> "(i) explicit conversion of the V_quad's CT v1.3 §3.5 4-tuple
> $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) =
> (1/6, 0, 0, -1/2)$ to KNY $(a_{0}, a_{1}, a_{2})$ — this is
> residual R1 partially closed; the 4-tuple does NOT satisfy
> Okamoto's $\alpha_{\infty}+\alpha_{0}+\beta_{\infty}+\beta_{0}=0$
> constraint (sums to $-1/3$)" (44 words.)

(One permitted occurrence of "closed" appears verbatim inside the
quoted 058R sentence — declared explicit per §6 envelope rule and
counted in `forbidden_verb_scan.md` as the single permitted quote.)

## §B.2 — Decomposition into structural primitives

The structural primitives below are extracted from the §B.1 verbatim
quotes. Each primitive is labelled `[GAP-PRIMITIVE-Bn]` per envelope
§6.

### [GAP-PRIMITIVE-B1] Domain space

- **Object:** the KNY 2017 §8.5.17 chart 3-tuple $(a_{0}, a_{1}, a_{2})$.
- **Dimensionality:** 3 real parameters.
- **Constraint(s):** linear relation $a_{0} + a_{1} = 1$ (cited via
  069 `phase_d_numerical.md` §1 SHA `e98d74ebd30eb43c..` per 069r1
  §1; reduces effective dimension to 2 + $a_{2}$).
- **Nature:** parameter-space coordinates of an irregular-singular
  difference / ODE setup; coefficients of the underlying KNY chart
  parametrisation, not function-space objects.

### [GAP-PRIMITIVE-B2] Codomain space

- **Object:** the Okamoto 1987 §3 four-tuple $(\alpha_{\infty},
  \alpha_{0}, \beta_{\infty}, \beta_{0})$ (per CT v1.3 §3.5 rename;
  equivalent to Okamoto's original $(\eta_{\infty}, \eta_{0},
  \theta_{\infty}, \theta_{0})$ Lax-pair monodromy parameters per
  069r1 anomaly U1).
- **Dimensionality:** 4 real parameters.
- **Constraint(s):** Okamoto null-sum $\alpha_{\infty} + \alpha_{0}
  + \beta_{\infty} + \beta_{0} = 0$ (reduces effective dimension to
  3).
- **Nature:** parameter-space coordinates of the same Painlevé-III
  equation in a second chart (Okamoto / monodromy chart); not a
  function-space object.

### [GAP-PRIMITIVE-B3] Map functional form

- **Object:** four scalar maps $f_{\alpha_{\infty}}$,
  $f_{\alpha_{0}}$, $f_{\beta_{\infty}}$, $f_{\beta_{0}}$.
- **Form requested by 069r1 verbatim:** "closed-form polynomial (or
  rational) expression in $(a_{0}, a_{1}, a_{2})$".
- **Nature:** algebraic identity between the two parameter charts;
  **NOT** a series expansion, **NOT** a function-of-$x$, **NOT** a
  matrix-valued object.

### [GAP-PRIMITIVE-B4] Map cardinality / arity

- **Cardinality:** 4 separate scalar maps $f_{\alpha_{\infty}},
  f_{\alpha_{0}}, f_{\beta_{\infty}}, f_{\beta_{0}}$ — one per
  output coordinate.
- **Arity:** each $f_{\ast}$ is a scalar function of three real
  inputs $(a_{0}, a_{1}, a_{2})$.
- **Net structure:** 3-real → 4-real (effectively 2-real → 3-real
  modulo the two algebraic constraints).

### [GAP-PRIMITIVE-B5] Sectorial / regional structure

- **Specification by 069r1 §A.1.5:** chart-map identity is **NOT**
  sector-dependent. The map is a single global parameter-chart
  identity for the same Painlevé-III equation.
- **Anchor:** 069r1 `phase_a_path_alpha.md` §1 + §1.5 expresses the
  4-tuple as scalar pinning at one V_quad parameter point
  $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) = (1/6,
  0, 0, -1/2)$, with the requested map relating the two coordinate
  charts globally on parameter space.

### [GAP-PRIMITIVE-B6] Constraint / linear relation structure

- **Domain:** $a_{0} + a_{1} = 1$ (algebraic linear constraint).
- **Codomain:** Okamoto null-sum $\alpha_{\infty} + \alpha_{0} +
  \beta_{\infty} + \beta_{0} = 0$ (algebraic linear constraint).
- **Compatibility requirement:** the chart-map must respect both
  constraints; failure to do so at the V_quad parameter point is
  the residual R1 itself (069 anomaly D2 + 069r1 §1.5).

### [GAP-PRIMITIVE-B7] Mathematical type

- **Type:** ALGEBRAIC chart-map between two parameter charts of the
  same Painlevé-III equation (project naming: the KNY chart and the
  Okamoto chart).
- **Distinction:** the map is **NOT** Stokes/connection-data
  expansion; it is **NOT** a Riemann-Hilbert correspondence (those
  link parameters to monodromy invariants of solutions, a different
  object); it is the chart-translation identity at the parameter-
  space level.

## §B.3 — Structural-form spec table (gap side)

Table format: each primitive is one row; each column captures one
structural attribute. This table is the input to Phase D's match
matrix.

| Primitive            | Gap-side specification                                                                                               |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| [GAP-PRIMITIVE-B1]   | Domain = real 3-tuple $(a_{0}, a_{1}, a_{2})$ of KNY-chart parameters; constraint $a_{0}+a_{1}=1$.                     |
| [GAP-PRIMITIVE-B2]   | Codomain = real 4-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$ of Okamoto parameters; null-sum 0. |
| [GAP-PRIMITIVE-B3]   | Form = closed-form polynomial OR rational expressions; **algebraic** identity, not series expansion.                   |
| [GAP-PRIMITIVE-B4]   | Cardinality = 4 separate scalar maps; arity 3-real → 1-real per map.                                                   |
| [GAP-PRIMITIVE-B5]   | NOT sector-dependent; single global parameter-chart identity.                                                          |
| [GAP-PRIMITIVE-B6]   | Algebraic constraints on both domain ($a_0+a_1=1$) and codomain (null-sum 0).                                          |
| [GAP-PRIMITIVE-B7]   | Type = algebraic chart-translation (parameter-chart ↔ parameter-chart).                                                |

## §B.4 — Discipline reassertion

This Phase-B output is a structural-form **specification** of what
069r1 A.1.5 declares as the open R1 substrate gap. It does **not**
construct the chart-map; it does **not** propose closed-form
expressions for $f_{\alpha_{\infty}}, f_{\alpha_{0}}, f_{\beta_{\infty}},
f_{\beta_{0}}$; it does **not** assert R1 is closed. Per envelope §6,
the substrate gap remains a W21 LANE-1 T1-Synth analytic-guidance
question (or path-δ literature acquisition question) per 069r1
NO_GO_SUBSTRATE_INSUFFICIENT verdict.

End of `chart_map_required_form.md`.
