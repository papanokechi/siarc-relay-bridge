# Handoff — R1-ROUTE-F-POC
**Date:** 2026-05-19
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~75 minutes
**Status:** COMPLETE

## What was accomplished
Built a proof-of-concept scaffold for Route F of R1 (the Sakai
surface-machinery route to the V_quad / PIII(D_6) chart-map
problem). Implemented the D_6^{(1)} affine root system as integer
vectors in Z^8 (7 simple roots, Cartan matrix, null root, finite
real-root predicate) and the Pic(X) intersection form for
X = Bl_{8 pts}(P^1 x P^1) in the generic configuration, with a
candidate D_6^{(1)} simple-root embedding orthogonal to -K_X.
31 unit tests pass; the reproduce command runs to exit code 0
and reports `"surface_type": "D6_affine"`. No claim was made
about closing R1, the V_quad correspondence, or the Stokes
constant.

## Key numerical findings
- All 7 candidate simple roots in Pic(X) have intersection -2
  with themselves and 0 with -K_X. Script: `sakai_d6/surface.py`.
- Pairwise Gram matrix of the 7 candidate simple roots equals
  the D_6^{(1)} symmetric Cartan form (corank 1, fork on each
  end of an A_3 spine). Script: `sakai_d6/surface.py`.
- Intersection form on Pic(X) (rank 10) is unimodular.
  Script: `sakai_d6/surface.py`.
- The supplied 7x7 Cartan matrix of D_6^{(1)} matches the
  matrix derived from the bilinear form on the simple roots in
  Z^8. Script: `sakai_d6/root_system.py`.
- The finite real-root set of D_6 has exactly 60 elements, each
  recognised by `is_root`. Script: `sakai_d6/root_system.py`.
- All evidence is computational; no precision-sensitive
  calculations were performed (the artefacts in `vquad_data/`
  were copied verbatim from prior workspace files; no new digits
  were generated).

## Judgment calls made
- The brief specified Z^8 for the affine root system; I embedded
  the 7 simple roots and the null root in Z^8 using six
  epsilon-basis coordinates, one slot for delta, and one padding
  slot reserved for the level grading. The padding slot is zero
  on every simple root and on delta, so the choice does not affect
  any test outcome.
- The brief said `is_root` "returns True/False on the finite set."
  I interpreted "finite set" as the set of finite real roots of
  the underlying D_6 inside the affine system, i.e. the 60
  vectors of the form +/- e_i +/- e_j (1 <= i < j <= 6). The
  module also exposes `finite_real_roots()` enumerating them.
- The brief said "8 base points on P^1 x P^1 as configurable
  parameters." I exposed `BASE_POINTS` as a Python list of 8
  generic affine pairs, but the lattice check itself is purely
  combinatorial on Pic(X) and does not consume the base-point
  parameters. This is documented in the module docstring.
- I chose the embedding of the 7 D_6^{(1)} simple roots in
  Pic(X) by direct constraint-solving (require each root to be
  -2 self-intersection, orthogonal to -K_X, and reproduce the
  D_6^{(1)} Dynkin adjacencies). The resulting embedding is
  recorded in `sakai_d6/surface.py::d6_affine_simple_roots`;
  notably alpha_3 = H_2 - H_1 is not effective. This is fine
  for the POC and consistent with how Sakai-style simple roots
  appear in Pic(X), but I did not verify literature alignment.

## Anomalies and open questions
- The chosen embedding uses the generic intersection form (8
  base points in general position). The Sakai PIII(D_6) surface
  actually requires a non-generic (infinitely-near) configuration
  with a different intersection form. The candidate roots used
  here would have to be re-verified, or a different embedding
  found, against the non-generic form. This was flagged in
  `README.md` under "Next session candidates" and is left for
  follow-up.
- The middle node alpha_3 = H_2 - H_1 is not an effective class;
  some literature conventions write the D_6^{(1)} simple roots
  as effective (-2)-curve classes. Whether the two conventions
  are related by a Weyl reflection or by a different choice of
  geometric configuration is left for follow-up.
- I did not verify that the rank-7 sub-lattice spanned by the
  candidate roots is saturated inside the orthogonal complement
  of -K_X (the orthogonal complement has rank 9; the candidate
  lattice has rank 7). Saturation is a non-trivial check left
  for follow-up.

## What would have been asked (if bidirectional)
- Is the intended verification target the generic Pic(X) form, or
  the Sakai non-generic form for PIII(D_6)? The brief said
  "generic" implicitly by asking for "8 base points as
  configurable parameters" without specifying a Sakai
  configuration; I went with generic and recorded the open
  question.
- Is the convention `alpha_3 = H_2 - H_1` (non-effective)
  acceptable, or should the embedding use only effective
  (-2)-curve classes? I went with non-effective because it gave
  a valid -2 / K-orthogonal / D_6^{(1)}-Cartan candidate without
  forcing the non-generic intersection form.

## Recommended next step
Replace the generic Pic(X) intersection form in `surface.py` with
the Sakai non-generic form appropriate to PIII(D_6) (8 base points
configured as 4 pairs of infinitely-near triples along the two
rulings, per Sakai 2001 §8). Either re-verify the candidate
embedding against the non-generic form, or run a constraint search
for a new embedding and document the comparison. Keep the scope
limited to "the embedding compiles and passes tests against the
non-generic form" — do not move toward V_quad mapping in that
next session.

## Files committed
- README.md
- refs.md
- halt_log.json
- discrepancy_log.json
- unexpected_finds.json
- COMPLETION_REPORT.md
- claims/claim-r1-poc-001.json
- claims.jsonl
- sakai_d6/__init__.py
- sakai_d6/root_system.py
- sakai_d6/surface.py
- sakai_d6/tests/__init__.py
- sakai_d6/tests/test_root_system.py
- vquad_data/stokes_table.json
- handoff.md (this file)

## AEAL claim count
1 entry pre-registered (`claims/claim-r1-poc-001.json`),
verified by the reproduce command. The same claim is also
recorded in `claims.jsonl` with SHA-256 output hash
`c3410c895eceb0dd5d7c3d6baacbec690cd5816b138576b9a47fd8b99617c9a3`
over the UTF-8 stdout of `sakai_d6/surface.py --verify-lattice`.
