# PREREG — CT-S51-UPLOAD-WALKTHROUGH

Written **before** running `scripts/check_upload_ready.py`. Thresholds fixed here.

## Context

Two uploads were prepared in June 2026 and left HELD for operator hand-action:

- `sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/` — Zenodo deposit of the
  V_quad period-representation paper.
- `sessions/2026-06-18/VQUAD-ARXIV-METADATA-001/` — arXiv submission metadata.

This session does **not** upload anything. It establishes which of those
actions has already happened, re-verifies every transcribable value against the
artefacts as they stand today, and produces operator walkthroughs.

## Hypothesis

**H1.** The Zenodo deposit is still pending, as its handoff states.

**H2.** The June arXiv metadata package is transcribable as written: every
field it lists still agrees with the `.tex` that would be uploaded and with the
live Zenodo record it was cross-checked against.

## Observables

Per-check verdicts from `check_upload_ready.py`, in four blocks:

- **A — source integrity.** Size, digest, self-containment (`\input`,
  `\include`, `\includegraphics`, `\bibliography` all zero; one
  `thebibliography`), identity (no `string from the private pattern file`, author reads `Papanokechi`),
  venue-leak (no `Compositio`, no `submitted to`), PDF pin and page count.
- **B — record state.** The live record's state, DOIs, license, file count and
  related-identifier count, read from a stored API snapshot.
- **C — epistemic agreement.** Whether the abstract that would be *typed into
  the arXiv form* says the same thing, with the same epistemic force, as the
  abstract inside the `.tex` that would be *uploaded*, and as the description
  on the live record.
- **D — corpus support.** Whether the corpus records a label for the Sakai
  `D_5^{(1)}` attribution.

## Falsifiers, with thresholds

- **F1.** Any block-A check fails ⇒ the source is not the certified one; the
  walkthrough must not tell the operator to upload it. Threshold: exact —
  byte size `87778`, PDF digest prefix `33f339ed`, and zero occurrences of each
  forbidden construct.
- **F2.** The live record reports `state != "done"` ⇒ H1 holds and the Zenodo
  walkthrough is a live action. If `state == "done"`, H1 is **refuted** and the
  June handoff is stale; that is a finding about the record, not a defect in
  the deposit.
- **F3.** The macro-expanded `.tex` abstract and the package's transcribable
  abstract differ ⇒ H2 is refuted. Threshold: exact string equality after the
  documented macro expansions and whitespace normalisation. **Any** difference
  fires; there is no tolerance, because the two texts are supposed to be the
  same text in two notations.
- **F4.** If F3 fires, the difference is classified, not tuned: report the
  differing words verbatim. A difference confined to hedging language is an
  **epistemic-status conflict** and is a blocking finding for the upload, since
  the uploaded source and the typed abstract would then disagree in public.

## Vacuity pre-check

Run **after** the observables, so a firing falsifier is never suppressed by an
instrument test (the CT-S47 ordering rule):

- **V1.** The self-containment reader must find the constructs when they are
  present: run it against a synthetic string containing `\input{x}` and
  `\includegraphics{y}` and require non-zero counts. A reader that finds
  nothing anywhere would pass block A vacuously.
- **V2.** The abstract comparator must report equality when given a text and
  its own macro-expanded form, and inequality when given a text differing by
  one word. A comparator that always reports difference would make F3 fire
  regardless of the artefact.
- **V3.** The snapshot reader must fail on a record field that does not exist,
  so "field absent" cannot be confused with "field unread".

## What this session will NOT do

- No upload, no deposit, no submission, no API call that writes.
- No edit to the June sessions, to the `.tex`, or to the live record.
- No decision about whether to hedge the manuscript. If F3/F4 fire, that is
  reported to the operator as a blocking question, not resolved here.
