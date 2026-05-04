PCF-1 v1.3 -- arXiv source pack (REBUILT, DOI-CORRECTED)
========================================================

Title:    Complex Multiplication as a Transcendence Predicate
          for Degree-Two Polynomial Continued Fractions
Author:   Papanokechi (ORCID 0009-0000-6192-8273)
Version:  1.3 (2026-05-01)
Pages:    16

Source provenance
-----------------
This pack rebuilds the v1.3 arXiv mirror tarball from the
canonical 16-page source preserved in the SIARC bridge repo at:

  commit:   58dfa9e732b41b65c2d8791037286a13e21c06be
  path:     sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex
  tex SHA-256: e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301
  pdf SHA-256: 63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e
  pdf bytes:   392886 (16 pages)

The PDF SHA-256 is byte-identical to the v1.3 deposit on Zenodo
(concept DOI 10.5281/zenodo.19931635; v1.3 record 19937196).

[ERRATUM 2026-05-04: the previous 00README.txt contained the
PCF-2 v1.3 DOIs (concept 19941678; record 19963298) here in
error; corrected in PCF1-V13-ARXIV-DRAFT-PREP session.]

Build instructions (from this tarball)
--------------------------------------
The .tex is a self-contained amsart document with an inline
thebibliography environment (no external .bib, no figure files,
no \input or \include). To rebuild the PDF:

    pdflatex p12_pcf1_main.tex
    pdflatex p12_pcf1_main.tex
    pdflatex p12_pcf1_main.tex

Three passes are sufficient (no bibtex run is required because the
bibliography is inline).

Files in this tarball
---------------------
    pcf1_v1.3/00README.txt    -- this file
    pcf1_v1.3/abstract.txt    -- abstract verbatim from the .tex
    pcf1_v1.3/p12_pcf1_main.tex   -- main LaTeX source (16pp, amsart)

The compiled PDF (p12_pcf1_main.pdf) is shipped alongside the tarball
in the wrapping directory (and on Zenodo) for byte-equality verification;
arXiv will recompile from source on upload.

Re-verification
---------------
The tarball SHA-256 and individual file hashes are recorded in the
sibling manifest.txt file in the wrapping pack directory.
