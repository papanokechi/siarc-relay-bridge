# OPT_A ACCEPTANCE — 059 disposition closure

**Decision date:** 2026-05-06 ~15:35 JST
**Decision-maker:** T0 operator (papanokechi)
**Decision channel:** CLI-Synth chat (T2 surfaced 3 options; T0 chose
OPT_A in single-token reply "OPT_A")

## Decision

**OPT_A** (accept 1921-line CMB.txt state + amend spec post-hoc).
Rejected OPT_B (manual +1 line) and OPT_C (revert + re-fire 060).

## Reasoning

1. **Content placement is bit-correct.** T2 reality-check confirmed
   CMB.txt post-SHA `723E9C60543E08B574BB4BB7CA6E9407875C4A65100CD30C83CD206699EBC3B0`,
   87 292 bytes, 1921 lines, OQ-token 1 hit + section header 1 hit
   + tail line `=====` PASS. The paste-block content matches the
   source-of-truth substrate `cmb_open_question_entry.txt` from
   `sessions/2026-05-06/048R-EARLY-FIRE-DECISION-SUBSTRATE/` verbatim.

2. **The halt was a spec defect, not a content defect.** The 059
   prompt's STEP 3 asserted `if ($lc -ne 1922) throw HALT_059_POST_LINE_COUNT`
   but the explicit NEW_STR rendered 24 lines and the OLD_STR was
   3 lines, so net delta = 21 (file 1900 → 1921, correctly).
   Headline "22 new lines" + "14-line body" in §STEP 2 both
   miscounted at draft time.

3. **OPT_B (manual +1 line) was structurally suboptimal.** No
   natural insertion point exists in the 22-new-line block: any
   added blank would either splice into the body (corrupting
   structure) or sit after the trailing `=====` (cosmetically odd
   relative to other CMB sections that end on a closing separator).

4. **OPT_C (revert + re-fire 060) was wasteful.** Reverting ~1700
   bytes of correct content + reapplying via a corrected spec
   would have consumed an additional T3 agent fire cycle solely
   to fix a 1-byte arithmetic miscount on an assertion the
   executer correctly halted on.

## Spec amendments (post-hoc; lessons stored in memory)

The 059 prompt itself remains immutable as deposit-time canonical
record. Amendments are captured as memory-class lessons applied
to FUTURE paste-class prompts:

- **L1** (subject: spec arithmetic verification): paste-class
  relay prompts must include an explicit
  `# DRAFT-TIME VERIFY: NEW_STR=<N>, OLD_STR=<M>, delta=<N-M>,
  expected post-LC=pre+delta=<X>` comment in the spec at draft
  time, computed by literal NEW_STR-line-count not by
  prose-structure-summary headcount.

- **L2** (subject: spec arithmetic verification): STEP 1 anchor
  checks should cover EVERY line of the OLD_STR (or hash the
  entire substring), not just sentinel start/end lines. For
  3-line OLD_STR: check all 3. For larger OLD_STR: byte-equality
  assertion of the substring against the file's content at the
  anchor position before attempting the edit.

## Provenance / SQL state

- `w19-relay-059-cmb-oq-paste-056-execution` → done
- `w20-operator-paste-056-cmb-open-questions` → done
- `w20-operator-decide-059-halt-disposition` → done
- Memory stored: "spec arithmetic verification" — paste-class
  prompts require literal NEW_STR/OLD_STR line-count verification
  + DRAFT-TIME VERIFY comment

## Bridge artefact integrity (deposit-time snapshot rule)

Per the SIARC AEAL deposit-time snapshot rule (memory subject:
"SIARC AEAL deposit-time snapshot rule"), the prior 059 halt
deposit at commit `7578f38` is **not** modified. The
`halt_log.json`, `discrepancy_log.json`, `claims.jsonl`, and
`handoff.md` from that fire remain as the canonical
deposit-time AEAL snapshot. This `OPT_A_ACCEPTANCE.md` is
**additive**: a new file in the same folder recording the
downstream operator decision, not a backdated edit to existing
files.

## Forward state

- CMB.txt 1921-line state is canonical going forward.
- T1 Synth W20 weekly cadence (Mon 2026-05-10 ISO / 2026-05-11
  per existing wording) consumes the §OPEN QUESTIONS FOR T1 SYNTH
  (W19 close) section's `[OQ-2026-05-06-048R-EARLY-FIRE]` entry
  and selects OPT_1 / OPT_2 / OPT_3 of the early-fire decision
  matrix (per `decision_matrix.md` of the 048R bridge session).
- Next agent-fire opportunity: 058R re-fire (CC-VQUAD-PIII
  normalization map main relay) — Tier-1 priority post-051
  Zenodo upload.

## End OPT_A_ACCEPTANCE.md
