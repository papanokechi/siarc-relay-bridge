# Prompt spec used — SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-ABSORB

This is a synthesizer-output absorption task, not a heavy-AEAL
relay execution. No formal prompt spec was used in the
conventional sense.

The triggering input was the operator-pasted synthesizer-Claude
response 2026-05-04 ~22:06 JST (captured verbatim in
`synthesizer_response_verbatim.md`).

## Implicit task spec

Per autopilot mode + standing instructions, the absorption task
implicit spec was:

1. Patch prompt 038 in workspace per Q38.1-Q38.6 arbitration
   results (apply patches required by Q38.2 / Q38.6; confirm
   defaults for Q38.1 / Q38.3 / Q38.4 / Q38.5; advance lifecycle
   from DRAFT-PENDING-SYNTHESIZER-QA → DRAFT-PENDING-OPERATOR-
   FIRE-AUTHORIZATION).

2. Re-stage prompt 038 SPEC to bridge folder
   `sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-
   M8B-M9-SPEC/prompt_spec.txt` (overwrite with post-amendment
   version).

3. Apply Track 2 Ramanujan Journal verification facts to
   workspace `tex/submitted/CMB.txt` (RAMANUJAN JOURNAL VERIFIED
   FACTS block in DAILY DECISION FRAMEWORK section). Surface
   Berndt EiC misattribution correction explicitly.

4. Surface portfolio collision flag (Item 17 / Item 23 dual-
   Ramanujan candidacy anti-pattern) in CMB.txt + dedicated
   audit artefact.

5. Create bridge audit deposit at
   `sessions/2026-05-04/SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-
   ABSORB/` with:
     - synthesizer_response_verbatim.md
     - q38_arbitration_summary.md
     - ramanujan_journal_verification.md
     - portfolio_collision_flag.md
     - claims.jsonl (≥ 8 AEAL)
     - handoff.md
     - halt_log.json (empty)
     - discrepancy_log.json (DISC_RAMANUJAN_001)
     - unexpected_finds.json (UNEXPECTED_001)
     - prompt_spec_used.md (this file)

6. SQL state updates:
   - Update `milestone-residual-gap-survey-m4-m7-m8b-m9-prompt038`
     description noting Q38 arbitration applied; status remains
     pending operator fire authorization.
   - New: `pcf1-meinardus-ramanujan-portfolio-collision-
     arbitration` (synthesizer-side; pending; gates on Item 17
     venue inventory).

7. git commit + push:
   `SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-ABSORB -- ...`

## Standing instruction citations

- B1-B5 standing protocol applies (bridge deposit + handoff +
  push + URL output)
- AEAL claim discipline applies (≥ 1 entry per arbitration call
  + verification fact)
- Halt conditions: standard relay halts; this absorption task
  has no novel halt conditions.

## Deferred items (out of scope for this task)

- Q38.2 / Q38.3 high-confidence upgrade (requires operator to
  paste prompt 038 SPEC into next synthesizer pass)
- Item 17 cross-domain venue inventory (separate task)
- Portfolio collision arbitration (gates on Item 17 inventory)
- Track 1 Garoufalidis pre-verification (operator-direct via
  SUSTech)
- M6 spec QA continuation (separate synthesizer queue item)
