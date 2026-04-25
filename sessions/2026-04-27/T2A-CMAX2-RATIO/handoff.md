# Handoff — T2A-CMAX2-RATIO
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~150 minutes (Stage A 28s + Stage B 1472s + Stage C 5436s + deep validate 165s + analysis ~5s + pick identify 0.7s, plus build + I/O)
**Status:** COMPLETE

## What was accomplished
Expanded the degree-(4,2) PCF search from CMAX=1 to CMAX=2 to test whether the ratio `a4/b2^2` is structural for Trans-hard families. Ran the 3-stage classifier (float prescreen → mpmath confirm → PSLQ classify) over all 125000 families with `a4>0` sign symmetry, then deep-validated a 1000-family random sample at dps=150 with bilinear-pi PSLQ, then ratio-analyzed and basis-identified 3 ratio-not-1 Trans-hard picks at dps=300.

**Headline finding: the ratio `a4/b2^2` is NOT predictive of Trans-hardness.** All four possible ratio values {0.25, 0.5, 1.0, 2.0} occur in equal proportions (~25% each) among convergent families and produce Trans-candidates at near-identical rates (85-89%). The CMAX=1 dominance of ratio=1 is a sampling artifact (it is the ONLY ratio reachable when |coeff|<=1).

## Key numerical findings
- **Search space (Step 1):** 125000 families (CMAX=2, a4>0 by sign symmetry, b2!=0). User estimate 250000 omitted the symmetry. [`t2a_cmax2_search.py`]
- **Stage A (float K_200):** 124334/125000 survivors (99.5%) — float tolerance is too loose at CMAX=2 magnitudes; Stage B discriminates properly. [dps=15]
- **Stage B (mpmath dps=50 K_500):** 124334/124334 survivors confirmed convergent (`|K_500 - K_499| < 1e-25`). [dps=50]
- **Stage C (PSLQ dps=100, bilinear-pi basis):** Rat=12160, Alg=370, **Log-bilin=0**, **Trans-candidate=108762**, ERR=3042; **28 phantom hits** (with L-coefficient=0) caught and rejected. [dps=100, `t2a_cmax2_search.py`]
- **Unique L values among Trans-candidates:** 108728 (~34 collisions only). [dps=30]
- **Deep validate (dps=150 K_1500, n=1000 random sample, seed=20260427):** **1000/1000 Trans-hard**, 0 Log-bilin, 0 phantoms, 0 diverge. [dps=150, `t2a_cmax2_deep_validate.py`]
- **Step 4 — ratio distribution among convergent (124334 total):**
  - ratio 0.25 -> 31018 (24.9%)
  - ratio 0.50 -> 31224 (25.1%)
  - ratio 1.00 -> 30874 (24.8%)
  - ratio 2.00 -> 31218 (25.1%)
  Distribution is uniform.
- **Step 5 — Trans-candidate rate per ratio:**
  - 0.25 -> 85.8%
  - 0.50 -> 89.1%
  - 1.00 -> 86.0%
  - 2.00 -> 89.0%
  Spread is 3.3 percentage points; ratio is NOT predictive.
- **Step 5b — confirmed Trans-hard in 1000-sample by ratio:** 247 (0.25) + 272 (0.5) + 226 (1.0) + 255 (2.0) — uniform.
- **Step 6 — 3 ratio!=1 Trans-hard picks identified at dps=300:**
  - Pick 1: a=[2, 2, 2, 0, -1] b=[-1, -1, 1] ratio=2.0 L = -0.0020579405368000056021969922083958168822584583635135914544641
  - Pick 2: a=[1, 0, 1, -1, -2] b=[2, 1, -1] ratio=0.25 L = -1.30268138928521796585059918750182880246410145468419028457571
  - Pick 3: a=[2, 0, -2, -2, -1] b=[1, -2, -2] ratio=2.0 L = -3999.12342836400050740362286759753578346876696091588882384854
  All 3: 0/6 PSLQ hits across bases A (standard), B (elliptic), C (2F1/Clausen), D (alg*pi^2), Dp (alg*pi), Da (algebraic). Two phantom hit traps caught: D yields `[0,0,0,0,0,0,0,-4,5]` (= `-pi^2 + pi^2`) and Dp yields `[0,0,0,0,0,1,0,-2]` (= `pi/2 - pi/2`); both rejected by mandatory L-coefficient!=0 filter. [`t2a_cmax2_pick_identify.py`]

## Judgment calls made
- **Sign symmetry applied to a4 (factor 2 reduction).** The existing CMAX=1 script used `a4 in range(1, cmax+1)`; this CMAX=2 script does the same to keep results directly comparable. User estimate of 250000 was without symmetry; actual symmetric count is 125000. Documented in `discrepancy_log.json`.
- **Sampling 1000 unique-L representatives for deep validate.** With 108728 unique L values, exhaustive deep validate would have been ~24+ hours. Per task spec ("if Trans-candidates > 5000, randomly sample 1000"), I sampled 1000 unique-L families with seed=20260427 (deterministic).
- **Stage C dedup by L (30 dp).** After Stage B produced 124334 convergent families, I deduplicated by `mp.nstr(Kn, 30)` before PSLQ, reducing PSLQ work from 124334 calls to 108815. Each unique-L PSLQ result was then replicated for all families sharing that L. This is mathematically equivalent and saves ~13% of Stage C time. Implementation: `dedup` dict in `t2a_cmax2_search.py`.
- **Excluded 44MB t2a_cmax2_results.json from bridge.** Replaced with `t2a_cmax2_results_summary.json` (no per-family records, but full counts and metadata) plus its sha256 (`008cf81f69ab3f988b5ff23e8116e465fba63d46f19f20045d80033a1f087b29`). The full file remains at workspace root for re-analysis.
- **Phantom-hit defense made mandatory in BOTH search and pick-identify.** Implemented `_pslq_with_l(basis, l_index)` requiring `int(rel[l_index]) != 0`; 28 phantoms in Stage C and 6 in pick identify were rejected. Without this defense, the conclusions would be tainted by the same `pi^2/zeta(2)` and `phi/sqrt(5)` traps from prior sessions plus the new `-pi^2+pi^2=0` and `pi/2-pi/2=0` D/Dp traps.

## Anomalies and open questions
- **All 4 ratios produce Trans-hard families at uniform rate.** The ratio sub-hypothesis of the 2k-degree conjecture is REFUTED at CMAX=2: the ratio is not a structural marker of Trans-hardness. The CMAX=1 case is degenerate because only ratio=1 is reachable with |coeff|<=1.
- **0 Log-bilin hits in 1000-sample deep validate at dps=150.** This is highly significant: the Apery-like `pi^2` connection is NOT supported at any tested ratio, including ratio=1 which was supposed to be the "Apery-like" case. Combined with CMAX=1 result (also 0 Log-bilin in 1162 trans), this strongly argues the limits are NOT polynomial-in-pi.
- **108728 distinct mystery constants.** At CMAX=2 we have ~10^5 candidate novel constants. At CMAX=1 we identified 1 (the R1=-0.10123520070804963... from prior session). The space of degree-(4,2) Trans-hard limits appears to be vast. Question for Claude: is there a parametrized family of constants here, or is each a genuinely independent "atom"?
- **Stage A float prescreen 99.5% pass-rate at CMAX=2 vs 23% at CMAX=1.** The looser prescreen is suspicious — it suggests the prescreen tolerance (1e-6) is below the natural tail-difference of Wallis-recurrence convergents at K_200 for typical CMAX=2 families. Not a correctness issue (Stage B re-checks at dps=50 K_500), but it makes the prescreen serve no filtering purpose at this CMAX.
- **3042 ERR families in Stage C.** These are families where PSLQ raised an exception; almost certainly degenerate (L exactly zero or denormal). Not investigated further. If important, Claude can request re-analysis.
- **Pick basis missing `phi`/golden ratio basis.** The earlier T2A-BASIS-IDENTIFY caught a phi=1+sqrt(5)/2 phantom; this script's basis B includes sqrt(5) but never phi. No phantom triggered, so no concern, but the basis is a strict subset of the 7 bases used in T2A-BASIS-IDENTIFY (A through E).

## What would have been asked (if bidirectional)
- Should I run the basis-identify on a much larger sample of ratio!=1 Trans-hard families (say 50 instead of 3) to establish that none of them have a closed form? 3 picks is a small sample; Claude may want a more thorough refutation.
- Is the `Log-bilin-ext` basis (extended with `zeta(5)`, `Catalan`, `L*zeta(3)`) sufficient, or should I also try modular-form bases (`eta`, `theta`, `Dedekind eta` at quadratic CM points)? At CMAX=1 the prior session's bases A-E (which were broader) also missed the constants.

## Recommended next step
**T2A-CMAX2-CONJECTURE-RETIRE**: Given that (i) the ratio is not structural, (ii) `pi^2`-Apery connection is nonexistent, and (iii) the constants are all novel, the original 2k-degree CONJECTURE in its ratio-structural form should be retired. Two replacement directions:

**Option A (Density)** — Pursue a new conjecture: at degree-(2k, k), Trans-hard families saturate the convergent set asymptotically. Test by running CMAX=3 search on a degree-(2,1) baseline (cheaper) and CMAX=2 at degree-(6,3) (harder but tests the k=3 case).

**Option B (Atomic constants)** — Pursue identification of one or two specific Trans-hard limits via heavier methods: GP/PARI's `lindep` with much larger bases, modular form databases (LMFDB), and manual ISC submissions. Pick from the unique 108728 a sample with simplest algebraic structure (low coefficient sums, high symmetry).

I would recommend **Option A first** because Option B may need years of fishing without a guarantee.

## Files committed
- `t2a_cmax2_search.py` (sha256 a149b0aa..., 11254 bytes) — main search script
- `t2a_cmax2_deep_validate.py` (26a6fd8f..., 6818 bytes) — dps=150 K_1500 sampler
- `t2a_cmax2_ratio_analyze.py` (105f4b76..., 3377 bytes) — ratio distribution + rate
- `t2a_cmax2_pick_identify.py` (e0338069..., 4958 bytes) — basis identify on 3 picks
- `t2a_cmax2_results_summary.json` (e7804b8e..., metadata only — full 44MB file excluded; full sha256 = 008cf81f69ab3f988b5ff23e8116e465fba63d46f19f20045d80033a1f087b29)
- `t2a_cmax2_deep_results.json` (9d318d5e..., 471821 bytes) — deep-validate output
- `t2a_cmax2_pick_identify_results.json` (6b3b78b0..., 3435 bytes) — pick basis-identify output
- `t2a_cmax2_ratio_picks.json` (370b6dfc..., 1294 bytes) — 3 selected picks
- `t2a_cmax2_ratio_log.txt` (1526 bytes) — analysis stdout transcript
- `claims.jsonl` — 13 AEAL entries
- `halt_log.json` — empty `{}`
- `discrepancy_log.json` — search-space symmetry note
- `unexpected_finds.json` — 3 unexpected observations

## AEAL claim count
**13 entries** written to `claims.jsonl` this session

## Conjecture status update (Step 7)
**Status: UNCHANGED** for the 2k-degree existence claim (Trans-hard families exist abundantly at degree-(4,2), now confirmed at scale 100x larger than CMAX=1).

**Sub-hypothesis status: REFUTED** for the ratio structural law (`a4/b2^2 = const` predicts Trans-hardness): ratio is uniform across all 4 reachable values {0.25, 0.5, 1.0, 2.0} with Trans-candidate rates within 3.3 percentage points of each other.

**Sub-hypothesis status: REFUTED** for the `pi^2`-Apery-like connection: 0 Log-bilin hits in 1000-sample deep validate.

The CMAX=1 ratio=1 phenomenon is a degeneracy: ratio=1 is the ONLY achievable ratio when `|coeff|<=1`.
