# Phase B — V1 Chart-Map Extraction (arXiv:2307.11217 v2)

**Session:** 086 T2-R5-LIT-HUNT-TRIANGULATION
**Phase:** B (V1 chart-map structural extraction)
**V1 source:** Barhoumi, Lisovyy, Miller, Prokhorov, "Painlevé-III
  Monodromy Maps Under the $D_6 \to D_8$ Confluence and Applications
  to the Large-Parameter Asymptotics of Rational Solutions",
  arXiv:2307.11217 v2 (9 Mar 2024) = SIGMA 20 (2024) 019, 77 pages.
**V1 PDF SHA-256:** `96C49CDD51B6C2A395CCD6CC3CB66BFFEB623643B1A2374DB3F203760F696BB3`
**V1 PDF size:** 2 018 889 B (re-downloaded 2026-05-07 fire-time;
  matches arXiv abstract metadata).

This artefact extracts the chart-map structure that V1 explicitly
documents for Painlevé-III($D_6$). Substrate-inventory scope only;
no construction of a V_quad → P_III($D_6$) map is attempted in
Phase B (that is Phase E's task).

---

## §B.1 — V1 chart-map levels (verbatim-anchored)

V1 §1 + §4 carry the chart-map across **six levels** of
parametrisation. The verbatim anchors below are quoted from
`v1_full.txt` as extracted at fire-time; quote-length ceiling
50 words (envelope §B.B3 standard).

### Level 1 — Painlevé-III($D_6$) parameters $(\alpha, \beta)$

V1 §1 eq. (1.1) (paraphrase: V1 fixes $(\alpha, \beta) \in \mathbb{C}^2$
as the seed-solution parameters of Painlevé-III(D_6) in the form
$u_{xx} = u_x^2/u - u_x/x + (\alpha u^2 + \beta)/x + 4u^3 - 4/u$).

Verbatim (v1_full.txt L391-394; 32 words):

> "From this point of view, one can show that for fixed $\alpha,
>  \beta \in \mathbb{C}$, the solutions of (1.1) are parametrized
>  by triples $(x_1, x_2, x_3) \in \mathbb{C}^3$ on the cubic
>  surface, known as the monodromy manifold"

### Level 2 — Lax-pair exponents $(\Theta_0, \Theta_\infty)$

V1 §4.1 eq. (4.6) gives the explicit affine relation between the
P_III(D_6) parameters $(\alpha, \beta)$ and the formal-solution
exponents $(\Theta_0, \Theta_\infty)$ at the irregular singular
points of the Lax pair (4.1)+(4.3).

Verbatim (v1_full.txt L2647-2650; 14 words plus formula):

> "we arrive at (1.1) with parameters $\Theta_0 = \alpha/4,
>  \Theta_\infty = 1 - \beta/4$. (4.6)"

This is a **closed-form linear chart-translation** between two
parameter charts of the **same** Painlevé-III(D_6) equation.

### Level 3 — Exponential constants $(e_0, e_\infty)$

V1 §1 eq. (1.14) + §4 eq. (4.13) give the further chart map onto
the exponential constants:

Verbatim (v1_full.txt L407-409; 12 words plus formula):

> "$e_0 := e^{i\pi\alpha/8} \neq 0$ and $e_\infty := i e^{-i\pi
>  \beta/8} \neq 0$. (1.14)"

Verbatim (v1_full.txt L2725-2726; 7 words plus formula):

> "$e_0 = e^{i\pi\Theta_0/2}$, $e_\infty = e^{i\pi\Theta_\infty/2}$. (4.13)"

(Consistency check: substituting (4.6) into (4.13) recovers (1.14)
modulo the $i$ factor convention on $e_\infty$.)

### Level 4 — Stokes multipliers + connection matrices

V1 §4.1 eq. (4.10)-(4.11) defines four Stokes multipliers
$s_1^\infty, s_2^\infty, s_1^0, s_2^0 \in \mathbb{C}$ and two
connection matrices $C_{0\infty}^+, C_{0\infty}^-$ relating the six
canonical solutions across Stokes sectors (eq. 4.14-4.15).

Verbatim (v1_full.txt L2719-2723; 20 words plus formulae):

> "the canonical solutions in consecutive Stokes sectors are related
>  to one another by multiplication on the right with Stokes
>  matrices, i.e., $\Psi_2^{(\infty,0)} = \Psi_1^{(\infty,0)}
>  S_1^{\infty,0}$, $\Psi_3^{(\infty,0)} = \Psi_2^{(\infty,0)}
>  S_2^{\infty,0}$"

The Stokes multipliers + connection-matrix entries together form
the **monodromy data** of the Lax system (4.1)+(4.3).

### Level 5 — Two essential monodromy parameters $(e_1, e_2)$

V1 §1 + §4.3 carries the key reduction: the four Stokes multipliers
+ two connection matrices are determined from just **two** complex
parameters $(e_1, e_2)$.

Verbatim (v1_full.txt L415-417; 35 words):

> "we parametrize points $(x_1, x_2, x_3)$ on the cubic surface
>  (1.13) using parameters $e_1, e_2$ appearing naturally from the
>  point of view of the Riemann–Hilbert problem. In fact, $e_1^2,
>  e_1^{-2}$ are eigenvalues of a certain monodromy matrix"

Verbatim (v1_full.txt L416-417; 14 words):

> "The parameter $e_2$ appears in the connection matrix for the
>  same system, see (4.28). We call $(e_1, e_2)$ monodromy
>  parameters."

### Level 6 — Cubic-surface coordinates $(x_1, x_2, x_3)$

V1 §1 eq. (1.13) + §4.6 eq. (4.38) define the monodromy manifold
as the cubic surface

$$
x_1 x_2 x_3 + x_1^2 + x_2^2 + x_2 (e_0^{-2} - e_\infty^{-2})
   + x_1 (1 + e_0^{-2} e_\infty^{2}) + e_0^{-2} e_\infty^{2} = 0 \,.
$$

(transcription from v1_full.txt L3434-3435 / eq. (4.38).)

V1 §1 eq. (1.17)-(1.19) gives explicit formulae for $(x_1, x_2,
x_3)$ in terms of the monodromy parameters $(e_1, e_2)$ and the
exponential constants $(e_0, e_\infty)$ — i.e. an **explicit
closed-form rational map** $(\alpha, \beta, e_1, e_2) \to (x_1,
x_2, x_3)$.

## §B.2 — Source / target / assignment-rule decomposition

For 086 cross-walk purposes, V1's chart-map is decomposed below
along the same 7-primitive axis as the 075 GAP-PRIMITIVE-B1..B7
axis (per envelope §D.D2 instruction).

| Primitive            | V1-side specification                                                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V1-PRIMITIVE-V1      | Domain = complex 2-tuple $(\alpha, \beta)$ of Painlevé-III($D_6$) seed-solution parameters in form (1.1).                                                    |
| V1-PRIMITIVE-V2      | Codomain = complex 5-tuple $(e_1, e_2, x_1, x_2, x_3)$ on monodromy manifold (1.13); equivalently, 4 Stokes multipliers + 2 connection-matrix entries.       |
| V1-PRIMITIVE-V3      | Form = compositional. (4.6) is a closed-form polynomial (linear). (1.14)+(4.13) is exponential. §4.4-§4.6 gives a closed-form rational map onto cubic surface. |
| V1-PRIMITIVE-V4      | Cardinality = (2 maps in (4.6)) + (2 maps in (1.14)) + (4 Stokes multipliers + connection-matrix entries determined by (e_1, e_2)) + (3 explicit formulae (1.17)-(1.19) for $x_i$). |
| V1-PRIMITIVE-V5      | NOT sector-dependent for (4.6) + (4.13) + (1.14). IS sector-dependent at Level 4: Stokes matrices (4.11) attach to specific Stokes sectors $S_k^{(\infty, 0)}$. |
| V1-PRIMITIVE-V6      | Algebraic linear constraint (4.6); exponential constraint (1.14)+(4.13); cubic-surface constraint (1.13) on $(x_1, x_2, x_3)$.                                 |
| V1-PRIMITIVE-V7      | Type = composite chart-map: parameter-chart $(\alpha, \beta) \to (\Theta_0, \Theta_\infty)$ algebraic; then $(\Theta) \to$ monodromy data via Riemann–Hilbert. |

## §B.3 — Chart-map cardinality summary

V1's chart-map from $(\alpha, \beta)$ to monodromy data has the
following cardinality structure:

- 2 algebraic maps at Level 2: $(\alpha, \beta) \to (\Theta_0, \Theta_\infty)$
- 2 exponential maps at Level 3: $(\Theta_0, \Theta_\infty) \to (e_0, e_\infty)$
- 4 Stokes multipliers + 4 connection-matrix entries at Level 4 (8 total)
- 2 essential parameters $(e_1, e_2)$ that determine Level 4 (per §4.3-§4.4)
- 3 explicit formulae for $(x_1, x_2, x_3)$ at Level 6 (per (1.17)-(1.19))

The **two essential complex parameters** $(e_1, e_2)$ play the
role of an irreducible monodromy-chart parametrisation; everything
else in Levels 4-6 is determined by $(e_1, e_2)$ together with the
exponential constants $(e_0, e_\infty)$.

## §B.4 — What V1 does NOT name

V1 §4 (the chart-map section) does NOT explicitly invoke:

- Sakai-classification surface type $D_6^{(1)}$ (cited only by name
  in V1's title; no surface-type derivation in §4).
- Affine Weyl group $(A_1 \times A_1)^{(1)}$ symmetry (per
  Reviewer D's pre-W21-synth Symmetry Consistency Check question:
  V1 §4 does not invoke this symmetry explicitly in the chart-map
  derivation).
- KNY 2017 §8.5.17 $(a_0, a_1, a_2)$ chart with constraint
  $a_0 + a_1 = 1$ (V1 §4 uses Jimbo-Miwa convention only; the
  Sakai/KNY $(a_0, a_1, a_2)$ chart is not bridged in V1).
- Okamoto 1987 four-tuple $(\alpha_\infty, \alpha_0, \beta_\infty,
  \beta_0)$ null-sum convention (V1 uses $(\Theta_0, \Theta_\infty)$
  Jimbo-Miwa convention; the Okamoto Hamiltonian-chart relabelling
  is not explicit in V1 §4).

These four absences are recorded as substrate-content gaps that
remain at fire time; they are NOT Phase E blockers because V1's
chart-map at the JM-convention level is sufficient for monodromy-
data alignment without invoking Sakai/KNY/Okamoto Hamiltonian-chart
intermediate notation. Phase E (Phi_prov) will route around these
gaps via the 058R B.5 Sakai-Okamoto cross-walk substrate.

## §B.5 — Discipline reassertion

This Phase B output is a **structural extraction** of V1's
chart-map at substrate-inventory scope. It does **not** assert
that V1 fills residual R1; it does **not** assert V1's chart
equals or differs from any specific SIARC B-candidate (that is
Phase D's task); it does **not** propose a V_quad → P_III map
(that is Phase E's task).

End of `v1_chart_map_extraction.md`.
