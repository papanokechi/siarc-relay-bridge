# PREREG.md — CT-S1-THEOREM (P4)

## 0. Scope and honesty note on ordering

P4 Task A (writing `theorem.tex`) is **not** a computation: it is a proof draft,
and it produces no numerical observable. P0's pre-registration requirement is
aimed at computations, so no hypothesis/falsifier is meaningful for Task A. What
*is* pre-registered for Task A is the **labelling rule** (§1).

P4 Task B involves two mechanical checks (a LaTeX compile and a `lake build`).
Their success criteria are stated in §2 and §3.

**Ordering disclosure.** The `lake build` and the `pdflatex` run were executed
before this file was finalised. The criteria in §2 and §3 are the standard,
binary, pass/fail criteria for those tools; **no criterion was chosen or
adjusted after seeing the result**, and both are recorded here exactly as they
would have been stated in advance. This disclosure is made because P0 requires
pre-registration and the literal ordering was not honoured.

## 1. Labelling rule for Task A (fixed in advance)

For each numbered step of each proof I record exactly one of:

* **complete** — the step is fully argued from stated hypotheses and results
  cited as standard-and-classical;
* **gap** — the step relies on a result that is quoted without proof, or an
  estimate that is asserted without derivation.

Then:

* a result with **zero** gaps is labelled **PROVEN**;
* a result with **one or more** gaps is labelled **STRUCTURAL**, and every gap
  is listed explicitly with an identifier.

This rule is applied mechanically. In particular, numerical agreement from
sessions `CT-S2-RHO-D4` and `CT-S3B-RINF` may be cited as corroboration but
**may never** convert a gap into a completed step, nor upgrade a label.

## 2. Success criterion — LaTeX (Task A deliverable)

`pdflatex -interaction=nonstopmode -halt-on-error theorem.tex` terminates with
exit code 0 and writes `theorem.pdf`. Binary; no threshold.

## 3. Success criterion — Lean (Task B)

`lake build` in `lean/` reports **`Build completed successfully`** with:

* **zero** errors;
* warnings **only** of the form `declaration uses 'sorry'`.

Binary; no threshold. A build that succeeds is evidence that **the statements
typecheck** — that the definitions and theorem statements are well-formed Lean
and that the Mathlib names they use exist. It is **not** evidence that anything
is proved. No `sorry`-free claim will be made.

## 4. Mathlib inventory rule (fixed in advance)

A Mathlib lemma may be listed as **CONFIRMED** only if its exact name was found
by searching the Mathlib source tree actually installed in this session
(`lean/.lake/packages/mathlib/`), with the file and line recorded. Anything not
found that way is recorded as **NOT FOUND**, even if I believe it exists.
No name is written from memory.

## 5. Halt conditions specific to P4

* If `op:xi0-singularity-type` or the "v1.6 vacuity finding" cannot be located
  in the repository, **do not invent a citation**: state the scope remark on its
  own terms and flag the missing identifiers for the operator. (Per
  `CT-S0-INVENTORY/REPORT.md` §3 items 4 and 5, both are in fact absent, so this
  branch is taken.)
* Do **not** edit the Channel Theory source, in this or any other session.
