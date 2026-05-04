# Handoff — PCF1-V13-ARXIV-DRAFT-PREP
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** COMPLETE_DRAFT_READY_FOR_OPERATOR_WEBFORM

## What was accomplished

Pre-staged the PCF-1 v1.3 arXiv submission package
corresponding to the Zudilin endorsement request sent earlier
today (commit `65dd9aa`). Operator can now begin the
arxiv.org/submit web-form draft at any time — starting the
draft is what generates the 6-character endorsement code that
Zudilin needs to enter at arxiv.org/auth/endorse.

Package contents at
`sessions/2026-05-04/PCF1-V13-ARXIV-DRAFT-PREP/`:

- `pack/p12_pcf1_main.tex` (46,349 B; SHA-256
  `e83bb377...`; byte-equal to canonical 2026-05-01 source)
- `pack/p12_pcf1_main.pdf` (392,886 B; SHA-256
  `63420dbf...`; byte-equal to Zenodo deposit
  10.5281/zenodo.19937196)
- `pack/abstract.txt` (1,486 B; verbatim from .tex)
- `pack/00README.txt` (2,157 B; **DOI typo corrected** —
  see anomaly section)
- `pack/manifest.txt` (864 B; SHA-256 record of all 4 files)
- `arxiv_submission_worksheet.md` (consolidated 10-section
  copy-paste sheet for the operator's web-form fill-in)
- `claims.jsonl` (7 AEAL entries)
- `handoff.md` (this file)
- `prompt_spec_used.md`
- `halt_log.json` (`{}`)
- `discrepancy_log.json` (1 entry — DOI typo)
- `unexpected_finds.json` (`{}`)

## Key facts

- **Manuscript:** Complex Multiplication as a Transcendence
  Predicate for Degree-2 Polynomial Continued Fractions
- **Author:** Papanokechi (ORCID 0009-0000-6192-8273)
- **Pages:** 16
- **Zenodo DOIs:** concept `10.5281/zenodo.19931635`;
  v1.3 `10.5281/zenodo.19937196`
- **arXiv classification:** primary `math.NT`, cross-list
  `math.CA`
- **MSC 2020:** Primary 11J70, 11J81; Secondary 34M55, 11G15
- **License:** CC-BY-4.0 (matches Zenodo)
- **Endorser:** Prof. W. Zudilin (`w.zudilin@math.ru.nl`,
  Radboud University Nijmegen). Endorsement-request email
  send event recorded in bridge commit `65dd9aa`
  (ZUDILIN-SEND-EVENT-LOG, 2026-05-04 ~18:12 JST).

## Anomalies and open questions

### ANOMALY-1: 00README.txt had PCF-2 DOIs in PCF-1 pack

**Severity:** medium (would have been visible to arXiv if
uploaded; would NOT have caused submission rejection but
would have created a confusing trail for any reviewer who
checked the README)

**Description:** The original 00README at
`sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3/
00README.txt` line 22 read:

> The PDF SHA-256 is byte-identical to the v1.3 deposit on
> Zenodo (concept DOI 10.5281/zenodo.19941678; v1.3 record
> 19963298).

But `19941678` and `19963298` are the concept and version
DOIs of **PCF-2 v1.3**, not PCF-1 v1.3. PCF-1 v1.3 is at
concept `19931635`, version `19937196`.

**Provenance hypothesis:** The 00README was likely templated
from PCF-2's pack and the DOI swap step was missed during the
rebuild cycle. The TeX itself is clean (no PCF-2 DOIs) —
only the README was affected.

**Fix:** This session's pack at
`sessions/2026-05-04/PCF1-V13-ARXIV-DRAFT-PREP/pack/00README.txt`
contains the corrected DOIs + an explicit ERRATUM note in
the body:

> [ERRATUM 2026-05-04: the previous 00README.txt contained
> the PCF-2 v1.3 DOIs (concept 19941678; record 19963298)
> here in error; corrected in PCF1-V13-ARXIV-DRAFT-PREP
> session.]

The original pack's 00README is preserved unmodified for
AEAL provenance. Recommend a separate small task
`PCF2-V13-PACK-DOI-AUDIT` that checks whether the
**PCF-2** pack (the source of the typo) has its own DOIs
correctly recorded (it likely does — the 030/034 manifests
confirm PCF-2 deposit md5 + SHA-256 match Zenodo, so the
file content is correct; only PCF-1's README was
contaminated by template-reuse).

### ANOMALY-2: PDF was at non-canonical path

**Severity:** low (purely a path-discovery issue)

**Description:** RUNBOOK_pcf1_v1.3.md §1 lists the PDF at
`sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3/
p12_pcf1_main.pdf`, but the actual canonical PDF lives at the
parent `pack/` level:
`sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/
p12_pcf1_main.pdf`

**Fix:** This session's pack consolidates all 4 files (TeX +
PDF + abstract + 00README) at one path level, matching the
arXiv submission expectation.

## Judgment calls made

### JC-1 — Did NOT modify the original ARXIV-PACK-V13-RE-VERIFY pack

Per AEAL deposit-time-snapshot rule (stored memory: prior
deposit packs are immutable provenance artefacts). The
DOI-typo fix lives in a NEW pack at this session's path; the
original pack's 00README remains as a historical record of
the typo.

### JC-2 — Did NOT auto-fill operator-personalisation placeholders in §6 follow-up email

The endorsement-code follow-up email template in §6 of the
worksheet preserves the same placeholder pattern used in the
original 2026-05-04 endorsement-request: `{{OPERATOR_NAME}}`,
`{{OPERATOR_FILLS_AT_SEND_TIME}}`,
`{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}`, and the actual
6-character endorsement code (which doesn't exist yet —
arXiv issues it at step 7 of the web-form click-through).

### JC-3 — Recommended NOT uploading PDF as primary source

arXiv math policy prefers `.tex` source. The worksheet §2
explicitly recommends uploading `p12_pcf1_main.tex +
00README.txt + abstract.txt` and reserving the PDF as a
local-disk-only fallback. Uploading both .tex and .pdf can
cause "PDF detected, source ambiguous" warnings.

### JC-4 — Did NOT pre-stage tarballs for the other 4 records

Per spec scope reasoning: the other 4 records (umbrella,
PCF-2, CT, T2B) all require their own endorsements (math.HO,
math.NT-via-PCF-1-acceptance, math-ph, math.HO respectively
per ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE inventory). PCF-2
v1.3 specifically does NOT need a fresh math.NT endorsement
once PCF-1 v1.3 is accepted, since math.NT endorsement is
per-operator-per-domain. Other 4 packs are deferred until
their respective endorsements land; pre-staging now would be
speculative work without operator-side trigger.

### JC-5 — Worksheet path uses operator's local Windows backslash format

The worksheet §2 file-attach checklist uses
`C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\
claude-chat\siarc-relay-bridge\...` absolute paths to make
copy-paste-into-File-Explorer or browser file-picker
straightforward for the operator. POSIX-style paths would not
work in the operator's Windows environment.

## What would have been asked (if bidirectional)

- "Operator: do you want me to also build a `.tar.gz`
  containing only the .tex + 00README + abstract (no PDF) as
  an arXiv-style upload bundle? arXiv accepts both individual
  files and tarballs."
- "Operator: should I pre-stage PCF-2 v1.3 in parallel since
  PCF-2 is also math.NT primary and would re-use the same
  Zudilin endorsement after PCF-1 lands?"

These are deferred per JC-4.

## Recommended next step

**For operator (any time, doesn't have to wait for Zudilin):**

1. Open `arxiv_submission_worksheet.md` in a side window
2. Visit https://arxiv.org/submit and click **Start new
   submission**
3. Walk through §5 click-through steps 1-7
4. At step 7, copy the 6-character endorsement code arXiv
   issues
5. Use §6 template to send a follow-up email to Zudilin with
   the code (replace `XXXXXX` with the actual code)
6. Save the arXiv draft and wait for Zudilin to enter the
   code at arxiv.org/auth/endorse
7. Once arXiv emails confirming endorsement, return to draft
   and submit (§5 steps 8-10)
8. Run §7 post-submission cross-link checklist

**For synthesizer (Claude-side, optional):** review the
worksheet for any operator-personalisation placeholders that
should be replaced with verified content (the operator's
ORCID is already filled at 0009-0000-6192-8273; only
`{{OPERATOR_NAME}}` and `{{OPERATOR_FILLS_AT_SEND_TIME}}`
remain). If the operator wants Claude-side QA before opening
the worksheet, paste the CLAUDE_FETCH URL.

## Files committed

- `sessions/2026-05-04/PCF1-V13-ARXIV-DRAFT-PREP/`
  - `pack/00README.txt` (DOI-corrected)
  - `pack/abstract.txt` (verbatim)
  - `pack/manifest.txt` (SHA-256 record)
  - `pack/p12_pcf1_main.pdf` (392,886 B; byte-equal Zenodo)
  - `pack/p12_pcf1_main.tex` (46,349 B; canonical source)
  - `arxiv_submission_worksheet.md` (the deliverable)
  - `claims.jsonl` (7 AEAL entries)
  - `handoff.md` (this file)
  - `prompt_spec_used.md`
  - `halt_log.json` (`{}`)
  - `discrepancy_log.json` (1 entry: DOI typo)
  - `unexpected_finds.json` (`{}`)

## AEAL claim count

**7 entries** written to `claims.jsonl` this session.
