# R1-ROUTE-F-POC completion report

Date: 2026-05-20T05:42:17Z
Duration: 60 min (v1.1 audit-and-close pass; original POC scaffold was
written 2026-05-19 in the precursor session and pre-registered then)
Brief version: v1.1

## Files created

POC scaffold (created in precursor session 2026-05-19, audited and
finalised here):

```
   67 README.md
   24 refs.md
    1 sakai_d6/__init__.py
  446 sakai_d6/surface.py
  186 sakai_d6/root_system.py
    0 sakai_d6/tests/__init__.py
  137 sakai_d6/tests/test_root_system.py
   11 vquad_data/stokes_table.json
   52 claims/claim-r1-poc-001.json
```

POC tests in `sakai_d6/tests/test_root_system.py`: 31. The wider
test suite (`sakai_d6/tests/`) contains 147 tests; the additional
116 are from cycles 1, 2, 3a, 3b and are out of scope for the POC
verification_criteria but are confirmed green for substrate
stability.

Surface module: 446 lines includes the cycle-1 KNY canonical
embedding extensions. The pure POC layer is the 8-point Pic
machinery, anti-canonical class, candidate alpha_0..alpha_6
embedding, and the `surface_type()` and `--verify-lattice` entry
points; all are exercised by the POC verification.

This audit session also wrote:

```
    7 vquad_data/stokes_table.json  (rewritten to brief schema)
    -  claims.jsonl                  (appended 1 line; now 5 entries)
    -  reproduce_pytest.txt          (16 KB captured pytest log)
    -  reproduce_verify_lattice.txt  (592 B verifier JSON)
```

## Reproduce command output

```
$ cd pcf-r1-route-f && python -m pytest sakai_d6/tests/ -v && \
    python sakai_d6/surface.py --verify-lattice
```

Pytest final summary line (verbatim; full per-test log saved at
`reproduce_pytest.txt`):

```
============================ 147 passed in 35.81s =============================
```

`--verify-lattice` stdout (verbatim, 592 bytes, exit code 0):

```
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
```

POC verification criteria mapping (all three satisfied):

- `test_root_system_passes`: pytest reports 147 passed
  (POC subset: 31 tests in `test_root_system.py`).
- `surface_intersection_form_is_unimodular`: verifier reports
  `"intersection_form_unimodular": true`.
- `orthogonal_complement_lattice_type`: verifier reports
  `"surface_type": "D6_affine"`.

## AEAL claim status

VERIFIED

SHA256 of verifier stdout:
`df6bbe767fddaa2dc306e04bf3bf56aee9806173711f6cc60db8c2c69bbdc121`
(bit-identical to `claim-r1-sakai-nongen-001` from cycle 1; the
match confirms that the deterministic JSON dump of `verify_report()`
has not drifted between the cycle-1 commit and this audit).

## Standard references cited

From `refs.md` (citations only, no claims):

- Sakai, H. (2001). "Rational surfaces associated with affine root
  systems and geometry of the Painlevé equations." Commun. Math.
  Phys. 220(1), 165-229. DOI: 10.1007/s002200100446.
- Okamoto, K. (1979). "Sur les feuilletages associés aux équations
  du second ordre à points critiques fixes de P. Painlevé." Japan.
  J. Math. 5, 1-79.
- Jimbo, M.; Miwa, T. (1981). "Monodromy preserving deformation of
  linear ordinary differential equations with rational coefficients.
  II." Physica D 2(3), 407-448.
- Its, A.; Kapaev, A. (2003). "Quasi-linear Stokes phenomenon for
  the Painlevé first equation." J. Phys. A 36(15), 4263-4283.
- Kac, V. (1990). "Infinite-Dimensional Lie Algebras," 3rd ed.,
  Cambridge University Press. Chapter 4. (Source for the D_6^{(1)}
  Cartan matrix.)
- Internal: NON-110708 (V_quad numerical data only).

## Open questions for next session

- Whether the POC-vs-KNY comparison documented in
  `claim-r1-sakai-nongen-001` should be promoted from "computational"
  evidence to a textual statement in any consolidation note. Out of
  scope for the POC.
- Whether the Stokes constant value should be captured by a separate
  data card sourced from `pcf-research/vquad/` rather than from the
  v1.1 brief context. Deferred to operator.
- Whether the V_quad value should be extended beyond the 31-digit
  pcf-spectral-classes record by importing from
  `pcf-research/vquad/` (with its own source_commit field).
  Deferred to operator.
- Whether `refs.md` should be extended to cite KNY 2017
  (arXiv:1509.08186v8) which is used by the cycle-1 substrate but
  not the POC layer. Currently kept POC-scoped.
- The original `Next session candidates` list in `README.md` was
  written for the cycle-1 successor and the items there have been
  partially addressed by cycles 1, 2, 3a, 3b; the residual is
  Weyl-orbit reproduction of the full real-root set (open).

## Anomalies

- Stokes constant S = 0.43770528 supplied in the v1.1 brief context
  is NOT stored in `pcf-spectral-classes` at the source_commit. The
  canonical workspace location is
  `pcf-research/vquad/scripts/t2_iter22_s_precision.json` (S_best =
  0.43770528073458051568, derived from Dingle late-terms, iter22).
  The 8-digit value in `stokes_table.json` matches the brief and the
  workspace value to its precision. Does not affect POC
  verification_criteria. Status: documented in claim and in
  `stokes_table.json`; not a halt condition.
- The pre-existing `stokes_table.json` recorded a 60-digit V_quad
  whose digits past position 32 are not present in
  `pcf-spectral-classes` at any commit. The file has been rewritten
  to record only the 31-digit value that IS present in
  `pcf-spectral-classes/pcf_spectral_phase1_taxonomy.csv` (row
  vquad-3-1-1). v1.1 no-from-memory rule respected.
- `claim-r1-poc-001.json` was pre-registered on 2026-05-19 without
  the v1.1 amendment fields `evidence_class_locked` or the two
  v1.1-specific `out_of_scope` entries. Those fields are backfilled
  in the `v1_1_audit` block of the claim with explicit disclosure.
- The verifier output SHA256 is bit-identical to cycle 1's hash.
  This is correct and meaningful (substrate stability) rather than
  a copy-paste error; noted explicitly in the claim's
  `hash_coincidence_note`.
- README's `Last run` line previously said "31/31 tests passed";
  this audit updates it to reflect the current 147/147 reality and
  to clarify that the 116 cycle-1+ tests are out of scope for the
  POC criteria.
