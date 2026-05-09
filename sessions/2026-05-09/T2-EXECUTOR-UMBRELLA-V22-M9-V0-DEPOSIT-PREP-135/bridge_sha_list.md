# Bridge SHA list — T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135

**Session**: T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135
**Date**: 2026-05-09
**Bridge HEAD pre-fire**: `fd669d3` (cascade-132 PATH_B operative decision)

The 9 substrate SHAs from prompt 135 §0.1, with full hashes, session names, and one-line role descriptions. All 9 verified via `git rev-parse --verify` at Phase A G1 (see `b5_pdflatex_compile_log.md` for verification log).

| SHA (short) | Full hash                                    | Bridge session                                                              | Role                                                                                                                |
|-------------|----------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `5f9db69`   | `5f9db69c754c410b79091cbd84e6d79b63d10b6e`   | `M4-V0-CLOSURE-CASCADE-106`                                                 | M4 V0 closure (deg-`a=0` row mechanism); pre-existing v2.1 row carried forward                                       |
| `7f93b9e`   | `7f93b9e4d624fdfca62f5d85393b4ead35cea751`   | `T1-SYNTH-M7-V0-CLOSURE-CASCADE-123`                                        | M7 V0 closure (cubic / quartic borderline-anormal `A` residual; soft-branch ratification); NEW v2.2 row              |
| `cb429e1`   | `cb429e1acba91ba47d1426950d924800a0b02a07`   | `T1-SYNTH-M8A-RATIFICATION-CASCADE-ABSORPTION-127R`                         | M8a V0 closure (catalogue-wide Painlevé-test stratum labeling); NEW v2.2 row                                         |
| `74c5630`   | `74c563022d3a2df0a4bea0088f4793170a1e64d3`   | `T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R`                         | M8b V0 closure (numerical foreclosure of `|S_2|` at d=2); NEW v2.2 row                                               |
| `8ebd1eb`   | `8ebd1ebb2aff635cbd12f6fa30c974bfb5aecbd9`   | `T2-EXECUTOR-115-ROUTE-F-D7-FIXED-POINT-EXTRACTION-132`                     | Route F slot 115 numerical re-derivation (`(0,0,1/9,0)` at dps=300; `s_1` fixed-point); pre-existing v2.1 row        |
| `8a22b11`   | `8a22b11577ca9fd582d03d48d66d743cd7c7e4dc`   | `T1-SYNTH-Q4-V2-VERDICT-ABSORPTION-131`                                     | M6.CC R1 verdict absorption; pre-existing v2.1 row                                                                   |
| `883dddf`   | `883dddf2058d1e2fb93f4bd936dfa35926742cd4`   | `T1-EXECUTOR-116-UMBRELLA-V21-M9-V0-DEPOSIT-133`                            | v2.1 internal staging deposit; SUPERSEDED by v2.2 per cascade-132 PATH_B (UF-135-2)                                  |
| `fd669d3`   | `fd669d347967db2e854f8e9d3725f625bf9fbc2a`   | `T1-SYNTH-M9-V0-CLOSURE-PATH-CONSULTATION-CASCADE-132`                      | PATH_B operative decision (full M-axis V0 closure series; v2.0 → v2.2 version-skip)                                  |
| `4816ebc`   | `4816ebc87ccbff03b1f78889a2dec1a540de7c84`   | `T1-SYNTH-M6CC-RESIDUAL-TRIAGE-134`                                         | M6.CC residual triage post-115 (0/5 residuals KEEP; 5/5 absorbed); cited in sec:closure-cascade-m6 body              |

## Inherited (non-§0.1) SHAs cited in body

These are inherited from v2.1 baseline and remain in v2.2 unchanged (not in the prompt 135 §0.1 verification list, but present verbatim in the umbrella source):

| SHA (short) | Bridge session                                          | Role                                                                                |
|-------------|---------------------------------------------------------|-------------------------------------------------------------------------------------|
| `10b5cf6`   | `T1-OPERATOR-Q4-ROUND2-DIRECT-DERIVATION-PACKET-130`    | M6.CC R1 substrate-direct derivation packet (Q4 v2 cascade)                          |
| `ae5b7f7`   | `T1-SYNTH-069R3-FINAL-VERDICT-ABSORPTION-124`           | 069r3 off-generic-stratum diagnosis (cited as cross-cascade convergence note)        |
| `e857172`   | (referenced in M7 closure-statement provenance)         | Prompt 014 handoff (j=0 Chowla-Selberg PSLQ source); referenced indirectly via M7 cascade record |

---

**Verification command** (Phase A G1):

```powershell
cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"
$shas = @('5f9db69','7f93b9e','cb429e1','74c5630','8ebd1eb','8a22b11','883dddf','fd669d3','4816ebc')
foreach ($s in $shas) { git rev-parse --verify $s }
```

All 9 returned full hashes; G1 PASS.
