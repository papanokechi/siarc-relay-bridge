# VQUAD-ZENODO-READY-001 · run-2

**RE-RUN of the final pre-flight for the V_quad exponential-period paper's Zenodo
deposit.** The first run (committed `c88b996`, files at the slot root) correctly
**halted at Stage 1** because the corrections chain had not started. All
prerequisites now exist and are committed, so this run executed **all 8 stages** and
refreshed every deposit pin. **Ready-state HELD** — no commit, no Zenodo API, no
token.

The first-run halt artifact at the slot root is **preserved**; this successful run
lives entirely in `run-2/`.

## Result

| | value |
|---|---|
| Status | **READY** — all stages PASS, HELD for operator |
| PDF pin | SHA-256 `4ca12a35…` · MD5 `028a1a5d…` · 714771 B · 24pp |
| Metadata anchor | SHA-256 `4a75234f…` (supersedes `dee9195c…`) |
| Related-ids | 11 (Scenario B: 2 continues + 1 isPartOf + 8 references; isSupplementTo dropped) |
| Gate 1 | PASS — hole-free, no version-DOI leak, retracted `20455090` absent |
| Gate 2.2 | PASS — `Compositio`/`AAECC`/`ETNA` absent in the `4ca12a35…` PDF |

## Files

| file | role |
|------|------|
| `stage1-prerequisite-verification.md` | 4/4 prerequisites met (PASS) |
| `stage2-pdf-pin.md` | PDF SHA-256 + MD5 refresh |
| `stage3-metadata-refresh.md` | new anchor; what changed (L-3 clause + F-AFFIL) |
| `stage4-related-identifiers.md` | Scenario B drop; Gate 1 |
| `stage5-wrong-venue-gate.md` | Gate 2.2 wrong-venue |
| `stage6-operator-checklist-reconciled.md` | 9/13 resolved; 4 operator hand-steps |
| `stage7-runner-pins.md` | final `run_production_draft.py` constant block |
| `zenodo_metadata.md` | **deposit metadata** (anchor `4a75234f…`) — runner loads this |
| `related_identifiers.md` | **deposit related-ids** (11, Scenario B) — runner loads this |
| `metadata-anchor-current.txt` | re-pinned anchor record |
| `_finalize_metadata.py` | auditable metadata generator (re-runnable) |
| `_validate_related_ids.py` | Gate-1 + Gate-2.2 validator (re-runnable) |
| `ledger.json` / `claims.jsonl` / `handoff.md` | run record + downstream handoff |

## Next

Four operator hand-steps remain (token ×2, Trap-7 post-staging re-hash, apply the
prepared `stage7` constants), then open **VQUAD-ZENODO-DEPOSIT-001** — deposit the
PDF **+** BUNDLE-002 zip as **one** CC-BY-4.0 record (Scenario B), STOP at the publish
gate. See `handoff.md`.
