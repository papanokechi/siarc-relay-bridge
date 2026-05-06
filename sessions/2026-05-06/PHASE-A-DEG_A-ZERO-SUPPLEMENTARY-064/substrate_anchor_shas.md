# Substrate anchor SHAs — `PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064`

**Date:** 2026-05-06 (W20)
**Purpose:** P2 + P3 pre-flight gate verification — confirm zero drift
of LANE-2 substrate (deposit `dee3c01`) and `bt_baseline_note.tex` v1.0
between the LANE-2 commit and the 064 fire time.
**Verdict:** ALL SEVEN ANCHORS MATCH; HALT_064_LANE2_DRIFT and
HALT_064_BT_BASELINE_DRIFT do NOT trigger.

---

## P2 — LANE-2 substrate (six files)

| Substrate file | Bytes | SHA-256 (full) | Expected prefix (per relay 064 PRECONDITIONS P2) | Verdict |
|----------------|-------|----------------|---------------------------------------------------|---------|
| `anchor_shas.md` | 2170 | `9C44526E23C2FBFC5C63EE51C34D4F3DA8FFC658B254F6E66A3108895B2B2668` | `9C44526E23C2FBFC..` | MATCH |
| `independent_substrate_verification.md` | 15695 | `56063BF7BA8AD6A01A89FA30A3C61FCE68F4AAB0BA0DC7C8E561A81188D7B1F5` | `56063BF7BA8AD6A0..` | MATCH |
| `independent_depth_probe.md` | 16698 | `20764101FCDEA73A57EE92B80C97B3EAB87C579CEEBED611FF9D2E6087B3885D` | `20764101FCDEA73A..` | MATCH |
| `lane2_six_item_verdict.md` | 18890 | `541663C69A5CE86B4F5D3799B04A0334C4A27E202DD9B3E2B80AFE16EE62B917` | `541663C69A5CE86B..` | MATCH |
| `lane2_meta_verdict.md` | 10606 | `2F7FE03B519CEEEF47948871C889DDAF55B623CF0831F8643691EF2DDAE8391C` | `2F7FE03B519CEEEF..` | MATCH |
| `adoption_audit.md` | 8027 | `4160A88F03FA75F9F695B459FF8492F6E2E63CC603C3EFB8A9BEAB7527368B15` | `4160A88F03FA75F9..` | MATCH |

LANE-2 deposit folder: `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/`
LANE-2 deposit commit: `dee3c01` (HEAD as of 064 fire time).

**P2 verdict:** PASS. HALT_064_LANE2_DRIFT does NOT trigger.

---

## P3 — `bt_baseline_note.tex` v1.0 (canonical, unmodified)

| Substrate file | Bytes | SHA-256 (full) | Expected prefix (per relay 064 PRECONDITIONS P3) | Verdict |
|----------------|-------|----------------|---------------------------------------------------|---------|
| `bt_baseline_note.tex` | 38023 | `6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B` | `6746692C517DC2523847..` (38023 B) | MATCH |

Path: `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex`.

**P3 verdict:** PASS. HALT_064_BT_BASELINE_DRIFT does NOT trigger.

---

## Verification command (PowerShell, repeatable)

```powershell
$lane2 = "siarc-relay-bridge\sessions\2026-05-06\T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4"
$bt    = "siarc-relay-bridge\sessions\2026-05-06\T1-PHASE2-BASELINE-NOTE\bt_baseline_note.tex"
@("anchor_shas.md","independent_substrate_verification.md",
  "independent_depth_probe.md","lane2_six_item_verdict.md",
  "lane2_meta_verdict.md","adoption_audit.md") | ForEach-Object {
    $p = Join-Path $lane2 $_
    "{0,-44} {1,8}  {2}" -f $_, (Get-Item -LiteralPath $p).Length,
        (Get-FileHash -Algorithm SHA256 -LiteralPath $p).Hash
}
"{0,-44} {1,8}  {2}" -f "bt_baseline_note.tex",
    (Get-Item -LiteralPath $bt).Length,
    (Get-FileHash -Algorithm SHA256 -LiteralPath $bt).Hash
```

**Expected output (re-run-stable):** the seven rows of the tables above
in matching order. Any mismatch → halt re-fire and treat as substrate
drift incident.
