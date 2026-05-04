# Handoff — WASOW-X3-OCR-ACQUISITION-PROBE
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

Phase A reproduced the prior-session finding under fresh AEAL: the
on-disk Wasow 1965 PDF at
`tex/submitted/control center/literature/g3b_2026-05-03/04_wasow_1965_dover.pdf`
(SHA-256 `f59d6835…aa5fd`, 5,557,950 bytes, 34 pages) is image-only
across all 34 pages, with zero text extracted by `pypdf` and zero
substring hits for "Theorem 11.1" / "11.1" / "sectorial". Phase B
located **two parallel CDL-grade Internet Archive copies of the
1965 Interscience original carrying full OCR text layers** (ABBYY
FineReader 11.0 on `asymptoticexpans0000waso`; tesseract 5.3.0 on
`bwb_P8-CYE-039`) and ruled out fully-OA HathiTrust. Phase C
classified both IA copies as Controlled Digital Lending (operator
sign-in required to borrow; per Rule 2 not auto-completable).
Phase D verdict: **OUTCOME_WASOW_X3_LIBRARY_LOAN_RECOMMENDED_INTERNET_ARCHIVE**
with **OUTCOME_WASOW_X3_OCR_FALLBACK_RECOMMENDED** as the in-house
backup (operator-gated on `winget install … TesseractOCR`).

## Key numerical findings

- Slot-04 PDF SHA-256 = `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`
  (matches `SHA256SUMS.txt` row for `04_wasow_1965_dover.pdf` and
  for `wasow_1965_chap_X.pdf`); script `phase_a_check.py`.
- Slot-04 text-layer chars per page = 0 on 34/34 pages
  (length histogram = `{'0': 34}`); script `phase_a_check.py`.
- Internet Archive item `asymptoticexpans0000waso`: identifier-ark
  `ark:/13960/t22c6sv2q`, OCLC 1147739906, OCR engine = ABBYY
  FineReader 11.0 (Extended OCR), language English, ix+362 p., 1965
  Interscience; CDL (`access-restricted-item: true`).
- Internet Archive item `bwb_P8-CYE-039`: identifier-ark
  `ark:/13960/s2nqrxhzt1z`, OCR engine = tesseract 5.3.0-3-g9920,
  language detected English; CDL.
- HathiTrust full-view (`ft=ft&setft=1`) for the title query: zero
  results on 2026-05-04.
- Operator-side `tesseract` binary: not installed (Get-Command =
  null); `pytesseract`, `pdf2image` not in venv; `PIL` present.

## Judgment calls made

- **Stopped Phase B at 5 routes** rather than exhaust author /
  institutional / library-loan-catalog paths. Justification: two
  high-quality CDL copies with vetted OCR engines were located
  almost immediately, both running ABBYY-grade or modern-Tesseract
  OCR; further searching (UW-Madison repository, Yokohama-area
  library catalogs, Dover/Krieger reprint resellers) would not
  beat the latency of operator-side IA borrow + in-book search.
  Phase B can be re-fired if route 1 turns out unusable.
- **Did not auto-attempt CDL borrow.** Per Rule 2 (no on-behalf
  submission, no browser-driver) and §6 OUT OF SCOPE, the IA
  borrow flow is operator-gated.
- **Did not modify slot 04 or `SHA256SUMS.txt`.** Per §6 (read-only
  for existing image-only copy); any acquired OCR-able PDF would
  be saved as additional slot 04b with a new `SHA256SUMS.txt` row.
- **Did not initiate `winget install` for Tesseract.** Per the
  relay's halt-condition design (`HALT_WASOW_X3_OCR_FALLBACK_NEEDS_TESSERACT`),
  installation surfaces operator-side; surfaced as a clean ask.
- **Did not auto-trigger OCR via cloud APIs.** Per Rule 1 (no API
  keys); Tesseract local install is the spec-aligned fallback.

## Anomalies and open questions

None detected at the level of falsified prior claims or unexpected
positives. Notes that may matter for Claude's review of T1 Phase 3
unblocking:

1. The PDF on disk at `04_wasow_1965_dover.pdf` is labelled "Dover"
   in the filename but the IA copy at `asymptoticexpans0000waso`
   is the 1965 Interscience **original** (publisher = "New York,
   Interscience Publishers", LCCN 65026224//r83, 1965 publication
   date). Pagination of the Wiley/Interscience 1965 hardcover and
   the Dover 1987 reprint is widely reported to be identical in
   the literature, but this is not algorithmically verified by
   this session; once the operator-side CDL borrow yields a
   §X.3 page anchor, the page numbers should be cross-checked
   against slot 04 to confirm the "pp. ~217–225" anchor still
   pins Theorem 11.1 in the IA copy. Low-risk, but worth a
   one-line check before AEAL-quoting.
2. Both IA copies are CDL with download disabled even during
   borrow ("DOWNLOAD OPTIONS — No suitable files to display here").
   Capturing the OCR text from the BookReader during a borrow
   session is via the in-book search endpoint
   (`?q=%22Theorem+11.1%22`), which returns OCR snippet text the
   operator can copy. This is sufficient for ≤30-word verbatim
   quotes at AEAL `literature_quotation` grade for T1 Phase 3
   citation, but it does **not** yield a portable OCR text file
   that could be saved alongside slot 04. If T1 Phase 3 needs
   more than a few quote-anchors, the in-house Tesseract path
   becomes the better choice.
3. Quality of ABBYY 11.0 OCR on Wasow 1965 mathematics: expected
   acceptable for theorem-statement words and Latin variable
   names, but small subscripts / accented indices in eq.
   11.1–11.10 may need diff-checking against the slot-04 image
   PDF before being treated as verbatim. Not blocking, just a
   citation-hygiene note.

## What would have been asked (if bidirectional)

1. Does T1 Phase 3 need (a) ≤3 short verbatim quotes from
   Theorem 11.1's statement (CDL borrow + in-book search is
   sufficient) or (b) the full proof construction of
   eq. 11.1–11.10 as a portable file (in-house Tesseract path
   preferred)? The answer changes which fallback to fire next.
2. Is the operator willing to install Tesseract via winget at
   this stage, or should the CDL route be fired first?

## Recommended next step

**One-line dispatch for the operator:**

> Borrow `https://archive.org/details/asymptoticexpans0000waso`
> at archive.org (sign-in required, 1-hour or 14-day CDL); use
> the in-book search box `?q="Theorem+11.1"` to anchor §X.3
> Theorem 11.1; capture ≤30-word verbatim text-layer snippet
> for the statement plus eq. 11.1 label, paste into a new
> `T1-PHASE3-ANORMAL-DISPATCH/wasow_x3_quote.md`, AEAL-hash
> the snippet (`evidence_type: literature_quotation`). If the
> §X.3 statement is captured cleanly, T1 Phase 3 (sectorial
> upgrade closing G23) is **unblocked**. If the snippet is
> ambiguous or if the proof construction is also needed,
> escalate to in-house Tesseract: `winget install --id
> UB-Mannheim.TesseractOCR`, then `pip install pytesseract
> pdf2image` plus a Poppler binary on PATH, then OCR slot 04
> §X.3 pages (≈ pp. 217–225 in Dover pagination, mapped to the
> 34-page slot via section/page anchors), saving corrected text
> to `literature/g3b_2026-05-03/04_wasow_1965_X3_OCR_extracted.txt`.

## Files committed

- `prompt_spec_used.md`
- `phase_a_check.py`
- `phase_a_check.log`
- `phase_b_routes.md`
- `claims.jsonl`
- `halt_log.json` (empty `{}`)
- `discrepancy_log.json` (empty `{}`)
- `unexpected_finds.json` (empty `{}`)
- `handoff.md`

## AEAL claim count

6 entries written to `claims.jsonl` this session.

---

**VERDICT:** `OUTCOME_WASOW_X3_LIBRARY_LOAN_RECOMMENDED_INTERNET_ARCHIVE`
(primary) + `OUTCOME_WASOW_X3_OCR_FALLBACK_RECOMMENDED` (subordinate,
operator-gated on Tesseract install).

**STRATEGIC IMPLICATION:** T1 Phase 3 (sectorial upgrade via Wasow
§X.3 Theorem 11.1, picture v1.17 §5 G23 closure) remains gated on
operator-side acquisition of an OCR-readable copy. Two clean routes
are now identified and laddered. Operator-side CDL borrow is the
fastest path to T1 Phase 3 dispatch readiness; in-house Tesseract on
slot 04 is the clean backup. The acquisition prerequisite is
**unblocked at the routing level** — no further structural search
is needed; only operator-side execution.
