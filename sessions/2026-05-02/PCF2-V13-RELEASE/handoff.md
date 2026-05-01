# Handoff — PCF2-V13-RELEASE
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes
**Status:** PARTIAL — build clean, all release artefacts staged; Phase D (Zenodo upload) is operator-blocking and the version DOI placeholder remains in `submission_log_patch_item17.txt`.

## What was accomplished

PCF-2 v1.3 was produced from the v1.2 source by absorbing the cubic-modular framing of Session T2 (2026-05-02) and the cleanup verdict of Sessions R1.1, R1.2, and R1.3 (all 2026-05-01). The source `tex/submitted/pcf2_program_statement.tex` was edited in place across seven edit sites (A1–A7); the resulting PDF builds cleanly in three pdflatex passes at 22 pages (v1.2 was 18). All Zenodo metadata, the submission-log patch (item 17 with `__VERSION_DOI__` placeholder), the verdict, the rubber-duck critique, and a 9-entry `claims.jsonl` are staged at `sessions/2026-05-02/PCF2-V13-RELEASE/`.

## Key numerical findings

- v1.3 PDF: 22 pages, 558 153 bytes, sha256 `87B845A8E382F3C124906ACE0C1A6763CE54BD14C5F9593BBADC77BDD81D263F`.
- v1.3 source: sha256 `82FE2315CFDA2047249D4978D7AE487C21D9BE16A35F15827CE132561F2C8541`.
- v1.2 baseline backup: sha256 `36A41E646C254701A17E1B69F74F30EBA3F295FDCF2C98BB25EF717B63B9D708`, preserved at `archive/pcf2_program_statement_v1.2_baseline.tex`.
- Build: pdflatex 3-pass via MiKTeX `C:\Users\shkub\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe`. pass3.log greps to a single `Output written` line; `! ` (true error) lines = 0; missing citations = 0; unresolved cross-references = 0 after pass 2.
- Edit line numbers in v1.3 source (`tex/submitted/pcf2_program_statement.tex`):
  - Title/version: lines 38–40 (v1.2 → v1.3 cubic-modular framing).
  - Abstract v1.3 closing paragraph: lines 88–99.
  - "What is new in v1.3" hat-line: lines 119–134.
  - B5/B6 d=3 signpost (sec:conjectures): lines 432–448.
  - sec:R1-finer-split rewrite: lines 593–702 (subsection title at 593, T2 phase B table input at 691, T2 phase E paragraph input at 702).
  - op:finer-cubic-split resolved + op:j-zero-amplitude-h6 + op:j-1728-wedge: lines 887–949.
  - AEAL schema (v1.3 canonical form) paragraph: lines 1192–1217.
  - Acknowledgements append: lines ~1380–1387.
  - 4 new bibitems: end of `thebibliography`.
- AEAL claims: 9 entries in `claims.jsonl`.

## Judgment calls made

1. **R1.3 v3 paragraph fix-out-of-band.** The session deliverable `sessions/2026-05-01/PCF2-SESSION-R1.3/v13_paragraph_insert_v3.tex` line 19 has bare `\mathrm{Jac}` outside math mode; this crashed the build with `! LaTeX Error: \mathrm allowed only in math mode.`. Resolution: copy the file to `sessions/2026-05-02/PCF2-V13-RELEASE/v13_paragraph_insert_v3_fixed.tex`, wrap the offending fragment in `$…$`, and `\input` the fixed copy from the v1.3 source. The original session file is left untouched. Logged in `unexpected_finds.json`.
2. **Routing all `\input`s through V13-RELEASE.** For build stability and reproducibility, the T2 phase B table and phase E paragraph were also copied into `sessions/2026-05-02/PCF2-V13-RELEASE/` (byte-identical) and the v1.3 source `\input`s the local copies, so future moves of the T2 and R1.3 session folders cannot break the v1.3 build.
3. **B5/B6 placement.** The formal Conjectures `conj:b5-d3` and `conj:b6-d3` live inside the included v3 file (which lives inside `sec:R1-finer-split`), not at the top of `sec:conjectures`. A signpost paragraph in `sec:conjectures` cross-references them with `\ref{conj:b5-d3}` / `\ref{conj:b6-d3}`. This keeps the empirical context (R1.3 quartic null + T2 modular framing) co-located with the conjectures and avoids a forward-reference at the top of `sec:conjectures`.
4. **F2-M3 caveat parked.** Per task §0, F2-M3 (stale PCF-2 v1.1 prose in the v1.2 zenodo description) is documented here as parked: it does not apply to PCF-2 v1.3 (this release), and applies to Channel-Theory-V13 if/when that fires. No edits to channel-theory metadata in this session.

## Anomalies and open questions

1. **arXiv ID placeholder in bibliography.** `Papanokechi2026R13` cites the polished R1.3 standalone note at `sessions/2026-05-01/STANDALONE-NOTE-POLISH/` with arXiv ID placeholder `XXXX.YYYYY`. If the operator submits to arXiv in parallel, the bibliography must be updated and the v1.3 PDF rebuilt; otherwise the placeholder remains visible in the final upload. Recommended: capture the arXiv ID before Zenodo upload, or accept the placeholder as a known minor caveat.
2. **PCF-1 reference URL change.** The v1.3 release-level Related Identifiers list `references → 10.5281/zenodo.19937196` (PCF-1 v1.3 concept). The pre-existing PCF-2 source-text `\bibitem{Papanokechi2026PCF1}` cites `10.5281/zenodo.19934553` (the PCF-1 series concept). Both are valid; the version-DOI distinction is intentional (concept-DOI for citation; version-DOI for the specific v1.3 record).
3. **B5/B6 numbering.** The R1.3 v3 file calls these "B5, restricted, d=3 only" and "B6, restricted, d=3 only" without a numerical anchor in the macro. They become Conjecture~5 and Conjecture~6 by the LaTeX `\newtheorem{conjecture}{Conjecture}` counter. Should B5/B6 be merged into a single conjecture in v1.3 since both are now d=3-restricted? Parked as a v1.4 cosmetic question; v1.3 keeps both for fidelity to the R1.3 verdict structure.
4. **f2-m3 caveat (Channel Theory v1.3).** Per task §0, F2-M3 is parked here. Recommended next step (separate prompt): run `CHANNEL-THEORY-V13-RELEASE` once PCF-2 v1.3 is on Zenodo, applying the F2-M3 prose-fix at that time.
5. **op:b5-degree-d definition site.** The R1.3 v3 file defines `op:b5-degree-d` inside `sec:R1-finer-split`, not in `sec:openproblems`. The cross-reference `\texttt{op:b5-degree-d}` in `sec:conjectures` resolves correctly because the label is global. Cosmetic question for v1.4: relocate to `sec:openproblems` for tidiness.

## What would have been asked (if bidirectional)

1. Should B5 and B6 merge into a single conjecture (same antecedent `j(Jac(C_b))=0`) in v1.3, since both are d=3-restricted and B5 is the strict-equality form while B6 is the rank-correlation form? Parked as v1.4.
2. Should the v1.3 release also patch the PCF-2 source to cite the freshly-minted Channel-Theory v1.3 record (when that exists), or wait for v1.4? Parked.
3. Should Fleet-A's H6 prediction be cited explicitly in `op:j-zero-amplitude-h6`? The body says "Fleet-A's H6 prediction (proposed during the v1.3 absorption cycle)" without a bib entry — this is intentional because Fleet-A is an internal-fleet artefact, not a citable preprint. Keep as is.

## Recommended next step

**Operator: upload v1.3 PDF to Zenodo as a new version of `10.5281/zenodo.19936297` per Phase D steps in `verdict.md`; then run `SUBMISSION-LOG-PATCH` to fill the `__VERSION_DOI__` placeholder in `submission_log_patch_item17.txt` and append the block to `tex/submitted/submission_log.txt`.**

Optional follow-ups (separate sessions): `CHANNEL-THEORY-V13-RELEASE` (apply F2-M3 prose fix); `T2.5d` (deep-WKB redesign for the j=0 amplitude / Chowla–Selberg closure).

## Files committed

In `sessions/2026-05-02/PCF2-V13-RELEASE/`:

```
archive/pcf2_program_statement_v1.2_baseline.tex
v13_paragraph_insert_v3_fixed.tex          (build-fix copy of R1.3 deliverable)
phase_E_v13_paragraph_fixed.tex            (verbatim copy of T2 deliverable)
phase_B_correlation_table.tex              (verbatim copy of T2 deliverable)
zenodo_description_v1.3.txt
zenodo_notes_v1.3.txt
submission_log_patch_item17.txt            (carries __VERSION_DOI__ placeholder)
verdict.md
rubber_duck_critique.md
build.log                                   (pdflatex pass 3 output)
build_diff.txt                              (Compare-Object v1.2 baseline vs v1.3)
claims.jsonl                                (9 AEAL entries)
halt_log.json                               ({})
discrepancy_log.json                        ({})
unexpected_finds.json                       (1 entry: v3 math-mode fix)
handoff.md                                  (this file)
```

In `tex/submitted/`:

```
pcf2_program_statement.tex                  (v1.3 source, in-place edit)
pcf2_program_statement.pdf                  (v1.3 build, 22pp)
```

## AEAL claim count

9 entries written to `claims.jsonl` this session.
