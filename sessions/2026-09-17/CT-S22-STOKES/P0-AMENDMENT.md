# Proposed P0 amendments

This file carries **two** proposed amendments to P0:

- **Amendment A — basis degeneracy pre-check** (§§1–6 below). Origin:
  `CT-S22-STOKES` Stage 5A.
- **Amendment B — artefact hashing and checker re-runs** (§7 below). Origin:
  `CT-S24-PAPER-OUTLINE`.

Status: **PROPOSED**, both. Operator-gated. P0 is pasted per-session and has no
canonical file in this repository; this document is the amendment text plus the
evidence that motivated it, so a future session can paste it verbatim.

---

# Amendment A — basis degeneracy pre-check

Origin: `CT-S22-STOKES`, Stage 5A. See `PREREG-STAGE5B.md` §4.1 for the
implemented form and `REPORT.md` §2.2 for the full analysis.

---

## 1. The gap in the existing rule

P0 currently says, under PRE-REGISTRATION:

> a vacuity pre-check (confirm the observable actually moves when the data the
> hypothesis is about moves).

That rule points **outward**: it asks whether the observable is coupled to the
structure under test. It is the right question for a transport, a perturbation,
or a fit.

It does not cover the case where the *instrument itself* is degenerate. An
integer-relation search does not merely observe a target; it searches a space of
its own construction. If that space contains a relation **among its own
generators**, the search can return that relation — with **coefficient zero on
the target** — and the target is never tested. Every outward-facing check still
passes, because the machinery is working exactly as designed on a space that
cannot answer the question.

This is a distinct surface from "a check that cannot fail". The check here
*could* fail, and did fail for three decoys. It simply failed for a reason
unrelated to the hypothesis.

## 2. The proposed clause

Append to P0 under PRE-REGISTRATION:

```text
- BASIS DEGENERACY PRE-CHECK. If the method searches a space you constructed
  (integer-relation/PSLQ/LLL over a basis, an ansatz with chosen generators, a
  fit over chosen predictors), you must test that space for internal relations
  BEFORE consulting the target, and pre-register the test:
    * Run the identical search on the basis with the TARGET REMOVED. It must
      return NO relation, at the same bound and tolerance the real search will
      use. A relation here means the space is degenerate: the search cannot
      test the target and any result it returns is VOID, not negative.
    * Treat a returned relation whose coefficient on the target is ZERO as a
      degeneracy detection, never as a rejection or a negative result.
    * State in the pre-registration which generators are known to be
      multiplicatively or linearly dependent and why the remainder are not.
  A vacuity pre-check tests the observable against the structure; this tests
  the search space against itself. Passing the first does not imply the second.
```

## 3. Why it is not redundant with any existing P0 line

| existing rule | what it catches | why it missed this |
|---|---|---|
| vacuity pre-check | observable not coupled to structure | the observable *was* coupled; the space was degenerate |
| falsifier with a numeric threshold | result inside tolerance by construction | the threshold was fine and never reached |
| "controls as assertions that can fail" | checks that cannot fail | this check *did* fail, for three decoys, for the wrong reason |
| "never upgrade a label" | prose inflation | the label was correct; the *result* was void |

## 4. The evidence

In Stage 5A the pre-registered basis was

```
[ log C, log 2, log 3, log pi, log Gamma(1/3), log Gamma(1/6), 1 ]
```

PSLQ returned, for the target `C` **and for all three decoys alike**, the
identical relation

```
-2 log2 + 3 log3 - 3 log(pi) + 12 log Gamma(1/3) - 6 log Gamma(1/6) = 0
```

whose coefficient on `log C` is **zero**. The cause is proved in
`scripts/gamma16_identity.py` (residual `1.69e-80`): Legendre duplication at
`z = 1/6` with reflection at `1/3` gives

```
Gamma(1/6) = 2^(2/3) sqrt(3) Gamma(1/3)^2 / (2 sqrt(pi))
```

so `log Gamma(1/6)` was never an independent generator.

**The failure mode in one line.** Stage 5A's vacuity pre-check reported the
required "3 decoys rejected, 1 control accepted" and therefore **PASSED FOR THE
WRONG REASON**: the decoys were rejected because PSLQ handed back a `C`-free
relation, not because the space discriminates between a true closed form and a
false one.

Had the basis been degenerate in a way that *also* swallowed the control, the
run would have produced a confident, fully-documented, entirely false NOT FOUND.

## 5. Handling, for the record

Stage 5A was **withdrawn as VOID and left unedited** — `PREREG-STAGE5.md` and
`scripts/stage5_pslq.py` are retained as the record of the void search, per that
pre-registration's own terms. The correction was written as a **separate**
pre-registration, `PREREG-STAGE5B.md`, which removes the redundant generator,
**loosens no bound**, and adds the missing falsifier as §4.1. Stage 5B's
degeneracy pre-check passed, all decoys were rejected on their own merits, the
control was recognised at cost 1.51, and the NOT FOUND it returned is genuine.

## 6. Scope note for any future Stage-5-like search

Gamma values at rational arguments are riddled with multiplicative relations
(duplication, reflection, Gauss multiplication). Any enlargement of the search
space — `Gamma(1/4)`, `Gamma(1/12)`, higher-degree algebraics over `Q(sqrt 3)`,
`zeta(3)`, polylogarithms — requires **its own** pre-registration **and its own
degeneracy pre-check**. The check is cheap; the failure it prevents is silent.

---

# Amendment B — artefact hashing and checker re-runs

Status: **PROPOSED**. Origin: `CT-S24-PAPER-OUTLINE`, revision 2. See that
session's `REPORT.md` §3.

## 7.1 The gap in the existing rule

P0 currently says, under AEAL RECORD:

> Every numerical claim must trace to a script in the session folder and a
> hashed output file.

It fixes **what** must be hashed and says nothing about **when**. A hash is a
pointer, and the rule as written permits taking the pointer while the target is
still moving. It also treats the checker as if it stood outside the system it
checks — but a checker writes an output file, that file gets hashed, and
**re-running the checker silently invalidates every hash pointing at its
output**. No invariant check catches this, because the checker does not police
its own artefact.

## 7.2 The proposed clause

Append to P0 under AEAL RECORD:

```text
- ARTEFACT HASHING IS TERMINAL. A claim's output_hash must be taken only after
  the artefact it points at is FINAL. Specifically:
    * Re-running a checker, or any script, invalidates every hash already
      pointing at its output. After any re-run, either re-point every affected
      claim or write to a NEW output filename; do not leave a stale hash.
    * Prefer writing to a new versioned filename over overwriting. A hash that
      resolves to nothing is worse than an extra file, and the previous
      content is unrecoverable once overwritten.
    * Never pipe a checker through a tee-style redirect onto a path that an
      existing claim already cites.
    * A script must read back what it wrote, and the hash must be computed
      from the file on disk, not from the in-memory string.
  The checker does not police its own output. Nothing else will catch this.
```

## 7.3 The evidence

Claims `S24-01`…`S24-07` carried `output_hash a3bab67a…` for
`CT-S24-PAPER-OUTLINE/outputs/verify_outline.out.txt`. Re-running

```powershell
python scripts\verify_outline.py | Tee-Object outputs\verify_outline.out.txt
```

overwrote that file. The new content hashed `fe5657ba…`. **Seven hashes then
resolved to nothing, and the revision-1 output was unrecoverable.**

It was caught on read-back, not by any checker — `check_invariants.py` verifies
label/evidence consistency across the corpus and has no visibility into whether
a hash still resolves. Repaired by re-pointing all 11 claims and correcting
`S24-01`'s stale section count, which had also gone stale in the same edit.

## 7.4 Why it is not redundant with any existing P0 line

| existing rule | what it catches | why it missed this |
|---|---|---|
| "hashed output file" | unhashed numerical claims | the claim *was* hashed — to a superseded artefact |
| "every script reads back what it wrote" | a script that wrote nothing or wrote wrong | the script wrote correctly; a *later* run clobbered it |
| "controls as assertions that can fail" | checks that cannot fail | the control passed; its recorded output was gone |
| invariant check | label/evidence mismatch | has no visibility into hash resolution |

## 7.5 Relation to an existing corpus rule

This is the same surface as the standing rule *never overwrite a hashed output
file that an existing claim already cites*. Amendment B states it as a P0 clause
and extends it in one direction the earlier form did not cover: **the checker's
own output is an artefact like any other**, and the act of re-checking is
itself a mutation.
