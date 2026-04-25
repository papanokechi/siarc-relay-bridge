# Handoff — UNSOLVED-PROBLEMS-TRIAGE-SWEEP
**Date:** 2026-04-25
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Produced an AEAL-tagged triage dossier for Collatz, strong Goldbach, and Birch-Swinnerton-Dyer. The dossier maps current frontiers, computationally reachable surfaces, PSLQ/pattern-search channels, <=500-line Lean targets, obstruction classes, first A1 relay entry points, and estimated A1->A4 relay depth. No new computational sweep was launched; this was intentionally an epistemic mapping and scouting task.

## Key numerical findings
- Collatz dossier cites Tao (2019; revised 2022) for logarithmic-density almost-bounded orbits and Barina (2020) for convergence verification below 2^68; dps=0, script `problem_dossiers.md`.
- Goldbach dossier cites Oliveira e Silva, Herzog, and Pardi (2014) for strong Goldbach verification up to 4 * 10^18; dps=0, script `problem_dossiers.md`.
- Goldbach Cycle-1 entry point is a bounded witness certificate for every even N <= 10^6; dps=0, script `problem_dossiers.md`.
- BSD Cycle-1 entry point is a selected rank-0 curve audit at >= 80 decimal digits plus finite-field point-count certificates for primes p <= 97; this is a proposed near_miss target, not a completed numerical identity.
- Dossier SHA-256 recorded in claims.jsonl: 345c11760f30e14c1631373106719caf951a00729e6bb6dc714109562c831913.

## Judgment calls made
- No explicit Task ID was supplied beyond the prompt title, so I used `UNSOLVED-PROBLEMS-TRIAGE-SWEEP`.
- Because the relay prompt had no separate DELIVERABLES section, I treated `problem_dossiers.md`, `claims.jsonl`, and the required JSON logs as the deliverable set.
- I used `near_miss` for all proposed relay entry points and <=4-cycle reachability assessments, reserving `independently_verified` for literature-backed frontier statements. No claim was tagged `numerical_identity` because this session performed no independent numerical verification.
- I ranked strong Goldbach first because it gives the cleanest finite certificate path to a formalized bounded theorem within 1-2 cycles.

## Anomalies and open questions
- No halt condition was triggered: no new sweep was run, no unexpected positive result was found, and no numerical contradiction was detected.
- Some literature-frontier claims were cited at author/year granularity per prompt rather than full bibliographic metadata. Claude may want a follow-up bibliography pass if this dossier is promoted into a public-facing document.
- The BSD dossier intentionally keeps the Lean target local and peripheral to BSD itself; this is an honest limitation rather than a proof-relevant global route.
- The Collatz and Goldbach entry points are bounded formalization targets. They are useful relay products but should not be represented as movement on the full conjectures.

## What would have been asked (if bidirectional)
- "Should the dossier use a compact Markdown-only format, or also include machine-readable JSON for downstream agent routing?"
- "For BSD, should the first curve be fixed as 11a1, or should A1 be allowed to choose any rank-0 curve with the simplest available independent backends?"

## Recommended next step
Commit Relay Cycle 1 resources to strong Goldbach: build a compact witness-certificate format for every even N <= 10^6, independently verify primality evidence, and have A3/A4 produce a <=500-line Lean checker for the bounded theorem.

## Files committed
- `problem_dossiers.md`
- `claims.jsonl`
- `halt_log.json`
- `discrepancy_log.json`
- `unexpected_finds.json`
- `handoff.md`

## AEAL claim count
4 entries written to claims.jsonl this session