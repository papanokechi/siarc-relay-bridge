# Handoff — T2-114-COPILOT-RESEARCHER-PROMPT-DRAFT-127

**Date:** 2026-05-08
**Agent:** GitHub Copilot CLI (claude-opus-4.7-xhigh)
**Session duration:** ~10 min (drafting + bridge deposit, parallel-batch with prompt-queue scoping)
**Status:** COMPLETE

## What was accomplished

Drafted SIARC relay prompt 114 for Copilot Researcher (T2 executor)
to reconcile A-115-1 (PRIMARY) + A-115-2 (SECONDARY) labeling-
convention divergence flagged at 107 QD-5 audit (bridge 115). The
3 classical-ODE-labeled artefacts (p12 Intro + p12 sec:vquad +
LIT dict) get either bracketed-expansion or full Hamiltonian
relabel + cross-walk footnote. The 3 Hamiltonian-labeled artefacts
(058R B.3 + CT v1.3 §3.5 + §3.5.1) are EXPLICITLY out of edit
scope (already correctly labeled).

Prompt at `tex/submitted/control center/prompt/114_t2_a_115_
reconciliation_labeling_convention.txt`; SHA `F8D6910833353F03`;
20,738 B / 427 lines.

This is one of 5 prompts in the post-113 closure queue; queue
overview document at session-state files/.

## Key numerical findings

Not applicable — prompt-draft session.

| Artefact | Path | SHA-16 |
|---|---|---|
| Prompt 114 | `prompt/114_t2_a_115_*.txt` | `F8D6910833353F03` |
| Bridge HEAD | (predecessor) | `1eed8ef` |

## Judgment calls made

1. **Edit-strategy defaults split between D1+D2 and D4.**
   Prompt 114 sets D1+D2 (p12 Intro + p12 sec:vquad) default to
   strategy (b) bracketed expansion preserving classical-ODE
   symbols. Rationale: p12 is a peer-reviewed journal submission;
   full notation rewrite is invasive. Sets D4 (LIT dict) default
   to strategy (a) full Hamiltonian relabel. Rationale: LIT dict
   is machine-readable; explicit subscripted names eliminate
   parser ambiguity. Documented under UF-127-2 + UF-127-3.

2. **D3 cross-walk footnote is load-bearing primitive.** The
   footnote MUST be present in the deposit regardless of D1/D2
   strategy choice — it carries the Hamiltonian-vs-classical-ODE
   disambiguation that makes either strategy honest. Prompt §2
   D3 makes this explicit.

3. **UF-115-3 deferred to future structural prompt.** Prompt 114
   limits scope to A-115-1 + A-115-2 (DOCUMENTATION harmonization).
   UF-115-3 (P_III(D_6)→P_III(D_7) degeneration limit) is a
   STRUCTURAL question best addressed post-Q4 verdict (since
   Q4's Route F outcome may inform Sakai-classification scope).
   Documented under UF-127-5.

4. **Zenodo / submission action explicitly forbidden.** Prompt
   §7 C4 + halt code HALT_114_SCOPE_CREEP_CT_V13_EDIT prevent
   the executor from re-depositing PCF-2 v1.4 or re-submitting
   p12. Working-source edits only; Zenodo decision remains
   gated on `pcf2-v1-4-deposit-decision-q22-gated` blocked todo.

5. **Parallel-safe with 113.** Prompt 114 has no source-file
   overlap with prompt 113 (113 reads Sakai/KNY substrate;
   114 edits p12 + vquad_p3d6_recovery.py + adds footnote).
   No Q4-verdict dependency. The two can fire concurrently
   without contention.

## Anomalies and open questions

(See `unexpected_finds.json` for the same items in machine form.)

1. **Scope-discipline watch (UF-127-1).** Post-edit diff scan
   at Phase F should verify NO unintended CT v1.3 / 058R /
   phase_b_canonical_map.md modifications.

2. **D1+D2 vs D4 default-strategy divergence (UF-127-2 / -3).**
   Justified as above; operator should review at fire-time.

3. **Subsec name uncertainty (UF-127-4).** D5 default falls
   through to strategy (b) "top-level prose" because subsection
   name is not checked at draft time. Researcher should grep
   p12 sec:vquad for subsection titles at fire time.

4. **bib-key uncertainty for kajiwara2017 (D3).** The cross-walk
   footnote cites KNY 2017 §8.5.17. If `kajiwaranoumiyamada2017`
   is not yet a bib key in the project .bib, document under
   UF-126-NEW-BIBKEY (analog of prompt 105 §3 S9 pattern); do
   NOT halt.

5. **UF-115-3 deferred (UF-127-5).** Out of scope for THIS task;
   future structural prompt.

## What would have been asked (if bidirectional)

1. Confirm edit-strategy defaults for D1+D2 and D4. Defaulted
   per Judgment call #1.

2. Confirm whether to include UF-115-3 in scope. Defaulted to
   defer (Judgment call #3).

3. Confirm cross-walk footnote wording. Defaulted to the body
   given in §2 D3 — operator may rewrite at fire-time review.

## Recommended next step

Operator decides fire order:
- Option A (parallel with 113): fire prompt 114 NOW in a separate
  Copilot Researcher session. Both can run concurrently. 114
  expected duration 30-60 min. 113 expected 30-60 min. Total
  parallel runtime ~30-60 min.
- Option B (sequential after 113): fire 113 first, then 114.
  Total wall-clock ~1-2 hr.

**Recommended: Option A** — parallel-safe per Judgment call #5;
saves ~30 min wall-clock; closes 3 SQL todos sooner.

Once 114 lands, the next 4 prompts in queue are 115 (Route F
executor envelope, conditional GO_ROUTE_F), 116 (path-delta
lit-recon envelope, conditional NO_GO), 117 (M4 V0 cascade
closure batch, ~5 todos), 118 (governance-parallel M9 V0
amendment draft, independent). See queue overview document
at session-state files/.

## Files committed

- `114_t2_a_115_reconciliation_labeling_convention.txt`
  (20,738 B / 427 lines / SHA F8D6910833353F03)
- `claims.jsonl` (5 entries)
- `halt_log.json` (empty `{}`)
- `discrepancy_log.json` (empty `{}`)
- `unexpected_finds.json` (5 entries: UF-127-1 through UF-127-5)
- `handoff.md` (this file)

## AEAL claim count

5 entries written to claims.jsonl this session.
