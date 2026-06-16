# Handoff — VQUAD-ZENODO-READY-001 run-3 (COMPLETE, HELD)

## What this run did
HASH-REFRESH of the deposit pre-flight: refreshed the stale run-2 pins to the **layout-fixed**
PDF and the **re-pinned** bundle, and re-confirmed every gate against the new PDF. No metadata
content was re-derived (the layout fix was reflow-only); the metadata anchor carries forward
unchanged.

## Deposit-ready pin set

| pin | value | vs run-2 |
|-----|-------|----------|
| **PDF SHA-256** | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` | re-pinned (was `4ca12a35…`) |
| PDF MD5 | `99faea5b0f4095788e4ee932436beeda` | re-pinned (was `028a1a5d…`) |
| PDF size / pages | 773171 B / 24 pp | was 714771 B / 24 pp |
| **bundle SHA-256** | `7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013` | re-pinned (was `8752d7c7…`) |
| bundle MD5 | `c1b5a39c0b56576e81b5c5723935669f` | new |
| bundle size / entries | 776968 B / 40 | was 721715 B / 40 |
| **metadata anchor** | `4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895` | **unchanged** |
| related-ids | 11 (2 + 1 + 8 + 0) | **unchanged** |

## Gates (all PASS against the new PDF)
- **Gate 1** (related-ids 11, hole-free, no BLOCKLIST leak, 20455090 absent / 20455089 present) — unchanged.
- **Gate 2.1** (PDF SHA == `33f339ed…`) — re-pinned.
- **Gate 2.2** (wrong-venue: Compositio/AAECC/ETNA absent) — **re-run on the `33f339ed…` PDF** (63713 chars).
- **Gate 2.3** (metadata anchor `4a75234f…`) — unchanged.

## NEXT — in order
1. **(this run) HELD** — operator commits the run-3 record by hand (COMPLETE message below).
2. **Reconcile `VQUAD-ZENODO-DEPOSIT-001/`** — that slot's 7 files (MANUAL-UPLOAD.md,
   gate0-authorization.md, operator-runbook.md, handoff.md, ledger.json, claims.jsonl, …)
   currently reference the **stale** `4ca12a35…` PDF and `8752d7c7…` bundle (committed at
   `627d17e`, ahead of its prerequisites). Rewrite them to `33f339ed…` / `7bc5d008…` and the
   re-pinned bundle. **This is the next task — its own slot edit, not done here.**
3. **Operator hand-steps** (4 remaining): export prod `ZENODO_TOKEN`; confirm scope
   `deposit:write` + instance production; Trap-7 post-staging PDF re-hash == `33f339ed…`; apply
   the `run3-stage7-runner-pins.md` constants into `run_production_draft.py` + `run_sandbox_draft.py`.
4. **Manual upload** — paper PDF `33f339ed…` + bundle zip `7bc5d008…` as one CC-BY-4.0 record
   (Scenario B). Verify Zenodo server-side MD5 == `99faea5b…` (PDF) and `c1b5a39c…` (zip). STOP
   at the publish gate.

## Files the runner loads (from run-3/)
- `zenodo_metadata.md` (anchor `4a75234f…`, byte-identical to run-2)
- `related_identifiers.md` (11 ids, byte-identical to run-2)
- paper PDF `33f339ed…` (from BUNDLE-002 run-2 `paper/`)
- bundle zip `7bc5d008…` (from BUNDLE-002 run-2)

## HELD — staging
Only `sessions/2026-06-16/VQUAD-ZENODO-READY-001/run-3/` files are git-add staged. run-1 (slot
root) and run-2 (`2a7f969`) are pristine; nothing outside run-3/ is staged. HEAD stays
`56a1402`. No commit / push / Zenodo API per the standing meta-rule.

### Prepared COMPLETE commit message (operator hand-commit)
```
VQUAD-ZENODO-READY-001 run-3 — pins refreshed to layout-fixed PDF 33f339ed… + bundle 7bc5d008…; all gates PASS; supersedes run-2 (stale 4ca12a35…/8752d7c7…); deposit-ready

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```
