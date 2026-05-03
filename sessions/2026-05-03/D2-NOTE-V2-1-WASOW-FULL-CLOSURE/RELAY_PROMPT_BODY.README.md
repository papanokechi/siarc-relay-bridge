# QS-2 RELAY-PROMPT BODY — operator how-to-fire

## What this is

`RELAY_PROMPT_BODY.txt` is the paste-ready body of QS-2
(D2-NOTE-V2-1-WASOW-FULL-CLOSURE), extracted from
`prompt_spec.md` lines 69-1340 (the operator-paste boundary
between `===== START / END` markers).

Bytes: ~62 KB / 1272 lines. UTF-8, no BOM, LF line endings.

`TODAY_DATE` has been pre-filled to `2026-05-03` (the date
this extraction was made, JST 19:23). If the fire slips past
JST midnight (i.e., past 2026-05-04 00:00 JST), edit the line
beginning `TODAY_DATE:` near the top before paste.

## How to fire

1. Open a fresh Copilot CLI session in the `claude-chat`
   workspace (the same workspace you are reading this from):
       cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat"
       copilot
   (or run `gh copilot` / however you invoke a fresh CLI;
    the agent must be a NEW session — do NOT reuse this one.)

2. Open `RELAY_PROMPT_BODY.txt` in any editor.

3. Select-all → copy → paste as the FIRST USER MESSAGE in the
   fresh CLI session. The body is a single coherent prompt;
   pasting all of it at once is correct.

4. The agent then auto-executes Phase 0 → Phase F over
   ~4-6 hours and writes deliverables to
   `siarc-relay-bridge/sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`
   (distinct from the synthesizer-draft session here).

## Pre-flight checklist (verify before firing)

- [x] B-T 1933 / Acta 60 PDF on disk at slot 03
      SHA-256 `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
- [x] Wasow 1965 PDF on disk at slot 04
      SHA-256 `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`
- [x] Birkhoff 1930 PDF on disk at slot 01
      SHA-256 `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`
- [x] Costin 2008 PDF on disk at slot 06 (Tier 2 secondary; ETHICS-GATED)
      SHA-256 `436c6c115149052634b103a2ed3b460680ad38cd161897794d5eb1f2f6243289`
- [ ] Loday-Richaud 2016 ch. 2 — NOT acquired (Scenario C). Per Q-S1 + Rev-A
      grant, single-source closure on B-T 1933 §§4-6 is sufficient. Costin
      acts as Tier-2 reinforcement if the relay agent verifies ch. 5.
- [x] D2-NOTE v2 source at
      `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/d2_note_v2.tex`
- [x] Picture v1.14 at
      `tex/submitted/control center/picture_revised_20260503.md` §24 (Q-S1..Q-S4 rulings)
- [x] Peer-review consolidation at
      `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-PEER-REVIEW/`
      (commit `95f06de`; agent will fetch from bridge if not local)

## Provenance

- Source: `prompt_spec.md` (75,824 B; this directory)
- Body extract: lines 69-1340 verbatim, with `<fill in current
  date YYYY-MM-DD at run time>` replaced by `2026-05-03`
- Body SHA-256: see `RELAY_PROMPT_BODY.sha256`
- Mirror copy: `tex/submitted/control center/prompt/008_qs2_d2_note_v2_1_wasow_full_closure.txt`
  (byte-identical)

## What to expect post-fire

The relay agent's first action (Phase 0.0) is to write the
prompt body to its own session dir as `prompt_spec.md` for
B1 provenance. It then does Phase 0 SHA verifications, Phase A
re-validation of the Phase A* sweep, Phase B Newton-polygon
characteristic-poly Lemma derivation, Phase C 4-source literature
synthesis, Phase D verdict aggregation, Phase E v2.1 LaTeX
rewrite + 4-pass build, Phase F handoff + AEAL claims +
Standing Final Step.

Most likely outcomes (per spec §6 OUTCOME LADDER):
- `UPGRADE_V2_1_FULL` — v2.1 PDF build-clean at ~10 pp,
  citation chain closed, F1 closed, F2 partial, F3 ameliorated,
  F4 deferred to operator (Q31). G1 fully closed; M2 done;
  prompt 7 retired in same session.
- `UPGRADE_V2_1_PARTIAL` — partial revisions; one or more gaps remain.
- `HALT_*` — gate failures (resumable).

The agent will print a `BRIDGE:` and `CLAUDE_FETCH:` URL pair
at the end of its run.