# arXiv metadata field package — VQUAD-ARXIV-METADATA-001 · Stage 2

Slot: `sessions/2026-06-18/VQUAD-ARXIV-METADATA-001/`
Purpose: every arXiv web-form field, ready to transcribe, source-cited to the layout-fixed `.tex`
and/or live Zenodo record 20719043. HELD — prepare + verify only.

Source legend:
- **TEX** = `sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.tex`
- **ZEN** = live Zenodo record `https://zenodo.org/api/records/20719043` (fetched 2026-06-18)
- **DEP** = `sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/MANUAL-UPLOAD.md`

---

## Field 1 — Title

```
An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient
```

- Source: **TEX** L51–52 `\title[...]{An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient}`.
- Cross-check **ZEN** `metadata.title` = "An explicit exponential-period representation of the V_quad connection coefficient" → **MATCH** (arXiv renders `$V_{\mathrm{quad}}$` as V_quad; Zenodo plain-text flattens it).
- Note: sentence case ("explicit", lowercase) — matches both TEX and ZEN. The Title-Case form seen in some ledger prose ("An Explicit … Coefficient") is a display artifact; **do not** use it. arXiv title field accepts inline `$...$` math, so keep `$V_{\mathrm{quad}}$`.

---

## Field 2 — Authors

```
Papanokechi
```

- Source: **TEX** L53 `\author{Papanokechi}`. Single author.
- ORCID `0009-0000-6192-8273` (**TEX** L54 `\thanks{ORCID ...}`; **ZEN** `creators[0].orcid`) — attached at the arXiv **account/claim** step (the ORCID link in the user profile), **not** typed into the author-name field.
- **No Kubota** anywhere in source (Stage 3 PASS). Author must read **Papanokechi** only.

---

## Field 3 — Abstract (CLEAN, arXiv-ready)

arXiv abstract = plain text with limited inline TeX. The custom preamble macros are **expanded**
to standard TeX below (arXiv does not load the paper preamble for the abstract field). This is the
clean **TEX** `\begin{abstract}` text (L59–72) — **not** the Zenodo entity-encoded HTML (Trap 3),
and **without** the 3 Zenodo deposit-context sentences (see note).

```
We prove that the connection coefficient $C$ of the $V_{\mathrm{quad}}$ polynomial continued fraction---the rank-one standalone closure on the Sakai surface $D_5^{(1)}$ (Painlev\'e~V)---admits an explicit exponential-period representation $C=(\lvert\Gamma(\beta)\rvert/2\pi)\int_\gamma e^{\xi}\widehat{B}(\xi)\,d\xi=\lvert\Gamma(\beta)\rvert K$, where $\widehat{B}$ is the Borel transform of the $V_{\mathrm{quad}}$ asymptotic series, holonomic of order $4$ (the Borel--Laplace dual of the order-$2$ operator annihilating the series) with coefficients in the real quadratic field $\mathbb{Q}(\sqrt3)$; $\gamma$ is an explicit Hankel rapid-decay cycle on $(-\infty,-2/\sqrt3]$; and $\beta=-1/(3\sqrt3)$. The identity is verified by three structurally independent methods---differential-equation/operator duality, Borel--Laplace contour deformation, and Stokes-data---agreeing to $46$ digits. The order-$2$ operator annihilating the asymptotic series has differential Galois group $\mathrm{SL}_2(\mathbb{C})$ by Kovacic's algorithm. As a by-product, holonomicity of the Borel transform forces a finite resurgent structure. Finally, conditional on the Fres\'an--Jossen period conjecture for exponential motives and on a stated motivic-comparison hypothesis, $C$ is transcendental over $\overline{\mathbb{Q}}$.
```

Macro expansions applied (preamble L38–49 → standard TeX): `\Vquad`→`V_{\mathrm{quad}}`,
`\Bhat`→`\widehat{B}`, `\Qsqrt`→`\mathbb{Q}(\sqrt3)`, `\Qbar`→`\overline{\mathbb{Q}}`,
`\SL`→`\mathrm{SL}`. `\K` (DeclareMathOperator) → `K`.

- Cross-check **ZEN** `metadata.description`: the scientific abstract is the **same statement**,
  modulo Trap-3 entity encoding (`&mdash;`, `&sup1;`, `&Gamma;`, `&radic;`, …) which are Zenodo HTML
  render artifacts — **MATCH**.
- **Deliberate difference:** ZEN appends 3 deposit-context sentences ("This record accompanies the
  VQUAD-PERIODREP reproducibility bundle…"; "The work was produced under the SIARC governance
  methodology…"; "The identity continues the V_quad companion paper (concept DOI …20455089)…").
  These describe the **deposit**, not the paper, and **must NOT** be in the arXiv abstract. The
  arXiv abstract is the paper's own abstract (the block above). ✔ intentional.

---

## Field 4 — Categories

| Field | Value | Source / note |
|---|---|---|
| **Primary** | `math-ph` (Mathematical Physics) | Marchal endorsement GRANTED for math-ph. |
| Cross-list (post-submission) | `math.NT` (Number Theory), `math.CA` (Classical Analysis and ODEs) | Add AFTER the initial submission/announcement; each cross-list **may require separate endorsement**. Not part of the first submit. |

---

## Field 5 — License (FLAG)

```
CC BY 4.0   (Creative Commons Attribution 4.0 International)
```

- Source: **ZEN** `metadata.license.id = cc-by-4.0`; operator decision = CC BY 4.0.
- ⚠ **MUST be actively selected** at the arXiv license step. arXiv's **default** is the
  *arXiv.org non-exclusive license to distribute* — **NOT** CC BY. Picking CC BY 4.0 keeps the
  arXiv preprint license consistent with the Zenodo deposit. Do not accept the default.

---

## Field 6 — Comments

```
24 pages
```

- Page count source: **TEX** `.log` "Output written on … (24 pages…)" + **ZEN**/DEP (24 pp). ✔
- **DECISION FLAG (operator):** optionally append the Zenodo concept DOI for cross-reference, e.g.
  `24 pages. Zenodo: https://doi.org/10.5281/zenodo.20719042`. Linking the preprint to the deposit
  is generally good practice; operator's call. (Use the **concept** DOI `…20719042` — cite-all —
  not the version DOI.)
- ⚠ **Do NOT** put any venue string (no "Compositio", no "submitted to …") in Comments — same
  wrong-venue gate as the deposit (Stage 3).

---

## Field 7 — MSC class (optional)

```
34M55, 11J81, 34E20, 14F40, 33C20, 37K10     (primary 34M55)
```

- Source: **DEP** L66 (Zenodo deposit assigned these; marked "optional"). The **paper source has no
  `\subjclass`** (TEX grep: 0), so MSC is **not** carried in the manuscript.
- **DECISION FLAG (operator):** arXiv's MSC-class field is optional. You may transcribe the
  deposit's codes (34M55 primary; 11J81, 34E20, 14F40, 33C20, 37K10) for consistency with Zenodo,
  or leave blank. No correctness impact either way.

---

## Field 8 — ACM class / Report-no / Journal-ref / DOI

| Field | Value |
|---|---|
| ACM class | (none) |
| Report-no | (none) |
| Journal-ref | (leave blank — no published venue; do **not** name any target venue) |
| DOI | **leave blank at submission** — arXiv assigns its own. The Zenodo DOI may be added later via the arXiv journal-ref/DOI facility, or surfaced in Comments (Field 6 flag). |

---

## Field 9 — Keywords

arXiv has **no free-keyword field** (classification is via Categories + optional MSC/ACM). The 8
Zenodo keywords (**DEP** L51) therefore do **not** transfer to arXiv. No action.

---

## Quick-transcribe summary

| arXiv field | Value |
|---|---|
| Title | `An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient` |
| Authors | `Papanokechi` (+ ORCID `0009-0000-6192-8273` via account claim) |
| Abstract | the clean block in Field 3 (macros expanded; no Zenodo deposit-context sentences) |
| Primary category | `math-ph` |
| Cross-list (later) | `math.NT`, `math.CA` |
| License | **CC BY 4.0** (actively select; not the arXiv default) |
| Comments | `24 pages` (+ optional `Zenodo: https://doi.org/10.5281/zenodo.20719042`) |
| MSC class | optional: `34M55, 11J81, 34E20, 14F40, 33C20, 37K10` |
| DOI / journal-ref / report-no | blank |

## Decision flags surfaced (operator decides; not decided here)
1. **Zenodo DOI in Comments?** — optional cross-reference; use concept DOI `…20719042` if yes.
2. **MSC class transcribed?** — optional; source has none, deposit has the 6 codes.
3. **Cross-lists** `math.NT` / `math.CA` — after first announcement; may need separate endorsement.
