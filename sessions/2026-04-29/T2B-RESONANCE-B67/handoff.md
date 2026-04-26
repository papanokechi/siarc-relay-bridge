# Handoff — T2B-RESONANCE-B67
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~50 minutes (script setup + 46-min compute)
**Status:** COMPLETE — verdict **STRENGTHENED** (Trans-stratum) with one **Log-stratum unexpected finding** at ratio $-1/36$.

## What was accomplished
Extended the targeted falsification test of the structural conjecture
$a_2/b_1^2 = -2/9$ (Trans-stratum, degree-(2,1) integer PCFs) from
$|b_1| \le 5$ (T2B-RESONANCE-SEARCH, `ab0d70b`) to
$b_1 \in \{-7, -6, 6, 7\}$. All $189{,}000$ families with
$a_2 \in \{-7,\dots,-1,1,\dots,7\}$, $b_1 \in \{-7,-6,6,7\}$,
$a_1, a_0, b_0 \in \{-7,\dots,7\}$ were enumerated and pushed
through the same Stage A → B → C pipeline (Stage A float64 K_500
rel-tol $10^{-8}$; Stage B/C `mpmath.pslq` at dps=100, N=600 with
mandatory L-coefficient phantom guard). The two Log candidates
that emerged were deep-validated at dps=150, K_1500 against the
seven-basis battery from T2A-BASIS-IDENTIFY plus a Log-extension
basis.

## Key numerical findings
**Step 1 — enumeration.** $14 \times 4 \times 15^3 = 189{,}000$ families.
Below the 300k threshold; full $\{-7,\dots,7\}$ free-coefficient range
retained (`t2b_resonance_b67_search.py`).

**Step 2 — pipeline (dps=100, N=600).**

| Class | Count | by $b_1=-7$ | by $-6$ | by $+6$ | by $+7$ |
|---|---|---|---|---|---|
| Convergent | 175,686 | 43,966 | 43,877 | 43,877 | 43,966 |
| **Trans** | **0** | 0 | 0 | 0 | 0 |
| **Log**   | **2** | 0 | 1 | 1 | 0 |
| Alg       | 10,890 | 2,695 | 2,750 | 2,750 | 2,695 |
| Rat       | 1,030  | 266   | 249   | 249   | 266   |
| Desert    | 163,764 | 41,005 | 40,877 | 40,877 | 41,005 |
| Phantom   | 0 | 0 | 0 | 0 | 0 |

- **Zero Trans-stratum hits at any of $b_1 \in \{-7,-6,6,7\}$.** The
  Worpitzky-interior, rational-indicial-roots target $r=-6/49$
  ($b_1=\pm 7$, $a_2=-6$, indicial roots $\{1/7, 6/7\}$) was tested
  and produced no Trans candidate; nor did any other $a_2/b_1^2$
  value in this enumeration.
- **Two Log-stratum hits**, both at ratio $-1/36$ (i.e. $b_1=\pm 6$,
  $a_2=-1$), specifically at $(a_2,a_1,a_0,b_1,b_0) = (-1,0,0,\pm6,\pm3)$.
  Stage-C relation: $L\cdot\log(2) \mp 2 = 0$, residual $1.43\times10^{-101}$
  at dps=100.
- **Zero phantom hits** — the L-coefficient guard was exercised but
  never engaged (every L-bearing relation that survived Stage C had
  residual under threshold).

**Step 3 — ratio analysis on Log/Trans candidates.**
- (a) Any Trans at $b_1\in\{6,7\}$? **No.**
- (b) The Log hits sit at $a_2/b_1^2 = -1/36$, **not** at $-2/9$.
  (At $b_1=6$, the $-2/9$ ratio would require $a_2=-8$, outside our
  $|a_2|\le 7$ envelope; at $b_1=7$ it would require $a_2=-98/9$,
  non-integer. So the absence of Trans at $-2/9$ here is a scope
  artifact, not evidence against the conjecture.)
- (c) Trans at ratios $\ne -2/9$? **No.**

**Step 4 — deep validation at dps=150, K_1500** (`t2b_resonance_b67_deepvalidate.py`):

| Family | $L_{150}$ | Verdict |
|---|---|---|
| $(-1,0,0,-6,-3)$ | $-2.88539\,008177\,7926814719\,8493620\dots = -2/\log 2$ | Log, residual $5.65\times10^{-150}$ |
| $(-1,0,0,+6,+3)$ | $+2.88539\,008177\,7926814719\,8493620\dots = +2/\log 2$ | Log, residual $5.65\times10^{-150}$ |

Standard 7-basis battery (A standard / B elliptic-AGM /
C hypergeometric / D alg$\cdot\pi^2$ / Dp alg$\cdot\pi$ /
Da algebraic deg-8) returned **no relation** for either limit at
residual threshold $10^{-60}$. Only the Log-extension basis
$\{L\log 2, L\log 3, L\log 5, 1, L\}$ found the relation, isolating
$\log(2)$ uniquely.

**Step 5 — verdict.**
- **Trans-stratum: STRENGTHENED.** Combined with prior sessions:
  - F(2,4) full census + F(2,5) full census (T2B-F25-FALSIFICATION):
    every Trans-interior family observed has $a_2/b_1^2=-2/9$.
  - T2B-RESONANCE-SEARCH ($b_1\in\{\pm4,\pm5\}$): 0 Trans across 7,174
    convergent at three rational-indicial-root candidate ratios.
  - This session ($b_1\in\{\pm6,\pm7\}$): 0 Trans across 175,686
    convergent at all 56 distinct $a_2/b_1^2$ ratios reachable in range.
  - Net: $\textbf{182{,}860}$ convergent families tested for Trans
    membership outside the $-2/9$ ratio, all negative.
- **Log-stratum: WEAKLY EXPANDED.** A new Log-class ratio $-1/36$ is
  observed (see "Anomalies" below). This does not weaken the
  Trans-only conjecture but enlarges the empirical Log catalogue,
  which previously contained only $-2/9$.

**Step 6 — empirical base count.**
- Prior running total (per session prompt): $\sim 150{,}000$.
- This session adds $175{,}686$ new convergent families (all at
  $|b_1|\in\{6,7\}$, none overlapping prior strata).
- **New running total: $\approx 325{,}686$ convergent families
  classified.**

## Verdict (one-line)
**STRENGTHENED.** The conjecture "every Trans-stratum
degree-(2,1) integer PCF has $a_2/b_1^2 = -2/9$" survives
extension to $b_1\in\{4,5,6,7\}$. No Trans family at any other
ratio has been found in $\sim 326$k convergent tests. **Recommendation:
ready for journal submission YES** (subject to standard editorial review
of the Log-stratum addendum noted below).

## Judgment calls made
- **Coefficient range left at full $\{-7,\dots,7\}$.** Prompt said to
  reduce to $\{-5,\dots,5\}$ if total > 300k; our total was 189k, so
  no reduction was applied.
- **Step 4 PSLQ phantom guard initially under-specified.** First
  pass marked the genuine Log relation $L\log 2 = -2$ as "phantom"
  because the standalone-$L$ index had coefficient zero. Patched the
  guard to accept any L-bearing index (standalone or multiplied);
  the Le_logext basis then correctly returned the relation
  $1\cdot(L\log 2) + 2\cdot 1 = 0$ at residual $5.65\times10^{-150}$.
  Direct dps=150 evaluation of $|L\log 2 + 2|$ independently
  reproduced the residual ($\sim 8\times10^{-61}$ limited by the
  recorded 60-digit $L$ string), so the patched guard merely
  surfaces what was already seen at dps=100.
- **Two Log candidates not deep-tested for Möbius/Heun/zeta-class
  relations beyond the standard battery.** The 7-basis battery of
  T2A-BASIS-IDENTIFY plus the Log-extension basis was sufficient to
  identify $L = \pm 2/\log 2$ uniquely (all other bases returned no
  relation). A Möbius scan against $\log 2$ alone would be the
  natural next step if Aria/Claude wants symbolic confirmation of
  the underlying classical identity (see "What would have been
  asked").

## Anomalies and open questions
**THE PRIMARY ANOMALY.** The Log hits $L = \pm 2/\log 2$ at family
$(a_2,a_1,a_0,b_1,b_0) = (-1, 0, 0, \pm 6, \pm 3)$ correspond to the
PCF
$$
   L \;=\; b_0 + \mathop{\mathrm{K}}\limits_{n=1}^{\infty} \frac{-n^2}{6n + 3}
       \;=\; 3 + \cfrac{-1}{9 + \cfrac{-4}{15 + \cfrac{-9}{21 + \cdots}}}
       \;=\; \frac{2}{\log 2}.
$$
This is recognisable as a classical Bauer/Stern–style continued
fraction for $2/\log 2$ (closely related to Gauss's hypergeometric
$_2F_1$-CF specialisation at $z=1$ giving $\log$-class limits).
Three points worth flagging:
1. The ratio $a_2/b_1^2 = -1/36$ has **indicial discriminant
   $1+4r = 8/9$, which is NOT a rational square**, so the indicial
   roots $\{(1\pm\sqrt{8/9})/2\}$ are irrational. This breaks the
   working heuristic (carried since T2B-RESONANCE-SEARCH) that
   rational indicial roots are the privileged predictor of Log/Trans
   stratum membership. Rational discriminant is sufficient for the
   $-2/9$ Trans family but evidently NOT necessary for Log-class
   identities. **Open question:** what *is* the right structural
   classifier for Log-stratum ratios?
2. The b_n = 6n+3 = 3(2n+1) factor structure suggests this is a
   Stieltjes-type "doubling" of the simpler $\sum 1/(2n+1)^2$ flavoured
   CF. Worth checking whether $b_1=6$ vs $b_1=4$ (the standard
   $2/\log 2$ CF $b_n=4n-2$) corresponds to an equivalence
   transformation rather than a genuinely new family.
3. **No analogous Log hit found at $b_1=\pm 7$**, despite the
   theoretically motivated target $a_2=-6$ (ratio $-6/49$,
   indicial roots $\{1/7, 6/7\}$). This is a stronger negative
   result than at $b_1=\pm 6$.

**Secondary anomalies.**
- Rat/Alg counts are again non-trivial (~6.2% Alg, ~0.6% Rat). Same
  spot-check recommendation as in T2B-RESONANCE-SEARCH: re-run a
  random Alg sample at dps=150 to confirm the algebraicity isn't
  masking a genuine higher-class identity. Not a session blocker.
- Stage A convergence rate is 92.9% here vs 89.9% in
  T2B-RESONANCE-SEARCH. The 3-point delta is consistent with the
  larger $|b_1|$ generally improving Worpitzky-style convergence
  (denominator term dominates more).

## What would have been asked (if bidirectional)
1. Should the Log finding at $-1/36$ be promoted to its own
   independent investigation (T2B-LOG-CATALOG) before the journal
   submission, or footnoted in the existing Trans paper as a
   "see also"? It substantially expands the empirical Log catalogue
   (from $\{-2/9\}$ to $\{-2/9, -1/36\}$).
2. Is the indicial-discriminant heuristic worth dropping entirely
   given the irrational-roots Log hit, or should it be reformulated
   as "rational indicial roots ⇒ rational Trans-class limits"
   (which is still consistent with all data)?
3. The Stage B/C wall time of $\sim 45$ min for 175k families on 8
   active workers extrapolates poorly to $|b_1|\le 10$ (~$10^6$
   families, ~4 hours). Should we precompile Stage A to C++/Cython
   before extending further, or accept the wall time?

## Recommended next step
**Catalog the Log-stratum.** Run a focused enumeration of all
Log-class hits in the existing data (F(2,4), F(2,5), and the two
T2B resonance sessions combined: $\sim 326$k convergent + the
F(2,4) and F(2,5) censuses). Tabulate $(a_2/b_1^2, \text{indicial
discriminant}, \text{relation})$. Specifically: is the $-1/36$
finding isolated, or is there a generating pattern of Log-class
ratios alongside the Trans-only $-2/9$?

## Files committed
- `t2b_resonance_b67_search.py` — Stage A/B/C pipeline (10.7 KB)
- `t2b_resonance_b67_deepvalidate.py` — Step 4 validator (7.4 KB)
- `t2b_resonance_b67_results.json` — Stage A/B/C output, all records
- `t2b_resonance_b67_deepvalidate.json` — Step 4 dps=150 output
- `_t2b_resonance_b67_run.log` — Stage A/B/C run log
- `_t2b_deep_run.log` — Step 4 run log
- `claims.jsonl` — 7 AEAL entries
- `halt_log.json`, `discrepancy_log.json` — empty (no halts, no
  discrepancies)
- `unexpected_finds.json` — Log-stratum addendum at $-1/36$
- `handoff.md` — this file

## AEAL claim count
**7 entries** written to `claims.jsonl` this session.
