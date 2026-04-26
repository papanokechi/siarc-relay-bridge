# Handoff — T2B-APERY-INVESTIGATION
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Theoretical analysis of the empirical identity $a_2/b_1^2 = -2/9$ shared
by all 24 $\Trans$ families in $F(2,4)$. Mapped the identity to the
asymptotic Worpitzky parameter under equivalence transformation,
checked classical $\pi$ / $\pi^2$ continued fractions, tested whether
Möbius-of-$\pi$ structure forces the ratio, and enumerated the
achievable ratios under the $D=4$ coefficient bound. Result: the
identity is an **arithmetic-exhaustion artifact** of the small bound,
not a deep structural law and not a Worpitzky critical value.
Deliverables: `t2b_apery_note.md` (theoretical note) and
`_t2b_check.py` (numerical verification at 50 dps).

## Key numerical findings
- Brouncker variant CF $4/\pi = 1 + n^2/(2n+1 + \ldots)$ verified
  to 50 dps; ratio $a_2/b_1^2 = 1/4$ (Worpitzky boundary), not $-2/9$.
  Script: `_t2b_check.py`, dps=50.
- Apéry's CF for $\zeta(2) = \pi^2/6$ is degree-(4,2), ratio
  $a_4/b_2^2 = -1/121 \approx -0.00826$. Different profile from $F(2,4)$.
- $|-2/9| = 0.2222\ldots < 0.25 = |-1/4|$: $F(2,4)$ Trans families
  lie strictly inside the Worpitzky parabolic region, not on boundary.
- Achievable ratios at $D=4$ from the empirical leading-coefficient
  pool $a_2 \in \{-2,1\}$, $b_1 \in \{\pm 2, \pm 3\}$: exactly four
  values $\{-1/2,\ -2/9,\ +1/9,\ +1/4\}$. Of these, $-1/2$ is outside
  the parabolic region (divergent), $+1/4$ is on the boundary, $+1/9$
  empirically populates Rat/Des, leaving $-2/9$ as the unique
  Worpitzky-interior negative ratio that admits a Trans population.

## Judgment calls made
- Used `mp.dps = 50` and 2000 CF terms for the Brouncker verification;
  this is sufficient to verify zero residual against `mpmath.pi` and
  was not specified in the prompt.
- Treated the paper's Prop. `prop:ratio` ("three representative
  families") together with the L2-EXACTNESS-SCANNER's all-24 result
  as the empirical ground truth; the prompt described both.
- Concluded the analysis at Step 4 without escalating to a formal
  Möbius-π forcing proof, because Brouncker $4/\pi$ provides an
  immediate Möbius-of-$\pi$ counterexample with ratio $+1/4 \ne -2/9$.

## Anomalies and open questions
- **Apparent inconsistency in `main_R1.tex`**: Prop. `prop:ratio`
  states the identity for "three representative families" (with
  "up to sign" qualifier), while the prompt and L2-EXACTNESS-SCANNER
  bridge note assert it for all 24 families. The "up to sign" clause
  may indicate that some families have ratio $+2/9$ rather than $-2/9$,
  which would be a sign-flip artifact of the canonical form. **This
  should be cross-checked against the H001-H004 verification artifacts.**
- The achievable-ratio enumeration in Step 3 assumes the empirical
  $a_2 \in \{-2, 1\}$ and $b_1 \in \{\pm 2, \pm 3\}$ from the paper.
  If H001-H004 used a wider leading-coefficient range, the pigeonhole
  argument needs refinement.
- $+1/9$ being absent from Trans is asserted on empirical grounds
  (paper's census). Worth a direct check: does $F(2,4)$ contain any
  family with $a_2 = 1$, $b_1 = \pm 3$ that converges to a
  transcendental? If yes, the pigeonhole argument is incomplete.

## What would have been asked (if bidirectional)
1. Should the equivalence-transformed $c_n \to -2/9$ asymptotic rate
   be computed explicitly for all 24 families (one-shot script) to
   tighten the analysis?
2. Is there interest in an $F(2,5)$ exhaustive search now to test
   the pigeonhole prediction (i.e., whether ratios other than $\pm 2/9$
   appear at $D = 5$)?

## Recommended next step
Run an $F(2,5)$ Trans-stratum search with the existing pipeline.
Predicted outcome under the pigeonhole hypothesis: new
Worpitzky-interior negative ratios (e.g., $-3/16$, $-2/16$, $-3/25$)
appear in the Trans population. If only $-2/9$ persists, escalate
to a genuine structural-arithmetic conjecture worthy of a separate
investigation.

## Files committed
- `t2b_apery_note.md` — 1-page theoretical note (sections a–e)
- `_t2b_check.py` — mpmath verification script (dps=50, Brouncker
  4/π verified, achievable-ratio enumeration)
- `handoff.md` — this file

## AEAL claim count
0 entries written to claims.jsonl this session — all numerical claims
are reproductions of standard CF identities (Brouncker 4/π) or
elementary arithmetic (ratio enumeration) and do not require AEAL
logging per project convention. The Brouncker verification is
reproducible via `_t2b_check.py` at any dps ≥ 50.
