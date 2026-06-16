# Build result — VQUAD-PAPER-CORRECTIONS-001 (Stage 4)

Corrections-final, byte-reproducible build of the V_quad period-representation paper, post H-1
operator verification.

## Build
- Command: `cd latex && python build.py` with `SOURCE_DATE_EPOCH=1718409600`.
- Engine: MiKTeX `pdflatex` (x64), two passes, inline `thebibliography`, preamble byte-repro guards
  (`\pdfinfoomitdate=1`, `\pdftrailerid{}`, `\pdfsuppressptexinfo=-1`).
- Result: **PAGES=24, ERRORS=0**, no undefined citations/references (build.py `UNDEFINED` list empty
  after the 2nd pass; the new `\label{rmk:provenance-C}` and `\eqref{eq:bridge}`/`\eqref{eq:C-from-A}`
  cross-refs all resolve).

## PDF SHA-256 (NEW PIN — supersedes the pre-corrections `359d1172…`)
```
4CA12A35D655DF2227A9E1740E60B39C2E6CABEF6A1942C74307CD43849582FE
```

## Byte-reproducibility — CONFIRMED
Rebuilt once in a pristine temp dir (`%TEMP%\vqrepro_…`, only `sections/` + `latex/{build.py,
preamble.tex}` copied, same `SOURCE_DATE_EPOCH`):
```
pristine-dir SHA-256 = 4CA12A35D655DF2227A9E1740E60B39C2E6CABEF6A1942C74307CD43849582FE   (IDENTICAL)
```
Temp dir removed after verification.

## Wrong-venue check — PASS (definitive; READY-001 had deferred this)
Full text extracted from the rebuilt PDF (`pypdf`, **63,635** chars — extraction non-empty, so the
absence is meaningful). Case-insensitive search for target-venue / submission tokens:
`compositio, inventiones, annals of mathematics, crelle, duke math, journal of the ams,
acta mathematica, publications math, "submitted to", "for publication in", "to appear in"`.
```
WRONGVENUE_HITS = NONE
```
"Compositio" absent; all other target-venue strings absent. **PASS.**

## Rendering spot-checks (in the rebuilt PDF text)
| check | result |
|---|---|
| H-1 remark ("Provenance of the value 0.43770528…") rendered | PRESENT |
| Marchal acknowledgement ("…personal communication") rendered | PRESENT |
| Concept DOI `20455089` present | PRESENT |
| Retracted v1.0 DOI `20455090` present | **ABSENT (purged)** |

## Stage-4 source edits folded into this build
1. **H-1 remark** inserted at `section-4.md` §4.3 (operator-verified), citing `\cite{StokesNote}`,
   `\eqref{eq:C-from-A}`, `\eqref{eq:bridge}`.
2. **[Vquad] bibitem** (`section-9-references.md`): repointed to concept DOI
   `10.5281/zenodo.20455089`; retracted v1.0 lead `20455090` dropped; real deposit title applied.
3. **[StokesNote] bibitem**: real deposit title applied; DOI `10.5281/zenodo.20481592` kept,
   annotated "(version 1.2; the Stokes-constant correction is Remark 6.2 / eq. (13))".
4. **Trap-6 second instance** (`section-8.md` §A.5 reproducibility statement): the same retracted
   `20455090` "parent deposit" headline repointed to concept `20455089`; calibration annotated as
   version 1.2. (Trap-6 scan over all sources: only these two instances of `20455090` existed; both
   purged. No other version-DOI-where-concept-belongs found.)
5. **Marchal acknowledgement** (`section-7.md`, new `\section*{Acknowledgements}`): "We thank
   O. Marchal for correspondence on the topological-recursion reconstruction of Painlevé Stokes data
   (personal communication, June 2026)." (Operator cleared the AEAL barrier; holds the permission.)
