# Handoff — PCF2-V11-RELEASE
**Date:** 2026-05-01
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished
Produced PCF-2 v1.1 source and PDF, integrating empirical results from
Sessions A2 (conductor-7 anchor), B (37-family CM PSLQ scan + WKB
harvest), and C1 (13-family non-CM WKB completion). v1.0 archived to
`tex/submitted/archive/pcf2_program_statement_v1.0.tex`. v1.1 source
replaces it in-place at `tex/submitted/pcf2_program_statement.tex`.
Companion artefacts (Zenodo description, Notes line, rubber-duck
critique) staged in this session directory.

## Key numerical findings
- **Conjecture B4 (sharp WKB exponent identity, cubic case) verified
  on 50/50 cubic families**: A_fit ∈ [5.85, 6.02], mean 5.978,
  σ = 0.026, all within 0.15 of A = 2d = 6.
  Source: combined Sessions A2 + B + C1 harvest, table reproduced
  via `\input` of `wkb_cubic_harvest_v2.tex`.
- **Refined Conjecture B4' empirically falsified at d = 3**:
  0/13 elementary-positive families approach A = 2d−1 = 5.
  Source: Session C1 (13/13 non-CM at A_fit ≈ 6).
- **Bin verdicts (50/50 unsplit at A = 6)**:
  −_S₃_CM: 37/37; +_S₃_real: 10/10; +_C₃_real: 3/3.
- **PCF-2 v1.1 PDF**: 14 pages, compiled cleanly in 3 pdflatex passes,
  0 errors, 0 undefined refs.

## Judgment calls made
1. **Label rename to avoid clash.** v1.0 used `\label{conj:B4}` for
   "B₃ part (iv): Painlevé-hierarchy reduction". The v1.1 prompt
   introduces a new top-level Conjecture B4 (sharp WKB), which would
   collide. Resolved by renaming the v1.0 label to `conj:B3iv` and
   updating the two `\ref{conj:B4}` call-sites (risk register, "Why
   this matters" §). The freed `conj:B4` slot is now the new sharp
   WKB conjecture. No semantic change in the renamed passages.
2. **Bibliography upgrade in place.** Updated the existing
   `Papanokechi2026PCF1` bibitem from "v1.2" to "v1.3" rather than
   adding a parallel `Papanokechi2026PCF1v13` entry, since the Zenodo
   concept DOI (10.5281/zenodo.19934553) auto-resolves to the latest
   version. No new bib entries strictly required for the v1.1 prose
   inserts.
3. **Open Problems section placement.** v1.0 had no Open Problems
   section. Placed the new `\section{Open Problems}` immediately
   after the new B4 section and before "Worked Landmarks", so the
   prompt's spatial constraint ("AFTER Section on Conjecture B3,
   BEFORE Open Problems") is honoured. The four problems are:
   `op:b4-degree-d`, `op:d2-anomaly`, `op:finer-cubic-split`,
   `op:cc-pipeline`.
4. **Op:cc-pipeline drafted from scratch.** v1.0 contained no prior
   op:cc-pipeline wording, so the prompt's "[keep existing wording]"
   could not be honoured literally. Wrote a fresh entry referencing
   PCF-1 Session E + the BOREL-CHANNEL-K-SCAN result, and naming the
   SIARC "CHANNEL-CC-PIPELINE" track (Prompt F).
5. **Table format kept portrait + scriptsize.** The 50-row C1 table
   fits on one page in `\scriptsize` without overflow; landscape
   would have required adding `rotating` to the preamble for
   marginal benefit. Documented in `rubber_duck_critique.md` §2.
   No halt triggered.

## Anomalies and open questions
1. **Concept DOI mismatch.** The prompt cites the existing PCF-2
   record as concept DOI 10.5281/zenodo.19936297 (latest version
   10.5281/zenodo.19936298). However v1.0 of `pcf2_program_statement`
   has not been logged in `tex/submitted/submission_log.txt`. **The
   user will need to verify** the concept DOI 10.5281/zenodo.19936297
   exists on Zenodo before uploading v1.1 as a "new version" of that
   record; if it does not, v1.1 should be uploaded as a new top-level
   record and a fresh concept DOI minted, with v1.0 either skipped
   or back-uploaded. This is flagged as a user-action-required item
   in the post-condition report.
2. **B4 hypothesis tightening deferred.** The conjecture statement
   inherits "the regularity hypotheses of PCF-1 v1.3 §5" by
   reference; the back-reference is mildly cyclic. Acceptable at the
   program-statement level; flagged for tightening if/when a PCF-2
   results paper folds B4 into a formal theorem. See
   `rubber_duck_critique.md` §1.
3. **No author commit to repos this session.** Per the Standing Final
   Step, the bridge directory is staged and ready to commit; the
   `tex/submitted/...` repository (claude-chat workspace, not
   pushed publicly) is updated in-place. The user should run a manual
   commit on `claude-chat` if that workspace is under git, and
   absolutely should not push the `tex/submitted/` PDF until the
   Zenodo upload is finalised.
4. **No reducible-control row in the per-bin verdict table.** The
   Apéry family is reducible and out-of-scope of B3(i) (per
   Remark `rem:apery-reducible`); excluding it from the WKB harvest
   is correct, but the verdict table caption explicitly notes the
   exclusion to avoid reader confusion.

## What would have been asked (if bidirectional)
- Should the PCF-1 v1.3 bib entry receive its own `\bibitem{Papanokechi2026PCF1v13}`,
  or is the in-place upgrade sufficient? (Chose the latter.)
- Is the v1.0 PCF-2 record (concept DOI 10.5281/zenodo.19936297)
  actually live on Zenodo, or is the prompt's DOI a forward
  reference for an upload that has not happened yet? (Cannot
  verify without web fetch; flagged as user-action.)

## Recommended next step
**(op:b4-degree-d) Quartic harvest.** Build a small quartic-family
catalogue (~20–30 Z-primitive irreducible quartics in a bounded lex
window), run the Session B+C1 WKB pipeline, and test whether
A_fit ≈ 8 unsplit (confirms B4 at d=4, supports the d=2-anomaly
hypothesis (a)) or whether a split appears (motivates a search for
the controlling invariant under op:finer-cubic-split). Either outcome
is publishable.

## Files committed (this session)
- `pcf2_program_statement.tex`             (v1.1 source, copied from `tex/submitted/`)
- `pcf2_program_statement.pdf`             (v1.1 PDF, 14 pp, 0 errors)
- `archive/pcf2_program_statement_v1.0.tex` (preserved v1.0 source)
- `zenodo_description_v1.1.txt`            (v1.0 + v1.1 changelog paragraph)
- `zenodo_notes_v1.1.txt`                  (single-line Notes field)
- `rubber_duck_critique.md`                (self-critique of v1.1)
- `handoff.md`                             (this file)
- `halt_log.json`, `discrepancy_log.json`, `unexpected_finds.json`
  (all empty `{}`; no halt or discrepancy triggered this session)

## AEAL claim count
**0** new entries written to `claims.jsonl` this session. v1.1 is a
documentation/release session: the underlying numerical claims
(50/50 cubic harvest, B4' falsification) were already filed under
the AEAL chains of Sessions A2, B, and C1.
