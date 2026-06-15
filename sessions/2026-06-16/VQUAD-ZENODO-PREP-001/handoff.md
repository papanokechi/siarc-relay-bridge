# Handoff — VQUAD-ZENODO-PREP-001

**This slot PREPARES the Zenodo deposit kit; it does NOT deposit.** No Zenodo API
was called, no token was handled, no sandbox dry-run was run, nothing was
committed. Everything below is staged to ready-state and **HELD** per the standing
meta-rule.

## What this slot established

| Stage | Deliverable | Result |
|---|---|---|
| 1 | `kit-verification.md` | Kit PRESENT — no critical tooling missing (templates path + playbook path corrected vs the brief) |
| 2 | `related-identifiers-resolved.json`, `related-identifiers.md` | **12 ids = 2 continues + 1 isPartOf + 8 references + 1 isSupplementTo-placeholder**; 5 Trap-6 version→concept corrections; 8 publisher DOIs available-to-add; 4 unresolved parked |
| 3 | `zenodo_metadata.md`, `metadata-anchor-current.txt`, `metadata-prepared.md` | Metadata drafted + JSON-validated; anchor `dee9195c…` (provisional) |
| 4 | `wrong-venue-token-decision.md` | Forbidden token = `Compositio`; `JSC` excluded (citation collision) |
| 5 | `operator-prep-checklist.md`, `deposit-pin-update-instructions.md` | 14-item gate, 0 complete; exact gate-constant edits documented |
| 6 | `sandbox-and-production-runbook.md` | Sandbox + production runbook; both runners STOP at publish gate |
| 7 | `ledger.json`, `claims.jsonl` (29), `handoff.md` | This hand-off |

## The gate between this slot and the deposit slot

`VQUAD-ZENODO-DEPOSIT-001` opens **only when all 14 `operator-prep-checklist.md`
items are checked**. None is agent-checkable — each is an operator hand-action or
depends on a not-yet-existing slot (VQUAD-PAPER-CORRECTIONS-001, BUNDLE-002). The
load-bearing ones:

1. **Paper-final** — cold-read Verdict A + corrections complete (paper is still
   "working draft; not yet submitted").
2. **Bundle-002** — regenerate post-corrections; its concept DOI fills the
   `isSupplementTo` placeholder (or the row is dropped if paper+bundle = one record).
3. **Re-pin** — PDF SHA-256 (provisional `359d1172…`) and metadata anchor
   (provisional `dee9195c…`) against the final corrected artifacts.
4. **Two decisions** — F-AFFIL (blank vs brief's value) and F-ANTICIPATORY (add
   citations for EBR-Ib/II, δ-Fredholm, the 3 Marchal papers, or ratify as pure
   provenance links).
5. **Gate constants** — update `run_production_draft.py` / `run_sandbox_draft.py`
   per `deposit-pin-update-instructions.md` (the largest single task).
6. **Token** — `set_prod_token.ps1` then `check_prod_token.ps1` (operator only).

## Recommended next operator action

When the gate clears: open `VQUAD-ZENODO-DEPOSIT-001`, run the **sandbox dry-run**
first (`ZENODO_SANDBOX=1` + `run_sandbox_draft.py --execute`), review the sandbox
draft, then the **production draft** (`run_production_draft.py --execute`), review
in the web UI, and **publish by hand**. Immediately append the §B
`submission_log.txt` ledger entry and the `DEPOSIT_LOG_INDEX.md` row in the same
session. The agent never publishes.

## Standing-rule status

Slot git-added (staged) only. **No commit, no push, no tag, no deposit.** Prepared
commit message:

> `VQUAD-ZENODO-PREP-001 — Zenodo deposit kit prepared and configured; awaiting cold-read and corrections before deposit`

(with the `Co-authored-by: Copilot` trailer). The operator runs the commit/push by
hand when ready.
