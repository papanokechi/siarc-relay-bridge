# Handoff — VQUAD-REPRO-BUNDLE-002 run-2 (COMPLETE, HELD)

## What this run did
HASH-REFRESH re-run of the deposit-target reproducibility bundle: swapped the paper PDF
(and `.tex` / `preamble.tex`) to the **layout-fixed** `33f339ed…` from
VQUAD-PAPER-LAYOUTFIX-001 (commit `627d17e`), refreshed `paper/build.py`'s target pin and the
one provenance doc, re-verified integrity, and re-packaged. Supersedes run-1 (`a33ff59`),
whose bundle embedded the clipped-digit `4ca12a35…` PDF.

## New pins (what downstream must point at)

| artifact | new pin | supersedes |
|----------|---------|------------|
| **paper PDF** SHA-256 | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` | `4ca12a35…` |
| paper PDF MD5 | `99faea5b0f4095788e4ee932436beeda` | `028a1a5d…` |
| paper PDF size / pages | 773171 B / 24 pp | 714771 B / 24 pp |
| **bundle archive** SHA-256 | `7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013` | `8752d7c7…` |
| bundle archive MD5 | `c1b5a39c0b56576e81b5c5723935669f` | — |
| bundle archive size / files | 776968 B / 40 | 721715 B / 40 |

## Verification (all PASS)
- **Integrity:** 13/13 scripts exit 0; 11 exact, 1 modulo-volatile (numcheck), 1 stdout-only
  (stage2_kovacic) — identical pattern to run-1. `scripts/` + `data/` byte-identical to the
  `a33ff59` bundle (only 5 paper/provenance files changed).
- **PDF reproduces** `33f339ed…` in-place and in a pristine temp dir (`REPRODUCIBLE=True`).
- **Archive:** testzip OK, 40 entries, single top dir, embedded PDF = `33f339ed…`, SHA stable
  on re-pack.
- **Hygiene:** `4ca12a35` / `714771` / `028a1a5d` absent; retracted `20455090` absent; concept
  `20455089` present.

## Next steps (cascade — Option A, clean slots)
1. **(this run) HELD** — operator commits the run-2 record by hand (COMPLETE message below).
2. **VQUAD-ZENODO-READY-001 run-3** — refresh the deposit pre-flight pins:
   - stage-2 PDF pin → `33f339ed…` (MD5 `99faea5b…`, 773171 B)
   - bundle-archive pin → `7bc5d008…` (MD5 `c1b5a39c…`, 776968 B)
   - re-run Gate 2.2 wrong-venue on the `33f339ed…` PDF; refresh the metadata anchor only if
     it carries the PDF hash (it did not in run-2 — confirm).
3. **Reconcile `VQUAD-ZENODO-DEPOSIT-001/MANUAL-UPLOAD.md`** — it currently references the
   **stale** `4ca12a35…` PDF and `8752d7c7…` archive (committed at `627d17e`, ahead of its
   prerequisites). Rewrite it to `33f339ed…` + `7bc5d008…` and the re-pinned bundle **after**
   READY-001 run-3 lands. Do **not** drive the manual upload off the current (stale) runbook.
4. **Manual upload** — paper PDF + bundle zip as one CC-BY-4.0 record (Scenario B). Verify
   Zenodo server-side MD5 == `99faea5b…` (PDF) and `c1b5a39c…` (zip).

## HELD — staging
Only `sessions/2026-06-16/VQUAD-REPRO-BUNDLE-002/run-2/` files are git-add staged. The run-1
(`a33ff59`) bundle and the LAYOUTFIX-001 slot are pristine. Nothing outside this run-record is
staged. HEAD stays `627d17e`. No commit / push / Zenodo API per the standing meta-rule.

### Prepared COMPLETE commit message (operator hand-commit)
```
VQUAD-REPRO-BUNDLE-002 run-2 — bundle re-pinned to layout-fixed PDF 33f339ed…; integrity PASS (13/13 scripts, 11 exact); new archive SHA 7bc5d008…; supersedes a33ff59 (clipped-digit PDF); scripts/data unchanged

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```
