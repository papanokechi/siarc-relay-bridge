# Handoff — UMB-CROSSDEG-29
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE (with scope correction; HALT condition not triggered)

## What was accomplished

Computed leading and sub-leading ratios $R_1 = a_4 / b_2^2$ and
$R_2 = a_2 / b_1^2$ for all 108,762 Trans-candidates of the existing
T2A CMAX=2 deg-(4,2) census. Generated histogram, concentration table,
and PSLQ-validated the three minimum-norm representatives at the most
populated $R_1$ values (dps=300, $K=2500$). Wrote symbolic indicial
table for $d \in \{2, 4, 6\}$ distinguishing the BT and Frobenius
polynomials, and produced a closed-form catalogue of "magic" ratios
predicting both $-2/9$ (Class A) and $+1/4$ (Class B) — but as **two
distinct families**, not one.

## Key numerical findings

- T2A CMAX=2 Trans-candidate **distinct $R_1$ values: only 4**
  $\{1/4, 1/2, 1, 2\}$, all positive (`crossdeg_ratios.py`,
  dps=0/exact rationals).
- $R_1 = -2/9$ has **0 hits** in the census because $|b_2| \le 2$
  forces $b_2^2 \in \{1,4\}$; **the prompt's target ratio is
  out-of-lattice in CMAX=2** (`crossdeg_ratios.py`).
- Top-3 $R_1$ concentrations (`pslq_validate.py`, dps=300, $K=2500$):
  - $R_1 = 1/4$ (26,622 families): rep $a=[1,0,0,0,0]$, $b=[-2,0,0]$,
    $L = -4.05723373\dots$, **NO PSLQ relation** vs $\{1, \pi, \pi^2, \log 2, \log \pi\}$ at hmax $=10^{12}$.
  - $R_1 = 1/2$ (27,822 families): rep $a=[2,0,0,0,0]$, $b=[-2,0,0]$,
    $L = -1.14342651\dots$, **NO PSLQ relation**.
  - $R_1 = 2$ (27,770 families): rep $a=[2,0,0,0,0]$, $b=[-1,0,0]$,
    $L = -0.53339518\dots$, **NO PSLQ relation**.
  All three rel_spread $< 5\times 10^{-301}$.
- Symbolic indicial polynomials for $d \in \{2,4,6\}$ are formally
  identical: BT $t^2 - t - \rho_d$, Frobenius $r^2 - r + \rho_d$.
  Dimension enters only through $\rho_d = a_d/b_{d/2}^2$
  (`indicial_symbolic.py`).
- Closed-form magic-rho catalogue (`indicial_table.json`):
  - **Class A** (BT rational sum-1): $\rho = -m(b-m)/b^2$, roots
    $\{m/b, (b-m)/b\}$. Includes $-2/9$ (b=3,m=1), $-2/25$ (b=5,m=2),
    $-12/49$ (b=7,m=3), …, 18 entries at $b \le 12$.
  - **Class B** (Frobenius double root): single point $\rho = +1/4$,
    $\Delta_F = 0$, $r = 1/2$ (matches Lean Thm66_ApparentSingularity).

## Judgment calls made

- **Skipped a fresh CMAX>=3 enumeration.** The prompt assumes the
  existing T2A CMAX=2 census suffices ("INPUT: existing T2A CMAX=2
  census"); rather than launch a multi-hour enumeration, I worked the
  data we have and documented the lattice limitation explicitly.
  Recommended next step (below) is the proper CMAX>=3 sweep.
- **Used minimum-coefficient-norm representatives** (`coeffs_norm`)
  for PSLQ, breaking ties by $|a_4|$. 26k+ families share each $R_1$;
  no single "canonical limit" exists per concentration. The reps I
  picked happen to have most subleading coefficients zero, hence are
  the cleanest test of pure-leading-ratio Trans behaviour.
- **Phantom guard:** required nonzero coefficient on the $L$-bearing
  index in PSLQ output (per project convention from
  T2B-LOG-MINUS-ONE-36 / forensic.py). No phantom hits to reject.
- **Two-class universality framing:** The prompt suggested ratios
  $\{-2/9, +1/4, \ldots\}$ might be a single family. I verified they
  are not — they obey two different indicial criteria (BT vs
  Frobenius). This is the key intellectual decision; reported as
  "partial universality" rather than triggering HALT.

## Anomalies and open questions

- **All Trans-candidate $R_1$ values are positive.** Negatives
  $\{-1/4, -1/2, -1, -2\}$ have **zero** Trans hits despite being
  on-lattice. The 16,422 missing Trans of "expected" symmetry are all
  classified Rat/Alg/Desert. Is negative-$R_1$ desert a structural
  fact at deg-(4,2), or a CMAX=2 artifact? Cannot resolve without
  CMAX>=3.
- **Class B $R_1 = +1/4$ is heavily populated (26,622 / 108,762
  Trans-candidates, ~24.5%) but UMB-CLASSB-SATURATION (today) found
  the Class B stratum NOT-SATURATED.** Five deep-validated candidates
  with Brouncker shape resisted all $\mathbb{Q}(\pi)_{deg \le 6}$
  reductions. This re-confirms here: even the simplest rep at
  $R_1 = 1/4$ shows no PSLQ relation in the small named-constant
  basis.
- **Cross-degree resonance NOT verified at $-2/9$.** The whole point
  of the probe is unanswerable from the available census.
- **Subleading $R_2 = -1/36$ (T2B Log family) is on-lattice
  (b1=6 exists in the census) but with $a_2 \in \{-2,..,-1,1,..,2\}$
  we'd need $b_1^2 / |a_2| = 36$, so $b_1^2 \in \{36, 72, 108, 144\}$
  — only $b_1 = \pm 6$ works at $a_2 = \pm 1$. CMAX=2 forces
  $|b_1| \le 2$, so $b_1 = \pm 6$ is also out-of-lattice. The
  $R_2 = -1/36$ count in our census is consequently 0.**
- **HALT not triggered:** Step 4 produced TWO closed forms (Class A
  infinite family + Class B isolated), not a single unifying family.
  Whether Claude considers this enough for UMB OP-7 escalation is
  the strategic call.

## What would have been asked (if bidirectional)

- "Should I launch a CMAX>=3 enumeration now (estimated 4–8 hours;
  ~2–4M new families) since the existing census provably cannot
  answer the prompt?"
- "Is 'dimension-independent partial universality' (two classes,
  each independent of d) the intended UMB OP-7, or do you require
  a single unifying invariant?"
- "Should the negative-$R_1$ Trans desert be probed with a separate
  symmetry-breaking experiment (e.g., $a \to -a$ doesn't preserve
  Trans classification at deg-4)?"

## Recommended next step

**UMB-CROSSDEG-29-CMAX3:** targeted CMAX=3 deg-(4,2) sweep on the
slice $b_2 \in \{\pm 3\}$, $a_4 \in \{\pm 1, \pm 2, \pm 3\}$,
$(a_3, a_2, a_1, a_0, b_1, b_0) \in [-3, 3]^6$. Approximately
$6 \cdot 6 \cdot 7^6 \approx 4.2 \cdot 10^6$ families. Stage A
float64 + Stage B/C PSLQ as in T2A CMAX=2. Look for Trans hits at
$R_1 = -2/9$ (i.e., $a_4 = -2, b_2 = \pm 3$). If any survive, deep-
validate at dps=300 and PSLQ against $\{1, \pi, \pi^2, \log 2,
\log \pi, G, \zeta(3)\}$ plus the existing T2B $-2/9$ Trans constant
(check whether the deg-(4,2) and deg-(2,1) Trans constants at $-2/9$
are equal or merely cousins).

## Files committed

```
sessions/2026-04-30/UMB-CROSSDEG-29/
  crossdeg_ratios.py
  pslq_validate.py
  indicial_symbolic.py
  ratios.jsonl
  concentration_table.json
  ratio_histogram_T2A.png
  top3_picks.json
  pslq_top3_validate.json
  indicial_table.json
  indicial_table.md
  step1_run.log
  step3_run.log
  step4_run.log
  claims.jsonl
  halt_log.json
  discrepancy_log.json
  unexpected_finds.json
  handoff.md
```

## AEAL claim count

7 entries written to `claims.jsonl` this session.
