# Carneiro cs.LO Endorsement Fire — Pre-Dispatch Prep Record

**Date:** 2026-05-13 08:02 JST
**Verdict authority:** Q-208-3 LOCK `γ FIRE_CARNEIRO_ONLY` (verdict_208.md L48)
**Target:** Mario Carneiro (Chalmers University of Technology, formerly CMU)
**Paper:** Tunnell CNP Lean 4 formalization (954 lines, zero `sorry`, 1 axiom)
**arXiv target:** cs.LO primary + math.NT cross-list

## All 5 dispatch gates GREEN

| Gate | Status | Evidence |
|---|---|---|
| 1. R1 abstract methodology-first | ✅ | `congruent-relay/paper/main.tex` L83-110 opens "We present a 954-line Lean 4 formalization..." |
| 2. R3 README front-matter complete | ✅ | tunnell-cnp-lean4 README has 0-sorry / named axiom / 98 tests + OEIS A003273 / Lean code blocks |
| 3. Carneiro email VERIFIED | ✅ | **`marioc@chalmers.se`** via Mathlib commits 0c43cd0 (2026-03-26 `fix: improve recall impl`) + e944708 (2025-11-24 `fix(Enriched/Ordinary/Basic)`); recent within 60 days |
| 4. Zenodo 19834824 sync | ✅ | Deposit modified 2026-04-28; local HEAD also 2026-04-28 (`e826140`); deposit content = CongruentStubs.lean only (36 KB) |
| 5. RULE 1 distribution-work exemption | ✅ | Q-208-3 verdict explicit: "firing Carneiro tomorrow does NOT count against journal-fire pacing flag (low-friction administrative, not substrate-heavy conversion)" |

## Pre-fire repo URL correction (commit 94c834b)

Legacy "congruent-relay" name lingered in 3 places:
1. ❌ `paper/main.tex` L6 header Repository comment
2. ❌ `paper/main.tex` L110 `\url{...}` in abstract
3. ❌ `README.md` L1 title

Canonical public repo URL is `tunnell-cnp-lean4` (used consistently in
submission_log.txt, JFR pre-query, LMCS cover letter, PORTFOLIO_INVENTORY,
PAPER_VENUE_LIKELIHOOD_MATRIX). The 3 legacy occurrences would have caused
404 link on click — endorsement-killing. Patch:

- README.md title → "# Tunnell CNP Lean 4 — A Layered, Axiom-Isolated Formalization"
- paper/main.tex L6 + L110 → `https://github.com/papanokechi/tunnell-cnp-lean4`

Public state verified live via github-mcp-server-get_file_contents after push.

## Operator affiliation note

Draft section header says "C6 Mario Carneiro (CMU)" but per GitHub profile
(retrieved 2026-05-13) Carneiro's current affiliation is **Chalmers University
of Technology**. The salutation in the email body is just "Dear Dr. Carneiro"
(institution-agnostic), so no email-body edit needed. Internal triage metadata
should be updated to reflect Chalmers affiliation for any future tracking.

## Operator-only remaining action

1. Request arXiv endorsement code at https://arxiv.org/auth/need-endorsement/cs.LO
2. Inject code into `[PASTE_OPERATOR_CODE_HERE]` placeholder
3. Inject canonical reply-email into `[YOUR_REPLY_EMAIL]` placeholder
4. Send to `marioc@chalmers.se`
5. Reply here with "Carneiro fired" + timestamp

## Post-fire bookkeeping (queued for "Carneiro fired" signal)

- SQL: mark `v208-fire-carneiro-tomorrow` done with timestamp
- SQL: create `carneiro-endorsement-14day-floor-tracker` due 2026-05-27
       (14-day floor for Avigad fallback pivot per Q-208-3 wording)
- submission_log.txt: add dispatch record under arXiv-endorsement-quest section
- Bridge follow-up commit recording dispatch timestamp + verification artefacts

## Fallback chain (per Q-208-3)

If Carneiro silent at 14-day floor 2026-05-27 → pivot to:
- **First fallback:** C3 Jeremy Avigad (CMU; drafted-frozen in endorsement_request_drafts_v1)
- **Second fallback:** C2 Kevin Buzzard (Imperial; drafted-frozen)
- **Third fallback:** C4 Patrick Massot (Paris-Saclay; drafted-frozen)
