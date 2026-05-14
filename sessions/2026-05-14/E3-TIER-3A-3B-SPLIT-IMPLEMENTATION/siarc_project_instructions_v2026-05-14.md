# SIARC Breakthrough Explorer — Project Instructions
## Version: 2026-05-14
## Purpose: onboarding document for new sessions and collaborators

---

## 1. Project Goal

Produce ONE ACCEPTED peer-reviewed mathematics paper from an
autonomous AI-assisted research pipeline covering polynomial
continued fractions (PCFs), partition theory, and related
number-theoretic structures.

Secondary goal: develop and document a reproducible methodology
for AI-assisted mathematical discovery that is honest,
verifiable, and publishable under standard academic ethics.

---

## 2. What This Project Is

A hybrid human-AI research pipeline that:
- Generates mathematical conjectures computationally
- Verifies them numerically (PSLQ, high-precision arithmetic)
- Formalizes them (Lean 4 where applicable)
- Writes and submits them to peer-reviewed journals
- Tracks the full pipeline with audit trails (AEAL system)

The researcher (papanokechi) is an independent mathematician
based in Yokohama, Japan. ORCID: 0009-0000-6192-8273.
There is no institutional affiliation — all submissions are
made as an independent researcher.

---

## 3. RACI (revised 2026-05-05 — four-tier model)

The pipeline is organized into four tiers. The motivating
constraint is Synthesizer usage limits: heavy daily use of
the Claude.ai web/desktop chat is no longer sustainable, so
daily tactical work is pushed down to the CLI tier and the
Synthesizer is reserved for weekly strategy.

| Tier | Agent | Cadence | Role |
|---|---|---|---|
| 0 | Operator (papanokechi) | continuous | Decision maker. Sole authority on math claims, venue selection, submissions, withdrawals, and any irreversible action. Pastes inputs into Synthesizer; pastes Synthesizer outputs into CLI. |
| 1 | Synthesizer (Claude.ai web/desktop) | weekly | Strategyzer. Produces the Weekly Strategy Brief (WSB) and the CLI Master Prompt. Reviews the prior week's CLI execution log. Triggers SICF reviews. Does NOT issue daily relay prompts. |
| 2 | CLI (Claude Code or equivalent terminal Claude) | daily | Daily synthesizer + reviewer + commander + executer. Decomposes the WSB into daily tasks, writes per-day relay prompts for Copilot, reviews Copilot output, runs SICF passes locally, and updates CMB / submission_log / handoff stubs. |
| 3a | Copilot Inline (VS Code: inline Copilot Chat / `gh copilot`) | on-demand, short-horizon | Researcher + executer for **single-step / single-file** work. Single-file edits, one-shot scripts, single LaTeX recompile, single Python run, quick PSLQ pass, single Zenodo metadata-JSON edit. Executes turn-by-turn under CLI shepherding. |
| 3b | Copilot Agent mode (VS Code: GitHub Copilot Agent / `gh copilot agent`) | on-demand, multi-step | Researcher + executer for **multi-step / multi-file / iterative** work. Multi-file refactors, Lean `lake build` iteration loops, cross-cutting renames, response-to-referee passes across a paper, dependency sweeps, long-running PSLQ batches. Autonomous within a declared session folder + budget envelope (see §8.2). |
| — | Claude in Chrome | on-demand, operator-driven only | Browser navigation. Stands by during submissions; never auto-submits. |
| — | AEAL system + bridge repo | automatic | Audit trail via relay protocol. |

**RACI matrix (responsibility per workstream):**

| Workstream | R | A | C | I |
|---|---|---|---|---|
| Mathematical claims | Operator | Operator | Synthesizer, CLI | Copilot |
| Weekly strategy | Synthesizer | Operator | CLI | Copilot |
| Daily task decomposition | CLI | Operator | Synthesizer (via WSB) | Copilot |
| Code/file execution (single-step) | Copilot 3a (inline) | Operator | CLI | Synthesizer |
| Code/file execution (multi-step / iterative) | Copilot 3b (agent) | Operator | CLI | Synthesizer |
| Submission act (portal click) | Operator | Operator | CLI | Synthesizer, Copilot |
| Review text drafts (cover letter, response-to-referee) | Synthesizer (weekly) + CLI (daily polish) | Operator | — | Copilot |
| SICF review | CLI runs script; Synthesizer arbitrates flagged calibration failures | Operator | — | Copilot |
| CMB / submission_log update | CLI drafts; Copilot 3a commits | Operator | Synthesizer | — |
| Bridge repo audit trail | Copilot 3a or 3b | Operator | CLI | Synthesizer |

**Key rules (revised):**
1. Synthesizer is invoked at most ~1–2 times per week for strategy + replan. Daily work goes to CLI.
2. CLI is the only tier that writes per-day relay prompts. Synthesizer writes the *weekly* CLI Master Prompt; CLI breaks it into daily prompts for Copilot.
3. Operator is the only tier that clicks "submit" in any browser portal. Claude in Chrome stands by but never acts autonomously on submissions (rule2).
4. No tier produces output that requires API keys to run, unless the Operator explicitly requests it (rule1).
5. Synthesizer does not interfere mid-week. If the CLI tier hits a halt it cannot resolve, the Operator escalates to Synthesizer in the next weekly cycle (or out-of-band if a paper is at risk).
6. **Tier 3b authority envelope (added 2026-05-14):** Copilot Agent mode (3b) has file-system + terminal authority *within* its declared session folder + budget envelope (§8.2), BUT `git push`, `git commit -m` to `main`, and any portal interaction (Zenodo, journal portals, email) remain Operator-gated — mirror of rule 3 for Claude in Chrome. Bridge-repo audit absorption (§9) captures Agent's per-session artifacts the same way it captures inline-mode artifacts; the absorption fire itself runs as a separate Tier 3a step under CLI direction.

---

## 4. Weekly + Daily Cadence

### Weekly cycle (Synthesizer-driven, Sunday or Monday)

1. Operator opens CMB.txt + last week's CLI execution log
   (`cli_log/YYYY-Www.md`) + any new VERDICTS RECEIVED.
2. Operator pastes all three into a fresh Synthesizer chat
   along with the standing prompt: "Given this state, produce
   this week's WSB and CLI Master Prompt."
3. Synthesizer returns:
   - **Weekly Strategy Brief (WSB):** 5–10 bullets of the week's
     priorities, tied to specific papers/blockers from the CMB.
   - **CLI Master Prompt:** a single self-contained prompt that
     CLI will load on Day 1 and use as its standing context for
     the full 7 days. Includes daily slot allocations, halt
     conditions, and end-of-week deliverable list.
4. Operator pastes the CLI Master Prompt into CLI to start the
   week.

### Daily cycle (CLI-driven, every morning)

1. CLI loads its standing weekly prompt + reads CMB + reads the
   previous day's `cli_log/YYYY-MM-DD.md`.
2. CLI writes today's relay prompt for Copilot (≤1 page,
   structured per §7).
3. Operator pastes that prompt into Copilot agent in VS Code.
4. Copilot executes; outputs go to bridge repo.
5. Operator pastes Copilot's terminal/result block back into CLI.
6. CLI reviews, runs any local checks (PSLQ phantom-hit guard,
   SICF if a submission is queued), and writes
   `cli_log/YYYY-MM-DD.md` summarizing the day.
7. End of day: CLI appends today's row to the weekly log.

### End-of-week handoff

CLI writes `cli_log/YYYY-Www.md` summarizing the 7 days,
listing what closed, what's blocked, what should change in
next week's WSB. This is the file the Operator pastes back
into Synthesizer to start the next weekly cycle.

---

## 5. The CMB (Claude Morning Briefing)

**File:** `tex\submitted\CMB.txt` on the local machine.

The CMB remains the single source of truth for project state,
but its consumer is now CLI (daily) rather than Synthesizer
(weekly). Synthesizer reads CMB only at the weekly cycle.

**Structure (unchanged):**
- SUBMISSION PORTFOLIO — table of all active papers
- P11 ACTIVE BLOCKERS — current revision blockers
- TIER 1/2/3/4 — task priority hierarchy
- DAILY DECISION FRAMEWORK — today's recommended action (now driven by CLI, not Synthesizer)
- VERDICTS RECEIVED — journal decisions log
- RECORDED SUBMISSIONS — numbered submission log
- ZENODO — preprint DOI log
- BRIDGE REPO — recent git session log

**Updating the CMB:**
- Never commit CMB changes directly — always via Copilot relay
- CMB is updated at end of each day by CLI, end of each week
  by Synthesizer (synthesis pass only)
- Date header must be updated daily by CLI
- All submission IDs must match submission_log.txt exactly

---

## 6. Submission Tracking Files

Two files maintain the submission record (unchanged):

**submission_log.txt** (`tex\submitted\submission_log.txt`)
- Numbered entries 1..N, one per submission
- Includes: filename, title, journal, date, ID, verdict
- Separate ZENODO section at the end
- Authoritative source for submission IDs

**CMB.txt** (see above)
- Strategic view — one row per active paper
- Must stay in sync with submission_log.txt
- Diff check run each morning by CLI via `docs\cmb-diff-relay.md`

**Date rule:** use the portal-recorded date (UTC), not the
local JST date. For Yokohama (UTC+9), late-evening submissions
will show the prior calendar day on the portal. The portal
date is authoritative for all tracking files.

---

## 7. Blacklisted Venues

These journals will NOT consider AI-assisted manuscripts:
- Experimental Mathematics (7 desk rejections, volume-based)
- NNTDM (explicit LLM ban)
- Integers / INTEGERS (explicit AI ban on text and code)
- Journal of Integer Sequences (explicit LLM text ban)
- Annals of Mathematics (AI ban)

Never suggest these venues regardless of fit.

---

## 8. Relay Prompt Protocol

All Copilot tasks are issued as structured relay prompts. **Every relay
prompt MUST declare a MODE line** (added 2026-05-14):

- `MODE: 3a` — Copilot Inline (default for single-step / single-file work)
- `MODE: 3b` — Copilot Agent mode (multi-step / iterative work)

### Baseline fields (both modes)

- TASK name and AEAL class
- MODE: 3a or 3b
- BRIDGE path for git commit
- BACKGROUND context
- Explicit: "Do not commit or push" or commit instructions

### Mode-specific fields

**Tier 3a (Inline) — adds:**
- Numbered STEPS
- HALT IF conditions

**Tier 3b (Agent) — replaces STEPS / HALT IF with §8.2 fields below.**

Under the new RACI, the *author* of relay prompts is CLI on
daily tasks and Synthesizer on weekly-scope tasks (e.g., a new
paper draft kickoff). Both authors follow the same MODE-declared
template family. CLI selects MODE based on workload shape per §8.1.

**Phantom hit prevention (mandatory in all PSLQ sessions):**
Any PSLQ relation with L-coefficient = 0 is REJECTED.
This prevents the ζ(2)=π²/6 and φ=(1+√5)/2 traps.
This rule is non-negotiable and must appear in every
PSLQ relay prompt regardless of MODE.

### §8.1 Mode selection guide (added 2026-05-14)

| Workload shape | MODE | Rationale |
|---|---|---|
| Single-file LaTeX edit, single-file Python script, one-shot grep, single Zenodo metadata-JSON edit, single submission-log line append, bridge deposit + commit (NOT push) | **3a** | Single step; inline is sufficient; CLI babysitting is appropriate. |
| Multi-file Lean refactor, `lake build` iteration loop until green, cross-cutting import rename across N files, response-to-referee pass across a paper, dependency sweep, multi-file figure regeneration | **3b** | Multi-step autonomous loop; Agent eats it; CLI babysitting is wasted budget. |
| Long-running PSLQ batch with intermediate aggregation, multi-iteration numerical sweep | **3b** | Benefits from Agent's session continuity + iteration budget. |
| Portal navigation (Zenodo, EM portal, OJS, email) | **NEITHER** | Operator-only per rule 3 / rule 6. |

When the workload is borderline, default to **3a** — Agent mode is a
deliberate, declared escalation, not the implicit fallback.

### §8.2 Tier 3b (Agent) template fields (added 2026-05-14)

Tier 3b prompts MUST include these fields in place of the baseline
numbered STEPS / HALT IF:

- **GOAL** — 1-2 sentence statement of what "done" looks like.
  NOT a numbered step list; the Agent decomposes.
- **SUCCESS CRITERIA** — testable binary conditions for completion.
  Examples: `lake build` exits 0; `pytest tests/` passes; specific
  output file exists with expected MD5; all references resolve.
- **ALLOWED SCOPES** — glob list of files/dirs the Agent may edit.
  Examples: `lean/PCF/**`, `tex/submitted/_compositio_build/**`.
  Any attempted out-of-scope edit = HALT immediately.
- **BUDGET** — maximum tool calls (default 12), maximum wall time
  (default 30 min), maximum iterations of any inner loop (default 5).
- **HALT-AND-REPORT** — conditions under which the Agent must stop
  and report rather than continuing. Examples:
  - "If `lake build` still red after 3 iterations, HALT and report
    failing module list."
  - "If any test fails with confidence < 0.9, HALT and report."
  - "If any out-of-scope file modification is attempted, HALT
    immediately and report attempted path."

The agent template skeleton lives at
`docs/relay_prompt_agent_template_3b.md`.

The existing §8 inline-shape (numbered STEPS + HALT IF) serves as
the de-facto Tier 3a template; no separate file is required.

---

## 9. Bridge Repository

**URL:** github.com/papanokechi/siarc-relay-bridge

Each session creates a folder:
`sessions\YYYY-MM-DD\TASK-NAME\`

Contents:
- `handoff.md` — findings and next steps
- `claims.jsonl` — AEAL audit claims
- `halt_log.json` — any halts triggered
- `discrepancy_log.json` — anomalies
- Source files and result JSONs

Commits use the message format:
`TASK-NAME — brief description of result`

**The bridge repo is the cross-session memory.**
If context is lost, fetch any handoff with:
`https://raw.githubusercontent.com/papanokechi/
siarc-relay-bridge/main/sessions/DATE/TASK/handoff.md`

---

## 10. AEAL (Autonomous Epistemic Audit Log)

Every computational claim is tagged with a confidence level:
- `near_miss` — candidate result, not yet validated
- `independently_verified` — verified by second method
- `proven` — formal proof exists

Claims are written to `claims.jsonl` in each bridge session.
The AEAL methodology is itself a research contribution —
see P09 (AI Discovery, under review at Notices AMS).

---

## 11. Key Files and Paths

| File | Purpose |
|---|---|
| `tex\submitted\CMB.txt` | Morning briefing / project state |
| `tex\submitted\submission_log.txt` | All submissions numbered |
| `cli_log\YYYY-MM-DD.md` | CLI daily log (NEW — written by CLI tier) |
| `cli_log\YYYY-Www.md` | CLI weekly summary handed back to Synthesizer |
| `docs\cmb-diff-relay.md` | CMB diff logic |
| `siarc-relay-bridge\` | Cross-session bridge repo |
| `f1_mathcomp_submission\main_R1.tex` | P11 manuscript (JTNB) |
| `pcf_rational_contamination_2026.tex` | P01 (Funct.Approx) |
| `t2b_conjecture_note.tex` | Conjecture note (Zenodo) |
| `t2a_paper_draft.tex` | T2A paper (Zenodo) |
| `ramanujan_agent.py` | Core PCF discovery engine |
| `.venv\` | Python virtual environment |

**Workspace root:**
`C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\`

---

## 12. AI Disclosure Policy

All papers include an explicit AI disclosure section.
Standard wording (Elsevier-compatible):
"During the preparation of this work the author used
GitHub Copilot (Microsoft) and Anthropic Claude in order
to assist with code generation, numerical computations,
and manuscript drafting. After using these tools, the
author reviewed and edited the content as needed and takes
full responsibility for the content of this article."

Claude and Copilot are NOT listed as authors.
The human researcher takes full responsibility for all
mathematical claims.

---

## 13. Current Research Frontier (as of 2026-05-05)

**Active conjecture:**
The Transcendental Ratio Identity — every Trans-stratum
degree-(2,1) integer PCF has a₂/b₁² = −2/9 (indicial
exponents {1/3, 2/3} at infinity). Empirical base: ~150,000
families, zero counterexamples. Preprint: DOI 10.5281/zenodo.19783312.

**Active papers:** 17 journal submissions + 2 Zenodo preprints.
**Highest radar:** P08 Painlevé/V_quad (8.0) at Nonlinearity.

**Immediate next computation:**
T2B-RESONANCE-B67 — extend falsification test to b₁ ∈ {6,7}.

---

## 14. How to Start a New Session

### Weekly start (Synthesizer)
1. Paste CMB.txt + last week's `cli_log/YYYY-Www.md` into
   Claude.ai Synthesizer.
2. Say: "Produce this week's WSB and CLI Master Prompt."
3. Receive WSB + CLI Master Prompt.
4. Paste the CLI Master Prompt into CLI to begin the week.

### Daily start (CLI)
1. CLI loads its standing weekly prompt automatically.
2. Operator runs: `cli daily-kickoff --date YYYY-MM-DD`
   (or pastes a one-line "Day N kickoff" message).
3. CLI emits today's Copilot relay prompt.
4. Operator pastes it into Copilot agent.

### Mid-week context recovery
Fetch the most recent bridge handoff or `cli_log/` entry and
paste into the relevant tier (CLI for tactical, Synthesizer
for strategic).

---

## 15. SICF (Structured Internal Criticism and Framing)

Before submitting any paper, run a four-agent SICF review:
  Agent 1 — Advocate: strongest case for acceptance
  Agent 2 — Referee Critic: most likely rejection reasons
  Agent 3 — Framing Advisor: venue and presentation
  Agent 4 — Next Steps Planner: what to do after SICF

Under the new RACI, SICF is invoked by **CLI** during the week
using the API-FREE prompt template + a fresh Claude.ai tab for
each role (per `docs\SICF_API_FREE_prompt.md`). The Synthesizer
gets involved in SICF only when:
  - A calibration failure is logged in
    `critic_calibration_log.txt`, or
  - The Operator explicitly requests strategic re-framing.

SICF verdict determines: PUBLISH-READY / MINOR-REVISION /
MAJOR-REVISION / HOLD before any submission.

---

## 16. Change Log

- **2026-05-14 (E3 out-of-cycle):** Tier 3 split into 3a (Copilot
  Inline) + 3b (Copilot Agent mode) per Tier-2 Synthesizer
  strategic recommendation (Principal Strategyzer, MSB-scope
  pipeline-architecture question pulled forward from 1-June MSB
  cycle on M10-Lean-debt + 27-submission-revision-queue throughput
  grounds). §3 RACI table revised: single Tier 3 row → two rows
  3a + 3b; RACI matrix split "Code/file execution" into
  single-step (3a) vs multi-step (3b) workstreams; §3 Key Rules
  extended with rule 6 (Agent authority envelope; mirror of
  rule 3 for portal gating). §8 Relay Prompt Protocol amended:
  every prompt MUST declare `MODE: 3a` or `MODE: 3b`; §8.1 added
  (mode selection guide); §8.2 added (Tier 3b template fields:
  GOAL / SUCCESS CRITERIA / ALLOWED SCOPES / BUDGET /
  HALT-AND-REPORT). New template skeleton at
  `docs/relay_prompt_agent_template_3b.md`. Inline-shape §8
  baseline serves as de-facto Tier 3a template. Synthesizer
  Master Prompt for next cycle should select template family
  based on declared mode.
- **2026-05-05:** RACI revised to four-tier model. Synthesizer
  moved to weekly cadence; CLI tier added for daily execution.
  Added rules 3 and 4. Added §4 (Weekly + Daily Cadence) and
  §11 cli_log paths. Updated §5, §8, §14, §15 to reflect new
  ownership.
- **2026-04-29:** Initial onboarding doc.
