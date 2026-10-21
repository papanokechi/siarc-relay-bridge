# WALKTHROUGH — Zenodo deposit (reusable)

**No deposit is authorised by this document.** It is the procedure, distilled
from the one deposit in this programme known to have gone end to end — the
V_quad period-representation paper, record `20719043`, published 2026-06-16 —
plus the rules earlier sessions paid for. Use it when a venue decision has been
made; it is written to be reusable for the Painlevé V paper.

> **Tooling note, verified 2026-09-21.** The June runbook drives the deposit
> through a runner kit — `run_sandbox_draft.py`, `run_production_draft.py`,
> `_zenodo_uploader.py`, `set_prod_token.ps1`, `check_prod_token.ps1`. **None of
> those files is in this repository** (recursive search: absent). They live in
> the operator's deposit folder outside the worktree. That is not evidence they
> do not exist — only that this tree cannot run them. The steps below are
> therefore written for the **web UI**, which needs no kit. If you still have
> the runner folder, its sandbox-then-production path is strictly better,
> because it rehearses the whole deposit before touching production.

---

## Stage 0 — before anything is staged

- [ ] **Decide the record shape.** One record carrying paper + reproducibility
      bundle (what V_quad did — "Scenario B"), or separate records? Decide
      before uploading; it changes the related-identifier set.
- [ ] **Freeze the artefacts.** Build the final PDF, build the bundle, and
      record the **sha256 of each**. Everything downstream cites these.
- [ ] **Write the metadata once, in a file**, not in the browser. Title,
      authors + ORCID, affiliation, description, license, keywords, related
      identifiers, version. The browser is for transcription only.

## Stage 1 — the pre-upload gates

These are the ones that have actually caught defects here.

- [ ] **Re-hash immediately before upload.** Hash the staged PDF and bundle
      again at the keyboard and compare to Stage 0. Files under a syncing
      folder can drift between build and upload; this is the only guard against
      depositing a file you did not certify.
- [ ] **Identity sweep.** Grep every uploaded artefact for any name that must
      not be public. Remember the archive's *contents* are public too, not just
      the PDF.
- [ ] **Venue sweep.** No target-venue string anywhere in the metadata or the
      artefacts.
- [ ] **Metadata-vs-archive diff.** Compare the metadata you are about to type
      against the `CITATION.cff` (or equivalent) **inside** the uploaded
      archive. Title, version and keyword drift between the form and the bundle
      is the recurring defect in this programme, and it has occurred more than
      once.
- [ ] **Epistemic sweep** — the finding from this session. Read the abstract
      and description you are about to publish and check every claim's force
      against the corpus label. A description asserting as established
      something the record labels CONJECTURED or INCONCLUSIVE is a defect that
      no digest, hash or build check can see. Zenodo metadata can be edited
      later; a published assertion has still been published.

## Stage 2 — rehearsal

- [ ] If you have the runner kit: sandbox draft first, eyeball it, discard.
- [ ] If you do not: create the record in the web UI, fill everything, and
      **stop before Publish**. Zenodo keeps unpublished drafts; use that as the
      rehearsal.

## Stage 3 — the record

- [ ] Upload the files. Confirm every file is listed with the expected size.
- [ ] Transcribe metadata from your Stage 0 file.
- [ ] **Related identifiers** — add them all; count them and compare to your
      plan. V_quad carries 11.
- [ ] **License** — set it deliberately, and make it match any preprint you
      will post.
- [ ] **ORCID** — attach it to the creator, not just to your account.
- [ ] Review the rendered draft as a reader would: title, authors, affiliation,
      abstract, files, license, related identifiers.

## Stage 4 — Publish (irreversible; operator only)

- [ ] Publish.
- [ ] **Capture BOTH DOIs immediately.** The **version DOI** and the **concept
      DOI** are different, and the concept DOI is **not** the record number:
      V_quad is record `20719043`, version DOI `10.5281/zenodo.20719043`,
      concept DOI `10.5281/zenodo.20719042`. Read `conceptdoi` from
      `https://zenodo.org/api/records/<id>` — never assume it.
- [ ] Cite the **concept** DOI wherever you mean "the work"; cite the version
      DOI only when you mean that exact deposit.

## Stage 5 — the same session, not the next one

The deposit-day rule: an identifier that exists only in your browser history is
not recorded.

- [ ] Append the ledger entry with both DOIs.
- [ ] Add the deposit-log index row.
- [ ] Verify what you wrote by **reading it back from the API**, resolving each
      field by its exact path (`pids.doi.identifier`, `parent.pids.doi.identifier`) —
      not by searching the JSON for a key named `doi`, which matches an object
      and will silently write a Python dict into your ledger. That has happened.
- [ ] Notify anyone owed the DOI.

## Stage 6 — after publication

- **Files are immutable.** Correcting a file requires a **new version**, which
  mints a new version DOI under the same concept DOI.
- **Metadata can be edited** on a published record without a new version.
  Confirm the current behaviour in the UI before relying on it.
- Any edit you make should be recorded in the session record the same day, with
  the reason — an unexplained metadata change is indistinguishable later from a
  mistake.
