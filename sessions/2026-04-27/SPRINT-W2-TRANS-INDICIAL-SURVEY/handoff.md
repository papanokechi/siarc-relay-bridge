# Handoff — SPRINT-W2-TRANS-INDICIAL-SURVEY
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 min
**Status:** COMPLETE  (negative-with-corollary: no new indicial invariant found, but an iff theorem connecting the Trans ratio to the characteristic-root modulus was confirmed by PSLQ)

## What was accomplished
Surveyed 50 integer Trans families ($a_2/b_1^2 = -2/9$) and 20 non-Trans families using the W1 closed-form indicial exponent formula. Tested whether sum, product, or discriminant of indicial exponents is constant across the Trans locus — they are not. The only universal Trans invariant in the Birkhoff leading-order framework is $|\mu_+/\mu_-| = (13 + 3\sqrt{17})/4$, which is algebraically equivalent to the Trans definition itself. PSLQ at dps=150 with non-zero L-coefficient confirmed this identity.

## Key numerical findings
- **`|μ+/μ-|` is constant** across all 50 Trans families: $(13 + 3\sqrt{17})/4 = 6.34232921921324541236605739198\ldots$ (confirmed to >100 digits).
- **Sum** $S = \alpha_+ + \alpha_-$ takes 3 distinct values $\{-3, -1, +1\}$ across the 50 families (driven by $s = a_1/b_1$).
- **Product** $P$ takes 9 distinct values in $[-2.235, +2.235]$.
- **Discriminant** $D = (\alpha_+ - \alpha_-)^2$ takes 8 distinct values in $[0.059, 9.94]$.
- **PSLQ result** on basis $\{1, \sqrt{17}, |\mu_+/\mu_-|\}$: integer relation $[13, 3, -4]$, L-coeff $= -4 \neq 0$, reconstruction error $= 0$ at >100 digits. Phantom Hit Rule passes.
- **Wider PSLQ** on $\{1,\sqrt 2, \sqrt 3, \sqrt 5, \sqrt{17}, \pi, \log 2, \rho\}$: returns the same identity $-13 - 3\sqrt{17} + 4\rho = 0$, with $L$-coeff $= 4 \neq 0$, all other algebraic-irrational coefficients zero.
- **Sympy verification:** $q := \mu_+/\mu_- = -(13+3\sqrt{17})/4$ gives $a_2/b_1^2 = q/(1+q)^2 = -2/9$ exactly. The positive-modulus branch $q = +(13+3\sqrt{17})/4$ gives $a_2/b_1^2 = +2/17$ — distinct locus.

## Revised theorem (Form 4)
> Let $b_1 \neq 0$, $a_2 < 0$. Then $a_2/b_1^2 = -2/9$ iff $|\mu_+/\mu_-| = (13+3\sqrt{17})/4$, where $\mu_\pm$ are roots of $\mu^2 - b_1\mu + a_2 = 0$.

The converse holds **with** the sign condition $a_2 < 0$; without it, the modulus identity selects two loci ($-2/9$ and $+2/17$).

## Judgment calls made
- **Synthetic vs T2B-dataset families.** The T2B Trans dataset wasn't accessed directly; instead I generated 50 small integer families satisfying the Trans constraint $a_2/b_1^2 = -2/9$ (which forces $b_1 \in 3\mathbb{Z}$). The conclusion is structural, not statistical, so the synthetic set is sufficient — any real T2B family would lie on the same locus.
- **Indicial-formula domain.** For Alg families with $a_2 = 0$, one of the $\mu$'s is zero and the W1 formula has a vanishing denominator. I returned `None` for those entries rather than abort; the survey continues using the remaining quantities.
- **No higher-order Birkhoff balance.** The $[n^{-1}]$ balance was deferred to Week 3 since deriving it cleanly requires expanding $(1\pm 1/n)^\alpha$ to order 2 and re-using the W1 indicial value — straightforward but a separate computation.
- **No push.** Per session prompt.

## Anomalies and open questions
- **The most important takeaway.** *The Birkhoff leading-order indicial framework does not see what makes Trans families special.* The Trans locus is a projective hypersurface in coefficient space (codim 1: $9 a_2 + 2 b_1^2 = 0$), and on this hypersurface the indicial exponents form a 2-parameter family in $(r, s) = (b_0/b_1, a_1/b_1)$ with no universal value. The only thing that *is* universal — the modulus ratio of characteristic roots — is by Vieta a function of $a_2/b_1^2$ alone, hence tautological.
- **Why does $a_2/b_1^2 = -2/9$ produce transcendental limits at all?** It is precisely the rational point where the discriminant of $\mu^2 - b_1\mu + a_2 = 0$ becomes $b_1^2(1 + 8/9) = b_1^2 \cdot 17/9$, introducing $\sqrt{17}$. This means *the characteristic ratio is irrational with quadratic surd $\sqrt{17}$*, but the same is true for many other rationals (e.g. $-1/9$ gives $\sqrt{13}/3$, etc.). What sets $-2/9$ apart is not visible at this level.
- **Convergence-rate uniformity.** All 50 Trans families converge at the same exponential rate $\rho^{-n}$ with $\rho = (13+3\sqrt{17})/4$, but the *sub-exponential* correction (controlled by the indicial exponent) differs. So the "Trans speed" is universal but the "Trans signature" within that speed varies.
- **Apparent mass concentration in `S`.** All 50 Trans families have $S \in \{-3, -1, +1\}$ — this is because I chose $a_1 \in \{-2a_2, 0, 2a_2\}$ in the generator, giving $s = a_1/b_1 \in \{-2 a_2/b_1, 0, 2 a_2/b_1\}$ and thus three discrete $S$ values. With a finer $a_1$ grid the sum would take a continuum.
- **Numerical $\alpha$-fit** matches the symbolic dominant root to ~$10^{-3}$ (the dominant root for $a_2 < 0$ is the smaller-$|\alpha|$ root since $\mu_+ > 0 > \mu_-$ on the Trans locus). No anomaly.

## What would have been asked (if bidirectional)
1. **T2B dataset access.** Are the 585k Trans families in `t2b/...` available as a tuple list? If so, run `indicial_survey.py` on a 1000-sample to confirm the universality of `|μ+/μ-|` empirically.
2. **Should the next sprint pivot to Padé rates?** The convergence-rate exponent $\rho^{-n}$ is universal on the Trans locus, but the constant in front is not. PSLQ on those constants might find a Galois-resolvent invariant.
3. **Is there a published result connecting Trans (in the Apéry / hypergeometric-CF sense) to a $\sqrt{17}$ surd?** I haven't seen one; this would be worth a literature pass.

## Recommended Week-3 prompt
> *"Compute the $[n^{-1}]$ Birkhoff balance for the degree-(2,1) PCF on the Trans locus $a_2 = -2b_1^2/9$, using the W1 indicial value $\alpha(\mu) = -((b_1-b_0)\mu + (a_1-a_2))/(b_1\mu - 2 a_2)$ as known. Specifically, expand the recurrence ansatz to order $1/n^3$, multiply by $n^3$, isolate the $[n^0]$ coefficient (which is now a polynomial in $a_0$, $b_0$, $a_1$, $b_1$ with the W1 $\alpha$ substituted in). Solve for the relation that this coefficient must satisfy for the ansatz to remain consistent. If this gives a non-trivial constraint involving $a_0$, that is the missing forcing condition. If it is identically zero (i.e. automatically satisfied), pivot to Padé convergence-rate analysis: compute $\lim_{n\to\infty} |y_n/x_n - L| / \rho^{-n}$ for several Trans families, run PSLQ on the limits, look for a Galois invariant."*

## Files committed
- `sprint_w2/indicial_survey.py`
- `sprint_w2/separation_test.py`
- `sprint_w2/forcing_condition.py`
- `sprint_w2/_indicial_survey.log`
- `sprint_w2/_separation_test.log`
- `sprint_w2/_forcing_condition.log`
- `sprint_w2/indicial_survey.json`
- `sprint_w2/claims.jsonl`
- `sprint_w2/halt_log.json`
- `sprint_w2/discrepancy_log.json`
- `sprint_w2/unexpected_finds.json`
- `sprint_w2/sprint_w2_report.md`
- `handoff.md` (this file)

## AEAL claim count
**6** entries in `sprint_w2/claims.jsonl`.
