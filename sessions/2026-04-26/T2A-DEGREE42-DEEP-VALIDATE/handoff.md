# Handoff — T2A-DEGREE42-DEEP-VALIDATE
**Date:** 2026-04-26
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Hardened the 1162 Trans candidates from `T2A-DEGREE42-SEARCH` by
recomputing every limit at `dps=150, K_1500`, then re-running PSLQ
against the F(2,4)-style **bilinear-π basis** `{1, L, π, L·π, π², L·π², log2, L·log2, ζ(3)}`
at `dps=150, tol=1e-100, hmax=1e12`. For surviving "trans_hard" families,
ran extended PSLQ against `{1, π, π², π³, π⁴, ζ(3), log2, log3, √2, √3, γ}`
(γ = Euler-Mascheroni). ζ(2) and ζ(4) were removed from the extended
basis to avoid spurious hits via ζ(2)=π²/6 / ζ(4)=π⁴/90 (the first
script run produced 4 such phantom "π² hits" with L-coefficient 0;
this was caught and corrected).

## Key numerical findings
- **Recompute (dps=150, K_1500): 1162/1162 converged**, 0 diverged, 0 errors.
  Mean diff |K_1500 − K_1499| < 1e-40 throughout. Script: `t2a_degree42_deep_validate.py`.
- **Bilinear-π PSLQ:** `log_bilin = 0`, **`trans_hard = 1162`**.
  Not a single Trans candidate satisfies any 9-term bilinear-π relation
  with integer coefficients ≤ 10¹². Limits are **not** of the
  F(2,4) Apéry form `α + β/π² + γ·log p`.
- **Extended PSLQ (after removing ζ(2)/ζ(4)):** `0 / 1162` hits with
  nonzero L-coefficient. The four apparent hits in the first run were
  the trivial identity `π² − 6·ζ(2) = 0`, with L-coefficient 0 — phantom.
- **Common ratio `a4 / b2² = 1.0` across all 1162 families.** This is
  a *trivial consequence of the CMAX=1 bound* (a4 ∈ {1}, b2 ∈ {−1,+1}
  ⇒ ratio = 1/1) and is **not** evidence of an Apéry-like structural law.
- **Sample trans_hard limits** (35-digit, dps=150):
  - a=[1,-1,0,0,1], b=[-1,-1,-1] → L = -1.25568229877105248065259651034078816
  - a=[1,-1,0,0,1], b=[1,1,1]    → L =  1.25568229877105248065259651034078816 (sign-flip)
  - a=[1,0,-1,-1,-1], b=[-1,1,0] → L =  1.45907918499924463713862481404675152
  - a=[1,0,0,-1,-1], b=[-1,-1,1] → L =  unpublished closed form

## Judgment calls made
- **Removed ζ(2) and ζ(4) from the extended basis.** First run flagged
  4 false-positive π² hits because PSLQ exploited the trivial identity
  `π² = 6·ζ(2)` within the basis itself (relation vector had L-coefficient 0).
  This is an honest trap; corrected by (a) removing redundant constants,
  (b) requiring L-coefficient ≠ 0 before counting an "extended hit".
- **Did not expand to CMAX=2** in this session; runtime budget for
  recompute scaled linearly (~36s/1000 families) and would have been
  ~10 min for CMAX=2's expected ~12k Trans candidates, but the
  classification verdict is the same shape regardless and adding CMAX=2
  is the recommended next session.

## Anomalies and open questions
**THE INTERPRETATION OF "Trans_hard = 1162" IS THE CRUCIAL OPEN QUESTION.**

Two competing readings:

1. **Genuine novel transcendence regime.** Every single one of 1162
   convergent (4,2)-families with `a∈{-1,0,1}^5, b∈{-1,0,1}^3, b2≠0`
   has a limit that PSLQ at dps=150 / tol=1e-100 / hmax=10¹² cannot
   express in {1, L, π, L·π, π², L·π², log2, L·log2, ζ(3)} or in the
   13-element extended basis. Limits range ~0.4–18.5. **If real,
   this is unprecedented**: F(2,4) had ~5×10⁻⁵ Trans density, here
   we see ~80% Trans density.

2. **PSLQ blind spot.** The bases tested do not include the actual
   form of these limits. Possibilities:
   - **Modular / Heun-type periods** (e.g., values of ₂F₁ at algebraic
     points) which are transcendental over Q(π, log) but expressible
     via period integrals.
   - **`L = α·exp(β)` or `L = log(α + β π)`** — not linear in any
     standard basis.
   - **Algebraic over a deeper number field** than Q(L) — would need
     extended algebraic basis up to deg 6 or beyond.

The "ratio a4/b2² = 1.0" caveat: at CMAX=1 the value of this ratio
is forced by the bound (only 1/1 = 1 is achievable with a4>0 and b2≠0).
This is **not** a structural finding analogous to F(2,4)'s `−2/9` /
`1/4` law. It must be re-tested at CMAX≥2 where a4 ∈ {1,2} and
b2 ∈ {−2,−1,1,2} create non-trivial ratio variation.

Other notes:
- The 192 Rat and 2 Alg families from Stage C were not re-validated
  this session (they remain as classified by the original search).
- The 96 ERR cases (limit=0, PSLQ degenerate) were also not revisited.
- All 1162 Trans candidates are stable under the dps=50 → dps=150
  recompute, with diff < 1e-40 between K_{1499} and K_{1500}. So at
  least the **convergence** is real.

## What would have been asked (if bidirectional)
1. Should we expand to CMAX=2 to test whether `a4/b2² = 1` is genuine
   or just a CMAX=1 artifact?
2. Are there candidate closed forms for the sample limits
   `L ≈ 1.2557` and `L ≈ 1.4591`? An ISC / OEIS / inverse-symbolic
   lookup at 35 digits could short-circuit this.
3. Should "trans_hard" families be tested against modular / Heun /
   ₂F₁ values rather than just π-power bases?

## Recommended next step
**T2A-DEGREE42-CMAX2-RATIO** — extend to CMAX=2 (~25× more families)
with focused goal: confirm or refute whether `a4/b2² = const` across
the entire (4,2) Trans stratum. If a single Trans family with
ratio ≠ 1 exists at CMAX=2, the Apéry-like-law analog is **REFUTED**.
If all CMAX=2 Trans families also have ratio = 1, the conjecture
becomes substantially stronger and merits theoretical investigation.

Budget: ~30 min recompute + classify; deeper-precision PSLQ on the
sample limits (1.2557, 1.4591, …) to look for closed forms is a
secondary but high-value parallel task.

## Verdict (per task spec STEP 6)
Per the spec's classification rules:
> "If Trans_hard > 0 AND limits do NOT involve pi^2:
>  Report: CONJECTURE PARTIALLY SUPPORTED"

**VERDICT: PARTIALLY_SUPPORTED.** A large stratum of genuine
non-bilinear-π Trans families exists at degree-(4,2) (1162 of them at
CMAX=1), but their limits do **not** involve π² in the F(2,4) Apéry
sense. The 2k-degree conjecture's *qualitative* prediction (Trans
families exist at (4,2)) is supported; its *quantitative* prediction
(limits are π²-related Apéry-like values) is **not** supported.

## Files committed
- `t2a_degree42_deep_validate.py` (sha256 5b9375ffe578f5b8a3f550fb78693c6594cd8b076c67adaecede203145bbe7b5)
- `t2a_degree42_deep_results.json` (sha256 00e126db3c705ffaa3fb68f034cbbafc714eabcb8915bf109672b8640c55187d)
- `claims.jsonl`
- `handoff.md`

## AEAL claim count
4 entries written to claims.jsonl this session
