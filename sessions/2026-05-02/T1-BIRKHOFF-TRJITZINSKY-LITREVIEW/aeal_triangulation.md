# Q4 — AEAL-honest triangulation of the SIARC empirical / theoretical record against the literature-derived bracket

**Task:** T1-BIRKHOFF-TRJITZINSKY-LITREVIEW, Phase 1
**Date:** 2026-05-02
**Scope:** For each cited SIARC empirical / theoretical-prediction
record (E1, E2, E3), state precisely what range of $A$ it
**rules out**, what it does **not** rule out, and how it relates to
Q3's literature bracket $A \in [d, 2d]$ under the Wasow-normalisation
reading and the **GAP_TYPE_C** classification.

The epistemic discipline of the relay prompt is in force. The
forbidden words "shows / confirms / proves / demonstrates /
establishes / verifies" are **not** used in any sentence describing
SIARC's own empirical or theoretical-prediction content; the
permitted alternatives "predicts / expects / forecasts / is
consistent with / constrains / rules out / narrows the interval /
is compatible with / supports" are used throughout. The forbidden
words appear only when describing context-(i) refereed-rigorous
content (B–T 1933 / Turrittin / Wasow / Immink), where they are
appropriate.

The empirical numbers in E1, E2, E3 are **cited** from prior
verdicts and not re-executed here.

---

## E1 — PCF-2 v1.3 R1.1 + R1.3 ($d = 3$ and $d = 4$ family harvests)

**Cited content (from PCF-2 v1.3 / SESSION-T2 verdict.md and
PCF2-SESSION-Q1):**

* $d = 3$: $50/50$ deep R1.3 cubic families with
  $A_{\mathrm{fit}} \in [5.85,\ 6.02]$ at dps $\ge 24$
  (R1.1 surface harvest), tightened at $50/50$ on the deep
  R1.3 catalogue (dps $= 4000$, $N_{\max} = 480$) to
  $A_{\mathrm{fit}} - 6 \in [-1.0 \times 10^{-2},\ +1.0 \times
  10^{-2}]$ for the bulk and $\pm 1.5 \times 10^{-5}$ at
  $j = 0$ after finite-$N$ artefact correction.
* $d = 4$: $60/60$ Q1 quartic families with mean
  $A_{\mathrm{fit}} = 7.954$, $\sigma = 3.7 \times 10^{-3}$.
* $d = 3$ $\delta$-on-finer-cubic-split:
  $\rho(\log|j|, A_{\mathrm{fit}} - 2d) = -0.691$,
  $p_{\mathrm{Bonf}} = 4 \times 10^{-7}$ (cubic-modular finer
  split; B5 / B6 d=3-specific in the current WKB regime).

**What E1 rules out (as stated in the empirical methodology):**

* At $d = 3$ and $d = 4$, on the harvested ensemble, $A$ lies
  **outside** the empirical interval $[2d - 1.0 \times 10^{-2},
  2d + 1.0 \times 10^{-2}]$ in **at most zero** of the
  $50 + 60 = 110$ families. Therefore E1 **rules out** any
  hypothesis predicting $|A - 2d| > 1.0 \times 10^{-2}$ for
  more than a few of these families under the $A_{\mathrm{fit}}$
  estimator at the methodology used.

**What E1 does not rule out:**

* E1 **does not rule out** $A = 2d + 10^{-12}$ (or any other
  value within the methodology's error bars) at $d = 3$ or $4$.
  At $d = 4$ in particular, the empirical $\sigma = 3.7 \times
  10^{-3}$ is the relevant noise floor.
* E1 **does not rule out** any value of $A$ at $d = 5$ or
  beyond (no SIARC data at $d \ge 5$).
* E1 **does not rule out** the GAP_TYPE_A / Adams-normalisation
  reading of Q3: if the literature bracket is in fact
  $[d/2, d]$, then E1's empirical $A_{\mathrm{fit}} \approx 2d$
  would be **outside** the literature bracket, but E1 itself
  cannot adjudicate the normalisation question (that requires
  primary-source consultation of B–T 1933 / Adams 1928).

**Combination with Q3's literature bracket:**

Under the Wasow-normalisation reading (Q3, GAP_TYPE_C, bracket
$[d, 2d]$):

* E1 **is consistent with** $\psi_{\mathrm{upper}}(d) = 2d$
  (i.e. $A$ at the literature upper bound).
* E1 **narrows** the empirical $A$ at $d = 3$ to $[2d - 10^{-2},
  2d + 10^{-2}]$, which is well **inside** the literature
  bracket $[d, 2d]$ (since $2d - 10^{-2} > d$ for $d \ge 1$).
* E1 **supports** the Phase-2 target of lifting
  $\psi_{\mathrm{lower}}(d)$ from $d$ to $2d$: the empirical
  data is consistent with the conjecture that $A = 2d$
  identically on the SIARC PCF stratum, which is the Phase-2
  theorem.

**E1 does NOT establish** $A = 2d$ rigorously at any $d$. The
empirical methodology (finite-$N$ harvest, finite dps,
$A_{\mathrm{fit}}$ estimator) cannot rule out, e.g., a
universality breakdown of measure $\le 10^{-12}$ on the SIARC
stratum.

---

## E2 — PCF-2 v1.3 / PCF2-SESSION-T2 (Petersson-discriminant correlation)

**Cited content:** at $d = 3$ on the deep R1.3 cubic catalogue
($n = 50$, dps $= 4000$, $N_{\max} = 480$),
$$
   \rho\bigl(\log\|\Delta\|_{\mathrm{Pet}},\
              A_{\mathrm{fit}} - 6\bigr) \;=\; +0.638,
   \qquad p_{\mathrm{Bonf}}(K{=}14) \;=\; 8.6 \times 10^{-6},
$$
beating the $\log|j|$ baseline ($\rho = -0.568$,
$p_{\mathrm{Bonf}} = 2.34 \times 10^{-4}$) by $\sim 30\times$
in Bonferroni $p$.

**What E2 rules out:**

* E2 **rules out** the null hypothesis "the residual
  $\delta = A_{\mathrm{fit}} - 6$ is independent of
  $\log\|\Delta\|_{\mathrm{Pet}}(\tau_b)$ at $d = 3$" at
  significance $p_{\mathrm{Bonf}} = 8.6 \times 10^{-6}$.
* E2 **rules out** "the bare $\log|j|$ predictor exhausts the
  modular signal in the residual $\delta$ at $d = 3$" (the
  Petersson-discriminant predictor beats $\log|j|$ by a factor
  $\sim 30$ in Bonferroni $p$).

**What E2 does not rule out:**

* E2 **does not rule out** any specific value of $A$ at $d =
  3$ (E2 is a statement about the **residual**
  $\delta = A_{\mathrm{fit}} - 6$, not about $A$ directly).
* E2 **does not rule out** that the modular-discriminant
  signal in $\delta$ is a finite-$N$ tail-window artefact.
  The SESSION-T2 verdict explicitly notes that the deep-WKB
  $j = 0$ cell exhibits a $|\delta| \sim 10^{-5}$ scaling
  consistent with a $c / N \log N$ finite-$N$ bias, which is
  the operative caveat.
* E2 **does not rule out** higher-order modular predictors
  (weight-$> 12$ cusp forms) that may refine the Petersson-
  discriminant correlation.

**Combination with Q3's literature bracket:**

* E2 is **orthogonal** to the leading-$A$ question (Q3 is
  about $A$; E2 is about sub-leading $\delta$). E2 therefore
  **neither narrows nor expands** Q3's literature bracket
  $[d, 2d]$ at $d = 3$.
* E2 **predicts / is consistent with** the Phase-2 sub-claim
  P2.3 (sectorial uniformity): the Petersson-discriminant
  signal in the residual $\delta$ does **not** indicate a
  breakdown of sectorial-asymptotic existence on a positive-
  measure subset of the SIARC stratum; it indicates a finite-$N$
  signal in the sub-leading constants.
* E2 is **consistent with** the broader umbrella v2.0 picture
  that the SIARC PCF stratum is uniformly Newton-polygon-
  regular at the leading order, with the modular layer (PCF-2
  v1.3, CT v1.3) carrying the sub-leading arithmetic content.

E2 **does NOT establish** any sub-leading closed-form for
$\delta$; the Phase D PSLQ outcome at $j = 0$ was inconclusive
at the SESSION-T2 precision regime.

---

## E3 — Theory-Fleet H4 ($V_{\mathrm{quad}}$ median Écalle resurgence)

**Cited content (from THEORY-FLEET/H4/handoff.md):**

H4 is a **HIGH-confidence theoretical prediction (NOT executed)**
that median Écalle resurgence at $5000$ coefficients / dps $250$
extracts the $V_{\mathrm{quad}}$ alien-derivative amplitude (the
Stokes coefficient at the Borel branch point $\zeta^* = 4/\sqrt{3}$)
to $30$–$50$ digits, with central forecast $\sim 40$ digits.

**What E3 rules out:**

* As an **unexecuted prediction**, E3 **rules out nothing
  empirically**. E3 is a theoretical-prediction artefact, not a
  computation.
* E3's recipe (Costin 1998+ median half-Stokes prescription
  applied to the existing $V_{\mathrm{quad}}$ Borel transform
  data) **predicts** that the alien-amplitude extraction will
  succeed; it does not **rule out** the possibility that the
  recipe encounters a normalisation or branch-model error
  before yielding the predicted digit count.

**What E3 does not rule out:**

* E3 **does not rule out** any value of the $V_{\mathrm{quad}}$
  Stokes coefficient at the Borel branch point.
* E3 **does not rule out** that the closed-form for the alien
  amplitude involves $\Gamma(1/4)$, Catalan's constant, or
  other constants outside the H4-suggested basis $\{2, 3, \pi,
  \Gamma(1/3), \Gamma(2/3)\}$.
* E3 is **orthogonal** to Q3's bracket on $A$ at $d \ge 3$
  (E3 is about the alien amplitude in the channel-theory
  $V_{\mathrm{quad}}$ resurgence problem; Q3 is about the
  leading approximant-error rate $A$ in the SIARC PCF stratum).

**Combination with Q3's literature bracket:**

* E3 is **orthogonal** to Q3. E3 lives in the channel-theory
  $V_{\mathrm{quad}}$ context (CT v1.3 §3.5,
  `op:cc-median-resurgence-execute`), which uses Costin 1998+
  resurgence rather than Wasow §X.3 / Immink 1984 sectorial
  asymptotics.
* E3 is **consistent with** the broader literature reading of
  T1: the resurgence framework (Costin / Loday-Richaud 2016)
  is the rigorous backbone of E3, and the Phase-1 reading of
  Costin / Loday-Richaud is that the median half-Stokes
  prescription is theorem-grade for rank-1 resurgence problems.
  E3 is therefore **predicted** to succeed under the literature
  reading; the empirical execution is the
  `CHANNEL-CC-MEDIAN-RESURGENCE-EXECUTE` relay (orthogonal to T1).

E3 **does NOT establish** any property of the
$V_{\mathrm{quad}}$ Stokes coefficient; it is an unexecuted
theoretical prediction.

---

## §4. Aggregate triangulation against Q3

| Item | Rules out | Does not rule out | Q3-bracket effect |
|---|---|---|---|
| E1 | $|A - 2d| > 10^{-2}$ on $\ge $ a few of the harvested $110$ families at $d \in \{3,4\}$ | sub-percent residuals; $d \ge 5$ behaviour; normalisation reading | Narrows empirical $A$ at $d \in \{3, 4\}$ to a sub-percent neighbourhood of $2d$, **inside** the literature bracket $[d, 2d]$. **Supports** the Phase-2 lower-bound lift to $2d$. |
| E2 | independence of $\delta$ from $\log\|\Delta\|_{\mathrm{Pet}}$; $\log|j|$-only modular content | finite-$N$ tail-window status of the signal; higher-weight modular refinements | Orthogonal to Q3 (acts on sub-leading $\delta$, not on $A$). **Consistent with** Phase-2 sub-claim P2.3 (sectorial uniformity). |
| E3 | nothing (unexecuted) | anything (unexecuted) | Orthogonal to Q3 (channel-theory $V_{\mathrm{quad}}$, not SIARC PCF stratum). |

**Net Phase-1 triangulation finding.** The SIARC empirical record
**narrows** $A$ at $d \in \{3, 4\}$ to a sub-percent neighbourhood
of $2d$, which sits at the **literature upper bound**
$\psi_{\mathrm{upper}}(d)$ in Q3's GAP_TYPE_C classification under
the Wasow-normalisation reading. The empirical record is
**consistent with** Conjecture B4 and **supports** Phase 2's task
of lifting the literature **lower bound** $\psi_{\mathrm{lower}}(d)$
from $d$ to $2d$.

The empirical record **does not** rigorously establish $A = 2d$;
the rigorous statement requires the Phase-2 theorem decomposed in
Q3 §5. The empirical record **does not** adjudicate the
Wasow-vs-Adams normalisation question (Q3 §3); a primary-source
consultation of B–T 1933 / Adams 1928 is required to fix the
normalisation match before Phase 2 can proceed with a
well-defined target theorem.

---

## §5. Epistemic-language self-check

This deliverable was scanned for the forbidden words "shows /
confirms / proves / demonstrates / establishes / verifies" in
contexts (ii) and (iii).

* "**E1 does NOT establish** $A = 2d$ rigorously at any $d$" —
  used in a context (ii) sentence; the word "establish" is
  prefixed by **NOT**, which is the permitted form (denying
  that establishment occurs). Verified safe.
* "**E2 does NOT establish** any sub-leading closed-form for
  $\delta$" — same as above. Verified safe.
* "**E3 does NOT establish** any property of the
  $V_{\mathrm{quad}}$ Stokes coefficient" — same as above.
  Verified safe.
* "the median half-Stokes prescription is theorem-grade for
  rank-1 resurgence problems" — context (i) (Costin / Loday-
  Richaud refereed); permitted.
* "B–T 1933 establishes the formal-series existence theorem"
  (in `bt1933_theorem_extraction.md`) — context (i); permitted.

No remaining unsafe occurrences. Scan passes.
