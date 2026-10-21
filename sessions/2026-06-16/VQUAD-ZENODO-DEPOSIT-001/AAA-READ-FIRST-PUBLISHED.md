# ⚠ READ FIRST — this deposit is PUBLISHED. Do not re-run the runbook.

**Sibling marker, written 2026-09-21 by `sessions/2026-09-17/CT-S51-UPLOAD-WALKTHROUGH`
under P0 amendment G. It edits nothing in this folder and disturbs no digest.**

## The discrepancy

`handoff.md` in this folder reads *"HELD at Gate 0 … upload-ready … the manual
upload may now proceed"*, and `operator-runbook.md` presents **Publish** as an
action still to take. Both were written **before** the deposit and were never
updated after it.

**The deposit was executed.** Verified 2026-09-21 against the live Zenodo API:

| | |
|---|---|
| record | `20719043` — `state: done`, `submitted: true` |
| published | **2026-06-16** |
| version DOI | `10.5281/zenodo.20719043` |
| concept DOI | `10.5281/zenodo.20719042` (**not** the record number) |
| files | `vquad-periodrep-paper.pdf`, `vquad-periodrep-bundle.zip` |
| related identifiers | 11 · licence `cc-by-4.0` · ORCID `0009-0000-6192-8273` |

Every value this session staged is present on the live record.

## The rule

`handoff.md` and `operator-runbook.md` are to be read as the record of how this
deposit was prepared, and **not as live instructions**.

- **Do not** follow them as steps to take. Doing so would attempt an
  already-completed irreversible action.
- **Do** read them for how the deposit was prepared. They are accurate about
  that, and they are why it went cleanly.
- The current state is
  `sessions/2026-09-17/CT-S51-UPLOAD-WALKTHROUGH/STATE.md`; the reusable
  procedure is `WALKTHROUGH-ZENODO.md` in the same folder.

## Why a marker and not a correction

Append-only: this session's files are cited by digest, so editing them would
strand those citations. The marker is an addition placed where the mistake
would be made — in this directory listing — rather than in a report three
sessions away, which is not read by the next person to open this folder.

Recorded as claim `S51-08`. The bar for a marker is demonstrated harm; here the
harm is a document that would cause a duplicate deposit.
