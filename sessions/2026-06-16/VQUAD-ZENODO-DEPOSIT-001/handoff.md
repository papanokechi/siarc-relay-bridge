# Handoff — VQUAD-ZENODO-DEPOSIT-001 (RECONCILED · upload-ready · HELD at Gate 0)

The deposit is **fully prepared and verified**; the runner execution, token handling,
and publish are **operator hand-steps**. No Zenodo API was called by the agent; the
token value was never read or logged.

## Reconciled 2026-06-16 (post-LAYOUTFIX) — now upload-ready
DEPOSIT-001 now points at the **layout-fixed PDF `33f339ed…`** and the **re-pinned bundle
`7bc5d008…`** (upload paths under `…\VQUAD-REPRO-BUNDLE-002\run-2\…`), exactly consistent
with READY-001 run-3 (`0d98662`). The stale pre-layout-fix pins are gone from all 7 files
(see `reconcile-verification.md`). **The manual upload may now
proceed against `MANUAL-UPLOAD.md`.** Metadata anchor `4a75234f…`, related-ids (11),
abstract, affiliation, page count 24 are unchanged.

Operator hand-steps before/at upload: **Trap-7** re-hash the staged PDF == `33f339ed…`
immediately before upload (OneDrive-drift backstop) → upload **PDF + bundle** (one record,
Scenario B) → fill metadata per `zenodo_metadata.md` (anchor `4a75234f…`) + the 11
related-ids → review render → **Publish** (irreversible) → capture concept + version DOIs →
same-session **§B ledger append** + update `DEPOSIT_LOG_INDEX.md` → send O. Marchal the
concept DOI → open `VQUAD-COMPOSITIO-PRECLEAR-001`.

## Why held (not a failure — the defining stop)

Gate 0 halts for two converging reasons (see `gate0-authorization.md`):
1. **Token absent** in the agent's execution environment — it lives in the operator's
   interactive shell, and a sandbox run needs a *sandbox* token besides. The task's own
   Gate 0.2 says: token absent → HALT, do not proceed.
2. **Standing meta-rule** — the agent never handles tokens, calls the Zenodo API, or
   publishes; it stages to ready-state and stops for the operator.

## Everything is verified and in place

- Prereqs committed: READY-001 run-3 `0d98662` (HEAD), BUNDLE-002 run-2 `56a1402`,
  LAYOUTFIX-001 `627d17e`.
- PDF SHA-256 `33f339ed…` (Trap-7 re-hash MATCH), MD5 `99faea5b…`, 24pp.
- Bundle zip SHA-256 `7bc5d008…` (MATCH).
- Metadata anchor `4a75234f…`; related-ids **11** (Scenario B); Gate 1 + wrong-venue
  (`Compositio` absent) pre-verified in run-3 (re-run against the `33f339ed…` PDF).
- Runner kit, playbook, and run-2 deposit inputs all present.

## Operator next actions (full commands in `operator-runbook.md`)

1. **Pre-flight** — stage PDF + bundle + `zenodo_metadata.md` + `related_identifiers.md`
   in a deposit folder with the runners; apply the `stage7` pin block to both runners;
   Trap-7 re-hash the staged PDF == `33f339ed…`; dry-run (no token) → all gates PASS.
2. **Sandbox** — `$env:ZENODO_SANDBOX=1` + sandbox token →
   `python run_sandbox_draft.py --execute` → eyeball the draft → discard.
3. **Production** — production token (`set_prod_token.ps1` / `check_prod_token.ps1`) →
   `python run_production_draft.py --execute` → **STOP at the publish gate**.
4. **Publish** (the only irreversible step — operator) — review the draft (title,
   abstract, Papanokechi + ORCID, affiliation, 11 related-ids, **both** files, CC-BY 4.0,
   no target-venue strings) → click Publish → capture version + concept DOI.
5. **Same session** — §B ledger append (`_zenodo_uploader.py ledger-entry … --append`),
   `DEPOSIT_LOG_INDEX.md` row, send Marchal the concept DOI, open
   `VQUAD-COMPOSITIO-PRECLEAR-001`.

## Standing-rule status

Slot `git add`-staged only. **No commit, no push, no Zenodo API, no token handled, no
publish.** HEAD stays `0d98662`. The runner-produced artifacts (`draft_ready.md`,
`upload_manifest.md`, sandbox/production result docs) are produced **by the operator's
runner execution**, not fabricated here. `EBR3-REVISION-001` left untracked.

Commit message for this reconciliation (pins-only swap; still HELD — **not** a deposit):
> `VQUAD-ZENODO-DEPOSIT-001 — reconciled stale pins to layout-fixed PDF 33f339ed… + bundle 7bc5d008…; MANUAL-UPLOAD.md now consistent with READY-001 run-3; upload-ready`
