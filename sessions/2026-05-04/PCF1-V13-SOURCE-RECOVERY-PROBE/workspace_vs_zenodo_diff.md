# Workspace vs Zenodo — TeX-level structural diff (PCF-1)

## Source identity

| File                       | Path                                                                  | SHA-256          | Bytes  | Lines | Build pages |
|----------------------------|-----------------------------------------------------------------------|------------------|-------:|------:|------------:|
| Canonical 16pp v1.3 TeX    | `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex` | `e83bb377…74be301` | 46,349 |   837 | 16 |
| Workspace current TeX      | `tex/submitted/p12_journal_main.tex`                                  | `82173a09…a4786853` | 72,311 | 1,498 | 21 |

The workspace TeX is **untracked** in the workspace `.git` repo
(verified via `git ls-files --error-unmatch`); no workspace-side
git history exists for it.

The bridge `arxiv_pack_pcf1_v1.3/pack/p12_pcf1_main.tex` is
**byte-identical** to the workspace `p12_journal_main.tex`
(both SHA `82173a09…a4786853`). The bridge "snapshot" therefore
captured the post-edit 21pp working draft, not the canonical
16pp deposit source. The canonical 16pp source lives only at
`sessions/2026-05-01/PCF1-V13-UPDATE/`.

## Structural-count diff

| Item                          | Canonical 16pp | Workspace 21pp | Δ      |
|-------------------------------|---------------:|---------------:|-------:|
| `\section{...}`               |              8 |              9 |    +1  |
| `\subsection{...}`            |              1 |             35 |   +34  |
| `\begin{theorem}`             |              1 |              1 |     0  |
| `\begin{corollary}`           |              0 |              1 |    +1  |
| `\begin{conjecture}`          |              4 |              5 |    +1  |
| `\begin{equation}` + `\begin{align}` |        4 |             12 |    +8  |
| `\bibitem{...}`               |             14 |             23 |    +9  |
| approx. word count            |          5,641 |          8,168 | +2,527 |
| TeX bytes                     |         46,349 |         72,311 | +25,962 |
| TeX lines                     |            837 |          1,498 |   +661 |

## Section-list diff

The workspace draft has been refactored from an outline-grade
manuscript into a journal-grade manuscript.

**Canonical (8 §, 1 §§):** Introduction → Spec(K) Framework v5 →
Sharp Dichotomy → Structural Evidence → WKB Exponent Identity →
V_quad Prototype (1 §§: Channel scope) → AEAL Evidence Chain →
Open Questions.

**Workspace (9 §, 35 §§):** Introduction (5 §§: transcendence
predicate, empirical dichotomy & conjecture, headline contributions,
relation to prior work, organisation) → **Background** (6 §§: PCFs &
Wallis convergents, Spec(K) classification, imaginary quadratic
fields & CM, Heun & Painlevé, Stokes phenomenon) → Theorem for Δ>0 →
Sharp Dichotomy & Conjecture A v5 (3 §§) → **Stokes-Exponent
Diagnostic** (7 §§: definitions, CM-respecting deformations, six-
family verification, best Painlevé residual, connection-coefficient
proxy, intra-field replication, Conjecture A v5 (iii)/(iv)) →
V_quad Painlevé Prototype (4 §§: PIII(D6) parameters, channel
distinction, Stokes data, Δ=−11) → **Computational Methodology**
(5 §§: high-precision Wallis, 18-element PSLQ basis, Heun-root
computation, deformation-derivative stencils, reproducibility) →
Open Problems → **Numerical methodology — detailed (appendix)**
(6 §§: Wallis pseudocode, stability digits, F(2,4) Trans closed
forms, Painlevé ansatz forms, per-family residual & Stokes tables,
reproducibility URLs).

Bold-text sections are net-new additions in the v1.4 working draft;
the others are reorganisations of canonical-source content.

## Drift assessment

- 21pp / 16pp = 1.3125× (well within the operator-defined "deep-drift"
  threshold of >50%; HALT_PCF1_V13_DEEP_DRIFT does NOT trigger).
- Net additions are dominated by (a) a Background section, (b) a
  Computational Methodology section, and (c) a 6-subsection appendix
  — i.e., journal-style scaffolding around the canonical research
  content rather than mathematical novelty. Theorem count is
  unchanged (1 → 1); conjecture count grows by 1 (4 → 5).
- This is consistent with "v1.4 working draft = v1.3 + journal
  packaging + one new conjecture" rather than a substantive
  re-derivation.
