# Reconcile diff — VQUAD-ZENODO-DEPOSIT-001 (Stage 2)

Every change made to the 7 deposit files, before → after. **Only** pin values (PDF/bundle
SHA-256, MD5, byte-size), the upload **paths**, and the **provenance** references (which
commit / which run produced the deposited artifacts) moved. No scientific metadata, DOI,
abstract, keyword, MSC, affiliation, page-count, or gate-semantic text was altered.

## Value map applied everywhere
- PDF SHA-256 `4ca12a35…3eea` → `33f339ed…3eea`
- PDF MD5 `028a1a5d…` → `99faea5b…`
- PDF size `714,771`/`714771` → `773,171`/`773171`
- bundle SHA-256 `8752d7c7…` → `7bc5d008…`
- bundle MD5 `9d811494…` → `c1b5a39c…`
- bundle size `721,715` → `776,968`
- upload dir `…\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle…` → `…\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle…`
- bundle-source commit `a33ff59` (BUNDLE-002) → `56a1402` (BUNDLE-002 run-2)
- pre-flight commit `2a7f969` (READY-001 run-2) → `0d98662` (READY-001 run-3)
- PDF-source commit `d4fc87a` (CORRECTIONS-001) → `627d17e` (LAYOUTFIX-001)
- pin-source doc `run-2/stage7-runner-pins.md` → `run-3/run3-stage7-runner-pins.md`
- metadata-source dir `…\READY-001\run-2\` → `…\READY-001\run-3\` (byte-identical content)
- PDF label "corrections-final PDF" → "layout-fixed PDF"

## Per-file

### MANUAL-UPLOAD.md
- §intro: "authoritative **run-2** deposit pins (…/run-2/…)" → "**run-3** deposit pins
  (…/run-3/…, byte-identical to run-2 — anchor 4a75234f unchanged)".
- §1 PDF row: path slot-root→run-2; `714,771 B`→`773,171 B`; SHA `4ca12a35…`→`33f339ed…`;
  MD5 `028a1a5d…`→`99faea5b…`.
- §1 bundle row: path slot-root→run-2; `721,715 B`→`776,968 B`; SHA `8752d7c7…`→`7bc5d008…`;
  MD5 `9d811494…`→`c1b5a39c…`.
- §2/§3 (metadata, abstract, keywords, MSC, **11 related-ids**, the "do not enter 20455090"
  caution): **untouched**.

### operator-runbook.md
- Paths table: metadata/related-ids run-2→run-3; PDF + bundle paths slot-root→run-2.
- "Final pins … from `run-2/stage7-runner-pins.md`" → "`run-3/run3-stage7-runner-pins.md`".
- `PDF_SHA256_PIN` `4ca12a35…`→`33f339ed…`.
- PDF MD5 `028a1a5d…`→`99faea5b…`; bundle SHA `8752d7c7…`→`7bc5d008…` (+ bundle MD5
  `c1b5a39c…` appended for the MD5↔MD5 check).
- Trap-7 "must equal `4ca12a35…`" → "`33f339ed…`".
- Sandbox expect "server-MD5 == `028a1a5d…`" → "`99faea5b…`".
- Gate-reference row 2 "PDF SHA-256 `4ca12a35…`" → "`33f339ed…`".
- `METADATA_ANCHOR`, BLOCKLIST, Gate-1 Scenario-B assertion, venue token, all procedure
  prose: **untouched**.

### gate0-authorization.md
- Prereq rows: READY-001 run-2 `2a7f969`→run-3 `0d98662`; BUNDLE-002 `a33ff59`→run-2
  `56a1402`; CORRECTIONS-001 `d4fc87a`→LAYOUTFIX-001 `627d17e`.
- Gate 0.4 "corrections-final PDF SHA-256 `4ca12a35…` ✓ MATCH" → "layout-fixed PDF SHA-256
  `33f339ed…` ✓ MATCH".
- "bundle archive SHA-256 `8752d7c7…` ✓ MATCH" → "`7bc5d008…` ✓ MATCH".
- "run-2 deposit inputs … present" → "run-3 deposit inputs …".
- HALT determination, token-safety note: **untouched**.

### ledger.json
- `prerequisites`: keys/commits → run-3 `0d98662` / BUNDLE-002 run-2 `56a1402` /
  LAYOUTFIX-001 `627d17e`, each with a "supersedes <old commit>" note.
- `trap7_pdf_sha256` `4ca12a35…`→`33f339ed…`; `bundle_zip_sha256` `8752d7c7…`→`7bc5d008…`.
- `run2_deposit_inputs_present` → `run3_deposit_inputs_present`.
- `pins_for_runner`: `PDF_SHA256_PIN`→`33f339ed…`, `PDF_MD5`→`99faea5b…`,
  `bundle_zip_sha256`→`7bc5d008…` (+ added `bundle_zip_md5` `c1b5a39c…`).
- `title`/`status` → reconciled/upload-ready; added a `reconciliation` block (new pins +
  unchanged-invariants list + on-disk verification; from→to map deferred to this file).
- `METADATA_ANCHOR`, gate1 assertion, affiliation, orcid, halt_reason, fabrications_avoided,
  operator_action_pending: **untouched**.

### handoff.md
- Prereq commits → run-3/run-2/LAYOUTFIX; PDF `4ca12a35…`/`028a1a5d…`→`33f339ed…`/`99faea5b…`;
  bundle `8752d7c7…`→`7bc5d008…`; "pre-verified in run-2"→"run-3 (re-run vs 33f339ed PDF)";
  Trap-7 `4ca12a35…`→`33f339ed…`; "HEAD stays `2a7f969`"→"`0d98662`"; slot commit message →
  the reconcile message. Operator-next-actions prose: **untouched**.

### claims.jsonl
- DEP1-G0-PREREQ: commits → run-3/run-2/LAYOUTFIX.
- DEP1-G0-TRAP7-PDF: "Corrections-final PDF … `4ca12a35…`", source `d4fc87a` → "Layout-fixed
  PDF … `33f339ed…`", source LAYOUTFIX-001 `627d17e`.
- DEP1-G0-BUNDLE: `8752d7c7…`, source `a33ff59` → `7bc5d008…`, source BUNDLE-002 run-2
  `56a1402`.
- DEP1-G0-INPUTS: "run-2 deposit inputs", source READY-001 run-2 → run-3.
- **Added** DEP1-RECONCILE-PINS and DEP1-RECONCILE-CONSISTENT (7 → 9 claims).
- DEP1-G0-TOKEN-ABSENT, DEP1-HALT-GATE0, DEP1-NO-API (governance): **untouched**.

### README.md
- Added a "Reconciled 2026-06-16" banner.
- Gate-0 table: prereqs → run-3/run-2/LAYOUTFIX; Trap-7 `4ca12a35…`→`33f339ed…`; bundle
  `8752d7c7…`→`7bc5d008…`.
- Files table: "with the run-2 final pins" → "run-3".
- HALT-at-Gate-0 framing, Next section: **untouched**.

## Confirmed unchanged (re-grepped present in the 7 files)
metadata anchor `4a75234f…` (×10); concept DOI `20455089` (×5); retracted version
`20455090` appears **only** as the "do not enter / absent" caution + BLOCKLIST (never an
active related-id); related-ids table still 11 rows; abstract / keywords (8) / MSC /
affiliation "Independent Researcher, Yokohama, Japan" / page count 24 / CC-BY-4.0 / all
gate semantics: **not edited**.
