# pcf-r1-route-f

Proof-of-concept scaffold for Route F of the chart-map closure
problem R1, attached to the V_quad / PIII(D_6) thread. This
directory implements just enough of the Sakai surface machinery
to verify that the D_6^{(1)} affine root system and the Pic(X)
intersection form compile and pass unit tests.

What this is
------------

A POC. Concretely:

* `sakai_d6/root_system.py` — D_6^{(1)} affine root system: 7
  simple roots and the null root delta as integer vectors in Z^8,
  a 7x7 Cartan matrix, and `is_root(v)` deciding membership in the
  finite real-root set.
* `sakai_d6/surface.py` — Pic(X) for X = Bl_{8 pts}(P^1 x P^1)
  in the generic configuration: the 10x10 integer intersection
  form, the anti-canonical class, a candidate embedding of the
  D_6^{(1)} simple roots, and `surface_type()` which reports
  ``"D6_affine"`` iff the candidate roots are orthogonal to -K_X
  and their pairwise intersection matrix matches the expected
  D_6^{(1)} symmetric Cartan form.
* `sakai_d6/tests/` — 31 unit tests covering the above.
* `vquad_data/stokes_table.json` — V_quad numerical data reproduced
  verbatim from prior workspace artefacts. No new digits computed.
* `claims/claim-r1-poc-001.json` — pre-registered AEAL claim.
* `refs.md` — citations only.

What this is NOT
----------------

* This does not construct the V_quad parameter correspondence.
* This does not derive the Stokes constant.
* This does not close R1 in any form, in part or in whole.
* The 8 base points on P^1 x P^1 are exposed as configurable
  parameters but are not used by the lattice check; the lattice
  check is combinatorial on Pic(X).

Reproduce
---------

From the workspace root (with the workspace's venv activated):

    cd pcf-r1-route-f
    python -m pytest sakai_d6/tests/ -v
    python sakai_d6/surface.py --verify-lattice

Last run: 31/31 tests passed; surface verifier returned
``"surface_type": "D6_affine"`` with exit code 0.

Next session candidates
-----------------------

Open questions that came up during this POC and that are out of
scope for any subsequent work on this scaffold:

* Replace the generic Pic(X) intersection form with the Sakai
  non-generic (infinitely near) configuration that physically
  corresponds to the PIII(D_6) surface, and confirm that the
  candidate roots above still embed (or substitute a configuration
  that does).
* Compare the candidate simple-root embedding here to the
  Sakai 2001 / Kajiwara-Noumi-Yamada conventions and document any
  isomorphism explicitly.
* Add a sanity check that the orthogonal complement of -K_X in
  Pic(X) ⊗ Q has rank 9 and that the rank-7 sub-lattice spanned by
  the candidate simple roots is saturated.
* Add a Z-basis check: verify the rank-7 sub-lattice with its
  symmetric form is isomorphic (as a Z-lattice) to the abstract
  D_6^{(1)} root lattice from `root_system.py`.
* Implement the Weyl-group action by simple reflections and check
  that orbits of the simple roots reproduce the full set of real
  roots in a bounded test.
