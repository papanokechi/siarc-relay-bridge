# Verdict — E3-TIER-3A-3B-SPLIT-IMPLEMENTATION

**Date:** 2026-05-14 (post-`8555f9f` bridge HEAD)
**Class:** E3 out-of-cycle governance escalation (operator-paste authorization)
**Trigger:** Principal Strategyzer (Tier 2) strategic recommendation — pipeline-architecture question pulled forward from 1-June MSB on M10-Lean-debt + 27-submission-revision-queue throughput grounds
**Operator authorization:** "help implement ASAP"

---

## Summary

Tier 3 single-row "Copilot agent (GitHub Copilot in VS Code)" formally split into:

- **Tier 3a — Copilot Inline** (single-step / single-file / turn-by-turn under CLI shepherding)
- **Tier 3b — Copilot Agent mode** (multi-step / multi-file / iterative; autonomous within declared session-folder + budget envelope)

The split is enforced operationally by a mandatory `MODE: 3a` or `MODE: 3b` declaration line in every relay prompt (§8 amendment) and a Tier-3b-specific template shape (§8.2 new fields: GOAL / SUCCESS CRITERIA / ALLOWED SCOPES / BUDGET / HALT-AND-REPORT) skeletoned at `docs/relay_prompt_agent_template_3b.md`. Tier 3b authority is bounded by a new Key Rule 6 mirroring Key Rule 3's portal-gate language: file-system + terminal authority within session-scope, but `git push` / `git commit -m main` / portal interaction remain Operator-gated.

---

## Strategic frame (verbatim from Synthesizer)

> Three execution surfaces, currently used asymmetrically: CLI Synthesizer (Tier 2), GitHub Copilot in VS Code (Tier 3), Copilot Agent mode inside VS Code. The gap: CLI Synthesizer writes a relay prompt → operator pastes into VS Code Copilot → in practice that's been inline-Copilot-style execution, not Copilot Agent mode. Multi-file Lean refactors / LaTeX rebuilds that *should* run as autonomous agentic loops are instead being shepherded turn-by-turn.
>
> Why this matters at portfolio scope: M10 Lean 4 mid-iteration multi-file refactor work, 27 active journal submissions with response-to-referee LaTeX edits, BibTeX hygiene, multi-file figure regeneration. **Is the Tier 3 surface configured to do the work Tier 2 thinks it's delegating? Currently, partially no.**

---

## Amendments landed

### §3 RACI table (line 49)

Before: single Tier 3 row "Copilot agent (GitHub Copilot in VS Code)".

After: two rows
- 3a — Copilot Inline (single-file / single-step examples enumerated)
- 3b — Copilot Agent mode (multi-step / multi-file / iterative examples enumerated; references §8.2 for budget envelope)

### §3 RACI matrix (workstream rows)

"Code/file execution" split into two rows:
- "Code/file execution (single-step)" → R: Copilot 3a (inline)
- "Code/file execution (multi-step / iterative)" → R: Copilot 3b (agent)

CMB / submission_log row clarified: "CLI drafts; Copilot 3a commits".
Bridge repo audit trail row clarified: "Copilot 3a or 3b".

### §3 Key Rules (appended rule 6)

> **Tier 3b authority envelope (added 2026-05-14):** Copilot Agent mode (3b) has file-system + terminal authority *within* its declared session folder + budget envelope (§8.2), BUT `git push`, `git commit -m` to `main`, and any portal interaction (Zenodo, journal portals, email) remain Operator-gated — mirror of rule 3 for Claude in Chrome. Bridge-repo audit absorption (§9) captures Agent's per-session artifacts the same way it captures inline-mode artifacts; the absorption fire itself runs as a separate Tier 3a step under CLI direction.

### §8 Relay Prompt Protocol (full rewrite)

Mandatory `MODE: 3a` or `MODE: 3b` declaration line added to baseline fields. Mode-specific field tables added (Tier 3a keeps STEPS + HALT IF; Tier 3b replaces with §8.2 fields). Phantom-hit-prevention PSLQ rule re-affirmed as MODE-invariant.

### §8.1 Mode selection guide (new)

4-row decision table mapping workload shape → MODE choice. Borderline default = 3a (Agent mode is deliberate escalation, not implicit fallback).

### §8.2 Tier 3b template fields (new)

GOAL / SUCCESS CRITERIA / ALLOWED SCOPES / BUDGET / HALT-AND-REPORT each defined with examples. Default BUDGET: 12 tool calls, 30 min wall time, 5 inner-loop iterations. Pointer to skeleton at `docs/relay_prompt_agent_template_3b.md`.

### §16 Change Log (prepended 2026-05-14 entry)

Full E3 amendment summary, framing as out-of-cycle pull-forward from 1-June MSB on throughput grounds.

### Filename version bump

`docs/siarc_project_instructions_v2026-05-05.md` → `docs/siarc_project_instructions_v2026-05-14.md` (Move-Item used since `docs/` is untracked in claude-chat repo).

### New template file

`docs/relay_prompt_agent_template_3b.md` (~285 lines, ~9.7 KB) — required prompt structure with field-by-field explanation, two worked examples (Example A: Lean build-until-green; Example B: paper14 response-to-referee), drafting checklist for CLI / Synthesizer authors, authority-envelope reminder cross-referencing §3 rule 6.

---

## Verification

- §3 rows 49-50 = 3a + 3b (verified via view tool post-edit)
- §3 RACI matrix rows 61-62 = single-step / multi-step split (verified)
- §3 rule 6 at line 75 (verified)
- §8 lines 183-258 = full new shape (verified)
- §16 change log entry top of section (verified)
- Old filename `..._v2026-05-05.md` no longer in `docs/` (Get-ChildItem confirmed)
- New filename `..._v2026-05-14.md` present, size 19,464 B (verified)
- New template `relay_prompt_agent_template_3b.md` present, size 9,687 B (verified)

---

## ALSO_KNOWN

- The claude-chat `docs/` directory is **untracked** in git; this E3
  amendment is local-only on the operator's workstation. The bridge-repo
  absorption of this session is the canonical external record of the
  amendment. If the operator wants the master doc to propagate via
  GitHub, `docs/` needs to be removed from `.gitignore` or explicitly
  `git add`-ed.
- No existing standalone Tier 3a template file — §8 baseline narrative
  is the de-facto inline template. A parallel `..._inline_template_3a.md`
  could be extracted for symmetry but is not required for correctness.
- The Synthesizer Master Prompt for the in-flight cycle is not amended;
  the *application* of this E3 governance to the Master Prompt is a
  Tier-1 action and should be picked up at the next 1-June MSB cycle.
- Rule 6's "absorption fire runs as a separate Tier 3a step" clause is
  a procedural innovation worth flagging: it means E3-class governance
  amendments themselves (like this one) deposit via Tier 3a paths, not
  Tier 3b — preventing Agent mode from gaining indirect commit/push
  authority by bootstrapping its own deposit.
