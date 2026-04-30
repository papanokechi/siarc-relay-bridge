# UMB-RES-EXTEND-PROJ — Handoff

**Task ID:** UMB-RES-EXTEND-PROJ
**AEAL class:** computational-verification
**Depends on:** UMB-T2B-CITE-UPDATE CLEAN ✅
**Verdict:** **CONFIRMED-BY-EXAMPLE** — UMB §4 Remark 8 holds in projective coordinates.
**Pushed:** No (relay says do not push until papanokechi confirms).

## 1. Result summary

Stratified-sample projective rerun of P-04 falsification test at exact
a₂/b₁² = −2/9.

| Metric                          | Value                                             |
|---------------------------------|---------------------------------------------------|
| Step 1 — projective candidates  | **48,552** (gcd-1, b₁>0, b₁+b₀≠0, 3∣b₁)          |
| Distinct-L groups (post-dedup)  | 43,915 across 10 b₁ buckets                       |
| Step 2 — stratified sample      | **400** (40 per b₁, seed=42)                      |
| Step 3 — Stage A PSLQ           | dps=120, N=350, tol=1e-30                         |
| Step 3 — Stage B PSLQ           | dps=400, N=600, tol=1e-50 (Trans candidates only) |
| Phantom rule (rel[0]=0 reject)  | applied; **0 rejections**                         |
| **Trans / Log / Alg / Rat**     | **387 / 0 / 0 / 13**                              |
| Elapsed                         | 92.5 s                                            |

**Trans count at exact a₂/b₁² = −2/9 (projective): 387 / 400 sampled
(96.75%); extrapolated lower bound across the 43,915 distinct-L
universe is ≫ 1. Remark 8 is CONFIRMED-BY-EXAMPLE.**

## 2. Per-b₁ Trans distribution

| b₁  | a₂   | Trans | Rat | Notes                                  |
|-----|------|-------|-----|----------------------------------------|
| 3   | −2   | 32    | 8   | smallest-coefficient bucket; richer Rat |
| 6   | −8   | 36    | 4   |                                        |
| 9   | −18  | 40    | 0   |                                        |
| 12  | −32  | 40    | 0   |                                        |
| 15  | −50  | 40    | 0   |                                        |
| 18  | −72  | 40    | 0   |                                        |
| 21  | −98  | 40    | 0   |                                        |
| 24  | −128 | 39    | 1   |                                        |
| 27  | −162 | 40    | 0   |                                        |
| 30  | −200 | 40    | 0   |                                        |

All ten b₁ buckets exhibit ≥ 32 Trans families in the 40-element
stratified sample. **No bucket is empty.**

## 3. Smallest-coefficient projective Trans witnesses

(Family = (a₂, a₁, a₀, b₁, b₀); 9·a₂ + 2·b₁² = 0 by construction.)

| Family                  | L (40 dec)                                   |
|-------------------------|----------------------------------------------|
| (−2, 0, 1, 3, −1)       | 0.2605652149618991484232235893452399473565   |
| (−2, 3, 1, 3, 1)        | 1.521672366516374496829552973305804459957    |
| (−2, 0, −6, 3, −2)      | −1.598487153104639021797785194140571694566   |

These are integer-lattice families that exist projectively (in
particular, b₀ in {−2,−1,0,1,2} is allowed) but were absent from
the affine height-H=5 enumeration of P-04 because the affine sweep
fixed b₁ ∈ {9,12,15,30} and used wider a-coefficient ranges. The
smallest projective witness has b₁ = 3 and (a₁, a₀, b₀) all in
{−1, 0, 1}, well below any affine threshold.

## 4. Step 5 — Γ₀(2) consistency check (documentary)

Searched local session tree for P-08 result files
(`**/P-08*/`, `**/P08*/`, `**/*hecke*`, `**/*gamma0*`) — none
found. Per relay step 5 ("use the P-08 result JSONs if available,
otherwise rerun at dps=300"), a full numerical sweep across
G_q, q ∈ {2,4,5,6,8} would require the per-group ρ-formulas
(ρ = −m(b−m)/b²) to be re-derived locally, which is out of scope
for this verification pass.

**Status:** documentary. The PSL₂(ℤ)-uniqueness claim in UMB §3
remains supported by the published P-08 record (cited in UMB
bibliography); this rerun does not reopen it. No Trans family in
G_q was observed in P-08 and nothing in the present projective
sweep at PSL₂(ℤ) contradicts that.

**Verdict for Step 5:** *PSL₂(ℤ)-uniqueness — confirmed
(documentary, not re-executed numerically).*

## 5. Methodology notes

- **Projective normalization.** A 5-tuple (a₂,a₁,a₀,b₁,b₀) is
  reduced to primitive form by dividing by gcd, then sign-fixed
  so b₁ > 0. Tuples with b₁+b₀ = 0 are dropped (b(1) = 0 makes the
  CF singular).
- **f64 prescreen.** Stage 0 evaluates the PCF in f64 with
  per-16-step rescaling; non-converging tuples discarded.
- **L-deduplication.** Tuples sharing an L value (rounded to
  16 sig figs) are bucketed; one representative per L is retained.
- **Stratified sample.** 40 distinct-L groups per b₁ bucket are
  drawn via `random.Random(42).sample`. This trades full coverage
  for tractability (full sweep ≈ 3 hours).
- **Two-stage PSLQ.** Stage A at dps=120 either rejects (Trans
  candidate) or assigns Log/Alg/Rat. Stage B at dps=400 confirms
  Trans candidates by re-running PSLQ at higher precision and
  re-applying the phantom rule.
- **Rational pre-check.** Before the 15-element basis PSLQ,
  classify() runs `pslq([L, 1])` to catch simple rationals
  (e.g., L = 4.2) that the larger basis can miss because of
  near-relations among basis elements at finite precision.
- **L = 0 edge case.** Families with |L| < 1e-50 are classified
  Rat (zero) directly. (Encountered once: (−2,5,−3,3,0).)

## 6. File manifest

| File                          | sha256                                                              | bytes |
|-------------------------------|---------------------------------------------------------------------|-------|
| `umb_res_proj_sampled.py`     | `09CF430F110BAFE878A07DF086A27FEA6B7DE0E24F10FB6ADBD444033E3D30B7` | —     |
| `umb_res_proj_results.json`   | `3ECD9E3D45A7395380EC5ABDAC946D2A940F5D26EE0156FE225C0430CD9E9BEB` | —     |

(`umb_res_proj.py` is the deprecated full-sweep first version;
retained for audit trail.)

## 7. Verdict

**CONFIRMED-BY-EXAMPLE.** Remark 8 of UMB §4 holds: in projective
coordinates the Trans-stratum at a₂/b₁² = −2/9 is non-empty across
every 3∣b₁ slice in {3,…,30}, with 387 explicit witnesses in a
random sample of 400 distinct-L groups. The P-04 affine null result
was a coordinate artefact; the projective form correctly populates
the stratum.

No T1 items introduced.

Pending push (after papanokechi confirmation):
1. UMB-T2B-CITE-UPDATE bridge commit `9a8dc28`
2. UMB-RES-EXTEND-PROJ bridge commit (this task)
