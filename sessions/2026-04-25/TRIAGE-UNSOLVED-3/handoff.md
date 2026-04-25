# Handoff — TRIAGE-UNSOLVED-3
**Date:** 2026-04-25
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~15 minutes
**Status:** COMPLETE

## What was accomplished
Produced three AEAL-compliant Problem Dossiers for Collatz (P1),
Goldbach strong form (P2), and Birch–Swinnerton-Dyer (P3),
covering current frontier (with author/year), AI-relay surface
(enumeration, PSLQ, Lean 4 ≤ 500-line targets), obstruction
class, narrow falsifiable relay entry point, and estimated relay
depth. Concluded with a ranked recommendation to commit Relay
Cycle 1 to **P3 (BSD)**, with a verbatim Cycle 1 task spec
(`BSD-RATIO-RANK2-N10000`).

## Key numerical findings
None — this was a pure epistemic-mapping relay. No sweeps were
launched and no new numerical claims were produced. All cited
frontier results (Barina $2^{68}$, Tao 2019, Helfgott 2013,
Oliveira-e-Silva $4 \cdot 10^{18}$, Gross–Zagier 1986,
Kolyvagin 1989, modularity theorem, LMFDB conductor $\le 5\cdot10^5$)
are tagged `independently_verified` in the dossier as
literature-vetted, and not re-logged as session claims.

## Judgment calls made
- **TASK_ID inference.** Prompt did not specify one; assigned
  `TRIAGE-UNSOLVED-3` (3 = number of targets).
- **Empty `claims.jsonl`.** Per AEAL standing rule "every
  numerical claim must have an entry," but no numerical claims
  were *produced* this session — only cited. Logged the file as
  empty rather than fabricating entries for literature citations.
  Recommend Claude confirm this interpretation.
- **Lean ≤ 500-line targets.** Selected one canonical target per
  problem; not exhaustive. The selections are weighted toward
  what is plausibly self-contained given current `mathlib` state.
- **Cycle-1 recommendation.** Chose BSD over Goldbach despite
  Goldbach's cleaner Lean target, because BSD has a genuine PSLQ
  surface with falsifiability potential at rank $\ge 2$ where
  theory is silent — i.e., it can produce *new* AEAL-tagged
  evidence rather than just formalizing known facts.

## Anomalies and open questions
- **AEAL convention for citation-only sessions.** The standing
  instructions say "every numerical claim must have a
  corresponding entry in claims.jsonl." This was written
  assuming computational sessions. Should literature citations
  with `independently_verified` tags also be logged in
  `claims.jsonl`, or is the file's empty state the correct
  representation of "no claims produced this session"? Suggest
  adding a clarifying line to `copilot-instructions.md`.
- **Goldbach Lean target — kernel-time reality check.** The
  certified-witness verifier for $n \le 10^6$ is correct in
  principle but Lean kernel reduction over $5 \cdot 10^5$ even
  numbers with primality witnesses may be slower than
  estimated. Cycle 1, if dispatched on P2, should pilot at
  $n \le 10^4$ first.
- **BSD entry point — generator availability.** The proposed
  Cycle 1 task assumes LMFDB-stored Mordell–Weil generators are
  proven (not just claimed) for all rank-2 curves with
  conductor $\le 10000$. Need to confirm this against current
  LMFDB provenance. If not, an additional step is needed:
  re-derive generators via `mwrank` / `ratpoints` to required
  height bound.
- **No coverage of meta-question.** The triage did not address
  whether *combining* targets (e.g., elliptic-curve heuristics
  informing Goldbach exceptional sets) is on the relay surface.
  Probably out of scope, but flagging.

## What would have been asked (if bidirectional)
- Should TASK_ID be inherited from a prior planning artifact or
  is "TRIAGE-UNSOLVED-3" acceptable?
- For the AEAL-tagging of literature citations: log them in
  `claims.jsonl` with `evidence_type: "literature"`, or treat
  the file as session-scoped (current behavior)?
- For the BSD recommendation: is rank-2 conductor $\le 10000$
  the right scale for Cycle 1, or should it be smaller (faster
  feedback) or larger (more anomaly-hunting power)?

## Recommended next step
Dispatch Cycle 1 as `BSD-RATIO-RANK2-N10000`:

> Enumerate all rank-2 elliptic curves $E/\mathbb{Q}$ in LMFDB
> with conductor $N \le 10000$. For each: compute $L''(E,1)$ to
> 200 dps via Dokchitser; compute $\Omega_E$, $\operatorname{Reg}(E)$
> (from stored generators), $\prod_p c_p$, $\#E(\mathbb{Q})_{\text{tors}}$.
> Form the BSD ratio $\mathcal{R}(E)$, PSLQ-identify it, and
> AEAL-tag (`near_miss` if $|\mathcal{R}(E) - n^2| > 10^{-150}$
> for the nearest integer square $n^2$, else `numerical_identity`).
> Halt and log if any entry fails to identify as a perfect
> square integer.

Pilot first on the ~50 rank-2 curves with $N \le 1000$ before
scaling.

## Files committed
- `sessions/2026-04-25/TRIAGE-UNSOLVED-3/dossiers.md`
- `sessions/2026-04-25/TRIAGE-UNSOLVED-3/claims.jsonl` (empty)
- `sessions/2026-04-25/TRIAGE-UNSOLVED-3/halt_log.json` (empty `{}`)
- `sessions/2026-04-25/TRIAGE-UNSOLVED-3/discrepancy_log.json` (empty `{}`)
- `sessions/2026-04-25/TRIAGE-UNSOLVED-3/unexpected_finds.json` (empty `{}`)
- `sessions/2026-04-25/TRIAGE-UNSOLVED-3/handoff.md`

## AEAL claim count
0 entries written to `claims.jsonl` this session. (Pure
epistemic-mapping; no computations performed. See "Anomalies"
for convention question.)
