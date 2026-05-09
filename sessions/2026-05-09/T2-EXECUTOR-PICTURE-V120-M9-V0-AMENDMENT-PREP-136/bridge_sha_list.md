# Bridge SHA list (slot 136 substrate)

**Session:** T2-EXECUTOR-PICTURE-V120-M9-V0-AMENDMENT-PREP-136
**Date:** 2026-05-09
**Resolution:** all 8 SHAs `git rev-parse` resolve at the bridge HEAD pre-fire (G1 PASS).

---

## Substrate-bridge SHAs (per prompt §0.1)

| Short hash  | Full hash                                          | Session / role |
|-------------|----------------------------------------------------|----------------|
| `887981b`   | `887981bf51860550a05ff949f0145c1687623689`         | T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135 — slot 135 LANDED 2026-05-09; umbrella v2.2 substrate-prep; FIRST realization of cascade-132 PATH_B Option α |
| `45e236c`   | `45e236c2d3f3ff690ede65762cfbfae482cd7560`         | T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137 — slot 137 LANDED 2026-05-09 21:52 JST; PCF-2 v1.4 substrate-prep; SECOND realization |
| `fd669d3`   | `fd669d347967db2e854f8e9d3725f625bf9fbc2a`         | T1-SYNTH-M9-V0-CLOSURE-PATH-CONSULTATION-CASCADE-132 — PATH_B Option α @ MEDIUM-HIGH operative decision; FIRST cross-axis (non-single-axis) M-axis consultation; FIRST cross-provider triple-witness in SIARC |
| `7f93b9e`   | `7f93b9e4d624fdfca62f5d85393b4ead35cea751`         | T1-SYNTH-M7-V0-CLOSURE-CASCADE-123 — M7 V0 canonical closure; qualifier `(SOFT-BRANCH; HARD-BRANCH-PENDING)` |
| `cb429e1`   | `cb429e1acba91ba47d1426950d924800a0b02a07`         | T1-SYNTH-M8A-RATIFICATION-CASCADE-ABSORPTION-127R — M8a V0 closure; qualifier `(ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B)` |
| `74c5630`   | `74c563022d3a2df0a4bea0088f4793170a1e64d3`         | T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R — M8b V0 closure; qualifier `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)` |
| `70d1a48`   | `70d1a4835ee0bc1f188aada9be65bb657f471730`         | PICTURE-V19-CONSOLIDATED-DEPOSIT — last-deposited picture-chain version (2026-05-06 ~12:13 JST); **slot 136 extends v1.20 in place per PATH_α** |
| `5f9db69`   | `5f9db69c754c410b79091cbd84e6d79b63d10b6e`         | M4-V0-CLOSURE-CASCADE-106 — M4 V0 closure; cross-reference only — see ANTI-CONFLATION rule §0.5 (M4 V0 numerical content does not bleed into M7/M8a/M8b annotations or amendment rows) |

---

## Slot 070 preflight (allowed precedent — not a supersession gate)

| Short hash    | Full hash | Session / role |
|---------------|-----------|----------------|
| (path resolved) | (preflight session in `siarc-relay-bridge/sessions/2026-05-07/PICTURE-V120-LATE-FIRE-PREFLIGHT-070`) | Picture v1.20 preflight 2026-05-07; recommended GO_PRIMARY_ONLY but NEVER landed an actual v1.20 deposit; slot 136 consumes the preflight recommendation AND adds the M-axis V0 closure-series amendments. **Not a supersession gate.** |

---

## Phase 0 STEP 0.1 verification log

```
=== SHA RESOLVE TEST (G1) ===
  OK  74c5630 -> 74c563022d3a  [T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R]
  OK  45e236c -> 45e236c2d3f3  [T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137]
  OK  fd669d3 -> fd669d347967  [T1-SYNTH-M9-V0-CLOSURE-PATH-CONSULTATION-CASCADE-132]
  OK  70d1a48 -> 70d1a4835ee0  [PICTURE-V19-CONSOLIDATED-DEPOSIT]
  OK  887981b -> 887981bf5186  [T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135]
  OK  cb429e1 -> cb429e1acba9  [T1-SYNTH-M8A-RATIFICATION-CASCADE-ABSORPTION-127R]
  OK  7f93b9e -> 7f93b9e4d624  [T1-SYNTH-M7-V0-CLOSURE-CASCADE-123]
  OK  5f9db69 -> 5f9db69c754c  [M4-V0-CLOSURE-CASCADE-106 (xref only)]
```

**G1 PASS — 8 / 8 SHAs resolve at bridge HEAD.**
