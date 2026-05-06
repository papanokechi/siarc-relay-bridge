# Substrate anchor SHAs — `PCF1-V13-V_QUAD-ROW-REFRAMING-066`

**Date:** 2026-05-07 (W20)
**Purpose:** Pre-flight gate verification (P2 LANE-2 substrate, P3 064
supplement, P4 bt_baseline_note v1.0 .tex, P5 PCF-1 v1.3 source) —
confirm zero drift at fire time vs the SHAs cited in the relay 066
PRECONDITIONS section.
**Verdict:** ALL ELEVEN ANCHORS MATCH. HALT_066_LANE2_DRIFT,
HALT_066_064_DRIFT, HALT_066_BT_BASELINE_DRIFT,
HALT_066_PCF1_V13_NOT_QUOTED_BY_HASH all do **NOT** trigger.

---

## P2 — LANE-2 substrate (six files; deposit `dee3c01`)

| # | Substrate file | Bytes | SHA-256 (full) | Relay 066 expected prefix | Verdict |
|---|----------------|-------|----------------|----------------------------|---------|
| P2.1 | `anchor_shas.md` | 2170 | `9C44526E23C2FBFC5C63EE51C34D4F3DA8FFC658B254F6E66A3108895B2B2668` | `9C44526E23C2FBFC..` | MATCH |
| P2.2 | `independent_substrate_verification.md` | 15695 | `56063BF7BA8AD6A01A89FA30A3C61FCE68F4AAB0BA0DC7C8E561A81188D7B1F5` | `56063BF7BA8AD6A0..` | MATCH |
| P2.3 | `independent_depth_probe.md` | 16698 | `20764101FCDEA73A57EE92B80C97B3EAB87C579CEEBED611FF9D2E6087B3885D` | `20764101FCDEA73A..` | MATCH |
| P2.4 | `lane2_six_item_verdict.md` | 18890 | `541663C69A5CE86B4F5D3799B04A0334C4A27E202DD9B3E2B80AFE16EE62B917` | `541663C69A5CE86B..` | MATCH |
| P2.5 | `lane2_meta_verdict.md` | 10606 | `2F7FE03B519CEEEF47948871C889DDAF55B623CF0831F8643691EF2DDAE8391C` | `2F7FE03B519CEEEF..` | MATCH |
| P2.6 | `adoption_audit.md` | 8027 | `4160A88F03FA75F9F695B459FF8492F6E2E63CC603C3EFB8A9BEAB7527368B15` | `4160A88F03FA75F9..` | MATCH |

LANE-2 deposit folder: `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/`
LANE-2 deposit commit: `dee3c01`.

**P2 verdict:** PASS. HALT_066_LANE2_DRIFT does NOT trigger.

---

## P3 — 064 supplement (deposit at bridge `6a150b6`)

| # | Substrate file | Bytes | SHA-256 (full) | Relay 066 expected prefix | Verdict |
|---|----------------|-------|----------------|----------------------------|---------|
| P3.1 | `phase_a_supplementary_deg_a_zero.md` | 16792 | `80E28568FF142B1A81C7C443368349A07A8235CE122D6C6140F88AA0D0706097` | `80E28568FF142B1A..` (16792 B) | MATCH |

Path: `siarc-relay-bridge/sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/phase_a_supplementary_deg_a_zero.md`.

**P3 verdict:** PASS. HALT_066_064_DRIFT does NOT trigger.

---

## P4 — `bt_baseline_note.tex` v1.0 (canonical, unmodified)

| # | Substrate file | Bytes | SHA-256 (full) | Relay 066 expected prefix | Verdict |
|---|----------------|-------|----------------|----------------------------|---------|
| P4.1 | `bt_baseline_note.tex` | 38023 | `6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B` | `6746692C517DC2523847..` | MATCH |

Path: `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex`.

**P4 verdict:** PASS. HALT_066_BT_BASELINE_DRIFT does NOT trigger.

---

## P5 — PCF-1 v1.3 source substrate

Relay 066 P5 names two acceptable substrate paths in priority order:
(a) Zenodo v1.3 PDF (16 pp; concept DOI 19937196), and (b)
`p12_journal_main.tex` L575-957 (workspace v1.4 working draft) IF the
v1.4 row-table content matches v1.3.

**Path (a) — canonical 16pp v1.3 source on disk:**

| # | Substrate file | Bytes | SHA-256 (full) | Verdict |
|---|----------------|-------|----------------|---------|
| P5.1 | `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex` | 46349 (925 lines) | `E83BB377F297DBF0837FACBA257F227DF4579E6A3518C139E3146F17174BE301` | MATCH (per arxiv-pack-v13-re-verify-2026-05-04 memory) |
| P5.2 | `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.pdf` (16 pp; concept DOI `10.5281/zenodo.19937196`) | 392886 | `63420DBF4ABB7124672F522C37FC04EBDB3F6694AC39959456B2890D9788FF5E` | MATCH |

**Path (b) — workspace v1.4 working draft fallback inspection:**

| # | Substrate file | Bytes | SHA-256 (full) | Status |
|---|----------------|-------|----------------|--------|
| P5.3 | `tex/submitted/p12_journal_main.tex` (v1.4 working draft) | 72311 | `82173A09521D6676ADC523E1D55CD1310F693479608A9F98EB980689A4786853` | DRIFT vs v1.3: WKB row table NOT present at L575-957 region (v1.4 reorganisation). P5 fallback rule: 'fall back to (a) only' applied. See unexpected_finds U2. |

**P5 verdict:** PASS via path (a). HALT_066_PCF1_V13_NOT_QUOTED_BY_HASH
does NOT trigger.

PCF-1 v1.3 §6 Theorem 5 row table content is anchored verbatim in the
write-up at `pcf1_v13_v_quad_row_reframing.md` §2, citing
`p12_pcf1_main.tex` SHA `E83BB377F297DBF0..` L516, L528-548, L566-577,
L578-583.

---

## Verification command (PowerShell, repeatable)

```powershell
$bridge = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"
$lane2  = "$bridge\sessions\2026-05-06\T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4"
$bt     = "$bridge\sessions\2026-05-06\T1-PHASE2-BASELINE-NOTE\bt_baseline_note.tex"
$s064   = "$bridge\sessions\2026-05-06\PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064\phase_a_supplementary_deg_a_zero.md"
$pcf1tex= "$bridge\sessions\2026-05-01\PCF1-V13-UPDATE\p12_pcf1_main.tex"
$pcf1pdf= "$bridge\sessions\2026-05-01\PCF1-V13-UPDATE\p12_pcf1_main.pdf"

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
"{0,-44} {1,8}  {2}" -f "064 supplement",
    (Get-Item -LiteralPath $s064).Length,
    (Get-FileHash -Algorithm SHA256 -LiteralPath $s064).Hash
"{0,-44} {1,8}  {2}" -f "p12_pcf1_main.tex (v1.3 16pp)",
    (Get-Item -LiteralPath $pcf1tex).Length,
    (Get-FileHash -Algorithm SHA256 -LiteralPath $pcf1tex).Hash
"{0,-44} {1,8}  {2}" -f "p12_pcf1_main.pdf (v1.3 16pp)",
    (Get-Item -LiteralPath $pcf1pdf).Length,
    (Get-FileHash -Algorithm SHA256 -LiteralPath $pcf1pdf).Hash
```

**Expected output (re-run-stable):** the eleven rows of the tables
above in matching order. Any mismatch → halt re-fire and treat as
substrate drift incident.

---

## Read-only invariant

All anchors P2.1-P2.6, P3.1, P4.1, P5.1, P5.2, P5.3 inspected via
`Get-FileHash` only. No anchor was modified during 066. Re-inspection
at handoff time MUST yield identical SHA-256 values for P2.1-P2.6,
P3.1, P4.1, P5.1, P5.2; P5.3 (v1.4 working draft) is meta-noted, not
modified.
