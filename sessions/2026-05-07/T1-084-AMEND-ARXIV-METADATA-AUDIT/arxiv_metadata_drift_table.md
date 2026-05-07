# arXiv Metadata-Persistence Drift Table — Phase D

**Relay:** 084-AMEND (T1; OPTION B follow-up onto landed 084)
**Date (JST):** 2026-05-07
**Bridge HEAD at fire time:** `dbe7a71`
**Substrate parent:** `sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/`
  - Anchor file: `zenodo_metadata_5_records.json`
  - Anchor SHA-256 (verbatim Zenodo API snapshot at 2026-05-04 fire time)

---

## Phase D.P1 + D.P3 — per-record arXiv current metadata

Audit performed 2026-05-07 ~20:30 JST. Each row records the live state of
the record on the arXiv side at audit time.

| # | Record | Zenodo version DOI | arXiv ID (current) | arXiv v1 date | arXiv vN date | arXiv title (canonical) | arXiv authors | arXiv abstract first 200 chars | arXiv MSC | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | SIARC umbrella v2.0 | `10.5281/zenodo.19965041` | _none_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | **PENDING_FIRST_SUBMISSION** |
| R2 | PCF-1 v1.3 | `10.5281/zenodo.19937196` | _none_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | **PENDING_FIRST_SUBMISSION** |
| R3 | PCF-2 v1.3 | `10.5281/zenodo.19963298` | _none_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | **PENDING_FIRST_SUBMISSION** |
| R4 | CT v1.3 | `10.5281/zenodo.19972394` | _none_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | **PENDING_FIRST_SUBMISSION** |
| R5 | T2B v3.0 | `10.5281/zenodo.19915689` | _none_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | **PENDING_FIRST_SUBMISSION** |

**Aggregate verdict:** 5 / 5 PENDING_FIRST_SUBMISSION. The 084 mirror runbook is a
pre-submission checklist; no own-record arXiv ID has been issued for any of the
five records. Phase D operates on a null-state arXiv side.

### Negative-state evidence (independent confirmations)

1. **084 substrate snapshot.** `zenodo_metadata_5_records.json` (5 rows) records
   the Zenodo `api_files` field for each record but contains no `arxiv_id` /
   `arXiv` / `arxiv.org/abs` field for any row (a `related_identifiers` arXiv
   entry would be the standard Zenodo ↔ arXiv cross-link signal; none present).
2. **submission_log.txt regex scan.** Pattern `arXiv:\s*\d{4}\.\d{4,5}` returns
   zero matches for own-record IDs across `tex/submitted/submission_log.txt`
   (the file's only `arXiv` substring is line 212 "Filename:
   pcf_unified_arxiv.pdf", a local PDF filename, not a published-record ID).
3. **Bridge handoff scan.** `arXiv:\d{4}\.\d{4,5}` patterns in
   `siarc-relay-bridge/sessions/**/handoff.md` resolve to external citations
   only: V1 = `arXiv:2307.11217` (Barhoumi-Lisovyy-Miller-Prokhorov 2024),
   V2 = `arXiv:1604.03082` (Its-Lisovyy-Prokhorov 2018), Witte-Forrester
   `arXiv:0911.1762` (lit-hunt anchor; cf. 031 verdict), Garoufalidis
   `arXiv:2412.04241` + `arXiv:1712.04887` (endorser papers from
   ENDORSER-HANDLE-ACQUISITION 2026-05-04), KNY 2017 `arXiv:1509.08186`. None
   are own-record IDs.
4. **Live arXiv author search.** `arxiv.org/search/?searchtype=author&query=papanokechi`
   returned literal text "Sorry, your query for author: papanokechi produced
   no results." at audit time.
5. **Live arXiv author endpoints.** `arxiv.org/a/papanokechi_s_1.html` and
   `arxiv.org/a/papanokechi_1.html` both return HTTP 404 at audit time
   (no public-author landing page exists).

These five independent signals jointly establish PENDING_FIRST_SUBMISSION
for all 5 records.

---

## Phase D.P2 — Zenodo ↔ arXiv crosswalk

Crosswalk is **N/A — VACUOUS** for the five records, since the arXiv side
is null. This subsection documents the *framework* that will activate the
moment the first own-record arXiv ID lands.

For each future-landed record, the crosswalk table will be:

| Field | Zenodo value (canonical) | arXiv value (live) | Drift |
|---|---|---|---|
| Title | (from Zenodo `metadata.title`) | (from arXiv abstract page `<title>`) | NONE / TITLE_DRIFT |
| Authors | (from Zenodo `metadata.creators[*].name`) | (from arXiv `<meta name="citation_author">`) | NONE / AUTHOR_DRIFT |
| Abstract first 200 chars (HTML-stripped, normalised whitespace) | (from Zenodo `metadata.description`) | (from arXiv abstract page `<blockquote class="abstract">`) | NONE / ABSTRACT_DRIFT |
| MSC subject classes | (from Zenodo `metadata.subjects` if present, else `metadata.keywords`) | (from arXiv `<meta name="citation_keywords">` and primary/cross-list categories) | NONE / MSC_DRIFT |
| DOI cross-link | (from Zenodo `metadata.related_identifiers[?relation=isAlternateIdentifier]`) | (from arXiv `<meta name="citation_doi">` if present) | NONE / CROSSLINK_DRIFT |

Drift triggers and dispositions are normative under the Phase D halt
register (§ HALT_084_AMEND_DRIFT_BLOCKING engages on drift across >2
records).

---

## Phase D — Zenodo metadata invariance spot-check (2 of 5 records)

To confirm that the 084 fire-time Zenodo snapshot remains stable for the
duration of the audit framework, two records were re-fetched live at
audit time and compared against the 084 snapshot:

| Record | Field | 084 snapshot value | 2026-05-07 live value | Match |
|---|---|---|---|---|
| R2 PCF-1 v1.3 | `id` | 19937196 | 19937196 | ✓ |
| R2 PCF-1 v1.3 | `metadata.version` | "1.3" | "1.3" | ✓ |
| R2 PCF-1 v1.3 | `metadata.title` | "Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions" | "Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions" | ✓ |
| R2 PCF-1 v1.3 | `files[0].size` | 392886 | 392886 | ✓ |
| R2 PCF-1 v1.3 | `files[0].checksum` | `md5:fbf5449b2678834b0204360d49aef5e0` | `md5:fbf5449b2678834b0204360d49aef5e0` | ✓ |
| R2 PCF-1 v1.3 | `modified` | (≤ 2026-05-04) | `2026-05-01T03:25:57.200363+00:00` | ✓ (no edit since deposit) |
| R3 PCF-2 v1.3 | `id` | 19963298 | 19963298 | ✓ |
| R3 PCF-2 v1.3 | `metadata.version` | "1.3" | "1.3" | ✓ |
| R3 PCF-2 v1.3 | `metadata.title` | "PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant Transcendence Predicate" | "PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant Transcendence Predicate" | ✓ |
| R3 PCF-2 v1.3 | `files[0].size` | 558153 | 558153 | ✓ |
| R3 PCF-2 v1.3 | `files[0].checksum` | `md5:cdd628911f3fd95cec8ed916c1958c51` | `md5:cdd628911f3fd95cec8ed916c1958c51` | ✓ |
| R3 PCF-2 v1.3 | `modified` | (≤ 2026-05-04) | `2026-05-02T00:03:55.887123+00:00` | ✓ (no edit since deposit) |

R2 and R3 are the two records that gate the math.NT endorsement chain
and are the most sensitive to template-side drift; both confirmed
hash-equal to the 084 snapshot at audit time.

R1, R4, R5 metadata not re-fetched (low-impact: math.HO + math-ph
endorsement chains are sequenced after R2 per 084 J6 recommendation;
no template was emitted for these in 084 Phase D).

---

## Phase D — Verdict

**Aggregate verdict:** `COMPLETE_AUDIT_CLEAN_VACUOUS_NO_ARXIV_IDS_TO_AUDIT`.

This is a sub-classification of the spec's `COMPLETE_AUDIT_CLEAN`
outcome: 0 records have arXiv IDs, so 0 records can exhibit drift,
so the audit is structurally CLEAN by null-state. The persistence
framework is now in place and re-fires the moment the first own-record
arXiv ID lands (forward-pointer captured in Phase H Recommended-Next-Step).

**Halts triggered:** 0 of 3 (HALT_084_AMEND_ARXIV_FETCH_FAIL +
HALT_084_AMEND_ID_HALLUCINATED + HALT_084_AMEND_DRIFT_BLOCKING all PASS).

**Post-031 pre-verification:** N/A_VACUOUS (no own-record arXiv IDs in
substrate to verify; rule remains armed for future-landed IDs and is
forward-pointed to the next 084-AMEND re-fire).

---

## Forward-pointer: re-fire conditions

The next 084-AMEND fire is not gated on calendar; it is gated on
**any of**:
1. First own-record arXiv ID lands (operator notifies via CMB.txt
   PORTFOLIO STATUS or VENUE STATUS row, OR via a substrate file in
   the bridge such as `submission_log.txt` Items 26+).
2. arXiv moderator email lands requesting metadata change to a
   landed record (operator forwards the email body to the bridge).
3. arXiv version-bump (vN → vN+1) on any landed record (announces
   itself via the arXiv abstract page `<meta name="citation_arxiv_id">`
   and date).

At any of those triggers, this audit re-runs in **OPTION A** mode
(full PHASE A/B/C/D/E end-to-end on all 5 records, with the now-non-
empty arXiv side actually populated).

Until then, the audit framework remains in null-state CLEAN.
