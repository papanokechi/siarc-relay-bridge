# Stage 3 — Metadata anchor refresh (re-run / run-2)

**New metadata anchor (whole-file SHA-256 of `zenodo_metadata.md`):**

```
4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895
```
supersedes the PREP-001 provisional `dee9195c7957f25fc57f497d6875cdd2b63d97d24f55f36b5e54e388ec003eb8`.

## How it was produced

`_finalize_metadata.py` (in this slot, re-runnable, `__file__`-relative to PREP-001)
reads the PREP-001 `zenodo_metadata.md` byte-for-byte (CRLF / UTF-8 preserved) and
applies exactly the changes below, then re-emits and prints the anchor. No field
other than those listed is touched.

| edit | what | source |
|------|------|--------|
| R1 | description (markdown body) — insert L-3 clause | corrections-final abstract |
| R2 | description (JSON `"description"`) — same L-3 clause | corrections-final abstract |
| R3 | creators `"affiliation"` = "Independent Researcher, Yokohama, Japan" | F-AFFIL Option C (operator) |
| R5 | banner `_affiliation_decision` → RESOLVED | F-AFFIL Option C (operator) |
| R6 | `_related_identifiers_pointer` → "11 ids; Scenario B — isSupplementTo dropped" | Scenario B (operator); was "12 ids; placeholder" |
| — | table row + finalization banner (provenance bookkeeping) | this run |

**L-3 clause (verbatim, both copies):** after "holonomic of order 4", insert
"(the Borel–Laplace dual of the order-2 operator annihilating the series)".

## Pinned-against (corrections-final, cold-read-certified)

- **Abstract:** corrections-final verbatim (only the L-3 clause differs from PREP-001).
- **Affiliation:** "Independent Researcher, Yokohama, Japan" (Option C).
- **Title:** *An explicit exponential-period representation of the V_quad
  connection coefficient* (unchanged).
- **Keywords (8):** unchanged from PREP-001.
- **MSC:** 34M55 (primary); 11J81, 34E20, 14F40, 33C20, 37K10 (unchanged).
- **Version:** 1.0.0. **Companion** cited at **concept** DOI `10.5281/zenodo.20455089`
  (retracted v1.0 `20455090` never present).
- **§6 framing:** unchanged — cold-read confirmed corrections did not shift the
  doubly-conditional G-MOTGALOIS heuristic.

## Verification

- `python _finalize_metadata.py` → printed anchor `4a75234f…`.
- JSON block parses; `description` length 1539 → 1612 chars (the inserted clause);
  affiliation present; title / version / 8 keywords intact.
- Rendered `zenodo_metadata.md` inspected: banner RESOLVED, no `{{…}}` placeholders.
