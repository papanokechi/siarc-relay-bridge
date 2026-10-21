# UPLOAD-SCREENS.md — the Zenodo deposit, screen by screen

**Status: for the operator, at the keyboard, on deposit day.**

This is the click sequence only. It deliberately does **not** restate values.

| You need | It lives in |
|---|---|
| Field values (title, description, keywords, related identifiers) | `DEPOSIT-FORM.md` |
| Policy and mechanics (why new-version, DOI rules, 504 fallback) | `DEPOSIT-WALKTHROUGH.md` §A3 |
| Abort conditions | `DEPOSIT-WALKTHROUGH.md` §A4 |
| Post-publish recording | `DEPOSIT-WALKTHROUGH.md` §A5 |

Three documents describing the same deposit is already one more than I would
like. It is kept thin on purpose: **every value is quoted in exactly one
place.** If you find a value restated here, that is a defect — this workflow
has lost a hash, a status line and a title to exactly that.

Zenodo's interface changes. Where a label below differs from your screen,
**go by function, not by wording**, and if you cannot tell which control is
meant, stop — an ambiguous convention is a halt condition.

---

## S0. Before the browser (2 min, local)

```powershell
cd C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S21-DEPOSIT-PREP
$env:PYTHONIOENCODING='utf-8'
python scripts\verify_upload_file.py
```

Leave that output on screen. It is what you will compare against, and it is the
only hash you should trust today — **not** the one in this file, not the one in
the chat log, not the one in `DEPOSIT-FORM.md`. Those are all copies, and
copies drift.

---

## S1. Find the record

Go to the record page for **`20481592`** (see §A3 for the DOIs).

Confirm on the page, by eye:

- it is the companion, and it reads **version 1.2**;
- the file list shows `vquad_resurgence.pdf`.

If the page 504s, it is Zenodo, not you — §A3 has the DataCite fallback for
*reading*, but you cannot deposit through it. Wait and retry.

---

## S2. "New version"

The button is on the record page, in the right-hand sidebar, visible only when
you are logged in as the owner.

**Do not** use "New upload" — that mints a new concept DOI and orphans the
record from its own history.

Zenodo creates a **draft** that is a copy of v1.2, including its files and its
metadata. Nothing is public until you press Publish. The draft is yours to
abandon.

---

## S3. Files — the one screen where the default is right

The draft already lists **`vquad_resurgence.pdf`**, carried over.

1. **Leave it alone.** Do not delete it. (§A2, and the operator's ruling: the
   concept DOI must resolve to a record that contains the paper, not only its
   erratum.)
2. Add the notice: drag in, or use the upload control, the file named by
   `verify_upload_file.py` — **from the `upload\` folder, not from
   `CT-R1-AUDIT\`.** The working copy is byte-identical but its *name* begins
   `DRAFT-`, and Zenodo publishes the filename you give it.
3. When the upload finishes, Zenodo lists the file with a size and an md5.
   **Compare both against the S0 output.** This is the verification that
   matters; every other hash in this workflow is hearsay.

You should now see **two** files.

> If Zenodo offers to make the new file the default preview, it does not matter
> for citation. Preferring the PDF is the friendlier choice for a reader.

---

## S4. Metadata

Work down the form with `DEPOSIT-FORM.md` open beside it. Only four things
change from what the draft pre-filled; everything else is inherited and must be
left byte-identical.

| Field | Action |
|---|---|
| Title | **leave exactly as inherited** (Option C — see the form sheet for why) |
| Version | change to `1.3` |
| Publication date | today |
| Description | replace, per the form sheet |
| Keywords | nine inherited, plus the two named in the form sheet |
| Related identifiers | **add nothing**; preserve the inherited row |
| Creators, affiliation, ORCID, licence, resource type | **do not touch** |

The affiliation string in particular has drifted before and is a logged defect.
If the form shows anything other than the inherited value, restore it rather
than retyping it.

**Save draft** before you go any further.

---

## S5. The diff, before Publish

This is §A3's requirement and the step this workflow exists for. With the saved
draft on screen, walk `DEPOSIT-FORM.md`'s pre-publish diff table and check the
**form** against the **document**, field by field, reading both.

Then re-read §A4's five abort conditions and answer each one out loud. Three of
them you have already cleared today; condition 5 can only be answered here,
looking at the form.

If one fires: **Save draft and stop.** A draft costs nothing. A published
version is permanent, and a fourth version published to fix a third is a worse
record than a deposit that happened a day later.

---

## S6. Publish

Zenodo will warn you that publishing is irreversible and that the DOI is
registered immediately. That warning is accurate: files and DOI cannot be
withdrawn by you afterwards, and metadata edits are possible but visible.

Press it once. Wait for the record page.

---

## S7. Immediately after

Before you close the tab, copy down from the published page:

- the **new version DOI**;
- the **new record id** (it will not be `20481592`);
- the publication date as Zenodo recorded it.

Then:

```powershell
python scripts\postpublish_readback.py <NEW_RECORD_ID>
```

That re-fetches the published record from the API and checks it against what
you intended — including that the concept DOI is unchanged, that both files are
present, and that the paper's md5 survived the carry-over. It writes a hashed
output for the claim line.

Then §A5: manifest row, audit section, one claim per fact, invariants, backup.

---

## If something goes wrong

| Symptom | Do this |
|---|---|
| Uploaded the `DRAFT-` named file | Delete that file from the **draft** and re-add the right one. Trivial before publish, permanent after. |
| Deleted the PDF | Re-add it from `refs\vquad_resurgence_v1.2_zenodo-20481592.pdf`; it is byte-identical to the deposited file (verified). |
| Published with wrong metadata | Do **not** publish a v1.4 to fix it. Zenodo permits metadata edits on a published record; make the edit, then record both the error and the edit in `AUDIT.md`. |
| Published with the wrong **file** | Files are immutable after publish. That is a v1.4, and a recorded one. |
| Zenodo 504s mid-deposit | The draft persists. Reload the record's draft rather than starting again. |
