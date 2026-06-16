# Gate 0 — Authorization → HALT (deposit execution is an operator hand-step)

**Slot:** VQUAD-ZENODO-DEPOSIT-001 · 2026-06-16 · **HELD at Gate 0**

This slot performs the Gate-0 read-only authorization checks, then **halts** — the
sandbox/production runner execution, the token handling, and the publish are
**operator hand-steps** under the standing meta-rule. No Zenodo API was called; the
token value was never read or logged.

## Gate 0 checks (all read-only)

| # | check | result |
|---|-------|--------|
| 0.1 | Prerequisite slots committed | **PASS** |
| | · VQUAD-ZENODO-READY-001 run-2 | `2a7f969` ✓ (HEAD) |
| | · VQUAD-REPRO-BUNDLE-002 | `a33ff59` ✓ |
| | · VQUAD-PAPER-CORRECTIONS-001 | `d4fc87a` ✓ |
| 0.2 | `ZENODO_TOKEN` present in agent env | **False** (value never logged) |
| 0.3 | token scope/instance | N/A — no token in agent env to inspect |
| 0.4 | Trap-7: corrections-final PDF SHA-256 | `4ca12a35…` ✓ **MATCH** |
| — | bundle archive SHA-256 | `8752d7c7…` ✓ **MATCH** |
| — | runner kit (4 scripts) + playbook present | ✓ |
| — | run-2 deposit inputs (`zenodo_metadata.md`, `related_identifiers.md`) present | ✓ |
| — | existing deposit working folder | none (operator stages it at run time) |

## Determination — HALT at Gate 0 (two converging reasons)

1. **Task Gate 0.2 (explicit):** *"Verify `ZENODO_TOKEN` present … If absent: HALT with
   instruction to run `set_prod_token.ps1` and `check_prod_token.ps1`, then re-run. Do
   not proceed."* The token is **absent** in the agent's execution environment — it
   lives in the operator's interactive PowerShell window; environment variables do not
   carry into the agent's fresh-process tool calls (and a sandbox run additionally
   needs a *sandbox* token, not the production one). So the task's own first gate
   mandates a halt.

2. **Standing meta-rule (governance):** the agent never handles tokens, never calls the
   Zenodo API, and never publishes — it prepares the deposit to ready-state and STOPS
   for the operator to run by hand. The sandbox `--execute`, the production
   `--execute`, and the publish are, by this rule, operator hand-actions. Operator
   prior review: *"the standing rule is a meta-rule about how to handle exactly this
   situation … the standing rule covers this case; held."*

The two reasons agree: **the deposit is fully prepared and verified; the runner
execution and publish are the operator's hand-steps.** See `operator-runbook.md` for
the exact, ready-to-run command sequence.

## Token-safety note

Only **presence** (True/False) and would-be **length** were ever checked. The token
value and any prefix were never read into a variable that is logged, never printed,
never written to any file. (Result: presence False — nothing to redact.)
