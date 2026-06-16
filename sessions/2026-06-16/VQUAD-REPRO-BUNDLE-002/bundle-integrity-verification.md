# Bundle integrity verification — VQUAD-REPRO-BUNDLE-002 (Stage 4)

**Timestamp:** 2026-06-16 (Asia/Tokyo)
**Bundle root:** `vquad-periodrep-bundle/`
**Harness:** `verify_bundle.py` (slot root, not shipped in bundle)
**Supersedes:** the BUNDLE-001 preview verification (PDF `359d1172…`).

This record satisfies the Stage-4 HALT GATE: every essential script executes
without error and every output matches the reference data in `data/` (modulo
documented volatile fields); the paper compiles clean and reproduces the
**corrections-final** PDF hash byte-for-byte.

---

## 1. Script execution + output comparison

Each script is run **from its own bundle directory** with a fresh interpreter.
Its emitted JSON is compared against the reference in `data/`, ignoring only
documented volatile fields (timestamps, wall-clock runtimes).

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
match-modulo-volatile, 1 stdout-only). **Identical pattern to BUNDLE-001** — the
corrections changed no script logic and no numerical result, as expected
(corrections were expository / bibliographic / terminological; see
VQUAD-PAPER-CORRECTIONS-001 `verification-pass.md`).

`q3_foundation.py` (03-verification) is a **support module** imported by
`stage0_residual_check.py`; byte-identical to
`01-algebraicity/holonomic_recognition_q3.py`, exercised transitively.

### Volatile-field note (script 9)
`numcheck_period_rep_results.json` carries `generated_utc` and `runtime_seconds`
(change every run); the harness strips `generated|utc|runtime|seconds` before
comparison. All 46-digit numerical content is an exact match.

---

## 2. No-absolute-path confirmation

The shipped `.py` are taken **verbatim** from the integrity-verified BUNDLE-001
tree (already path-relativized to `os.path.dirname(os.path.abspath(__file__))`,
UTF-8-guarded, and carrying the `stage4_methods.py` +1/z Borel-sum convention
patch). The clean harness run above — each script finds inputs / writes outputs
from its own dir — is the positive confirmation that relativization holds in the
new slot. No script body was modified in BUNDLE-002.

---

## 3. Paper compilation + byte-reproducibility (corrections-final)

- **Builder:** `paper/build.py` (bundle-specific; compiles the self-contained
  `paper/vquad-periodrep-paper.tex` directly — `pdflatex` ×2, PATH→MiKTeX
  fallback, `SOURCE_DATE_EPOCH=1718409600`). Reproducibility target refreshed to
  the corrections-final pin.
- **Run from `paper/`:** `PAGES=24`, `ERRORS=0`, `PDF_EXISTS=True`.
- **SHA-256 (rebuilt):**
  `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe`
- **Target (corrections-final, VQUAD-PAPER-CORRECTIONS-001):**
  `4CA12A35D655DF2227A9E1740E60B39C2E6CABEF6A1942C74307CD43849582FE`
- **REPRODUCIBLE = True** (714771 bytes, 24 pp). Independently re-confirmed by a
  build in a **pristine temp directory** (only `.tex` + `preamble.tex` +
  `build.py` copied): identical hash `4ca12a35…`.

---

## 4. Data presence + scripts-clean

All 12 reference JSONs are present in `data/`. After the harness regenerated each
result JSON next to its script, those regenerated copies and `__pycache__` were
removed so `scripts/0X-*/` ship **clean** (`.py` + `README.md` only) — the
intended reproduction action is for a user to regenerate them. Bundle file count
restored to **40**.

| data/ file | produced by |
|------------|-------------|
| holonomic_recognition_q3_results.json | holonomic_recognition_q3.py |
| operator_verification_results.json | extract_verify_operators.py |
| indicial_results.json | indicial_analysis.py |
| borel_pade_results.json | borel_pade_census.py |
| stage2_kovacic_results.json | stage2b_symsquare.py |
| stage3_galois_LV_results.json | stage3_galois_LV.py |
| stage3b_frobenius_results.json | stage3b_frobenius_v2.py |
| numcheck_period_rep_results.json | numcheck_period_rep.py |
| stage4_methodA_results.json | stage4a_methodA_v2.py |
| stage4_methods_results.json | stage4_methods.py |
| stage0_residual_results.json | stage0_residual_check.py |
| stage1_hankel_results.json | stage1_hankel_period.py |

---

## 5. Retracted-DOI / stale-string scan (the Trap-6 guard)

Whole-bundle scan of `.md/.tex/.py/.json/.txt` for the retracted `20455090`, the
stale version DOI `20624814`, and `C. Marchal` → **NONE** (clean). The embedded
`paper/*.pdf` does not contain `20455090`. Corrected values present:
`20455089` (concept) ×5, `20624813` (concept) ×2, `20694840` (Sakai) ×2,
`O. Marchal` ×3. All DOIs sourced from
`VQUAD-ZENODO-PREP-001/related-identifiers.md` (never memory).

---

## 6. Gate disposition

**STAGE-4 HALT GATE: PASS.** No script failed; no data file is missing or
mismatched beyond the one documented volatile case; the paper compiles clean and
reproduces the corrections-final PDF hash; the retracted DOI is absent. The
bundle is internally complete and was packaged in Stage 5.

Unlike BUNDLE-001, **no editorial-finality gate remains open**: the cold-read
(Verdict A) and corrections cycle have both landed and the H-1 remark was
operator-verified. This bundle is the **deposit-target** artifact.
