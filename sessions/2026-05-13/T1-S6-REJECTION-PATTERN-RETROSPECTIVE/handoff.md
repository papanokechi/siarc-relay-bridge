# Handoff — T1-S6-REJECTION-PATTERN-RETROSPECTIVE
**Date:** 2026-05-13
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~80 minutes
**Status:** COMPLETE — private foundational planning artefact, no public release

---

## What was accomplished

Executed Tier-1 (b) S6 rejection-pattern retrospective per the
2026-05-13 morning triage envelope (operator pick: "(b) S6
retrospective"). The corpus-review framing question — *"for each
rejection, what was the most charitable interpretation of the
editorial reasoning?"* — was applied to all 20 rejection events
across 16 unique manuscript families in the
tex/submitted/submission_log.txt corpus. Deliverable is a single
private planning document (~31 KB) at this session folder.

Three foundational outputs:

1. **Accurate rejection census** correcting the 2026-05-12 corpus
   review estimate ("13 rejections") to the verified figure (20).
2. **6-class rejection-reasoning taxonomy** mapping each rejection to
   its actionable class (A venue-state-backlog, B content-mute desk,
   C policy-disclosed, D scope-fit, E qualification-gap, F
   volume-fatigue).
3. **8 codified pre-fire action items** (A1–A8) — 3 agent-actionable
   audits, 2 operator-discipline rules, 3 manuscript-substance work
   items.

The single highest-leverage finding: **the hypothesis "the math is
fine but the framing makes it hard to review" explains 60% of
rejections cleanly** (12 of 20). The remaining 40% are
venue-state-uncontrollable (15%), manuscript-substance-policy (10%),
or inconclusive (15%). This validates the corpus-review framing as
the most-actionable single-explanation lens.

## Key numerical findings

(All 5 audit-class AEAL claims at `claims.jsonl`; bundle hash
`6244951f6104308a91f907a38c7e8f2aeb133daf1b51eb6414fd5af312e059f7`.)

- 20 distinct rejection events / 16 manuscript families / 2 author-
  side withdrawals in submission_log.txt as of 2026-05-13.
- **85%** of rejections returned no substantive content critique.
- **75%** of rejections had ≤10-day turnaround (desk-screen mode).
- **29%** of journal submissions (8/28) went to Experimental
  Mathematics before that venue was project-blacklisted at desk-
  reject n=7.
- Single most-frequent rejection-reasoning class: B (content-mute
  desk) at 35%.
- Project-blacklisted venues: 5 per `_RULES.txt` §F (ExpMath, NNTDM,
  Integers, J. Integer Sequences, Annals of Math); only 2 of those
  (ExpMath + NNTDM) appear in resubmission-relevant context, which
  is why the 2026-05-12 review cited "2 blacklists".

## Judgment calls made

1. **Did not file as Zenodo deposit.** This is a private planning
   artefact per the corpus-review S6 RULE-1 classification (J.3:
   "Foundational (planning artefact, no public release) — PERMITTED").
   Filing to Zenodo would (a) signal a structural-weakness narrative
   externally, (b) violate the corpus review's explicit "not in a
   paper — that would be unwise" instruction.

2. **AEAL evidence_type = "audit" not "computation".** Per copilot-
   instructions.md AEAL requirement ("Every NUMERICAL claim must have
   a corresponding entry in claims.jsonl"), I included entries for
   the 5 load-bearing numerical claims with `evidence_type: "audit"`
   and `dps: 0` since these are corpus-counting claims, not floating-
   point computations. All 5 reference the retrospective markdown
   hash as their `output_hash`.

3. **Counted ExpMath rejections separately from Class B
   content-mute.** In §2 taxonomy, the 7 ExpMath desk rejects are
   classified under Class F (volume-fatigue) rather than Class B
   (content-mute) because the volume-fatigue mechanism (cumulative
   submission-load gating) is editorially distinct from the
   content-mute desk pattern (one-off scope/fit screening). This
   matters for resubmission viability: Class F → blacklist venue,
   Class B → retry with framing-tweak elsewhere.

4. **Charitable interpretations are deliberately not exculpatory.**
   Where the operator made an error (Item 8 J. Adv. Res. wrong-venue
   submission; Item 25 J. Adv. Res. scope-fit pre-submit-withdrawal),
   the retrospective records the operator-side error honestly rather
   than constructing an editorial defense. Charitable-to-the-editor
   is the prompt, not charitable-to-the-author.

5. **Did not propose specific next-paper redirects.** Per S6 framing,
   this is planning-tier output, not strategy-tier. Specific venue
   choices are W21+ operator-side decisions informed by this
   retrospective but not prescribed by it.

## Anomalies and open questions

1. **Discrepancy with corpus review J.3 count (D-S6-1, LOW
   severity):** "13 rejections + 1 withdrawal + 2 blacklists" was the
   2026-05-12 reviewer's estimate with explicit accept-caveat
   ("operator should verify exact count"). Verified count is 20
   rejections + 2 withdrawals + 5 venue-blacklists (2
   resubmission-relevant + 3 precautionary). The corpus review caveat
   was correct; verification produced the canonical figures here.

2. **Title-spacing pathology is corpus-wide, not isolated (UF-S6-1,
   MEDIUM severity, HIGH leverage):** 5 distinct instances across
   the corpus. Diagnosed as systematic LaTeX→PDF→metadata pipeline
   gap. Highest-leverage agent-actionable fix in the retrospective.
   Action A1 (pre-fire ligature/spacing audit script) is the canonical
   next concrete agent task; not executed in this session because S6
   scope is retrospective + planning, not corpus-modifying.

3. **Bibliography hygiene drift (UF-S6-2, MEDIUM severity, MEDIUM
   leverage):** Rejected-venue citations not swept on each redirect.
   Two concrete recent instances (Item 27 Compositio pre-fire +
   April-10 PCF README A-STEP1-1). Action A2 (venue-reference grep
   audit) is the canonical fix.

4. **Item 5 (Khinchin @ ExpMath, in-progress 24d):** This is the
   only post-blacklist-decision ExpMath submission still live. PROMPT
   202 Q-202-8 PULL-AT-30d already locked; the verdict expected
   around 2026-05-25 will be the 8th ExpMath verdict regardless of
   outcome. Operator-aware; no new finding here.

5. **5 of 20 rejections were operator-side errors or board-policy
   inconclusives (Items 8, 22, 24, 25, indirectly 12):** These do not
   fit the framing hypothesis cleanly. Treating them as their own
   class would change the 60% figure; the retrospective treats them
   as "inconclusive" rather than "framing" to remain conservative.

## What would have been asked (if bidirectional)

Q1: Operator, do you want the retrospective also surfaced as a
SQL-todos batch (one todo per action item A1–A8) so the agent can
work them as discrete tasks under future operator gates? Or kept as
prose-only planning until W21 cycle starts?

Q2: Do you want a **shorter operator-facing brief** (e.g., 1-2 page
condensed action-list) extracted from the retrospective for daily-use
reference, separate from the 31 KB analysis document?

Q3: The Action A1 (ligature/spacing audit script) is the
highest-leverage single agent-actionable item in the retrospective.
Should I draft + commit that script in a follow-up session today, or
queue it for W21 / post-RULE-1-lift?

## Recommended next step

**Operator-facing next step:** Read the retrospective (§0 executive
summary is ~3 paragraphs; §6 action-items is the actionable list).
Decide whether to (a) action A1 now [~30-60 min agent work], (b) queue
A1–A8 as SQL todos, or (c) shelve and move to a different morning
activity.

**Agent-facing next step:** None without operator decision. SQL todo
`corpus-review-s6-rejection-retrospective` should be flipped to
`done` with citation to this session.

The remaining morning queue (DECISION 4 Prompt 209, DECISION 5
corpus-review a/b/c selection) is also unblocked by this fire — both
are LOW-cost decisions if operator wants to clear the morning queue
before larger Tier-1 (c) triple-win M-C work.

## Files committed

- `s6_rejection_pattern_retrospective.md` (31.2 KB; the analysis)
- `_retrospective_hash.txt` (SHA-256 fingerprint)
- `claims.jsonl` (5 audit-class AEAL entries)
- `halt_log.json` (empty)
- `discrepancy_log.json` (D-S6-1)
- `unexpected_finds.json` (UF-S6-1, UF-S6-2, UF-S6-3)
- `handoff.md` (this file)

## AEAL claim count

**5** entries written to `claims.jsonl` this session. All
`evidence_type: "audit"`, `dps: 0`, referencing the retrospective
markdown's SHA-256 as `output_hash`.
