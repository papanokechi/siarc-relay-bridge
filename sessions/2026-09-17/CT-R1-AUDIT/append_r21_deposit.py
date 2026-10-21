"""Append the R21b reference-bytes section to DEPOSIT-DEPENDENCIES.md."""
import os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DEPOSIT-DEPENDENCIES.md')
MARK = '## R21b — the reference bytes, and what the deposit-day pass must not assume'

with open(P, encoding='utf-8') as f:
    before = f.read()
assert MARK not in before, 'already present'

SEC = """
""" + MARK + """

*No support row moves. This section is here because the deposit-day citation
pass reads this file, and two of its standing assumptions were wrong.*

**1. The manifest existed only as a decision.** `REFS-LICENCE-REVIEW.md`
recommended committing a manifest of hashes rather than the reference bytes.
The recommendation was adopted in prose and cited afterwards as though it were
in force. No manifest file existed, and no `.gitignore` anywhere above
`CT-S1-THEOREM/lean/` excluded anything. `REFS-MANIFEST.md` now exists: path,
byte length, full sha256 for all **69** files under `refs/` and `pages/`.
`sessions/2026-09-17/.gitignore` now makes the exclusion mechanical, verified by
`git add --dry-run` — 391 paths stageable, exactly one of them under `refs/`
(a script written in this run, re-admitted by an explicit negation), zero
third-party bytes. Claims `R1-105`, `R1-107`.

**2. The inventory the gate reads is incomplete.** **40 of 69** third-party
files have **no row** in `REFS-LICENCE-REVIEW.md`; the whole of
`CT-S8-LITCHECK/refs/` and `CT-S9-PVPARAMS/refs/` had never been enumerated,
including seven complete third-party articles. The hold's wording covers them —
*"everything under any `refs/` directory"* — so nothing was exposed, but wording
is not machine-readable and the table is. Claim `R1-106`.

### What this means for the deposit-day pass

- Treat `REFS-MANIFEST.md`, not `REFS-LICENCE-REVIEW.md`, as the population.
  The review is the *assessment* of a subset; the manifest is the *census*.
- Every row is **NOT CHECKED** until its licence is read **on the item itself** —
  the article's own title page, the arXiv abstract page for *that submission*
  (the licence is per-submission and the default grants no redistribution
  right), or the Zenodo record's `metadata.rights` fetched with
  `Accept: application/vnd.inveniordm.v1+json`. The status of a publisher, a
  venue, or a neighbouring row clears nothing.
- The AIF title page reads *tous droits réservés*. Free to **read** is not free
  to **redistribute** (fourth amendment). That position is unchanged.
- Nothing here licenses a deposit of any reference file. The deposit is the
  companion, not the references.
"""

with open(P, 'a', encoding='utf-8') as f:
    f.write(SEC)

with open(P, encoding='utf-8') as f:
    after = f.read()
assert MARK in after and 'R1-106' in after and 'NOT CHECKED' in after, 'readback failed'
print('DEPOSIT-DEPENDENCIES.md %d -> %d lines' % (before.count('\n'), after.count('\n')))
print('READBACK OK')
