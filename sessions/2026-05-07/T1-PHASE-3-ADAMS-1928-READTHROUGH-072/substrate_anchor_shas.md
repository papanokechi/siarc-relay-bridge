# Substrate Anchor SHAs

**Session:** 2026-05-07 T1-PHASE-3-ADAMS-1928-READTHROUGH-072.
**Computed:** post all Phase E remediations, immediately before
handoff.md authoring.

## Source-substrate SHAs (read-only inputs)

| File | SHA-256 | Size (B) | Pages |
| --- | --- | --- | --- |
| `tex/submitted/control center/literature/g3b_2026-05-03/Adams-IrregularCasesLinear-1928.pdf` | `d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18` | 1 266 209 | 36 |
| `tex/submitted/control center/literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf` | `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6` | (slot 03; not re-measured) | 89 |
| `tex/submitted/control center/literature/g3b_2026-05-03/04_wasow_1965_dover.pdf` | `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd` | (slot 04; not re-measured) | (n/a in this session) |
| `tex/submitted/control center/literature/g3b_2026-05-03/06_costin_2008_chap5.txt` | `93f1e9bf0a5fc4f65f7601f3de357bd008afdc892db8f50097b16d10e415981a` | (slot 06; not re-measured) | (n/a) |

## Deliverable SHAs (committed to bridge)

Computed at the moment of handoff.md authoring. Any subsequent edit
(including handoff.md itself) will not be reflected here; the values
below are pinned to the immediately-pre-handoff state.

| Deliverable | SHA-256 |
| --- | --- |
| `adams_1928_section_index.md` | `dd4a2390cbc47da99bab177f96e046d42ea7753e53dbddaff714342ee34ad86a` |
| `adams_1928_section_1_extract.md` | `742d2ef380bf74625a55d8fa66621059c4d69963155308421e87969b70a7575d` |
| `adams_1928_section_2_extract.md` | `1c7a6daf0d54bf6a08b02a8c79bb508646318d9f1d89f82e7a50f93506f4ed98` |
| `adams_1928_section_1_2_claim_table.md` | `7c91fd0d8d52be82dedd6da9bd6b29565964a8e3c960502fcef856649716d3ab` |
| `adams_1928_main_theorems_summary.md` | `7d0fe053f517b0f845a8776bad2fe7d22e2e869fe42a66921254765d947d1164` |
| `adams_1928_bibliography.md` | `36f73142f8b52e68e50955193f92f434e254199d342d63d83e04ae66daeb39a4` |
| `adams_to_bt1933_ladder_map.md` | `60ae4328517b13ef556edda8344ea9ad924acac34cecc7a0201c8305b95abca4` |
| `sectorial_upgrade_gap_status.md` | `4e538b586d55421af08b87d9d30f38654aea3ca0469c848633021cd9b52cbc2e` |
| `forbidden_verb_scan.md` | `af562a924dbd033b8e78437a0b62505877360f5f7067426df665a579a5c7bc11` |
| `substrate_anchor_shas.md` | (this file; SHA self-referential) |
| `handoff.md` | (computed post-authoring; recorded in commit message) |
| `claims.jsonl` | (computed at AEAL deposit time) |
| `halt_log.json` | (computed at AEAL deposit time) |
| `discrepancy_log.json` | (computed at AEAL deposit time) |
| `unexpected_finds.json` | (computed at AEAL deposit time) |

## Reproducibility

To reproduce the deliverable SHAs, a future agent reading this handoff
may run, from the workspace root:

```powershell
$dir = "siarc-relay-bridge\sessions\2026-05-07\T1-PHASE-3-ADAMS-1928-READTHROUGH-072"
Get-ChildItem $dir -File -Filter *.md | Sort-Object Name | ForEach-Object {
    $h = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLower()
    "$h $($_.Name)"
}
```

The Adams 1928 PDF SHA can be reproduced via:

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath `
   "tex\submitted\control center\literature\g3b_2026-05-03\Adams-IrregularCasesLinear-1928.pdf").Hash.ToLower()
```
