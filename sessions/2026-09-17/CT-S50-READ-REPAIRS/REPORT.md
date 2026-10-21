# REPORT — CT-S50-READ-REPAIRS

Executing the operator's rulings on the fourteen findings of `CT-S49-FULLREAD`.

---

## 0. Result

```
BUILD         39 pages, 0 undefined references, 0 multiply-defined labels
REPAIRS       25 checks, 0 FAILED; 19 controls, 19 FIRED
SYMBOL INDEX  31 multi-role letters; control FIRED
```

Fourteen rulings applied across nine files. Every repair is verified three ways:
the new text is **present** in the live tree, the pre-repair text is **gone**,
and `refs/` — a pre-repair snapshot taken before any edit — **still carries**
the old text. The third side is the `S38-07` snapshot guard: without it,
"the old text is absent" cannot be distinguished from "my reader cannot see
it", and a repair that was never needed would pass silently.

---

## 1. Finding 1 — the stale disclaimer

The ruling was to rewrite rather than delete, and to use *re-derived* in the
strict sense. Both sites now carry the routed census, and each figure was
resolved against the manifest before it was printed, not transcribed from the
ruling:

| route | count | anchored at |
|---|---|---|
| S-here (re-derived symbolically) | 21 | `CT-S46…/outputs/manifest.out.txt:3` |
| S-corpus (traced to a claim) | 15 | `…:4` |
| P (verified against the page) | 9 | `…:5` |
| DEF (definitional) | 11 | `…:6` |
| UNROUTED | 0 | `…:7` |

with `census=56 manifest=56` on line 1. The residual **twelve** is derived,
not asserted: the manifest's fifteen `S-corpus` rows include exactly three at
`section5.tex L117/L122/L127` (claim `S16-12`), which are the §5 `q` and `p`
that `CT-S47` re-derived per coefficient. 15 − 3 = 12. Check `G6` recomputes
this rather than matching the word "twelve" alone.

§9.4 item 6 now also drops the false clause that Appendix A's formulas were
"transcribed from page images rather than computed" — Appendix A's own closing
note says both routes were exercised there, which is what made the two
passages contradict.

**A note on what was *not* changed.** Appendix A's closing note stands as
drafted. The contradiction is resolved by correcting the sections that were
stale, not by softening the section that was right.

## 2. The remaining rulings

| # | ruling | where | id |
|---|---|---|---|
| 2 | the self-contradicting count, fixed by counting correctly | §8.7 | `R2` |
| 3 | the phantom quotation replaced by what §5.3 actually shows | §5.4 | `R3` |
| 4 | `R` unified to §1's typography | §6.2, §9.1 | `R4a/b` |
| 5 | the declared scalar form made the one in use | §1 | `R5` |
| 6 | `b` entered in the reuse list, with all four meanings | §1 | `R6` |
| 7 | `b_1` defined at first use, §6.3 no longer load-bearing | §5.3, §6.3 | `R7` |
| 8 | `s_1,s_2` → the declared `a_1,a_2` | §7.3 | `R8` |
| 9 | the Katz dash convention widened; all multisets 4-slot | §1, §3, §4, §0, §5, §9 | `R9a–d`, `G1` |
| 10 | the counterexample kept in §6.1, referenced from §10.1 | §10.1 | `R10` |

Three of these needed a fact checked before the edit could be made honestly:

- **`R8`.** `section7.tex:170` states `a_i = tr(B_i) ≡ 2`. The value `2` is
  `a_i`'s, so `s_1=s_2=2` is a surviving symbol from an earlier draft, not a
  third meaning of `s`. The rename is therefore a correction, not a choice.
- **`R9c`.** Writing System A's multiset with four slots asserts that both the
  `r(1)` and `r(t)` points are absent. `section3.tex:32` states `z=0` is its
  **only** finite singular point (`S4-05`), so `(½,−,½,−)` is read off the
  paper, not supplied.
- **`R7`.** `eq:fam-b` is affine in `z` — its first term is linear, its second
  constant — so "the coefficient of `z` in the entry `b`" is well defined and
  `b_1=0` does say `b` is constant. Checked in the display before writing it.

## 3. The instrument finding

The operator asked that `R` in four typographies be recorded as an instrument
finding and not only a prose repair. It is sharper than "the pass missed two
sites":

**`S44-05` is literally accurate.** It claims that *section 3's* normal
potential was unified to section 1's form — and it was. What the notation pass
never did was ask where else `R` occurs. Its items were scoped by **where a
collision had been noticed**, which came from a read of §3 and §6, so §9's
`R=P^2/4+P'/2-Q` was never in view.

So the defect is not a false claim but an **unswept scope**: a pass that
repairs the instances it was told about, and reports success in those terms,
leaves a reader with no way to tell a swept symbol from a spot fix. The same
shape explains `b` — §1's reuse list had six entries because six collisions
had been noticed, not because six letters are reused.

`scripts/symbol_index.py` is the sweep that was missing. It classifies every
single letter by **syntactic role** (`CALL` `x(·)`, `SUB` `x_k`, `BARE` `x`)
across all thirteen section files, and reports the 31 letters in two or more
roles across two or more sections, flagging those no `\item` head in §1 names.

It is deliberately a **census, not a gate**. Two syntactic roles need not mean
two meanings, and §1 declares some reuse in prose outside the list — `P`/`Q`
against `Q_n`, `s` against `s_±` — which an item-head reader cannot see. Making
it fail on the 26-letter residue would be a threshold tuned to an answer. What
it does assert is narrow and controlled: **`b` was in two roles across four
sections, was named by no item head before this session, and is named now.**

This failure class is written up as
`P0-AMENDMENT-H-UNSWEPT-SCOPE.md`, **ADOPTED 2026-09-21 by operator ruling**.
It is not covered by the existing amendments: A–G each guard whether a check
can *fire*, and `S44-05`'s check fired perfectly and reported truthfully. What
went wrong is upstream — the **item list** came from the report rather than
from the artefact, so the question "where else does `R` occur?" was never asked
and so could never fail. The amendment requires a sweep to state where it
*looked*, and distinguishes "X was unified in §3" from "X is unified", which
only a census can support.

**The ruling added one clause**, and it is the operative half: when a repair
pass is commissioned from a reported list, its **first act** is to sweep for
the same defect elsewhere, and the sweep's result is part of the output
*whether or not it finds anything*. Both halves are load-bearing. A sweep run
*after* the reported items are repaired is written from inside the reported
list and inherits its shape — the defect reintroduced at the point meant to
catch it. And a null result that need not be printed makes an empty sweep
indistinguishable from an absent one, which is this run's non-vacuity rule in
another costume. `S44-05` would have failed the clause: its output named no
scope, so nothing in the record separated "§6 and §9 were checked and are fine"
from "§6 and §9 were never looked at". They were never looked at.

The adoption is recorded as `S50-12`, which carries `supersedes: S50-06`;
`S50-06`, written while the amendment was PROPOSED, stands unedited. The
emitter now reads the amendment file as evidence and refuses unless its head
declares `ADOPTED`, its body carries the commissioning clause, and the claim
it supersedes exists. Four control arms in a scratch tree at repo-relative
depth: an unmutated baseline **writes**, reverting the status to `PROPOSED`,
deleting the clause and superseding a nonexistent `S50-99` each **refuse at
exit 2 for exactly the injected reason and no other**, and restoring writes
again. The live `claims.jsonl` was byte-identical before and after.

A first attempt at those arms is itself worth recording: the scratch copy was
made at an arbitrary temp path, so `ROOT = HERE.parents[2]` did not resolve and
**the baseline refused too**. All three arms still printed their injected
reason and would have been scored CAUGHT — refusing for a reason that had
nothing to do with the mutation. Only the A0 baseline exposed it. An arm that
checks for its reason string in the output, without a baseline that passes,
cannot tell a fired control from a broken one.

### Two reader defects, both caught by the control refusing

Writing that screen reproduced the run's most persistent hazard twice, in the
same function:

1. The item-head regex matched `\beta_k` and returned the Latin **`b`**, so the
   pre-repair list appeared to name `b` already. Same atom-blindness as
   `coeff(sqrt(11))` against the `sqrt(33)` atom.
2. With that fixed, the search still ran past the head into the item **body**,
   where the `β` entry's prose mentions `$b(n)$` — and returned `b` again.

Both times the control `C1` went **DEAD** and the script **refused (exit 2)**
rather than printing a census. Had it merely warned, a screen that cannot see
its own motivating defect would have reported 26 candidates and looked
productive. A third reader defect — a case-sensitive needle for "the remaining
twelve" against §9's "The remaining twelve" — failed `G6` on the first repair
run.

Three reader defects, zero paper defects, in one session's instruments.

## 3a. The three open items, closed

The operator ruled on all three. Two required an edit; the third required
looking at the page.

**`\nameref` in §10.1 — the instinct was right, and it was worse than
predicted.** Checked against the rendered text rather than the source, it
produced:

> set out at **What is false (S17-02, PROVEN)** (S17-02, PROVEN), is trivial
> after tensoring with itself…

`\nameref` pulls the *whole* paragraph title, and that title already carries
its citation — so the reference read as a title where a number was meant **and**
printed `(S17-02, PROVEN)` twice. Replaced by `\ref`, which now renders:

> the 2-torsion object $L=\partial-\tfrac{1}{2z}$ of §7.1 (S17-02, PROVEN) is
> trivial after tensoring with itself but not before…

This is the first check in the run whose subject is only visible **after
typesetting**: the source was well-formed, the build was clean, every reference
resolved, and the defect existed solely in the rendering. Checks `G7`–`G9` are
therefore run against `pdftotext` output, with a control requiring that the
page reader *can* see paragraph titles — otherwise "no doubled citation" would
be satisfied by a reader blind to titles altogether.

**§1's "Seven further letters".** Dropped, as ruled: the list now opens *"The
following letters are reused"*. The count was unverifiable by the letter screen
because `β` is Greek, and removing it removes a figure nothing checks rather
than leaving one that must be maintained by hand. `G9` confirms no letter count
survives on the page.

**The 26 candidates.** Left as a census in the record, and the census was
**re-run after these further prose edits**: 31 multi-role letters, 26 unnamed,
control fired — unchanged, so the recorded figure still matches the text.

## 4. Claims

| id | label | subject |
|---|---|---|
| `S50-01` | `INSPECTED` | §9.4 and §B.5 rewritten; the routed census with its anchored figures |
| `S50-02` | `VERIFIED` | 25 checks / 19 controls, every repair snapshot-guarded |
| `S50-03` | `VERIFIED` | 39 pages, 0 undefined references |
| `S50-04` | `INSPECTED` | `a_i=tr(B_i)≡2` establishes `s_1,s_2` as a draft residue |
| `S50-05` | `INSPECTED` | System A's singular set is `{0,∞}`, so `(½,−,½,−)` is read off |
| `S50-06` | `STRUCTURAL` | the unswept-scope finding; `S44-05` accurate, its pass not exhaustive |
| `S50-07` | `INSPECTED` | the symbol index: 31 multi-role letters, 26 unnamed, reported as candidates |
| `S50-08` | `VERIFIED` | the two item-head reader defects, caught by `C1` refusing |
| `S50-09` | `CONJECTURED` | the 26-letter residue is a candidate list, not a defect list |
| `S50-10` | `INSPECTED` | the `\nameref` defect, visible only in the rendering, and its repair |
| `S50-11` | `STRUCTURAL` | a source-level check cannot see a typesetting defect |
| `S50-12` | `INSPECTED` | amendment H adopted, with the commissioning clause; supersedes `S50-06` |

## 5. What was NOT established

- **The three queries of `CT-S49` (findings 11–13) are untouched.** The
  p. 2655 / p. 2629 attribution conflict, §10's "no section sets up", and
  §7.1's "performed" all stand exactly as reported. They need the page images
  or a ruling, not an edit. The operator's position of 2026-09-21: they were
  raised as **queries rather than defects**, so unless the pen-and-paper
  sitting turns one into a defect, a decision to leave them is a legitimate
  close. No instrument work is owed on them.
- **The 26-letter residue has not been adjudicated.** Most are certainly
  innocent. Which are not is a reading question.
- **No mathematics was re-checked.** Every edit is to prose, notation or
  cross-reference. `R9b`–`R9d` change how multisets are *written*, not which
  invariants they record; `G1` confirms no 3-slot form survives.
- **The end-to-end read by a person is still owed.** This session repaired what
  an assisted read found. It did not look again.

## 6. Open questions for the operator

None outstanding. All three items raised in the first pass were ruled on and
are closed in §3a above — the `\nameref` rendering was checked against the
page and replaced, §1's unverifiable count was dropped, and the census was
re-run against the edited text and is unchanged. Amendment H was ruled on and
is **adopted**, with the commissioning clause folded in (§3).

`CT-S49`'s findings 11–13 are not open questions for an instrument: they are
queries the sitting either turns into defects or closes.

What remains is not an instrument's work: the paper has still never been read
as a piece of writing — whether the argument arrives in the right order,
whether §9's limits are the ones a referee would ask about, whether the
introduction promises what the paper delivers. After that, a venue decision,
shaped by the arXiv endorsement barrier and the absence of an affiliation —
deliberately a separate conversation, not the tail of a session.

## 7. Uncommitted files

All new. **No file outside this session was created or modified**; the sources
were copied from `CT-S45-FORMULA-A`, which is untouched.

```
sessions/2026-09-17/CT-S50-READ-REPAIRS/
  PREREG.md  REPORT.md  claims.jsonl
  P0-AMENDMENT-H-UNSWEPT-SCOPE.md   ADOPTED 2026-09-21 by operator ruling
  *.tex                          the repaired paper (15 files)
  refs/*.tex                     pre-repair snapshot (15 files)
  scripts/check_repairs.py
  scripts/symbol_index.py
  scripts/emit_claims_s50.py
  outputs/check_repairs.out.txt
  outputs/symbol_index.out.txt
  outputs/paper_text.txt         the rendering, for the page-level checks
  paper.pdf  paper.log           39 pages
```
