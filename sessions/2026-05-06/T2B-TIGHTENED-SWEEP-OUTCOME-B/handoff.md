# Handoff — T2B-TIGHTENED-SWEEP-OUTCOME-B
**Date:** 2026-05-06
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes (script wall: 20.9 s; total session incl. dedup-fix iteration ~30 min)
**Status:** COMPLETE
**Outcome tag:** **`B-T-A`** (zero new off-orbit n/log(2) hits)
**Relay prompt:** 044B (revised 2026-05-06 post-044R verdict)
**Anchor 044R commit:** `fe15737`
**Source 044R unexpected_finds.json SHA-256:**
`74813228c0994fa8dabb5ba4ec79c9fd91646ec145cafd1da32467aed9048a23`
**Sweep script SHA-256:**
`c0b9df78d803623f924bda8e845d484ac09595593e2254178c6341885a5ecdc2`

---

## What was accomplished

044B operationalised the structural-coincidence question raised by the
044R verdict (b7 singular at ratio 8/49 and b10 044R outlier at ratio
−9/100 both yielding $L = 3/\log 2$). Three components were executed:

* **STEP 2A — sign-orbit closure** of the 044R hit. All 8 tuples
  $(a_2, a_1, a_0, b_1, b_0) = (\pm 9, 0, 0, \pm 10, \pm 5)$ evaluated
  at dps=300 with PSLQ at $h \le 10^9$.
* **STEP 2B — Bauer-shape family sweep** of $(a_2, a_1, a_0) =
  (-k^2, 0, 0)$ for $k \in \{1, 2, 3, 4, 5\}$ at $b_1 \in
  \pm B(k) \setminus \{\pm 6k\}$, $b_0 \in [-7, 7]$ (1 620 tuples;
  Stage A K_500 → 1 058 convergent → Stage B PSLQ dps=150 $h \le 10^7$
  → Stage D deep-verify dps=300 $h \le 10^9$ on Log/Trans hits).
* **STEP 2C / P5 — b7 singular re-verify** at dps=300 (re-confirmed
  $L = 3/\log 2$ exactly; relation `[-3, 0, 0, 0, 0, 0, 0, 1]`).

After dedup against the sign-orbit closure of the two known anchors,
**zero structurally new off-orbit $n/\log(2)$ data points** were
surfaced. Outcome **B-T-A** at the bounded h-levels actually swept
($h \le 10^9$ on the 8 sign-orbit tuples, $h \le 10^7$ on the
Bauer-shape family).

## Key numerical findings

* **P5 b7 re-verify** *(dps=300, t2b_tightened_sweep.py)*:
  $L_{b7} = 4.32808512266689022207977404300567641227993786245895780240635$;
  $|L_{b7} - 3/\log 2| = 0$ exactly to dps=300; PSLQ relation
  `[-3, 0, 0, 0, 0, 0, 0, 1]` $\Rightarrow$ $L = 3/\log 2$, $n=3$.
* **STEP 2A sign-orbit** *(dps=300, t2b_tightened_sweep.py)*:
  2 of 8 tuples are off-orbit $n/\log(2)$ — $(-9,0,0,10,5)$ with
  $n=+3$ (the 044R anchor itself) and $(-9,0,0,-10,-5)$ with
  $n=-3$ (the $L \to -L$ sign-symmetric mirror). The other 6 tuples
  classify as Desert. All 8 are: not on the Bauer-1872 orbit, not on
  the Brouncker-boundary $4a_2 - b_1^2 = 0$, not on the Trans-stratum-
  proper $9 a_2 + 2 b_1^2 = 0$ (all `disc=neither`).
* **STEP 2B Bauer-shape family** *(dps=150 → 300, t2b_tightened_sweep.py)*:
  enumeration_total = **1 620** $\to$ Stage A convergent **1 058**
  $\to$ Stage B Log = **2**, Trans = **0**, Phantom = **0**
  $\to$ Stage D off-orbit = **2**. The 2 Stage D off-orbit hits are
  exactly $(-9,0,0,10,5)$ and $(-9,0,0,-10,-5)$ — both already in
  the b10 044R sign-orbit closure (the Bauer-shape parameterization
  with $k=3$ contains $b_1 \in \{\pm 10\}$ and $b_0 \in [-7,7]$).
* **Dedup partition**:
  raw_hit_records = 4, deduped_unique_tuples = 2,
  known_anchor_orbit (b10 044R) = 2, **new_off_orbit = 0**.
* **Ratio-pattern fit** *(STEP 3, 2 anchors only)*:
  linear $\phi(b_1) = -1241 b_1 / 14\,700 + 11\,087 / 14\,700$ passes
  through both anchors with residual 0; integer-relation
  $3 a_2 + 17 b_1 - 143 = 0$ also passes through both ($24+119-143 = 0$
  and $-27+170-143 = 0$). NOTE: with only 2 anchor points any
  degree-1 / 2-term integer relation is identically determined; the
  fit makes no structural claim. `max_abs_denom = 143 > 30`, so the
  fit does NOT satisfy the prompt's "low-denominator curve" criterion.
* **n=3 anchor count**: **2** (b7 singular + b10 044R; no new hits to
  add).

## Judgment calls made

1. **Dedup against sign-orbit closure of known anchors.** First-pass
   classification yielded outcome `B-T-C` (4 raw "off-orbit" hits)
   because the prompt's STEP 2A is BY DEFINITION the sign-orbit closure
   of the b10 044R anchor, and the Bauer-shape sweep with $k=3$
   contains $b_1 = \pm 10$ as well, so the two genuine sign-orbit
   tuples appeared twice. I judged that "new off-orbit $n/\log(2)$
   hits" in STEP 4 meant **structurally** new tuples — i.e., tuples
   NOT in the sign-orbit closure of $\{$b7 singular $(8,-4,0,7,4)$,
   b10 044R $(-9,0,0,10,5)\}$ — and added a `known_anchor_class`
   classifier that excludes those. The L → −L sign-symmetric mirror
   $(-9,0,0,-10,-5)$ giving $n=-3$ is treated as the same structural
   datum as the $n=+3$ anchor. The dedup partition is preserved
   verbatim in `results.json` → `off_orbit_hits_classification` and in
   `unexpected_finds.json` for full traceability.
2. **Fit-residual gating in STEP 3.** With only 2 anchors and no new
   hits, any 2-term integer relation through them is trivially exact.
   I gated `curve_residual_le_1e_200` on (a) the fit being exact at
   all anchors, (b) `max_abs_denom <= 30`, AND (c) `n_anchors >= 3`.
   The current 044B fit has 2 anchors and `max_abs_denom = 143`, so
   the curve criterion is False — preventing a spurious B-T-C
   escalation from a meaningless 2-point fit.
3. **Sign-orbit closure definition.** I take the sign-orbit of
   $(a_2, a_1, a_0, b_1, b_0)$ to be $\{(\pm a_2, \pm a_1, \pm a_0,
   \pm b_1, \pm b_0) : \text{numerator and denominator signs flip
   together}\}$. This is consistent with the prompt's STEP 2A wording
   ("sign-orbit of (b1,b0) plus sign-flips of a2 on the a1=a0=0
   axis"). For the b7 singular this means $\{(\pm 8, \mp 4, 0,
   \pm 7, \pm 4)\}$ (numerator coefficients flip together).

## Anomalies and open questions

* **The integer relation $3 a_2 + 17 b_1 - 143 = 0$** is exact through
  the two known anchors but `max_abs_denom = 143` exceeds the
  prompt's "denominator $\le 30$" threshold and the fit is
  underdetermined with only 2 points. This is NOT a structural curve;
  it is a numerical curiosity. T1 Synthesizer arbitration should not
  treat it as evidence either way — the proper next step is more
  anchors (higher $h$, broader $b_1$, or non-Bauer-shape sweeps).
* **n=3 collision unresolved.** Both known anchors yield $n=3$, but
  the present sweep adds zero new data points, so the empirical
  question raised by 044R remains open: is $n=3$ structural, or is it
  an attractor for small-coefficient PCFs? The Bauer-shape family
  k∈{1..5} at $b_1 \ne \pm 6k$, $b_0 \in [-7,7]$, $h \le 10^7$
  produces NO new $n/\log(2)$ hits; this RULES OUT the
  "Bauer-pencil-at-non-on-orbit-$b_1$" hypothesis at this bounded
  level. It does NOT rule out (i) Bauer-shape with $a_1, a_0 \ne 0$,
  (ii) larger $|a_2|$ or $|b_1|$, or (iii) higher $h$.
* **Sign-orbit asymmetry within b10 044R orbit.** Of the 4 tuples
  with $a_2 = -9$ (a Bauer-shape numerator $a_2 = -k^2$ for $k=3$),
  only 2 produce $n/\log(2)$: $(\pm 10, \pm 5)$ (signs aligned).
  The cross-sign tuples $(-9, 0, 0, \pm 10, \mp 5)$ are Desert. This
  is consistent with the Bauer-1872 sign convention but worth
  flagging — it suggests the L value depends on the sign-coupling
  of $(b_1, b_0)$, not just their magnitudes.
* **Zero hits with $a_2 = +9$** in STEP 2A. All 4 tuples with
  $a_2 = +9$ are Desert (no PSLQ relation). This is consistent with
  the Bauer-shape requirement $a_2 = -k^2$ (negative); positive $a_2$
  on the $(a_1=a_0=0)$ axis is not the Bauer-shape numerator and was
  not expected to produce hits.
* **NO structural identity claimed.** The 044B harness explicitly
  reports residuals only and disclaims structural identity in claims
  044B-A4 and 044B-A5. The questions "Is this an extension of the
  Brouncker–Stieltjes–Wallis triangle? a Bauer–Forrester pencil at
  $b_1 \ne \pm 6k$? a new family?" remain T1 Synthesizer questions.

## What would have been asked (if bidirectional)

* "Should the L → −L sign-mirror $(-9,0,0,-10,-5)$ count as a
  separate data point or as the same anchor?" — I treated it as the
  same. If the synth wants per-sign-orbit-element accounting, the
  `unexpected_finds.json` and `results.json` retain the full raw
  list for re-classification.
* "What is the intended interpretation of the Bauer-shape family
  with $a_1, a_0 \ne 0$?" — the prompt scopes 044B to
  $(a_2, a_1, a_0) = (-k^2, 0, 0)$, so I did not extend. A 044C-style
  follow-up could lift this restriction.
* "Should the b7 singular be included in the Bauer-shape sweep with
  $k$ such that $a_2 = -k^2 = 8$?" — $a_2 = 8$ is NOT $-k^2$ for any
  integer $k$, so b7 is structurally outside the Bauer-shape family
  by definition. The 044B harness correctly excludes it from STEP 2B
  enumeration.

## Recommended next step

**T1 Synthesizer arbitration on the n=3 coincidence (deferred to
W20 weekly cadence).** The 044B B-T-A outcome means PCF-2 v3.x
wording softens from "b7 singleton" to "b7 + b10 two known data
points at $h \le 10^9$ (sign-orbit + b10 044R Bauer-shape Stage B at
$h \le 10^7$)". The literature/identity question remains open and is
the right T1 question:

> Is $L = 3/\log 2$ at off-orbit PCFs (a) an extension of the
> Brouncker–Stieltjes–Wallis triangle, (b) a Bauer–Forrester pencil
> at $b_1 \ne \pm 6k$ with non-Bauer numerators (b7 has
> $(a_2, a_1) = (8, -4) \ne (-k^2, 0)$), or (c) a new structural
> family?

Concrete next computational probes (for a 044C-style P0 if the
synth recommends harden):

1. Bauer-shape with $a_1, a_0 \ne 0$: same $(a_2, a_1, a_0) =
   (-k^2, *, *)$ but allow $a_1, a_0 \in [-5, 5]$ at the
   non-on-orbit $b_1 = \pm 10$ corridor.
2. Generic-numerator sweep at $b_1 = 10$ with full $a_2 \in
   [-30, 30] \setminus \{0\}$, $a_1, a_0 \in [-5, 5]$, $b_0 \in
   [-7, 7]$, $h \le 10^9$ — the b7 analog at $b_1 = 10$.
3. $b_1$ corridor extension: $b_1 \in \{11, 13, 14, 15, 16, 17\}$
   (avoiding $\pm 6k$ and $\pm 12$, $\pm 18$).
4. Higher $h$: re-run the b10 sign-orbit at $h = 10^{10}$ and
   $h = 10^{11}$ to test bounded-evidence stability.

## Files committed

`sessions/2026-05-06/T2B-TIGHTENED-SWEEP-OUTCOME-B/`
* `t2b_tightened_sweep.py` — sweep harness (STEP 1 / P5 / STEP 2A /
  STEP 2B / STEP 3 / STEP 4 / claims builder).
* `results.json` — full per-step records incl. step2a (8 tuples),
  step2b stage_d records, dedup partition, ratio-pattern fit,
  outcome details.
* `unexpected_finds.json` — partition of off-orbit hits into
  known-anchor-orbit (2) and new (0) with dedup rationale.
* `claims.jsonl` — 8 AEAL claims (044B-A1 through 044B-A8).
* `halt_log.json` — `{}` (no halt fired).
* `discrepancy_log.json` — `{}` (no discrepancies).
* `run.log` — full stdout/stderr capture of the sweep.
* `handoff.md` — this file.

## AEAL claim count

8 entries written to `claims.jsonl` this session (044B-A1 through
044B-A8 per relay 044B STEP 5).

## Epistemic discipline check (self-audit)

* Outcome reporting carries the h-bound qualifier explicitly:
  $h \le 10^9$ for the 8 sign-orbit tuples (STEP 2A direct dps=300
  PSLQ + STEP 2B Stage D deep-verify on Log/Trans hits) and
  $h \le 10^7$ for the Bauer-shape Stage B screen. Bare "no off-orbit
  hits exist" is NOT claimed.
* Ratio-pattern fit residuals are reported (zero at both anchors);
  no claim of "exact structural curve" is made because (a) only 2
  anchors, (b) `max_abs_denom = 143 > 30`.
* Bauer-shape enumeration is restricted to $(a_2, a_1, a_0) =
  (-k^2, 0, 0)$; the prompt does NOT claim closure for
  $a_1, a_0 \ne 0$. This is repeated in claim 044B-A2 and the
  "Anomalies" section above.
* The $n=3$ collision is reported as EMPIRICAL; structural identity
  questions are explicitly handed off to T1 Synthesizer in claims
  044B-A4 and 044B-A5 and in "Recommended next step".
* No `VERDICT_OMITS_H_BOUND_QUALIFIER` violation: every outcome
  statement above includes an explicit "$h \le 10^9$" or
  "$h \le 10^7$" qualifier.
