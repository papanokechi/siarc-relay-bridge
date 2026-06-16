# Operator runbook — VQUAD-ZENODO-DEPOSIT-001

The agent prepared and verified everything; **these steps are operator hand-actions**
(token export, sandbox/production `--execute`, and the irreversible Publish). The
runners create a **reversible draft** and **STOP at the publish gate** — they never
call `/actions/publish`. Run every command in **one** PowerShell window (env vars do
not cross windows).

## Paths

| what | path |
|------|------|
| Runner kit | `C:\LocalWork\project-fingerprint\sectorial\cc_transcendence\sakai-stratification\` |
| Deposit metadata | `…\VQUAD-ZENODO-READY-001\run-2\zenodo_metadata.md` |
| Related-ids (underscore) | `…\VQUAD-ZENODO-READY-001\run-2\related_identifiers.md` |
| Paper PDF | `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle\paper\vquad-periodrep-paper.pdf` |
| Bundle (secondary file) | `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle.zip` |

## Final pins to apply in the runner(s) — from `run-2/stage7-runner-pins.md`

```python
PDF_NAME        = "vquad-periodrep-paper.pdf"
PDF_SHA256_PIN  = "4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe"
METADATA_ANCHOR = "4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895"
TITLE           = "An explicit exponential-period representation of the V_quad connection coefficient"
BLOCKLIST       = {"20455090", "20481592", "20694841", "19885550",
                   "20569724", "20571232", "20624814"}
# Gate-1 count assertion (Scenario B — isSupplementTo dropped, 11 ids):
sp = sum(1 for r in arr if r["relation"] == "isSupplementTo")
if not (len(arr) == 11 and c == 2 and ip == 1 and rf == 8 and sp == 0):
    halt("wired array not hole-free 11 (2+1+8+0).")
# forbidden-venue token: ETNA -> Compositio
```
PDF MD5 (compare to Zenodo's returned upload checksum, **MD5↔MD5**): `028a1a5d9e10a3a9487596f6db3e6a38`
Bundle zip SHA-256: `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb`

## Pre-flight (once)

1. Make a deposit working folder; copy in: the **PDF**, the **bundle zip**,
   `zenodo_metadata.md`, and `related_identifiers.md` (already underscore-named),
   alongside the runner scripts (the scripts read these from their own dir via
   `STAGE`).
2. Apply the pin block above in `run_production_draft.py` **and**
   `run_sandbox_draft.py` (`ETNA`→`Compositio`, the Scenario-B Gate-1 assertion, all
   constants).
3. **Trap-7** — re-hash the PDF *in the deposit folder*; must equal `4ca12a35…`:
   ```powershell
   (Get-FileHash -Algorithm SHA256 .\vquad-periodrep-paper.pdf).Hash.ToLower()
   ```
4. **Dry-run (no network, no token):**
   ```powershell
   python run_production_draft.py        # Gate 0 PENDING, Gate 1, self-test, Gate 2
   ```
   All gates must PASS before exporting any token.

## Step 1 — SANDBOX `--execute` (sandbox token)

Sandbox needs a **sandbox** token from `https://sandbox.zenodo.org/account/settings/applications/`
(scope `deposit:write`). A production token 401s against sandbox.
```powershell
$env:ZENODO_SANDBOX = "1"
$env:ZENODO_SANDBOX_TOKEN = "<sandbox token>"   # operator; never commit
python run_sandbox_draft.py --execute
```
Expect: Gate 0/1/2 PASS, draft created, PDF + bundle uploaded, server-MD5 == `028a1a5d…`,
`draft_ready.md` + `upload_manifest.md` written, 3 `api_call` claims (sandbox=true),
**STOP at publish gate**. Open the sandbox draft URL, eyeball the render (Greek/sub-
superscripts/dashes, 11 related-ids, CC-BY-4.0), then **discard** the throwaway draft.
**Any sandbox gate fails → fix and re-run; do not go to production.**

## Step 2 — PRODUCTION draft `--execute` (production token)

```powershell
Remove-Item Env:ZENODO_SANDBOX -ErrorAction SilentlyContinue
.\set_prod_token.ps1      # export ZENODO_TOKEN (operator)
.\check_prod_token.ps1    # confirm deposit:write + production instance
python run_production_draft.py --execute
```
Expect: Gate 0/1/2 PASS against `https://zenodo.org/api`, **production draft** created
(NOT published), PDF + bundle uploaded, `draft_ready.md` (production draft URL,
**reserved-not-minted** DOI, raw description, operator-only publish `curl`) +
`upload_manifest.md`, 3 `api_call` claims (sandbox=false), **STOP at publish gate**.

> Scenario B: the deposit carries **two files** — the PDF and the bundle zip. Confirm
> both appear in `upload_manifest.md`. If the runner is single-file, add the bundle in
> the web UI (Edit → Upload) **before** publishing.

## Step 3 — MINT (operator only, irreversible — NOT in this slot)

Review the production draft in the web UI:
- title; abstract; author **Papanokechi** + ORCID `0009-0000-6192-8273`;
  affiliation **"Independent Researcher, Yokohama, Japan"**;
- related-ids: **11**, correct verbs (2 continues, 1 isPartOf, 8 references);
- **both** files present (PDF 24pp + bundle.zip) and downloadable;
- license **CC-BY 4.0**; no PII beyond ORCID; `Compositio`/target-venue strings absent.

If satisfied → **Publish** (web-UI button or the `curl` in `draft_ready.md`). **This is
the only irreversible step. Only the operator does it.** Capture the published
**version** DOI and **concept** DOI.

## Step 4 — SAME SESSION post-publish bookkeeping

1. Verify the published description with the **normalized** compare (strip `<p>`, strip
   Markdown italics, HTML-decode entities — Trap 3; the `<p>`-wrap appears only on the
   published render, not the draft GET).
2. **§B ledger append** (a published record with no §B entry is an unlogged mint —
   incident, not TODO):
   ```powershell
   $Up   = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\siarc\submitted\_zenodo_uploader.py"
   $Spec = "<deposit folder>\ledger_entry_spec.json"
   python "$Up" ledger-entry --spec "$Spec" --record <version_id> --concept <concept_id> `
     --ledger "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\siarc\submitted\submission_log.txt" --append
   ```
   (Back up `submission_log.txt`/`.html` first; `--append` rebuilds the HTML mirror.)
3. Append the new row to `DEPOSIT_LOG_INDEX.md` (version + concept DOI).
4. Send **O. Marchal** the live **concept** DOI (committed action — the paper cites his
   personal communication + 3 papers).
5. Open **VQUAD-COMPOSITIO-PRECLEAR-001** with the concept DOI.

## Gate reference

| Gate | Checks | HALT trigger |
|---|---|---|
| 0 | token present; target instance | `--execute` with no token |
| 1 | 11-id counts (2+1+8+0); no `BLOCKLIST` leak | wrong counts / a version DOI in the array |
| 2 | PDF SHA-256 `4ca12a35…`; `Compositio` absent; anchor `4a75234f…` | pin mismatch / venue token present / anchor changed |
| self-test | description normalize round-trip + drift detection | normalization mismatch |
| **publish** | **the defining stop** | **never auto-called — operator hand-step** |
