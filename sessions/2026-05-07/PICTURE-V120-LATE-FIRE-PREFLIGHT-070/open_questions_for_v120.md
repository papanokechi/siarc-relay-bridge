# Open Questions Forward-Pointed by Picture v1.20 LATE-FIRE

This file enumerates open-question (OQ) candidates surfaced by W20-cascade
verdicts that picture v1.20 LATE-FIRE will forward-point. Entries
follow the relay 070 STEP C.1 FIXED ENTRY TEMPLATE: 4 fields exactly,
no added prose.

The W21 LANE-1 todo cross-reference column lists the SQL todo ID
pattern as a forward-pointer. Operator-side SQL lookup
(`SELECT id FROM todos WHERE id LIKE 'w21-lane1-%'`) finalises the
exact ID at LATE-FIRE time. This preflight does not query the
todos database (P7 NO CHROME ACTIVITY discipline; bridge-local only).

This preflight forward-points to existing OQs without resolving them
(STEP C.1 §"do NOT emit author-side analysis of OQ merit, scope-split,
or recommendation"). HALT_070_069R1_SCOPE_OVERREACH gate observed:
OQ-069-R1 entry below contains only the verbatim quote of 069 handoff
§Recommended next step + the W21 LANE-1 todo cross-reference. No
analytical commentary on path α/β merit is included.

---

## OQ-069-R1

- **OQ tag:** OQ-069-R1
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L78: `**P1 (HIGH) — Operator dispatch 069r1 R1-closure preflight relay** at synthesizer cadence (~1–2 h synthesizer activity). 069r1 lands a clean $(a_{1}, a_{2})$ at V_quad parameter point via path α (additional shift in $(a_0, a_1, a_2)$ chart that restores Okamoto null-sum) or path β (τ-function reparametrisation per Okamoto 1987 §3). Suggested deliverables for 069r1:`
- **Source:** bridge commit `05810a2` ·
  `sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/handoff.md`
  · line 78 (under §"Recommended next step" header at line 76)
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-069r1%'`
  (operator-side resolution pending; not queried by this preflight)

---

## OQ-068-Q1

- **OQ tag:** OQ-068-Q1
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L85-86: `Confidence MEDIUM-HIGH rather than HIGH.** HIGH was withheld pending two open inquiries: W21 LANE-1 T1-Synth ratification (RACI Tier 1 weekly cadence) AND Wasow §X.3 OCR acquisition.`
- **Source:** bridge commit `e7bfe49` ·
  `sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068/handoff.md`
  · lines 84-87 (Q1 = W21 LANE-1 T1-Synth ratification leg)
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-068-m4-ratify%'`

---

## OQ-068-Q2

- **OQ tag:** OQ-068-Q2
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L85-86: `Confidence MEDIUM-HIGH rather than HIGH.** HIGH was withheld pending two open inquiries: W21 LANE-1 T1-Synth ratification (RACI Tier 1 weekly cadence) AND Wasow §X.3 OCR acquisition.`
- **Source:** bridge commit `e7bfe49` ·
  `sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068/handoff.md`
  · lines 84-87 (Q2 = Wasow §X.3 OCR acquisition leg)
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-068-wasow-x3-ocr%'`

---

## OQ-LANE-2-R5

- **OQ tag:** OQ-LANE-2-R5 (alias: Item 5 picture v1.20 ANOMALY_ENTRY)
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L184: `- **Item 5 (picture v1.20):** ANOMALY_ENTRY status (with promotion to`
  (continues L185: `  primary substrate row gated on Item 2 sub-tasks 3-A + 3-B).`)
- **Source:** bridge commit `dee3c01` ·
  `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/handoff.md`
  · lines 184-185 (under §"6-item adjudication" or equivalent
  §"Concrete next relay prompt" preamble)
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-lane2-r5-picture-v120%'`

---

## OQ-LANE-2-R6 (alias OQ-061-D)

- **OQ tag:** OQ-LANE-2-R6 (alias OQ-061-D)
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L132-135: `- **OQ-061-D** (PCF-1 v1.3 V_quad): does the V_quad upper-branch reinterpretation (A=4 = deg_a=0 row, NOT borderline) require an errata to PCF-1 v1.3 itself? Out of LANE-2 scope; surfaced for LANE-1 weekly arbitration.`
- **Source:** bridge commit `dee3c01` ·
  `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/handoff.md`
  · lines 132-135 (under §"Open questions for canonical T1-Synth
  (Claude.ai) at W21+ cadence")
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-061-d-pcf1-v13-errata%'`

---

## OQ-048R-EARLY-FIRE

- **OQ tag:** OQ-048R-EARLY-FIRE
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L155-156: `1. **5-day-early re-fire vs scheduled Sunday primary.** The`
  (continues L156: `   048 prompt explicitly schedules "Sun: (this session —`)
- **Source:** bridge commit `6bbd3f0` ·
  `sessions/2026-05-06/W19-CLOSING-W20-WSB/handoff.md`
  · lines 155-178 (under §"Anomalies and open questions"; entry 1
  containing the 5-day-early re-fire flag)
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-048r-early-fire-disposition%'`
  (also tracked at `OQ-2026-05-06-048R-EARLY-FIRE` per CMB.txt
  OPEN QUESTIONS section paste landed at relay 059 OPT_A acceptance)

---

## OQ-055-N3-RANKING

- **OQ tag:** OQ-055-N3-RANKING
- **VERBATIM-QUOTED phrasing from source handoff.md:**
  L22: `**Arbitration judgement is RESERVED for T1 Synth W20 weekly cadence.**`
- **Source:** bridge commit `7509e34` ·
  `sessions/2026-05-06/N3-FOURTH-LAW-ARBITRATION-SUBSTRATE/handoff.md`
  · line 22 (under §"What was accomplished"; H_BSW + H_BFP + H_C
  hypothesis-ranking arbitration reserved for T1 Synth W20 weekly
  cadence)
- **W21 LANE-1 todo cross-reference:**
  `SELECT id FROM todos WHERE id LIKE 'w21-lane1-055-n3-fourth-law-rank%'`
  (Note: per relay 070 STEP C.2, if T1 Synth W20 cadence concludes
  ON SCHEDULE 2026-05-11 Sun close-of-week, this OQ may be CLOSED
  before LATE-FIRE; W21 LANE-1 is the fallback cadence if W20 weekly
  arbitration is deferred)

---

## Entry count + 069r1 single-entry guard

- Total OQ entries: 7 (OQ-069-R1 + OQ-068-Q1 + OQ-068-Q2 +
  OQ-LANE-2-R5 + OQ-LANE-2-R6 + OQ-048R-EARLY-FIRE +
  OQ-055-N3-RANKING)
- 069r1-single-entry guard: PASS (exactly 1 entry tagged OQ-069-R1;
  contains only the verbatim quote of 069 handoff §Recommended next
  step + the W21 LANE-1 todo cross-reference; zero analytical
  commentary on path α/β merit, KNY chart shift, or Okamoto §3
  τ-function reparametrisation merit)
- All 7 entries follow FIXED ENTRY TEMPLATE 4-field structure:
  PASS
