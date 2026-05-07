# Zenodo upload runbook -- D2-NOTE v1.0 (relay 083 refresh)

**Date prepared:** 2026-05-07 (Thu, W20)
**Bridge HEAD at draft time:** `402c7de`
**Agent:** GitHub Copilot (VS Code), session `T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083`
**SQL todo addressed:** `zenodo-upload-d2-note` (id N/A; status `pending` per
`tex/submitted/control center/sql_todos_snapshot_2026-05-07_18-40-JST.md` L118).
**Supersedes (refreshes):** `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/zenodo_upload_d2_note_runbook.md`
(2026-05-02 original runbook; substrate carried verbatim where unchanged).

> **OPERATOR ACTION REQUIRED BEFORE FOLLOWING SECTIONS 4-8 BELOW.**
> See `## 0. Pre-deposit decision: SUPERSESSION GATE` immediately below.
> The agent did NOT pre-select a disposition; the operator must choose
> DROP, DEPOSIT_AS_NEW_CONCEPT, or DEFER before any web-form action.

---

## 0. Pre-deposit decision: SUPERSESSION GATE

The picture chain memory + `close_out_matrix_2026-05-07.md` +
`sql_todos_snapshot_2026-05-07_18-40-JST.md` jointly record TWO
already-landed D2-NOTE deposits on Zenodo, both at the SAME concept
DOI:

| Version | Concept DOI | Version DOI | Deposit timestamp |
|---|---|---|---|
| v2.0 (6 pp) | 10.5281/zenodo.19996689 | 10.5281/zenodo.19996690 | 2026-05-03 ~16:00 JST |
| v2.1 (6 pp) | 10.5281/zenodo.19996689 | 10.5281/zenodo.20015923  | 2026-05-04 ~07:00 JST |

Anchoring (Phase A.P3 cross-check): see `picture_revised_20260507.md`
L265 / L2052 / L2339 / L2378; `picture_revised_20260504.md` L220 /
L2007 / L2294 / L2333; `picture_revised_20260503.md` L203 / L1875 /
L2162 / L2201; `close_out_matrix_2026-05-07.md` L132. (No D2-NOTE
entries are recorded in `tex/submitted/submission_log.txt` Zenodo
sub-section as of 2026-05-07; that file's Zenodo block ends at Item 10
T2B v3.0 dated 2026-04-30 -- a separate inventory gap noted as D-3 in
`discrepancy_log.json`.)

D2-NOTE v1.0 (this runbook's payload target) is the 4-page 343 419-byte
2026-05-02 pre-cursor draft -- a strict subset of the v2.0 / v2.1
6-page material by content (per the close-out matrix cross-reference
at L132 and the v2 Phase-A revalidation memo).

The operator must choose ONE of the following dispositions BEFORE
running sections 4-8 of this runbook:

### Option A -- DROP (recommended for economy, agent-non-binding)

Treat the v1.0 deposit as superseded by v2.0/v2.1; mark the SQL todo
as done with a `superseded_by: v2.0_at_19996689` note. No Zenodo
action; runbook archived as substrate-only.

```sql
UPDATE todos
SET status = 'done',
    description = description
                 || char(10) || char(10)
                 || '[2026-05-07 HH:MM JST] DROPPED -- superseded by D2-NOTE v2.0 deposit at concept DOI 10.5281/zenodo.19996689 (version 19996690 / v2.0 6pp / 2026-05-03) and v2.1 at 20015923 (2026-05-04). v1.0 4pp content is a strict subset of v2.0/v2.1 per close_out_matrix_2026-05-07.md L132.'
WHERE id = 'zenodo-upload-d2-note';
```

### Option B -- DEPOSIT_AS_NEW_CONCEPT (orphan-concept route)

Deposit v1.0 as a fresh Zenodo record with a NEW concept DOI distinct
from 19996689. Description must explicitly note that v2.0/v2.1 at
concept 19996689 are the canonical D2-NOTE record; v1.0 as deposited
under this option is a historical 4-page consolidatory draft. Run
sections 4-8 below with the `_supersession_warning` block in
`zenodo_d2_note_metadata.json` materialised in the Zenodo description
field as a "Historical preface" paragraph.

### Option C -- DEFER

Hold the v1.0 deposit pending W21 LANE-1 (Mon 2026-05-12) ratification
of the disposition. No Zenodo action this week. Archive this runbook
as substrate-only; surface the question to the synthesiser briefing
pack.

> Until the operator selects Option A, B, or C, the rest of this
> runbook (sections 1 through 9) is intentionally inert. Sections 1-9
> assume Option B was selected; if Option A or C is selected, only
> the SQL update of section 0 (Option A) or no action (Option C) is
> taken.

---

## 1. Pre-deposit checks

The pre-deposit checks below run BEFORE clicking "New upload" on
Zenodo. Their purpose is to re-verify the v1.0 substrate as
bit-identical to the 2026-05-02 freeze captured in `claims.jsonl`
D2-A6/A8.

- [ ] D2-NOTE v1.0 PDF + .tex + bib SHA-256 verified (run command in
      §1.1 below; expected hashes in §1.2)
- [ ] arXiv classification status documented. Per SQL todo
      `q-claude-30-31-send-d2-note-v21` (status `pending` per
      sql_todos_snapshot_2026-05-07_18-40-JST.md L138):
      Q-Claude-31 (arXiv classification) has agent-side advisory
      `math.CA` primary / `math.NT` cross-list, NOT YET ratified by
      Claude. Cite this status in the Zenodo description's
      "Historical preface" paragraph if Option B is taken.
- [ ] Self-containment status documented. Same row notes Q-Claude-30
      (self-containment) substrate at v2.1 + Phase A* + BT1933
      §§4-6 + Newton-polygon Lemma + Wasow §19 chain. v1.0 PRE-DATES
      this v2.1 substrate; v1.0 self-containment status is the
      2026-05-02 baseline (CT v1.3 Prop 3.3.A + PCF-1 v1.3 Theorem 5
      + PCF2-SESSION-Q1 d=4 verification at dps=80, spread 0).

### 1.1 SHA-256 verification command

From the workspace root:

```powershell
cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-02\D2-NOTE-DRAFT"
Get-FileHash -Algorithm SHA256 d2_note.pdf, d2_note.tex, annotated_bibliography.bib, claims.jsonl |
    ForEach-Object { "{0}: {1}" -f ($_.Path | Split-Path -Leaf), $_.Hash.ToLower() }
(Get-Item d2_note.pdf).Length    # expected 343419
```

### 1.2 Expected hashes (substrate freeze 2026-05-02; re-verified 2026-05-07)

| File | Size (bytes) | SHA-256 (lowercase hex) |
|---|---:|---|
| `d2_note.pdf`               | 343419 | `f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8` |
| `d2_note.tex`               |  16189 | `14044cd41760977504ef68725ebc9d2481d36dce22272227c24f9f9464dabc70` |
| `annotated_bibliography.bib`|  30011 | `d1b16d781881737599f3e5d44ebf9bc4b35e38006159885e871bec57c93937f5` |
| `claims.jsonl`              |   5205 | `026e821afa5c5f3748e43d8b56b83b92f8a11ba2aa29a4493248a9d0405e8e81` |

The `d2_note.pdf` SHA matches the 2026-05-02 D2-A6/A8 anchor verbatim;
no drift across the 5-day interval.

---

## 2. Files to upload

From `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/`:

| File | Required | Purpose |
|---|---|---|
| `d2_note.pdf`                | YES | Main artefact (4 pages, 343 419 B) |
| `d2_note.tex`                | YES | LaTeX source for reproducibility |
| `annotated_bibliography.bib` | YES | Bibliography source |
| `claims.jsonl`               | YES | AEAL claim ledger (8 entries D2-A1..D2-A8) |

Do NOT upload: `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`, `*.toc`,
`pass3.log`, `d2_note.log.tmp` (derivative build artefacts).

---

## 3. Web-form steps

1. Navigate to <https://zenodo.org/uploads/new>.
2. Click **New upload** (do NOT click "New version" of any existing
   record; per Option B, v1.0 must mint a fresh concept DOI distinct
   from 19996689).
3. Upload the four files in §2, in the order listed (`d2_note.pdf`
   first; Zenodo uses the first-listed PDF as the default preview).
4. Paste metadata fields per `zenodo_d2_note_metadata.json` (in the
   same bridge session directory). The mapping from JSON keys to
   Zenodo form fields is:

| JSON key | Zenodo form field | Paste contents |
|---|---|---|
| `upload_type`       | Resource type           | Publication |
| `publication_type`  | Publication type        | Preprint    |
| `title`             | Title                   | verbatim from JSON |
| `creators[].name`   | Creator name            | one row per creator |
| `creators[].affiliation` | Creator affiliation | one per row |
| `creators[].orcid`  | Creator ORCID           | one per row |
| `description_paste_instruction` | Description    | paste contents of `zenodo_description_d2_note.txt` Description block (between the `<!-- ===== Description ===== -->` marker and the `<!-- ===== Related Identifiers ... -->` marker) |
| `keywords`          | Keywords                | comma-separated |
| `license`           | License                 | select `Creative Commons Attribution 4.0 International` |
| `communities`       | Communities             | empty (operator may add `siarc` if standard for this cohort) |
| `version`           | Version                 | `1.0` |
| `language`          | Language                | English (eng) |
| `publication_date`  | Publication date        | `2026-05-02` (artefact freeze date; the upload-event date is recorded by Zenodo separately) |
| `related_identifiers` | Related identifiers   | one row per JSON entry; map `relation` -> Zenodo dropdown, `scheme` -> `DOI` or `URL`, `identifier` -> verbatim |

5. **OPTION B HISTORICAL PREFACE.** If Option B is taken, prepend the
   following paragraph to the Description field BEFORE the substrate
   block. The paragraph is META-class (operator-action / orphan-concept
   disclosure) and does NOT count against the forbidden-verb scan.

   > [META] Historical preface (added 2026-05-07 at deposit time).
   > This 4-page record is the 2026-05-02 pre-cursor draft of D2-NOTE.
   > A 6-page expanded version (D2-NOTE v2.0) was already deposited
   > 2026-05-03 at concept DOI 10.5281/zenodo.19996689 / version DOI
   > 10.5281/zenodo.19996690, and a further amended v2.1 at version
   > DOI 10.5281/zenodo.20015923 (2026-05-04). The current record is
   > deposited under a DISTINCT concept DOI for archival completeness;
   > the canonical citable D2-NOTE artefact is the v2.x record at
   > concept 19996689. Cross-reference: close_out_matrix_2026-05-07.md
   > L132; sql_todos_snapshot_2026-05-07_18-40-JST.md L118 (SQL todo
   > zenodo-upload-d2-note v1.0).

6. **Reserve DOI before save** -- on the Zenodo upload form, click
   "Reserve DOI" to mint a draft concept + version DOI pair. Record
   both in section 6 of this runbook (post-deposit verification).

7. Click **Save** (draft).

8. Click **Preview**; verify the rendered description does not
   render raw HTML comment markers (`<!-- ... -->`) and that all 10
   Related Identifier rows resolve (Zenodo renders a green check or
   text marker).

9. Click **Publish**; record final concept + version DOIs in §6.

---

## 4. Post-deposit verification

- [ ] Concept DOI resolves: open <https://doi.org/10.5281/zenodo.{NEW_CONCEPT}>
      and verify it routes to the new record.
- [ ] Version DOI resolves separately from concept (different page).
- [ ] Title rendered on Zenodo matches PDF metadata title.
- [ ] Authors row matches PDF metadata author + ORCID.
- [ ] All 10 Related Identifier rows live (8 References + 2
      isDocumentedBy); each external DOI resolves in a fresh tab.
- [ ] PDF download SHA matches local SHA. Run:

      ```powershell
      $pub = "https://zenodo.org/records/{NEW_VERSION_ID}/files/d2_note.pdf?download=1"
      Invoke-WebRequest $pub -OutFile zenodo_readback.pdf
      (Get-FileHash zenodo_readback.pdf -Algorithm SHA256).Hash.ToLower()
      # MUST equal: f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8
      Remove-Item zenodo_readback.pdf
      ```
- [ ] (Option B only) Historical preface paragraph rendered cleanly;
      `19996689` and `19996690` and `20015923` all appear as expected.

If the readback hash does not match the local hash, do NOT trust the
upload; re-upload from the local source files (Zenodo does not allow
post-publish file edits; a corrective v1.0.1 would be required).

---

## 5. Submission log update

After Phase 4 verification, splice a new Item NN entry into
`tex/submitted/submission_log.txt`. Current state of the Zenodo
sub-section: items 1 through 10 are present (final entry is Item 10
T2B v3.0 from 2026-04-30, version DOI `10.5281/zenodo.19915689`
concept DOI `10.5281/zenodo.19783311`). The next item number for the
Zenodo sub-section is **Item 11**.

The Zenodo sub-section starts at L227 (`Recorded Submissions
(https://zenodo.org/)`), with separator at L228, Item 1 starting at
L229. Item 10 ends at L284 (the file's last non-blank line is the
ORCID URL `https://orcid.org/0009-0000-6192-8273` at L284 with the
closing trailer `Verdict: N/A` at L243). The splice point for Item
11 is **between L243 and L244** (after the final `Verdict: N/A` of
Item 10 and before the blank-line + Note + ORCID trailer that ends
the file).

Per `tex/submitted/submission_log.txt` substrate snapshot 2026-05-07
~18:40 JST (file size 17030 bytes, line count 284, SHA-256
`2A28465AE39BADF5AB245C3114C84E3E1469BF2FA1CDD967AC017FF4C617E45A`).

Item template (mirrors Item 10 verbatim form):

```
11. Filename: d2_note.pdf
    Title: Newton-polygon universality of the Borel-singularity radius for polynomial continued fractions
    Submitted on: 2026-05-07
    Status: Published on Zenodo (preprint, no journal review)
    Submission ID: DOI 10.5281/zenodo.{NEW_VERSION_ID}
    Concept DOI: 10.5281/zenodo.{NEW_CONCEPT_ID}
    Version: 1.0
    Notes: Option B orphan-concept deposit; historical preface added at deposit time per relay-083 runbook section 3 step 5; canonical D2-NOTE record is v2.0/v2.1 at concept 10.5281/zenodo.19996689 (version DOIs 19996690 and 20015923).
    Verdict: N/A
```

Splice mechanic: paste the 9-line block above between the final
`Verdict: N/A` of Item 10 (L243) and the blank line that precedes
the `Note:` trailer block (L244-L284). After splice, file LC =
284 + 9 = 293; SHA changes; Item 11 anchor token `11. Filename:
d2_note.pdf` should match exactly once.

---

## 6. SQL update

After deposit lands and submission_log Item 11 splices clean:

```sql
UPDATE todos
SET status = 'done',
    description = description
                 || char(10) || char(10)
                 || '[2026-05-07 HH:MM JST] Deposited at concept DOI 10.5281/zenodo.{NEW_CONCEPT_ID} / version DOI 10.5281/zenodo.{NEW_VERSION_ID}; Option B orphan-concept route; historical preface noting v2.0/v2.1 supersession added at deposit time.'
WHERE id = 'zenodo-upload-d2-note';
```

---

## 7. Bridge URLs (post-publish)

After deposit + submission_log splice + SQL update, the bridge
advertisements are (substitute the minted IDs):

```
BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-07/T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083/
CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-07/T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083/handoff.md
ZENODO (v1.0 orphan concept): https://doi.org/10.5281/zenodo.{NEW_CONCEPT_ID}
ZENODO (canonical v2.0/v2.1): https://doi.org/10.5281/zenodo.19996689
```

---

## 8. If anything fails

- **Upload page hangs / Zenodo 502:** retry once. If still failing,
  save the draft and notify; do NOT click Publish on a partial
  upload.
- **DOI mints with a chained-version link to 19996689 instead of a
  fresh concept:** STOP. Contact Zenodo support before publishing;
  publishing under a chained version corrupts the concept-DOI lineage
  for v2.0/v2.1. (Option B requires a clean orphan concept.)
- **PDF readback hash mismatch:** treat as data loss; pull the record
  via Zenodo support (post-publish file edits are not supported) and
  re-upload from local source files as v1.0.1.
- **Operator changes mind to Option A mid-flight:** if `Save (draft)`
  has been clicked but `Publish` has not, click `Discard` to drop the
  draft. Then run the Option-A SQL update from §0.

---

## 9. Cross-references

- 2026-05-02 original runbook: `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/zenodo_upload_d2_note_runbook.md`
- 2026-05-03 v2.0 runbook: not separately archived; deposit captured
  in `picture_revised_20260503.md` L2162 + claims.jsonl D2-A claim 64
  (per picture chain).
- 2026-05-03/04 v2.1 deposit: `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/zenodo_upload_d2_note_v2_1_runbook.md`
- v2.1 self-containment + arXiv classification: SQL todo
  `q-claude-30-31-send-d2-note-v21` (pending; sql_todos_snapshot
  L138).
- Picture chain memory: `tex/submitted/control center/picture_revised_20260507.md`.

End of runbook.
