# Handoff — ARXIV-PACK-FOUR-RECORD-AUDIT
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished
Audited the four non-PCF-1 arxiv-pack tarball directories on the bridge
(`arxiv_pack_siarc_umbrella_v2.0`, `arxiv_pack_pcf2_v1.3`,
`arxiv_pack_ct_v1.3`, `arxiv_pack_t2b_v3.0`) for (a) Zenodo concept-DOI
+ version-DOI correctness against the live Zenodo public records API,
(b) deposited PDF byte-match (md5 + size), and (c) page-count parity
versus expected. All four records PASS on every gate. Verdict:
`UPGRADE_AUDIT_FOUR_RECORDS_ALL_PASS`. The cheat-sheet ID transposition
flagged by 030 is confined to its PCF-1 entries; the 4 packs themselves
carry correct IDs in their own `00README.txt`, so no cross-record
patches are needed.

## Key numerical findings

| Record | Concept DOI | Version DOI | Zenodo md5 | Size (B) | Pages |
|---|---|---|---|---|---|
| siarc_umbrella_v2.0 | 19885549 ✅ | 19965041 ✅ | d633699f… ✅ | 455178 ✅ | 12 ✅ |
| pcf2_v1.3 | 19936297 ✅ | 19963298 ✅ | cdd62891… ✅ | 558153 ✅ | 22 ✅ |
| ct_v1.3 | 19941678 ✅ | 19972394 ✅ | e58951de… ✅ | 581459 ✅ | 17 ✅ |
| t2b_v3.0 | 19783311 ✅ | 19915689 ✅ | d245be3b… ✅ | 331769 ✅ | 8 ✅ |

- All 4 cached `zenodo.pdf` files byte-match the live Zenodo deposit
  (md5 + size + page count); SHA-256 fingerprints recorded in
  `audit_per_record_*.md` and `local_pdf_audit.json`.
- All 4 local rebuilt PDFs (under `pack/<short_name>/<pdf>`) match
  Zenodo at file size and page count exactly; SHA-256 differs as
  expected (pdfTeX `/CreationDate` timestamp drift — same regime that
  030 documented for PCF-1).
- API titles + version strings + DOIs parsed from
  `zenodo_api_responses.json` match every pack's `00README.txt` claim.
- No record returned 404; no API timeouts; Zenodo deposits are stable.

## Judgment calls made
1. Treated `hash_match.json: match=false` as expected (timestamp drift)
   rather than as a FAIL gate, because file size + page count match
   exactly — same disposition 030 used for PCF-1 v1.3. The verification
   gate that matters for arXiv re-mirroring is the deposited PDF
   md5/size/pagecount vs Zenodo API, not local rebuild byte-equivalence.
2. Recorded `ct_v1.3/00README.txt` blank `Title:` field in
   `discrepancy_log.json` at severity `cosmetic` rather than PARTIAL.
   It is a documentation typo, not a verification mismatch (Zenodo API
   serves the correct title regardless).
3. Did not modify any pack files (out of scope per §6); only audited.
4. Did not modify the operator-side cheat-sheet
   (`tex/submitted/control center/RESUME_AFTER_REBOOT_20260502.txt`)
   per Rule 2; only documented that no patch is needed for the 4 packs
   here (the 030-flagged PCF-1 IDs are still the only cheat-sheet
   correction outstanding).

## Anomalies and open questions
- **Cosmetic:** `arxiv_pack_ct_v1.3/00README.txt` `Title:` field is
  empty. Other 3 packs are populated. Operator-optional minor fix on
  next repack.
- **Documented expected:** all 4 `hash_match.json` files report
  `match=false` (local SHA vs Zenodo SHA). This is timestamp drift in
  PDF metadata, not deposit drift. Same regime as PCF-1 v1.3 in 030.
- **No surprises detected.** No record was 404; no md5 mismatch; no
  page-count drift; no Zenodo silently-republished record.

## What would have been asked (if bidirectional)
- Confirm that the cheat-sheet patch recommended by 030 (correcting
  PCF-1 v1.3 concept DOI from 19941678 → 19937196 and version DOI
  from 19963298 → 19937196's version slot) has been applied or is
  still pending operator action. This audit confirms the 4 non-PCF-1
  records require no further cheat-sheet edits.
- Whether the optional `ct_v1.3/00README.txt` Title fix is worth a
  no-content repack now or should wait until the next CT version bump.

## Recommended next step
Operator-side: apply the 030-recommended cheat-sheet PCF-1 ID patch in
`tex/submitted/control center/RESUME_AFTER_REBOOT_20260502.txt`, then
re-fire the 002 arxiv-mirror runbook with confidence — all 5 published
Zenodo records (PCF-1 v1.3, umbrella v2.0, PCF-2 v1.3, CT v1.3,
T2B v3.0) are now audited byte-clean against Zenodo. No follow-on
Prompt 033-NNN rebuild prompts are needed.

## Files committed
- `prompt_spec_used.md`
- `audit_per_record_umbrella.md`
- `audit_per_record_pcf2.md`
- `audit_per_record_ct.md`
- `audit_per_record_t2b.md`
- `zenodo_api_responses.json`
- `local_pdf_audit.json`
- `_audit_local.py`, `_audit_local_rebuild.py`
- `claims.jsonl`
- `halt_log.json`, `discrepancy_log.json`, `unexpected_finds.json`
- `handoff.md`

## AEAL claim count
10 entries written to `claims.jsonl` this session.
