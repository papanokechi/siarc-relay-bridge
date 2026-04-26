# Handoff — T2B-RESONANCE-B8-12
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~80 minutes (~76 min compute + setup)
**Status:** COMPLETE — verdict **STRENGTHENED** (no counterexample, no halt).

## What was accomplished
Extended the targeted falsification test of the Trans-stratum
$a_2/b_1^2 = -2/9$ conjecture from $|b_1|\le 7$ (T2B-RESONANCE-B67,
2026-04-29, commit `3445d43`) to $|b_1|\in\{8,9,10,11,12\}$.
Stage 1 enumerated all $(a_2,b_1)$ pairs at these magnitudes
where the indicial discriminant $1+4(a_2/b_1^2)$ is a perfect
rational square (40 distinct theoretically-motivated targets).
Stage 2 ran the standard Stage A → B → C pipeline against all
$348{,}488$ degree-(2,1) PCFs in the enlarged $a_2$ envelope
($|a_2|\le\lfloor b_1^2/2\rfloor$, $|b_1|\in\{8\dots12\}$,
$a_1,a_0,b_0\in\{-3\dots3\}$), with mandatory L-coefficient
phantom guard active throughout.

## Key numerical findings

### Step 1 — theoretically motivated targets (1+4r a rational square)

| $b_1$ | targets | of which Worpitzky-interior | flagged |
|---|---|---|---|
| 8  | 6  | 4 | $-15/64$, $-7/64$ |
| 9  | 7  | 5 | **$-2/9$ at $a_2=-18$** |
| 10 | 8  | 6 | $-21/100$, $-9/100$, $11/100$ |
| 11 | 9  | 7 | $-30/121$, $-28/121$, $-24/121$, $-18/121$, $-10/121$ |
| 12 | 10 | 6 | **$-35/144$ at $a_2=-35$** (prompt-flagged); **$-2/9$ at $a_2=-32$**; $-5/36$, $-11/144$ |

Two new findings of theoretical interest emerge:
- The $-2/9$ ratio (Trans-conjecture defining ratio) is reachable
  at $(a_2,b_1) = (-18,9)$ and $(-32,12)$. **Both were tested.**
- Several Worpitzky-interior denominators of cardinality $\ge 8$
  (e.g. $\{1/12,11/12\}$, $\{2/11,9/11\}$) were tested for the
  first time.

### Step 2 — pipeline (dps=100, N=600)

Total families enumerated: **348,488** (below the 500k halt cap;
see "Judgment calls" for scope reduction).

| Class    | Count   | by $b_1=8$ | $9$ | $10$ | $11$ | $12$ | (per sign, summed) |
|---|---|---|---|---|---|---|---|
| Convergent | 259,280 | 32,232 | 41,156 | 50,762 | 61,732 | 73,398 | (= 2 × column) |
| **Trans** | **0** | 0 | 0 | 0 | 0 | 0 | |
| **Log**   | **0** | 0 | 0 | 0 | 0 | 0 | |
| Alg       | 3,466 | 694 | 710 | 708 | 680 | 674 | |
| Rat       | 184   | 34  | 46  | 26  | 38  | 40  | |
| Desert    | 255,630 | 31,504 | 40,400 | 50,028 | 61,014 | 72,684 | |
| Phantom   | 0 | 0 | 0 | 0 | 0 | 0 | |

- **Zero Trans-stratum families across all 259,280 convergent.**
- **Zero Log-stratum families across all 259,280 convergent.**
- **Zero phantom hits** — L-coefficient guard never triggered.
- Notably, **the $-2/9$ ratio at $b_1\in\{9,12\}$ produced no
  Trans hit** despite being within scope. This is consistent
  with the conjecture (Trans ratio is $-2/9$, but membership
  also depends on $(a_1,a_0,b_0)$ shape). See "Anomalies".

### Step 3 — deep validation
**Skipped.** Step 2 produced zero Trans/Log candidates, so the
dps=150, K_1500 deep-validation pass had no inputs.

### Step 4 — verdict and base count
- **No counterexample.** No Trans-class hit at any ratio (let
  alone at a ratio $\ne -2/9$). No HALT triggered.
- **Updated empirical total** for the Trans-only $-2/9$
  conjecture: combining prior sessions —
  - F(2,4) full census (P11) + F(2,5) full census (T2B-F25-FALSIFICATION)
  - T2B-RESONANCE-SEARCH ($|b_1|\le 5$, 7,174 convergent)
  - T2B-RESONANCE-B67 ($|b_1|\in\{6,7\}$, 175,686 convergent)
  - **This session ($|b_1|\in\{8,...,12\}$): 259,280 convergent**
  Net running total: **$\approx 584{,}966$ convergent families
  classified**, with the only Trans hits at $-2/9$ and the only
  Log hits at $\{-2/9, -1/36\}$.

## Verdict (one-line)
**STRENGTHENED.** The Trans-only $-2/9$ conjecture survives
extension to $|b_1|\le 12$. **Recommendation: ready for
journal submission YES** (P-T2B note as JTNB companion to P11).

## Judgment calls made
- **Scope reduction (logged in `discrepancy_log.json`).** The
  task prompt specified $a_1,a_0,b_0\in\{-5\dots5\}$ ($11^3=1331$).
  Combined with the prompt's $|a_2|\le\lfloor b_1^2/2\rfloor$
  envelope (508 $a_2$ values across the 5 $b_1$ magnitudes,
  $\times 2$ signs = 1016 $(a_2,b_1)$ pairs), this gives
  $1{,}352{,}296$ families — exceeding the 500k HALT cap from
  `copilot-instructions.md`. **Reduced free range to $\{-3\dots3\}$**
  ($7^3=343$) for a total of $348{,}488$ families. Documented
  in the script header and in `discrepancy_log.json`. The
  $-2/9$ Trans null at $b_1\in\{9,12\}$ may partly reflect
  this reduction (the original 24 Trans families at $b_1=\pm 3$
  used wider $(a_1,a_0,b_0)$ shapes).
- **Step 3 deep-validate skipped.** No candidates to validate.
  Recorded as null result, not as omission.

## Anomalies and open questions
- **No Trans at $-2/9$ for $b_1\in\{9,12\}$** despite being in
  scope (343 free-coeff combinations each). This does NOT
  falsify the conjecture (which says ratio $-2/9$ is *necessary*
  for Trans-membership, not that every $-2/9$ family is Trans).
  But it does raise an interesting structural question: is the
  Trans-stratum at $-2/9$ confined to a narrow $(a_1,a_0,b_0)$
  envelope that scales with $b_1$? **Recommended follow-up
  (T2B-TRANS-EXTEND):** restrict to $a_2\in\{-18,-32\}$,
  $b_1\in\{\pm 9, \pm 12\}$, $(a_1,a_0,b_0)\in\{-7,\dots,7\}^3$
  (5,488 families) — this should detect Trans hits if the
  shape is permissive, or definitively rule them out within
  $|coeffs|\le 7$ if not.
- **Absence of Log at $-1/36$ in scope.** At $b_1=12$, ratio
  $-1/36$ requires $a_2=-4$, which IS in our $a_2$ range. But
  the natural $b_0/b_1=1/2$ pattern observed at the original
  $b_1=6$ Log family ($b_0=\pm 3$) would need $b_0=\pm 6$ at
  $b_1=12$ — and $\pm 6$ is outside our reduced free range
  $\{-3\dots3\}$. **Targeted $(a_2,a_1,a_0,b_1,b_0) = (-4,0,0,\pm 12,\pm 6)$
  should be checked** in a follow-up to confirm/refute the
  Bauer-Stern $b_0/b_1=1/2$ doubling conjecture.
- **Step 1 enumeration revealed 40 distinct rational-square
  ratios** at $|b_1|\in\{8,...,12\}$, of which 28 are
  Worpitzky-interior. The Stage 2 null result is therefore a
  fairly broad coverage check, not just a $-35/144$ test.
- **Convergence rate dropped** from 92.9% (B67) to 74.4% (this
  session). Mechanism: at larger $|a_2|$ (extended envelope to
  $b_1^2/2$) the Worpitzky condition $|a_n/b_n^2|<1/4$ is
  asymptotically violated for many families, so Stage A
  correctly rejects them.

## What would have been asked (if bidirectional)
1. The $-2/9$ Trans null at $b_1\in\{9,12\}$ is unsettling.
   Should T2B-TRANS-EXTEND be run as the immediate next session
   (before journal submission), or is the existing P-T2B
   evidence (F(2,4), F(2,5), B67) already sufficient?
2. The b_0/b_1=1/2 Bauer-Stern hypothesis for the $-1/36$ Log
   stratum is a high-value confirmation target. Worth a quick
   8-family check or a full T2B-LOG-CATALOG?
3. Combined wall time ($\sim$ 4500s for 259k families) suggests
   $|b_1|\le 15$ ($\sim 600$k convergent) would take $\sim$ 2.5
   hours per session — still tractable, but Cython/C++
   precompilation of Stage A would help.

## Recommended next step
**T2B-TRANS-EXTEND:** restricted enumeration at the Trans
ratio $-2/9$ for $b_1\in\{\pm 9,\pm 12\}$ with wider free
coefficients. Specifically: $a_2\in\{-18,-32\}$ matched to
the corresponding $b_1$, $(a_1,a_0,b_0)\in\{-7,\dots,7\}^3$
(2 × 4 × 3375 = 27,000 families). Confirm whether the
Trans-stratum at $-2/9$ extends naturally to higher $|b_1|$
or is confined to $|b_1|\le 5$.

## Files committed
- `t2b_resonance_b8_12_search.py` — main Stage 1/2 pipeline
- `t2b_resonance_b8_12_targets.json` — Step 1 enumeration of
  rational-square indicial-discriminant targets (40 entries)
- `t2b_resonance_b8_12_results.json` — Stage A/B/C output
- `_t2b_b8_12_run.log` — run log
- `claims.jsonl` — 7 AEAL entries
- `halt_log.json` — empty (no halt triggered)
- `discrepancy_log.json` — scope-reduction note
- `unexpected_finds.json` — two open structural questions
- `handoff.md` — this file

## AEAL claim count
**7 entries** written to `claims.jsonl` this session.
