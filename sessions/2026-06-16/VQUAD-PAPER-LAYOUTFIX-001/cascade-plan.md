# cascade-plan.md — VQUAD-PAPER-LAYOUTFIX-001 Stage 4

The new paper PDF SHA-256 **`33f339ed…`** (was `4ca12a35…`) invalidates every
downstream pin that referenced the old hash. Recommended **Option A** (keep slots
clean: re-run each downstream as a fresh pass rather than hand-patching pins).

## The single source-of-truth pin every downstream must point to
| artifact | OLD (retire) | NEW (use everywhere) |
|---|---|---|
| paper PDF SHA-256 | `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe` | **`33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea`** |
| paper PDF MD5 | `028a1a5d9e10a3a9487596f6db3e6a38` | **`99faea5b0f4095788e4ee932436beeda`** |
| paper PDF bytes / pages | 714771 / 24 | **773171 / 24** |

## Cascade chain (run in order)
1. **LAYOUTFIX-001 (this slot)** — DONE. PDF fixed, 0 overfull, byte-repro,
   content-diff reflow-only, re-pinned. HELD for operator hand-commit.

2. **→ VQUAD-REPRO-BUNDLE-002 re-run (BUNDLE-003 or in-place refresh)**
   - Swap `paper/` (.tex + **new .pdf 33f339ed…** + preamble) into the bundle tree.
   - Update `paper/build.py` `TARGET_SHA` + header comment `4CA12A35…` → `33F339ED…`,
     `714771 B` → `773171 B` (pages still 24).
   - Re-run `verify_bundle.py` (all 13 scripts must still PASS — scripts/data are
     unchanged; only the paper PDF changed).
   - Re-zip `vquad-periodrep-bundle.zip` → **new archive SHA-256** (supersedes
     `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb`).
   - The corrections were layout-only ⇒ all constants/scripts identical ⇒ the bundle
     verification result is unchanged except the paper hash.

3. **→ VQUAD-ZENODO-READY-001 run-3**
   - `stage2-pdf-pin`: PDF SHA-256 → `33f339ed…`, MD5 → `99faea5b…`, bytes → 773171.
   - `stage7-runner-pins.md`: `PDF_SHA256_PIN` → `33f339ed…`.
   - **metadata anchor**: re-pin **only if** `zenodo_metadata.md` embeds the PDF hash.
     The run-2 anchor `4a75234f…` folds the abstract + F-AFFIL Option C; if the
     abstract/affiliation/keywords/MSC are unchanged (they are — layout-only) and the
     metadata file does **not** carry the PDF SHA, the anchor is unaffected. **Verify:
     grep `zenodo_metadata.md` for `4ca12a35`; if absent, anchor unchanged; if present,
     swap to `33f339ed…` and recompute `4a75234f…`.**
   - Re-confirm Gate 1 (related-ids 11, Scenario B) and Gate 2.2 (Compositio absent) —
     unchanged by a layout fix, but re-assert against the new PDF.

4. **→ VQUAD-ZENODO-DEPOSIT-001** (operator hand-step)
   - Use the **new** PDF `33f339ed…` + the new bundle zip as the Scenario-B record.
   - The manual-upload sheet `…/VQUAD-ZENODO-DEPOSIT-001/MANUAL-UPLOAD.md` PDF pins
     must be updated to `33f339ed…` / `99faea5b…` before upload.

## Note
This is layout-only; **no mathematical/text content changed** (proven, multiset diff
= −2 hyphens / 0 other chars). The cascade is a pure hash-refresh — no re-review of
constants, no re-verification of claims is required, only the file-integrity pins.
