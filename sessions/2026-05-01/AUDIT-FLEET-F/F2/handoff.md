# Fleet-F · F2 — DOI / Zenodo Metadata Audit

**Status:** completed (read-only audit)

## Verdict

**MEDIUM** — three reflexivity / staleness issues; no broken DOIs.

## Stats

- DOIs checked: 11 (all HTTP 200)
- Reflexivity edges checked: 3
- Submission-log integrity: no gaps or monotonicity issues in the sampled rows
- arXiv presence: no mirror evidence in scanned artifacts (INFO)

## Findings

### MEDIUM

- **F2-M1 (reflexivity gap)** — `PCF2-V12-RELEASE/zenodo_description_v1.2.txt:32-33`
  declares `IsSupplementedBy 10.5281/zenodo.19941678` (Channel Theory v1.1
  concept), but `CHANNEL-THEORY-V12/zenodo_description_v1.2.txt:9` still
  describes itself as supplementing **PCF-2 v1.1**
  (`10.5281/zenodo.19939463`), not v1.2 (`19951458`). The two papers no longer
  point at each other's current versions.
- **F2-M2 (stale citation)** — `CHANNEL-THEORY-V11/zenodo_description_v1.1.txt:9`
  still cites `PCF-2 v1.1 (10.5281/zenodo.19939463)` even though v1.2 supersedes
  it. (Acceptable for the v1.1 record itself, but should be flagged in the
  reflexivity table.)
- **F2-M3 (stale citation in v1.2 source)** —
  `CHANNEL-THEORY-V12/zenodo_description_v1.2.txt:9` still references PCF-2
  v1.1 (`19939463`) inside the v1.2 description body, and
  `PCF2-V12-RELEASE/zenodo_description_v1.2.txt:43` still lists `PCF-2 v1.1
  (10.5281/zenodo.19939463)` as the `isNewVersionOf` predecessor. The
  predecessor is structurally correct (v1.2 _is_ a new version of v1.1), but
  any reader reading the description prose alongside the metadata will see two
  different "current" PCF-2 references.

### LOW / INFO

- **F2-L1** — Concept/version DOI usage is otherwise consistent across the
  scanned artifacts.
- **F2-I1** — No arXiv mirrors found for any of the 4 published Zenodo records
  (`19885550`, `19937196`, `19951458`, `19951331`).

## DOIs verified (HTTP 200)

`19885550`, `19934553`, `19937196`, `19936297`, `19951458`, `19941678`,
`19951331`, `19939463`, `19941679`, `19915689`, `19783312`.

## Recommendation

Fix in any future Channel-Theory-V13 release:

1. Replace prose-level citation in `zenodo_description_v1.2.txt:9` with PCF-2
   v1.2 (`19951458`).
2. When PCF2-V13 publishes, update the `IsSupplementedBy` target on the Channel
   Theory record (and re-version Channel Theory if the relationship changes
   substantively).
