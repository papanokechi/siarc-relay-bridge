# SCRUB-HASH-NOTE (DRAFT, not committed)

Status: draft. Commit to `main` only AFTER the STOP 3 force-push. No manifest was edited.

The history scrub rewrote the text of some files that three manifests cite by sha256. The three entries below
no longer match the files they list. All other checked entries are unaffected.

Method: each listed hash was looked up among all blobs of the pre-scrub tree (`6a15e07`) and of the
rewritten tree, in LF and CRLF forms. Raw output: `scratch\hash_note_data2.out.txt` and
`scratch\manifest_check3.out.txt`.

| # | Manifest (path in repo) | Listed sha256 (old) | File(s) it covers | New sha256, same line-ending form | Cause |
|---|---|---|---|---|---|
| 1 | `sessions/2026-05-05/P008-INPUT-PACKAGE-FOR-MSB-2026-06/p008_substrate_manifest.json` | `538b897c75908c9e25b2ad5c6f7ee8317a5906d2e7668809dbf58e7db7755b79` (CRLF form) | `sessions/2026-05-05/P008-INPUT-PACKAGE-FOR-MSB-2026-06/S4_t2b_v3.1.tex` and its twin `sessions/2026-05-07/PCF-2-V2-BIPARTITION-PROMOTION/t2b_paper_v3.1_bipartition_promotion.tex` | `5bf9adf493fc22fc1fb73abd2fd52be387f8dac96befd7d22333b5d944a4ac23` (CRLF); LF form `53176472901d9c13aa01e1c035a6c0717dfff75fa4e5983a44258cc3470877d6` | One `\email{...}` line: the old personal address was replaced by the contact address. |
| 2 | `sessions/2026-05-08/P008-INPUT-PACKAGE-FOR-MSB-2026-06/p008_substrate_manifest.json` | `538b897c75908c9e25b2ad5c6f7ee8317a5906d2e7668809dbf58e7db7755b79` (CRLF form) | same two `.tex` files as row 1 | same as row 1 | Same cause as row 1. |
| 3 | `sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/m6_substrate_manifest.json` | `aae81fa1a33bb2919bab68f231ca8c4e98476b5336e02bd3066070fa4cc15633` (LF form) | `sessions/2026-05-08/P008-INPUT-PACKAGE-FOR-MSB-2026-06/p008_input_package_for_msb_2026-06.md` | `7dd3370f46ff62265424a0e22b453fc8cd3db1e47677d160389e56f9f5bf49c1` (LF); CRLF form `7670a86d2d195ad7a189f7460bf0c7198367f14baad591bbd9cb287694019c7e` | 6 lines held a local Windows user path; the user name was replaced by `USER`. |

Rows 1 and 2 are one file pair, counted twice because two manifests list it. In total: 3 entries, 2 distinct file hashes.

## To recover the old content

The pre-scrub files are in the local backup `C:\LocalWork\siarc-backup-before-scrub.bundle`. They contain the
personal strings the scrub removed, so they are not to be republished.

## Not caused by the rewrite

- `sessions/2026-05-18/T3B-VQUAD-EXCL-PEGZ3/manifest.json` and `sessions/2026-05-19/T3B-VQUAD-EXCL-T2PRIME/manifest.json`
  each have one self-referencing entry that did not match before the rewrite either.
- 37 entries reference files outside the repository and cannot be checked from it.
- 91 entries match in both the old and the rewritten tree.

## Also changed in their own text (not hash mismatches)

Six manifest files had `C:\Users\<name>\...` lines rewritten to `C:\Users\USER\...`. Their own hashes are not
listed by any other manifest.
