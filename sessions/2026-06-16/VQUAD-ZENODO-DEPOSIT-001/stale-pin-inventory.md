# Stale-pin inventory — VQUAD-ZENODO-DEPOSIT-001 (Stage 1)

DEPOSIT-001 was committed at `627d17e` riding the **pre-layout-fix** cascade. Every pin
below points at the stale PDF (`4ca12a35…`) or stale bundle (`8752d7c7…`). This inventory
is the complete `file:line → stale value` list the Stage-2 swap must clear.

## Deposit-ready target values (verified on disk this task)

| artifact | path (run-2 cascade) | SHA-256 | MD5 | bytes |
|---|---|---|---|---|
| paper PDF | `…\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle\paper\vquad-periodrep-paper.pdf` | `33f339ed…3eea` | `99faea5b…eeda` | 773171 |
| bundle zip | `…\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle.zip` | `7bc5d008…e013` | `c1b5a39c…669f` | 776968 |

Get-FileHash this task confirmed both exactly. **The slot-root path
`…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle\…` still hashes to `4ca12a35…`** — so the
file-path pins are stale too and MUST be repointed to `run-2\`, else the operator uploads
the clipped-digit PDF.

## Stale → deposit-ready value map

| kind | stale | deposit-ready |
|---|---|---|
| PDF SHA-256 | `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe` | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` |
| PDF MD5 | `028a1a5d9e10a3a9487596f6db3e6a38` | `99faea5b0f4095788e4ee932436beeda` |
| PDF size | `714,771` / `714771` | `773,171` / `773171` |
| bundle SHA-256 | `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb` | `7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013` |
| bundle MD5 | `9d811494d77f4ffa84127ef4d105584a` | `c1b5a39c0b56576e81b5c5723935669f` |
| bundle size | `721,715` | `776,968` |
| PDF/bundle dir | `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle…` | `…\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle…` |
| bundle commit | `a33ff59` (BUNDLE-002) | `56a1402` (BUNDLE-002 run-2) |
| pre-flight commit | `2a7f969` (READY-001 run-2) | `0d98662` (READY-001 run-3) |
| PDF-source commit | `d4fc87a` (CORRECTIONS-001) | `627d17e` (LAYOUTFIX-001) |
| pin-source doc | `run-2/stage7-runner-pins.md` | `run-3/run3-stage7-runner-pins.md` |
| PDF label | "corrections-final PDF" | "layout-fixed PDF" |

## file:line → stale occurrence

### MANUAL-UPLOAD.md
- L4–5 — "authoritative **run-2** deposit pins (from …/run-2/zenodo_metadata.md + related_identifiers.md)" → run-3 (metadata content byte-identical; pointer only)
- L14 — PDF path `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle\paper\…` · `714,771 B` · SHA `4ca12a35…` · MD5 `028a1a5d…`
- L15 — bundle path `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle.zip` · `721,715 B` · SHA `8752d7c7…` · MD5 `9d811494…`

### operator-runbook.md
- L14–15 — metadata/related-ids paths `…\VQUAD-ZENODO-READY-001\run-2\…` → run-3
- L16 — PDF path `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle\paper\…`
- L17 — bundle path `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle.zip`
- L19 — "from `run-2/stage7-runner-pins.md`" → run-3/run3-stage7-runner-pins.md
- L23 — `PDF_SHA256_PIN = "4ca12a35…"`
- L34 — PDF MD5 `028a1a5d…`
- L35 — bundle SHA `8752d7c7…`
- L46 — Trap-7 "must equal `4ca12a35…`"
- L65 — "server-MD5 == `028a1a5d…`"
- L126 — Gate-2 row "PDF SHA-256 `4ca12a35…`"

### gate0-authorization.md
- L15 — READY-001 run-2 `2a7f969` ✓ (HEAD) → run-3 `0d98662`
- L16 — BUNDLE-002 `a33ff59` → run-2 `56a1402`
- L17 — CORRECTIONS-001 `d4fc87a` → LAYOUTFIX-001 `627d17e` (PDF source)
- L20 — "corrections-final PDF SHA-256 `4ca12a35…` ✓ MATCH" → layout-fixed `33f339ed…`
- L21 — "bundle archive SHA-256 `8752d7c7…` ✓ MATCH" → `7bc5d008…`
- L23 — "run-2 deposit inputs … present" → run-3

### ledger.json
- L11 — key `…READY-001_run-2`, commit `2a7f969` (HEAD) → run-3 `0d98662`
- L12 — `VQUAD-REPRO-BUNDLE-002` commit `a33ff59` → run-2 `56a1402`
- L13 — `VQUAD-PAPER-CORRECTIONS-001` `d4fc87a` → `VQUAD-PAPER-LAYOUTFIX-001` `627d17e`
- L17 — `trap7_pdf_sha256` `4ca12a35…`
- L18 — `bundle_zip_sha256` `8752d7c7…`
- L21 — `run2_deposit_inputs_present` → run3
- L26 — `PDF_SHA256_PIN` `4ca12a35…`
- L27 — `PDF_MD5` `028a1a5d…`
- L32 — `bundle_zip_sha256` `8752d7c7…`

### handoff.md
- L18 — prereq commits `2a7f969` / `a33ff59` / `d4fc87a`
- L20 — PDF `4ca12a35…` / MD5 `028a1a5d…`
- L21 — bundle `8752d7c7…`
- L22–23 — "pre-verified in run-2" → run-3
- L30 — Trap-7 == `4ca12a35…`
- L45 — "HEAD stays `2a7f969`" → `0d98662`
- L49–50 — slot commit message (refresh to the reconcile message)

### claims.jsonl
- L1 DEP1-G0-PREREQ — `2a7f969` / `a33ff59` / `d4fc87a`
- L3 DEP1-G0-TRAP7-PDF — "Corrections-final PDF … `4ca12a35…`", source `d4fc87a`
- L4 DEP1-G0-BUNDLE — `8752d7c7…`, source `a33ff59`
- L5 DEP1-G0-INPUTS — "run-2 deposit inputs", source READY-001 run-2

### README.md
- L16 — prereq commits `2a7f969` / `a33ff59` / `d4fc87a`
- L18 — Trap-7 `4ca12a35…`
- L19 — bundle `8752d7c7…`
- L28 — "the run-2 final pins" → run-3

## UNCHANGED (do NOT alter)
metadata anchor `4a75234f…`; related-ids (11, incl. concept `20455089`, no version
`20455090`); abstract; keywords (8); MSC 2020; affiliation "Independent Researcher,
Yokohama, Japan"; page count 24; CC-BY-4.0; all procedure prose; all gate semantics
(Gate-0 HALT, token-absent, no-API).

## Note on scope
The brief frames this as a hash/size swap, but the explicit PURPOSE is "so the operator
uploads the correct file." The slot-root paths resolve to the **stale** `4ca12a35…` PDF,
so the file-path pins and the pin-source provenance (which commit produced the deposited
PDF/bundle) must move with the hashes, or the runbook would be self-contradictory
(hash `33f339ed…` next to a path/commit that yields `4ca12a35…`). No scientific metadata,
DOI, or abstract text is touched. Every change is enumerated in `reconcile-diff.md`.
