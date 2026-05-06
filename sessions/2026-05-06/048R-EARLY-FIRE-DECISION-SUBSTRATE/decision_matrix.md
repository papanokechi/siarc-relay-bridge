# 048R 5-day-early-fire — decision matrix

**Tier discipline:** CLI-Synthesizer in-tier (T2). T2 *enumerates*
options and surfaces operational / AEAL implications; T1 Synth
*ranks* and *decides* in W20 weekly cadence. **No ranking,
preference, or "recommended" markers appear in this file**, per
HALT_056_RANKING_DRIFT.

**Anchor (verbatim source):** 048R bridge folder
`sessions/2026-05-06/W19-CLOSING-W20-WSB/handoff.md`,
SHA-256 `E3F6E9414DDCF69DB83BF29F40995C5A8772D7489188990A025EC368A880E7FC`,
341 lines.

**Triggering text:** §"Anomalies and open questions" item 1
(handoff L156-L184), and §"Judgment calls made" item 1
(handoff L78-L91). The closing question of §Anomalies #1 reads:

> "Flag to Synthesizer: **does the W19 closing get re-fired on
> 2026-05-10 close-of-week if any external event lands?** My
> read is that the relay 048 STEP 1 day '(this session — closing
> day)' semantics is 'the writeup happens on Sun'; re-firing 5
> days early makes the closing timestamp 2026-05-06, not
> 2026-05-10. If the Synthesizer wants the artefact dated
> 2026-05-10, recommend a brief re-fire on 2026-05-10 with
> addendum-only edits."

The 048R executer's own §Anomalies recommendation ("a brief
re-fire on 2026-05-10 with addendum-only edits") is the
substrate for OPT_2 below; it is recorded as substrate, not
as a 056-level ranking.

**Context constants:**

- 048R fire date: 2026-05-06 (Wed, W19 day 3).
- 048 prompt-header schedule: "Sun: (this session — closing
  day)"; `Drafted: 2026-05-05 ~21:55 JST (Tue, W19); Priority:
  P1 — W19 Sunday primary"`.
- Days between fire and scheduled close-of-week: **5**
  (Wed → Sun = Wed/Thu/Fri/Sat/Sun, with Sun being target).
- W19 inputs status at fire time of 048R: 044 + 045 + 046 +
  047 all landed (HEAD `78c7b16`); arc-inventory substrate
  validity is unaffected by early-fire.
- Items potentially shifting Wed-Sat 2026-05-06 → 2026-05-10:
  - P11 JTNB-2400 editorial verdict (AWAITED).
  - R5 = Okamoto 1987 §§2-3 + Conte-Musette 2008 ch. 7
    acquisition (operator-side; would unblock M6.CC).
  - M8b dispatch (would trigger 050 P-009 caveat re-render).

---

## OPT_1 — Accept 048R as canonical

**Stance:** 048R-as-fired is the W19 closing artefact; the
"Sunday primary" schedule label in 048's prompt header is
superseded by the operator's Wed dispatch.

**Implication:** `cli_log/2026-W19.md` is anchored "as of
2026-05-06"; if external events (P11 JTNB verdict, R5
acquisition, M8b dispatch) land between 2026-05-06 and
2026-05-10, they appear in the W20 WSB carry-forwards but
NOT in the W19 closing arc.

**AEAL impact:** 048R AEAL claims C1-C9 stand as recorded;
no re-anchoring needed. No new claims-file entries.

**Memory impact:** process-amendment note added to RACI
memory formalizing "operator-dispatch supersedes
prompt-header schedule" (T1 Synth weekly cadence operates
within RACI R3, not against prompt-header fire-date).

**Operational cost:** zero re-fire effort; one memory note.

**Precedent value:** medium — establishes that
operator-dispatch is the binding fire-date authority, but
does not give downstream prompts a structural template for
early-fire branches.

**Recurrence-prevention:** none — does not change the 048
prompt-spec, so future close-of-week prompts could repeat
the same 5-day-early ambiguity.

---

## OPT_2 — Require 2026-05-10 brief re-fire (addendum-only)

**Stance:** 048R is preliminary; a brief 2026-05-10
close-of-week re-fire produces the canonical artefact dated
to the actual Sunday primary date with addendum-only edits
to capture any shifts (JTNB, R5, M8b).

**Implication:** `cli_log/2026-W19.md` gets either
edited-in-place (with diff-tracked addendum) or replaced
wholesale by a 2026-05-10 fresh fire. The W20 WSB is
regenerated from the updated arc inventory.

**AEAL impact:** 048R AEAL claims C1-C9 are deposit-time-
preserved (the `[SYNTH-TRACK 2026-05-06 W19 CLOSING + W20 WSB]`
block at CMB.txt L1869+ stays bit-for-bit); the new
2026-05-10 fire produces a NEW set of AEAL claims with
explicit "supersedes 048R" citations + a `[SYNTH-TRACK
2026-05-10 W19 CLOSING (canonical re-fire)]` block.

**Memory impact:** process-amendment note formalizing
"early-fire re-fire pattern" (the 048R handoff
§Anomalies #1 already flagged this option as the executer's
read).

**Operational cost:** ~30 minutes of T2 in-tier executer
time on 2026-05-10 for the addendum-only re-fire (writing
~150-300 words of addendum text + a regenerated WSB +
SYNTH-TRACK append + bridge push).

**Precedent value:** low — case-by-case workaround; does
not give the 048 prompt-spec a structural early-fire
branch.

**Recurrence-prevention:** manual — the next close-of-week
prompt that fires early would also need a manual
addendum-only re-fire decision.

---

## OPT_3 — Amend 048 prompt-spec to add early-fire branch

**Stance:** the 048 spec template is amended to formalize an
"early-fire branch" wherein operator-dispatch on Wed-Sat
triggers a flagged-but-canonical re-fire path that does NOT
require Sunday re-anchoring.

**Implication:** future relay 048-class prompts get an
explicit P0 branch-selection step ("If fire-date <
scheduled-date, apply early-fire branch: anchor artefact
to fire-date, list shift-eligible items in §addenda-window
section"). The 048 STEP-template is rewritten to include a
§"addenda-window" section template that the executer fills
when fire-date < scheduled-date.

**AEAL impact:** no impact on 048R; 048R's AEAL claims
stand as recorded. Impact is on FUTURE close-of-week
prompts, which would carry an extra AEAL claim citing the
early-fire branch trigger and the addenda-window
population.

**Memory impact:** process-amendment note added formalizing
"early-fire branch" as a permanent prompt-spec feature for
weekly closing prompts. The note pins the trigger condition
(fire-date < scheduled-date by ≥1 calendar day) and the
addenda-window section template.

**Operational cost:** ~1 hour one-time prompt-spec
amendment + memory note + (optional) 048R retrospective
addenda-window backfill if the Synthesizer wants 048R
itself to demonstrate the branch.

**Precedent value:** high — gives future prompts a
structural template; the early-fire pattern becomes a
first-class spec feature rather than a per-fire judgment
call.

**Recurrence-prevention:** systemic — once the spec
amendment lands, future weekly closing prompts cannot
repeat the 048R ambiguity by construction.

---

## Comparison axes (T1 Synth ranks; 056 does NOT rank)

| axis                  | OPT_1   | OPT_2   | OPT_3     |
|-----------------------|---------|---------|-----------|
| re-fire effort        | 0       | ~30 min | ~1 h once |
| substrate validity    | full    | full    | full      |
| AEAL discipline       | clean   | clean   | clean     |
| precedent value       | medium  | low     | high      |
| recurrence-prevention | none    | manual  | systemic  |

**Reading guide for T1 Synth:** the axes are descriptive only.
Higher precedent / recurrence-prevention is not automatically
"better"; it depends on whether early-fire is expected to
recur (in which case OPT_3 amortizes one-time spec cost over
many future prompts) or is a one-off (in which case OPT_1
costs nothing). OPT_2 reflects the 048R executer's own
read in §Anomalies #1 and is the conservative option that
preserves the "Sunday closing" semantics at the cost of a
single re-fire round-trip.

---

## Out-of-scope reminders

- 056 does NOT modify CMB.txt directly. The recommended
  CMB §"Open questions" entry text is in
  `cmb_open_question_entry.txt`; the paste-target
  instructions are in `cmb_paste_target.md`. Operator
  dispatches the paste at next CMB session.
- 056 does NOT amend the 048 prompt-spec. OPT_3 above
  describes what a future amendment would look like; the
  amendment itself is operator-dispatched if T1 Synth
  selects OPT_3.
- 056 does NOT pre-fire a 2026-05-10 re-fire prompt. OPT_2
  above describes what the addendum-only re-fire would
  look like; the re-fire prompt itself is operator-
  dispatched on 2026-05-10 if T1 Synth selects OPT_2.

---

## End decision_matrix.md
