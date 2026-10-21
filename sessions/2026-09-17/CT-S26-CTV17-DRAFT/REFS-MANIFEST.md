# `refs/` manifest — Channel Theory version records

Fetched 2026-09-19 in session `CT-S26-CTV17-DRAFT`. All are the operator's own
CC-BY-4.0 deposits. Bytes and sha256 are read **from disk**, not from any
in-memory string.

## Files held

| File | Bytes | sha256 |
|---|---|---|
| `zenodo_22782807.json` | 31957 | `cacfb91d913eb95385c97a9e1a56898c3ee7225e21c54aec09d97b622528a737` |
| `zenodo_22782807.description.txt` | 22704 | `82d51c5375754b0220475a393d517815266cdd7529433b4e2b7a1cbb0bbb596b` |
| `zenodo_22717792.json` | 24503 | `fe6ca2f17f0dbe94db5b3d69f4e0d8c92249e5854381e32e7beb0ba74361df64` |
| `zenodo_22717792.description.txt` | 14925 | `0898719bf793867add756a64cbacc2e621588f9a0df91eb24e82905eb6a50c20` |
| `zenodo_v15_doi.json` | 25448 | `48707d28ad8d376a622ba7cd18810c8d3c6986b50d6591e03a6b128fff6cb736` |
| `datacite_concept.json` | 69555 | `22978f14678ec8f8ca9d58f3e8117ca6a12d083a5ddb7e2ae6a77905ecd1aeb3` |
| `datacite_20585624.json` | 40125 | `58ba35aa4bc8a5d58d0e5e67373ca4468f7501ea99d761b49241911f74bf060a` |
| `datacite_20585624.description.txt` | 6018 | `dd37d2a8ce9dcdfa6d9e06f7ff0b98a557d80d5a9e59fd0775f0f7965dfc00ca` |
| `datacite_19972394.json` | 38950 | `0c11834472245807b98628e5b260496177ef66763f46e416c8c7396b50685cf7` |
| `datacite_19972394.description.txt` | 5872 | `d278d5fa9cfaf6acf36fc0f98f4d0470c25aab8454db330c357e7c9d2e2e7921` |

## The version map, read from live records

| Version | Version DOI | Published | Source file |
|---|---|---|---|
| v1.1 | `10.5281/zenodo.19941679` | — | `datacite_concept.json` (`HasVersion`) |
| v1.2 | `10.5281/zenodo.19951331` | — | `datacite_concept.json` (`HasVersion`) |
| v1.3 | `10.5281/zenodo.19972394` | 2026-05-02 | `datacite_19972394.json` (`version: '1.3'`) |
| v1.4 | `10.5281/zenodo.20585624` | 2026-06-07 | `datacite_20585624.json` (`version: '1.4'`) |
| v1.5 | `10.5281/zenodo.22717792` | 2026-09-12 | `zenodo_22717792.json` (`metadata.version`) |
| v1.6 | `10.5281/zenodo.22782807` | 2026-09-16 | `zenodo_22782807.json` (`metadata.version`) |
| concept | `10.5281/zenodo.19941678` | — | `conceptdoi` on both Zenodo records; DataCite reports current version `1.6` |

DataCite lists exactly **six** `HasVersion` identifiers for the concept DOI. **No
v1.0 version DOI appears among them**; that is reported as read, not explained.
The concept DOI was taken from the `conceptdoi` field, never from a record number.

## NOT obtained

| Item | Expected | Why not |
|---|---|---|
| v1.6 `channel_theory_outline.pdf` | 609300 B, md5 `aa56a94a9354b5533b04c89461950eb1` | HTTP **504** on `api/records/…/files/…/content` and on `records/…/files/…?download=1`, retried 2026-09-19 |
| v1.5 `channel_theory_outline.pdf` | 620544 B, md5 `a197906025f6428173f30b2c912a5dc4` | HTTP **504**, same two endpoints, same retry |

The expected sizes and md5s above are **read from the records' own `files[]`
entries**, not from the files, which are not held. Consequence: **§9 of the v1.5
and v1.6 PDFs — the open-problems section carrying the falsifier statements and
their numeric thresholds — has not been read**, and no falsifier text is quoted
anywhere in `NOTICE-v1.7.md`.

## API behaviour, for the next session

* `https://zenodo.org/api/records/<ID>` returns the **legacy** shape here:
  top-level `doi` / `conceptdoi`, `metadata.license.id`, and `files` as a **list**
  of `{key, size, checksum}` — *not* the RDM shape (`pids.doi.identifier`,
  `parent.pids.doi.identifier`, `files.entries`). `scripts/read_zenodo.py` handles
  both and asserts on neither being present.
* Two record GETs succeeded; then the search endpoint, `/versions`, both file
  routes and five further record GETs all returned 504 with a 92-byte HTML body.
  **Those bodies were deleted rather than left on disk**, so that nothing in
  `refs/` looks like a fetch that was not one.
* `https://api.datacite.org/dois/<DOI>` answered throughout and carries
  `attributes.version`, `attributes.dates`, `attributes.relatedIdentifiers` and
  `attributes.descriptions` — enough to fill the erratum stack without
  `zenodo.org`.
* DataCite returns a **single** description; Zenodo carries the full HTML. The
  v1.3 and v1.4 texts here may therefore be partial. The v1.4 notice is in any
  case retained verbatim inside the v1.6 description, and that is the copy used.
