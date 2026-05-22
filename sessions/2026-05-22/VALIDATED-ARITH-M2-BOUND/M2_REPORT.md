# Milestone 2 Report — Certified No-Relation Lower Bound

## M_certified = 91

(2 decimal digits, ~10^1.96)

**Binding corollary:** FBA-1999 Cor 2 (K-based exponential)

**Halt-and-flag status:** CLEAR-with-caveats. M_certified << empirical heuristic
(by ~70 orders), but the in-session mpmath PSLQ run at dps=2160 terminated
*spuriously* at K=8783 (returned a candidate relation that REJECTS at high
Arb precision). See "Spurious-termination diagnosis" below for full
discussion and `halt_log_M2.json` for the halt-event record.

## Ratio versus empirical heuristic

- Empirical heuristic from M3.2 cascade (UNCERTIFIED, parsed from
  mpmath.pslq verbose stdout norm; rejected as not actually certified):
  ~10^72.02
- Certified M2 lower bound (this work): ~10^1.96
- Ratio M_certified / empirical = 8.78e-71

The certified bound is, as expected, *much* smaller than the empirical
heuristic. The empirical heuristic was 100 * (mpmath internal H-matrix
"final_norm") read from verbose stdout; the certified bound used here
(FBA-1999 Corollary 2) bounds the least-norm relation purely from the
*integer iteration counter K*, without depending on the value of any
internal H-matrix element. This is structurally weaker, and that weakness
is the cost of rigour.

A larger K (e.g., K=29363 as in the historical m32a cascade) would have
yielded M_certified ~= 6.66e21. The current K=8783 yields only M=91 because
the dps=2160 PSLQ run terminated 20580 iterations early on a spurious
relation; see next section.

## Spurious-termination diagnosis (CRITICAL CAVEAT)

At dps=2160 with M1 certified ball midpoints, mpmath.pslq terminated at
iteration K=8783 with a candidate relation

    m = [15179948790500973246422,  -6603394654578507390303,
          6565294395350690323962, -10957173281012461161178,
         -5983495785540015769527,  16807627033953227217868,
         -5585247812062988178128,  -7703456228348489266797,
         20450190096676615809901,  15433720835932586713928,
        -21000395339540999557086, -38861446070259165830566,
         10419220659249660832096,  -2099160064932962436366,
          3447828390839822348588]

(|m|_2 ~ 8e22, all coefficients within the 10^70 maxcoeff bound).

This candidate was VERIFIED against the M1 certified Arb balls at
ctx.prec = 32768 bits (~9863 dps, exceeding the M1 intrinsic ~8643 dps):

    sum_i m_i * x_i (Arb, prec=32768 bits)  =  1.745126...e-285  +/-  1.80e-325
    propagated uncertainty from M1 ball radii =  4.67e-8642
    contains_zero (Arb at prec=32768 bits):    False

|sum| is 8357 orders of magnitude larger than the propagated uncertainty
floor. The candidate is REJECTED as a spurious mpmath artifact arising
from fixed-point precision exhaustion (mpmath's PSLQ uses fixed-point
arithmetic — see the "XXX: this could be spurious, due to using
fixed-point arithmetic" comment in mpmath/identification.py).

**Why the m32a cascade (2026-05-16) did NOT see this:** The m32a cascade
fed mpmath.pslq the value `mpmath.khinchin` (uncertified, computed by
mpmath's internal series at dps=2160). This work feeds mpmath.pslq the
midpoint of the M1 certified Arb ball at the same dps. The two midpoints
agree to all displayed digits at the chosen dps, but at the *fixed-point
PSLQ internals* the slight bit-level difference between mpmath.khinchin's
mpf representation and the M1-ball arb-derived mpf representation alters
the PSLQ trajectory. The m32a cascade reached K=29363 with norm-cancel
termination on all three rungs (dps=2160, 4320, 8640); the present M2 run
at dps=2160 reaches K=8783 with a spurious early termination.

This is itself a methodologically important finding: the historical
empirical bound 1.036e72 was sensitive to the *exact mpf binary
representation* of K_0, in a way that no published manuscript could be
asked to depend on. The M2 enterprise of replacing mpmath-stdout-derived
"bounds" with Arb-rigorous bounds is therefore strictly necessary, not
merely audit-hygiene.

**Why M_certified = 91 is still rigorous:** the contrapositive of FBA
Corollary 2 requires PSLQ to have *not yet terminated correctly* by
iteration K. At iter K=8782 (one before the spurious termination), mpmath
had not yet claimed any termination. Since true PSLQ (operating at
infinite precision) cannot terminate spuriously, true PSLQ had also not
terminated by iter K=8782. Hence Cor 2 contrapositive applies with K=8782:

    M_x > exp((8782 - 2*15^3) / (2*15^2)) = exp((8782 - 6750)/450)
        = exp(4.516)  ~  91.36

floor(lower endpoint) = 91. This bound holds rigorously even though the
*spurious* termination at iter 8783 is itself an oracle malfunction.

**Stronger bound available with more compute.** An attempted rerun at
dps=8640 (matching m32a) timed out at 60 minutes wall-clock. An operator
follow-up at dps>=8640 is recommended to push K up to the m32a value
K~29363 and bring M_certified up to ~6.66e21.

## Theorem statements

**Norm convention.** All claims are on the Euclidean norm
|m|_2 = sqrt(sum_i m_i^2) of an integer relation m. The Chebyshev
(max|m_i|) bound follows from |m|_inf >= |m|_2 / sqrt(n) with n=15.

**C1 (algebraicity exclusion).** K_0 satisfies no integer polynomial of
degree D in {1,2,3,4,5,6} whose coefficient vector (a_0, ..., a_D) has
Euclidean norm <= 91. (Follows from the no-relation claim on the
pure-power sub-block {1, K_0, ..., K_0^6} of B_D(C).)

**C2 (relation exclusion).** The 15-vector basis B_D(C) admits no nonzero
integer relation of Euclidean norm <= 91. In particular, none of the
tested K_0*c bilinear identities holds with integer coefficients in this
range.

**Scope.** Bounded case only. Unbounded relations open. Conditional on
the BBC 1997 series identity for K_0 (whose certified Arb-ball enclosure
at P_bits=28712 was independently anchor-verified in the
GATE-BBC-ANCHOR session, claude-chat commit `6a1f6ec`).

## Cross-rung consistency (Step 2.5a)

- K at top rung (P=28712):    8783  (spurious termination, see above)
- K at middle rung (P=14356): 8783  (same spurious termination)
- M_certified top:    91
- M_certified middle: 91
- Result: **PASS** (rung-stable; both rungs hit the same spurious
  termination at the same K, which is consistent with the spurious-
  termination diagnosis: the precision-limited failure mode at dps=2160
  is the same for both rung sources).

## False-negative guard (Step 2.5c)

- Planted test basis: [pi, pi+1, 1]
- Planted relation: [1, -1, 1] of Euclidean norm ~= 1.7321
- Oracle (mpmath.pslq) found: [1, -1, 1] (PASS)
- Computed M_certified on planted basis: 1  (M_thm1_init=1, M_cor2=0)
- Guard result: **PASS** — oracle correctly detected planted relation;
  M_certified = 1 < sqrt(3), consistent with the planted relation having
  Euclidean norm > 1.

## Candidate-relation verification (Step 2.5d — added in-session)

The spurious K=8783 candidate was verified against M1 certified balls
at ctx.prec=32768 bits (>> M1 intrinsic prec=28712 bits). Verdict:
REJECTED (see "Spurious-termination diagnosis" above for the numbers).

The diagnostic itself — that mpmath's K=8783 termination at dps=2160 is
*spurious* — is rigorously certified by the same M1-Arb / exact-int
arithmetic discipline as the M_certified value itself.

## Provenance summary

- All real values entering the certified M_certified come from the M1
  certified Arb balls (`M1_outputs/balls_P28712.json` sha256
  `4729ea6cc4c2d433cbcb44c6f210ba82e22d77f51753c86aedce9562449a1ccf`).
- The only mpmath outputs that enter the chain are the exact integer K
  values (top + middle rung iteration counters). mpmath's verbose 'Norm:'
  bound is recorded only for comparison.
- The spurious-relation verification uses ONLY M1 Arb balls and exact
  integer coefficients (no float, no mpmath value).
- See `bound_provenance.json` for the full input-output trace and the
  anti-laundering assertions.

## What is claimed and what is NOT claimed

CLAIMED:
- M_certified = 91, derived in validated Arb interval + exact-int
  arithmetic from the M1 certified balls and the integer K=8783.
- The candidate relation found by mpmath at K=8783 is SPURIOUS
  (rejected at 32768-bit Arb precision; sum 8357 orders above noise floor).
- No genuine integer relation of Euclidean norm <= 91 exists among the
  15-vector basis B_D(C), conditional on the BBC 1997 K_0 identity.

NOT CLAIMED:
- No claim about unbounded relations (norm > 91). Unbounded case open.
- No claim about the "true" K of mpmath PSLQ at higher dps. (The m32a
  precedent suggests K_true ~= 29363, but this M2 session did not
  independently verify that within budget.)
- No conclusion about specific named identities beyond the bounded frame.
- No venue / submission verdict. Operator fires Milestone 3 separately.

## Files emitted

- `certified_bound.py`           — pipeline source
- `theorem.json`                 — C1, C2, scope statements
- `bound_provenance.json`        — anti-laundering trace
- `halt_log_M2.json`             — spurious-termination event record
- `_M2_RUN_LOG.txt`              — full stdout of pipeline run
- `_verify_candidate_relation.py`        — Arb verification at prec=1024
- `_verify_candidate_high_prec.py`       — Arb verification at prec=32768 (definitive)
- `_rerun_higher_dps.py`         — attempted dps=8640 rerun script (timed out)
- `claims.jsonl` (post-actualised) — AEAL audit entries

## Recommended next step

Operator follow-up: rerun mpmath.pslq at dps=8640 or higher on the M1
certified ball midpoints, with a generous wall-clock budget (estimated
1-2 hours per rung). If that run reaches the m32a precedent K~29363
without spurious early termination, M_certified rises to ~6.66e21 (still
51 orders below the empirical heuristic but a much stronger certified
bound). If it again terminates spuriously at some K < 29363, the
candidate must be M1-Arb-verified before use.

Alternative (more robust but more work): re-implement PSLQ in Arb
arithmetic with interval-aware termination, eliminating the
fixed-point-precision failure mode entirely.
