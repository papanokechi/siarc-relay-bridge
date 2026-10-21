# DEPOSIT-FORM — Channel Theory v1.7

**Not a deposit. Not an instruction to deposit.** This is the set of values that
would be typed or uploaded, written down so they can be **checked against the
deposited v1.6 record before anything is irreversible** rather than reconciled
after. Every value below is read from a held record file, not from memory.

Sources: `../CT-S26-CTV17-DRAFT/refs/zenodo_22782807.json` (the v1.6 record) and
`../CT-S26-CTV17-DRAFT/refs/datacite_concept.json`.

---

## 1. The published artefact

**v1.7 uploads no file.** The ruling is description-only: the v1.6 PDF carries
over to the new version unchanged, and the notice becomes the record
description. So the artefact whose bytes matter is `DESCRIPTION-v1.7-rev3.html`, not
an upload.

```form
deposit_shape: DESCRIPTION-ONLY
upload_dir_must_be_empty: true
description_file: DESCRIPTION-v1.7-rev3.html
description_sha256: 33a3893372dfd9dcd2c89c4202b8db5aa6d8914acf4707bfd93e7442f8c7e293
description_chars: 68303
description_md5: cdfa63630469ee75834acd725a64415b
source_notice: ../CT-S26-CTV17-DRAFT/NOTICE-v1.7.md
source_notice_sha256: a0bb2b84472965d8e6d1eb8ce12f2ee0491ef5bcd233a3e55299f300185c6320
carried_file_key: channel_theory_outline.pdf
carried_file_md5: aa56a94a9354b5533b04c89461950eb1
carried_file_bytes: 609300
```

**The hashes above are taken from the files on disk after the last edit**, and
the pre-flight recomputes both rather than trusting these values. The
`carried_*` values are the v1.6 file as the record reports it; they are what the
carried-over file must still show in the new draft, and they are checked by eye
at the dialog, since a file carried over by the platform is not one this session
can hash.

**No file is staged, and `upload/` is required to be empty.** That is stronger
than staging the notice and choosing not to upload it: the only way to publish
the wrong file is to have one sitting there.

## 2. Metadata — every value diffed against the v1.6 record

The recurring defect is drift between the form and the deposited text. Values
marked `same-as-v1.6` must match the record byte for byte; only `version` is
declared as a deliberate change.

```form
title: Channel Theory for Polynomial Continued Fractions: Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture
title_policy: same-as-v1.6
version: 1.7
version_policy: deliberate-change
version_previous: 1.6
creator_name: papanokechi, papanokechi
creator_affiliation: Independent Researcher
creator_policy: same-as-v1.6
license: cc-by-4.0
license_policy: same-as-v1.6
keywords_policy: same-as-v1.6
keywords_count: 27
concept_doi: 10.5281/zenodo.19941678
concept_doi_source: conceptdoi field of record 22782807
version_doi: MINTED-ON-PUBLISH
publication_date: SET-ON-DEPOSIT-DAY
```

**On the title.** It is retained unchanged from v1.6. The notice corrects the
Painlevé target inside the text, but the title names the `ξ₀ = 2/√β₂` identity,
which §2 of the notice **attributes** rather than withdraws, so no title change
is warranted. A change here would be exactly the drift class this form exists to
catch, and would need its own ruling.

**On the concept DOI.** `10.5281/zenodo.19941678` is read from the `conceptdoi`
field. It is **not** the record number and must never be derived from one. The
version DOI is minted by Zenodo on publish and cannot be written in advance.

**On the date.** Set on the day of deposit, and it must equal the day the record
is actually published — not the day this file was written.

## 3. Deposit shape — **RULED: description-only**

```form
deposit_shape_ruled: DESCRIPTION-ONLY
deposit_shape_ruled_on: 2026-09-19
pdf_rebuild_possible: false
pdf_held: false
new_file_uploaded: false
```

The operator's ruling:

> **Rule it a description-only version.** That is what v1.7 actually is. The
> notice corrects and attributes; it doesn't change the paper. Every prior
> version in this record carries its erratum in the description, and v1.6's own
> defect (1) was precisely a *build* problem — the wrong PDF attached — which is
> the failure mode you avoid entirely by not attaching a build you cannot
> verify.

The v1.6 record publishes exactly one file:

| key | bytes | md5 |
|---|---|---|
| `channel_theory_outline.pdf` | 609300 | `aa56a94a9354b5533b04c89461950eb1` |

**That file carries over to v1.7 unchanged.** It is not re-uploaded by hand and
it is not rebuilt.

**Rebuild was refused outright.** The newest Channel Theory LaTeX in the tree is
v1.3.1; there is no v1.4, v1.5 or v1.6 source, and both PDFs returned HTTP 504
when fetched. A build from v1.3.1 would silently revert two versions of
corrections — the Painlevé-target correction made at v1.4 and the analytic
residual added at v1.6, both of which the notice relies on. **That is worse than
no new file.**

The three shapes considered before the ruling, retained because the reasoning
is the record of why this one was chosen:

| # | shape | what it needed | why not |
|---|---|---|---|
| A | description-only, **re-uploading** the v1.6 PDF by hand | the v1.6 PDF bytes | **not held**; unnecessary — the platform carries the file over, so nothing needs re-uploading |
| B | v1.6 PDF plus the notice as a second file | the v1.6 PDF bytes | **not held**; and a second file needs its relationship to the PDF stated |
| C | rebuild the outline at v1.7 | v1.4–v1.6 LaTeX | **absent**; would revert two versions of corrections |

**The ruled shape is A minus its blocker**: description-only, with the file
carried over by the platform rather than re-uploaded. It needs no bytes this
repository does not hold, which is exactly why it is executable when the other
three were not.

If the v1.6 sources or PDF become available and an updated build is wanted,
**that is v1.8.**

## 4. What must be re-checked at the dialog, by eye, against this file

1. The **Files** panel shows exactly one file, `channel_theory_outline.pdf`,
   **609 300 bytes**, carried over from v1.6 — and **no second file**.
2. The description pasted is 68 303 characters and ends with the last line of
   §10; the field did not truncate it.
3. The version field reads **1.7** and not the previous value.
4. The affiliation reads **Independent Researcher** exactly.
5. The keyword count is **27**.
6. The reserved DOI shown is a **version** DOI; the concept DOI is not edited.

None of these can be fixed after publishing.

## 5. Corrections made to this form after a pre-flight FAIL

**`keywords_count: 28` → `27`.** The pre-flight's `C4` compared the declared
count against `len(metadata.keywords)` in the held v1.6 record and failed: the
record carries **27** keywords, not 28. The 28 was carried from an earlier
version's count and had never been checked against the deposited text. The
record is authoritative and this form was the stale copy — the same class the
version-notice round hit, arriving here in the metadata rather than the prose.

The correction is to the **form**, not to the check. The check fired exactly as
intended and its threshold was not touched.
