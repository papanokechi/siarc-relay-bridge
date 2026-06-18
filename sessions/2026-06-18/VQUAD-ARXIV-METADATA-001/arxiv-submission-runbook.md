# arXiv submission runbook (operator web hand-action) — VQUAD-ARXIV-METADATA-001 · Stage 4

Slot: `sessions/2026-06-18/VQUAD-ARXIV-METADATA-001/`
This slot PREPARED + VERIFIED the metadata (gate PASS). The arXiv web submission is the
operator's identity-bound hand action — like the Zenodo publish. The agent does NOT submit, does
NOT call any arXiv API. Transcribe the verified values from `arxiv-metadata-package.md`.

---

## Pre-flight (operator, before opening the form)
- [ ] Confirm logged into arXiv as **Papanokechi** (account renamed; the public byline must be
      Papanokechi, never Kubota).
- [ ] Have `arxiv-metadata-package.md` open (the field values) and `arxiv-source-inventory.md`
      (the upload file).
- [ ] Separate pre-flight: confirm the Compositio preprint policy does not conflict with the live
      pseudonymity pre-clearance thread (do this BEFORE announcing; not part of the form).

## Web-form steps
1. **Log in** to arXiv (Papanokechi account).
2. **Start submission** → set **primary category = `math-ph`**.
3. **Upload source** — the single file `vquad-periodrep-paper.tex`
   (`sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.tex`).
   - It is self-contained: embedded `\thebibliography` (no `.bbl`/bibtex), TikZ inline (no figures),
     no `\input`. **Upload only this `.tex`** — do **NOT** also upload `preamble.tex`, `build.py`,
     or the PDF. (arXiv v1.5 also accepts a single `.zip`/`.tar.gz`, but one bare `.tex` is simplest.)
   - arXiv requires the SOURCE, not the PDF; the uploaded TeX source is made **public**.
4. **Verify arXiv's compile succeeds** — check the arXiv-generated PDF preview. Expect 24 pages.
   The arXiv PDF differs from the Zenodo PDF `33f339ed…` (arXiv adds a header/ID stamp) — **expected,
   not a defect**. Confirm the bibliography renders (embedded list) and there are no missing-figure
   or undefined-citation errors.
5. **Transcribe metadata** (from `arxiv-metadata-package.md`):
   - Title: `An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient`
   - Authors: `Papanokechi`
   - Abstract: the clean macro-expanded block (Field 3) — **not** the Zenodo entity-encoded text and
     **without** the 3 Zenodo deposit-context sentences.
   - Comments: `24 pages` (+ optional `Zenodo: https://doi.org/10.5281/zenodo.20719042` — your call).
   - MSC class (optional): `34M55, 11J81, 34E20, 14F40, 33C20, 37K10`.
   - DOI / journal-ref / report-no: leave **blank**.
6. **License step — ACTIVELY select `CC BY 4.0`.** ⚠ arXiv's default is the non-exclusive
   distribution license, NOT CC BY. You must change it to Creative Commons Attribution 4.0 so the
   preprint matches the Zenodo deposit license.
7. **Author/claim** — set author = `Papanokechi`; claim authorship ("yes, I am an author");
   **attach ORCID `0009-0000-6192-8273`**.
8. **BEFORE final submit / BEFORE public announcement** — review the preview AND the
   submission-history metadata; confirm **only Papanokechi** shows and **no Kubota** anywhere public.
   Use the unsubmit window if any correction is needed. (Source scan is already clean — this is a
   confirmation, not an expected fix.)
9. **Submit.** After it announces, attempt **cross-lists** `math.NT` and `math.CA` (each may require
   separate endorsement).
10. **Optional** — add the Zenodo DOI later via the arXiv journal-ref/DOI facility (if not put in
    Comments at step 5).

## After announcement (downstream)
- Capture the arXiv ID + abs URL.
- Send Marchal the concept DOI `10.5281/zenodo.20719042` (already-planned) and, if desired, the
  arXiv abs link.
- Log the arXiv submission in the SIARC ledger §A when ready (separate bookkeeping step; not in
  this slot).

---

## One-screen field crib

| Field | Value |
|---|---|
| Primary category | `math-ph` |
| Cross-list (after) | `math.NT`, `math.CA` |
| Source upload | `vquad-periodrep-paper.tex` (only) |
| Title | `An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient` |
| Authors | `Papanokechi` (+ ORCID `0009-0000-6192-8273`) |
| Abstract | clean block, `arxiv-metadata-package.md` Field 3 |
| License | **CC BY 4.0** (actively select) |
| Comments | `24 pages` (+ optional Zenodo concept DOI) |
| MSC (optional) | `34M55, 11J81, 34E20, 14F40, 33C20, 37K10` |
| DOI / journal-ref | blank |
