# Handoff — VQUAD-ARXIV-METADATA-001

Date: 2026-06-18 · Status: **COMPLETE** (prepare + verify) · **HELD** for operator web submission.

## What this slot delivered
The arXiv submission metadata package for the V_quad paper, cross-verified against the layout-fixed
source and the live Zenodo record 20719043. The consistency gate is **PASS** (no wrong-venue leak,
identity Papanokechi-only with no Kubota residue, title + abstract match Zenodo). The metadata is
ready to **transcribe** into the arXiv web form — no composing at submission time.

## The arXiv submission is the operator's web hand-action
The agent did NOT submit and did NOT call any arXiv API (same discipline as the Zenodo publish).
Drive the submission from `arxiv-submission-runbook.md`.

## Three things to get right (operator)
1. **Upload SOURCE, not PDF** — the single self-contained file
   `sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.tex`.
   Embedded bibliography (no `.bbl`), TikZ inline (no figures), no `\input`. Do **not** also upload
   `preamble.tex`/`build.py`/the PDF. (A single `.zip`/`.tar.gz` is allowed by arXiv v1.5, but the
   bare `.tex` is simplest.) arXiv makes the TeX source **public** — the source scan is clean.
2. **Actively select CC BY 4.0** — arXiv's default license is NOT CC BY; pick Creative Commons
   Attribution 4.0 to match the Zenodo deposit.
3. **Pre-announcement name-check (mandatory)** — before final submit / public announcement, confirm
   the preview + submission-history metadata show **only Papanokechi**, no Kubota anywhere public;
   use the unsubmit window if needed. Attach ORCID `0009-0000-6192-8273`.

## Field values
See `arxiv-metadata-package.md` (one-screen crib at the bottom). Primary category `math-ph`
(Marchal-endorsed); cross-lists `math.NT`/`math.CA` after announcement (may need separate
endorsement). Abstract = the clean macro-expanded block (no Zenodo deposit-context sentences).

## Decision flags surfaced (operator decides)
- Zenodo concept DOI `10.5281/zenodo.20719042` in Comments? (good cross-reference; optional)
- MSC class `34M55, 11J81, 34E20, 14F40, 33C20, 37K10` transcribed? (source has none; optional)

## ⚠ Staging hygiene — flag before any hand-commit
At task start the index already contained **two DEPOSIT-001 files** pre-staged HELD from the prior
task: `sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/MANUAL-UPLOAD.md` (modified) and
`upload-copy-paste.md` (added). This slot stages **only its own files** (explicit paths). Because a
single hand-commit sweeps the whole index, **commit per slot**: either commit the DEPOSIT-001 pair
separately first, or knowingly include them — do not let them ride along unnoticed under the arXiv
commit message. (`sessions/2026-06-15/EBR3-REVISION-001/` remains untracked and is not ours.)

## HELD commit message (operator)
```
VQUAD-ARXIV-METADATA-001 — arXiv submission metadata prepared + verified (math-ph primary, CC BY 4.0, author Papanokechi); source = layout-fixed; consistency gate PASS; web submission held for operator

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

## Downstream
Operator runs the runbook → arXiv announces → capture arXiv ID + abs URL → send Marchal the concept
DOI → optional SIARC §A ledger log of the arXiv submission (separate bookkeeping).
