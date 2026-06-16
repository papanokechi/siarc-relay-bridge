# Bundle archive info — VQUAD-REPRO-BUNDLE-002 run-2 (Stage 4)

**Date:** 2026-06-16 (Asia/Tokyo)
**Packager:** `run-2/_package_bundle.py` (slot, not shipped in bundle)
**Archive:** `run-2/vquad-periodrep-bundle.zip`

---

## New archive pin (supersedes `8752d7c7…`)

| field | value |
|-------|-------|
| **SHA-256** | `7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013` |
| **MD5** | `c1b5a39c0b56576e81b5c5723935669f` |
| **size** | 776968 bytes (758.8 KiB) |
| **entries** | 40 |
| **top-level dir** | `vquad-periodrep-bundle/` (single) |
| **embedded paper PDF** | `33f339ed…` (773171 B) — re-hashed from inside the zip, MATCH |
| **testzip** | OK (no bad entries) |
| **stable on re-pack** | yes (identical SHA-256 on a second packaging run) |

**Supersedes:** the run-1 archive `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb`
(721715 B), which embedded the pre-layout-fix `4ca12a35…` PDF. This is the archive
**VQUAD-ZENODO-READY-001 run-3** will pin.

The size grew by 55,253 B (721715 → 776968) entirely because the layout-fixed PDF is larger
(714771 → 773171 B); `scripts/`, `data/`, `LICENSE`, structure and file count are unchanged.

## Packaging properties (deterministic)

- forward-slash entry names (portable: Linux / macOS / Zenodo unzip cleanly)
- single top-level directory `vquad-periodrep-bundle/`
- entries sorted lexicographically (stable ordering)
- `__pycache__`, `*.pyc`, and LaTeX aux (`.aux/.log/.out/.toc/.fls/.fdb_latexmk`) excluded —
  no stray byproducts
- re-packing the unchanged tree yields a byte-identical archive (verified: SHA-256 stable)

## Directory listing (40 entries)

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

## Scenario B

The bundle zip rides as a **secondary file** in the paper's single Zenodo deposit; there is
**no separate bundle DOI**. The deposit will carry the layout-fixed paper PDF (`33f339ed…`)
plus this archive (`7bc5d008…`) as one CC-BY-4.0 record.
