# Substrate anchor SHAs — relay 067 (BT-BASELINE-NOTE-FOLLOWUP-V1-0)

This file pins every substrate SHA-256 cited in
`bt_baseline_note_followup_v1_0.tex` and in `claims.jsonl`. All
SHAs were computed locally with `Get-FileHash -Algorithm SHA256`
at draft time on 2026-05-07 (W20).

## P2 — LANE-2 substrate (canonical re-arbitration; bridge `dee3c01`)

| File (relative to repo root)                                                                                                  | SHA-256 (full)                                                     | Bytes  |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_six_item_verdict.md`                       | `541663C69A5CE86B4F5D3799B04A0334C4A27E202DD9B3E2B80AFE16EE62B917` | 18890  |
| `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_substrate_verification.md`           | `56063BF7BA8AD6A01A89FA30A3C61FCE68F4AAB0BA0DC7C8E561A81188D7B1F5` | 15695  |
| `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_depth_probe.md`                      | `20764101FCDEA73A57EE92B80C97B3EAB87C579CEEBED611FF9D2E6087B3885D` | 16698  |
| Bridge commit (LANE-2 deposit)                                                                                                 | `dee3c01` (short)                                                  | —      |

## P3 — 064 + 065 substrate (Wave 1; bridge `6a150b6`)

| File                                                                                                              | SHA-256 (full)                                                     | Bytes  |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| `siarc-relay-bridge/sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/phase_a_supplementary_deg_a_zero.md`  | `80E28568FF142B1A81C7C443368349A07A8235CE122D6C6140F88AA0D0706097` | 16792  |
| `siarc-relay-bridge/sessions/2026-05-06/PCF2-CF_VALUE-AUDIT-9IMPLS-065/cf_value_audit_pcf2_9impls.md`              | `16512BCC71C9A19ED59B808D8D070877F2160C5A7A062381C0FC9533182D3BF9` | 11700  |
| Bridge commit (064 + 065 co-deposit)                                                                              | `6a150b6` (short)                                                  | —      |

## P4 — 066 substrate (Wave 2; bridge `9261c79` = HEAD at 067 fire time)

| File                                                                                                                  | SHA-256 (full)                                                     | Bytes  |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| `siarc-relay-bridge/sessions/2026-05-07/PCF1-V13-V_QUAD-ROW-REFRAMING-066/pcf1_v13_v_quad_row_reframing.md`           | `79933B694DD2BF99793429B1A122A4BFF3260A42A93680886D5EF89B4E10FDCD` | 24073  |
| Bridge commit (066 deposit)                                                                                           | `9261c79` (short)                                                  | —      |

## P5 — bt_baseline_note v1.0 .tex (canonical, unmodified by 067)

| File                                                                                                              | SHA-256 (full)                                                     | Bytes  |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex`                              | `6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B` | 38023  |

## P6 — bt_baseline_note v1.0 PDF (Zenodo deposit; readback verified)

| File / DOI                                                                                                       | SHA-256 (full)                                                     | Bytes   |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|---------|
| `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.pdf`                             | `23022F0DE77AC8388ED584B2196C0AB995CD8CF18B2DD71EFBC0488A0F6E5B7C` | 409337  |
| Zenodo concept DOI                                                                                                | [10.5281/zenodo.20048196](https://doi.org/10.5281/zenodo.20048196)  | —       |
| Zenodo v1.0 version DOI                                                                                           | [10.5281/zenodo.20048197](https://doi.org/10.5281/zenodo.20048197)  | —       |

## PCF-1 v1.3 + PCF-2 v1.3 sources (cited in 067 bibliography)

| File / DOI                                                                                                              | SHA-256 (full)                                                     | Bytes  |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`  (PCF-1 v1.3 16pp source)                     | `E83BB377F297DBF0837FACBA257F227DF4579E6A3518C139E3146F17174BE301` | 46349  |
| PCF-1 v1.3 Zenodo concept DOI                                                                                            | [10.5281/zenodo.19937196](https://doi.org/10.5281/zenodo.19937196)  | —      |
| PCF-2 v1.3 Zenodo concept DOI                                                                                            | [10.5281/zenodo.19963298](https://doi.org/10.5281/zenodo.19963298)  | —      |

## 067 deliverables (this session)

| File                                                                              | SHA-256 (full)                                                     | Bytes  |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| `bt_baseline_note_followup_v1_0.tex`                                              | `F11F8A6519D6FE65720F6E1789E7D4CE456AF4A9A0F9C431072F2C148F60B023` | 18161  |
| `bt_baseline_note_followup_v1_0.pdf`                                              | `E01B8F30C34DEC1E7AF83C7B414416035E7B3EB0C4449967A69601C4192957AB` | 309445 |
| `bt_baseline_note_followup_v1_0.bbl`                                              | `1F82CA4F068719526C82A6BD519EBB2C2C40CBC7E95611430CBAEDB3419FDCAB` | 4714   |
| `annotated_bibliography_followup.bib`                                             | `A3B4EC4CDD643F7B312A91292D2070C72D59A0F72D82A78F8235E7DEB7FD15D3` | 6928   |
