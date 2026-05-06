# Substrate anchor SHAs — PCF2-CF_VALUE-AUDIT-9IMPLS-065

**Method:** SHA-256 hashes captured at fire time
(2026-05-06 ~20:30 JST) for each substrate input and each
audited source file.

---

## A. LANE-2 deposit (parent substrate, bridge `dee3c01`)

| File | SHA-256 |
|------|---------|
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/handoff.md`                     | `64B7AF644A69BAD26741C945EB209A74BE22BCE0B5550F35839304AC56198915` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/anchor_shas.md`                 | `9C44526E23C2FBFC5C63EE51C34D4F3DA8FFC658B254F6E66A3108895B2B2668` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_depth_probe.md`     | `20764101FCDEA73A57EE92B80C97B3EAB87C579CEEBED611FF9D2E6087B3885D` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_substrate_verification.md` | `56063BF7BA8AD6A01A89FA30A3C61FCE68F4AAB0BA0DC7C8E561A81188D7B1F5` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_meta_verdict.md`          | `2F7FE03B519CEEEF47948871C889DDAF55B623CF0831F8643691EF2DDAE8391C` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_six_item_verdict.md`      | `541663C69A5CE86B4F5D3799B04A0334C4A27E202DD9B3E2B80AFE16EE62B917` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/adoption_audit.md`              | `4160A88F03FA75F9F695B459FF8492F6E2E63CC603C3EFB8A9BEAB7527368B15` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/claims.jsonl`                   | `422B41BBEE1940B837588D36B3C9196BEFC29F005540376EB6B68EAA887CABF8` |
| `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/discrepancy_log.json`           | `F3C593D917BCFB700B2AC01E0182285E94161E88D39F4AAD163FC435DA16BA3B` |

**Status:** All present and unmodified at session start.
HALT_065_LANE2_DRIFT did not trigger.

## B. Audited source files (`pcf-research/pcf2/`)

| # | Path                                                                     | SHA-256 (first 16 hex) |
|---|--------------------------------------------------------------------------|------------------------|
| 1 | pcf-research/pcf2/session_A_2026-05-01/cubic_family_enumeration.py       | `47476C32F7239EEB`     |
| 2 | pcf-research/pcf2/session_A2_2026-05-01/conductor7_verify.py             | `10C002157CA705B6`     |
| 3 | pcf-research/pcf2/session_B_2026-05-01/session_b_pslq.py                 | `8C709D7E7795F53C`     |
| 4 | pcf-research/pcf2/session_C1_2026-05-01/session_c1_wkb.py                | `2D43BFD55E0DB584`     |
| 5 | pcf-research/pcf2/session_Q1_2026-05-01/session_q1_wkb.py                | `F8317F53FB5D00B9`     |
| 6 | pcf-research/pcf2/session_R1_1_2026-05-01/r1_1_correlation_probe.py      | `06E8AC6F5B7B7C67`     |
| 7 | pcf-research/pcf2/session_R1_2_2026-05-01/fam32_deep_escalation.py       | `E7A5C90F3615B08C`     |
| 8 | pcf-research/pcf2/session_R1_2_2026-05-01/quartic_tail_fit_all60.py      | `FA4B8FCD0C4B7D47`     |
| 9 | pcf-research/pcf2/session_R1_2_2026-05-01/r1_2_quartic_j_probe.py        | `19B08389C4667F20`     |
|10 | pcf-research/pcf2/session_R1_3_2026-05-01/r1_3_extended_enumeration.py   | `4CC0F2014AA2E687`     |
|11 | pcf-research/pcf2/session_R1_3_2026-05-01/r1_3_family32_deep.py          | `0CCE126B8BA56958`     |
|12 | pcf-research/pcf2/session_R1_3_2026-05-01/r1_3_residualization.py        | `CC056D53CFC59328`     |

## C. This-session deliverable

| File | SHA-256 |
|------|---------|
| `repo_sweep_grep_output.txt` | `C1DA6232E73A34A43077869C41D161764674B5F9DABC61522B5634E499AC8147` |

---
