# Prompt 181 verbatim — for audit trail

# Drafted: 2026-05-11 ~15:33 JST
# Type: T2-Executor (literature reconnaissance) OR T1-Synth (consultation)
# Synth-recommended FIRST fire per slot 156 verdict (Pathway E lowest cost;
#                                                     literature signal informs B vs D)
# Cost: hours to 1-2 days agent-time
# Substrate references:
#   - P-009 spec at bridge SHA 1873538
#   - Template ref: bridge SHA a26ab27 (038 literature reconnaissance)
# SQL todo: t1-156-followup-e
# UF: UF-156-A2 (P-009 NOT_YET_DISPATCHED state persistent since 2026-05-06)

(See operator-side relay prompt for full text; reproduced here is the
operative SUMMARY of the prompt content used by this T2-Executor fire.)

## Phase 0 — Supersession Gate

1. Scan bridge HEAD for any prior P-009 / T1-156-E / FOLLOWUP-E /
   d>=3-binding-window LANDED session. Halt if superseded.
2. Verify P-009 spec at bridge SHA 1873538 — confirm d>=3 binding-
   window scope.
3. Verify 038 template at bridge SHA a26ab27 — read handoff for
   fire-structure reference.

## Phase A — Target Definition

Target literature class: works addressing d>=3 binding-window phenomena
in Painleve III / V_quad / continued-fraction analytic-continuation
contexts.

Candidate keywords:
  - "d>=3 binding window"
  - "higher-Painleve III"
  - "V_quad parameter-space binding"
  - "Forrester-Witte" + ("d>=3" OR "higher")
  - "Birkhoff-Trjitzinsky" + ("invariant" OR "d=3")
  - Adjacent: "binding window" + ("transcendence" OR "Painleve")

Pre-verification (mandatory per copilot-instructions Bibliographic
identifier pre-verification rule).

## Phase B — Reconnaissance Execution

B.1: Web search via web_search tool for each keyword. Capture top
     5-10 hits per keyword.
B.2: For each promising hit: fetch metadata; verify identifier;
     score relevance.
B.3: Synthesise findings into a 1-2 page reconnaissance report.

## Phase C — Halt Modes

- HALT_E_LITERATURE_NULL — zero STRONG hits
- HALT_E_BINDING_WINDOW_HIT — 1+ STRONG hit
- HALT_E_PAYWALL_BLOCKED — STRONG hit but paywalled

## Phase D — B1-B5 Standing Closure

Per SIARC standing protocol (copilot-instructions): 6-10 deliverables,
path-specific staging, 9-section handoff, commit format
"T2-EXECUTOR-T1-156-E-P009-LITERATURE-NNN -- ...".

## Downstream Absorption

SQL todo t1-156-followup-e flips pending -> done. D-156-2 re-evaluated.
Operator-tier follow-up: SQL todo d-156-1-v0plus-vs-v1 resolved based
on E result.
