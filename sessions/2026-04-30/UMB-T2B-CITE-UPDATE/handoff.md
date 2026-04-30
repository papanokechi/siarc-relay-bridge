# UMB-T2B-CITE-UPDATE — handoff

**Task ID:** UMB-T2B-CITE-UPDATE
**AEAL class:** manuscript-correction
**Verdict:** CLEAN
**File:** `tex/submitted/umbrella_program_paper/main.tex`

## Edits applied (two locations)

### 1. Companion-papers longtable T2B row (line 377)
- **Title** (working): `The Trans-Stratum $-2/9$ phenomenon: empirical census and heuristic derivation` → `Two arithmetic classes of degree-$(2,1)$ Trans-stratum continued fractions: a Birkhoff--Trjitzinsky / Gauss-continued-fraction dichotomy`
- **Status**: `Preprint on Zenodo (v2.0)` → `Preprint on Zenodo (v3.0, 2026-04-30)`
- **DOI**: `10.5281/zenodo.19801038` → `10.5281/zenodo.19915689`

### 2. `\bibitem{T2B}` (lines 416–422)
- Title updated as above
- `Zenodo, 2026.` → `Zenodo preprint, v3.0, 2026-04-30.`
- Added **Version DOI** `10.5281/zenodo.19915689` alongside the retained **concept DOI** `10.5281/zenodo.19783311` (the latter preserves v1→v2→v3 lineage and is best practice for Zenodo citations)

## Inline-mention sweep
Searched UMB main.tex for any other occurrence of `19801038` or the old titles outside the bibliography:
- `19801038` → 0 remaining hits ✅
- `Transcendental Ratio Identity` → 0 hits (was already absent — v2 retitle was post-deposit)
- `Trans-Stratum $-2/9$ phenomenon` → 0 remaining hits ✅

## Verification

| Check | Required | Observed | Pass |
|-------|----------|----------|------|
| Old DOI `19801038` | 0 hits | 0 | ✅ |
| New DOI `19915689` | ≥1 hit | 2 (table + bibitem) | ✅ |
| Old title in T2B bib entry | 0 hits | 0 | ✅ |
| pdflatex build | 0 errors | 2 passes, 0 errors | ✅ |

## Build artefacts
- pdf size: 287,549 B
- tex sha256: `4D82354AC36E30F1FBB6C0C712EBBEA55604A2FB91BF5864D2E66CE313EB0068`
- pdf sha256: `5A4AEDF468B936AB1E2E7969D08049025881FEF1AF0E201B8503206F30DC4CEF`

## Push policy
**NOT PUSHED** — relay says push only after papanokechi confirms.
