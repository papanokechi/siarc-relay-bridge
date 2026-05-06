# Zenodo upload runbook — bt_baseline_note (T1-PHASE2-BASELINE-NOTE v1.0)

This is a **NEW concept DOI** deposit (not a New Version on an
existing DOI). The deposit creates a new Zenodo record with a
fresh concept-DOI and a fresh version-DOI v1.0.

## Pre-flight

Owner: Mauricio Echizen Kubo (papanokechi).
ORCID: 0009-0000-6192-8273.
SIARC community: `siarc`.

Build artefacts staged in:
`siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/`

Files to upload to Zenodo (in this order, primary file first):

1. `bt_baseline_note.pdf` — primary artefact, 8 pages,
   409,337 bytes, SHA-256
   `23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`.
2. `bt_baseline_note.tex` — LaTeX source, SHA-256
   `6746692c517dc25238473e819527c5682465cdc9e1def69d1f6df31c1014d51b`.
3. `annotated_bibliography.bib` — BibTeX bibliography
   (15 entries), SHA-256
   `589f6e4a0b29de401229d60a6252de15436f355a2fa8b3ac04907779c2de923d`.
4. `claims.jsonl` — AEAL provenance log, 10 entries.
5. `rubber_duck_critique.md` — pre-commit self-review, SHA-256
   `97765d9b5c303cf5b13c5a9e4e67323dc47c9e5256b2be4301d0d458fe11bfa3`.

## Step 1 — Open Zenodo new upload

1. Go to https://zenodo.org/.
2. Sign in with the SIARC project account
   (papanokechi / ORCID 0009-0000-6192-8273).
3. Click **+ New upload** in the top-right menu.
4. Do **NOT** start from an existing record this time. This is a
   fresh concept DOI.

## Step 2 — Files

1. Drag `bt_baseline_note.pdf` into the file area first.
2. Then drag the other 4 files. The primary file is auto-set to
   the first file uploaded; verify that the **primary** badge is
   on `bt_baseline_note.pdf`. If not, click the file menu next
   to it and select **Set as primary**.

## Step 3 — Resource type

- Resource type: **Publication** -> **Working paper**.

## Step 4 — Title

Title (paste verbatim, single line):

```
A Newton-polygon formal-level baseline for the Birkhoff-Trjitzinsky exponent on the SIARC polynomial continued-fraction Wallis stratum
```

## Step 5 — Authors

- Mauricio Echizen Kubo (papanokechi)
  ORCID: 0009-0000-6192-8273
  Affiliation: Independent researcher, Yokohama, Japan.

(Single author. Add via the **+ Add another creator** flow only
if a second author is named in a future revision.)

## Step 6 — Description

Paste the **entire** contents of
`zenodo_description_bt_baseline_note.txt` into the Description
field. The file is plain-text wrapped at ~70 columns; Zenodo's
description field accepts plain text and will render line breaks
correctly.

Verify the four bullet sections of the triple framing
(PROVEN / VERIFIED / STRUCTURAL FRAMING / CONJECTURED) are
intact after pasting. This is a HARD HALT: if any of the four
sections is missing or appears truncated, do NOT publish; fix
the description and retry.

## Step 7 — License

License: **Creative Commons Attribution 4.0 International
(CC-BY 4.0)**.

## Step 8 — Keywords

Add each keyword as a separate entry (press Enter between
entries):

- Newton polygon
- Birkhoff-Trjitzinsky
- formal asymptotic exponent
- polynomial continued fractions
- SIARC
- Wallis stratum
- Wimp-Zeilberger ansatz
- difference equations

## Step 9 — Communities

Add to community: **siarc** (SIARC Self-Iterating Analytic
Relay Chain).

## Step 10 — Related identifiers

Add **eight** related identifiers (use the **+ Add another
identifier** button after each):

| Relation         | Identifier (DOI)             | Identifier type |
| ---------------- | ---------------------------- | --------------- |
| isPartOf         | 10.5281/zenodo.19937196      | DOI (PCF-1 v1.3)|
| isPartOf         | 10.5281/zenodo.19963298      | DOI (PCF-2 v1.3)|
| isContinuationOf | 10.5281/zenodo.20015923      | DOI (D2-NOTE v2.1) |
| isCitedBy        | 10.5281/zenodo.19899996      | DOI (CT v1.3)   |
| isCitedBy        | 10.5281/zenodo.19915689      | DOI (T2B v3)    |
| isPartOf         | 10.5281/zenodo.19965041      | DOI (umbrella v2.0) |
| references       | 10.1007/BF02398269           | DOI (Birkhoff-Trjitzinsky 1933) |
| isSupplementTo   | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER | URL (bridge commit 37c939f) |

## Step 11 — Funding

Leave blank (no funding to declare).

## Step 12 — Pre-publish review checklist

Before clicking **Publish**, walk through this checklist line by
line. **All must be YES.**

- [ ] Title matches exactly the title in `bt_baseline_note.tex`
      `\title{...}`.
- [ ] Authors / ORCID set on the upload form match the title-page
      author block of the PDF.
- [ ] Description text contains the four sections of the triple
      framing intact.
- [ ] License is CC-BY 4.0.
- [ ] Resource type is "Publication / Working paper".
- [ ] Communities includes `siarc`.
- [ ] Eight related identifiers added per Step 10.
- [ ] Five files staged: `bt_baseline_note.pdf` (primary),
      `bt_baseline_note.tex`, `annotated_bibliography.bib`,
      `claims.jsonl`, `rubber_duck_critique.md`.
- [ ] No build artefacts are present in the upload (no `.aux`,
      `.bbl`, `.blg`, `.log`, `.out`, `.synctex.gz`,
      `__pycache__`, `.venv`, `*.olean`, `*.ilean`).
- [ ] PDF SHA-256 matches the value above
      (`23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`).
      Verify with `Get-FileHash -Algorithm SHA256 bt_baseline_note.pdf`
      against the local file before uploading.
- [ ] Page count of the PDF is in the spec band [8, 12]
      (currently exactly 8).

If all twelve boxes are YES, click **Publish**.

## Step 13 — Capture DOIs and update bookkeeping

After **Publish**, Zenodo will assign a concept DOI (suffix
ending in `0`) and a v1.0 version DOI. Capture both:

- **Concept DOI**: `10.5281/zenodo.NNNNNNN`
- **v1.0 DOI**:    `10.5281/zenodo.NNNNNNN+1` (typically)

Update the following local artefacts (these are **post-publish**
edits and may be folded into a v1.1 of the note if desired):

1. `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/handoff.md` —
   add the captured DOIs to the **Files committed** or
   **Recommended next step** section.
2. `repo/sequel-papers/bt_baseline_note/annotated_bibliography.bib`
   (when added to the umbrella v2.x cycle) — add an
   `@misc{papanokechi_bt_baseline_v1, ...}` entry referencing
   the concept DOI.

## Halt conditions specific to upload

- **HALT_DOI_COLLISION**: if Zenodo rejects the upload as a
  duplicate of an existing record (this should not happen since
  this is a fresh concept DOI), do NOT force-publish; investigate
  whether a prior aborted upload was created and either delete it
  in Zenodo's draft area or use that record's URL.
- **HALT_PRIMARY_FILE_WRONG**: if the **primary** badge is not
  on `bt_baseline_note.pdf`, do NOT publish; re-set the primary
  file and retry.
- **HALT_TRIPLE_FRAMING_MISSING**: if any of the four
  PROVEN / VERIFIED / STRUCTURAL FRAMING / CONJECTURED sections
  appears truncated in the rendered preview, do NOT publish; fix
  the description and retry.

## Notes

- The note is intentionally short (8 pp) and structured around a
  single positive formal-level result + a single open-question
  proposition. Future revisions (v1.1, v1.2) may extend the
  Phase B sweep table to d in [5, 8] explicitly, add the
  secondary-indicial step to Section 2.2, or fold in any
  acquired piece of the sectorial-upgrade literature
  (Adams 1928 if acquired; Turrittin 1955; Immink 1984).
- Coordinate any v1.x revision with the umbrella-v2.x cycle so
  that the umbrella's Sequel-Papers section can list the
  bt_baseline_note as a citable companion.
