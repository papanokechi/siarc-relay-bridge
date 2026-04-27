# Handoff — T2B-MONAT-PREP-FIX
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** COMPLETE

## What was accomplished
Applied two anomaly fixes to the Monatshefte für Mathematik
submission package: (1) updated the Zenodo DOI to the v2 record
`10.5281/zenodo.19801038`; (2) kept the headline figure
"~585,000 families" as the primary figure and added a one-line
clarifying footnote at its first occurrence (the abstract)
disclosing that Experiment C re-classifies a subset of Experiment
B and that the de-duplicated convergent total is ~578,000.
Recompiled the manuscript cleanly (2 × pdflatex, both exit 0),
producing a 9-page R1 PDF.

## Files staged in this session folder
- `t2b_monat_submission_R1.tex` — copy of `t2b_monat_submission.tex`
  from `sessions/2026-04-27/T2B-MONAT-PREP/`, with the two fixes applied.
- `t2b_monat_coverletter.txt` — copy from the same source folder
  (already compliant; see Step 4 below).

## Step 2 — Anomaly 2 (Zenodo DOI v2)
**Manuscript** (`t2b_monat_submission_R1.tex`):
- Line 109 (was 106 in pre-edit copy): replaced
  `https://doi.org/10.5281/zenodo.19783312` → `…/zenodo.19801038`
  AND link text `10.5281/zenodo.19783312` → `10.5281/zenodo.19801038`.
- This was the **only** occurrence of the v1 DOI in the manuscript.
  Verified by `Select-String 19783312` on the staged file: zero hits
  post-edit.

**Cover letter** (`t2b_monat_coverletter.txt`):
- The cover letter already cited the v2 DOI `10.5281/zenodo.19801038`
  and the headline figure "approximately 585,000 convergent integer
  families". No replacement was needed; file copied unchanged from
  `T2B-MONAT-PREP/`.

## Step 3 — Anomaly 1 (empirical-base clarification)
The manuscript already used "~585,000" as the headline figure
(abstract line 62 / 63 in R1; §3 line 129; Table 4 final row;
§3 aggregate prose at line 398). No figure values were changed.

A single footnote was added at the first occurrence (the abstract),
attached to "$\sim 585{,}000$ families", inserted as lines 63–66
of the R1 manuscript:
```
\footnote{Experiment C ($b_1 \in \{\pm 4, \pm 5\}$, $7{,}174$
convergent families) is a subset of Experiment B; de-duplicated
total is approximately $578{,}000$.}
```
Table 1 row values are unchanged. The §3 aggregate text and the
Table 4 "Total across all experiments (A–D)" row are unchanged
(the footnote in the abstract carries the disclosure for both).

## Step 4 — Cover letter
Inspected `t2b_monat_coverletter.txt`:
- No occurrence of `~325,686` or `325,686` — already states "~585,000".
- No occurrence of `19783312` — already cites v2 DOI `19801038`.
The cover letter is therefore copied unchanged. Confirmed compliant
with relay requirements.

## Step 5 — Compile
Two `pdflatex -interaction=nonstopmode -halt-on-error` passes; both
returned exit code 0. The footnote in `\begin{abstract}` typesets
correctly under the journal-neutral `article` class with
`\thanks` not in conflict; pass-2 log reports `(9 pages, ...)` and
no undefined references.

- Output: `t2b_monat_submission_R1.pdf`
- Size: **434,592 bytes** (~ 425 KB)
- Pages: **9**
- Build logs retained as `_build1.log` / `_build2.log` for audit.

## Files for portal upload
- `t2b_monat_submission_R1.pdf` (manuscript; 9 pages, 425 KB)
- `t2b_monat_coverletter.txt` (cover letter)

## Recommended next step
P-T2B-MONAT-SUBMIT: papanokechi to upload R1 PDF + cover letter
manually via Editorial Manager at
**https://www.editorialmanager.com/mfma/** (Monatshefte für
Mathematik, "Submit New Manuscript"). The Zenodo v2 record at
https://doi.org/10.5281/zenodo.19801038 is publicly available and
matches the citation in the manuscript.

## Judgment calls made
- The footnote was inserted in the abstract block. `article`-class
  abstracts accept `\footnote`; the second pdflatex pass typesets
  it cleanly with no undefined-reference warnings. If MFMA's house
  template later objects to footnotes-in-abstract, a one-line
  rewrite is sufficient (move the footnote to §3 line 129 instead).
  Did not preemptively duplicate the footnote in §3 — the relay
  asked for ONE footnote at the first occurrence.
- Did not modify the `Combined` row (442,140) or the `Total across
  all experiments (A–D) ≈ 585,000` row of Table 4, per relay
  instruction "Do not change Table 1 row values — only add footnote".
- Cover letter required no edits (already had v2 DOI and 585,000);
  treated this as a satisfied no-op and copied unchanged.

## Anomalies and open questions
- None. Both fixes applied cleanly; clean compile; cover letter
  was already compliant.

## Files committed
- `handoff.md`
- `claims.jsonl`
- `halt_log.json` (empty)
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)
- `t2b_monat_submission_R1.tex`
- `t2b_monat_submission_R1.pdf`
- `t2b_monat_coverletter.txt`
- `_build1.log`, `_build2.log`, `t2b_monat_submission_R1.aux`,
  `t2b_monat_submission_R1.log`, `t2b_monat_submission_R1.out`
  (auxiliary; <50 KB each).

## AEAL claim count
1 entry written to `claims.jsonl` this session.
