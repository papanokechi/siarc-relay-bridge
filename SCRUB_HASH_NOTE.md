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

## Second scrub (scrub 2): files whose bytes changed and whose hash is cited elsewhere

Scrub 2 rewrote the history again, so every commit id changed. Besides text files, it replaced the three PDFs and the three JSON files listed below.
Seven files in the repository (`claims.jsonl`, `halt_log.json`, two runbooks, one metadata JSON) cite the old sha256 of the three PDFs; they are not edited and no longer match the PDFs.

| # | File | Old sha256 | New sha256 | Cause |
|---|---|---|---|---|
| 1 | `sessions/2026-05-02/D2-NOTE-DRAFT/d2_note.pdf` | `f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8` | `55b8d5c1f7ef685b7e1d09557958dc8ff370cc025094203644c2dc1b339d7c45` | Stale PDF printed an old contact address; rebuilt from the `.tex` at the same commit (which already carries the no-reply address). Text differs only on the e-mail line. |
| 2 | `sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/d2_note_v2.pdf` | `1bb2311b80808e9b6805aabf4308b3aac5cb373ca5887e8d2a328966c6eceb06` | `7dd20e252ddd9e1bb8817919a0b1b1cc13b71a6843a300cec3e34bacfd73101c` | Same cause as row 1. This is the version of the file at commit `ea78160`. |
| 3 | `sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/d2_note_v2.pdf` | `3496d5b6e0eaf992842ccfdaf3bf51aa0beecb34c3f99e76391c876072e3dc09` | `9dcc82e75dbf208dce24503e6e331769eaf2277cc788c324149584e3ee7bbedb` | Same cause as row 1. This is the version of the file at commit `7fd52e0`. |
| 4 | `sessions/2026-05-18/VENUE-RELAY-KSPSLQ-001/stage1_fingerprint.json` | `27dfe854cab08ceb42cb8cc1a552db9ff1b5b51581ce659b9ae0641c3d8f7014` | `58fcac0f6edcd509ffa5570b39dbf0cd2cb7fa136e62eebf44d414160708e33b` | Author's name replaced by `Papanokechi`; one sentence that tied the name to the ORCID record was removed (stage1: `pseudonymity_context`; unexpected_finds: the "broader portfolio" sentence). Still valid JSON. |
| 5 | `sessions/2026-05-18/VENUE-RELAY-KSPSLQ-001/stage5_ledger_and_aeal.json` | `78b71660947c815a82bc143fe9ce34fc2619e295d95fc3dc13815e91c3a4edb0` | `eb8f33b798a5c36012213333108bdd73132bb7bff3bd1a3b4a80ac62555fbcc5` | Author's name replaced by `Papanokechi`; one sentence that tied the name to the ORCID record was removed (stage1: `pseudonymity_context`; unexpected_finds: the "broader portfolio" sentence). Still valid JSON. |
| 6 | `sessions/2026-05-18/VENUE-RELAY-KSPSLQ-001/unexpected_finds.json` | `a2f4132ad80053e6e291a4f6059773998085ddcf5ed8801350125e54d8cb0b4c` | `3ee6654ccf42cf1c834382a44ee7513b4a92392b7780b8baddccf9a6bfb7cbf2` | Author's name replaced by `Papanokechi`; one sentence that tied the name to the ORCID record was removed (stage1: `pseudonymity_context`; unexpected_finds: the "broader portfolio" sentence). Still valid JSON. |

Rows 2 and 3 are two historical versions of the same path; the file at `main` today is a later, unrelated change. Each new hash above was checked against the file at the cited path in the rewritten history.

The pre-scrub-2 content is in the operator's local backup bundle. It contains the personal strings and is not to be republished.
