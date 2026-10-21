# catalog_d2 status annotation (added 2026-09-13 by FILTRATION-NOGO)

`catalog_d2.csv` is NOT modified and must not be. Its sha256 is
`45074eb04841547ed7250bba9386bb5b0eddaa0a4a9c898b993059a87a88155e`, which is the
`output_hash` of claim line 1 in this session's `claims.jsonl`, recorded
`reproducible: true`. Editing it in place would silently invalidate that claim.

`catalog_d2.STATUS_ANNOTATED.csv` is a derived copy. Every pre-existing column
and value is byte-identical; it adds three columns beside `known_reduction`:

  known_reduction_status   RETRACTED | (empty when no label)
  known_reduction_as_of    2026-06-01
  known_reduction_source   the retraction chain

Only one row carries a label: `V_quad -> P_III(D6)`. That label's sole anchor was
CT v1.3 Thm 3.3.D, retracted by ct15 v1.4 (2026-06-01) and corrected to a
CONJECTURED `P_V/D_5^(1)` correspondence whose parameter point has
`delta = -1/2 != 0`, so it is **not** a `P_III(D6)` reduction. The original
column has no status field, which is why the withdrawal could not travel with
the label.

Consumers should read the annotated copy. Known inheritor as of 2026-09-13:
`tc3/artifacts/family_select.json` (V_quad row, `is_F_ref: true`).

## The inheritor list is as-of, not standing

`tc3/artifacts/family_select.json` is the known inheritor **as of 2026-09-13**.
That is a measurement, not a property: anything that consumed the label after
that date is not in it, and a stale inheritor list fails in exactly the way the
label itself did. Re-derive rather than trust it.

Re-run `recheck_inheritors.py` (beside this file) at correction-batch time. It
carries its own predicate and prints the set with its as-of; it changes nothing.

Predicate: a file mentioning `P_III(D6)`/`P_III(D_6)` within +-900 characters of
a `known_reduction` key or the ten-family / whole-catalogue / Conte-Musette
result, and carrying no caveat marker in that window. Caveat markers must
include `necessary-criterion` as well as `necessary condition` -- omitting the
hyphenated form produced a false positive on 2026-09-13.
