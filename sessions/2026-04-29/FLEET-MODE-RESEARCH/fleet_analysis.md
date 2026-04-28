# FLEET-MODE-RESEARCH — Fleet Mode Feasibility for SIARC

Task ID: FLEET-MODE-RESEARCH-2026-04-29
Class: strategic_research
Synthesizer: Opus 4.7 (Copilot CLI session)
Date: 2026-04-29

---

## AREA 1 — Fleet mode definition and current options

### 1a. GitHub Copilot CLI
"Fleet" in the Copilot-CLI sense means launching N independent
`copilot` CLI processes, each in its own PowerShell window or
its own working directory, with separate session IDs. Each
agent has:
  - its own conversation context (no shared memory)
  - its own tool-call history
  - its own write access to the filesystem (NOT isolated by default)

What Copilot CLI provides natively:
  - per-session state under `~/.copilot/session-state/<id>/`
  - per-session SQL scratch DB
  - per-session plan.md
  - parallel invocation works (no rate-limit collision observed
    for ≤4 simultaneous sessions on a single Copilot subscription)

What Copilot CLI does NOT provide:
  - workspace isolation (two agents can clobber the same file)
  - automatic result merging
  - inter-agent messaging
  - a coordinator role

Accessibility: AVAILABLE NOW. No new setup. SIARC already runs
one Copilot CLI session; running 2–5 in parallel is just
"open more PowerShell windows."

### 1b. Anthropic Claude API
Fleet via API means N parallel `messages.create` calls, each
with a different system prompt or task. Orchestration patterns:
  - fan-out/fan-in (map-reduce): one orchestrator dispatches N
    completions, collects N responses, synthesizes
  - role-specialized agents (e.g., 4 SICF roles as 4 system
    prompts running in parallel)
  - tool-use loop per agent (each agent can call tools
    independently)

Accessibility: REQUIRES API KEY. Per project rules
(siarc_context.md governance), Claude API key usage is NOT
the default. claude.ai web (papanokechi's Plus/Max) is the
sanctioned channel. Therefore Option C below is GATED on
explicit human enablement and is not the recommended path.

### 1c. Open source frameworks
  - LangGraph: stateful multi-agent graphs, requires LLM
    backend (would route to Claude API or local model).
    Heavy dependency, Python venv install.
  - AutoGen (Microsoft): conversational multi-agent, similar
    backend requirement.
  - CrewAI: role-based crews, similar.
  - All three are Python frameworks that wrap an LLM API.
    They do NOT remove the API requirement; they just
    structure the orchestration.

Accessibility: PARTIAL. The frameworks themselves are pip-
installable in the existing `.venv`. But they are useless
without an LLM endpoint. With Copilot CLI (which is not an
API endpoint these frameworks know how to call), they cannot
be used as-is. Conclusion: not accessible without API key.

### Verdict on accessible options
  ACCESSIBLE NOW (no new accounts, no API key):
    (i) Multiple parallel Copilot CLI sessions
    (ii) Python `subprocess` / `multiprocessing` fleet for
         pure-compute tasks (PSLQ, Padé–Borel, sweeps)
    (iii) claude.ai web tabs run in parallel by papanokechi
         (manual fleet, slow, not scriptable)
  GATED (requires explicit human enablement):
    (iv) Claude API multi-agent
    (v) LangGraph/AutoGen/CrewAI on top of Claude API

---

## AREA 2 — SIARC problems most suited to fleet mode

Reviewed siarc_context.md (P1–P5 + portfolio) and
session_state.md (D1–D3, NEXT/TOMORROW priorities) and
the 22-paper submission_log.txt portfolio.

| Candidate | Parallelizable | Fleet benefit | Coord. complexity | Conflict risk |
|-----------|----------------|---------------|-------------------|---------------|
| (a) T2B-STOKES-NUMERICAL — 5 families, Padé–Borel [40/40], dps≥150 | YES (embarrassingly parallel; per-family compute is independent) | HIGH (5× wall-clock speedup; each family runs ~minutes) | LOW (each agent writes one row to a shared CSV; merge is `cat` + sort) | LOW if per-family output files are namespaced by family ID |
| (b) SICF 4-agent review (Advocate / Critic / Framing / Next Steps) | YES (designed for independence) | HIGH (4× speedup AND quality gain from enforced independence) | MEDIUM (coordinator must merge 4 verdicts into one decision) | LOW if agents are blinded to each other's outputs until all are written |
| (c) Multi-paper PSLQ sweeps (large search spaces) | YES (partition the search space by chunk) | HIGH (linear speedup with N up to compute limit) | LOW (chunked workers, master claims.jsonl appended atomically) | MEDIUM — phantom hits could propagate if one worker's bad dps infects merged dataset |
| (d) Paper revision + new conjecture search in parallel | PARTIAL (different tasks, different files) | MEDIUM (decouples blocked work; not a speedup of either task individually) | LOW (no shared files if scoped properly) | LOW (different directories) |
| (e) CMB portfolio monitoring (22 submissions, verdict checks) | YES (per-submission status check is independent) | MEDIUM (22 checks are I/O-bound; serial is already fast enough) | LOW (each agent writes one status row) | LOW |
| P1 Paper v4 rewrite | NO (requires a single coherent voice) | LOW | — | HIGH (multi-agent on prose causes drift, contradictions) |
| P3 Zenodo v3 abstract | NO (single 200-word artifact) | LOW | — | HIGH |
| Theorem proof construction | NO (sequential reasoning, shared state) | LOW | — | HIGH |

Top three fleet candidates, ranked by leverage:
  1. SICF 4-agent review (b) — natural fit, designed for it
  2. T2B-STOKES-NUMERICAL family sweep (a) — clean parallel
  3. Multi-paper PSLQ sweeps (c) — biggest absolute speedup
     but biggest phantom-propagation risk

---

## AREA 3 — Concrete fleet architecture for SIARC

### Option A — Copilot CLI parallel sessions
  Mechanism: papanokechi opens N PowerShell windows, runs
  `copilot` in each, hands each a different session prompt
  pointing at a different bridge subdirectory.
    e.g., agent1 → sessions/.../STOKES-FAM1/
          agent2 → sessions/.../STOKES-FAM2/
  Coordinator: a final Opus 4.7 session reads all
  per-agent claims.jsonl files and synthesizes.

  Setup effort: MINUTES (no new code; just window discipline).
  Race conditions: LOW if each agent writes only inside its
    own session dir. Merge step is read-only for the
    coordinator.
  Result merging: by the coordinator session, manually
    instructed to read N files and emit one synthesis.
    No data loss because per-agent files are independent.
  AEAL audit trail: PRESERVED per agent. Each Copilot session
    already maintains its own session-state folder, plan.md,
    and (if instructed) its own claims.jsonl under its bridge
    subdir. The audit trail is the union of N per-agent
    trails plus one synthesis trail.

### Option B — Python subprocess fleet
  Mechanism: an orchestrator script (e.g.,
  `scripts/fleet_runner.py`) uses `concurrent.futures` or
  `multiprocessing.Pool` to launch N worker processes, each
  running a deterministic compute task (PSLQ, Padé–Borel,
  Stokes residue evaluation). Workers write to namespaced
  per-worker output files (`worker_{i}.jsonl`); the
  orchestrator concatenates and validates at the end.

  Setup effort: HOURS (one orchestrator script; reuses
  existing `stokes_numerical.py` per-family logic).
  Race conditions: LOW with namespaced output files. NEVER
    share a single open file handle across workers.
  Result merging: orchestrator does explicit append +
    deduplication + AEAL claim validation post-run.
  AEAL audit trail: PRESERVED if the orchestrator writes one
    aggregate claims.jsonl with `worker_id` and `task_id`
    fields per row, AND each worker keeps its own raw output
    file for forensic replay.
  Best for: pure compute (Stokes sweeps, PSLQ, Padé–Borel).
    NOT for tasks that need an LLM judgement loop — workers
    here are dumb subprocesses, not agents.

### Option C — Claude API multi-agent  [GATED]
  Mechanism: Python script issues N parallel
  `anthropic.messages.create` calls with role-specific
  system prompts. Coordinator collects responses.
  STATUS: REQUIRES EXPLICIT API KEY ENABLEMENT.
  Per project rules, default channel is claude.ai web,
  not API. This option is FLAGGED, not recommended,
  and listed only for completeness.
  If enabled: setup is HOURS, costs are per-token billed,
  audit trail must be added (API does not auto-log).

### Option D — Hybrid: Copilot CLI fleet + Opus synthesis
  Mechanism: 2–4 parallel Copilot CLI sessions each handle a
  parallel subtask (per-family Stokes verification, or one
  SICF role each). One Opus 4.7 CLI session is the
  designated coordinator: it reads all per-agent outputs
  from the bridge and produces the synthesis. claude.ai web
  is reserved for final strategic review of the synthesis
  (matching current SIARC two-tier pattern).

  Setup effort: MINUTES to HOURS (no code; just process
  discipline + an explicit "coordinator prompt" template).
  Race conditions: LOW (per-agent bridge subdirs).
  Result merging: by Opus 4.7 coordinator session, with the
    same AEAL discipline currently used.
  AEAL audit trail: FULLY PRESERVED — each Copilot session
    keeps its own session-state and claims.jsonl; the
    coordinator's synthesis is itself a session with its own
    audit log. claude.ai final review is logged in to_claude.md
    as today.
  Cost: zero new (uses existing Copilot subscription only).

### Comparison table

| Option | Setup | Race risk | Merge safety | AEAL preserved | Cost |
|--------|-------|-----------|--------------|----------------|------|
| A | minutes | low | manual | yes | $0 |
| B | hours   | low | scripted | yes if worker_id logged | $0 |
| C | hours   | medium | API-coded | NO unless added | $$ per token |
| D | minutes→hours | low | hybrid | yes | $0 |

### Recommendation
**Option D (hybrid)** is the best default for SIARC because:
  - reuses existing Copilot CLI + Opus + claude.ai stack
  - no API key required, no new subscription
  - preserves the two-tier (executor / synthesizer) pattern
    already validated by current pipeline
  - degrades gracefully: if a fleet agent fails, the
    coordinator still produces a partial synthesis from the
    surviving agents

Option B should be added as a complement specifically for
heavy-compute sweeps (PSLQ, Padé–Borel) where an LLM is not
needed in the inner loop — there, raw Python subprocesses
are faster and cheaper than CLI agents.

---

## AREA 4 — Fleet mode for SICF specifically

SICF = 4-role review: Advocate / Referee Critic /
Framing Advisor / Next Steps Planner.
Currently: 4 roles run serially in one or several claude.ai
tabs; total wall-clock ≈ 1 hour.

### How to run 4 parallel SICF agents in Copilot CLI
  1. Create bridge subdir
       sessions/<DATE>/SICF-<PAPER-ID>/
       containing:
         input/paper_draft.tex   (read-only by all agents)
         agent_advocate/         (output dir for agent 1)
         agent_critic/           (output dir for agent 2)
         agent_framing/          (output dir for agent 3)
         agent_nextsteps/        (output dir for agent 4)
         coordinator/            (output dir for synthesis)
  2. Open 4 PowerShell windows. In each, start Copilot CLI
     and paste a role-specific system prompt that:
       - identifies the agent's role (e.g., "You are the
         Referee Critic; produce only critic-style review;
         do NOT read other agents' outputs")
       - points to `input/paper_draft.tex` as the only input
       - instructs the agent to write only inside its
         assigned `agent_<role>/` directory
       - instructs it to produce `verdict.md` with a
         standardized header (verdict, confidence, top-3
         issues, recommendation tag)
  3. Run all 4 in parallel. Independence is enforced by
     filesystem convention, not by sandboxing — each agent
     is *instructed* not to read sibling dirs, and the
     coordinator verifies by checking timestamps that each
     agent finished before any sibling output existed in
     its accessible scope (cheap proxy for blinding).
  4. Coordinator (5th Copilot session, or the same Opus
     session that initiated the SICF) reads all four
     `verdict.md` files and synthesizes into one
     `coordinator/sicf_decision.md` with one of:
       PUBLISH-READY / MINOR-REVISIONS /
       MAJOR-REVISIONS / HOLD.

### Independence guarantee
The hard truth: Copilot CLI cannot enforce file-system
isolation. Independence depends on prompt discipline plus
verifiable timestamps. Mitigation: rename `agent_*/` dirs
to `agent_*_DRAFT/` while running and have the coordinator
rename to final names atomically at merge time. The
forensic check is "all four verdict.md files have mtimes
before any read access by a sibling." This is sufficient
for SIARC's audit standard but is not cryptographic.

### Coordinator merge rule
Decision matrix for the four verdicts:
  - 4× PUBLISH-READY → PUBLISH-READY
  - ≥1 HOLD → HOLD (any single HOLD is decisive; HOLD means
    a structural issue that blocks publication)
  - ≥1 MAJOR and 0 HOLD → MAJOR-REVISIONS
  - all in {PUBLISH-READY, MINOR} with ≥1 MINOR → MINOR-REVISIONS
  - mixed otherwise → coordinator writes a "needs human
    arbitration" note and escalates to claude.ai strategist
This rule is conservative: any single dissenter for HOLD
wins. This matches the SIARC overclaiming-aversion stance.

### Estimated time saving
Serial SICF (current): ~60 min wall-clock (4 × ~15 min).
Fleet SICF (proposed): ~15–20 min wall-clock (slowest
agent + ~5 min coordinator merge).
Speedup: ~3×, with a quality gain from enforced blinding.

---

## AREA 5 — Risks and failure modes

### R1 — File write conflicts (two agents writing same file)
  Risk: HIGH if dirs are not namespaced.
  Mitigation: per-agent output directories; coordinator
  reads only; one canonical output file per agent role.
  Fleet runner script (Option B) must use `worker_<id>.jsonl`
  files, never a shared append target.

### R2 — PSLQ phantom-hit propagation across agents
  Risk: HIGH for parallel PSLQ sweeps. A worker running at
  insufficient dps may emit a phantom integer relation; if
  the orchestrator merges naively, the phantom enters the
  unified claims.jsonl.
  Mitigation:
    (i) every parallel PSLQ worker MUST run dps escalation
        (dps_lo, dps_hi) as in current SIARC pipeline;
    (ii) post-merge, a separate verification pass re-runs
         each surviving claim at dps_hi + Δ on a single
         worker to ensure stability;
    (iii) `claim_id` includes `worker_id` so a bad worker
          can be quarantined and its claims revoked
          atomically.

### R3 — Overclaiming risk
  Risk: HIGH. Fleet agents under time pressure may relax
  HALT-IF discipline ("the other agents found nothing,
  I'll claim something").
  Mitigation:
    (i) each agent's system prompt includes the full
        SIARC HALT-IF rules verbatim (no shortened version);
    (ii) coordinator runs an explicit HALT-IF audit pass on
         every claim before promoting it to the merged
         claims.jsonl;
    (iii) any claim that fails HALT-IF audit is logged to
          `coordinator/rejected_claims.jsonl` with reason
          (this is itself an AEAL-required artifact).

### R4 — Context drift (agents diverge from project rules)
  Risk: MEDIUM. Without a shared session_state.md each
  agent loses portfolio context.
  Mitigation:
    (i) every fleet agent's launch prompt includes
        siarc_context.md and session_state.md verbatim
        as preamble (~200 lines, fits in one prompt);
    (ii) coordinator re-reads session_state.md before
         synthesizing and updates it post-run;
    (iii) one (and only one) agent owns session_state.md
          write privilege per run — typically the
          coordinator. Fleet agents read but do not write
          it.

### R5 — Audit trail fragmentation
  Risk: MEDIUM. With N parallel agents, the audit trail is
  N+1 separate session folders. A future replay must
  reconstruct the partial order of events.
  Mitigation:
    (i) coordinator emits a single `fleet_manifest.json`
        listing each agent's session ID, start/end times,
        input hash, output files, and result status;
    (ii) bridge subdir for the run becomes the canonical
         AEAL artifact (single dir = single auditable
         event), even though it contains N+1 session
         lineages.

### R6 — Subscription / rate-limit collision
  Risk: LOW for ≤4 parallel Copilot CLI sessions on a
  single account; UNKNOWN above that.
  Mitigation: cap fleet size at 4 by default. Scale to 8+
  only after empirical confirmation that no rate-limit
  truncation occurs.

---

## HALT-IF self-check (per task spec)

  - Option C (Claude API) the only viable option?
      NO — Options A/B/D are all viable without API.
  - Fleet architecture breaks AEAL audit trail?
      NO — Option D preserves per-agent claims.jsonl and
      adds a fleet_manifest.json. Option B preserves audit
      via worker_id-stamped output. R5 mitigation suffices.
  - Requires new accounts or paid subscriptions?
      NO — Options A, B, D use only existing tools
      (Copilot CLI + Python venv + claude.ai). Option C
      would require API enablement; flagged, not
      recommended.

No HALT conditions triggered.

---

## Closing recommendation

Adopt **Option D (Hybrid: Copilot CLI fleet + Opus synthesis)**.
First concrete pilot: parallel SICF on
`tex\drafts\t2b_paper_draft_v4.tex` with 4 agents
(Advocate / Critic / Framing / Next Steps) and Opus 4.7 as
coordinator. This is the smallest, lowest-risk, highest-
leverage fleet test in the portfolio. Second pilot, only
after the SICF pilot validates: parallel Stokes-numerical
sweep over the revised D1 family list (b1 ∈ {3,6,9,12,15})
using Option B (Python subprocess) with one PSLQ-stability
re-verification pass per surviving claim.
