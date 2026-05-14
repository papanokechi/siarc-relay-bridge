# Handoff — E3-TIER-3A-3B-SPLIT-IMPLEMENTATION
**Date:** 2026-05-14
**Agent:** GitHub Copilot (VS Code, CLI mode)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

Implemented the out-of-cycle E3 escalation pulled forward from the 1-June MSB
cycle on M10-Lean-debt + 27-submission-revision-queue throughput grounds: Tier 3
(Copilot agent) formally split into **3a (Inline)** + **3b (Agent mode)** per the
Principal Strategyzer (Tier 2) strategic recommendation. Three governance
artefacts amended/created: (i) master governance doc renamed
`siarc_project_instructions_v2026-05-05.md` → `..._v2026-05-14.md` with §3
RACI, §3 Key Rules, and §8 Relay Prompt Protocol amendments; (ii) new
`docs/relay_prompt_agent_template_3b.md` skeleton (~9.7 KB, 5 mandatory fields
+ 2 worked examples + drafting checklist + authority-envelope reminder); (iii)
§16 Change Log entry documenting the 2026-05-14 E3 amendment.

## Key numerical findings

(No new numerical claims — governance amendment session.)

- Master doc grew from 14,126 B → 19,464 B (+5,338 B, +37.8%) reflecting
  §3 row-split + §3 rule 6 + §8 mandatory MODE line + §8.1 selection guide +
  §8.2 template-fields spec + §16 change-log entry.
- New `relay_prompt_agent_template_3b.md` = 9,687 B (~285 lines).
- Total governance footprint delta: +15,025 B across 2 files.

## Judgment calls made

1. **Filename versioning convention.** Bumped filename from
   `siarc_project_instructions_v2026-05-05.md` →
   `siarc_project_instructions_v2026-05-14.md` rather than keeping the
   filename and only bumping the internal `## Version:` line. Rationale:
   the predecessor transition (2026-04-29 → 2026-05-05) bumped the
   filename per the existing convention; preserving filename-as-version
   keeps inline references self-dating. Pre-grep confirmed zero
   external references to the old filename, so the rename is safe.
   `Move-Item` used instead of `git mv` because `docs/` is untracked
   in the claude-chat repo (local-only governance — likely intentional).

2. **Template file location.** Placed
   `relay_prompt_agent_template_3b.md` under `docs/` (alongside master
   governance doc) rather than `tex/submitted/control center/` (alongside
   prompt artefacts). Rationale: this is a *template* (spec-level
   artefact), not a *fired prompt* (artefact-level). Symmetry with
   `siarc_project_instructions_v2026-05-14.md` location.

3. **Tier 3a template — no separate file.** The synth recommendation
   asked for a Tier 3b template; I deliberately did NOT create a
   parallel `relay_prompt_inline_template_3a.md` because the existing
   §8 baseline (numbered STEPS + HALT IF) already serves as the
   de-facto Tier 3a template. Adding an inline template file would
   duplicate §8 verbatim. Documented this explicitly at §8.2 closing
   paragraph.

4. **§3 Key Rules rule-6 phrasing.** Rule 6 mirrors rule 3's portal-gate
   language ("Operator-gated") rather than coining new authority
   terminology. Also added the absorption-fire-runs-as-Tier-3a clause
   to make explicit that bridge-deposit work itself (which often
   touches CMB / submission_log / .fleet.yaml outside the Agent's
   declared session scope) is a separate Tier 3a step under CLI
   direction.

5. **§8.1 selection guide — borderline default.** Codified the default
   as "when borderline, pick **3a**" — deliberate-escalation
   semantics. Rationale: Agent mode consumes more budget per task; an
   implicit-fallback to 3b would invert the friction in the wrong
   direction.

6. **No Synthesizer Master Prompt edit.** Left the next 1-June MSB
   to formally pick up the dual-template instruction at its next cycle
   rather than amending the in-flight Master Prompt. Rationale: the
   E3 governance edit lands now; the *application* of that governance
   to the Master Prompt is a Tier-1 (Synthesizer) action and should
   not be unilaterally pre-empted by Tier 3.

## Anomalies and open questions

1. **`docs/` is not git-tracked in claude-chat.** The whole `docs/`
   directory showed `??` (untracked) in `git status`. This means the
   master governance doc is *local-only* — not visible in any GitHub
   browser, not propagated via repo clones, not in CI scope. Worth
   confirming with Operator whether this is intentional (privacy /
   draft-state) or oversight. If intentional, the bridge-repo
   absorption of this E3 session is the canonical external record of
   the amendment.

2. **No existing relay-prompt template file to reference.** The
   inline-shape "template" is implicit in §8 prose, not extracted to
   a standalone artefact. New users learning the protocol have to
   read §8 narrative and infer the shape. Low-priority cleanup
   candidate: extract a parallel `relay_prompt_inline_template_3a.md`
   for symmetry, but only if usage friction surfaces.

3. **Synthesizer Master Prompt currently mode-agnostic.** The in-flight
   Master Prompt does not declare MODE for any embedded relay
   prompts. The next 1-June MSB needs to adopt the dual-template
   convention; until then, relay prompts will need MODE-line
   retro-fitting by the CLI tier. Not blocking — CLI is already
   familiar with the §8 baseline shape.

4. **No bridge deposit standing rule for E3-class governance edits.**
   The STANDING FINAL STEP in copilot-instructions.md assumes a "relay
   prompt" fired by an operator; E3 escalations are operator-pasted
   strategic recommendations rather than synth-drafted relay prompts.
   I've absorbed this one under the same STANDING FINAL STEP template
   for consistency, but the governance stack may want an explicit
   "E3 absorption" deposit shape for future iterations. Low priority.

## What would have been asked (if bidirectional)

1. **Version-string convention** — simple date bump `2026-05-14` or
   explicit-revision `2026-05-14-E3`? Chose date-bump for parity with
   the existing 2026-04-29 → 2026-05-05 precedent. Operator may
   prefer the explicit-revision form if future E3s are anticipated
   in the same calendar day.

2. **Should §8.2 default BUDGET tighten?** Defaulted to 12 tool calls
   / 30 min / 5 inner-loop iterations. These are conservative
   estimates — actual M10 Lean-build loops may need 20+ build
   iterations; LaTeX response-to-referee passes may need 16+ tool
   calls. Documented as "default; adjust upward only with
   justification" but the right number depends on observed Agent
   behavior post-deployment.

3. **Should rule 6 explicitly call out `gh copilot` / `gh copilot
   agent` as the surface boundaries?** I named both as parenthetical
   examples in the §3 table rows but didn't make the surface-name
   normative in rule 6. If Operator expects to use only one of the
   two surfaces (e.g., always VS Code Copilot Agent, never
   `gh copilot agent` CLI), rule 6 could be tightened.

## Recommended next step

**One bright-line option, two flavor options:**

- **Bright line:** at the next 1-June MSB, the Synthesizer Master
  Prompt MUST declare a default MODE for each embedded relay prompt,
  and CLI MUST select template family based on declared mode. This
  is the throughput-realization of this E3 amendment.

- **Optional flavor A (low cost):** retrofit MODE: 3a / MODE: 3b
  declarations into any in-flight relay prompts still pending
  fire (next-10-list items 1, 2, 5—well, #5 is MOOT—and the M2 Q22
  / .fleet.yaml work). Mechanical, ~5 min.

- **Optional flavor B (medium cost):** dry-run the new Tier 3b
  template against the M10 Lean discharge work (deferred to 2026-08-02
  status report). Tests whether the template's BUDGET defaults and
  HALT-AND-REPORT conditions catch real friction modes before they
  matter operationally.

## Files committed

- `verdict.md` (this session's amendment summary)
- `claims.jsonl` (4 AEAL entries)
- `halt_log.json` (empty `{}`)
- `discrepancy_log.json` (1 INFO discrepancy, resolved)
- `unexpected_finds.json` (3 UFs, all MEDIUM/LOW)
- `handoff.md` (this file)
- `diff_summary.md` (line-by-line summary of edits to master doc)
- `siarc_project_instructions_v2026-05-14.md` (copy of post-amendment master doc)
- `relay_prompt_agent_template_3b.md` (copy of new template skeleton)

## AEAL claim count

4 entries written to claims.jsonl this session.
