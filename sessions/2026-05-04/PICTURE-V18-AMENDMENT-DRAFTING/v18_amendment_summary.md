# v1.17 → v1.18 Amendment summary (13-delta digest)

**Spec:** PICTURE-V18-AMENDMENT-DRAFTING (Prompt 035) §0 / §2 / §3 / §7
**Outcome class:** `PARTIAL_V18_DRAFT_M6_CASE_DEFERRED` (§7 second outcome — 12 of 13 deltas absorbed cleanly; M6 Phase B.5 row in Case 3 STILL_PARTIAL_PENDING_PIVOT_DECISION because prompt 033 SIARC-PRIMARY-W-DERIVATION operator-deferred)

**v1.17 source:** `tex/submitted/control center/picture_revised_20260504.md`
- SHA-256: `5DC76D9F459D340006F23D11F165FCDB32E479AECB9222DE33979A14DA9F4255`
- size: 322 666 bytes / 3 193 lines

**v1.18 draft:** `picture_v1.18.md` (this folder)
- SHA-256: `4D852C978DD82275B7B5DBA4F458F10FB6C669E5E2638E7C75414E74CDBAC750`
- size: 349 145 bytes / 3 335 lines (Δ = +26 479 bytes / +142 lines)

**Diff:** `v17_to_v18.diff` (unified; `git diff --no-index`)
- SHA-256: `D5334F842B67F76CB467672A0EB3D2FC1C31155D336E5ADF57B2B009FCD047A3`
- size: 35 442 bytes / 196 lines

## 13-delta digest (one row per delta)

| # | Row id / scope | Status change | Cite list (handoff SHA-16) |
|---|----------------|----------------|----------------------------|
| 1 | G24 (PCF-2 v1.3 §6 Phase-2 anomaly) | ANCHOR-PARTIAL → CLOSED_NEGATIVELY (`UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL`) | 018 `711E10C9...AB8A` |
| 2 | G3b (i) Wasow 1965 §X.3 | ANCHOR-PARTIAL → CLOSED_VIA_OPERATOR_GATED_OA_ROUTES (image-only PDF reaffirmed) | 019 `B1FBFA91...A54A` |
| 3 | G3b (ii) Adams 1928 | ANCHOR-PARTIAL → CLOSED_VIA_TRANSITIVE_T1_A01 (`UPGRADE_ADAMS_NIA_ILL_RECOMMENDED_AMS`); spec PII typo corrected | 021 `AA4198B1...F235` |
| 4 | G3b (iii) Conte–Musette 2008 ch. 7 | ANCHOR-PARTIAL → CLOSED_VIA_COSTIN_SUBSTITUTE (`UPGRADE_CONTE_NIA_ILL_RECOMMENDED_yokohama_or_tokyo_libs`) | 028 `58F90C80...86F8` |
| 5 | G12 (PCF-1 v1.3 source state) | ANCHOR-PARTIAL → CLOSED_VIA_BRIDGE_SNAPSHOT_58DFA9E_DOI_19937196 | 027 `B4D73276...9F54` + 030 `039B0C60...8458` |
| 6 | G14 (endorser handle acquisition) | ANCHOR-PARTIAL → CLOSED_PENDING_OPERATOR_OUTREACH (3 Tier-1 handles confirmed) | 022 `BB1CA745...5F95` |
| 7 | G17 (CT v1.4 §3.5 amendment) | NEW → AMENDMENT_PENDING_READING_DECISION (Reading A vs Reading B operator gate; 4-source lit anchor) | 023 `375A9D1A...D3E8` + 026 `1E86A9B4...4D91` |
| 8 | G18 (Birkhoff–Trjitzinsky 1933 anchor) | ANCHOR-PARTIAL → CLOSED_TRIANGULATED_3_SOURCE (B-T 1933 + Sakai 2001 + Jimbo–Miwa 1981 II + Okamoto 1987 P_III parameter-pin) | 020 `2A1DE817...98A2` (2026-05-02) + 024 `5F77175D...39CD` + 025 `CDEAC35F...4F7A` + Okamoto-pin `5381C2C0...84DF` |
| 9 | M6 Q36 / Phase B.5 W cross-walk | PARTIAL → **STILL_PARTIAL_PENDING_PIVOT_DECISION** (Case 3 of §B.10; literature path exhausted; 033 deferred) | 029 `FECAD682...D3EA` + 031 `D5A39FCE...D98F` |
| 10 | §11 arxiv-pack inventory | sharpened to `UPGRADE_AUDIT_FOUR_RECORDS_ALL_PASS` (umbrella v2.0 / PCF-2 v1.3 / CT v1.3 / T2B v3.0) + PCF-1 hazard flag | 030 `039B0C60...8458` + 032 `55B7EF5C...35F7` |
| 11 | Methodology footnote (NEW) | INSERT — anchors "folklore-Lie-theory" framing for $W(B_2) \leftrightarrow W((2A_1)^{(1)})$ pending 033 | composite (#9) |
| 12 | PII typo correction | `PII-1501457-9` → `PII-1501443-6` recorded (informational; typo never landed in this file) | 021 (per delta #3) |
| 13 | Version bump + Updated timestamp | header bumped v1.17 → v1.18; new Updated 2026-05-04 17:00 JST line | (administrative) |

## Operator + Claude review path

1. **Read** `picture_v1.18.md` end-to-end (full revised file).
2. **Inspect** `v17_to_v18.diff` for spot-checking the actual edit hunks.
3. **Audit** `cross_row_consistency_audit.md` — confirm C.1–C.6 verdicts.
4. **Decide** (operator + Claude):
   - (a) **Accept v1.18 as drafted** → operator deposits to Zenodo →
     submission_log Item 20 splice (separate future agent prompt mirroring
     001 / Item 17 / 18 / 19 patches);
   - (b) **Request amendments** → drafter agent applies and re-deposits as
     v1.18.1 (in this same folder, with new diff);
   - (c) **Defer v1.18** → wait for prompt 033 to fire and absorb its
     outcome into v1.19 directly (skipping v1.18); this is a strategic
     call (operator sells one Zenodo deposit but consolidates two
     micro-cycles).

## Out-of-scope (per PICTURE-V18 §6)

- Zenodo deposit of v1.18 (operator action).
- submission_log Item 20 splice (post-deposit operator action; future agent prompt).
- M6 spec text edits (separate todo if Case 4 surfaces).
- CT v1.4 §3.5 text edits (G17 row tracks status only).
- Re-running any of 018–032 verdicts (those are inputs).
- Editing the next-prompts queue `_INDEX.txt` (operator + Claude).
- Editing umbrella v2.0 → v2.1 (separate prompt `siarc-umbrella-v2-1-dispatch`).
