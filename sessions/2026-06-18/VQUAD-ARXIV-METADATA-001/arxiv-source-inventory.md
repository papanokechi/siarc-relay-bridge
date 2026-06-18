# arXiv source package inventory — VQUAD-ARXIV-METADATA-001 · Stage 1

Slot: `sessions/2026-06-18/VQUAD-ARXIV-METADATA-001/`
Source tree: `sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/` (committed `627d17e`)
Date: 2026-06-18 · HELD per standing meta-rule (prepare + verify only)

---

## 1.1 — What arXiv needs (and what it does NOT)

arXiv compiles **LaTeX source**, not the Zenodo PDF. Accepted source formats include
(La)TeX / AMS(La)TeX / PDFLaTeX (operator-supplied arXiv submission-help, v1.5). The upload
may be a **single `.tex` file** OR a single `.zip` / `.tar.gz` bundle.

### THE upload (minimal, recommended): one file

| Upload | File | Size | Role |
|---|---|---|---|
| ✅ **YES** | `vquad-periodrep-paper.tex` | 87,778 B | The flattened, self-contained manuscript source. Compiles standalone. |

Because the manuscript is a **single self-contained `.tex`**, the simplest correct upload is
that one file. Optionally it may be wrapped in a `.zip`/`.tar.gz` (arXiv v1.5 accepts either);
the bare `.tex` is preferred — fewer moving parts.

### Do NOT upload these (build inputs / artifacts / derivatives)

| File | Why excluded |
|---|---|
| `preamble.tex` | **Inlined already.** `build.py` concatenates it into `vquad-periodrep-paper.tex` (lines 1–74). It is NOT `\input` at compile time. It also carries its own `\documentclass`+`\begin{document}` with **no** `\end{document}` — uploading it alongside would give arXiv a second, incomplete `\documentclass` file and risk a wrong main-file pick. **Exclude.** |
| `build.py` | Local build driver (concatenate + pdflatex×2). Not a TeX source; not needed by arXiv. |
| `sections/*.md` | Body fragments that `build.py` concatenates into the `.tex`. Already inside the flattened file. Not present in `latex/` (they live in the slot's `sections/`). |
| `vquad-periodrep-paper.pdf` | **Derivative.** arXiv requires the SOURCE for (La)TeX submissions, not the PDF (arXiv submission-help: "must submit the source … not derivative dvi, Postscript, or PDF"). The Zenodo PDF `33f339ed…` is the deposit artifact, not the arXiv upload. |
| `*.aux` `*.log` `*.out` | pdflatex byproducts. Never uploaded. |

---

## 1.2 — Bibliography mechanism (CRITICAL)

**Mechanism: embedded `\begin{thebibliography}{99}` (line 1302).**

- `\bibitem{...}` entries are written inline in the `.tex`; the references print from the
  embedded list.
- **No external bibtex.** No `\bibliography{...}`, no `\bibliographystyle{...}` anywhere in the
  source (grep: 0 matches).
- ⇒ **No `.bbl` file is required.** arXiv will typeset the bibliography from the embedded
  `thebibliography` block on the normal latex passes — no bibtex pass, no `.bbl` upload.

This is the arXiv-ready case: a single `.tex` with an embedded bibliography compiles cleanly
without any auxiliary bibliography file.

### Figures / inputs
- `\includegraphics`: **none** (grep: 0). The only graphics are **TikZ**, compiled inline from
  the source (`\usepackage{tikz}` + `\usetikzlibrary{...}` in the inlined preamble). No external
  figure files to upload.
- `\input` / `\include`: **none** (grep: 0). The file is fully self-contained.

⇒ **Upload bundle = exactly one file: `vquad-periodrep-paper.tex`. Nothing else.**

---

## 1.3 — Source is the LAYOUT-FIXED version (not stale)

Verified on disk (2026-06-18):

| Check | Result |
|---|---|
| `vquad-periodrep-paper.pdf` SHA-256 | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` ✅ = layout-fixed pin |
| PDF size | 773,171 B ✅ |
| Page count (from `.log`: "Output written on … (24 pages, 773171 bytes)") | **24 pages** ✅ |
| LAYOUTFIX guards present in `.tex` | `\emergencystretch=3em` (L20) + breakable `\_` redefinition (L21–24) ✅ |
| `preamble.tex` ≡ `.tex` lines 1–74 | byte-identical (the flattened head) ✅ |

The on-disk PDF re-hashes to the exact layout-fixed pin `33f339ed…`, and the `.tex` carries the
LAYOUTFIX-001 guards, so the `.tex` to upload is the layout-fixed source — not a stale
pre-fix version. arXiv's own compile will differ (arXiv header/ID stamp) — **expected, not a
defect**; we only certify the SOURCE is layout-fixed.

> Build provenance: `build.py` sets `SOURCE_DATE_EPOCH=1718409600` and runs `pdflatex` ×2 for the
> byte-reproducible local PDF. arXiv ignores this (its compile is stamped) — fine.

---

## 1.4 — Public-source note (arXiv v1.5)

"TeX source uploaded to arXiv will be made publicly available." The uploaded `.tex` becomes
**public**. This is consistent with the already-public Zenodo bundle, and the source has been
scanned (Stage 3) for identity/venue leaks: **no "Kubota", no "Compositio"/venue strings** in the
`.tex` or inlined preamble. Public source is therefore safe. (The pre-announcement name-check in
the runbook is the final guard.)

---

## Summary

- **Upload:** `vquad-periodrep-paper.tex` (single self-contained file; optionally zipped). **Not** the PDF, **not** `preamble.tex`, **not** `build.py`.
- **Bibliography:** embedded `\thebibliography` ⇒ **no `.bbl`, no bibtex** needed.
- **Figures/inputs:** none external (TikZ inline; no `\includegraphics`/`\input`).
- **Source is layout-fixed:** PDF re-hashes to `33f339ed…`, 24 pp, guards present.
- **Public-source:** safe (no identity/venue leak — Stage 3).
