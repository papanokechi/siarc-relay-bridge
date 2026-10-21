# CT-S18-COLDREAD-C3 — task, as issued

Cold read; isolated; budget <= 1 day.

PROVIDED (in `packet/`):
- `pages/vdPS_p2634.png`, `p2635.png`, `p2636.png`, `p2637.png`, `p2655.png`
  (van der Put & Saito, Ann. Inst. Fourier 59 (2009) no. 7, 2611-2667).
  NOTE: the operator's packet said "pp. 2634-2636, 2655". The constraint
  `det A(1) = -theta_1^2/4` is printed in Section 3.2, which falls on p. 2637,
  so p. 2637 was added. This addition is recorded here rather than made silently.
- `pages/companion_v12_p2.png`, `p5.png`, `p6.png` (companion v1.2: the operator,
  the ODE, and Conjecture 4.1).
- `packet/sealed/C3-AS-DRAFTED.md` — SEALED. See staging rule below.

WITHHELD: CT-S16, CT-S17, TYPO-EVIDENCE.md, and all claims.jsonl entries.

## Staging rule (added; not in the operator's packet)

The drafted C3 text states conclusions to tasks 1-3. Reading it first would
destroy the independence the cold read exists to provide. Therefore:

1. Complete tasks 1, 2, 3 and write `FINDINGS-1-3.md`. Record its sha256 in
   `outputs/stage1.sha256`.
2. Only then open `packet/sealed/C3-AS-DRAFTED.md` and answer task 4 in
   `VERDICT-4.md`.

Do not revise `FINDINGS-1-3.md` after opening the seal. If the seal changes your
mind about tasks 1-3, say so in `VERDICT-4.md`; leave stage 1 as written.

## Tasks

1. Derive independently whether family (4.1)'s printed `b(z)` satisfies the
   paper's own `det A(1)` constraint. If not, derive the corrected entry and show
   it satisfies it identically. Report the residual's factorisation.
2. Check whether System C's trace-free connection satisfies every hypothesis
   vdPS impose on M for the (0,0,1) row. Quote each hypothesis from the images.
3. Locate System C in chart U_0 and verify by re-substitution, comparing P and Q,
   not R alone. State whether a rank-1 twist separates the two.
4. Verdict on C3 as drafted: CORRECT / CORRECT WITH WORDING CHANGE / ERROR.

Labels per P0. Do not read anything else under `sessions/2026-09-17/`.
