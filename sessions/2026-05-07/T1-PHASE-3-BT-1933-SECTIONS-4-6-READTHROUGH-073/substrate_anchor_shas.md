# 073 Substrate-Anchor SHAs (I.8)

**Session:** T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073.
**Date:** 2026-05-07.
**Computation:** PowerShell `Get-FileHash -Algorithm SHA256` over every
file in the 073 session directory.

## Source-paper anchors (referenced from outside the 073 directory)

| Slot | Artefact | SHA-256 (lowercase, full 64 hex) | Size (B) |
| --- | --- | --- | --- |
| Adams-1928 | `literature/adams_1928_trans_ams_30.pdf` | `d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18` | 1 266 209 |
| 03 | `literature/bt_1933_acta_60.pdf` | `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6` | (per slot ledger) |
| D2-v2.1 | `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.pdf` | `a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e` | 443 759 |

## In-session deliverables (this directory)

| File | SHA-256 | Size (B) |
| --- | --- | --- |
| `_d2_note_v21_text.txt` | `0a45847117646216c24204ef17bf3d49419e5354d658dbdb9816d98d76d95a71` | 31 952 |
| `adams_bt_ladder_map_v2_with_bt_4_6.md` | `dc3b048c39aca27a8f0adfaab922ffaa0e54e394b7b1ece301ab5b3e76da54b1` | 11 917 |
| `bt_1933_pypdf_text.txt` | `0bf983cbd5109fb15df536795c0494c49817039c802384598147d69c209a7692` | 141 283 |
| `bt_1933_section_4_claim_table.md` | `2c14404dd9ee0ca022364907df8f5d1e9b746c4d6ca7fb81e5b624d482867b41` | 6 638 |
| `bt_1933_section_4_extract.md` | `b3abede24ff368d088cabbf0a92044e7ca5ffbf739dd5fa9e7f92a62e3022f83` | 18 891 |
| `bt_1933_section_5_claim_table.md` | `00103c17ff3b7a99cc4fc248684f77ea83185b2ca9f6fe1376d6509590826750` | 8 406 |
| `bt_1933_section_5_extract.md` | `ec2c0d5a2dadef3b3b5342869fff31b5ae7644efe84853512485ffbc014e6b97` | 15 440 |
| `bt_1933_section_6_claim_table.md` | `64bd696b3108403c0dd0f29f70a3a633520dd2726dcfd0d2c54009d2bf70f1a1` | 7 259 |
| `bt_1933_section_6_extract.md` | `744a197dec758e0dbb4c2ddf3c09f4bfec915d5fe9253bf1cd80d0c4dcc13734` | 7 489 |
| `bt_1933_section_index_4_6.md` | `ddf5296c950d577b775e51ee5b31f32331a867651e3c28dd39773e6b35abed10` | 3 575 |
| `bt_1933_sections_4_6_internal_xref.md` | `f170e30b3886a8ef344b11cd89b9966408477134dac86887bf8630d4c85e384a` | 11 340 |
| `bt_1933_sections_4_6_main_theorems.md` | `eddfe12431a9b29fe56cc0545ee7fac96746b16d384de48824e9eafa688ea138` | 5 976 |
| `d2_note_v21_bt_citation_audit.md` | `7cf2279aa15df44fef1e530c0d5c033090ae9b1258a76b7a6dbceb4880400dd5` | 11 443 |
| `forbidden_verb_scan.md` | `b4a1b8400bbbc2036ebe6850527f4c78e34f4a34fb7c8fd9bd4ce4e06e7c807f` | 10 819 |
| `sectorial_upgrade_gap_status_v2_with_bt_4_6.md` | `d6bc0b7f72f27a9a616589a0b33022a3ddaa4fcdbd939724092c79e79f171e5f` | 11 579 |

(`substrate_anchor_shas.md`, `claims.jsonl`, `halt_log.json`,
`discrepancy_log.json`, `unexpected_finds.json`, `handoff.md` are
written after this file and will appear in the bridge commit but are
not self-included in this SHA index since the SHA is computed before
they are written. The session bridge commit hash will fix the
final state.)

## Verification procedure (for downstream readers)

To re-verify any deliverable in this directory:

```powershell
cd siarc-relay-bridge/sessions/2026-05-07/T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073/
Get-FileHash <filename> -Algorithm SHA256
```

The hash should match the table above (16 files at the time of
writing this index).

To re-verify the source-paper SHAs:

```powershell
Get-FileHash literature/bt_1933_acta_60.pdf -Algorithm SHA256
# expect: dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6

Get-FileHash literature/adams_1928_trans_ams_30.pdf -Algorithm SHA256
# expect: d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18

Get-FileHash siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.pdf -Algorithm SHA256
# expect: a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e
```

## I.8 verdict

**SHA-256 anchors recorded for 15 files** (3 source-paper anchors +
12 in-session deliverable anchors at the time of writing this file;
the further 6 deliverables — `substrate_anchor_shas.md`,
`claims.jsonl`, `halt_log.json`, `discrepancy_log.json`,
`unexpected_finds.json`, `handoff.md` — are downstream of this index
and reach their final SHAs only at bridge-commit time).

(`bt_1933_pypdf_text.txt` and `_d2_note_v21_text.txt` are working
artefacts of the pypdf extraction step; they are kept in the bridge
session directory for reproducibility but are not "deliverables" in
the relay-prompt-listed sense.)
