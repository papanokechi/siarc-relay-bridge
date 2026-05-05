Title: Channel theory for polynomial continued fractions: asymptotic channels, the xi_0 = 2/sqrt(beta_2) identity, and a bridge conjecture
Short name: ct_v1.3
Zenodo version DOI: 10.5281/zenodo.19972394
Zenodo concept DOI: 10.5281/zenodo.19941678
License: CC BY 4.0 (matches Zenodo upload)
Expected page count: 17

Compile recipe (pdfTeX, MiKTeX or TeX Live):
  pdflatex -interaction=nonstopmode channel_theory_outline.tex
  bibtex channel_theory_outline    # only needed for bibtex (external .bib)
  pdflatex -interaction=nonstopmode channel_theory_outline.tex
  pdflatex -interaction=nonstopmode channel_theory_outline.tex

LaTeX packages required (from preamble):
  geometry, amsmath, amssymb, amsthm, mathrsfs, enumitem, xcolor, booktabs, hyperref, cleveref

No external figure files; document is text+math only.
