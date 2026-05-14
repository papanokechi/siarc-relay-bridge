# Tier 3b — Copilot Agent Mode Relay Prompt Template

**Companion to:** `docs/siarc_project_instructions_v2026-05-14.md` §8.2
**Added:** 2026-05-14 (E3 out-of-cycle escalation)
**Use when:** workload shape matches §8.1 row 2 or row 3 (multi-step /
multi-file / iterative; long-running PSLQ batch). When borderline,
default to Tier 3a inline (§8 baseline) instead.

---

## When to use this template (not the §8 inline shape)

Pick **3b** if any of these are true:

- More than ~3 files will be edited
- An inner loop must iterate to a fixpoint (`lake build` until green;
  `pytest` until all-pass; PSLQ until residual below threshold)
- A cross-cutting rename / API-change propagation is required
- A response-to-referee pass across an entire paper is needed
- The work has a clear binary success criterion but no enumerable step list

Otherwise use the §8 baseline (numbered STEPS + HALT IF) under
`MODE: 3a`.

---

## Required prompt structure

Copy the skeleton below and fill every section. Do not delete fields.
If a field genuinely has no content, write `N/A` with a one-line
justification.

```
TASK: <KEBAB-CASE-TASK-NAME>
AEAL_CLASS: <computation | verification | refactor | rebuild | other>
MODE: 3b
BRIDGE: siarc-relay-bridge/sessions/<YYYY-MM-DD>/<TASK-NAME>/
BACKGROUND:
  <2-6 sentences of context. State the upstream substrate (prior bridge
  SHAs, prior verdicts, prior file states). Cite at least one verified
  SHA per upstream artefact. Pre-resolve any DOIs / arXiv IDs per the
  bibliographic identifier pre-verification rule.>

GOAL:
  <1-2 sentences. What does "done" look like? Be concrete. Examples:
  - "Bring `lean/PCF/M9/Closure.lean` to sorry-free green build."
  - "Apply Reviewer 2's 14 comments to `paper14_R3.tex` and produce
    `paper14_R4.tex` + `response_to_referee_R3.md`."
  - "Rename `pcf_v2_old_*` → `pcf_v2_*` across all .tex and .py files
    in `tex/submitted/` and `pslq/`."
  NOT a numbered step list — the Agent decomposes.>

SUCCESS CRITERIA:
  - <Binary testable condition 1, e.g., `cd lean && lake build` exits 0>
  - <Binary testable condition 2, e.g., `grep -rn 'sorry' lean/PCF/M9/`
    returns no matches>
  - <Binary testable condition 3, e.g., diff between
    `paper14_R3.tex` and `paper14_R4.tex` includes edits at all 14
    line ranges listed in the referee report>
  - <Add as many as needed. Each MUST be checkable by the Agent
    without operator input.>

ALLOWED SCOPES:
  - <glob 1, e.g., lean/PCF/M9/**>
  - <glob 2, e.g., tex/submitted/paper14_compositio/*.tex>
  - <glob 3, e.g., tex/submitted/paper14_compositio/figures/**>
  Any attempted edit outside these globs = HALT immediately.
  README / governance / change-log edits require explicit inclusion.

BUDGET:
  - Tool calls: <default 12; adjust upward only with justification>
  - Wall time: <default 30 min>
  - Inner-loop iterations: <default 5; the typical `lake build` cap>
  - Token / context budget: <if applicable>

HALT-AND-REPORT:
  - If <inner-loop fixpoint condition> not reached after BUDGET
    iterations, HALT and report current state + last error.
  - If any out-of-scope file modification is attempted, HALT
    immediately and report attempted path.
  - If any test fails with confidence < 0.9, HALT and report.
  - If any AEAL claim cannot be verified (computation produces NaN /
    inf / negative residual), HALT per standing halt-conditions rule.
  - <Add task-specific halt conditions as needed.>

DELIVERABLES:
  - <file 1 the Agent must produce>
  - <file 2>
  - handoff.md  (per STANDING FINAL STEP B3)
  - claims.jsonl (one entry per numerical / verification claim)
  - halt_log.json (empty {} if no halt triggered)
  - discrepancy_log.json (empty {} if none)
  - unexpected_finds.json (empty {} if none)

PHANTOM HIT PREVENTION (PSLQ only):
  Any PSLQ relation with L-coefficient = 0 is REJECTED. Non-negotiable.

COMMIT INSTRUCTIONS:
  - Stage the bridge session folder via `git add <BRIDGE>/`
  - Commit with message `<TASK> — <one-line result summary>`
  - DO NOT push. Operator pushes per rule 6.
  - Append the standard `Co-authored-by` trailer per git_commit_trailer.
```

---

## Examples (illustrative, do not copy verbatim)

### Example A — Lean build-until-green

```
TASK: M10-CLOSURE-LEAN-BUILD-GREEN
AEAL_CLASS: verification
MODE: 3b
BRIDGE: siarc-relay-bridge/sessions/2026-06-15/M10-CLOSURE-LEAN-BUILD-GREEN/
BACKGROUND:
  M10 V0 closure committed-by-2026-08-02 per cascade-132 sec 5
  documented-commitment route (bfcfd92 RULE 1 LIFT). Hard Lean
  discharge is OPTIONAL UPLIFT but desirable for the status report.
  Current state at lean/PCF/M10/Closure.lean: 7 sorries remaining;
  last successful `lake build` was 2026-05-12 at SHA a1b2c3d.

GOAL:
  Discharge the 7 remaining sorries in lean/PCF/M10/Closure.lean
  and produce a sorry-free green `lake build` for the M10 module.

SUCCESS CRITERIA:
  - `cd lean && lake build PCF.M10.Closure` exits 0
  - `grep -rn 'sorry' lean/PCF/M10/` returns no matches
  - No new axioms introduced (compare `#print axioms` output to
    baseline at lean/PCF/M10/baseline_axioms.txt)

ALLOWED SCOPES:
  - lean/PCF/M10/**
  - lean/PCF/M9/Bridge.lean  (read-only references only; HALT if edit attempted)

BUDGET:
  - Tool calls: 20
  - Wall time: 45 min
  - Inner-loop iterations: 8 (lake build attempts)

HALT-AND-REPORT:
  - If `lake build` still red after 8 iterations, HALT and report
    the failing module list + most recent error.
  - If any new axiom appears in `#print axioms`, HALT.
  - If any edit is attempted outside lean/PCF/M10/, HALT.

DELIVERABLES:
  - lean/PCF/M10/Closure.lean  (modified)
  - lean/PCF/M10/lake_build_log.txt
  - handoff.md, claims.jsonl, halt_log.json, discrepancy_log.json,
    unexpected_finds.json

COMMIT INSTRUCTIONS:
  - git add siarc-relay-bridge/sessions/2026-06-15/M10-CLOSURE-LEAN-BUILD-GREEN/
  - Commit message: "M10-CLOSURE-LEAN-BUILD-GREEN — 7 sorries discharged; lake build green"
  - DO NOT push.
```

### Example B — Response-to-referee multi-file pass

```
TASK: PAPER14-R3-RESPONSE-TO-REFEREE
AEAL_CLASS: refactor
MODE: 3b
BRIDGE: siarc-relay-bridge/sessions/2026-06-20/PAPER14-R3-RESPONSE-TO-REFEREE/
BACKGROUND:
  Paper14 v1.1 (Zenodo 10.5281/zenodo.20174933) returned from
  Compositio with 3 referee reports totalling 14 comments. Reports
  at tex/submitted/paper14_compositio/R3_referee_reports/.

GOAL:
  Apply all 14 referee comments to paper14_R3.tex, producing
  paper14_R4.tex + response_to_referee_R3.md with point-by-point replies.

SUCCESS CRITERIA:
  - paper14_R4.tex compiles cleanly via `pdflatex paper14_R4.tex`
  - response_to_referee_R3.md contains exactly 14 numbered responses
  - Each response cites at least one diff hunk in paper14_R3.tex → R4.tex
  - bibliography unchanged (no new \cite{} entries without operator approval)

ALLOWED SCOPES:
  - tex/submitted/paper14_compositio/paper14_R4.tex (create)
  - tex/submitted/paper14_compositio/response_to_referee_R3.md (create)
  - tex/submitted/paper14_compositio/paper14_R3.tex (READ ONLY; HALT if modified)
  - tex/submitted/paper14_compositio/figures/** (modify only if explicitly needed)

BUDGET:
  - Tool calls: 16
  - Wall time: 40 min
  - Inner-loop iterations: 3 (pdflatex passes)

HALT-AND-REPORT:
  - If any \cite{} key is introduced that's not in references.bib, HALT.
  - If pdflatex fails after 3 retries, HALT and report log tail.
  - If any referee comment can't be addressed without operator input
    (e.g., new mathematical claim required), HALT and report.

DELIVERABLES:
  - paper14_R4.tex
  - response_to_referee_R3.md
  - paper14_R4.pdf
  - handoff.md + standard bridge deposit artefacts

COMMIT INSTRUCTIONS:
  - git add siarc-relay-bridge/sessions/2026-06-20/PAPER14-R3-RESPONSE-TO-REFEREE/
  - Commit message: "PAPER14-R3-RESPONSE-TO-REFEREE — all 14 referee comments addressed"
  - DO NOT push.
```

---

## Drafting checklist (CLI / Synthesizer)

Before firing a Tier 3b prompt, the author confirms:

- [ ] MODE: 3b is genuinely appropriate per §8.1 (not just laziness
      to avoid enumerating steps)
- [ ] GOAL is testable, not aspirational
- [ ] SUCCESS CRITERIA are all binary and Agent-checkable
- [ ] ALLOWED SCOPES list is exhaustive — the Agent must HALT on
      any edit attempt outside this list
- [ ] BUDGET is realistic and tighter than the worst-case the Agent
      could reasonably need; over-budgeting risks aimless iteration
- [ ] HALT-AND-REPORT covers the inner-loop fixpoint condition AND
      out-of-scope edit attempts AND task-specific failure modes
- [ ] Phase 0 STEP 0.1-0.6 supersession-gate has been run (no prior
      LANDED fire of the same scope, no third-path resolution)
- [ ] All cited bridge SHAs pre-verified via `git rev-parse`
- [ ] All cited DOIs / arXiv IDs pre-resolved per
      bibliographic-identifier rule

---

## Authority envelope reminder (rule 6, §3)

Tier 3b has file-system + terminal authority **within** the declared
ALLOWED SCOPES + BUDGET. It does NOT have:

- `git push` authority (Operator-gated)
- `git commit -m` to `main` authority (Operator-gated; Agent commits
  to a session-folder-only staging area)
- Portal interaction authority — Zenodo, EM portal, OJS, email
  (Operator-only per rule 3)
- Authority to broaden ALLOWED SCOPES mid-session — any expansion
  requires a fresh relay prompt

If the Agent reaches a state where any of these would be needed, it
must HALT and report.
