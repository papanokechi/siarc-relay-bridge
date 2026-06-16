# Stage 3 — Docs update record (BUNDLE-002)

All DOIs below are sourced from the authoritative
`VQUAD-ZENODO-PREP-001/related-identifiers.md` (itself line-cited to the corpus
`sakai-stratification/related_identifiers.md` + `submission_log.txt`), **never
from memory**, and match the corrections-final paper's bibliography.

## DOI resolutions used (from related-identifiers.md)

| Ref | Stale value (BUNDLE-001) | Corrected (concept) DOI | related-identifiers.md cite |
|---|---|---|---|
| V_quad companion | `20455090` (retracted v1.0) | **`10.5281/zenodo.20455089`** | F-DOI-1 / table L47, L100 |
| δ Fredholm cross-check | `20624814` (version) | **`10.5281/zenodo.20624813`** | F-DOI-4 / table L68, L106 |
| Sakai-stratification program | "to be inserted… not yet minted" | **`10.5281/zenodo.20694840`** | table L48 |
| Stokes calibration | `20481592` (already correct) | `10.5281/zenodo.20481592` (v1.2) | L47 (same concept 20455089) |

## Files changed

### `README.md`
- **Page count.** `(23 pp)` → `(24 pp)` (corrections-final paper is 24 pp).
- **Companion DOI.** "(Zenodo 10.5281/zenodo.20455090) and the … Stokes
  calibration (Zenodo 10.5281/zenodo.20481592)" →
  "(Zenodo, concept DOI 10.5281/zenodo.20455089) and the … Stokes calibration
  (Zenodo 10.5281/zenodo.20481592, version 1.2)". Retracted `20455090` removed.

### `docs/SIARC_PROVENANCE.md`
- **Provenance chain.** Replaced the single *pending* `VQUAD-PAPER-CORRECTIONS-001`
  row with two COMPLETE rows: **VQUAD-COLDREAD-001** (Verdict A, commit `e207b33`)
  and **VQUAD-PAPER-CORRECTIONS-001** (COMPLETE, commit `d4fc87a`, PDF `4ca12a35…`,
  24 pp). Both carry the standard slot + `claims.jsonl` BRIDGE URLs.
- **Honesty note → Provenance note.** Rewrote the "corrections slot does not yet
  exist / cold-read unrecorded" disclaimer to state the bundle is now built
  against the corrections-final paper (cold-read + corrections landed, H-1
  operator-verified) and **supersedes** the BUNDLE-001 preview.
- **Parent deposits.** Companion headline DOI `20455090`→ concept `20455089`
  (retracted v1.0 dropped; the literal retracted digits are not printed anywhere).
  Stokes line annotated "(version 1.2; same concept 20455089)". δ-Fredholm
  `20624814`→ concept `20624813`. Sakai program "to be inserted" → resolved
  concept `20694840`.
- **Personal communication.** `C. Marchal` → **`O. Marchal`**; reframed as an
  acknowledgement (not a load-bearing §2 citation), consistent with the
  corrections-final paper's Acknowledgements + its three published Marchal
  topological-recursion references.

### `docs/CONVENTIONS.md`
- §2 normalisation attribution: `(personal communication, C. Marchal, June 2026;
  cited in §2)` → `(after O. Marchal; cf. §2 and the paper's Acknowledgements,
  June 2026)`. The convention itself (`L_{1,2}=x²+⅓x+⅓`) is **unchanged**; only
  the misattributed initial and the over-stated "cited in §2" were corrected.

## Unchanged docs (verified)
- `docs/REPRODUCIBILITY.md` — references the PDF hash only indirectly ("recorded
  in the bundle's integrity-verification record"); carries no literal hash, no
  retracted DOI, no page count. **No edit.**
- `docs/DEPENDENCIES.md` — environment of record only; no hash/DOI. **No edit.**
- per-dir `README.md` ×4 — script descriptions only. **No edit.**

## Stage 3.2 scan result
Whole-bundle scan (`.md/.tex/.py/.json/.txt`) for `20455090`, `20624814`,
`C. Marchal` → **NONE** (clean). Embedded `paper/*.pdf` binary scan for
`20455090` → not present. Corrected values present: `20455089` ×5, `20624813`
×2, `20694840` ×2, `O. Marchal` ×3.
