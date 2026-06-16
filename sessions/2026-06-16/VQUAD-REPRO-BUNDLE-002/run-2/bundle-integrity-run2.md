# Bundle integrity — VQUAD-REPRO-BUNDLE-002 run-2 (Stage 3 HALT GATE)

**Date:** 2026-06-16 (Asia/Tokyo)
**Bundle root:** `run-2/vquad-periodrep-bundle/`
**Harness:** `run-2/verify_bundle.py` (slot, not shipped in bundle)
**Supersedes:** the run-1 verification (`a33ff59`, PDF `4ca12a35…`).

This record satisfies the Stage-3 HALT GATE: every essential script executes without error
and reproduces its reference output, and the paper compiles clean and reproduces the
**layout-fixed** PDF hash byte-for-byte. The layout fix was proven reflow-only upstream
(LAYOUTFIX-001), so constants are **not** re-reviewed here — but script integrity and PDF
reproduction ARE re-run, as the brief requires.

---

## 1. Script execution + output comparison

Each script is run from its own bundle directory with a fresh interpreter; its emitted JSON
is compared against the reference in `data/`, ignoring only documented volatile fields
(timestamps, wall-clock runtimes).

| # | script | dir | exit | compare to `data/` |
|---|--------|-----|------|--------------------|
| 1 | holonomic_recognition_q3.py | 01-algebraicity | ok | exact |
| 2 | extract_verify_operators.py | 01-algebraicity | ok | exact |
| 3 | indicial_analysis.py | 01-algebraicity | ok | exact |
| 4 | borel_pade_census.py | 01-algebraicity | ok | exact |
| 5 | stage2_kovacic.py | 02-galois | ok | — (stdout only) |
| 6 | stage2b_symsquare.py | 02-galois | ok | exact |
| 7 | stage3_galois_LV.py | 02-galois | ok | exact |
| 8 | stage3b_frobenius_v2.py | 02-galois | ok | exact |
| 9 | numcheck_period_rep.py | 03-verification | ok | match (modulo volatile) |
| 10 | stage4a_methodA_v2.py | 03-verification | ok | exact |
| 11 | stage4_methods.py | 03-verification | ok | exact |
| 12 | stage0_residual_check.py | 03-verification | ok | exact |
| 13 | stage1_hankel_period.py | 04-cycle | ok | exact |

**Result: ALL ESSENTIAL SCRIPTS PASS — True** (13 run, exit 0; 11 exact, 1
match-modulo-volatile, 1 stdout-only). **Identical pattern to run-1 (`a33ff59`)** — expected,
because `scripts/` and `data/` are byte-identical to the run-1 bundle (the layout fix touched
only the paper). `q3_foundation.py` is the support module imported by
`stage0_residual_check.py` (byte-identical to `holonomic_recognition_q3.py`), exercised
transitively.

### Volatile-field note (script 9)
`numcheck_period_rep_results.json` carries `generated_utc` / `runtime_seconds` (change every
run); the harness strips `generated|utc|runtime|seconds` before comparison. All 46-digit
numerical content is an exact match.

---

## 2. Paper compilation + byte-reproducibility (layout-fixed)

- **Builder:** `paper/build.py` (bundle-specific; compiles the self-contained
  `paper/vquad-periodrep-paper.tex` directly — `pdflatex` ×2, PATH→MiKTeX fallback,
  `SOURCE_DATE_EPOCH=1718409600`). Reproducibility target refreshed to the layout-fixed pin.
- **Run from `paper/`:** `PAGES=24`, `ERRORS=0`, `PDF_EXISTS=True`.
- **SHA-256 (rebuilt):** `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea`
- **Target (layout-fixed, VQUAD-PAPER-LAYOUTFIX-001):**
  `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea`
- **REPRODUCIBLE = True** (773171 bytes, 24 pp). Independently re-confirmed by a build in a
  **pristine temp directory** (only `.tex` + `preamble.tex` + `build.py` copied): identical
  hash `33f339ed…`.

---

## 3. Embedded-PDF re-hash + scripts-clean

- After the harness regenerated each result JSON next to its script, those 12 regenerated
  copies and `__pycache__` were **removed** so `scripts/0X-*/` ship clean (`.py` + `README.md`
  only); bundle file count restored to **40**.
- The PDF embedded in the assembled bundle (and in the packaged archive) re-hashes to
  `33f339ed…` (773171 B) — matching the LAYOUTFIX-001 pin exactly (see archive-info Stage 4).

---

## 4. Retracted-DOI / old-hash scan

Whole-bundle scan: retracted `20455090` → **NONE**; superseded `4ca12a35` / `714771` /
`028a1a5d` → **NONE**. Concept `20455089` present. (Unchanged from run-1: the layout fix
touched no references.)

---

## 5. Gate disposition

**STAGE-3 HALT GATE: PASS.** No script failed; the one volatile case is documented; the paper
compiles clean and reproduces the layout-fixed PDF hash (in-place + pristine temp dir); the
retracted DOI and the superseded hash are both absent. The bundle is internally complete and
was packaged in Stage 4.
