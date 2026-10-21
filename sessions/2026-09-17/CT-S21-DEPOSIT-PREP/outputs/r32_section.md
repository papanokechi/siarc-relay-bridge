
---

## R32 — the related-identifier row that should not be added

Operator's instruction for the form said to add `10.5281/zenodo.20481592` as
*is supplemented by*; this sheet said *is supplement to*. Checking the direction
showed the row should not be added at all, and that the disagreement about which
way it points was the symptom rather than the problem.

Read back from the live v1.2 record:

- `related_identifiers` holds exactly one row, `10.5281/zenodo.20173773` /
  *references*. It contains **no** row for v1.1 (`20480603`), v1.0
  (`20455090`) or the concept DOI. The existing versions do not hand-link each
  other.
- Version linkage is maintained by Zenodo elsewhere:
  `metadata.relations.version = [{"index": 2, "is_last": true, "parent":
  {"pid_value": "20455089"}}]`.

So with the paper retained (§R31), v1.3 is a **version** of the work, not a
supplement to its own predecessor. Adding either direction would mislabel the
lineage in exchange for something Zenodo already records. DataCite has no
`corrects` relation, so there is no honest row to add even if one were wanted;
the correction is carried by the version string, the description and the notice
file.

This supersedes my own earlier advice in `DEPOSIT-FORM.md`, which was written
for the notice-only shape and not revisited when §R31 changed that shape —
guidance that was correct under an assumption and not re-derived when the
assumption moved. Two dependent spots were stale with it: the sheet's
pre-publish diff row ("the two DOIs in A3") and A3's own paragraph in the
walkthrough. Both corrected.

That makes three documents in two rounds carrying a consequence of a superseded
decision — the same shape as the stale hash and the stale status header, but at
the level of *reasoning* rather than a value: when a decision is overruled, what
was derived from it does not update itself.
