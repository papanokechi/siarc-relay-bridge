
---

## R31 — the paper stays in the record

Operator reconsidered the deposit shape and overruled A2's *notice only*. A new
version whose sole file is an erratum makes the concept DOI
`10.5281/zenodo.20455089` resolve to a record where the paper itself is absent,
so a reader following a citation to the companion lands on a correction with
nothing to correct. The record keeps both.

Checking how to do that produced a better answer than re-uploading. On Zenodo
**New version** the previous files are **carried over by default**, so keeping
the paper is the default and the notice-only shape would have required actively
**deleting** `vquad_resurgence.pdf` from the draft. A2 now says: do not delete
it, add the notice beside it. Belt and braces, the held copy
`refs/vquad_resurgence_v1.2_zenodo-20481592.pdf` was checked against the live
record and is byte-identical — 612 719 bytes, md5 `4d1e4d59…`, matching the
record's own checksum field — so a hand re-upload could not alter the paper.

The ruling had two consequences the form sheet had not accounted for.

**The record title should probably now stay unchanged.** Options A and B were
written for a notice-only record, where the title had to announce the erratum or
the record would misdescribe itself. With the paper retained, the companion's
title still describes the record accurately, and leaving it byte-identical to
v1.2 means citations resolve to a record titled as cited. Added as **Option C**
and recommended; A remains defensible if the erratum should be visible in search.

This also exposed a conflation in the sheet's own pre-publish table, which
required the form title to match the notice's H1. The **record** title and the
**document** H1 are different objects. The notice's H1 reads as a correction
notice whichever record title is chosen. Row corrected.

**The notice's filename begins `DRAFT-`, and Zenodo publishes the filename you
upload.** Sixth instance of author-addressed scaffolding inside the deposited
object, and the first that is not text at all — no scan over file *contents*
could have found it, because the defect is in the name. A copy renamed
`vquad_resurgence_v1.3_correction_notice.md` is staged under `upload/` and
verified byte-identical to the notice, `c936662f…`.
