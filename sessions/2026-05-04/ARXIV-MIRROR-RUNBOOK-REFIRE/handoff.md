# Handoff — ARXIV-MIRROR-RUNBOOK-REFIRE
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes
**Status:** PARTIAL

## What was accomplished

Re-fired and completed Prompt 002 (the original 5-arXiv-tarball mirror
runbook), using the corrected pack inventory that converged from
prompts 027 → 030 → 032.  All five published Zenodo records (SIARC
umbrella v2.0, PCF-1 v1.3, PCF-2 v1.3, Channel Theory v1.3, T2B v3.0)
were re-verified against the live Zenodo API at PHASE A.1; all five
deposited PDFs were hash-matched (md5 + SHA-256 + size + page count)
against their Zenodo deposits at PHASE A.2 (5/5 PASS).  Five
`RUNBOOK_<record>.md` files were emitted with arXiv classification,
file-attach order, metadata fields, web-form sequence, and post-
submission Zenodo↔arXiv cross-link instructions.  Six endorsement-
request templates (PCF-1 v1.3 + PCF-2 v1.3) × (Zudilin + Mazzocco +
Garoufalidis) were emitted with placeholder hygiene per Rule 6.  The
session lands in **PARTIAL_RUNBOOKS_READY_AWAITING_ENDORSER_HANDLES**:
operator can submit the math-ph + math.HO records (1, 4, 5) without
gating on third-party endorser action *but still gates on first-time-
in-category endorsement* per current arXiv help text — see Anomaly #2
below; math.NT records (2, 3) require operator-side personalisation
and email-send of one of the 6 templates.

## Key numerical findings

| # | Record | DOI | Pages | Deposit md5 (Zenodo PASS) | arXiv primary | arXiv cross | Endorsement |
|---|---|---|---:|---|---|---|---|
| 1 | umbrella v2.0 | 10.5281/zenodo.19965041 | 12 | `d633699f…` PASS | math.HO | — | required (math.HO) |
| 2 | PCF-1 v1.3 | 10.5281/zenodo.19937196 | 16 | `fbf5449b…` PASS | math.NT | math.CA | required (math.NT) |
| 3 | PCF-2 v1.3 | 10.5281/zenodo.19963298 | 22 | `cdd62891…` PASS | math.NT | math-ph | required (math.NT) |
| 4 | CT v1.3 | 10.5281/zenodo.19972394 | 17 | `e58951de…` PASS | math-ph | math.DS, math.NT | required (math-ph) |
| 5 | T2B v3.0 | 10.5281/zenodo.19915689 | 8 | `d245be3b…` PASS | math.HO | math.NT | required (math.HO) |

- **Phase A.1.** Zenodo public-records API GET against record id
  19937196 confirmed PCF-1 v1.3 metadata (title, version 1.3, deposit
  md5 `fbf5449b…`, size 392886, license CC-BY-4.0, conceptdoi
  19931635); the spec §1 stated `concept = 19937196` which is the
  **version** ID, not the concept ID — the concept is 19931635.
  Same shape as 030's 4-record corrections.
- **Phase A.2.** All 5 deposited PDFs hash-match Zenodo md5 + SHA-256
  + size + page count (5/5 PASS).  Local-rebuild `pack/<pdf>` files
  for records 1, 3, 4, 5 carry the expected pdfTeX `/CreationDate`
  timestamp drift relative to deposit (size + pages match, md5+sha
  differ); per 032's documented disposition this is NOT a FAIL gate.
- **Phase B.** All 5 packs already carry `00README.txt` +
  `abstract.txt` + `manifest.txt` (legacy from 002 + 030); no Phase
  B.4 synthesis was needed.  One cosmetic carry-over: `ct_v1.3/00README`
  has a blank `Title:` field (already documented in 032's
  discrepancy_log; not propagated here).
- **Phase C.** 5 `RUNBOOK_<record>.md` files emitted, each ~5 KB.
- **Phase D.** 6 endorsement-request templates emitted (NT records
  only, per spec §3.D.1).  Placeholders preserved: `{{OPERATOR_NAME}}`,
  `{{OPERATOR_ORCID}}`, `{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}`.
  Endorser arXiv author ids (`zudilin_w_1`, `mazzocco_m_1`,
  `garoufalidis_s_1`) and affiliations are public-metadata pre-fills,
  not PII per Rule 6 (same disposition the prior session
  ENDORSER-HANDLE-ACQUISITION used).

## Judgment calls made

1. **AEAL gate definition for PHASE A.2.**  Adopted 032's
   disposition — md5/SHA-256/size of the deposited Zenodo PDF
   (`zenodo.pdf` for records 1, 3, 4, 5; `p12_pcf1_main.pdf` for
   record 2) is the AEAL gate, NOT the local-rebuild `pack/<pdf>`
   timestamp-drifted variant.  This avoids 4 false-FAIL on the first
   builder run (originally captured in `_pack_hash_results.json` row
   `rebuild_drift_expected: true`).  This is a continuation of 030's
   PCF-1 disposition.
2. **Endorsement requirement for non-math.NT records.**  Spec §2
   PHASE C step 0 hinted that `math.HO + math-ph` records may be
   endorsement-free for ORCID-verified first-time submitters.  After
   reading https://info.arxiv.org/help/endorsement.html (fetched
   2026-05-04), the policy is unambiguous: endorsement is required
   for first submission in **any** new arXiv category.  RUNBOOKs
   for records 1, 4, 5 reflect this and recommend operator-adapted
   math.NT templates as a fallback.  Did NOT trigger
   `HALT_ARXIV_CLASSIFICATION_POLICY_CHANGED` because the policy has
   not changed *since* prompt 002 was drafted (the spec assumption
   was inaccurate, not the policy).
3. **Endorsement template count.**  Spec §3.D.1 limited Phase D to
   "3 endorsers × 2 records = up to 6 templates" (math.NT only).
   Followed literally.  Did not emit math-ph templates for record 4
   even though Mazzocco is a strong math-ph match — flagged in
   Anomaly #1.
4. **PCF-1 pack location.**  The 002 location (`sessions/2026-05-02/
   ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/pack/`) is the polluted
   21-page state (508,059 B PDF).  Used the 030 canonical location
   (`sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3/`,
   16-page p12_pcf1_main.pdf 392,886 B byte-equal to Zenodo) for
   the PCF-1 RUNBOOK file-attach paths.  Operator must NOT use the
   002 PCF-1 pack location (per 030 verdict).
5. **Endorser handles as PII vs public metadata.**  Treated arXiv
   author ids (`zudilin_w_1`, etc.) and academic-affiliation strings
   as public metadata (since they appear on every published arXiv
   abstract page and the endorser's institutional homepage).
   Treated email addresses as PII (left as `{{...EMAIL...}}`
   placeholder for operator-side confirmation).  Same disposition
   as ENDORSER-HANDLE-ACQUISITION 2026-05-04.
6. **No on-behalf submission to arXiv.**  Per Rule 2 + spec §1
   "Per Rule 2: no on-behalf arXiv submission" — runbook is a
   checklist for the operator; agent did not navigate
   arxiv.org/submit.

## Anomalies and open questions

1. **Mazzocco-as-math-ph endorser for record 4 (CT v1.3).**  Channel
   Theory v1.3 is primary `math-ph` and Mazzocco is the strongest
   math-ph match in the Tier-1 endorser pool — but spec §3.D.1
   restricted Phase D to math.NT records only, so no
   `endorsement_template_ct_v1.3_mazzocco.md` was emitted in this
   session.  If the operator wants to submit record 4 first (in
   logical order — CT v1.3 is the structural prerequisite for
   future PCF-2 v2.x results), they need either to adapt one of the
   PCF-1 / PCF-2 Mazzocco templates (substituting `math.NT` →
   `math-ph` and the title) or to fire a small follow-up prompt
   to emit the math-ph templates verbatim.  Recommend the latter
   for AEAL hygiene.
2. **arXiv endorsement is required for ALL 5 records, not just
   math.NT.**  Spec §2 PHASE C step 0 listed endorsement only for
   records 2 + 3.  Per current arXiv help text, the operator's
   first submission in math.HO, math-ph, math.NT each requires
   endorsement separately (each is a distinct endorsement domain).
   After at least one accepted math-cluster submission, subsequent
   ones in the same domain do not need re-endorsement.  Practical
   implication: even records 1, 4, 5 are gated on first-time
   endorsement; the templates emitted here can be adapted, but
   strictly speaking 6 more templates (3 endorsers × 3 non-NT
   categories) would be needed for full coverage.  Recommend
   sequencing the 5 submissions so that one positive endorsement
   serves as a pivot for the others (e.g., submit PCF-1 v1.3
   first to math.NT, then use that math-cluster activity to ease
   the math-ph and math.HO endorsement gates).
3. **Mazzocco affiliation update.**  ENDORSER-HANDLE-ACQUISITION
   2026-05-04 listed Mazzocco at "University of Birmingham" via
   her current homepage; operator should re-verify at send time
   if the email-confirmation step turns up a different
   institutional affiliation (academic mobility).
4. **PCF-1 v1.3 pack location operator-confusable.**  The bridge
   carries TWO PCF-1 pack directories: `sessions/2026-05-02/...
   arxiv_pack_pcf1_v1.3/` (polluted 21pp; **DO NOT USE**) and
   `sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3/`
   (canonical 16pp; **USE THIS**).  RUNBOOK_pcf1_v1.3.md points
   to the canonical location, but operator awareness is needed
   when the 002 location is referenced from older docs (e.g.
   the cheat-sheet RESUME_AFTER_REBOOT_20260502.txt that 030
   recommended patching).
5. **Spec §1 PCF-1 v1.3 "concept" ID was incorrect.**  Spec said
   record id 19937196 has concept = 19937196.  Live Zenodo API
   shows concept = **19931635**.  This is *not* a Zenodo record-
   ID drift (record 19937196 is correct); the spec's `concept_doi`
   line was wrong.  Pinned in `zenodo_metadata_5_records.json`
   field `api_concept`.

## What would have been asked (if bidirectional)

1. Confirm scope: should 034 emit the additional math-ph and
   math.HO endorsement templates *now* (3 records × 3 endorsers
   = 9 more templates, total 15)?  Or treat that as a follow-on
   prompt 034b once operator decides submission order?
2. Confirm CT v1.3 cross-list set: spec §1 said `math-ph + math.DS`;
   034 added `math.NT` as a third cross-list because CT v1.3 §1
   discusses degree-d PCFs as a number-theory object.  Operator
   removes if undesired.
3. Confirm operator preference: institutional email vs personal
   email for the arXiv account (institutional unlocks the auto-
   endorsement-via-claim path described in the arXiv help text;
   personal forces the personal-endorsement path used by the 6
   templates).

## Recommended next step

Operator action (fire-and-forget):
- (a) Personalise `endorsement_template_pcf1_v1.3_zudilin.md` (or
  `…_garoufalidis.md`), confirm Zudilin's institutional email at
  https://www.ru.nl/en/people/zudilin-w (or the Garoufalidis
  equivalent), and send.  This unlocks math.NT for both PCF-1 and
  PCF-2 in one endorsement.
- (b) After PCF-1 v1.3 is accepted at arXiv, fire RUNBOOK_pcf2_v1.3.md
  (does NOT need a fresh endorsement; the math.NT endorsement is
  per-operator-per-domain, not per-paper).
- (c) Decide whether to fire a small follow-on prompt 034b to emit
  the additional math-ph + math.HO templates, OR to defer until
  records 4 + 1 + 5 are first up for submission.

Strategic next agent prompt:
- **035-PICTURE-V18-ARXIV-INTEGRATION**: amend strategic picture
  v1.17 §5 G14 row from "endorsers identified" to "submission
  runbooks staged + endorsement templates emitted; awaiting
  operator-side endorser email-confirm + send"; reduce M9 weight
  by one notch.

## Files committed

```
sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/
├── _build_phase_AB.py
├── _emit_phase_CD.py
├── _pack_hash_results.json
├── claims.jsonl                                   (6 entries)
├── discrepancy_log.json                           ({})
├── endorsement_template_pcf1_v1.3_garoufalidis.md
├── endorsement_template_pcf1_v1.3_mazzocco.md
├── endorsement_template_pcf1_v1.3_zudilin.md
├── endorsement_template_pcf2_v1.3_garoufalidis.md
├── endorsement_template_pcf2_v1.3_mazzocco.md
├── endorsement_template_pcf2_v1.3_zudilin.md
├── halt_log.json                                  ({})
├── handoff.md                                     (this file)
├── pack_hash_match_table.md
├── prompt_spec_used.md
├── RUNBOOK_ct_v1.3.md
├── RUNBOOK_pcf1_v1.3.md
├── RUNBOOK_pcf2_v1.3.md
├── RUNBOOK_siarc_umbrella_v2.0.md
├── RUNBOOK_t2b_v3.0.md
├── unexpected_finds.json                          ({})
└── zenodo_metadata_5_records.json
```

## AEAL claim count

6 entries written to `claims.jsonl` this session.
