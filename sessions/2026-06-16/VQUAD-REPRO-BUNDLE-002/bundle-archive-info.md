# Bundle archive info — VQUAD-REPRO-BUNDLE-002 (Stage 5)

**Built:** 2026-06-16 (Asia/Tokyo) via `_package_bundle.py` (slot root, auditable).
**Supersedes:** VQUAD-REPRO-BUNDLE-001 archive (preview;
`e7eff5c8…`, 708568 B) — rebuilt against the corrections-final paper.

| field | value |
|-------|-------|
| **Archive** | `vquad-periodrep-bundle.zip` (slot root) |
| **Format** | standard ZIP (Deflate); forward-slash entry names; single top-level dir `vquad-periodrep-bundle/` |
| **SHA-256** | `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb` |
| **Size** | 721715 bytes (704.8 KiB) |
| **File count** | 40 |

## Cross-platform / integrity checks (Stage 5.1)

- `zipfile.testzip()` → `None` (no CRC errors).
- All 40 entries use **forward-slash** separators (`ALL_FORWARD_SLASH=True`) →
  extract cleanly on Linux / macOS / Zenodo.
- All entries live under a single top-level dir `vquad-periodrep-bundle/`
  (`SINGLE_TOPDIR=True`).
- `__pycache__`, `*.pyc`, regenerated `scripts/**/*.json`, and LaTeX aux files
  excluded (`STRAY_BYPRODUCTS=[]`): scripts/ ship **clean** (`.py` + `README.md`).
- Embedded `paper/vquad-periodrep-paper.pdf` re-hashed from inside the zip:
  `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe`
  (714771 bytes) — **matches the corrections-final target exactly**.

## Composition (40 files — unchanged structure vs BUNDLE-001)

| group | count | files |
|-------|-------|-------|
| top-level | 2 | `README.md`, `LICENSE` (CC BY 4.0) |
| `paper/` | 4 | `vquad-periodrep-paper.pdf` (corrections-final), `vquad-periodrep-paper.tex`, `preamble.tex`, `build.py` |
| `scripts/` | 18 | 14 `.py` (13 runnable + 1 support module `q3_foundation.py`) + 4 per-dir `README.md` |
| `data/` | 12 | reference `*_results.json` |
| `docs/` | 4 | `REPRODUCIBILITY.md`, `DEPENDENCIES.md`, `SIARC_PROVENANCE.md`, `CONVENTIONS.md` |

### File-count delta vs BUNDLE-001
**0** — identical 40-entry structure. Only **content** changed: the `paper/`
PDF+`.tex` (corrections-final) and three docs (`README.md`, `SIARC_PROVENANCE.md`,
`CONVENTIONS.md`) + `paper/build.py` target SHA. Size grew 708568 → 721715 B
(+13147 B) because the corrected PDF is 714771 B vs the preview's 698730 B (+16041 B).

## Directory listing (archive order)

```
vquad-periodrep-bundle/LICENSE
vquad-periodrep-bundle/README.md
vquad-periodrep-bundle/data/borel_pade_results.json
vquad-periodrep-bundle/data/holonomic_recognition_q3_results.json
vquad-periodrep-bundle/data/indicial_results.json
vquad-periodrep-bundle/data/numcheck_period_rep_results.json
vquad-periodrep-bundle/data/operator_verification_results.json
vquad-periodrep-bundle/data/stage0_residual_results.json
vquad-periodrep-bundle/data/stage1_hankel_results.json
vquad-periodrep-bundle/data/stage2_kovacic_results.json
vquad-periodrep-bundle/data/stage3_galois_LV_results.json
vquad-periodrep-bundle/data/stage3b_frobenius_results.json
vquad-periodrep-bundle/data/stage4_methodA_results.json
vquad-periodrep-bundle/data/stage4_methods_results.json
vquad-periodrep-bundle/docs/CONVENTIONS.md
vquad-periodrep-bundle/docs/DEPENDENCIES.md
vquad-periodrep-bundle/docs/REPRODUCIBILITY.md
vquad-periodrep-bundle/docs/SIARC_PROVENANCE.md
vquad-periodrep-bundle/paper/build.py
vquad-periodrep-bundle/paper/preamble.tex
vquad-periodrep-bundle/paper/vquad-periodrep-paper.pdf
vquad-periodrep-bundle/paper/vquad-periodrep-paper.tex
vquad-periodrep-bundle/scripts/01-algebraicity/README.md
vquad-periodrep-bundle/scripts/01-algebraicity/borel_pade_census.py
vquad-periodrep-bundle/scripts/01-algebraicity/extract_verify_operators.py
vquad-periodrep-bundle/scripts/01-algebraicity/holonomic_recognition_q3.py
vquad-periodrep-bundle/scripts/01-algebraicity/indicial_analysis.py
vquad-periodrep-bundle/scripts/02-galois/README.md
vquad-periodrep-bundle/scripts/02-galois/stage2_kovacic.py
vquad-periodrep-bundle/scripts/02-galois/stage2b_symsquare.py
vquad-periodrep-bundle/scripts/02-galois/stage3_galois_LV.py
vquad-periodrep-bundle/scripts/02-galois/stage3b_frobenius_v2.py
vquad-periodrep-bundle/scripts/03-verification/README.md
vquad-periodrep-bundle/scripts/03-verification/numcheck_period_rep.py
vquad-periodrep-bundle/scripts/03-verification/q3_foundation.py
vquad-periodrep-bundle/scripts/03-verification/stage0_residual_check.py
vquad-periodrep-bundle/scripts/03-verification/stage4_methods.py
vquad-periodrep-bundle/scripts/03-verification/stage4a_methodA_v2.py
vquad-periodrep-bundle/scripts/04-cycle/README.md
vquad-periodrep-bundle/scripts/04-cycle/stage1_hankel_period.py
```

## Note on zip reproducibility

The ZIP's own SHA-256 is **not** claimed byte-reproducible across rebuilds (ZIP
entries embed per-file mtimes). The reproducible artifact is the **PDF** (hash
above) and the script outputs (each `data/*.json`). The ZIP SHA-256 recorded here
pins *this* built archive for the Zenodo metadata. Scenario B: this zip rides as a
**secondary file** in the paper's single deposit — **no separate bundle DOI**.
