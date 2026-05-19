# Handoff — R1-ROUTE-F-SAKAI-NONGEN
**Date:** 2026-05-20
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~85 minutes
**Status:** COMPLETE (cycle 1 of 3; cycles 2-3 not in scope per dispatch rule)

## What was accomplished

Tier-3b cycle 1 of the three-cycle R1-ROUTE-F follow-up brief is
complete. The Sakai non-generic intersection form for the PIII(D_6)
configuration was sourced from Kajiwara-Noumi-Yamada (KNY) 2017
(arXiv:1509.08186v8 = J. Phys. A 50 (2017) 073001), the
configuration-independence of the Pic intersection form (KNY
sec.3.3 eq (3.26)) was discovered and documented, and the canonical
KNY simple roots `delta_0..delta_6` from sec.8.2.19 eq (8.101) were
implemented and validated. The predecessor cycle's `alpha_i`
embedding was compared to the canonical one; verdict resolved to
`SAKAI_FORM_REQUIRES_NEW_EMBEDDING`. All 48 tests pass (31
predecessor + 17 cycle 1). No halt condition fired. Per the brief's
locked rule, cycle 2 is NOT started — returned for review.

## Key numerical findings

- `intersection_form_sakai_nongen()`: 10x10 integer matrix,
  det = +/- 1 (unimodular), signature (1, 0, 9) via
  `numpy.linalg.eigvalsh` with tol 1e-9. Coincides EXACTLY with the
  generic 8-point blow-up form `GRAM_PIC`. Recorded at dps = 0
  (integer arithmetic). Script: `sakai_d6/surface.py`.
- KNY canonical simple roots `delta_0,...,delta_6` per eq (8.101):
  each has `<delta_i, delta_i> = -2`, each is orthogonal to
  `-K_X = 2 H_1 + 2 H_2 - E_1 - ... - E_8`, and pairwise Gram
  matches the symmetric D_6^{(1)} Cartan matrix with two-fork
  topology (forks at indices 2 and 4). Script:
  `sakai_d6/surface.py`.
- POC `alpha_0,...,alpha_6` from predecessor: under the
  (configuration-independent) Sakai form they still satisfy the
  D_6^{(1)} Cartan condition, but they differ from the canonical
  KNY embedding as unordered sets of integer vectors. Specifically
  `alpha_3 = H_2 - H_1` (POC fork node) vs
  `delta_3 = H_2 - E_5 - E_6` (KNY fork node, effective). Script:
  `sakai_d6/surface.py`.
- Verifier stdout SHA256:
  `df6bbe767fddaa2dc306e04bf3bf56aee9806173711f6cc60db8c2c69bbdc121`.
  Recorded in `claims.jsonl` and `claims/claim-r1-sakai-nongen-001.json`.

## Judgment calls made

1. **Primary source choice.** Sakai 2001 (Comm. Math. Phys. 220,
   DOI 10.1007/s002200100393) is Springer-paywalled at the agent's
   position; KNY 2017 (arXiv:1509.08186v8) is open access and is
   explicitly permitted by the brief. I used KNY 2017 exclusively.
   A future paywall-accessing session can cross-check.
2. **Identifying the relevant KNY section.** The brief named
   "Sakai 2001 sec.8 or KNY 2017 sec.4". KNY sec.4 is methodological
   (concrete realisations on rational surfaces); the actual data
   for PIII(D_6) lives in sec.8.2.19 (eq (8.98) for the base-point
   configuration, eq (8.100) for the Dynkin diagram, eq (8.101) for
   the simple roots). I used sec.8.2.19 + sec.3.3 (the form). The
   brief allows substitution if it leads to the same canonical
   object.
3. **No constraint search.** The brief permits "do not derive
   Sakai-convention claims from scratch". Primary-source lookup
   replaced enumeration; no `max_coef` sweep was needed.
4. **POC gram test outcome.** The brief said: "If POC Gram matches
   D_6^{(1)} Cartan under the Sakai form, the test passes; if not,
   capture in JSON and `xfail` it". It PASSES (because the Pic form
   is unchanged from the generic case), so no `xfail` is needed.
   The JSON artefact `poc_gram_under_sakai_form.json` is written
   for downstream inspection regardless.

## Anomalies and open questions

**THIS IS THE PRINCIPAL ITEM FOR SYNTHESIZER REVIEW.**

1. **Configuration-independence of the Pic intersection form.**
   Per KNY 2017 sec.3.3 eq (3.26), the bilinear form on
   Pic(X) = Z H_1 + Z H_2 + Z E_1 + ... + Z E_8 is determined by
   the rank-10 combinatorial class "8-point blow-up of P1 x P1",
   NOT by the geometric position of the 8 base points. The "Sakai
   non-generic intersection form for PIII(D_6)" is therefore
   identical to the generic form already implemented in cycle 0
   (POC).

   The PIII(D_6) non-genericity shows up in the CHOICE of seven
   simple roots `delta_0..delta_6` (KNY eq (8.101)) attached to the
   irreducible components of the anti-canonical divisor under the
   infinitely-near base-point configuration P_12 + P_34 + P_5678.

   **Implication for cycle 2.** The brief's precondition "with the
   Sakai non-generic form from cycle 1 fixed" should be rephrased
   as "with the canonical Sakai-convention KNY embedding from
   cycle 1 fixed", with the consumed inputs being:
   - `intersection_form_sakai_nongen()` (= generic Pic form);
   - `d6_affine_simple_roots_kny()` (KNY eq (8.101));
   - `anti_canonical()` (unchanged from POC);
   - `expected_d6_affine_symmetric_cartan_kny()` (KNY's
     two-fork adjacencies).

   This rephrasing does not change the technical scope of cycles
   2 or 3, but it should be noted in the cycle 2 dispatch.

2. **Verdict branch 2 (`SAKAI_FORM_REQUIRES_NEW_EMBEDDING`)** is
   the resolved outcome. Both POC `alpha_i` and KNY `delta_i`
   satisfy the abstract D_6^{(1)} Cartan condition under the
   (unchanged) form, but they differ as unordered sets of integer
   vectors. The POC chose `alpha_3 = H_2 - H_1` (not effective);
   KNY chooses `delta_3 = H_2 - E_5 - E_6` (effective, with
   non-negative E-coefficients). Cycle 2 should consume the KNY
   `delta_i` as the canonical fixed input.

3. **Sakai 2001 original not retrieved.** Springer paywall. KNY
   2017 alone was used and is authoritative for the simple-root
   embedding. Future session with paywall access could
   cross-verify against Sakai 2001 sec.10 / sec.11 directly.

## What would have been asked (if bidirectional)

- "The brief frames the work as 'discover the Sakai non-generic
  intersection form'. KNY 2017 sec.3.3 eq (3.26) makes the Pic
  bilinear form configuration-independent. Confirm you want me to
  interpret 'non-generic data' as 'non-generic CHOICE of simple
  roots' (KNY eq (8.101))?"
- "Sakai 2001 §10 vs KNY 2017 §8.2.19 — do you want both, or is
  KNY 2017 sufficient (since the brief explicitly permits it)?"

Both questions were resolved by the locked dispatch rule
("permitted to substitute KNY 2017 if Sakai 2001 unretrievable")
and by recording the divergence prominently in this handoff.

## Recommended next step

**Launch cycle 2 (R1-ROUTE-F-K-PERP-SAT-SAKAI) with a corrected
precondition.**

Concrete dispatch:

> "Cycle 2 of the R1-ROUTE-F three-cycle brief: K_X-perp lattice
> saturation in Pic(X), with the cycle-1 canonical Sakai-convention
> KNY embedding fixed. Consume from cycle 1 (bridge commit at
> `R1-ROUTE-F-SAKAI-NONGEN`): `intersection_form_sakai_nongen()`
> [= generic form per KNY 3.26], `d6_affine_simple_roots_kny()`
> [KNY eq (8.101) seven delta_i], and the Gram-form-test passes
> recorded in `sakai_d6/tests/test_sakai_nongen.py`. Discover
> whether the rank-7 sub-lattice spanned by `{delta_i}` is
> SATURATED inside the rank-9 orthogonal complement of `-K_X`
> under the Pic bilinear form. If saturated, output
> SATURATED_AT_RANK_7; if not, output the saturation closure
> generators with computed Smith Normal Form invariants."

The brief's verbatim cycle 2 spec already captures this; the only
adjustment is that "with the Sakai non-generic FORM from cycle 1
fixed" should be read as "with the canonical Sakai-convention KNY
EMBEDDING from cycle 1 fixed" (the form coincides with the
generic).

## Files committed

```
sessions/2026-05-20/R1-ROUTE-F-SAKAI-NONGEN/
├── claims/
│   └── claim-r1-sakai-nongen-001.json   (2,653 bytes)
├── sakai_d6/
│   ├── surface.py                       (19,811 bytes, cycle-1 extended)
│   └── tests/
│       └── test_sakai_nongen.py         (9,335 bytes, 17 new tests)
├── claims.jsonl                         (1,134 bytes, 1 AEAL line)
├── COMPLETION_REPORT.md                 (7,116 bytes)
├── discrepancy_log.json                 (4 bytes, "{}")
├── halt_log.json                        (4 bytes, "{}")
├── poc_gram_under_sakai_form.json       (918 bytes)
├── sakai_nongen_verdict.json            (2,930 bytes)
├── unexpected_finds.json                (2,174 bytes, configuration-independence finding)
└── handoff.md                           (this file)
```

## AEAL claim count

1 entry written to `claims.jsonl` this session
(`claim_id = r1-sakai-nongen-001`, verdict
`SAKAI_FORM_REQUIRES_NEW_EMBEDDING`, output_hash
`df6bbe767fddaa2dc306e04bf3bf56aee9806173711f6cc60db8c2c69bbdc121`).
