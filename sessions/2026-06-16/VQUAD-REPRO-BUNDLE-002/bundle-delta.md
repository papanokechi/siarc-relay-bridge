# Stage 1 — Inventory and delta (BUNDLE-001 → BUNDLE-002)

**Chain:** VQUAD-REPRO-BUNDLE-002 · **Date:** 2026-06-16 · **Repo HEAD:** `d4fc87a`
**Template baseline:** `VQUAD-REPRO-BUNDLE-001/vquad-periodrep-bundle/` (the preview bundle)
**Purpose:** regenerate the bundle against the **corrections-final** paper
(VQUAD-PAPER-CORRECTIONS-001, PDF SHA-256 `4ca12a35…`, 24 pp), superseding the
preview. Scenario B (bundle rides as a secondary file in the paper's single
Zenodo deposit; **no separate bundle DOI**).

## Prerequisites (all met — unlike BUNDLE-001)

| # | Prerequisite | State | Evidence |
|---|---|---|---|
| 1 | `VQUAD-PAPER-CORRECTIONS-001` complete | ✅ MET | Committed `d4fc87a`; corrections-final PDF `4ca12a35…`, 24 pp, byte-reproducible |
| 2 | `VQUAD-REPRO-BUNDLE-001` exists (template) | ✅ MET | Committed `219df0e`; 40-file preview bundle used as assembly template |
| 3 | Scenario B confirmed (no separate bundle DOI) | ✅ MET | Operator-confirmed in the brief; `related-identifiers.md` `isSupplementTo` row is a placeholder to be **dropped** at READY-001, not filled here |

## What changed, by bundle component

| Component | Disposition | Why |
|---|---|---|
| `paper/` | **UPDATED** | New corrections-final PDF (`4ca12a35…`, 714771 B, 24 pp), corrected self-contained `.tex` (87354 B), `preamble.tex` — all copied from `VQUAD-PAPER-CORRECTIONS-001/latex/`. `paper/build.py` kept (bundle-specific, compiles the self-contained `.tex` directly) with its reproducibility target refreshed `359d1172…`→`4ca12a35…` and `23 pages`→`24 pages`. |
| `scripts/` | **UNCHANGED** | The corrections were expository / bibliographic / terminological — **no script logic changed** (VQUAD-PAPER-CORRECTIONS-001 `verification-pass.md`: constants unchanged, bridge residual 0). The already-relativized, UTF-8-guarded, `stage4_methods.py`-patched copies were taken **verbatim from BUNDLE-001** (the verified set), not re-derived — guaranteeing byte-identity with the previously-integrity-checked scripts. Re-verified by `verify_bundle.py` in Stage 4. |
| `data/` | **UNCHANGED** | No numerical result changed, so every `*_results.json` reference is identical to BUNDLE-001. Re-confirmed by re-running each script and comparing in Stage 4. |
| `docs/` | **UPDATE-REQUIRED** | Old PDF page count, the **retracted DOI 20455090**, a stale δ-DOI (version `20624814`), and a misattributed initial (`C. Marchal`) all flow from the pre-corrections template and must be repointed to the corrections-final state. See `docs-update.md`. |
| `README.md` | **UPDATE-REQUIRED** | Page count `23 pp`→`24 pp`; companion DOI `20455090`→ concept `20455089`. |
| `LICENSE` | **UNCHANGED** | CC BY 4.0 canonical text. |
| per-dir `README.md` ×4 | **UNCHANGED** | Script-description only; carry no PDF hash, DOI, or page count (grep-confirmed). |

## Assembly note (auditable)

`relativize_and_copy.py` (the parent→bundle transformer) is retained in the slot
root with its `BUNDLE` constant pointed at BUNDLE-002 for provenance, **but it was
not re-run**: BUNDLE-002 copies the already-relativized scripts verbatim from the
verified BUNDLE-001 tree. `verify_bundle.py` and `_package_bundle.py` are the
tools actually exercised this slot. `_package_bundle.py` is `__file__`-relative
(no path constant); `verify_bundle.py`'s `BUNDLE` constant was repointed to
BUNDLE-002.
