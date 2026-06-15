# Bundle archive info — VQUAD-REPRO-BUNDLE-001 (Stage 6)

**Built:** 2026-06-16 (Asia/Tokyo) via `_package_bundle.py` (slot root, auditable).

| field | value |
|-------|-------|
| **Archive** | `vquad-periodrep-bundle.zip` (slot root) |
| **Format** | standard ZIP (Deflate); forward-slash entry names; single top-level dir `vquad-periodrep-bundle/` |
| **SHA-256** | `e7eff5c85de1a495165730742772ec0a0eac6aa58f46bb210ce4c37bf43d3432` |
| **Size** | 708568 bytes (692.0 KiB) |
| **File count** | 40 |

## Cross-platform / integrity checks (Stage 6.1)

- `zipfile.testzip()` → `None` (no CRC errors).
- All 40 entries use **forward-slash** separators → extract cleanly on
  Linux / macOS / Zenodo (Windows `Compress-Archive` was deliberately avoided
  because PowerShell 5.1 can emit backslash separators that corrupt names on
  non-Windows extraction).
- All entries live under a single top-level directory `vquad-periodrep-bundle/`
  → tidy extraction, no CWD litter.
- `__pycache__`, `*.pyc` and LaTeX aux files (`.aux/.log/.out/.toc/.synctex.gz`)
  excluded by the packager.
- Embedded `paper/vquad-periodrep-paper.pdf` re-hashed from inside the zip:
  `359d1172af3f867f4349cf4776a222813a855cd354bc78c0b68ccfb0026c702b`
  (698730 bytes) — **matches the deposited target exactly**.

## Composition (40 files)

| group | count | files |
|-------|-------|-------|
| top-level | 2 | `README.md`, `LICENSE` (CC BY 4.0) |
| `paper/` | 4 | `vquad-periodrep-paper.pdf`, `vquad-periodrep-paper.tex`, `preamble.tex`, `build.py` |
| `scripts/` | 18 | 14 `.py` (13 runnable + 1 support module `q3_foundation.py`) + 4 per-dir `README.md` |
| `data/` | 12 | reference `*_results.json` |
| `docs/` | 4 | `REPRODUCIBILITY.md`, `DEPENDENCIES.md`, `SIARC_PROVENANCE.md`, `CONVENTIONS.md` |

### scripts/ breakdown
- `01-algebraicity/` — 4 `.py` + README (holonomic recognition over ℚ(√3))
- `02-galois/` — 4 `.py` + README (Kovacic L_φ=SL2; L_V structure)
- `03-verification/` — 5 `.py` (incl. support `q3_foundation.py`) + README (Methods A/B/C)
- `04-cycle/` — 1 `.py` + README (Hankel rapid-decay cycle)

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

The ZIP's own SHA-256 is **not** claimed byte-reproducible across rebuilds: ZIP
entries embed per-file modification times, which vary by checkout. The
reproducible artifact is the **PDF** (hash above) and the script outputs (each
`data/*.json`). The ZIP SHA-256 recorded here pins *this* built archive for the
Zenodo metadata; regenerating the archive will change its hash but not its
contents. For a byte-reproducible re-pack, set all entry mtimes to a fixed epoch
before zipping.
