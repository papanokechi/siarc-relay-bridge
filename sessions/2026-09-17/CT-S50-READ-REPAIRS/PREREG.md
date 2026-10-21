# PREREG — CT-S50-READ-REPAIRS

## 0. What this session does

Applies the operator's rulings on the fourteen findings of `CT-S49-FULLREAD`.
This is an **execution session**: the findings were established and confirmed
elsewhere, and the decisions are the operator's. What is pre-registered here is
not a discovery but the **standard by which a repair counts as landed**.

## 1. Hypothesis

Each ruling can be applied to the source without breaking the build, without
changing any mathematical content, and without leaving the pre-repair text
anywhere in the tree.

## 2. Observable

For each repair, a **three-sided predicate**:

- **NOW** — the repaired text is present in the live tree;
- **GONE** — the pre-repair text is absent from the live tree;
- **SNAPSHOT** — the pre-repair text *is* present in `refs/`, a copy taken
  before any edit.

Plus, globally: the build page count and undefined-reference count.

## 3. Falsifiers

- **F1.** Any repair whose NOW side fails: the edit did not land.
- **F2.** Any repair whose GONE side fails: the edit landed somewhere but the
  old text survives elsewhere, which is worse than not editing — the paper
  would then say both things.
- **F3.** Build regression: fewer than 39 pages, or any undefined reference.
- **F4.** Any figure printed into §9.4 or §B.5 that does not resolve to an
  anchored line of the route manifest. Figures are not transcribed from the
  ruling; the ruling is checked against the evidence.

Thresholds are exact-match. None is tunable.

## 4. Vacuity pre-check

The SNAPSHOT side **is** the vacuity check, and it is a refusal condition, not
a warning: if the pre-repair text is not in `refs/` either, then "GONE" is
satisfied by a reader that cannot see the string at all, and the repair is
unverifiable. The script exits 2 in that case rather than reporting success.

For the symbol index, the control is `C1`: the screen must show that **`b`** —
the letter whose omission motivated it — is multi-role, was unnamed by any
`\item` head before this session, and is named now. If `C1` does not fire the
screen cannot see its own motivating defect, and any census it prints is
uninterpretable. Refusal, not a warning.

## 5. Advance prediction

I expect the instruments, not the paper, to be the source of trouble. The
repairs are short and local; the checks involve needles over LaTeX, which has
broken a reader in this run five times. **Specifically, I expect at least one
control to go DEAD or one needle to miss because of case, wrapping, or a
LaTeX command being read as a letter.**

*(Recorded before either script was run. Outcome: three reader defects, zero
paper defects — `G6` case-sensitivity, and two in the item-head extractor,
`\beta_k` read as `b` and the search running into the item body. The
prediction named the class correctly and one of the three mechanisms.)*

## 6. Scope limit

- Only the twelve ruled items are repaired. `CT-S49` findings 11–13 are
  queries and are **not** touched.
- No mathematical content is changed. Multiset repairs change how a multiset is
  *written*, never which invariants it records.
- `CT-S45-FORMULA-A` and every earlier session are **read-only**. The sources
  are copied here; nothing upstream is edited.
