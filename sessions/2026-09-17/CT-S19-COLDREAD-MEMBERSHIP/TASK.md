# CT-S19-COLDREAD-MEMBERSHIP — task, as issued

Cold read; isolated; budget <= 1 day.

## Why this packet exists

A previous cold read of this material returned a verdict that was overruled,
because it silently made a choice the packet had not asked it to justify. That
choice is now **task 1**, named explicitly, so that whatever you conclude rests
on an argument rather than on a default. You are NOT told what the previous
reader chose, nor what the outcome was.

PROVIDED (in `packet/`):
- `pages/vdPS_p2634.png` ... `p2637.png`, `p2654.png`, `p2655.png`, `p2656.png`
  (van der Put & Saito, Ann. Inst. Fourier 59 (2009) no. 7, 2611-2667).
- `pages/companion_v12_p2.png`, `p5.png`, `p6.png` (companion v1.2).
- `packet/sealed/MEMBERSHIP-SENTENCE.md` — SEALED. See staging rule.

WITHHELD: CT-S16, CT-S17, CT-S18, all adjudication files, and all claims.jsonl
entries anywhere in the tree.

KNOWN DEFECT IN THE SOURCE, given to you so you do not have to rediscover it:
on p. 2655 the first square in `b(z)` prints `(p + 1/2(q-1)q)^2`. This appears to
be a typo for `(p + 1/2(q-1)q t)^2`; the printed form fails the paper's own
`det A(1) = -theta_1^2/4` and the corrected form satisfies it identically. Verify
this for yourself in one line, then use the corrected form. This is given because
it is settled and is not what this packet is testing.

## Staging rule

1. Complete tasks 1-4 and write `FINDINGS-1-4.md`; record its sha256 in
   `outputs/stage1.sha256`.
2. Only then open `packet/sealed/MEMBERSHIP-SENTENCE.md` and answer task 5 in
   `VERDICT-5.md`.
Do not revise `FINDINGS-1-4.md` after opening the seal.

## Tasks

1. **The component question.** A rank-2 first-order system `Y' = N Y` does not
   determine a single scalar second-order ODE. Derive, from scratch and by
   elimination, every scalar reduction it admits; say exactly which component of
   `Y` each one governs, and how they differ. Then decide **which one a given
   scalar equation must be compared against**, and justify the decision from the
   structure of the equations rather than by convention. Read the paper's own
   definition of `q` off the page images and say whether it bears on the choice.
2. **Locate System C.** System C is `(3x^2+x+1) y'' + (6x+1) y' - x^2 y = 0`.
   Map its two finite singular points to `z = 0, 1` by an affine change, then
   determine whether there is a point of the chart `U_0` of family (4.1) whose
   associated scalar equation is System C. Derive the point yourself; do not
   assume one exists. Verify by re-substitution comparing **both** `P` and `Q` in
   `y'' + P y' + Q y = 0`, never the normal-form invariant `R` alone, since `R`
   is blind to a rank-1 twist.
3. **Independent control.** Whatever you conclude in task 2, test it by a route
   that does not reuse the same algebra: for instance, solve the *system*
   numerically at an ordinary point and check which scalar ODE the relevant
   component actually satisfies, over more than one initial condition. State the
   residuals and the dps.
4. **Hypotheses.** Check System C's trace-free connection against every
   hypothesis vdPS impose on `M` for the `(0,0,1)` row. Quote each hypothesis
   from the page images. Report SATISFIED / VIOLATED / UNDECIDED with reasons.
5. **Verdict** on the sealed sentence: CORRECT / CORRECT WITH WORDING CHANGE
   (give the change) / ERROR.

Labels per P0. A table-row or formal-type match is STRUCTURAL at most and is a
necessary condition only. Do not read anything else under `sessions/2026-09-17/`.
