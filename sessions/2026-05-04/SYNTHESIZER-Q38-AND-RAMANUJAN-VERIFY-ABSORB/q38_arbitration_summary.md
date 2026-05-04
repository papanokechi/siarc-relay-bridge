# Q38 arbitration summary — synthesizer-Claude pass 2026-05-04 ~21:40 JST

| ID | Question | Synthesizer answer | Confidence | Spec patch applied | Audit |
| --- | --- | --- | --- | --- | --- |
| Q38.1 | Sub-task scope: parallel vs sequential | ALL parallel, single ~3-4 hr session | High | None (default confirmed) | AMENDMENT 1 absorbs |
| Q38.2 | M9 sub-task keep / narrow / drop | KEEP with §6 CONTEXT amended to require surveyor to assume M6 closed at INDEX-2 final per 036 verdict | Medium | YES — §6 CONTEXT block patched with STARTING-CONTEXT REQUIREMENT note | spec L155-176 (post-amendment) |
| Q38.3 | M8b foreclosure-guard adequacy | Default — current §2 OUT-OF-SCOPE + §8 HALT_038_OUT_OF_SCOPE_NUMERICAL_REVIVAL covers it | Low (no spec read) | None | AMENDMENT 1 absorbs |
| Q38.4 | Slot 038 vs thematic re-slot | Slot 038 (default) | High | None (default confirmed) | AMENDMENT 1 absorbs |
| Q38.5 | Compute budget ~3-4 hr full vs ~2-3 hr | ~3-4 hr full (paired with Q38.2 keep) | High | None (default confirmed) | AMENDMENT 1 absorbs |
| Q38.6 | Forbidden-verb list completeness | EXTENDED — add passive voice + reflexive forms + hand-wave family | Medium-High | YES — §9 AEAL DISCIPLINE patched with extended list | spec §9 (post-amendment) |

## Spec patch summary

Two surgical patches applied to `tex/submitted/control center/prompt/038_milestone_residual_gap_survey_m4_m7_m8b_m9.txt`
(also re-staged to bridge `sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9-SPEC/prompt_spec.txt`):

### Patch 1: §6 CONTEXT (M9 sub-task starting-context requirement, Q38.2)
Added explicit STARTING-CONTEXT REQUIREMENT block referencing
036 SIARC-OKAMOTO-1987-SEC3-SCAN verdict 2026-05-04 (cokernel
Z/2 = P^∨(B_2) / Q^∨(B_2) = centre Spin(5) = Sp(2)).
Surveyor must treat M6 as closed-with-residual-zero at INDEX-2
final, not residual.

### Patch 2: §9 AEAL DISCIPLINE (forbidden-verb extension, Q38.6)
Original active-voice-only list extended to four families:
- **Active voice** (original): shows / proves / confirms / establishes / demonstrates that / implies that / follows that
- **Passive voice** (new): is shown / is proven / is established / is demonstrated
- **Reflexive forms** (new): it can be shown / it can be proven / one can show
- **Hand-wave family** (new): clearly / obviously / trivially / immediately / it is easy to see

The "it is easy to see" pattern explicitly called out as the
most-common escape route for hand-waving over a step that
should actually be checked.

## Top-of-file metadata patches

- GATES line: `DRAFT-PENDING-SYNTHESIZER-QA` → `DRAFT-PENDING-OPERATOR-FIRE-AUTHORIZATION`
- AMENDMENT 1 block inserted between metadata block and §0 GOAL
  (records all 6 Q38.* arbitration outcomes + audit trail
   pointer to this folder)

## Status

Prompt 038 post-amendment: **DRAFT-PENDING-OPERATOR-FIRE-AUTHORIZATION**.
All synthesizer-side gates resolved. Operator authorization is
the only remaining gate before researcher session fires
(~3-4 hr expected).

## Confidence calibration

Synthesizer flagged Q38.2 medium-confidence + Q38.3 low-confidence
because the synthesizer could not fetch the bridge SPEC during
arbitration (bridge URLs aren't search-engine-indexed; same
fetch limitation that produced false-positive defect flags
earlier today).

Synthesizer offered upgrade-path: "If you want me to upgrade
Q38.2 and Q38.3 to high-confidence, paste the spec body.
Otherwise the defaults are defensible."

Operator decision deferred. The Q38.2 patch has been applied
(low-cost, no risk if redundant); Q38.3 default stands (no
patch required for default confirmation). Either:
- (a) operator pastes prompt 038 spec into next synthesizer
      pass for Q38.2 / Q38.3 high-confidence verification, or
- (b) operator authorizes fire on current medium / low
      confidence (defensible per synthesizer's own framing)
