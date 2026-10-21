# Cross-tree session-number collisions

Recorded 2026-09-19 under ruling 4 of CT-S34-CHECKER-RULINGS.
**Nothing is renamed by this note.** Renaming a folder rewrites paths that
claims already cite, which is the defect this note exists to avoid.

## The collision

Two trees carry session folders numbered in one sequence:

- `C:\LocalWork\siarc-relay-bridge\sessions\<date>\CT-Sn-*`  (git-tracked)
- `C:\LocalWork\SCOPE\CT-Sn-*`                               (out of tree)

Two numbers exist in both, with different contents:

| number | repository tree | SCOPE tree |
|---|---|---|
| `CT-S32` | `sessions/2026-09-17/CT-S32-LD2-ORDINARY-LOCUS` | `C:\LocalWork\SCOPE\CT-S32-PACKET-SEALED` |
| `CT-S33` | `sessions/2026-09-17/CT-S33-CHECKER-SCOPE`      | `C:\LocalWork\SCOPE\CT-S33-COLDREAD-OUTPUT` |

A citation of the form "CT-S32" or "CT-S33", or of a claim id `S32-nn` /
`S33-nn`, is therefore **ambiguous by number alone**. Both trees mint claim ids
from the same `S<n>-<nn>` pattern, so the ambiguity reaches the claim ids and
not only the folder names.

## Disambiguation rule for existing citations

Cite by **full path**, or by folder name including the suffix
(`CT-S33-CHECKER-SCOPE`, never bare `CT-S33`). The suffixes are distinct, so
no existing artefact needs editing; only bare-number citations are ambiguous,
and any that appear in a deposited file must be expanded before deposit.

## Convention adopted going forward

New sessions in `C:\LocalWork\SCOPE` take the prefix **`SC-Sn`**, with claim
ids `SC-n-nn`. New sessions in the repository keep `CT-Sn`. The two sequences
then cannot collide, and a bare number identifies its tree.

This applies to sessions created **after** this note. `CT-S28`, `CT-S29`,
`CT-S30`, `CT-S31`, `CT-S32-PACKET-SEALED` and `CT-S33-COLDREAD-OUTPUT` keep
their names; several are already cited.

## Why this is a note and not a repair

The collision is a **citation hazard**, not a corruption: every folder is
internally consistent and every claim resolves against the path it was written
under. The hazard materialises only when a number is cited without its tree.
Recording it costs nothing and rewrites nothing; renaming would invalidate
citations in `CT-S32-LD2-ORDINARY-LOCUS` and in the CT-S33 report, both of
which quote paths.

## Related

`C:\LocalWork\SCOPE` is not walked by `check_invariants.py` (CT-S34 ruling 4).
Its exclusion is printed on every run with three reasons, one of which is this
collision. Restoring it to `ROOTS` requires all three to be settled, of which
adopting `SC-Sn` settles only the third.

`C:\LocalWork\SCOPE\CT-S31-COLDREAD-ROWS` is under a standing instruction not
to be read, written, listed or deleted. It is excluded separately and by name.
