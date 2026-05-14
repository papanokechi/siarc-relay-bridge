# Diff Summary — E3 Tier 3a/3b split amendment

**Master doc:** `docs/siarc_project_instructions_v2026-05-05.md` (14,126 B)
→ `docs/siarc_project_instructions_v2026-05-14.md` (19,464 B, +5,338 B)

**New template:** `docs/relay_prompt_agent_template_3b.md` (9,687 B, new file)

---

## Master doc — edit-by-edit summary

### Edit 1: Version line (line 2)

```diff
- ## Version: 2026-05-05
+ ## Version: 2026-05-14
```

### Edit 2: §3 RACI table — Tier 3 row split (lines 49-50)

```diff
- | 3 | Copilot agent (GitHub Copilot in VS Code) | on-demand | Researcher + executer. Runs Python, LaTeX, git, Lean. Executes the relay prompts CLI hands it. Owns the file system. |
+ | 3a | Copilot Inline (VS Code: inline Copilot Chat / `gh copilot`) | on-demand, short-horizon | Researcher + executer for **single-step / single-file** work. Single-file edits, one-shot scripts, single LaTeX recompile, single Python run, quick PSLQ pass, single Zenodo metadata-JSON edit. Executes turn-by-turn under CLI shepherding. |
+ | 3b | Copilot Agent mode (VS Code: GitHub Copilot Agent / `gh copilot agent`) | on-demand, multi-step | Researcher + executer for **multi-step / multi-file / iterative** work. Multi-file refactors, Lean `lake build` iteration loops, cross-cutting renames, response-to-referee passes across a paper, dependency sweeps, long-running PSLQ batches. Autonomous within a declared session folder + budget envelope (see §8.2). |
```

### Edit 3: §3 RACI matrix workstream rows (Code/file execution split + clarifications)

```diff
- | Code/file execution | Copilot | Operator | CLI | Synthesizer |
+ | Code/file execution (single-step) | Copilot 3a (inline) | Operator | CLI | Synthesizer |
+ | Code/file execution (multi-step / iterative) | Copilot 3b (agent) | Operator | CLI | Synthesizer |
  ...
- | CMB / submission_log update | CLI drafts; Copilot commits | Operator | Synthesizer | — |
+ | CMB / submission_log update | CLI drafts; Copilot 3a commits | Operator | Synthesizer | — |
- | Bridge repo audit trail | Copilot | Operator | CLI | Synthesizer |
+ | Bridge repo audit trail | Copilot 3a or 3b | Operator | CLI | Synthesizer |
```

### Edit 4: §3 Key Rules — appended rule 6 (after line 74)

```diff
  5. Synthesizer does not interfere mid-week. If the CLI tier hits a halt it cannot resolve, the Operator escalates to Synthesizer in the next weekly cycle (or out-of-band if a paper is at risk).
+ 6. **Tier 3b authority envelope (added 2026-05-14):** Copilot Agent mode (3b) has file-system + terminal authority *within* its declared session folder + budget envelope (§8.2), BUT `git push`, `git commit -m` to `main`, and any portal interaction (Zenodo, journal portals, email) remain Operator-gated — mirror of rule 3 for Claude in Chrome. Bridge-repo audit absorption (§9) captures Agent's per-session artifacts the same way it captures inline-mode artifacts; the absorption fire itself runs as a separate Tier 3a step under CLI direction.
```

### Edit 5: §8 Relay Prompt Protocol — full rewrite (lines 183-258)

Before (19 lines): single-shape narrative with TASK / BRIDGE / BACKGROUND / numbered STEPS / HALT IF / commit fields.

After (75 lines):

- §8 baseline now MANDATES `MODE: 3a` or `MODE: 3b` declaration line
- Mode-specific field tables: 3a keeps STEPS + HALT IF; 3b replaces with §8.2 fields
- §8.1 added — 4-row mode-selection guide mapping workload-shape → MODE
- §8.2 added — Tier 3b template fields with field-by-field semantics
- Default BUDGET values codified: 12 tool calls / 30 min / 5 inner-loop iterations
- Pointer to skeleton at `docs/relay_prompt_agent_template_3b.md`
- §8 baseline declared the de-facto Tier 3a template (no separate file)
- Phantom-hit-prevention PSLQ rule re-affirmed as MODE-invariant

### Edit 6: §16 Change Log — prepended 2026-05-14 entry

```diff
  ## 16. Change Log

+ - **2026-05-14 (E3 out-of-cycle):** Tier 3 split into 3a (Copilot
+   Inline) + 3b (Copilot Agent mode) per Tier-2 Synthesizer
+   strategic recommendation (Principal Strategyzer, MSB-scope
+   pipeline-architecture question pulled forward from 1-June MSB
+   cycle on M10-Lean-debt + 27-submission-revision-queue throughput
+   grounds). §3 RACI table revised: single Tier 3 row → two rows
+   3a + 3b; RACI matrix split "Code/file execution" into
+   single-step (3a) vs multi-step (3b) workstreams; §3 Key Rules
+   extended with rule 6 (Agent authority envelope; mirror of
+   rule 3 for portal gating). §8 Relay Prompt Protocol amended:
+   every prompt MUST declare `MODE: 3a` or `MODE: 3b`; §8.1 added
+   (mode selection guide); §8.2 added (Tier 3b template fields:
+   GOAL / SUCCESS CRITERIA / ALLOWED SCOPES / BUDGET /
+   HALT-AND-REPORT). New template skeleton at
+   `docs/relay_prompt_agent_template_3b.md`. Inline-shape §8
+   baseline serves as de-facto Tier 3a template. Synthesizer
+   Master Prompt for next cycle should select template family
+   based on declared mode.
  - **2026-05-05:** RACI revised to four-tier model. ...
  - **2026-04-29:** Initial onboarding doc.
```

### Edit 7: Filename version bump (Move-Item, not git mv)

```
docs/siarc_project_instructions_v2026-05-05.md
→ docs/siarc_project_instructions_v2026-05-14.md
```

(claude-chat `docs/` is untracked in git, so Move-Item rather than git mv;
see UF-E3-TIER-1 and discrepancy D-E3-TIER-1)

---

## New template — structural summary

`docs/relay_prompt_agent_template_3b.md` (9,687 B, ~285 lines)

Sections:
1. Header + reference back to §8.2 of master doc
2. When to use this template (not §8 inline) — 5 trigger criteria
3. Required prompt structure — full skeleton with field-by-field semantics
4. Example A — M10 Lean build-until-green (concrete, BUDGET 20/45min/8 iter)
5. Example B — paper14 R3 response-to-referee (concrete, BUDGET 16/40min/3 iter)
6. Drafting checklist (8 items) for CLI / Synthesizer authors
7. Authority envelope reminder — cross-references §3 rule 6
