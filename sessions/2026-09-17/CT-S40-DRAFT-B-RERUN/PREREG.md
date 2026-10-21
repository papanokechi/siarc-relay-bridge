# PREREG — CT-S40-DRAFT-B-RERUN

Written **before** any script in this session was run. Thresholds fixed here
are not revised after seeing results; if one proves ill-posed that is reported
as a finding, in the form CT-S37 used for its own `MIN_PAIRS` amendment.

## 1. Why this session exists

CT-S37-DRAFT-B drafted §3 and §4 and checked them, but its check ran while two
of its inputs were wrong:

- **§2 did not exist.** §3 and §4 cite the growth section; the check could not
  tell a correct cross-reference from a dangling one.
- **§1 was the pre-repair copy.** CT-S38 repaired three collisions in §1 (the
  ρ sentence, `Q`, `s`). `CT-S37-DRAFT-B/refs/section1.tex` is 13 660 B; the
  repaired file is 14 325 B. Group B was therefore checked against a §1 that no
  longer exists.

Both are now available, so the check is re-run against them.

Three further actions are carried from the operator's ruling and `S39-08`:

1. drop the `CT-` prefix alias from `draft_check.py`;
2. invert mutant `M7`, so the bare short form must now **fail**;
3. remove the `NOTE` at `draft_check.py:195–196`, which asserts that
   `OUTLINE.md` cites the family as `S9-PVPARAMS-*`. CT-S38 fixed the outline,
   so that sentence is now **false**.

**This session does not edit CT-S37-DRAFT-B.** Its `claims.jsonl` cites the
digest of its own `draft_check.out.txt`, and editing the script in place would
strand it. The scripts are copied here and amended in the copy, which is the
same reasoning that left the alias alone at the time.

## 2. Hypothesis

With §1 repaired and §2 present, §3 and §4 remain correct: every cited claim id
resolves in the corpus **without alias assistance**, every label asserted in the
prose matches the label the corpus record carries today, no cited claim is
structurally superseded, and every cross-reference out of §3 and §4 resolves
against the real §1 and §2 rather than a stub.

## 3. Observables

- **O1** — resolution and label verdicts from `draft_check.py`, alias removed.
- **O2** — the alias census: how many citations resolved *only* via the alias in
  CT-S37, and how many do so now. The prediction is **zero in both**, i.e. the
  alias was already dead code at the time it was retained.
- **O3** — undefined references and multiply-defined labels in a build of
  §0 §1 §2 §3 §4 together.
- **O4** — whether the repaired §1 changed anything §3 or §4 depends on:
  every `\ref`/`\eqref` target used by §3/§4 and defined in §1 must still exist
  in the repaired file.

## 4. Falsifiers, with thresholds

- **F1** `UNRESOLVED + SUPERSEDED + MISMATCH > 0` in §3/§4 → FAIL.
- **F2** any citation resolves only via the `CT-` alias → the alias was **not**
  dead code and dropping it is a behaviour change, not a cleanup. Report and
  halt; do not re-add it silently.
- **F3** the combined build reports **any** undefined reference, or any
  multiply-defined label → FAIL.
- **F4** any `\ref`/`\eqref` target that §3 or §4 takes from §1 is absent from
  the **repaired** §1 → FAIL. (This is the one the CT-S37 run could not see.)
- **F5** `OUTLINE.md` still contains a bare `S9-PVPARAMS-` occurrence not
  preceded by `CT-` → the outline fix did not land; the NOTE must stay.
- **F6** any mutant arm is MISSED → the controls do not bound the check.

Reader-integrity bounds are inherited from CT-S37 unchanged (`MIN_BYTES` 4000,
`MIN_SUBSECTIONS` 4, `MIN_PAIRS` 5 per file / 30 across the group). They are
bounds, not fingerprints, per `S36-09`.

## 5. Vacuity pre-checks

Every falsifier gets an arm that makes it fire. The nine CT-S37 arms are kept,
with `M7` **inverted**, and three are added:

- **M10** — an `\eqref` in §3 pointed at a label absent from §1 and §2; F3 must
  fire in the build.
- **M11** — `OUTLINE.md` staged with a bare `S9-PVPARAMS-C005`; F5 must fire.
- **M12** — the repaired §1 replaced by the stale CT-S37 copy; the §1-provenance
  check must fire. Without this arm, "checked against the repaired §1" is a
  claim about a file path, which is the `S35-16` failure.

`M7` inverted is the **boundary mutant** for the alias removal: it asserts the
bare form is now refused, not quietly resolved.

## 6. Self-exclusion (the `S34` ordering trap)

`draft_check.py` walks every `claims.jsonl` under `sessions/`, and this session
writes one. Any claim citing the gate's output digest would go stale the moment
the gate is re-run. As in CT-S38 and CT-S39, `claim_index.build()` is amended to
**exclude this session's own `claims.jsonl` by construction**, and the exclusion
is asserted non-vacuously: the file must **exist** and be **absent** from the
walk. Gate ordering is then not something that has to be remembered.

## 7. What this session does NOT establish

- It does not re-derive any formula in §3 or §4. A transposed digit inside an
  equation passes every check here. Unchanged from CT-S37 and CT-S39.
- It does not re-read the primary literature behind §3/§4; that was CT-S37's
  scope.
- It does not renumber or rewrite §3 or §4. They are copied **unmodified**; if
  the check fails, the failure is the output.
