# Sandbox & production runbook — VQUAD-ZENODO-PREP-001 (Stage 6)

For the eventual `VQUAD-ZENODO-DEPOSIT-001` slot. Both runners create a
**reversible draft** and **STOP at the publish gate** — they never call
`/actions/publish`, never mint, never commit (standing meta-rule). Publishing is
the operator's separate by-hand step. **This prep slot runs neither.**

## Pre-flight (do once, before either runner)

1. Apply `deposit-pin-update-instructions.md`: update `PDF_NAME`,
   `PDF_SHA256_PIN`, `METADATA_ANCHOR`, `TITLE`, `BLOCKLIST`, the Gate-1 count
   assertion, and the venue token `ETNA`→`Compositio` in the runner(s).
2. Stage these three files **in the same folder as the runner** (the script reads
   them from its own directory via `STAGE`):
   - the final corrected **`vquad-periodrep-paper.pdf`**;
   - **`zenodo_metadata.md`** (this slot's file, corrections folded);
   - **`related_identifiers.md`** — copy this slot's `related-identifiers.md`
     **renaming the hyphen to an underscore** (the script loads
     `related_identifiers.md`), with the bundle `isSupplementTo` placeholder
     filled or the row removed.
3. **Dry-run first (no network, no token):**
   ```powershell
   python run_sandbox_draft.py        # or run_production_draft.py
   ```
   Runs Gate 0 (PENDING, no token), Gate 1 (DOI completeness), the description
   normalization self-test, and Gate 2 if the PDF is staged. All gates must PASS
   before exporting any token.

## Step 4a — SANDBOX dry-run (operator hand-step)

- **Environment:** `ZENODO_SANDBOX=1` **required** (the script refuses otherwise),
  plus a **sandbox** token (`ZENODO_SANDBOX_TOKEN`, or `ZENODO_TOKEN`) from
  `https://sandbox.zenodo.org/account/settings/applications/` (scope
  `deposit:write`). A production token 401s against the sandbox.
- **Command:**
  ```powershell
  $env:ZENODO_SANDBOX = "1"
  $env:ZENODO_SANDBOX_TOKEN = "<sandbox token>"
  python run_sandbox_draft.py --execute
  ```
- **Expected gates:**
  - **Gate 0** PASS — token present (value never printed); target = sandbox.zenodo.org.
  - **Gate 1** PASS — wired array hole-free at the V_quad counts (Scenario A
    `12 (2+1+8+1)` or Scenario B `11 (2+1+8)`); no version/predecessor DOI from
    `BLOCKLIST` leaked in.
  - **Gate 2** PASS — staged PDF SHA-256 == re-pinned `PDF_SHA256_PIN`;
    `Compositio` absent in PDF text; `zenodo_metadata.md` SHA-256 ==
    re-pinned `METADATA_ANCHOR`.
  - self-test — description normalization round-trip MATCH + drift still detected.
- **Expected outputs:** `draft_ready.md` (sandbox draft-edit URL, reserved DOI,
  raw stored description, by-hand publish command), `upload_manifest.md`, and
  appended `api_call` AEAL claims in `claims.jsonl`. STOPS at the publish gate.
- **HALT condition:** any gate failing aborts the run with `*** HALT: …`; the
  operator fixes the cause (re-pin, fill placeholder, correct venue token) and
  re-runs. Nothing is published.
- **Verify in the UI:** open the sandbox draft URL, confirm the description
  renders (Greek/sub-superscripts/dashes survive the `<p>`-wrap + entity-encode),
  the 12 related identifiers, keywords, license CC-BY-4.0. Then **discard** the
  sandbox draft (it is throwaway).

## Step 5 — PRODUCTION draft (operator hand-step)

- **Environment:** a **production** token from
  `https://zenodo.org/account/settings/applications/` (scope `deposit:write`; add
  `deposit:actions` only if you will publish via API). The script reads
  `ZENODO_TOKEN` then `ZENODO_PROD_TOKEN`. `set_prod_token.ps1` exports it;
  `check_prod_token.ps1` confirms scope + production instance.
- **Command:**
  ```powershell
  .\set_prod_token.ps1                 # export ZENODO_TOKEN (operator)
  .\check_prod_token.ps1               # confirm deposit:write + production
  python run_production_draft.py --execute
  ```
- **Gates / outputs:** identical to sandbox (Gate 0/1/2 + self-test), against
  `https://zenodo.org/api`. Writes `draft_ready.md` (PRODUCTION draft URL, the
  **reserved-but-NOT-minted** DOI, raw description, and the operator-only publish
  `curl`), `upload_manifest.md`, and `claims.jsonl` entries.
- **Duplicate-title guard:** the runner aborts if a draft/record with the exact
  V_quad `TITLE` already exists (resume-vs-new is the operator's call).
- **STOP:** the run ends at the publish gate. The DOI is reserved, not minted.

## MINT — operator only, irreversible (NOT in any slot)

Review the production draft in the web UI, then **either** click **Publish**
**or** run the by-hand `curl` printed in `draft_ready.md`. Publishing mints the
real concept + version DOIs. Immediately after, add the §B `submission_log.txt`
ledger entry **in the same session** (`_zenodo_uploader.py ledger-entry … --append`)
and append the `DEPOSIT_LOG_INDEX.md` row (version + concept DOI). The agent never
runs publish.

## Quick gate reference

| Gate | Checks | HALT trigger |
|---|---|---|
| 0 | token present; target instance | `--execute` with no token |
| 1 | wired-array counts; no `BLOCKLIST` leak | wrong counts, or a version DOI in the array |
| 2 | PDF SHA-256 pin; `Compositio` absent; metadata anchor | pin mismatch, venue token present, anchor changed |
| self-test | description normalize round-trip + drift detection | normalization mismatch |
