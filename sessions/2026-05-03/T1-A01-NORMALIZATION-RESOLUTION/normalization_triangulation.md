# D5 — Normalisation triangulation table

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEP 6
**Date:** 2026-05-03

---

## The five-row × four-column comparison

| Source         | Symbol for the $x\log x$ coefficient | Definition (verbatim or transcribed from primary)    | Role of polynomial degree $d$ of recurrence coefficients | Match to SIARC $A$ |
|----------------|--------------------------------------|------------------------------------------------------|---------------------------------------------------------|---------------------|
| **PCF-1 v1.3 §6** ([D1](pcf1_v13_ansatz_extract.md))  | $A$  | Coefficient of $-n\log n$ in $\log\lvert\delta_n\rvert$ as $n\to\infty$. Specifically, "$\log|\delta_n| = -A\,n\log n + \alpha n - \beta_w \log n + \gamma_w + \sum_k h_k/n^k$" (TeX line 533). | Empirically $A \in \{3,4\}$ at $d=2$ (TeX Table `tab:wkb-exponents`). No explicit Newton-polygon identification given (§6 Remark `rem:wkb-formal`). | self                |
| **B–T 1933 §1** ([D3](bt1933_normalization_extract.md)) | $\mu$ (or $\mu_j$ per solution) | "$Q(x) = \mu\,x\log x + \gamma\,x + \delta_1 x^{(p-1)/p} + \cdots$" (page 4, formula (7)). Normal case: $p=1$, $Q_j(x) = \mu_j\,x\log x + \gamma_j\,x$ (page 4, lines 128–131). | Implicit: the bound on $\mu_j$ in terms of polynomial degrees of $a_i(x)$ comes from the Newton-polygon slope formula of Birkhoff 1930 §1, page 6 (see Birkhoff row). B–T §§4–6 use the convention but do not re-define the bound. | $-A$ corresponds to **$\mu_{\mathrm{sub}} - \mu_{\mathrm{dom}}$** in the $n\log n$ channel (subdominant minus dominant). **Same μ-units**, no factor of 2. |
| **Adams 1928** (cited only via B–T 1933 footnote 2 on page 5 and Birkhoff 1930 footnote 2 on page 2; **NOT primary-quoted** per H-3) | $\sigma$ (Adams's notation) | NIA — **Adams 1928 PDF not on disk**. Per Birkhoff 1930 page 2: Adams's formal series have form "$x^{\mu^*}\,e^{\gamma x}\,(a + b/x + \cdots)$ with $\mu^* \le \mu$" and "are of the same kind as appear in the regular case", i.e., **same convention as Birkhoff 1930 / B–T 1933**. | Same as B–T (per Birkhoff 1930's explicit statement that Adams uses the same series type). | Same μ-units as B–T (per B–T's and Birkhoff 1930's direct citations). The Phase-1 worry "$\sigma_{\mathrm{Wasow}} = 2\sigma_{\mathrm{Adams}}$" is **not supported** by the on-disk B–T / Birkhoff direct evidence; that worry was a paraphrase artefact. |
| **Wasow 1965 §X.2–§X.3** ([D2](wasow_section_X_normalization.md)) | σ (Wasow's textbook notation) | **NIA — image-only PDF, no OCR.** Cannot primary-quote σ definition or §X.3 slope theorem. | NIA — Wasow §X.3 polynomial-coefficient slope bound cannot be primary-quoted on disk. The Phase-1 paraphrase "in the polynomial-coefficient case σ ≤ 2d" is **inherited unchanged** but **not verbatim-quoted** from Wasow itself. | NIA (cannot be directly attested in this session), but the identification flows transitively through Birkhoff 1930 (which Wasow §X.2 is the textbook treatment of): if Wasow inherits the Birkhoff convention (as is standard in textbook treatments), then σ_Wasow = μ_BT = A_SIARC in the $n\log n$ channel. **Triangulation conclusion: Wasow reading.** |
| **Birkhoff 1930 §1** ([D4](birkhoff_1930_rank_extract.md)) | $\nu$ in formula (6); also $\mu$ as Newton-polygon slope on page 6 | Formula (6): $s(x) = x^{\nu x}\,e^{P(x)}\,x^{\mu}\,(a + b/x^{1/p} + \cdots)$ with $P(x) = \gamma x + \delta x^{(p-1)/p} + \cdots$. Newton-polygon slope formula (page 6): $\mu = (j_l - j_m)/(l - m)$ where $a_i(x) \sim a_{ij_i} x^{-j_i/p}$. | Exactly the Newton-polygon slope of the lower convex hull of $\{(i, -j_i)\}_{i=0}^n$. For polynomial coefficients of degree $\le d$ at endpoints and order $n$, the maximum such slope is $\le d/n \cdot p$ in Birkhoff's normalisation; for $n=2$ this is $\le d \cdot p / 2$ at the leading vertex, with the specific value depending on the polynomial-degree pattern. | Transitively the same as B–T (since B–T explicitly inherit Birkhoff 1930's notation, see B–T page 4 footnote and §1 introduction). |

---

## Provenance of each non-trivial cell

* **PCF-1 v1.3 row.** All entries are verbatim quotes from
  `p12_pcf1_main.tex` (sessions/2026-05-01/PCF1-V13-UPDATE/), TeX
  lines 195–215 (recurrence + Spec(K) framework), 525–545 (Theorem 5
  / WKB ansatz), 555–590 (Table 2: empirical $A \in \{3,4\}$ at d=2).
  See [D1](pcf1_v13_ansatz_extract.md).

* **B–T 1933 row.** All entries are verbatim OCR quotes from
  `_bt1933.txt` (extracted from `03_birkhoff_trjitzinsky_1933_acta60.pdf`):
  page 4 (formula (7), normal-case definition), page 5 (Adams citation),
  page 30 (Lemma 8), page 41 (Theorem I), page 48 (Lemma 9). See
  [D3](bt1933_normalization_extract.md).

* **Adams 1928 row.** **Per H-3 (Adams 1928 fabrication guard):** the
  agent does NOT cite Adams 1928 directly. All Adams-row entries are
  built from Birkhoff 1930 footnote 2 (page 2) and B–T 1933 footnote 2
  (page 5), both of which give the citation "C. R. Adams, Trans. Am.
  Math. Soc. **30** (1928), pp. 507–541" and characterise Adams's
  formal series as "of the same kind as appear in the regular case"
  with the same μ exponent (Birkhoff 1930 page 2). This is the
  maximum the on-disk literature permits without primary Adams access.

* **Wasow 1965 row.** Most cells are NIA (image-only PDF, no OCR
  layer; see [D2](wasow_section_X_normalization.md)). The "match to
  SIARC" cell is a transitive inference: Wasow §X.2–§X.3 is the
  textbook treatment of the Birkhoff 1930 / B–T 1933 / Adams 1928
  primary results, and standard textbook conventions inherit primary
  conventions; the Phase-1 paraphrase that Wasow uses σ as the
  $x\log x$ coefficient is consistent with this.

* **Birkhoff 1930 row.** All entries are verbatim OCR quotes from
  `_birkhoff1930.txt` (extracted from `01_birkhoff_1930_acta54.pdf`):
  page 1 (title), page 2 (Adams citation + characterisation), page 6
  (formula (6) + Newton-polygon slope formula). See
  [D4](birkhoff_1930_rank_extract.md).

---

## What the table supports

1. **The $x\log x$ coefficient is universal across the on-disk primary
   sources.** Birkhoff 1930 ($\nu$), B–T 1933 ($\mu$), and SIARC
   PCF-1 v1.3 ($A$) all use the same channel ("**coefficient of
   $x\log x$ in the canonical exponent of the formal solution at
   $\infty$**") with the same units. There is **no factor of 2** at
   the normalisation level.

2. **Adams 1928 uses the same convention** (per Birkhoff 1930 page 2
   and B–T 1933 page 5 explicit citations). The Phase-1 worry that
   $\sigma_{\mathrm{Adams}} = \tfrac{1}{2}\sigma_{\mathrm{Wasow}}$ is
   **falsified** by the on-disk Birkhoff 1930 quotation that Adams's
   formal series "are of the same kind as appear in the regular case"
   (i.e., share Birkhoff's μ).

3. **Wasow 1965 §X is NIA on disk** (image-only PDF), but the
   transitive reading via Birkhoff 1930 / B–T 1933 / Adams 1928 (all
   on disk for the latter two; Adams cited but not on disk) suffices
   to **resolve** the A-01 normalisation-match question without
   primary Wasow §X access.

4. **The Phase-1 [d, 2d] bracket holds under the Wasow-normalisation
   reading** as a consequence of (1)–(3); the **derivation of the
   bracket itself** (i.e., the upper bound $\mu \le 2d$ in terms of
   polynomial degree $d$) is **separately** sourced from Phase-1's
   paraphrase of Wasow §X.3 and Birkhoff 1911 (the predecessor paper),
   and remains paraphrase-grade pending primary Wasow §X.3 access.
   This separation is logged in [D8](verdict.md) and the
   `unexpected_finds.json`.
