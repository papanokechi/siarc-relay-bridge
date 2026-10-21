# DEPOSIT-FORM.md — the Zenodo form, field by field

For **New version** on record `20481592`. The form arrives **pre-filled from
v1.2**, so most of the work is deciding what *not* to touch. Every "keep" value
below was read from the live v1.2 record this round
(`outputs/depday_zenodo_20481592.json`), not from memory.

Companion object (working file): `CT-R1-AUDIT/DRAFT-COMPANION-v1.3-NOTICE.md`.
**Upload the staged copy instead:** `upload/vquad_resurgence_v1.3_correction_notice.md`,
byte-identical, under a publishable name —
sha256 `c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c`,
35 918 bytes.

---

## ⚠ Two things to settle before you open the form

**1. If you render a PDF, `c936662f…` is no longer the hash to verify.**
That hash is the **Markdown** file's. A2 leaves the deposit form (PDF render vs
Markdown as-is) explicitly unsettled, and the moment you render, the artefact in
the dialog is a different file with a different hash. Either deposit the `.md`
and verify `c936662f…`, or render and compute the PDF's own sha256 **before**
uploading and record that one in A5. Do not carry `c936662f…` across a format
change — that is the stale-hash defect again, one file-format wide.

*Suggestion, not a ruling:* upload **both** — the PDF for readers, the `.md` as
the byte-exact source the record's hashes refer to. Then both hashes go in A5.

**2. What lands on the concept DOI — SETTLED: keep the paper in the record.**
Operator ruling (AUDIT §R31), superseding A2's earlier "notice only" reading. A
new version whose sole file is an erratum makes `10.5281/zenodo.20455089`
resolve to a record where the paper itself is absent — anyone following a
citation to the companion lands on a correction with nothing to correct.

The mechanics make this the easy path: on **New version**, Zenodo carries the
previous files over by default. So —

| Action | File |
|---|---|
| **Leave it alone** | `vquad_resurgence.pdf` (carried over, 612 719 B, md5 `4d1e4d59…`) |
| **Add** | `upload/vquad_resurgence_v1.3_correction_notice.md` |

The notice-only shape would have required actively **deleting** the carried-over
PDF from the draft. Do not delete it.

*Also fixed:* the notice's own filename begins `DRAFT-`, and Zenodo publishes
the filename you upload. A copy renamed
`vquad_resurgence_v1.3_correction_notice.md` is staged in `upload/`, verified
byte-identical to the notice (`c936662f…`). **Upload that copy, not the
`DRAFT-` one.**

The table below assumes A3 as written: **new version**.

---

## The fields

| Field | Value | Source / action |
|---|---|---|
| **Upload type** | Publication → **Preprint** | v1.2's `resource_type` is `publication / preprint`. Keep it unless you consciously reclassify; if the dialog offers *Other* or *Technical note*, either is arguably a better fit for a notice, but changing it makes v1.3 inconsistent with v1.1–v1.2 of the same concept |
| **Publication date** | the date you publish (e.g. `2026-09-18`) | **Change.** v1.2 shows `2026-06-01`; the form may keep it |
| **Title** | see the two options below | **Change** — decision needed |
| **Authors** | `Papanokechi`, affiliation `Independent Researcher`, ORCID `0009-0000-6192-8273` | **Keep byte-identical.** v1.2 prints exactly `Independent Researcher`. Affiliation-string drift between form and file is a logged defect in this workflow — do not let it become `Independent researcher, Yokohama, Japan` or any other variant |
| **Description** | draft below | **Change** |
| **Version** | `1.3` | **Change** from `1.2` |
| **Licence** | `Creative Commons Attribution 4.0 International` (`cc-by-4.0`) | Keep — v1.2's `license.id` is `cc-by-4.0` |
| **Keywords** | v1.2's nine, plus at most two | see below |
| **Related identifiers** | see below | preserve the existing row |
| **Language** | English | keep if pre-filled |

### Title — reconsider, now that the paper stays in the record

The earlier A/B options assumed a **notice-only** record, where the title had to
announce the erratum or the record would misdescribe its contents. With the
paper retained that reasoning weakens: the record holds the companion *and* its
correction, so the companion's title still describes it accurately.

- **Option C (now recommended).** Leave the record title **exactly as v1.2**:
  > *A non-classical Painlevé V transcendent from a quadratic polynomial continued fraction: surface classification and resurgent Stokes data*

  Citations to the companion keep resolving to a record whose title is the one
  they cite. The correction is carried by the **description**, the version
  string `1.3`, and the notice file itself. Zero drift against v1.1–v1.2.

- **Option A** (title + `— v1.3 correction notice`) is still defensible if you
  want the erratum visible in search results, but it retitles a record whose
  principal file is the paper.

- **Option B** (standalone notice title) no longer fits — the record is not a
  standalone notice.

Note the distinction the earlier draft of this sheet blurred: the **record**
title and the **document** H1 are different objects. The notice's H1 correctly
reads as a correction notice whichever record title you choose; it does **not**
have to match the form. The "title must match the H1" rule came from the
notice-only shape and no longer applies.

### Description (draft — edit freely; Zenodo accepts HTML)

> This notice records five items affecting v1.2 of the companion paper
> (<code>10.5281/zenodo.20481592</code>). Two are corrections: Remark 2.2's
> claim that the finite singularities are apparent is false in general, and a
> lemma shows such points are never apparent; and Conjecture 4.1's stated
> derivation of &beta; = &gamma; = 0 is refuted, with &gamma; = 1 on the
> companion's own data. One item is a clarification that strengthens the
> companion: Conjecture 4.1 presupposes rather than derives the isomonodromic
> deformation family, and that presupposition is supported by the van der
> Put&ndash;Saito moduli-space framework. The remaining two items concern object
> labelling and the scope of passages affected. Quotations from the cited
> literature were verified against page images on the day of deposit.

Check it asserts nothing as author-confirmed: the typo reported to van der Put
and Saito is **not** mentioned above, deliberately — no reply had been received.

### Keywords

Keep all nine from v1.2 — `polynomial continued fractions`, `resurgence`,
`Stokes constant`, `apparent singularity`, `confluent Heun equation`,
`Painlevé V`, `Sakai surface D5^(1)`, `Borel summation`,
`arithmetic identification`.

Add at most: **`correction notice`**, and **`isomonodromic deformation`** (used
throughout C3). Do not add `van der Put–Saito` or a moduli-space term unless you
want the record indexed against work the notice only *cites*.

### Related identifiers — add nothing (this supersedes my earlier advice)

- **Preserve** v1.2's existing row: `10.5281/zenodo.20173773`, relation
  **references**. It will be pre-filled; do not drop it.
- **Do not add a row for `10.5281/zenodo.20481592`.** My earlier draft of this
  sheet said to add it as *is supplement to*, and that was written for the
  notice-only shape. With the paper retained, v1.3 is a **version** of the work,
  not a supplement to its own predecessor — and Zenodo already records the
  version linkage itself, outside `related_identifiers`. Read back from the live
  record:

  > `metadata.relations.version = [{"index": 2, "is_last": true, "parent": {"pid_value": "20455089"}}]`

  and v1.2's `related_identifiers` contains **no** row for v1.1 (`20480603`),
  v1.0 (`20455090`) or the concept DOI. The existing versions do not hand-link
  each other, and v1.3 should not start.

- The direction slip is itself the symptom: *is supplement to* and *is
  supplemented by* point opposite ways, and neither is right for a version of
  the same work. Adding one would mislabel the lineage in exchange for nothing
  Zenodo isn't already recording.

- DataCite's vocabulary has no `corrects` relation, so there is no honest row to
  add here even if one were wanted. The correction is carried by the version
  string, the description and the notice file.

---

## Pre-publish diff (A3's requirement, made concrete)

Check each form field against the document, not against this file:

| Form field | Check against |
|---|---|
| Title | v1.2's record title (Option C) — or your chosen variant. It need **not** match the notice's H1; record and document are different objects |
| Version `1.3` | the notice's own version string |
| Authors + affiliation | v1.2 record, byte-identical |
| Licence `cc-by-4.0` | v1.2 record |
| Related identifier rows | exactly one row — `10.5281/zenodo.20173773` / *references*, pre-filled. Nothing added |
| File hash in the dialog | `c936662f…` for the `.md`, or the PDF's own hash |

Then A4's five abort conditions, then publish, then A5.
