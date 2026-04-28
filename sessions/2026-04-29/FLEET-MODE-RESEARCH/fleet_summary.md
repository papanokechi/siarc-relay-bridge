# FLEET-MODE-RESEARCH — Executive Summary
Date: 2026-04-29 | Synthesizer: Opus 4.7 | Class: strategic_research

VERDICT: Fleet mode is feasible NOW for SIARC using only
existing tools (Copilot CLI + Python venv + claude.ai).
No new accounts, no API key, no paid subscriptions required.

ACCESSIBLE OPTIONS (zero cost):
  A. Multiple parallel Copilot CLI sessions
  B. Python subprocess fleet (multiprocessing) for compute
  D. Hybrid: Copilot CLI fleet + Opus 4.7 synthesizer  ← RECOMMENDED
GATED (NOT recommended by default):
  C. Claude API multi-agent — requires explicit API key
     enablement per project rules; flagged, not adopted.

TOP FLEET CANDIDATES (ranked):
  1. SICF 4-agent review (Advocate/Critic/Framing/NextSteps)
     ~3× speedup (60 min → ~20 min) + quality gain via
     enforced blinding. Lowest risk, highest leverage.
  2. T2B-STOKES-NUMERICAL family sweep (5 families parallel)
     ~5× speedup; clean per-family namespacing.
  3. Multi-paper PSLQ sweeps. Biggest absolute speedup but
     phantom-hit propagation risk; needs dps re-verify pass.

KEY RISKS + MITIGATIONS:
  R2 PSLQ phantom propagation → mandatory dps escalation +
     post-merge re-verify on single worker.
  R3 Overclaiming under fleet pressure → HALT-IF rules in
     every agent prompt + coordinator audit pass.
  R5 Audit fragmentation → fleet_manifest.json per run;
     bridge subdir = single canonical AEAL artifact.

RECOMMENDED FIRST PILOT: parallel SICF on
t2b_paper_draft_v4.tex with 4 Copilot CLI agents +
Opus 4.7 coordinator. Smallest, safest, highest-leverage
test. Setup effort: minutes. Awaiting papanokechi go-ahead.
