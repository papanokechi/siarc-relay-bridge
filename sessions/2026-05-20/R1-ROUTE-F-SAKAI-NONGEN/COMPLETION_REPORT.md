# R1-ROUTE-F-SAKAI-NONGEN cycle 1 completion report
Date: 2026-05-20
Predecessor: R1-ROUTE-F-POC (bridge commit `0d7d20e`)
Cycle: 1 of 3 (cycles 2 and 3 NOT in scope this session)

## What this cycle was

Tier-3b cycle 1: discover the Sakai non-generic intersection form
for the PIII(D_6) configuration on Pic(X), implement it, and decide
whether the predecessor POC's seven simple roots alpha_0,...,alpha_6
survive under the canonical Sakai form.

The locked dispatch rule (verbatim from the brief) was: "Run cycle 1
first and return for review before launching cycle 2." Cycle 2
(K_X-perp saturation) and cycle 3 (effectivity classification) are
not started.

## Primary source

  Kajiwara, Noumi, Yamada (KNY) 2017,
  "Geometric Aspects of Painleve Equations",
  J. Phys. A: Math. Theor. 50 (2017) 073001,
  arXiv:1509.08186v8 (168 pages, retrieved 2026-05-20).

  - sec.3.3 eq (3.26): the Pic(X) intersection form for any 8-point
    blow-up of P1 x P1.
  - sec.8.2.19 eq (8.98): the PIII(D_6) blow-up base-point
    configuration P_12 + P_34 + P_5678 (two 2-fold + one 4-fold
    infinitely-near).
  - sec.8.2.19 eq (8.100): the Dynkin diagram with the two-fork
    topology (left fork at delta_2 connecting delta_0, delta_1;
    right fork at delta_4 connecting delta_5, delta_6).
  - sec.8.2.19 eq (8.101): the canonical seven simple roots delta_i.

  Sakai 2001 (Comm. Math. Phys. 220, DOI 10.1007/s002200100393) is
  the original; the brief explicitly permits KNY 2017 as a
  substitute. Sakai 2001 itself is Springer-paywalled at the agent's
  position. KNY 2017 is open access via arXiv.

## Key algebraic-geometry finding (recorded in `unexpected_finds.json`)

The Pic(X) intersection form is configuration-independent: it
depends only on the rank-10 combinatorial class of "8-point blow-up
of P1 x P1", not on the position of the 8 base points. Hence the
PIII(D_6) "non-generic intersection form" coincides with the
generic 8-point blow-up form already implemented in the
predecessor session.

The PIII(D_6) non-genericity manifests instead in the CHOICE of the
seven simple roots delta_0,...,delta_6 (KNY eq (8.101)) attached to
the irreducible components of the anti-canonical divisor under the
infinitely-near base-point configuration.

The brief's framing "discover the Sakai non-generic intersection
form" is therefore a slight misnomer. The technical content of
cycle 1 is the canonical Sakai-convention SIMPLE-ROOT EMBEDDING,
not the form itself. This finding does not invalidate cycles 2
or 3; it merely rephrases their preconditions.

## Cycle 1 verdict (resolved to exactly one of three branches)

  SAKAI_FORM_REQUIRES_NEW_EMBEDDING

Justification:
  - Both POC alpha_i and KNY delta_i satisfy abstract D_6^{(1)}
    Cartan condition under the same (configuration-independent)
    form: each squared length -2, pairwise zero-or-one off-diagonal,
    orthogonal to -K_X, Gram matrix matches the D_6^{(1)} Cartan
    with two-fork topology.
  - But they differ as unordered sets of integer vectors in Pic(X).
    POC: alpha_3 = H_2 - H_1 (central node, NOT effective in the
    sense of having E coefficients all >= 0).
    KNY: delta_3 = H_2 - E_5 - E_6 (effective).
  - Therefore the canonical Sakai embedding is the KNY one, which
    is different from the POC one. Cycle 2 should consume the KNY
    embedding (delta_i) as the canonical fixed input.

## Files touched this cycle

Files modified (extended in place from predecessor):
  - `sakai_d6/surface.py`     270 -> 590 lines (added Sakai-form
                              machinery; predecessor API unchanged)
  - `claims/claim-r1-sakai-nongen-001.json`  pre-registered, output
                              hash filled in after reproduce run
  - `unexpected_finds.json`   was {}; now records the
                              configuration-independence finding
  - `COMPLETION_REPORT.md`    this file (replaces predecessor's)

Files created this cycle:
  - `sakai_d6/tests/test_sakai_nongen.py`   17 tests in 4 classes
  - `claims.jsonl`            1 AEAL line for cycle 1
  - `poc_gram_under_sakai_form.json`        the 7x7 POC Gram under
                              the Sakai form
  - `sakai_nongen_verdict.json`             the verdict, the two
                              embeddings, and the source citation

Files unchanged from predecessor (passing through to bridge):
  - `sakai_d6/__init__.py`, `sakai_d6/root_system.py`,
    `sakai_d6/tests/__init__.py`, `sakai_d6/tests/test_root_system.py`,
    `README.md`, `refs.md`,
    `halt_log.json` (still {}), `discrepancy_log.json` (still {}),
    `claims/claim-r1-poc-001.json`, `vquad_data/stokes_table.json`.

## Reproduce command

  cd pcf-r1-route-f
  python -m pytest sakai_d6/tests/ -v
  python sakai_d6/surface.py --verify-lattice

Output (verifier-only, the AEAL-hashed stdout):

  {
    "cycle1_verdict": "SAKAI_FORM_REQUIRES_NEW_EMBEDDING",
    "intersection_form_unimodular": true,
    "kny_embedding_gram_matches_expected": true,
    "kny_embedding_orthogonal_to_canonical": true,
    "kny_embedding_self_intersection_minus_two": true,
    "pic_rank": 10,
    "sakai_form_equals_generic_form": true,
    "sakai_form_signature_negative": 9,
    "sakai_form_signature_positive": 1,
    "sakai_form_signature_zero": 0,
    "sakai_form_unimodular": true,
    "simple_root_gram_matches_expected": true,
    "simple_roots_orthogonal_to_canonical": true,
    "surface_type": "D6_affine"
  }

  exit=0

SHA256 of verifier stdout:
  df6bbe767fddaa2dc306e04bf3bf56aee9806173711f6cc60db8c2c69bbdc121

Pytest summary: 48 passed in 16.64 s (31 predecessor + 17 cycle 1).

## AEAL claim status

VERIFIED.

`claims/claim-r1-sakai-nongen-001.json` was pre-registered before
retrieval with three named verdict branches and three halt
conditions. The actual resolved verdict
`SAKAI_FORM_REQUIRES_NEW_EMBEDDING` is recorded in the claim, in
`sakai_nongen_verdict.json`, and as the single line in
`claims.jsonl`. No halt condition fired.

## Anomalies and open questions

1. The brief's framing of a "non-generic Pic intersection form" is
   technically a misnomer (see "Key algebraic-geometry finding"
   above). This is the principal item for synthesizer review.
   Cycles 2 and 3 are unaffected in substance, but their
   precondition phrasing should be adjusted from "with the Sakai
   non-generic FORM from cycle 1 fixed" to "with the canonical
   Sakai-convention KNY EMBEDDING from cycle 1 fixed".

2. Cycle 2 (K_X-perp saturation) and cycle 3 (effectivity
   classification) are NOT started this session. The brief locked
   "Run cycle 1 first and return for review before launching
   cycle 2"; this is being honoured.

3. Sakai 2001 §10/§11 (the original paper) was not retrieved
   (Springer paywall). All Sakai-convention claims are sourced
   from KNY 2017. This is permitted by the brief but should be
   noted: a future session with paywall access could
   cross-verify KNY against Sakai directly.

