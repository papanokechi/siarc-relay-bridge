# Substrate anchor SHAs — relay 068 (T1 Phase 3 M4 closure attempt)

**Task ID:** `T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068`
**Date authored:** 2026-05-07 (W20 dispatch; W21 LANE-1 ratification follows)
**Authoring tier:** T2 analytical (CLI-Synth substitute draft)
**Bridge HEAD at session start:** `ec5eaca` (`BT-BASELINE-NOTE-FOLLOWUP-V1-0-067`)

---

## 1. Primary substrate inventory

All SHA-256 hashes captured at session start by
`Get-FileHash -Algorithm SHA256` (PowerShell 7.x).

### 1.1 T1 Phase 2 substrate (P2 gate)

| File | Path | SHA-256 (16-prefix) | Bytes |
|------|------|----------------------|-------|
| Phase D verdict | `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_d_verdict.md` | `7145A00D62B9716C…` | (cited via line range L1-200) |
| Phase A summary | `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_a_summary.md` | `71CAC875C98A6CE8…` | (cited via L34-44) |
| Phase C lit verification | `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_c_literature_verification.md` | `C6CC2B1AC437647F…` | (cited via L1-100) |
| Phase 2 handoff | `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/handoff.md` | `1D4799203825029A…` | — |
| Phase 2 claims | `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/claims.jsonl` | `E725303E3EC443CD…` | — |
| Bridge commit | `37c939f` (T1-BIRKHOFF-PHASE2-LIFT-LOWER) | (git SHA) | — |

Phase 2 verdict: `UPGRADE_PARTIAL_FORMAL_LEVEL` — A_naive ≤ d+1 derived
for the normal three-convention enumeration (deg_a ∈ {d-1, d, d+1});
upper-branch lift to A=2d at d ≥ 3 framed structurally but not closed
under that enumeration.

### 1.2 LANE-2 substrate (064 supersession path)

| File | Path | SHA-256 (16-prefix) | Bytes |
|------|------|----------------------|-------|
| 064 supplement (Phase A deg_a=0 row) | `siarc-relay-bridge/sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/phase_a_supplementary_deg_a_zero.md` | `80E28568FF142B1A…` | 16792 |
| LANE-2 V6 substrate | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_substrate_verification.md` | `56063BF7BA8AD6A0…` | 15695 |
| LANE-2 P3 substrate | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_depth_probe.md` | `20764101FCDEA73A…` | 16698 |
| 065 cf_value audit | `siarc-relay-bridge/sessions/2026-05-06/PCF2-CF_VALUE-AUDIT-9IMPLS-065/cf_value_audit_pcf2_9impls.md` | `16512BCC71C9A19E…` | 11700 |
| 066 V_quad row reframing | `siarc-relay-bridge/sessions/2026-05-07/PCF1-V13-V_QUAD-ROW-REFRAMING-066/pcf1_v13_v_quad_row_reframing.md` | `79933B694DD2BF99…` | 24073 |
| 067 follow-up note .tex | `siarc-relay-bridge/sessions/2026-05-07/BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/bt_baseline_note_followup_v1_0.tex` | `F11F8A6519D6FE65…` | 18161 |
| 067 follow-up note .pdf | `siarc-relay-bridge/sessions/2026-05-07/BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/bt_baseline_note_followup_v1_0.pdf` | `E01B8F30C34DEC1E…` | 309445 |
| bt_baseline_note v1.0 .tex | `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex` | `6746692C517DC252…` | 38023 |

Verdict-ladder substrate: 064 introduces the four-row Phase A
enumeration (deg_a ∈ {0, d-1, d, d+1}), with the new deg_a = 0 row
carrying A_naive = 2d at d ∈ {2, 3, 4} (boldface in §2.3 of 064).
V6 derives the closed-form general formula A_naive = 2d - d_a
(L268-282 of V6, §V6 Step 4). 065 + 066 confirm the SIARC stratum
(PCF-2 cf_value impls + PCF-1 V_quad) sits at deg_a = 0 in 13 of 13
PCF-2 implementations and 1 of 1 PCF-1 quartic-irrational anchor.

### 1.3 Literature substrate (Costin / B-T 1933 / Wasow)

| File | Path | SHA-256 (full) | Bytes |
|------|------|----------------|-------|
| Costin 2008 Asymptotics + Borel summability (chap5 OCR txt) | `tex/submitted/control center/literature/g3b_2026-05-03/06_costin_2008_chap5.txt` | `93F1E9BF0A5FC4F65F7601F3DE357BD008AFDC892DB8F50097B16D10E415981A` | 469749 |
| B-T 1933 PDF | `tex/submitted/control center/literature/g3b_2026-05-03/birkhoff_trjitzinsky_1933.pdf` | `DCD7E3C6B2A12AE1CE917D322763FF9DDE5EC69AB5F23080D043699822D68FE6` | 3411000 |
| B-T 1933 OCR text dump | `siarc-relay-bridge/sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/_bt1933.txt` | `5FBB3E2FDC7AC71E7209DF16F60F0B6FC42D9D251B1A8821F6C93889CD910DA1` | 140094 |
| Wasow chap X PDF (image-only; OCR-deferred) | `tex/submitted/control center/literature/g3b_2026-05-03/wasow_1965_chap_X.pdf` | `F59D6835DB58D2DE59EAB843B881B97106EEE6C66E56BFCE43DE5788BBBAA5FD` | 5557950 |

Costin chap5 line ranges cited:
- §4.7a Theorem 4.147 (Watson — Gevrey-1 ↔ Borel-summability):
  L6478-6500 (operative; Phase B citation).
- §5.0c Theorem 5.11 (analytic structure of Borel transform Y0;
  resurgent singularities at lλ_j): L7724-7755 (operative; Phase B
  citation for resurgent-singularity radius bound).
- §4.4 Borel transform definition (Definition 4.96 area): L5510-5640
  (background; cited in passing).

B-T 1933 line ranges cited:
- §1 canonical-form ansatz e^{Q(x)} s(x) at p ≥ 1 (eq. 7 + 7a):
  L107-118.
- §1 normal vs anormal classification: L131-142.
- §1 Galbrun special anormal regular type at p=2 (q=2 fractional
  rank in relay-prompt notation): L150-160.
- §1 Definition 1 (s-series): L119.
- §§7-9 existence + factorization + Fundamental Theorem: covered by
  Phase 2 Phase C extracts (cited via `phase_c_literature_verification.md`
  C.1-C.5, SHA `C6CC2B1AC437647F…`).

Wasow chap X: image-only PDF on disk; **OCR not performed** in this
session (LANE-2 Item 2 sub-task 3-E DEFER discipline). Theorem 11.1
(Newton-polygon factorization) cited transitively via T1-A01 verdict
`A01_WASOW_READING_CONFIRMED` (bridge `b1457ae`).

### 1.4 PCF-2 v1.3 source + empirical anchors (P5 + P6 gate)

| File | Path | SHA-256 (16-prefix) | Bytes / lines cited |
|------|------|----------------------|---------------------|
| PCF-2 v1.3 .tex source | `tex/submitted/pcf2_program_statement.tex` | `82FE2315CFDA2047…` | 75098 B; eq. (B4) at L460-466 |
| PCF-2 v1.3 PDF (V13-RELEASE) | `tex/submitted/pcf2_program_statement.pdf` | `87B845A8E382F3C1…` | 558153 B; 22 pp |
| Session Q1 wkb_run.log (d=4 quartic empirical) | `siarc-relay-bridge/sessions/2026-05-01/PCF2-SESSION-Q1/wkb_run.log` | (cited via line range L1-200) | A_fit ≈ 7.949–7.952 across windows |
| PCF-2 v1.2 release claims | `siarc-relay-bridge/sessions/2026-05-01/PCF2-V12-RELEASE/claims.jsonl` | (cited L1) | dps=1200; A_fit cubic 5.978±0.026 / quartic 7.954±0.0037 |
| Session Q1 script | `siarc-relay-bridge/sessions/2026-05-01/PCF2-SESSION-Q1/session_q1_wkb.py` | (cited via PCF-2 v1.2 claims output_hash) | dps=1200 reproducible |
| Session C1 script | `siarc-relay-bridge/sessions/2026-05-01/PCF2-SESSION-C1/session_c1_wkb.py` | (cited via PCF-2 v1.2 claims output_hash) | dps=800; cubic harvest 50/50 |
| G24 readback handoff | `siarc-relay-bridge/sessions/2026-05-04/PCF2-V13-AFIT-DEFINITION-READBACK/handoff.md` | (cited L1-120) | verdict UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL |

Empirical anchors:
- Cubic d=3: A_fit = 5.978 ± 0.026 across 50/50 jointly harvested
  Sessions B + C1 families (dps=800; window N ∈ [200, 800]).
- Quartic d=4: A_fit = 7.954 ± 0.0037 across 60/60 lex-window quartic
  Session Q1 families (dps=1200; window N ∈ [200, 800]).
- V_quad d=2: A = 4 (PCF-1 v1.3 §6 Theorem 5; H4_EXECUTED_PASS at
  108 digits per Prompt 005 anchor; ratified by 066 row reframing).

PCF-2 v1.3 eq. (B4) verbatim (`pcf2_program_statement.tex` L459-466):
> "the convergent residual δ_n = p_n/q_n − L has leading WKB
> asymptotic … log|δ_n| = −A n log n + α n − β log n + γ + o(1)
> (n → ∞), with the sharp identification A = 2d"

G24 verdict: `UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL` —
A_fit (PCF-2 v1.3 eq. (B4)) ≡ μ_dom − μ_sub structurally (matches
T1 Phase 2 Phase A baseline). P6 gate PASSES.

---

## 2. Bridge HEAD provenance

- Session start HEAD: `ec5eaca`
  (`BT-BASELINE-NOTE-FOLLOWUP-V1-0-067` ladder commit; 2026-05-06).
- Recent landings absorbed by 068 substrate:
  - `ec5eaca` 067 (LANE-2 Item 3 + sub-task 3-C follow-up note v1.0)
  - `9261c79` 066 (LANE-2 Item 1 R1 PCF-1 V_quad row reframing)
  - `c1b8c54` 065 handoff addendum
  - `6a150b6` 065 main + 064 main (parallel deposit; 064 SHA
    `80E28568FF142B1A…`)
  - `dee3c01` LANE-2 ACCEPT_WITH_REVISIONS verdict
  - `8ed7417` PCF2-V13-AFIT-DEFINITION-READBACK verdict
  - `37c939f` T1-BIRKHOFF-PHASE2-LIFT-LOWER verdict
  - `b1457ae` T1-A01-NORMALIZATION-RESOLUTION verdict

All listed bridge commits verified by `git log --all --oneline` at
session start.

---

## 3. SHA-coverage for 7-anchor table (Phase A.1 + A.2 + A.3 readback)

The 9 anchors below are the ones cited verbatim or by line range
within the 068 deliverables (the 7 wrapper files plus the 6 phase
documents). Each anchor file carries an explicit SHA-256 prefix in
the per-deliverable citation block.

| # | Anchor description | File | SHA prefix | Cited by |
|---|---------------------|------|------------|----------|
| 1 | Phase 2 Phase D verdict | phase_d_verdict.md | `7145A00D62B9716C…` | A.1, m4_closure_attempt §3 |
| 2 | 064 deg_a=0 supplement | phase_a_supplementary_deg_a_zero.md | `80E28568FF142B1A…` | A.0, m4_closure §4, phase_d §1 |
| 3 | LANE-2 V6 substrate | independent_substrate_verification.md | `56063BF7BA8AD6A0…` | A.0, phase_d §2, m4_closure §5 |
| 4 | 065 cf_value audit | cf_value_audit_pcf2_9impls.md | `16512BCC71C9A19E…` | A.0, phase_d §3 |
| 5 | 066 V_quad reframing | pcf1_v13_v_quad_row_reframing.md | `79933B694DD2BF99…` | A.0, phase_d §3 (P9) |
| 6 | Costin chap5 (Theorem 4.147 + Theorem 5.11) | 06_costin_2008_chap5.txt | `93F1E9BF0A5FC4F6…` | phase_b §2-§3 |
| 7 | B-T 1933 §1 ansatz | _bt1933.txt | `5FBB3E2FDC7AC71E…` | phase_c §1-§2 |
| 8 | PCF-2 v1.3 eq. (B4) | pcf2_program_statement.tex | `82FE2315CFDA2047…` | A.2, phase_d §6 (G24) |
| 9 | G24 readback verdict | PCF2-V13-AFIT-DEFINITION-READBACK/handoff.md | (cited via L1-120) | A.2 |

---

*End of `substrate_anchor_shas.md`.*
