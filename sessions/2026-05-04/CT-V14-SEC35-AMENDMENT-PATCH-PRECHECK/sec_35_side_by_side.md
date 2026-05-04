# CT v1.4 §3.5 — side-by-side comparison

**Task:** CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK
**Source:** `siarc-relay-bridge/sessions/2026-05-03/CT-V14-NARRATIVE-DRAFT/ct_v1.4_main.tex`
**SHA-256:** `0600A4456803A43D967788196C501534716852652030FC4225E6B42921AE77E1`
**Lines:** 948–995 (subsection start through last line before next `\subsection`)
**Insertion point:** end of §3.5, before the `\subsection{Median Écalle resurgence …}` at line 996.

---

## Change-class summary

| Class      | Count | Notes                                                                |
|------------|-------|----------------------------------------------------------------------|
| Insertion  | 1     | New `\paragraph{Layer note (added v1.4).}` block (≈190 words)        |
| Replace    | 0     | No existing wording is altered.                                       |
| Delete     | 0     | No existing wording is removed.                                       |

The amendment is **purely additive** (matches the v1.4 framing
"Version 1.4 (2026-05-03) is purely additive: no v1.0 / v1.1 /
v1.2 / v1.3 theorem, proposition, or conjecture is rewritten",
ct_v1.4_main.tex:241).

---

## Side-by-side (current ↔ proposed)

| Current §3.5 (verbatim, lines 948–995)                                    | Proposed §3.5 (post-amendment)                                                |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `\subsection{The locked WKB exponent identity}`                           | (unchanged)                                                                  |
| `\label{ssec:wkb}`                                                        | (unchanged)                                                                  |
|                                                                           |                                                                              |
| `\begin{proposition}[WKB exponent identity, empirical;`                   | (unchanged)                                                                  |
| `\cite{siarc_pcf1_v13,siarc_borel_kscan,siarc_cc_pipeline_f}]`            | (unchanged)                                                                  |
| `\label{prop:wkb}`                                                        | (unchanged)                                                                  |
| `For each of the six $\Delta<0$ degree-$2$ families surveyed,`            | (unchanged)                                                                  |
| `the leading trans-series exponents of`                                   | (unchanged)                                                                  |
| `$\log\|\dn\| = -A n \log n + \alpha n - \beta \log n + \gamma`           | (unchanged)                                                                  |
| `+ \sum_{k \ge 1} h_k / n^k$`                                             | (unchanged)                                                                  |
| `satisfy the closed form …`                                               | (unchanged)                                                                  |
| `\end{proposition}`                                                       | (unchanged)                                                                  |
|                                                                           |                                                                              |
| `\Cref{prop:wkb} fixes the leading WKB exponent of`                       | (unchanged)                                                                  |
| `$\log\|\dn\|$ but \emph{not} the residual Laplace step that`             | (unchanged)                                                                  |
| `converts the Birkhoff-factored formal pair $f_\pm(u)$ of the`            | (unchanged)                                                                  |
| `$\CC$ channel into Stokes data; that step is formally`                   | (unchanged)                                                                  |
| `separate, and Theory-Fleet H4 …`                                         | (unchanged)                                                                  |
| `extracts the alien amplitude at $\zeta_*=4/\sqrt 3$ to $30$--$50$ digits.`| (unchanged)                                                                 |
|                                                                           |                                                                              |
| `The relevance of \Cref{prop:wkb} for v1.1 is the …`                      | (unchanged)                                                                  |
| `… resolved at $d=2,4$ via the linear formula`                            | (unchanged)                                                                  |
| `$\xi_0 = d / \beta_d^{1/d}$ (\Cref{conj:xi0-univ}).`                     | (unchanged)                                                                  |
|                                                                           | **`<<NEW v1.4>>`**                                                           |
|                                                                           | `\paragraph{Layer note (added v1.4).}`                                       |
|                                                                           | `The residual Laplace step invoked above is naturally`                       |
|                                                                           | `described in two formally distinct layers, in the sense of`                 |
|                                                                           | `the asymptotic / isomonodromic literature`                                  |
|                                                                           | `\cite{costin2008asymptotics,birkhofftrjitzinsky1932analytic,jimbomiwa1981monodromy}.` |
|                                                                           | `The \emph{L-equation layer} is the linear differential or`                  |
|                                                                           | `difference operator $L(y)=0$ whose formal-series solutions`                 |
|                                                                           | `$e^{Q(x)}\,s(x)$ are the OGF / wave-function objects of the`                |
|                                                                           | `underlying analytic problem; it is satisfied by --- not equal`              |
|                                                                           | `to --- the OGF in the $(z,w)$ function-space layer`                         |
|                                                                           | `(Birkhoff--Trjitzinsky 1933 for the difference setting;`                    |
|                                                                           | `Costin 2008 ch.~5 for the differential / Borel-summability`                 |
|                                                                           | `setting). The \emph{isomonodromic-deformation layer}`                       |
|                                                                           | `describes how the monodromy data (Stokes constants,`                        |
|                                                                           | `connection matrices) of $L$ deform as a parameter $t$ varies;`              |
|                                                                           | `it lives in the $(q,p,t)$ Hamiltonian / monodromy-data layer`               |
|                                                                           | `(Okamoto 1987 for the $P_{III}'$ / $P_{III}$ Hamiltonian`                   |
|                                                                           | `formulation; Jimbo--Miwa 1981 II for the Lax-pair`                          |
|                                                                           | `monodromy-preserving-deformation construction;`                             |
|                                                                           | `Barhoumi--Lisovyy--Miller--Prokhorov 2024 §4.1 for the`                     |
|                                                                           | `canonical textbook statement). The bridge between the two`                  |
|                                                                           | `layers is the over-determined Lax pair`                                     |
|                                                                           | `$(\Lambda(\lambda,x),\,X(\lambda,x))$ whose compatibility`                  |
|                                                                           | `condition $[\partial_x - X,\,\partial_\lambda - \Lambda] = 0$`              |
|                                                                           | `returns the deformation equation. In particular, the`                       |
|                                                                           | `$\Vquad$ recovery of \Cref{thm:vquad-cc} is read as an`                     |
|                                                                           | `identity at the level of monodromy data on the deformation`                 |
|                                                                           | `side, \emph{not} as an identification of the $\Vquad$ scalar`               |
|                                                                           | `ODE with the $(q,p,H_{III'}(t;q,p))$ Hamiltonian on the`                    |
|                                                                           | `function-space side.`                                                       |

---

## §3.5-vs-§3.3 numbering note (operator + Claude review)

The G17-LAYER-SEPARATION-LIT-ANCHOR Phase C.3 DRAFT mentions
"the map Φ in CT v1.3 §3.5". In CT v1.4 main.tex
(2026-05-03 in-flight), the relevant **CC-channel V_quad
recovery theorem** (`\thm:vquad-cc` containing the
`exact algebraic identity` wording) is in **§3.3** (line ~796–820,
inside `\subsection{The connection-coefficient channel $\CC$ …}`),
**not** in §3.5. The current §3.5 is "The locked WKB exponent
identity", which discusses the **residual Laplace step
$\to$ Stokes data**, i.e. the *bridge* between the two layers.

Two reading-of-§3.5 are possible:

* **Reading A (chosen for this patch):** insert the layer
  note at the end of §3.5 (locked WKB), where the residual
  Laplace step → Stokes data discussion already gestures
  at the layer separation. The cross-reference to
  `\Cref{thm:vquad-cc}` (in §3.3) keeps the V_quad
  recovery anchor.
* **Reading B (alternative):** the G17 handoff
  "CT v1.3 §3.5" referred to a **different** §3.5 in the
  *published* CT v1.3 PDF, which may have had different
  numbering. If operator + Claude prefer to match
  the v1.3-numbered location, the patch should be moved
  to the end of §3.3 (after `\Cref{thm:vquad-cc}` at line
  ~820) instead.

This precheck adopts **Reading A**; surfaces **Reading B**
as a deferred operator + Claude review decision before
manual `git apply`.
