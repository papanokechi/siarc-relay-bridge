# R1-ROUTE-F-K-PERP-BASIS cycle 2 completion report
Date: 2026-05-20
Predecessor (cycle 1): R1-ROUTE-F-SAKAI-NONGEN (bridge commit `53efe94`)
Cycle: 2 of 3 (cycle 3 NOT in scope this session)

## What this cycle was

Tier-3b cycle 2 of the R1-ROUTE-F three-cycle brief: with the
cycle-1 canonical Sakai-convention KNY embedding fixed
(`d6_affine_simple_roots_kny()` per KNY 2017 sec.8.2.19 eq (8.101),
under the configuration-independent Pic form per KNY sec.3.3
eq (3.26)), decide whether the rank-7 sublattice
`L_delta = Z<delta_0,...,delta_6>` is SATURATED inside the
rank-9 orthogonal complement
`K_X^perp = { v in Pic(X) : <v, -K_X> = 0 }`.

Synthesizer amendment from cycle 1's review (verbatim): "the
cycle's fixed input is the canonical Sakai-convention KNY embedding
from cycle 1, not a 'non-generic intersection form'. Consume
`d6_affine_simple_roots_kny()` as the canonical delta_i; the Pic
form is the standard 8-point-blow-up form per KNY sec.3.3
eq (3.26)."

## Primary source (re-anchored from cycle 1)

  Kajiwara, Noumi, Yamada (KNY) 2017,
  "Geometric Aspects of Painleve Equations",
  J. Phys. A: Math. Theor. 50 (2017) 073001,
  arXiv:1509.08186v8 (168 pages).

  - sec.3.3 eq (3.26): Pic intersection form
    (configuration-independent).
  - sec.8.2.19 eq (8.101): canonical D_6^{(1)} simple roots delta_i.

  These are the same source pages used in cycle 1; no new primary
  retrieval needed.

## Method

1. Construct an explicit Z-basis of `K_X^perp` (rank 9) by
   parametrising the kernel of the integer linear functional
   `f(v) = <v, -K_X> = 2 v_{H_1} + 2 v_{H_2} + sum_{j=1..8} v_{E_j}`
   over the canonical Pic basis. The free coordinates are
   `(v_{H_1}, v_{H_2}, v_{E_2}, ..., v_{E_8})` with `v_{E_1}`
   determined. The resulting basis is:

       b_1 = H_1 - 2 E_1
       b_2 = H_2 - 2 E_1
       b_{3+k} = E_{2+k} - E_1   (k = 0..6)

   Because `gcd(2, 2, 1, ..., 1) = 1`, `K_X^perp` is a primitive
   rank-9 sublattice of `Pic(X) = Z^10`.

2. Express each KNY `delta_i` as a Z-linear combination of
   `{b_1, ..., b_9}`. By the free-coordinate construction this
   reduces to reading off the (H_1, H_2, E_2..E_8) coordinates of
   `delta_i`. Result: the 7x9 integer matrix M
   = `kny_in_k_perp_coords()`.

3. Compute the Smith Normal Form of M via
   `sympy.matrices.normalforms.smith_normal_form`. Read off the
   seven elementary divisors `d_1, ..., d_7`. By the SNF
   structure theorem `K_X^perp / L_delta` has torsion part of
   order `prod(d_i)`; `L_delta` is saturated iff every `d_i = 1`.

## Cycle 2 verdict (resolved to exactly one of two branches)

  SATURATED_AT_RANK_7

  Elementary divisors: `(1, 1, 1, 1, 1, 1, 1)`.
  Saturation index: 1.
  Closure generators needed: 0.

Justification:
  - All `d_i = 1`, so `K_X^perp / L_delta` is torsion-free.
  - Equivalently, every primitive integer vector `v in Q L_delta`
    that lies in `K_X^perp` is already in `L_delta` itself.
  - The quotient `K_X^perp / L_delta` is a free abelian group of
    rank `9 - 7 = 2` (corresponding to the two-parameter Halphen
    pencil dimension of the PIII(D_6) initial-value space).

## Files touched this cycle

Files modified (extended in place from predecessors):
  - `claims.jsonl`            1 -> 2 lines (cycle 2 AEAL line appended)
  - `unexpected_finds.json`   cycle 1 entry preserved; cycle 2
                              algebraic-geometry pins added
  - `COMPLETION_REPORT.md`    this file (cycle 1 version preserved
                              in bridge at sessions/2026-05-20/
                              R1-ROUTE-F-SAKAI-NONGEN/)

Files created this cycle:
  - `sakai_d6/saturation.py`               cycle-2 module
  - `sakai_d6/tests/test_k_perp_basis.py`  26 tests in 5 classes
  - `claims/claim-r1-k-perp-basis-001.json`  pre-registered claim
  - `k_perp_basis.json`                    9x10 K_perp Z-basis
  - `kny_in_k_perp_coords.json`            7x9 KNY delta_i in K_perp coords
  - `saturation_verdict.json`              verdict + SNF + index

Files unchanged from cycle 1 (passing through):
  - `sakai_d6/surface.py`, `sakai_d6/root_system.py`,
    `sakai_d6/__init__.py`, `sakai_d6/tests/__init__.py`,
    `sakai_d6/tests/test_root_system.py`,
    `sakai_d6/tests/test_sakai_nongen.py`,
    `claims/claim-r1-poc-001.json`,
    `claims/claim-r1-sakai-nongen-001.json`,
    `poc_gram_under_sakai_form.json`,
    `sakai_nongen_verdict.json`,
    `halt_log.json` (still {}), `discrepancy_log.json` (still {}),
    `README.md`, `refs.md`, `vquad_data/stokes_table.json`.

## Reproduce command

  cd pcf-r1-route-f
  python -m pytest sakai_d6/tests/ -v
  python -m sakai_d6.saturation --analyze

Output (analyze stdout, the AEAL-hashed scope):

  {
    "cycle2_verdict": "SATURATED_AT_RANK_7",
    "elementary_divisors": [1, 1, 1, 1, 1, 1, 1],
    "k_perp_basis_has_rank_9": true,
    "k_perp_basis_orthogonal_to_canonical": true,
    "k_perp_rank": 9,
    "kny_orthogonal_to_canonical": true,
    "n_closure_generators": 0,
    "reconstruction_kny_from_k_perp_coords": true,
    "saturation_index": 1,
    "snf_seven_nonzero_elementary_divisors": true
  }

  exit=0

SHA256 of analyze stdout:
  fe150ee817030bab070b2fa1c07cfbedb4c6e058e4882875db7a9aba0b371ee4

Pytest summary: 74 passed in 5.14 s (31 cycle 0 + 17 cycle 1 + 26 cycle 2).

## AEAL claim status

VERIFIED.

`claims/claim-r1-k-perp-basis-001.json` was pre-registered with
two named verdict branches and five halt conditions. Actual
verdict `SATURATED_AT_RANK_7` is recorded in the claim, in
`saturation_verdict.json`, and as the second line of
`claims.jsonl`. No halt condition fired.

## Algebraic-geometry pins (new, cross-cycle)

These were not asserted before but are now established by the
cycle-2 cross-consistency tests:

1. **KNY imaginary root identity.** `sum_i a_i * delta_i = -K_X`
   with affine marks `a = (1, 1, 2, 2, 2, 1, 1)`. This identifies
   the affine D_6^{(1)} imaginary root with the anti-canonical
   class in Pic(X). Pinned by
   `test_kny_imaginary_root_equals_anti_canonical`.

2. **Anti-canonical self-intersection.** `(-K_X)^2 = K_X^2 = 0`
   for Bl_8(P^1 x P^1) (Halphen pencil / rational elliptic surface
   with K^2 = 0). The predecessor test
   `test_self_intersection_is_eight` actually asserts the value 0
   despite its misnomer name (verified in cycle 2 by reading the
   test body). Pinned in cycle 2 by
   `test_anti_canonical_self_intersection_is_zero`.

3. **Anti-canonical is isotropic and in K_X^perp.** Because
   `(-K_X) . (-K_X) = 0`, `-K_X` itself satisfies the orthogonality
   condition defining `K_X^perp` and therefore belongs to that
   sublattice. Explicit decomposition:
   `-K_X = 2 b_1 + 2 b_2 - b_3 - b_4 - b_5 - b_6 - b_7 - b_8 - b_9`.
   Pinned by `test_anti_canonical_is_in_k_perp`.

## Anomalies and open questions

1. **Pre-existing test name "test_self_intersection_is_eight"
   asserts the value zero.** The predecessor (cycle 0) test name
   suggests `K^2 = 8` but the body asserts `intersect(k, k) == 0`
   with an inline comment explaining the misnomer. Cycle 2 leaves
   the test as-is (it passes and its content is correct) and adds
   a clearly-named cross-consistency test
   `test_anti_canonical_self_intersection_is_zero` in
   `test_k_perp_basis.py` to make the actual asserted value
   discoverable by name.

2. **Cycle 3 (effectivity classification) is NOT started this
   session.** Per the locked cycle dispatch rule, cycle 3 will be
   relayed separately after synthesizer review of this cycle.

3. **Quotient K_X^perp / L_delta has rank 2.** This is the
   expected dimension count for the "transcendental" parameter
   space of the PIII(D_6) initial-value variety (the two-parameter
   Halphen pencil). Cycle 3 may want to compute the Picard form
   restricted to this rank-2 quotient and identify the resulting
   lattice (e.g., is it the trivial lattice
   Z*K_anti + Z*F for a fibre F, or something else?). This is
   left as an open item; the synthesizer can decide whether
   cycle 3 should encompass this or stop at the effectivity
   classification of the delta_i.

4. **No closure generators were produced** because the verdict
   was SATURATED (index 1). The `saturation_closure_generators()`
   helper is implemented but returns an empty list. It is wired
   to the (lazily-imported) `smith_normal_decomp` in
   `sympy.matrices.normalforms`. If the verdict had been
   NOT_SATURATED_WITH_INDEX_k, this code path would have produced
   the generators. The branch is therefore code-complete but
   not exercised by an actual run; a future regression test could
   cover it with a synthetic example.
