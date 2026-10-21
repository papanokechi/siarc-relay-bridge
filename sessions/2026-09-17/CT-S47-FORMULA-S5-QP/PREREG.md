# PREREG — CT-S47-FORMULA-S5-QP

Third and final instalment of the formula re-derivation pass. Scope: the exact
algebraic `q` and `p` of section 5, and the figures printed beside them.

Written before any computation in this session.

## 0. What this instalment actually closes

CT-S45 did Appendix A, CT-S46 did the 56 displays of sections 0-10 and left 15
routed to a resolving corpus claim rather than re-derived. Three of those 15 are
section 5's located point (`S16-12`), and they are the largest exact expressions
in the paper: six integers up to eleven digits, over `Q(i sqrt 11, sqrt 3)`.

The corpus already contains a check that looks like it covers them, and does
not. `S25-01` re-derived the six generators of the matching system independently
and confirmed that **both recorded solutions** annihilate all six exactly. But
"recorded" means the values as stored in `CT-S16-MEMBERSHIP-C/claims.jsonl`.
Between that record and the printed page there is a transcription step that no
check in the corpus has ever tested. A digit transposed **at typesetting** is
invisible to `S25-01`, to every citation check, and to the clean build.

So the object under test is not the mathematics. It is the specific character
string in `refs/section5.tex`.

## 1. Hypothesis

H: the numerals printed in `section5.tex` lines 117-130 are the located point --
that is, the values as parsed off the page satisfy the matching system exactly,
and their exact integers agree coefficient by coefficient with an independent
solve.

## 2. Observable

Two routes, reported per coefficient, never per display.

**Route ALPHA (decidable; needs no reference value).** Rebuild the six
generators from the construction in `locate_final.py`'s docstring -- family
(4.1) with `theta_0 = theta_1 = 0`, `R = (a^2 + b_0 c - a' D - 1/4)/D^2`,
matched against System C's `r_z` -- and substitute the values **parsed out of
the .tex file**. Observable: each generator's `simplify` is symbolic zero.

This route is decidable and self-contained: a transposition anywhere upstream,
including in the claim text, cannot make a wrong value annihilate the system.

**Route BETA (per-coefficient).** Solve the system independently in this
session. Extract the six integers from the .tex by regex. Compare each integer
separately and report a per-coefficient ledger, so that "the display matches"
is never a single boolean.

**Route GAMMA (the printed approximations).** The four `\approx` figures and the
two `theta_infty` values are also printed digits. Evaluate the exact values at
dps >= 60 and compare each against the printed figure at the precision printed,
one row per figure.

## 3. Falsifiers, with thresholds

- **F1.** Any generator fails to simplify to exact symbolic zero at the parsed
  values. Threshold: exact zero, not a norm. HALT and report.
- **F2.** Any of the six integers differs from the independent solve. Threshold:
  exact integer equality. HALT and report.
- **F3.** Any printed approximation differs from the exact value by more than
  half a unit in its last printed place. Threshold: `|printed - exact| <=
  0.5 * 10^(-k)` for a figure printed to `k` decimals. HALT and report.
- **F4.** The branch pairing is wrong: the `theta_infty` printed with a branch
  does not solve the system on that branch's `t`. Threshold: exact.
- **F5.** Fewer or more than two solutions, or a solution with `q` in `{0, 1}`
  (outside chart `U_0`). Threshold: exact.

## 4. Vacuity pre-checks — the transposition arms

The defect this whole pass exists to catch is a transposed digit. So the
vacuity check is not generic perturbation; it is that exact defect.

- **V1.** For each of the six exact integers, swap its last two digits and
  re-run route ALPHA. Each of the six must make at least one generator nonzero.
  If any transposition still annihilates the system, the generators do not
  determine that coefficient and route ALPHA is vacuous for it -- report that as
  a finding, not as a pass.
- **V2.** A transposition arm that changes nothing (a repdigit ending, e.g.
  `...00`) must be reported as SKIPPED, never as CAUGHT. A no-op mutation that
  scores as a detection is a false control.
- **V3.** Positive control on the parser: the extracted integers, re-rendered
  into the printed LaTeX shape, must reproduce the source line byte for byte
  after whitespace squashing. If the parser can silently drop a digit, every
  route downstream inherits it.
- **V4.** Negative control on route GAMMA: perturbing an exact value in its
  fifth decimal must make its comparison fail, confirming the tolerance is not
  so loose that it accepts anything.

## 5. Advance prediction

Recorded before computing, so that agreement is informative.

I predict **all four routes pass and no repair is needed**, on the ground that
`S25-01` annihilated the recorded values and CT-S46 found sections 0-10 clean.

I attach a specific caveat that makes the prediction falsifiable in a definite
place rather than vaguely: the single most likely failure is **not** in the
eleven-digit integers, which are long enough that a transposition tends to be
caught by eye, but in **`122408`** -- short, unremarkable, and the one integer a
reader's eye slides over -- or in the branch pairing of F4, where the two
`theta_infty` values differ only in a sign and are printed eleven lines apart.

If the pass is clean, that caveat was wrong and I record it as wrong.

## 6. Scope limit, stated in advance

The other twelve route-S-corpus displays are **out of scope** by operator
ruling: they are shorter and a reader would notice. This session does not
license any statement about them. `S47`'s claims say nothing about
`S1-04`, `S26-01`, `S3B-02`, `S4-03`, `S6-C18`, `S16-03`, `S17-10` or `S22-12`.

## 7. Governance

Draft only. No commit, push, tag, PR or deposit. No file outside
`sessions/2026-09-17/CT-S47-FORMULA-S5-QP/` is modified, with one exception
carrying an explicit operator ruling: a new `README.md` is **added** beside the
page images in `CT-S21-DEPOSIT-PREP/pages/`. That is an addition, not an edit;
it strands no digest.
