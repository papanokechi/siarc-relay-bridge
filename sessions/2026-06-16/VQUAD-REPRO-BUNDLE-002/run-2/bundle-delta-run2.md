# Bundle delta — VQUAD-REPRO-BUNDLE-002 run-2 (Stage 1)

**Date:** 2026-06-16 (Asia/Tokyo)
**Run-record:** `sessions/2026-06-16/VQUAD-REPRO-BUNDLE-002/run-2/`
**Supersedes:** the committed run-1 bundle (commit `a33ff59`) whose paper PDF was the
pre-layout-fix `4ca12a35…` (clipped right margin on ≥3 pages).
**Trigger:** VQUAD-PAPER-LAYOUTFIX-001 (commit `627d17e`) re-pinned the paper PDF to the
layout-fixed `33f339ed…`. This is a **HASH-REFRESH** re-run: the layout fix was proven
**reflow-only** (PDF text diff = −2 line-end hyphens, 0 content characters), so no script,
data, or constant re-review is performed — only the paper PDF / `.tex` / `preamble.tex` and
the one doc that hard-coded the old hash change.

---

## 1. What changed vs the `a33ff59` bundle (full-tree SHA-256 diff)

A byte-level SHA-256 comparison of every file in run-1's
`vquad-periodrep-bundle/` against run-2's confirms **exactly 5 files differ**, all in the
expected set; **40 files both sides**, no file added or removed:

| file | change | run-1 (a33ff59) | run-2 |
|------|--------|-----------------|-------|
| `paper/vquad-periodrep-paper.pdf` | layout-fixed PDF | `4ca12a35…` 714771 B | **`33f339ed…` 773171 B** |
| `paper/vquad-periodrep-paper.tex` | layout-fixed source | 87354 B | 87778 B (+424 B) |
| `paper/preamble.tex` | LAYOUTFIX preamble (`\emergencystretch` + breakable `\_`) | 3037 B | 3320 B (+283 B) |
| `paper/build.py` | TARGET_SHA + docstring hash/size refreshed to `33f339ed…` / 773171 | 3094 B | 3094 B (content only) |
| `docs/SIARC_PROVENANCE.md` | added LAYOUTFIX-001 provenance row; note re-pinned to `33f339ed…` | — | — |

`paper/build.py` is the bundle's **self-contained compiler** (compiles the pre-assembled
`.tex` with preamble + bibliography inline); only its `TARGET_SHA` (line 30) and docstring
header (lines 13–14) were edited — its build logic is unchanged.

## 2. scripts/ and data/ are BYTE-IDENTICAL

The same full-tree SHA-256 diff confirms **every file under `scripts/` and `data/` is
byte-identical** to the `a33ff59` bundle. The layout fix touched only the paper; no script
logic and no numerical result changed. **No HALT** (Stage 1.2 condition: scripts/data must be
unchanged — confirmed).

## 3. Old-hash hygiene (whole-tree scan after the swap)

| token | meaning | run-2 bundle tree |
|-------|---------|-------------------|
| `4ca12a35` (any case) | superseded PDF SHA-256 | **ABSENT** ✓ |
| `714771` | superseded PDF size | **ABSENT** ✓ |
| `028a1a5d` | superseded PDF MD5 | **ABSENT** ✓ |
| `20455090` | retracted v1.0 companion DOI | **ABSENT** ✓ |
| `33f339ed` | layout-fixed PDF SHA-256 | present (SIARC_PROVENANCE ×2, build.py ×2) ✓ |
| `773171` | layout-fixed PDF size | present (build.py) ✓ |
| `20455089` | concept companion DOI | present (README, SIARC_PROVENANCE, paper `.tex`) ✓ |

Retracted-DOI hygiene held over from run-1 is intact (the layout fix touched no references).

## 4. Disposition

Delta is exactly the hash-refresh footprint: paper PDF/`.tex`/`preamble` + `build.py` pin +
one provenance doc; scripts/data untouched. Proceed to assemble (done in-place here),
integrity (Stage 3), and packaging (Stage 4).
