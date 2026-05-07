# Phase E — Provisional Normalization Map $\Phi_{\rm prov}$

**Session:** 086 T2-R5-LIT-HUNT-TRIANGULATION
**Phase:** E (citation-derived provisional normalization map)
**Inputs:** V1 (arXiv:2307.11217), V2 (arXiv:1604.03082), C1
  (Jimbo-Miwa-Ueno 1981 canonical), 058R substrate (V_quad → KNY
  chart), 069r1 (R1 anomaly substrate).
**Output:** $\Phi_{\rm prov}: V_{\rm quad} \to P_{III}(D_6)$ at
  monodromy-data level, plus enumeration of what $\Phi_{\rm prov}$
  does NOT determine (R5 audit-anchor residual).

Substrate-inventory scope. No closure of residual R1; no new
theorem; no Stokes-constant numerical evaluation.

---

## §E.1 — Construction

$\Phi_{\rm prov}$ is constructed as a **6-stage composition** that
carries the V_quad OGF representation onto a monodromy-manifold
point on the cubic surface (1.13) of P_III($D_6$). Each stage
cites a specific substrate / V1 / V2 / C1 ingredient.

Stage 0 (pre-stage; 058R substrate; UNCHANGED):

$$
\Phi_0:\ V_{\rm quad}\ \text{OGF}\ f(z) \quad \to \quad \text{V_quad
  CT v1.3 §3.5 four-tuple}\ (\alpha_\infty, \alpha_0, \beta_\infty,
  \beta_0) = (1/6, 0, 0, -1/2)
$$
- Cite: 058R `phase_b_canonical_map.md` SHA `F831F9BD58D1F306..91FF8BB3` §B.2.
- Anomaly D2 (058R inherited): null-sum $-1/3 \neq 0$ at V_quad
  parameter point. **Carry forward unchanged**.

Stage 1 (058R B.2 + B.3; UNCHANGED):

$$
\Phi_{\rm resc} \circ \Phi_{\rm shift}:\ V_{\rm quad}\ \text{chart}
\quad \to \quad \text{KNY 2017 §8.5.17}\ (a_0, a_1, a_2)\ \text{chart}
$$
with $\lambda = c_0^2/4 = 1/3$ (rescaling), $t_0 = -4\sqrt{3}$
(affine shift; sign-orientation degree of freedom), and KNY chart
parameters $(a_0, a_1, a_2)$ subject to $a_0 + a_1 = 1$.
- Cite: 058R `phase_b_canonical_map.md` §B.2-§B.3.
- Per 058R B.5: surface type $D_6^{(1)}$ + symmetry type $(A_1
  \times A_1)^{(1)}$ Sakai classification.

Stage 2 (058R B.5 cross-walk + Φ_symp structurally constructible):

$$
\Phi_{\rm symp}:\ \text{KNY}\ (a_0, a_1, a_2)\ \text{chart}
\quad \to \quad \text{Jimbo-Miwa}\ (\Theta_0, \Theta_\infty)\
   \text{Lax-pair convention}
$$
- Substrate path: 058R B.5 surface-type identification +
  Hamiltonian-form alignment between Okamoto $H_{III}$ (058R B.1
  citing Okamoto 1987 §1.1, FE 30) and KNY §8.5.17 $H_{D_6}^{\rm KNY}$.
- The (3-dim KNY chart with $a_0 + a_1 = 1$ constraint, effectively
  2-dim) ↔ (2-dim Jimbo-Miwa chart $(\Theta_0, \Theta_\infty)$)
  identification is structurally constructible at substrate-inventory
  scope; the explicit map between conventions remains an open
  computational task (058R B.3 sub-task (i): explicit conversion of
  V_quad's CT v1.3 §3.5 4-tuple to KNY $(a_0, a_1, a_2)$).
- **R5 audit-anchor residual at this stage**: the explicit Sakai-
  Okamoto convention dictionary for the Hamiltonian-form leading-
  coefficient is canonically attributed to Okamoto 1987; cited via
  058R B.1 verbatim transcription but not yet fully cross-walked.

Stage 3 (V1 §4.1 eq. 4.6; CLOSED-FORM ALGEBRAIC):

$$
\Phi_{\rm JM}:\ (\Theta_0, \Theta_\infty) \quad \to \quad
   (\alpha, \beta)
$$
explicitly via V1 (4.6): $\Theta_0 = \alpha/4$,
$\Theta_\infty = 1 - \beta/4$, equivalently
$\alpha = 4\Theta_0$, $\beta = 4(1 - \Theta_\infty)$.
- Cite: V1 §4.1 eq. (4.6) verbatim (`v1_chart_map_extraction.md`
  §B.1 Level 2).
- $\Phi_{\rm JM}$ is bijective with explicit inverse.

Stage 4 (V1 §1 (1.14) + §4 (4.13); CLOSED-FORM EXPONENTIAL):

$$
\Phi_{\rm exp}:\ (\alpha, \beta) \quad \to \quad (e_0, e_\infty)
$$
explicitly via V1 (1.14): $e_0 = e^{i\pi\alpha/8}$, $e_\infty =
i e^{-i\pi\beta/8}$.
- Cite: V1 §1 (1.14) + §4 (4.13).
- $\Phi_{\rm exp}$ is bijective on a fundamental domain modulo
  the discrete shift symmetries enumerated in V1 §1 just after
  (1.16).

Stage 5 (V1 §4.3 + §4.4 + §4.6; RH-DERIVED CHART):

$$
\Phi_{\rm RH}:\ (e_0, e_\infty;\ e_1, e_2) \quad \to \quad
   (s_1^\infty, s_2^\infty, s_1^0, s_2^0;\ C_{0\infty}^+,
    C_{0\infty}^-;\ x_1, x_2, x_3)
$$
- Cite: V1 §4.3-§4.6 + cubic surface (1.13) / (4.38).
- The 2 essential monodromy parameters $(e_1, e_2)$ + exponential
  constants $(e_0, e_\infty)$ together determine all Stokes
  multipliers, both connection matrices, and the cubic-surface
  point. Explicit closed-form rational-map formulae for $(x_1, x_2,
  x_3)$ given in V1 (1.17)-(1.19).

Stage 6 (V2 §1.3 + §4 emulation; STRUCTURALLY APPLICABLE):

$$
\Phi_{\rm tau}:\ \text{(P_III(D_6) RH problem 4.1 monodromy data)}
\quad \to \quad \text{(extended tau function }\tau_{\rm ext}
   \text{ + asymptotic constant factors)}
$$
- Cite: V2 §1.3 eq. (1.10)-(1.11) + §4.1 Theorem 4.2.
- V2 does NOT directly compute the P_III($D_6$) connection
  constants; V2's machinery is structurally applicable to V1's
  Lax pair via the Malgrange-Bertola extension principle. Explicit
  computation = open Phase D.2 numerical task per 058R substrate.

## §E.2 — Composition

$$
\boxed{\;\Phi_{\rm prov} \;:=\;
   \Phi_{\rm tau} \,\circ\, \Phi_{\rm RH} \,\circ\,
   \Phi_{\rm exp} \,\circ\, \Phi_{\rm JM} \,\circ\,
   \Phi_{\rm symp} \,\circ\, \Phi_{\rm shift} \,\circ\,
   \Phi_{\rm resc}\,.\;}
$$

Effective domain: V_quad OGF data at $z = 0$.
Effective codomain: P_III($D_6$) monodromy-data chart at
  $\lambda = 0, \infty$ irregular singular points + extended tau-
  function asymptotic constant factors.

## §E.3 — Citation chain (AEAL-traceable)

| Stage         | Substrate / source                                    | SHA-256 (16-char prefix)                             |
|---------------|-------------------------------------------------------|------------------------------------------------------|
| Stage 0       | 058R `phase_b_canonical_map.md` §B.2 (V_quad CT v1.3 four-tuple)       | `F831F9BD58D1F306`                                   |
| Stage 1       | 058R `phase_b_canonical_map.md` §B.3 (Φ_resc + Φ_shift pinned)        | `F831F9BD58D1F306`                                   |
| Stage 2       | 058R `phase_b5_affine_weyl_crosswalk.md` (Sakai-Okamoto cross-walk)   | `B9D4FFD2F279A33C`                                   |
| Stage 3       | V1 §4.1 eq. (4.6) — `v1_arxiv_2307_11217.pdf`         | `96C49CDD51B6C2A3`                                   |
| Stage 4       | V1 §1 eq. (1.14) + §4 (4.13)                          | `96C49CDD51B6C2A3`                                   |
| Stage 5       | V1 §4.3-§4.6 + cubic surface (1.13) / (4.38)          | `96C49CDD51B6C2A3`                                   |
| Stage 6       | V2 §1.3 eq. (1.10)-(1.11) + §4.1 Theorem 4.2          | `B63A1E2EC2E6E7A6`                                   |
| Anchor canon  | C1 = JMU 1981 Physica D 2 + 4 series; V2 §1.2 + Prop. 2.3 transcribes $\omega_{JMU}$ verbatim | (canonical reference; not a SIARC-internal artefact) |
| Substrate gate | 086 `citation_pre_verification_2026-05-07.md`         | `1584C61EF68B984A`                                   |

The complete citation chain is sub-graph of the bridge HEAD `14e6b09`
+ 058R LANDED at `f8099b4` (058R `prompt_spec_used.md`) +
  069r1 LANDED at session `2026-05-07/M6-CC-R1-CLOSURE-PREFLIGHT-069R1`.

## §E.4 — What $\Phi_{\rm prov}$ DOES determine

At substrate-inventory scope, $\Phi_{\rm prov}$ provides:

1. A bijective composition $V_{\rm quad}$ chart $\to$ KNY $(a_0,
   a_1, a_2)$ chart $\to$ Jimbo-Miwa $(\Theta_0, \Theta_\infty)$
   chart $\to$ P_III($D_6$) parameters $(\alpha, \beta)$ at the
   parameter-space level.
2. An explicit closed-form rational map onto the cubic-surface
   monodromy manifold (1.13) / (4.38) parametrised by 2 essential
   monodromy parameters $(e_1, e_2)$.
3. A structurally applicable methodology (V2 §4.1 Theorem 4.2 +
   V2 §1.3 closed-form $\hat\omega$ + Malgrange-Bertola extension)
   for evaluating asymptotic constant factors of the P_III($D_6$)
   tau function at the V_quad parameter point.
4. An explicit Lax pair (V1 (4.1)+(4.2)+(4.3)) at the V_quad
   parameter point, sufficient to instantiate V2's $\omega$ and
   $\hat\omega$ for explicit numerical computation.

## §E.5 — What $\Phi_{\rm prov}$ does NOT determine ("R5 audit-anchor residual")

These are the items that remain in the R5 (Okamoto 1987) physical-
access dossier as **final-pass audit anchors**, not as M6.CC
critical-path blockers:

1. **Okamoto Hamiltonian-chart numerical normalisation**: the
   precise relation between Okamoto 1987's $(\eta_\infty, \eta_0,
   \theta_\infty, \theta_0)$ four-tuple (with hygiene-permitted
   convention $\eta_0 = \eta_\infty = 1$) and the Sakai-classification
   $(a_0, a_1, a_2)$ KNY chart at the $D_6^{(1)}$ surface type level.
   058R B.1 transcribes the Hamiltonian $H_{III}$ verbatim;
   058R B.5 identifies surface type. The full algebraic dictionary
   between conventions remains an audit anchor.
2. **V_quad CT v1.3 §3.5 four-tuple null-sum anomaly**: the
   sum $\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = -1/3
   \neq 0$ at V_quad parameter point. Carried forward as 058R
   anomaly D2 / 069 anomaly D4. R5 (Okamoto 1987) audit would
   confirm whether this is a genuine null-sum violation or a
   convention-rename artefact.
3. **Reviewer D Symmetry Consistency Check ($D_6$ Weyl group
   structure on V_quad Lax pair)**: V1 §4 does not explicitly
   invoke this symmetry. R5 + KNY 2017 §8.5 + Sakai 2001 surface
   type literature would address it.
4. **Φ_symp Jacobian determinant at V_quad parameter point**: the
   numerical residual identified in 058R B.3 sub-tasks (i)-(iii).
   Computable from V1 (4.1)+(4.2) + V2 §4.1 machinery; the
   numerical value of $|\det J(\Phi_{\rm symp})|$ acting on Stokes
   data remains the open Phase D.2 numerical task.
5. **Schlesinger transformation explicit formulae** (V1 §6 +
   Gromak Bäcklund (1.2) reproduces these for V1's seed-solution
   $u_0$ to $u_n$ family). For V_quad's specific parameter point
   the Schlesinger formula application is a specialisation; not
   yet computed at 086 scope.

R5 (Okamoto 1987) physical access remains a **valuable**
substrate item for cross-checking items (1)-(4); however, it
is **not blocking** for M6.CC pre-fire under the $\Phi_{\rm prov}$
B4-routing (per Phase F).

## §E.6 — Discipline reassertion

$\Phi_{\rm prov}$ is **provisional** in three concrete senses:

- **Phase D.2 numerical residual deferred** (Φ_symp Jacobian +
  $(e_1, e_2)$ values at V_quad parameter point): open
  computational task, not addressed at 086 scope.
- **R5 (Okamoto 1987) audit anchor outstanding**: R5 cross-check
  not performed; carried as Phase F R5_RESIDUAL_ONLY caveat.
- **Reviewer D Symmetry Consistency Check open**: the $D_6$ Weyl
  group structure on V_quad Lax pair remains a W21 LANE-1
  question.

$\Phi_{\rm prov}$ is **citation-derived**: every stage is anchored
to a specific verbatim substrate / V1 / V2 quote with SHA-256
provenance. No new theorem is asserted; no R1 is closed; no Stokes-
constant numerical match is claimed.

End of `provisional_normalization_map.md`.
