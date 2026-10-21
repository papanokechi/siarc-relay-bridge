# P0 amendments A–D — RULED

**Status: all four ADOPTED, 2026-09-19, by operator ruling.** C was adopted as
amended, with the non-ASCII sentinel sub-clause folded into the clause text.

P0 is pasted per session and has no canonical file in this repository, so
"adopted" means: **§ADOPTED TEXT below is pasted into the preamble of every
subsequent session.** That is the whole of the action authorised. This document
does not edit either originating file.

The operator's ruling, recorded verbatim:

> **A and B** (from CT-S22-STOKES): approve as written. The search-space
> degeneracy rule and the transit manifest both earned their place on live
> defects.
>
> **C** — approve, with the non-ASCII sentinel sub-clause folded in. State it
> as: a check that reads a file must assert a known-present feature, including
> at least one non-ASCII character where the file has one, before evaluating any
> absence.
>
> **D** — approve. It has now earned its keep twice before being ruled on: the
> five stale statements, and the 28-versus-27 keyword count.
>
> That clears the backlog. Don't let a fifth accumulate unruled.

On finding 2, also recorded because it names the asymmetry the C clause exists
to break:

> a check that confirms your own hypothesis from an empty search produces no
> symptom. D2 walked the wrong root, found nothing, and would have reported
> "blocker confirmed" — the answer you already believed. Only the mandatory
> known-present assertion turned it into a FAIL. That's the asymmetry: a check
> that disagrees with you gets investigated, a check that agrees doesn't.

**Backlog: empty. Nothing is now PROPOSED and unruled.**

> **Superseded the same day, and in the intended way.** A fifth amendment did
> arise — **E, mutant provenance** — and was ruled on in the round it was
> proposed rather than accumulated. See `P0-AMENDMENT-E.md`: **ADOPTED**.
> Amendment C was **extended** in the same ruling with the symmetry bullet.
> The backlog is again **zero**.

| | amendment | P0 section | origin | ruling |
|---|---|---|---|---|
| **A** | basis degeneracy pre-check | PRE-REGISTRATION | `CT-S22-STOKES` Stage 5A | **ADOPTED as written** |
| **B** | artefact hashing is terminal | AEAL RECORD | `CT-S24-PAPER-OUTLINE` rev 2 | **ADOPTED as written** |
| **C** | reader integrity | PRE-REGISTRATION | `CT-S26-CTV17-DRAFT` | **ADOPTED as amended** (sub-clause folded in), **extended** same day with the symmetry bullet |
| **D** | deposited text is authoritative | GOVERNANCE | `CT-S26-CTV17-DRAFT` | **ADOPTED as written** |
| **E** | mutant provenance | PRE-REGISTRATION | `CT-S27-CTV17-DEPOSIT-PREP` (`X2`; `P1` without `P2`) | **ADOPTED** — see `P0-AMENDMENT-E.md` |

**Originals, not superseded by this file** — each carries its full evidence
section and its own "why it is not redundant" table:

- A and B: `sessions/2026-09-17/CT-S22-STOKES/P0-AMENDMENT.md`
- C and D: `sessions/2026-09-17/CT-S26-CTV17-DRAFT/P0-AMENDMENT.md`

Those two files still read **PROPOSED**, which is correct: they record what was
proposed and the evidence for it. **This file is where the ruling lives.** The
paste-ready text is `P0-ADOPTED-ABCD.txt`, generated from the clause blocks
below and byte-checked against them.

---

## Why these four and not a fifth

Each of the four was written after a defect that **passed every check then in
force**. That is the admission threshold: an amendment is warranted only when
the existing rules were followed and the defect survived them.

- **A**: Stage 5A's vacuity pre-check reported the required *3 decoys rejected,
  1 control accepted* and **passed for the wrong reason**.
- **B**: the claims were hashed, as required. The artefact then moved.
- **C**: the check's logic was correct and its mutants all fired. Its **reader**
  was wrong, and a broken reader rejects the mutant too — so the control class
  in force could not reach it.
- **D**: a repository-wide search was run correctly and returned the correct
  answer *about the repository*. The conclusion drawn was about the corpus.

They are also mutually non-overlapping: A is about the space searched, B about
when a pointer is taken, C about the input path of a check, D about which copy
of a text is primary. No two of them would have caught each other's defect.

---

## Amendment A — basis degeneracy pre-check

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

**Cost if ruled in.** One extra PSLQ run per search, at the same bound. The
Stage 5B implementation took minutes.

---

## Amendment B — artefact hashing is terminal

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

**Cost if ruled in.** Extra output files accumulate. That is the intended
trade: this session already has `verify_notice.out.txt`,
`verify_notice_rev2.out.txt` and `verify_notice_rev3.out.txt` side by side, and
`preflight_deposit.out.txt` alongside `preflight_deposit_r2.out.txt`, because
each is cited or is evidence of a catch.

---

## Amendment C — reader integrity

Append to P0 under PRE-REGISTRATION, after the vacuity pre-check clause:

```text
- READER INTEGRITY. A check that reads a file must verify that it read the
  file, before it evaluates anything about the contents:
    * Assert at least one KNOWN-PRESENT feature (a title line, a required
      section heading, a character set the file is known to contain) and abort
      on failure. Only then evaluate any known-absent or count-based
      condition. Where the file contains non-ASCII text, at least one asserted
      feature MUST contain a non-ASCII character: an ASCII-only sentinel set
      survives a wrong-codec read intact and cannot detect it.
    * Where the check reports an ABSENCE, the known-present assertion is
      mandatory, because "content missing" and "my reader could not see it"
      produce identical output otherwise. This is most dangerous when the
      absence CONFIRMS the hypothesis: a check that disagrees with you gets
      investigated, a check that agrees does not, so an empty search that
      returns the expected answer produces no symptom at all.
    * The requirement is SYMMETRIC. A reader that misses a real defect and a
      reader that manufactures a phantom one are the same failure, and the
      phantom is worse if acted on: it spends a round correcting text that was
      already correct. So a check must verify it read the file CORRECTLY, not
      merely that it read something, and a finding must be confirmed against
      the raw artefact before it is treated as a defect.
    * Control the reader as well as the content: run the same check through at
      least one deliberately defective reader (wrong codec, no newline
      normalisation, truncated input) and require it to be CAUGHT. Mutant
      testing verifies a check's logic; it cannot verify its input path,
      because a broken reader rejects the mutant too.
    * Normalise line endings once, in one place, immediately after decoding.
```

**Adopted as amended.** The first bullet's non-ASCII requirement and the second
bullet's confirming-absence sentence are the folded-in additions; the rest is
the proposed text unchanged. Both additions are evidenced in this session —
`S27-03` (the latin-1 control that would not fire) and `S27-04` (`D2`
confirming its own hypothesis from an empty search of the wrong directory).

**Extended 2026-09-19, by operator ruling, with the symmetry bullet.** The
occasion was `S27-19`: an audit reported 85 space-before-punctuation defects in
the description, of which the raw HTML contains **zero** — the audit's own
tag-stripping substitutes a space for each tag and so manufactured every one.

> a reader that *invents* a defect is Amendment C in reverse, and 85 phantom
> findings from your own tag-stripping is the same cost as missing 85 real ones
> — worse, if acted on. C's clause could carry the symmetry: a check that reads
> a file must verify it read it correctly, in both directions.

C as originally proposed was one-directional: it guarded against a reader that
cannot see what is there. The symmetry bullet closes the other direction. Both
are the same underlying requirement — *the check's picture of the file must be
the file* — and separating them would have invited the same defect to be
rediscovered under a new name.

This is the fourth instance of *the control must be able to reach the thing it
controls*, after: a mutant that only reaches prose cannot control a check that
reads a record (`R9`); a mutant targeting a line-wrapped string inside a
blockquote is not a mutant at all; and a drop-sensitivity arm cannot test an
instrument on an overdetermined system.

---

## Amendment D — deposited text is authoritative

Append to P0 under GOVERNANCE:

```text
- DEPOSITED TEXT IS AUTHORITATIVE. For any work this corpus has deposited, the
  deposited record is the primary source and the working tree is a copy that
  may be behind it.
    * Before writing any version notice, erratum, or statement of the current
      state of a deposited work, FETCH the deposited text of every version you
      intend to characterise, store it under refs/ with bytes and sha256, and
      quote from that. A version notice written without reading the record it
      amends is not verifiable.
    * Where repository material and deposited text disagree, the record is
      authoritative and the repository copy is stale, unless you can show the
      reverse. Mark the stale copy so it is not carried forward.
    * A repository-wide search establishes absence FROM THE REPOSITORY. Never
      report it as absence from the corpus. Say which artefact was searched.
    * Prior session records may also live outside the worktree; check those
      before treating a citation as unsourced.
```

**Amendment D earned its keep again, in this session, before being ruled on.**
The pre-flight's `C4` compared `DEPOSIT-FORM.md`'s declared keyword count
against the held v1.6 record: the form said **28**, the record has **27**. The
28 had been carried forward from an earlier version and never checked against
the deposited text. Metadata rather than prose, but the same class and the same
direction of error: **the working copy was stale and the record was right.**

---

## The paste-ready text

`P0-ADOPTED-ABCD.txt` holds the four adopted clauses and nothing else — no
commentary, no evidence, no markdown — so it can be pasted into a session
preamble without editing. It is **generated** from the four ```text blocks
above by `scripts/emit_p0_adopted.py`, which extracts them and asserts each
extracted block is byte-identical to the corresponding block in this file. It is
not maintained by hand, so the two cannot drift.

**Backlog status: empty.** Nothing is PROPOSED and unruled. Any fifth amendment
should be ruled on when it arises rather than accumulated.

> **And one did, the same day.** Amendment **E** (mutant provenance) was
> proposed and **ADOPTED** in a single round, which is the behaviour this
> paragraph asked for. Amendment **C** was extended with the symmetry bullet in
> the same ruling. Backlog remains **zero**. See `P0-AMENDMENT-E.md`.
