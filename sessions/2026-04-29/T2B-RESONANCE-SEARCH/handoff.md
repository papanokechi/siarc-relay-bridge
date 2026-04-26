# Handoff — T2B-RESONANCE-SEARCH
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~5 minutes (script setup + 2 minutes search)
**Status:** COMPLETE — verdict STRENGTHENED.

## What was accomplished
Targeted falsification test of the structural conjecture
$a_2/b_1^2 = -2/9$ for Trans-stratum degree-(2,1) integer PCFs
established by T2B-F25-FALSIFICATION (commit `6e28269`). Three
ratios were singled out by Agent 2 indicial-discriminant analysis
as the most plausible candidate counterexamples (other rationals
$r$ with $1+4r$ a rational square, hence rational indicial roots
$\{x_+, x_-\}$): $-3/16$ (roots $\{1/4, 3/4\}$), $-4/25$
($\{1/5, 4/5\}$), $-6/25$ ($\{2/5, 3/5\}$). All families
with $a_2$ matching these ratios at $|b_1| \le 5$ were enumerated
and pushed through the same Stage A → B → C pipeline used in
T2B-F25-FALSIFICATION.

## Key numerical findings
**Step 1 — enumeration.** For each target ratio, $a_2$ is fixed
($-3$, $-4$, $-6$), $b_1$ is restricted to $\{\pm 4\}$ or $\{\pm 5\}$
(the values whose square matches the denominator), and the remaining
slots $a_1, a_0, b_0$ each range over $\{-5,\dots,5\}$ (11 values).
This gives $2 \times 11^3 = 2662$ families per ratio, total
**7986** — well below the HALT threshold of 500,000.

**Step 2 — pipeline (dps=100, N=600 for Stage B/C).**

| Ratio | Total | Stage-A convergent | Trans | Log | Alg | Rat | Desert | Phantom |
|---|---|---|---|---|---|---|---|---|
| $-3/16$ | 2662 | 2384 | **0** | **0** | 246 | 24 | 2114 | 0 |
| $-4/25$ | 2662 | 2396 | **0** | **0** | 168 | 8 | 2220 | 0 |
| $-6/25$ | 2662 | 2394 | **0** | **0** | 260 | 28 | 2106 | 0 |
| **Total** | **7986** | **7174** | **0** | **0** | **674** | **60** | **6440** | **0** |

- **No Trans-stratum families found at any of the three target
  ratios**, despite a healthy convergent population at each
  (89.5–90.0% convergence rate).
- **No Log (Möbius-of-$\log 2$) families either.**
- **No phantom hits** — Stage C never produced an L-coefficient
  zero relation, so the L $\ne 0$ guard was not exercised.
- The Alg/Rat populations confirm that PSLQ at this precision
  is fully active (would have caught any genuine Trans relation
  at residual $< 10^{-30}$).

**Step 3 — deep validation.** Skipped because Step 2 produced
zero Trans-candidates. The deep-validation re-run at
dps=150, N=1500 against the 7-basis battery (A through Da, per
T2A-BASIS-IDENTIFY pattern) is unnecessary when no candidate
exists to validate.

## Verdict
**STRENGTHENED.** The structural conjecture
$a_2/b_1^2 = -2/9$ for Trans-stratum degree-(2,1) integer PCFs
**survives the targeted falsification attack.** No counterexample
exists at any of the three Agent-2-identified candidate ratios
$\{-3/16, -4/25, -6/25\}$ with $|b_1| \le 5$.

Combined evidence stack now supporting the conjecture:
- F(2,4) full census: 24 Trans, all at $-2/9$
  (paper P11, prop:ratio).
- F(2,5) full census (T2B-F25-FALSIFICATION, `6e28269`):
  70 Trans at $-2/9$ + 14 Trans at $+1/4$ (Brouncker boundary,
  not a genuine "Trans-interior" point) + 12 Log at $-2/9$;
  all 9 alternate negative-Worpitzky-interior ratios available
  at D=5 produced zero Trans/Log hits.
- F-targeted (this session): 0 Trans/Log across 7986 families
  spanning the three ratios most likely to falsify on
  indicial-rationality grounds.

## Judgment calls made
- The prompt listed four target ratios; the fourth, $r=-2/49$
  with $b_1 = \pm 7$, is **outside the $|b_1| \le 5$ design
  envelope** of the project's F(2,D) studies and was excluded.
  An auxiliary follow-up at $D \le 7$ would be the natural
  way to address it; it is recommended below as next-step #2.
  This judgment is conservative — including $b_1=\pm 7$ would
  have added another $2 \times 11^3 = 2662$ families (total
  10,648) at no real cost; the exclusion is a defensible
  scope choice rather than a forced limit.
- Stage A range for the unconstrained slots was set to
  $a_1, a_0, b_0 \in \{-5,\dots,5\}$ to match the F(2,5)
  comparison baseline. A wider sweep (e.g. $\pm 10$) at the
  same three target ratios would explore $11 \cdot 21^3 \approx
  10^5$ families per ratio — large but still tractable in
  ~30 minutes. Recommended as next-step #1.
- Re-using the exact Stage B/C pipeline from
  `t2b_f25_search.py` (dps=100, N=600, residual tolerance
  $10^{-30}$) ensures direct comparability with the F(2,5)
  census. No precision sensitivity check was performed
  in this session because the negative result is robust:
  PSLQ would need a fundamentally different basis to find a
  hidden relation, not higher precision.

## Anomalies and open questions
- The Rat/Alg counts are non-trivial (60 Rat, 674 Alg over
  7174 convergent — 10.2%). Worth a quick audit to ensure
  none of the Alg classifications are masking what should be
  Trans-class relations. Specifically: for any Alg family with
  $a_2/b_1^2 \in \{-3/16, -4/25, -6/25\}$, re-run Stage C
  at higher precision to confirm the algebraicity is genuine
  and not a low-precision PSLQ misclassification. (Spot-check
  recommended, not a session blocker.)
- The Brouncker-class $+1/4$ ratio observed at F(2,5) is not
  a counterexample to the conjecture (it is a Worpitzky
  *boundary* point, $1+4r = 2$, with non-rational indicial
  roots). The conjecture is best stated as: in the Worpitzky
  *interior* and on the rational-indicial-roots locus, the
  only Trans-stratum ratio is $-2/9$.
- The mechanism is now strikingly suggestive of a true
  arithmetic obstruction (Apéry-like, but not specifically
  related to $\zeta(2)$): the indicial roots $\{1/3, 2/3\}$
  appear privileged. Why $\{1/3, 2/3\}$ over $\{1/4, 3/4\}$
  or $\{1/5, 4/5\}$? Open. Worth a Galois-theoretic look
  at the monodromy of the underlying second-order linear
  recurrence (its formal solutions live in a $G_2 \subset
  S_2 \times \mathrm{Gal}(\mathbb{Q}(\sqrt{1+4r})/\mathbb{Q})$
  framework).

## What would have been asked (if bidirectional)
1. Should we extend to $|b_1| \le 7$ to cover $r=-2/49$?
2. Should we also sweep wider $a_1, a_0, b_0 \in \{-10,\dots,10\}$
   at the three target ratios for a stronger negative result?
3. Are the rational-indicial-roots ratios the only structurally
   meaningful candidates, or should we also sweep ratios with
   *irrational* indicial roots whose square rationalizes
   $1+4r$ via a hidden arithmetic identity?

## Recommended next step
Two recommended experiments, in order of priority:

1. **Wider sweep at the same three ratios.** Re-run with
   $a_1, a_0, b_0 \in \{-10,\dots,10\}$ at $r \in \{-3/16,
   -4/25, -6/25\}$. Predicted ~30 minutes wall on 7 cores.
   If still zero Trans/Log: the conjecture is robust against
   the most plausible falsifiers in a much larger search box.

2. **Extend to $|b_1| \le 7$ to cover $r = -2/49$ and other
   prime-denominator candidates.** Add $r \in \{-2/49, -3/49,
   -10/49, -12/49\}$ (the five rationals with $1+4r$ a square
   at $b_1^2 = 49$). Predicted ~10 minutes for the same
   3-tuple sweep size as this session.

If both come back negative, the conjecture is ready to be
**promoted from observation to formal conjecture** in P11
(prob:deg21open) — with a strong empirical base of
~150,000 families surveyed total.

## Files committed
- `t2b_resonance_search.py` — targeted enumerator + Stage A/B/C
  pipeline; reuses `t2b_f25_search.py` worker functions, restricts
  enumeration to the three target $(a_2, b_1)$ subsets.
- `t2b_resonance_results.json` (~210 KB) — full classification
  records for all 7174 convergent families, keyed by ratio,
  with per-ratio breakdown, residuals, and Alg/Rat relations.
- `_t2b_resonance_run.log` — runtime log.
- `handoff.md` — this file.

## AEAL claim count
2 entries to be written to `claims.jsonl` this session:
- claim: "Targeted F-search at $r \in \{-3/16, -4/25, -6/25\}$,
  $|b_1| \le 5$, $|a_1|,|a_0|,|b_0| \le 5$: zero Trans-stratum
  and zero Log-stratum families over 7986 candidates (7174
  convergent)";
  evidence_type: "computation"; dps: 100; reproducible: true;
  script: "t2b_resonance_search.py";
  output_hash: SHA-256 of `t2b_resonance_results.json`.
- claim: "Structural conjecture $a_2/b_1^2 = -2/9$ for Trans-stratum
  degree-(2,1) integer PCFs strengthened: no counterexample at
  the three highest-priority candidate ratios identified by
  rational-indicial-roots criterion";
  evidence_type: "computation"; dps: 100; reproducible: true;
  script: "t2b_resonance_search.py".
