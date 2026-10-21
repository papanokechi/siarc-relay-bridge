# PREREG — CT-S35-CTV17-ITEM6

Written **before** the splice and before either gate was run in this session.
Draft only. No deposit, no metadata edit.

## 1. Hypothesis

A sixth item can be added to the v1.7 notice which states a three-tier result
about the formal type of `L_d`, such that **the tier of every load-bearing
sentence is recoverable from the published text itself**, and such that the
four required qualifications survive publication:

* Q1 a matching Katz multiset is a **necessary condition only** — the procedure
  excludes rows and assigns none;
* Q2 the notice asserts **no Painlevé label for `V_quad`**;
* Q3 the record's own label history is **stated on both sides and not
  adjudicated** — `P-III(D₆)` (v1.0–v1.3) inside the surviving set,
  `P_V/D₅^(1)` (v1.4, conjectural at v1.5) outside it — with the reason a row
  exclusion is not a row assignment;
* Q4 every tier marker is **in the prose**, not only in a heading.

## 2. Observable

The pass/fail vector of `scripts/verify_description.py` over the regenerated
`DESCRIPTION-v1.7-rev3.html`, and of `scripts/preflight_deposit_rev2.py` over
the deposit packet.

Four checks are added for the four qualifications, and each must be able to
fail:

| check | fails when |
|---|---|
| `N5` | a tier is missing, or a tier marker appears only in a heading and not in the prose |
| `N6` | the necessary-condition/assigns-none statement is absent, or a sentence assigns a row, or a Painlevé label is asserted for `V_quad` |
| `N7` | the label history is stated on only one side, or is adjudicated |
| `N8` | a superseded description hash is published, or the current hash/md5 is absent from the packet |

## 3. Falsifiers, with thresholds, fixed before running

* **F1.** `verify_description.py` reports `checks failed > 0` or
  `broken checks > 0`. Threshold: **any non-zero count**.
* **F2.** Any of `N5`–`N8` has **fewer than 2** can-fail mutants, or any mutant
  is **accepted**. Threshold: **mutants rejected must equal mutants offered,
  and that count must be ≥ 2 for each of the four.**
* **F3.** `preflight_deposit_rev2.py` returns anything other than
  `GATE: PASSED`, with `checks failed = 0` and `broken checks = 0`.
* **F4.** Any quotation of Table 2.1 in §7 disagrees with the page image at its
  printed folio in any cell. Threshold: **one cell**.
* **F5.** The published description still contains the superseded hash
  `026e7a9e…` or the superseded `39903126…` as a *current* value.

If a falsifier fires, stop and report; do not adjust the threshold.

## 4. Vacuity pre-check

Each of the four new checks is only meaningful if it moves when the thing it is
about moves. Per **Amendment E**, the mutants must not be drawn from the
checks' own required-string lists, since a mutant built from the list can only
show the list is consulted.

* **N5** — mutant: move a tier marker out of the prose and into a heading only.
  If N5 still passes, it is testing the heading, not the sentence.
* **N6** — mutant: append a sentence assigning a row
  (*"`L_d` is therefore a `PIII(D₈)` connection."*). If N6 still passes, it is
  testing a disclaimer rather than the conduct.
* **N7** — mutant: append a sentence adjudicating the history
  (*"the v1.4 correction was therefore mistaken"*), and separately delete the
  `P-III(D₆)`-inside-the-set half so the history is one-sided. If N7 still
  passes, it cannot distinguish a balanced statement from a verdict.
* **N8** — mutant: reinstate a superseded hash as a current value.

**Known-present assertion (Amendment C).** Every check reads the description
only after asserting a known-present feature including a **non-ASCII** one; an
absence reported by a reader that did not read is not a finding.

## 5. What would make this session report a finding rather than a result

* A required qualification that **cannot** be expressed as a failing check.
  Report it as unenforced rather than claiming it is enforced.
* A Table 2.1 cell that cannot be read confidently from the image. Report the
  cell, do not infer it.
* A tier that, on drafting, turns out not to be separable from the tier above
  it. Report the merge rather than publishing a false separation.

## 6. Budget

≤ 1 day. Halt and report if exceeded, or if any halt condition in P0 occurs.
