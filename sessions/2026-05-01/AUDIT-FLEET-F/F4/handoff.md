# Fleet-F · F4 — BibTeX Hygiene Audit

**Status:** completed (read-only audit)

## Verdict

**HIGH** — multiple cite-but-not-defined issues. Will produce `??` in printed
output unless fixed before next submission.

## Findings

### HIGH — cite-but-not-defined

- **F4-H1** — `mpmath` cited but undefined in any scoped `.bib` for:
  - `tex/submitted/p12_journal_main.tex`
  - `tex/submitted/rigidity_entropy_expmath_article.tex`
  - `tex/submitted/rigidity_entropy_expmath_resubmission*.tex`
  - `tex/submitted/vquad_resurgence_R1.tex`
  - `tex/submitted/vquad_resurgence_R2.tex`
- **F4-H2** — `olver1974`, `odlyzko1995` cited in
  `tex/submitted/paper14-ratio-universality-SUBMISSION.tex` but not in scoped
  `.bib`.
- **F4-H3** — `Okamoto1987` cited in `tex/submitted/p12_journal_main.tex` but
  not in scoped `.bib`.

### LOW — missing DOI

- **F4-L1** — `tex/submitted/SpectralClasses/pcf_spectral_refs.bib:13-20`
  (`@book{costin2008asymptotics}`) has no DOI field.

### INFO — defined-but-not-cited

- **F4-I1** — `pcf_spectral_refs.bib` entries are not cited anywhere in
  `tex/submitted/*.tex`: `poincare1885`, `frobenius1873`, `apery1979`,
  `ronveaux1995`, `wall1948`, `lorentzen2008`, `raayoni2021`,
  `cohen2024database`, `pcf_unified_2026`, `ratio_universality_2026`,
  `pcf_bifurcation_2026`. Likely a "library" bib for future use, not a bug,
  but worth flagging.

### CLEAN

- No duplicate keys.
- No reciprocity issues spotted in scoped `.bib` files.

## Recommendation

Before any future arXiv / journal submission of the affected papers, add bib
entries for the four missing keys (`mpmath`, `olver1974`, `odlyzko1995`,
`Okamoto1987`). Suggested canonical entries:

```bibtex
@misc{mpmath,
  author = {Johansson, Fredrik and others},
  title  = {{mpmath}: a Python library for arbitrary-precision floating-point arithmetic},
  year   = {2023},
  url    = {https://mpmath.org}
}
@book{olver1974,
  author    = {Olver, F. W. J.},
  title     = {Asymptotics and Special Functions},
  publisher = {Academic Press},
  year      = {1974}
}
@book{odlyzko1995,
  author    = {Odlyzko, A. M.},
  title     = {Asymptotic enumeration methods},
  booktitle = {Handbook of Combinatorics},
  publisher = {Elsevier},
  year      = {1995}
}
@article{Okamoto1987,
  author  = {Okamoto, Kazuo},
  title   = {Studies on the {Painlev{\'e}} equations},
  journal = {Annali di Matematica Pura ed Applicata},
  year    = {1987},
  volume  = {146},
  pages   = {337--381},
  doi     = {10.1007/BF01762370}
}
```

(Verify exact metadata before committing.)
