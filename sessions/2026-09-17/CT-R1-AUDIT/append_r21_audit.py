"""Append the R21 section to AUDIT.md. Writes, reads back, asserts."""
import os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AUDIT.md')
MARK = '## R21 — the seventh amendment, and the manifest that did not exist'

with open(P, encoding='utf-8') as f:
    before = f.read()
assert MARK not in before, 'section already present'
n0 = before.count('\n')

SEC = """
""" + MARK + """

*Operator review #19 asked for one thing: that S17-22 be lifted out of the sixth
amendment's consequence clause and written into P0 as its own line. Doing that
was half an hour. Checking the round's own commit-readiness claim, which was the
other half of #19, took the rest and produced two findings that were not on
anyone's list.*

### The seventh amendment

Written at `P0-CITATION-RULE.md` §Seventh amendment. The operator's framing is
the one adopted: the earlier family was **steps that could not fail**, and this
is a **step that could not succeed**. Both certify nothing, and the second is
worse, because it arrives as a confident negative verdict that looks like a
finding. CT-S18's ERROR read as a real defect for two rounds and cost two
further cold packets to clear.

The diagnostic, in one line: *what would this test have returned had the claim
been true?* If the answer is the same thing, the test has not been run.

Claim `R1-102`, STRUCTURAL.

### A false claim in this round's own record — `R1-103`

`R1-103` was written to close #19's commit-readiness item. It said:

> *"`refs/` is excluded mandatorily under the licence hold (fourth amendment)
> and `lean/.lake/` for size; both exclusions were re-verified at this round's
> backup, which included 454 files and skipped 124116 excluded paths."*

**The first half is false.** `make_backup.py` carries
`EXCLUDE_DIRS = {".lake", "__pycache__", ".git"}` and no `refs` entry; the
archive holds **34** `refs/` paths. The clause *"both exclusions were
re-verified"* describes a verification that never happened — and it is the
seventh amendment's own failure mode in miniature, an assertion about a check
whose result was assumed from its plausibility.

What makes it worth recording rather than quietly fixing is *why* it was caught:
the sentence **named a mechanism**, and naming a mechanism invites reading it.
Had it said only "the backups are safe", nothing would have prompted opening the
script.

The error is a conflation of two holds that had been running under one word:

| hold | what it governs | is it in force? |
|---|---|---|
| retain locally | the backup archive | `refs/` **is** included — correct and intended |
| do not redistribute | commit, deposit | was **not** mechanised at all |

A backup that omitted the reference bytes would defeat its own purpose. The hold
is about redistribution. So the claim was not merely unverified — it named the
wrong side of the distinction. Amended in place under the R20 precedent (backup
to `.bak-r21b`, prior text quoted above, provenance note inside the claim text,
label unchanged, amendment itself claimed as `R1-104`). No downstream claim had
cited it.

### The finding underneath: the manifest route was a decision, not an artefact

Checking the redistribution side turned up something larger.
`REFS-LICENCE-REVIEW.md` recommended committing **a manifest of hashes** instead
of the reference bytes. The recommendation was adopted in prose, cited in later
rounds as though in force, and described to the operator as one of the two
things standing between the record and a bad `git clean`. In fact:

- **no manifest file existed** anywhere under `sessions/2026-09-17/`;
- the repository has **no root `.gitignore`**;
- the only mechanical exclusion in the tree was `CT-S1-THEOREM/lean/.gitignore`,
  covering the Lean build directory, for size and not for licence.

So a `git add sessions/` on the morning of R21b would have staged **all 69**
files under `refs/` and `pages/` — including the whole-page *Annales de
l'Institut Fourier* renders and the Gautschi page image, the two items the
review names explicitly as DO NOT COMMIT. The hold was carried entirely by the
intention of whoever next typed the command.

`REFS-MANIFEST.md` now exists: path, byte length and full sha256 for all 69, the
artefact the route had only ever named. Claim `R1-105`.

### And a gap in the inventory the deposit gate reads

Building it exposed a second gap. **40 of the 69** third-party files have **no
row** in `REFS-LICENCE-REVIEW.md`. The whole of `CT-S8-LITCHECK/refs/` and
`CT-S9-PVPARAMS/refs/` had never been enumerated — among them seven *complete
third-party articles* rather than page regions (Gautschi 1967, Perron 1913,
Nemes 2025, Wang JAT 2014, `polycf`, `bt1933`, Jimbo 1982 PRIMS), their
extracted-text derivatives, and fifteen page images under
`CT-S16-MEMBERSHIP-C/pages/`.

Nothing was exposed: the hold's wording reads *"everything under any `refs/`
directory"*, which covers them. What failed is that **the wording and the
inventory diverged, and only the inventory is machine-readable**. Every one of
the 40 is recorded **NOT CHECKED**. No licence determination was made for any
file this round, and none will be made except by reading the licence on the item
itself. Claim `R1-106`.

### The mechanism, verified by effect

`sessions/2026-09-17/.gitignore`, written at R21b. Patterns exclude directory
*contents* rather than the directories (`**/refs/*`, `**/pages/*`) precisely so
that a negation can re-admit session-produced scripts (`!**/refs/*.py`) — git
cannot re-include a file whose parent directory is excluded.

Verified by `git add --dry-run`, which stages nothing and is reversible:
**391** paths would be added, of which **exactly one** lies under `refs/` or
`pages/` — `CT-R1-AUDIT/refs/parse_dlmf.py`, written in this run and re-admitted
by the negation. `git ls-files --others --ignored` reports **97** ignored paths.
Zero third-party bytes would be staged. Claim `R1-107`, VERIFIED.

This is preparatory and reversible. **Nothing was committed.**

### Two counting failures, and an extension to the fifth amendment

`git check-ignore -v` printed the *negation* pattern for `parse_dlmf.py` while
still **exiting 0** — which reads as IGNORED and is the reverse of the truth. A
tool's exit status is not its answer; the dry run settled it.

Worse, a PowerShell statement that invoked `git add -n` twice in one line and
counted the second reported **7** stageable paths against a true **391**. It
exited zero. Seven is *plausible*, and it would have supported the conclusion
that almost nothing was stageable — the exact opposite of `R1-105`. It was
caught only by re-running the enumeration alone. Two counts given to the
operator earlier in the round (*71 files*) were also wrong; the figure is **69**.

The fifth amendment is extended accordingly: **the readback rule covers counts,
not only writes.** A quantity that will be reasoned from is re-derived in a
separate invocation, and a plausible number is the dangerous case — an
implausible one gets checked. Claim `R1-108`.

### Position

Claims **344 in 21 files**, all identifiers unique, all five invariants pass.
Deposit position unchanged at **48 of 49**, `R1-57` the sole remainder. The R21b
findings are about the *record's own handling*, not about any deposited claim,
so no support row moves.

### Queue

Items 3, 4 and 5 — the deposit-day citation pass and the companion v1.3 deposit,
the vdPS letter, the Wong–Li purchase — remain **operator actions** and were not
performed. Nothing was committed, deposited, sent or bought. Committing the
session tree is now *safe to attempt*, in the narrow sense that the held bytes
can no longer be staged by accident; whether to commit remains the operator's
call.
"""

with open(P, 'a', encoding='utf-8') as f:
    f.write(SEC)

with open(P, encoding='utf-8') as f:
    after = f.read()
assert MARK in after, 'section absent after write'
for probe in ('R1-108', 'manifest route was a decision', '**69**', 'NOT CHECKED'):
    assert probe in after, 'missing %r' % probe
print('AUDIT.md %d -> %d lines' % (n0, after.count('\n')))
print('READBACK OK')
