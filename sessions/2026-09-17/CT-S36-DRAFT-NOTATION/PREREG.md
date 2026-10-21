# PREREG.md — CT-S36-DRAFT-NOTATION

Session type: **drafting**. Two of the three tasks produce prose and LaTeX and
have no observable to pre-register. The third, the 171-item check, has a
pre-registered control and is registered here.

## 0. Why a PREREG exists at all for a drafting session

`S24-07` set the precedent that a drafting session with no computation writes
no PREREG rather than back-filling a vacuous one, and `CT-S23-OUTSIDER-READ`
did the same. CT-S36 differs in one respect: task 3 requires a check *that can
fail*, and the task names a control. A check with a control is an instrument,
and its control must be fixed before it is run. Only §3 below is a genuine
pre-registration; §1 and §2 record that nothing is pre-registerable.

## 1. Task 1 — Proposition U into `theorem.tex`

No observable. The success condition is stated by the task itself: the file
compiles with no undefined references. Reported with old and new sha256.
Nothing here can be tuned after the fact, because the proof is transcribed from
`CT-S26-UPPER-BOUND/PROOF.md` and claim `S26-01`, not derived here.

## 2. Task 2 — §1 as paper prose

No observable. The task enumerates what §1 must define; task 3's coverage arm
is what turns that enumeration into something checkable.

## 3. Task 3 — the 171-item check

**Hypothesis.** §1 as drafted defines, before first use, a substantial part of
the vocabulary the isolated reader of CT-S23 found used-before-defined, and the
remainder is enumerable.

**Observable.** For each of the 171 items in
`CT-S23-OUTSIDER-READ/outputs/coldread_main.txt` task 2, one of
`DEFINED IN SECTION 1` / `DEFINED ELSEWHERE` / `STILL UNDEFINED`.

**The STILL UNDEFINED count is the output, not the falsifier.** A large count
is a finding about the state of the material, not a failure of the session, and
is reported as such. There is no threshold on it and none may be introduced
later.

**Falsifiers, each with a numeric threshold.**

| # | Falsifier | Threshold |
|---|---|---|
| F1 | A ruling of `DEFINED IN SECTION 1` whose declared anchor string is absent from `section1.tex` | any occurrence, count ≥ 1 → exit 1 |
| F2 | A definition the session task names explicitly is absent from §1 | any occurrence, count ≥ 1 → exit 1 |
| F3 | The rulings table does not cover exactly 171 items | ≠ 171 → exit 1 |
| F4 | Reader-integrity assertion fails | any occurrence → exit 1 |

**Pre-registered control (required by the task).** Item **054**, *“apparent
singularity”*, is deliberately left undefined in §1 and **must be reported
`STILL UNDEFINED`**. If it is ever reported otherwise, the check exits 1. This
is declared here, before the check is run to completion, and is not to be
changed.

**Vacuity pre-check.** The observable must move when the thing the hypothesis
is about moves. `scripts/mutants_171.py` damages §1 or the item list one way at
a time and requires the check to exit 1 *for the stated reason*, rejecting any
arm that merely crashed the script. Per P0 Amendment E the damage is chosen
from outside the check's own anchor list: arms M1–M4 delete subsections or a
hypothesis of §1, named by their prose headings. If any arm reports MISSED, the
check is not sensitive to the material and the result is void.

**Reader integrity (P0 Amendment C).** Before any absence is reported, the
check asserts known-present features of both inputs, two of them non-ASCII
(`ξ₀`, `β_k`, `D̃₅`), so a mis-decoded or empty read cannot pass as a clean
result. An undecodable input is reported in the same words as any other failure
to see the content, never as a traceback.

## 4. Halt conditions

Unchanged from P0. In addition: if a falsifier fires, the finding is reported
and the *ruling* is corrected, never the check.
