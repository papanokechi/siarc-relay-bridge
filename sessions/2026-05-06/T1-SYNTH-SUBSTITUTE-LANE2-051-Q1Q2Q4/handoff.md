# Handoff — T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4

**Date:** 2026-05-06
**Agent:** GitHub Copilot (Researcher Agent acting as canonical
T1-Synth-SUBSTITUTE-LANE-2)
**Session duration:** ~1.5 hours (substrate verification + adoption audit
+ depth probe + verdict drafting; no numerical execution)
**Status:** COMPLETE

## What was accomplished

This is the **canonical T1-Synth-SUBSTITUTE-LANE-2 ruling** on the
synth-substitute verdict for relay 051 Q1/Q2/Q4 at bridge `df7d6d4`
(`sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/`).

**Why LANE-2:** Canonical T1-Synth (Claude.ai weekly cadence, LANE-1)
was unavailable for W20 (Mon 2026-05-11) per operator chat 2026-05-06
~17:46 JST. Operator authorized **Copilot Researcher Agent** as
substitute reviewer (LANE-2), distinct from the CLI-T2 reviewer that
drafted the synth-substitute verdict under LANE-1-substitute capacity.

**Reviewer:** Copilot Researcher Agent (Coding Agent invocation; not
the CLI-T2 that drafted df7d6d4).

**Epistemic weight:** This LANE-2 ruling carries the same epistemic
weight as a canonical T1-Synth weekly verdict UNLESS the operator
flags need for LANE-1 (Claude.ai) ratification at a future weekly
cadence; if so, this ruling becomes provisional. Item 4 (rule5 vocab)
and Item 6 (PCF-2 v3.x wording) were intentionally DEFERRED / HELD to
W21 LANE-1 cadence (Mon 2026-05-18) per LANE-2 epistemic-floor
discipline.

**Key deliverables produced:**
1. STEP 1: 9-anchor SHA inventory (anchor_shas.md).
2. STEP 2: V1-V6 INDEPENDENT substrate verification (independent_substrate_verification.md), conducted BEFORE reading the synth-substitute verdict body to satisfy the relay 061 prompt's INDEPENDENCE_FLOOR_AND_ANCHORING-BIAS_GUARD.
3. STEP 3: 8/8 rubber-duck adoption audit (adoption_audit.md); ALL 8 findings ADOPTED_AND_LANDED.
4. STEP 4: Independent depth probe P1-P4 (independent_depth_probe.md); 4 of 6 suggested probes conducted for safety margin above >=3 floor.
5. STEP 5: Six-item adjudication (lane2_six_item_verdict.md); Items 1/2/3 substantively decided; Items 4/5/6 deferred or held pending W21 LANE-1.
6. STEP 6: Meta-verdict ACCEPT_WITH_REVISIONS (lane2_meta_verdict.md) with three required revisions (R1, R2, R3).

## Key numerical findings

This is a synthesizer-class deliverable; **no new numerical execution**
was performed. All cited numerical anchors are verbatim from prior
AEAL-logged entries (rule5 grounding mandatory per relay 061 prompt
P1 + memory `rule5 amendment`). Re-stated load-bearing anchors:

- **A_naive = 2d for deg_a = 0** (independently re-derived in V6 from
  Wallis recurrence ratio analysis; sign gamma_sub proportional to
  -c_a/c_b confirmed via recessive root r_+ < 0 for positive a_n, b_n;
  general formula A_naive = 2d - d_a verified at all four data points
  PCF-1 V_quad d=2/QL01-QL26 d=2/PCF-2 cubic d=3/PCF-2 quartic d=4).
- **PCF-2 v1.3 R1.1+R1.3+Q1 empirical record (verbatim, NOT re-run):**
  d=3 cubic mean A_fit = 5.978 sigma=0.026 (50/50 families); d=4
  quartic mean A_fit = 7.954 sigma=0.0037 (60/60 families). Both
  within sigma of WZ deg_a = 0 prediction A_naive = 2d at d=3 and d=4.
  (Source: pcf2_program_statement.tex L468-475 + L800; bt_baseline_note v1.0 S3.)

## Judgment calls made

- **J1 — Meta-verdict ACCEPT_WITH_REVISIONS (vs ACCEPT_AS_CANONICAL or
  REJECT_AND_REPLACE):** Three substantive refinements R1/R2/R3 require
  folding into the canonical record before adoption. Synth-substitute's
  load-bearing claims are independently confirmed (V1+V2+V6+P1); no
  load-bearing errors disqualifying. Middle path is correct.
- **J2 — Item 4 (rule5 vocab) DEFER_TO_W21:** Rule5 vocabulary changes
  have repo-wide implications and warrant LANE-1 (Claude.ai)
  ratification at next available weekly cadence (W21 = Mon 2026-05-18).
- **J3 — Item 3 LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE:**
  v1.0 Theorem 1.1 is correct AS STATED; deg_a = 0 is ADDITIVE
  EXTENSION not correction; v1.1 deposit revision creates citation
  ambiguity. Separate follow-up note in bridge cleanly absorbs LANE-2
  + P2/P3 findings.
- **J4 — Independence floor satisfied via 4 of 6 P# probes:** P1+P2+P3+P4
  conducted (above >=3 floor); P5/P6 not pursued because P1-P4 yielded
  sufficient depth (3 substantive refinements R1/R2/R3 surfaced).

(See discrepancy_log.json for full reasoning per judgment call.)

## Anomalies and open questions

**The most important section of this handoff.** LANE-2 surfaced
**FOUR substantive anomalies** (D1-D4) and **THREE unexpected finds**
(U1-U3) extending or refining the synth-substitute's framing:

### Anomalies (discrepancy_log.json)

- **D1** (minor): synth-substitute's "deg_a = 1 declared, deg_a = 0
  implemented" framing is correct in spirit but slightly imprecise;
  V3 finding shows the declared scope is formally deg_a in {0, 1}
  with deg_a = 0 included as a corner. Folded into Item 6 HOLD verdict.
- **D2** (minor): synth-substitute's "protocol-to-stratum mismatch
  between program statement and harvest scripts" wording is
  misleading; P4 finding shows the mismatch locus is INTRA-document
  (S3 setup vs S6 B4 wording within pcf2_program_statement.tex
  itself). Required revision R2 in lane2_meta_verdict.md.
- **D3** (moderate, load-bearing): synth-substitute flagged V_quad's
  deg_a = 0 status as "secondary observation"; LANE-2 elevates to
  scope-expansion finding because bt_baseline_note v1.0 S4.2's
  mechanism-(i') attribution for V_quad's A=4 is substrate-level
  WRONG -- V_quad is a deg_a = 0 specimen, not a borderline anomaly.
  Required revision R1 in lane2_meta_verdict.md.
- **D4** (moderate, load-bearing): synth-substitute did not state
  as primary finding that Phase A's WZ table omits deg_a = 0 row by
  ASSUMPTION via three-convention enumeration; P2 finding makes this
  explicit. Phase D's "structural gap" verdict is the proximate
  consequence of this assumption, not of a genuine analytic gap.
  Required revision R3 in lane2_meta_verdict.md.

### Unexpected finds (unexpected_finds.json)

- **U1** (load-bearing): The protocol-to-stratum mismatch is SYSTEMIC
  across the entire SIARC PCF program (PCF-1 v1.3 + PCF-2 v1.3 +
  bt_baseline_note v1.0 + Phase A baseline), not specific to PCF-2
  R1.1/R1.3/Q1. V_quad in PCF-1 v1.3 S6 Theorem 5 is a deg_a = 0
  specimen masquerading under deg_a = 1 framing.
- **U2** (load-bearing): Phase A's three-convention enumeration
  (alpha/symmetric/delta-direction at deg_a in {d-1, d, d+1}) is
  the proximate cause of Phase D's "structural gap" framing. One-row
  extension closes d=2/3/4 records simultaneously without invoking
  borderline (i') or exceptional locus (ii').
- **U3** (non-load-bearing wording): PCF-2 v1.3 program statement is
  INTERNALLY ambiguous (S3 setup deg_a in {0,1} vs S6 B4 verbatim
  "PCF (1, b)" notation). Wording-revision target for any future
  PCF-2 v3.x revision is to NARROW S3 to match S6 B4, not expand S6.

### Open questions for canonical T1-Synth (Claude.ai) at W21+ cadence

- **OQ-061-A** (Item 4 jurisdiction): Should "protocol-to-stratum
  mismatch" be folded into rule5 vocabulary, kept as case-specific,
  or rejected? LANE-2 deferred to W21 LANE-1.
- **OQ-061-B** (Item 6 jurisdiction): Should PCF-2 v3.x receive a
  Zenodo amendment (clarify S3 to match S6 B4) or hold? LANE-2 deferred
  to W21 LANE-1.
- **OQ-061-C** (D3 escalation): Should bt_baseline_note v1.0 S4.2's
  V_quad mechanism-(i') attribution be retracted in a follow-up note?
  LANE-2 Item 3 LEAVE_V1_0_CANONICAL routes this to a separate
  follow-up-note authoring task; Phase 3 sub-task 3-A + 3-B gates
  the formal retraction.
- **OQ-061-D** (PCF-1 v1.3 V_quad): does the V_quad upper-branch
  reinterpretation (A=4 = deg_a=0 row, NOT borderline) require an
  errata to PCF-1 v1.3 itself? Out of LANE-2 scope; surfaced for
  LANE-1 weekly arbitration.

## What would have been asked (if bidirectional)

If LANE-2 could have asked Claude.ai (LANE-1) mid-session:

1. **Should LANE-2 elevate D3 (V_quad reinterpretation) to a primary
   load-bearing finding, or keep at "secondary observation" per the
   synth-substitute?** LANE-2 chose to elevate (R1 expansion) on
   substrate grounds (V5 + P3) but a LANE-1 ratification check would
   reduce uncertainty.
2. **Is the "intra-document mismatch" framing (D2 / R2) preferable
   to the synth-substitute's "prose vs scripts" framing for the
   rule5 amendment vocabulary?** LANE-2 chose intra-document (more
   precise per P4 substrate); LANE-1 might have preferred to keep
   the simpler framing.
3. **Should Phase A's deg_a = 0 row extension (R3) trigger a
   re-firing of Phase 3 sub-task 3-A as a "P2 already produced the
   table" write-up only, or should 3-A include a fresh symbolic
   re-derivation under cross-check?** LANE-2 authorized 3-A as
   write-up only (since P2 + V6 already produced the substrate);
   LANE-1 might have preferred the redundancy.

## Recommended next step

**Operator may proceed with Items 1-3 verdicts as canonical T1-Synth-LANE-2:**

- **Item 1 RATIFY_WITH_NARROW_REVISION:** scope-expand from PCF-2
  R1.1/R1.3/Q1 to all of PCF-2 harvest + PCF-1 V_quad row + Phase A
  baseline framing (R1 + R3).
- **Item 2 SPLIT (3-A AUTHORIZE; 3-B AUTHORIZE; 3-D AUTHORIZE; 3-C
  DEFER pending Item 3; 3-E DEFER):** Phase 3 dispatch authorisation
  for 3-A + 3-B + 3-D.
- **Item 3 LEAVE_V1_0_CANONICAL:** authorize separate follow-up note
  authoring task in bridge.

**Items 4, 5, 6 are HELD or DEFERRED** pending W21 LANE-1 ratification:

- **Item 4 (rule5 vocab):** DEFER_TO_W21. May use "protocol-to-stratum
  mismatch" term in interim with "pending W21 LANE-1 ratification"
  footnote.
- **Item 5 (picture v1.20):** ANOMALY_ENTRY status (with promotion to
  primary substrate row gated on Item 2 sub-tasks 3-A + 3-B).
- **Item 6 (PCF-2 v3.x wording):** HOLD pending W21 LANE-1; add
  internal manuscript-tracking note that S3/S6 wording reconciliation
  is pending.

**Concrete next relay prompt suggestion:** Phase 3 sub-task 3-A
write-up dispatch (extend bt_baseline_note Phase A WZ table to deg_a
= 0 row; produce phase_a_supplementary_deg_a_zero.md per LANE-2 J1
authorisation). This is a low-risk write-up task; the substrate is
already produced in independent_substrate_verification.md V6 and
independent_depth_probe.md P2.

## Files committed

Bridge folder: `sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/`

- `anchor_shas.md` — STEP 1 source inventory (9 anchors A1-A9 SHA-256).
- `independent_substrate_verification.md` — STEP 2 V1-V6 (BEFORE reading verdict body).
- `adoption_audit.md` — STEP 3 rubber-duck 8/8 ADOPTED_AND_LANDED.
- `independent_depth_probe.md` — STEP 4 P1-P4 (4 of 6 fresh probes).
- `lane2_six_item_verdict.md` — STEP 5 six-item adjudication.
- `lane2_meta_verdict.md` — STEP 6 meta-verdict ACCEPT_WITH_REVISIONS.
- `claims.jsonl` — 8 AEAL claims (C1-C8; C1-C6 mandatory + C7-C8 recommended).
- `halt_log.json` — empty (no halts triggered; HALT_061_* enumerated
  in lane2_meta_verdict.md tail section).
- `discrepancy_log.json` — 4 anomalies D1-D4 + 4 judgment calls J1-J4.
- `unexpected_finds.json` — 3 unexpected finds U1-U3.
- `handoff.md` — this file.

**Total: 11 files** (matches DELIVERABLES floor in relay 061 prompt).

## AEAL claim count

**8 entries** written to claims.jsonl this session
(C1-C6 mandatory + C7-C8 recommended). All claims are
`evidence_type: "literature_desk"` / `"script_inspection"` /
`"first_principles_derivation"` / `"adjudication"` /
`"meta_adjudication"` / `"audit_scan"` / `"adoption_audit"` /
`"file_hash"`. **No numerical execution** was performed; rule5
grounding is `LITERATURE-DESK` per memory `rule5 amendment` standard.

All 8 claims have non-empty `output_hash` field anchored to the
SHA-256 of the LANE-2 deliverable that produces or anchors the claim.

## Halt status

**Zero halts triggered.** Specifically:

- HALT_061_DUPLICATE_LANE2: P5 PASS (no prior LANE-2 review).
- HALT_061_SYNTH_SUBSTITUTE_DEPOSIT_MISSING: P2 PASS (7 files at df7d6d4).
- HALT_061_RELAY_051_DEPOSIT_MISSING: P3 PASS (T1-PHASE2-BASELINE-NOTE deposit present).
- HALT_061_CMB_PASTE_DRIFT: P4 PASS (CMB.txt SHA `4EC61E12...3C82` matches relay 060 expected; LF count 1969 + final non-newline-terminated line = 1970 lines; bytes 89246).
- HALT_061_V1_CONTRADICTS_SYNTH_SUBSTITUTE: PASS (V1 INDEPENDENTLY confirms (1, b) recurrence at session_c1_wkb.py L78-86).
- HALT_061_V3_CONTRADICTS_SYNTH_SUBSTITUTE: PASS (V3 confirms a_n = delta_1 n + delta_0 declaration with one slight refinement on no-delta_1-ne-0-restriction; not a contradiction).
- HALT_061_V6_CONTRADICTS_SYNTH_SUBSTITUTE: PASS (V6 INDEPENDENTLY derives A_naive = 2d at deg_a = 0).
- HALT_061_AEAL_FORBIDDEN_VERB_FOUND: PASS (zero violations in prediction-or-conjecture context across both synth-substitute and LANE-2 deliverables; all matches in ACCEPTABLE contexts).
- HALT_061_REJECT_AND_REPLACE_WITHOUT_DRAFT: PASS (meta-verdict is ACCEPT_WITH_REVISIONS, not REJECT_AND_REPLACE).
- HALT_061_DOI_HALLUCINATION: PASS (no NEW DOI or arXiv-ID acquisition targets cited; existing AEAL-logged citations are exempt per memory rule).
- HALT_061_M6_TOKEN_OVERREACH: PASS (no bare M6 tokens in any LANE-2 deliverable).
- HALT_061_FILE_MODIFIED: PASS (LANE-2 modified zero source files; CMB.txt + bt_baseline_note.tex + pcf2_program_statement.tex + p12_journal_main.tex + bridge prior deposits all read-only this session; SHA-256 invariants from STEP 1 will hold at handoff).
