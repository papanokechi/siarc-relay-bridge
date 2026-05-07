# Phase D — Structural-Form Match Matrix

**Session:** 075 T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK
**Phase:** D
**Scope:** side-by-side comparison of the Phase B.3 spec table
(chart-map required form, gap side) against the Phase C.4 spec
table ((13 a) form, fill side); per-primitive verdict marking.
SUBSTRATE-INVENTORY ONLY; no chart-map construction; no R1-closure
assertion.

---

## §D.1 — Side-by-side comparison

| Primitive | Gap side (Phase B.3)                                                                                                              | Fill side (Phase C.4)                                                                                                                  | Match verdict      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| **B1↔C1** | Real 3-tuple $(a_{0}, a_{1}, a_{2})$ of KNY-chart parameters; constraint $a_{0}+a_{1}=1$.                                         | $(i, j, r) \in \{1,\ldots,n\}^{2} \times \{m,\ldots,\eta-1\}$ + continuous $x$ in strip; function-space object.                          | [MISMATCH-D1]      |
| **B2↔C2** | Real 4-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$ of Okamoto parameters; null-sum 0.                       | $\mathbb{C}$-valued holomorphic function of $x$ on strip $V_{r,r+1}$; periodic in $\Im x$.                                              | [MISMATCH-D2]      |
| **B3↔C3** | Form = closed-form polynomial OR rational expressions; **algebraic** identity, not series expansion.                              | Form = Fourier / q-series $\sum_{\pi} c_{\pi} e^{-\pi_{i j}(r,r+1)}$ in $z = e^{-x_{r}}$; **analytic** series, not closed-form algebraic. | [MISMATCH-D3]      |
| **B4↔C4** | Cardinality = 4 scalar maps; arity 3-real → 1-real per map.                                                                       | Cardinality = $n^{2} \times (\eta - m)$ scalar entry-functions; arity each: 1 complex variable $x$ → $\mathbb{C}$.                       | [MISMATCH-D4]      |
| **B5↔C5** | NOT sector-dependent; single global parameter-chart identity.                                                                     | Sector-dependent **by construction** — defined per adjacent-region pair $(r, r+1)$ separated by B'-curve $B^{r}$.                        | [MISMATCH-D5]      |
| **B6↔C6** | Algebraic constraints on both domain ($a_0+a_1=1$) and codomain (null-sum 0).                                                     | Analytic constraints (convergent power series in $z$; non-vanishing leading coefficient); no algebraic linear constraint on parameters. | [MISMATCH-D6]      |
| **B7↔C7** | Type = algebraic chart-translation (parameter-chart ↔ parameter-chart).                                                           | Type = analytic connection-matrix / Stokes-data (function-space object), **not** algebraic chart-translation.                            | [MISMATCH-D7]      |

## §D.2 — Per-primitive justifications (each ≤ 30 words)

### [MISMATCH-D1] — Domain space
Justification (28 words): gap-side B1 is a real 3-tuple of equation-
coefficient parameters; fill-side C1 is a function-space object
indexed by $(i, j, r)$ with continuous strip variable $x$. Cite
069r1 `phase_a_path_alpha.md` SHA `c8dc5f4e..` §1.5 + 073
`bt_1933_section_5_extract.md` SHA `ec2c0d5a..` [p. 46] eq. (11 a).

### [MISMATCH-D2] — Codomain space
Justification (28 words): gap-side B2 is a real 4-tuple of Okamoto
parameter scalars constrained by null-sum 0; fill-side C2 is a
$\mathbb{C}$-valued holomorphic function of $x$ on a strip. Cite
069r1 `phase_a_path_alpha.md` SHA `c8dc5f4e..` §1 + 073
`bt_1933_section_5_extract.md` SHA `ec2c0d5a..` [p. 47] eq. (13 a).

### [MISMATCH-D3] — Map functional form
Justification (29 words): gap-side B3 explicitly requires "closed-
form polynomial (or rational) expression"; fill-side C3 is a
discrete-index Fourier / q-series in periodic variable
$z = e^{-x_{r}}$. Cite 069r1 `phase_a_path_alpha.md` SHA
`c8dc5f4e..` §1.5 + 073 `bt_1933_section_5_extract.md` SHA
`ec2c0d5a..` (13 a) line.

### [MISMATCH-D4] — Map cardinality
Justification (30 words): gap-side B4 is 4 scalar maps with
3-real domain; fill-side C4 is $n^{2} \times (\eta - m)$ entry-
functions of one complex variable; cardinality structures coincide
only superficially at $n = 2$. Cite 069r1 §1.5 + 073 (11 a)/(13 a).

### [MISMATCH-D5] — Sectorial structure
Justification (29 words): gap-side B5 is a single global parameter-
chart identity (not sector-indexed); fill-side C5 is sector-indexed
by adjacent-region pair $(r, r+1)$ separated by B'-curve $B^{r}$,
sectorial **by construction**. Cite 069r1 §A.1.5 + 073 [p. 46].

### [MISMATCH-D6] — Constraint structure
Justification (30 words): gap-side B6 carries algebraic linear
constraints ($a_{0}+a_{1}=1$ and null-sum); fill-side C6 carries
analytic constraints (convergent power series; non-vanishing
leading coefficient); no algebraic-vs-analytic structural overlap.
Cite 069r1 §1.5 + 073 [p. 47] (13) preamble.

### [MISMATCH-D7] — Mathematical type
Justification (30 words): gap-side B7 is an algebraic parameter-
chart translation between two parameter charts of one Painlevé-III
equation; fill-side C7 is analytic Stokes / connection-matrix data
between sectorial proper solutions. Cite 069r1 §1.5 + 073 [p. 46]-
[p. 47].

## §D.3 — Aggregate count per envelope §9 ladder

| Verdict label   | count |
|-----------------|-------|
| MATCH           | 0     |
| MISMATCH        | 7     |
| UNDETERMINED    | 0     |

Total primitives compared: 7.

Per envelope §9 ladder:
- **STRUCTURAL_MATCH** condition (≥ 80 % MATCH AND 0 % MISMATCH):
  not satisfied (0 % MATCH; 100 % MISMATCH).
- **STRUCTURAL_MISMATCH** condition (≥ 1 MISMATCH; agent must
  enumerate which): satisfied — all 7 primitives MISMATCH;
  enumeration is §D.2 above (D1 through D7).
- **INSUFFICIENT** condition (mixed UNDETERMINED with no MISMATCH):
  not satisfied (no UNDETERMINED).

Aggregate verdict: **STRUCTURAL_MISMATCH**.

## §D.4 — Discipline reassertion

The aggregate verdict above is a **structural-form check** at 075's
T2-mechanical scope. Per envelope §4.D.3:

> "NEVER assert 'structural match implies R1 closure'. ALWAYS
>  reassert 'structural match is necessary but not sufficient for
>  chart-map closure; closure discharge requires T1 synthesis
>  (076 if applicable), not 075 substrate inventory.'"

The dual reassertion holds for STRUCTURAL_MISMATCH: the present
verdict says (13 a)'s syntactic form is incompatible with the
chart-map-required structural form at every primitive. This is
**not** an assertion that R1 cannot be closed via any path; it is
**not** an assertion that the BT framework is irrelevant to R1; it
is **only** an assertion that (13 a) **as quoted** in 073 §5 does
not, at structural-form level, supply the algebraic parameter-chart
translation 069r1 §A.1.5 specifies.

R1 closure remains gated at W21 LANE-1 per 069r1
NO_GO_SUBSTRATE_INSUFFICIENT verdict; the 075 STRUCTURAL_MISMATCH
verdict feeds Phase E recommendation that path-δ literature
acquisition be considered downstream of OQ-W21-LITERATURE-
ALTERNATIVE resolution at W21 LANE-1.

End of `structural_match_matrix.md`.
