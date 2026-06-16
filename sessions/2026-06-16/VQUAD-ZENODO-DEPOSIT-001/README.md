# VQUAD-ZENODO-DEPOSIT-001

**Production deposit of the V_quad period-representation paper — HELD at Gate 0.**

> **Reconciled 2026-06-16 (post-LAYOUTFIX):** all pins swapped from the stale pre-layout-fix
> PDF/bundle to the deposit-ready layout-fixed PDF `33f339ed…`/bundle `7bc5d008…`, and the
> upload paths repointed to `…\VQUAD-REPRO-BUNDLE-002\run-2\…`. The slot is now consistent
> with READY-001 run-3 (`0d98662`) and upload-ready. Metadata anchor `4a75234f…`, related-ids
> (11), abstract, affiliation, and page count are unchanged. Full pre-layout-fix from→to map
> in `stale-pin-inventory.md` / `reconcile-diff.md`; see `reconcile-verification.md`.

The agent ran the Gate-0 read-only authorization checks (prerequisites, PDF/bundle
hashes, token presence) and **halted**: the sandbox/production runner `--execute`, the
token handling, and the irreversible Publish are **operator hand-steps** under the
standing meta-rule, and the production token is not present in the agent's environment
(the task's own Gate 0.2 mandates a halt when the token is absent). **No Zenodo API was
called; the token value was never read or logged.**

## Gate 0 result

| check | result |
|-------|--------|
| Prereqs (READY-001 run-3 `0d98662`, BUNDLE-002 run-2 `56a1402`, LAYOUTFIX-001 `627d17e`) | PASS |
| `ZENODO_TOKEN` in agent env | **False** (value never logged) |
| Trap-7 PDF SHA-256 `33f339ed…` | PASS (MATCH) |
| Bundle zip SHA-256 `7bc5d008…` | PASS (MATCH) |
| Runner kit + playbook + run-2 inputs | PASS |
| **Determination** | **HALT at Gate 0 — deposit prepared; execution is the operator's hand-step** |

## Files

| file | role |
|------|------|
| `gate0-authorization.md` | Gate-0 checks + the HALT determination (token-safety note) |
| `operator-runbook.md` | **the deliverable** — exact ready-to-run command sequence (pre-flight → sandbox → production draft → publish gate → §B append → index → Marchal → Compositio preclear) with the run-3 final pins |
| `handoff.md` | operator next actions, concise |
| `ledger.json` | held-state record (status HELD-AT-GATE-0) |
| `claims.jsonl` | prereq / PDF / bundle / governance claims — **no api_call entry** (none made) |

The runner-produced files (`draft_ready.md`, `upload_manifest.md`, sandbox/production
result docs) will be created **by the operator's runner execution**; they are not
fabricated here.

## Next

Operator runs the `operator-runbook.md` sequence (sandbox → production draft → STOP at
publish gate → review → **Publish by hand**), then the same-session §B append +
`DEPOSIT_LOG_INDEX.md` row + sends Marchal the concept DOI, then opens
**VQUAD-COMPOSITIO-PRECLEAR-001**.
