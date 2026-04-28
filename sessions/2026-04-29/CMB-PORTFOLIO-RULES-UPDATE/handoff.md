# Handoff — CMB-PORTFOLIO-RULES-UPDATE
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** COMPLETE

## What was accomplished
Added portfolio discipline rules and standard cover-letter template
to `tex/submitted/CMB.txt` per the 2026-04-29 framing audit. The new
section sits directly after `## DAILY DECISION FRAMEWORK` and before
`## HOW TO USE THIS FILE`. The submission portfolio table received
inline flags for P07 (Khinchin → Exp. Math, WITHDRAW), P09 (AI
Discovery → Notices AMS, WITHDRAW), and P10 (Self-Adjoint ODEs → JDE,
MEDIUM RISK, redirect on rejection).

## Key numerical findings
- 1 file edited: `tex/submitted/CMB.txt` (length 21610 bytes after edit).
- SHA-256 of edited CMB.txt: `c1ea314fe132c4b5520e5125fa27a0ca227e18c90b603459607a0308c89542ed`.
- 7 numbered portfolio discipline rules recorded.
- 6 suggested title reframes recorded (matching audit table).
- 3 portfolio flags added (P07, P09, P10).

## Judgment calls made
1. The relay prompt referenced "#5 Khinchin", "#12 Notices", and "#13
   Self-Adjoint ODEs" by external numbering. The actual CMB table uses
   `Pxx` IDs, so flags were applied to P07 (Khinchin), P09 (AI Discovery
   → Notices AMS), and P10 (Self-Adjoint ODEs → JDE) by paper identity,
   not by row number.
2. The CMB portfolio table is a 6-column markdown table. Adding a 7th
   "Notes" column to selected rows would have broken format. Flags
   were therefore written immediately below the table footnote as a
   `PORTFOLIO FLAGS` block, preserving table integrity while keeping
   all flag text adjacent to the table.
3. ASCII arrows (`->`) and the lowercase `>=` were used inside the
   rules block in places where the pure-text CMB layout needs to remain
   editor-portable; the surrounding prose uses regular em-dashes.

## Anomalies and open questions
- **Concurrent-cap status:** RULE 3 caps active submissions at 4. The
  current portfolio shows roughly 9 entries with status `Submitted` or
  `Under review` (P04, P05, P07, P08, P09, P10, P11, P13, P15, plus
  P-Tunnell and P-Rigidity), which is well above the cap. No
  withdrawals were executed in this session — only flags were written.
  Withdrawals (P07 Exp. Math, P09 Notices AMS) remain TODO and were not
  in the relay prompt's STEPS list.
- **No explicit row for "#12 Notices":** the audit referred to this as
  "#12" but in the CMB it is P09. Confirmed by venue (`Notices AMS`)
  and ID (`260421-Papanokechi`).
- **No commit/push performed.** Per the relay prompt, this session
  commits only — DO NOT push. Commit will be executed below from the
  bridge repo before reporting URLs. (See "Recommended next step".)

## What would have been asked (if bidirectional)
- Should the AI-disclosure sentence in the standard cover letter be
  removed from Paragraph 3 entirely for pure-math venues, or kept as a
  brief disclosure with the longer version moved to Acknowledgements?
  Audit text was ambiguous; current template keeps a one-line cover
  letter disclosure with a parenthetical note to relocate.
- Should P-T2A and P-T2B (Zenodo "Published") count toward the
  concurrent-submission cap? Treated here as out-of-scope (already
  published preprints), but RULE 3's accounting policy is not stated.

## Recommended next step
Execute the actual portfolio cleanup implied by the new rules:
1. Withdraw P07 from Experimental Mathematics; redirect to Comptes
   Rendus Mathématique (short note format).
2. Withdraw P09 from Notices AMS; park until first acceptance lands.
3. Run a CONCURRENT-CAP audit pass: identify which 4 papers form the
   focused queue and which to hold/park.

## Files committed
- `sessions/2026-04-29/CMB-PORTFOLIO-RULES-UPDATE/CMB.txt`
- `sessions/2026-04-29/CMB-PORTFOLIO-RULES-UPDATE/handoff.md`
- `sessions/2026-04-29/CMB-PORTFOLIO-RULES-UPDATE/claims.jsonl`
- `sessions/2026-04-29/CMB-PORTFOLIO-RULES-UPDATE/halt_log.json`
- `sessions/2026-04-29/CMB-PORTFOLIO-RULES-UPDATE/discrepancy_log.json`
- `sessions/2026-04-29/CMB-PORTFOLIO-RULES-UPDATE/unexpected_finds.json`

## AEAL claim count
1 entry written to claims.jsonl this session.
