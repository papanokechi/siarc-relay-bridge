# Stage 4 — Bundle archive pin refresh (run-3)

**New bundle archive pin (supersedes run-2's `8752d7c7…`):**

| field | value |
|-------|-------|
| archive | `vquad-periodrep-bundle.zip` |
| **SHA-256** | `7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013` |
| **MD5** | `c1b5a39c0b56576e81b5c5723935669f` |
| size | 776968 bytes |
| entries | 40 |
| embedded paper PDF | `33f339ed…` (re-hashed from inside the zip) |

**Source:** `VQUAD-REPRO-BUNDLE-002` run-2 (`56a1402`). The re-pinned bundle swapped the
clipped-digit `4ca12a35…` PDF for the layout-fixed `33f339ed…`; scripts/data are byte-identical
to the run-1 bundle (only paper + one provenance doc changed). Integrity PASS (13/13 scripts;
PDF reproduces `33f339ed…` in-place + pristine-temp).

## Scenario B — unchanged

- The bundle is a **secondary file** in the paper's **single** Zenodo deposit; there is **no
  separate bundle DOI**.
- `isSupplementTo` remains **dropped** (Scenario B); the related-identifiers array stays at
  **11** (2 continues + 1 isPartOf + 8 references + 0 isSupplementTo).
- The bundle hash change does **not** alter the related-identifiers: the bundle is not a
  related *work* — it rides as an uploaded file in the same record. Gate 1 is unaffected (see
  Stage 5).

## Size delta (informational)

776968 − 721715 = **+55,253 B**, attributable entirely to the larger layout-fixed PDF
(773171 − 714771 = +58,400 B in the paper, partly offset by compression). File count, scripts,
data, structure: unchanged.
