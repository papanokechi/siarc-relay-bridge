# PREREG — CT-S46-FORMULA-SECTIONS

Written before `route_s_sections.py` is executed. Prediction F5 below was
reached by hand expansion, on paper, before the script existed.

## Hypothesis

Every displayed formula in sections 0–10 of the paper is either

- **route S** — reproducible by symbolic computation from other material the
  paper itself displays, or from a named corpus script; or
- **route P** — a transcription of a specific page of a specific source, to be
  compared against the held page image with the folio read off that image;

and each display's printed form agrees with whichever route it takes.

An equation for which **neither route is available in this session** is
reported `UNROUTED`. That is a finding about the paper, not a gap to be
quietly closed.

## Observable

For route S: the sympy residual
`simplify(together(expand(derived − displayed)))`, which must be exactly `0`.

For route P: the literal agreement of the transcribed symbols against the
page image, with the running head, folio and one adjacent sentence quoted from
the image as proof the correct page was read.

## Falsifiers, with thresholds

- **F1** Any route-S residual is non-zero. Threshold: exact `0`; no tolerance,
  these are rational-function identities.
- **F2** The display census extracts fewer than 10 displays, or captures
  inline math, or captures `\\[2pt]` line-break spacing. Any of these means
  the reader is broken and no census figure may be reported.
- **F3** Any figure cited in a claim does not resolve to a line of its
  evidence file that also carries the named anchor for that figure. (The
  standing rule from S44-17: a numeral in a file does not evidence that
  quantity — `128` once matched a line number.)
- **F4** The display-consistency check fails to flag its planted
  sign-differing control pair.
- **F5 — the advance prediction.** Hand expansion of System C under
  `x = s_+ + δz`, with `s_+ = (−1+i√11)/6` and `δ = −i√11/3`, gives

  `Q(z) = (22z² − 22z − 2i√11 z + 5 + i√11) / (54 z(z−1))`,

  which **agrees** with the printed `eq:QC`, and

  `P(z) = (2z−1)/(z(z−1))`, which **agrees** with the printed `eq:PC`.

  Likewise the normal potential of `eq:sysA` expands to
  `(−3z² − 5z + 3)/(9z³)`, which **agrees** with the printed `eq:rA`.

  These three are therefore predicted to MATCH. If the script reports DIFFERS
  on any of them, either my hand expansion or the script is wrong and the
  disagreement must be resolved by a third route before anything is recorded.
  This is registered because `eq:QC`'s `22/22/54/5` is the display the
  operator named as the transposed-digit risk, and a check that can only
  confirm is worth nothing: the prediction is what makes a MATCH informative.

## Vacuity pre-checks

The observable must be shown to move when the data the hypothesis is about
moves. Before any verdict is reported:

- **V1** Perturbing a single coefficient of `eq:sysA` (e.g. `10z²f' → 11z²f'`)
  must make the `eq:rA` residual non-zero. If it does not, the check is not
  reading the equation it claims to read.
- **V2** Perturbing one digit of the printed `eq:QC` — precisely the defect
  class under test — must make its residual non-zero.
- **V3** The unperturbed residuals must be `0`, so that V1 and V2 are
  measuring a change and not a constant failure.
- **V4** At least two perturbations must be drawn from **outside** any list
  the script itself enumerates, so that the arms do not merely confirm that
  the script consults its own constants.

## Budget

3 hours. Halt and report at 9 hours.

## Halt conditions

Halt and report rather than improvise if a falsifier fires, a convention is
ambiguous, required data is missing, or the budget is exceeded threefold.
