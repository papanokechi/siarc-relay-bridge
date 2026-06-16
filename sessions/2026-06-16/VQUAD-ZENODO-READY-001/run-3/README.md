# VQUAD-ZENODO-READY-001 · run-3

**HASH-REFRESH re-run of the final pre-flight for the V_quad exponential-period paper's
Zenodo deposit.** run-2 (committed `2a7f969`) pinned the **pre-layout-fix** PDF
(`4ca12a35…`) and bundle (`8752d7c7…`). The LAYOUTFIX (committed `627d17e`) and the
re-pinned BUNDLE-002 run-2 (committed `56a1402`) make both stale. run-3 refreshes them to
the **layout-fixed** PDF (`33f339ed…`) and the re-pinned bundle (`7bc5d008…`), and
re-confirms every gate against the new PDF. **Ready-state HELD** — no commit, no Zenodo
API, no token.

Because the layout fix was proven **reflow-only** (−2 line-end hyphens, 0 content), no
metadata content is re-derived: the abstract, affiliation, title, keywords, MSC, version
and all 11 related-ids carry forward byte-identical, and the **metadata anchor is
unchanged** (Case A — the anchor hashes `zenodo_metadata.md`, not the PDF).

run-1 (slot-root HALT artifact) and run-2 (`2a7f969`) are **preserved untouched**; this
run lives entirely in `run-3/`.

## Result

| | value | vs run-2 |
|---|---|---|
| Status | **READY** — all gates PASS against the new PDF, HELD for operator | |
| PDF pin | SHA-256 `33f339ed…` · MD5 `99faea5b…` · 773171 B · 24pp | re-pinned (was `4ca12a35…`) |
| Bundle pin | SHA-256 `7bc5d008…` · MD5 `c1b5a39c…` · 776968 B · 40 entries | re-pinned (was `8752d7c7…`) |
| Metadata anchor | SHA-256 `4a75234f…` | **unchanged** (Case A) |
| Related-ids | 11 (Scenario B: 2 continues + 1 isPartOf + 8 references; isSupplementTo dropped) | unchanged |
| Gate 1 | PASS — hole-free, no version-DOI leak, retracted `20455090` absent / concept `20455089` present | unchanged |
| Gate 2.1 | PASS — PDF SHA == `33f339ed…` | re-pinned |
| Gate 2.2 | PASS — `Compositio`/`AAECC`/`ETNA` absent in the **`33f339ed…`** PDF (63713 chars) | re-run on new PDF |
| Gate 2.3 | PASS — anchor `4a75234f…` | unchanged |

## Files

| file | role |
|------|------|
| `run3-prerequisite-verification.md` | Stage 1 — LAYOUTFIX + BUNDLE-002 run-2 present; new PDF/bundle hash as stated |
| `run3-stage2-pdf-pin.md` | Stage 2 — PDF pin refresh `4ca12a35…`→`33f339ed…`; Trap-7 PENDING-HAND-ACTION |
| `run3-metadata-anchor.md` | Stage 3 — Case A proof: anchor not PDF-dependent → carries forward `4a75234f…` |
| `run3-stage4-bundle-pin.md` | Stage 4 — bundle pin refresh `8752d7c7…`→`7bc5d008…`; Scenario B unchanged |
| `run3-gates-precheck.md` | Stage 5 — Gates 1 / 2.1 / 2.2 / 2.3 PASS against the new PDF |
| `run3-stage7-runner-pins.md` | Stage 6 — final runner constant block (PDF/bundle/anchor) |
| `run3-operator-checklist.md` | Stage 6 — 9/13 resolved; 4 operator hand-steps remain |
| `zenodo_metadata.md` | **deposit metadata** (anchor `4a75234f…`) — runner loads this (== run-2) |
| `related_identifiers.md` | **deposit related-ids** (11, Scenario B) — runner loads this (== run-2) |
| `_validate_related_ids.py` | Gate-1 + Gate-2.2 validator, re-pointed to the `33f339ed…` PDF (re-runnable) |
| `ledger.json` / `claims.jsonl` / `handoff.md` | run record + downstream handoff |

## Next

Operator hand-commits run-3 (message in `handoff.md`), then **reconcile
`VQUAD-ZENODO-DEPOSIT-001/`** — its 7 files still reference the stale `4ca12a35…` /
`8752d7c7…` and must be rewritten to `33f339ed…` / `7bc5d008…` **before any upload** (its
own next task). Then the 4 operator hand-steps (token ×2, Trap-7 re-hash now == `33f339ed…`,
apply the `run3-stage7` constants) and the manual upload of the PDF **+** bundle zip as
**one** CC-BY-4.0 record (Scenario B), STOP at the publish gate. See `handoff.md`.
