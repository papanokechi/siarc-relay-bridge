# Proposed P0 amendments — `CT-S26-CTV17-DRAFT`

This file carries **two** further proposed amendments to P0. It does **not**
restate or supersede the two already pending in
`sessions/2026-09-17/CT-S22-STOKES/P0-AMENDMENT.md` (Amendment A — basis
degeneracy pre-check; Amendment B — artefact hashing and checker re-runs), both
of which remain **PROPOSED** and operator-gated. Amendments are lettered
consecutively across files so that a future session can paste A, B, C and D in
order.

- **Amendment C — a check that reads a file must verify it read it.**
  Origin: `CT-S26-CTV17-DRAFT`, revision 1 → revision 2.
- **Amendment D — deposited text is authoritative; the working tree may be
  behind it.** Origin: `CT-S26-CTV17-DRAFT`, the v1.4–v1.6 fetch.

Status: **PROPOSED**, both. P0 is pasted per-session and has no canonical file
in this repository; this document is the amendment text plus the evidence that
motivated it.

---

# Amendment C — a check that reads a file must verify it read it

## C.1 The gap in the existing rule

P0 and the corpus's standing practice already require that a control be an
assertion **that can fail**, and mutant testing is the instrument: perturb the
input, confirm the check rejects the perturbation. That discipline verifies a
check's **logic**.

It does not verify the check's **input path**. If the reader is broken, the
check evaluates the wrong bytes — and a mutant test **cannot** detect this,
because a broken reader rejects the mutant too, for the same wrong reason. The
can-fail control fires, the mutant is caught, and the check still reports a
false result about the real file.

The failure is at its worst for checks that report **absence**, because a
broken read and a genuinely missing feature produce **verbally identical**
output. There is nothing in the message to distinguish them.

## C.2 The proposed clause

Append to P0 under PRE-REGISTRATION, after the vacuity pre-check clause:

```text
- READER INTEGRITY. A check that reads a file must verify that it read the
  file, before it evaluates anything about the contents:
    * Assert at least one KNOWN-PRESENT feature (a title line, a required
      section heading, a character set the file is known to contain) and abort
      on failure. Only then evaluate any known-absent or count-based
      condition.
    * Where the check reports an ABSENCE, the known-present assertion is
      mandatory, because "content missing" and "my reader could not see it"
      produce identical output otherwise.
    * Control the reader as well as the content: run the same check through at
      least one deliberately defective reader (wrong codec, no newline
      normalisation, truncated input) and require it to be CAUGHT. Mutant
      testing verifies a check's logic; it cannot verify its input path,
      because a broken reader rejects the mutant too.
    * Normalise line endings once, in one place, immediately after decoding.
```

## C.3 The evidence

`CT-S26-CTV17-DRAFT/scripts/verify_notice.py` (revision 1) read
`NOTICE-v1.7.md` in **binary** and matched fenced code blocks with a pattern
for a triple backtick followed by `\n`. The file has **CRLF** line endings, so
the pattern matched nothing and the check reported:

> no fenced block containing the basis was found

which is **verbally identical** to what it reports if the PSLQ basis had really
been omitted — exactly the defect that check exists to catch, and exactly the
carry-over the operator had named as most likely to be lost in transit.

It was caught **only** because a second, differently-implemented read of the
same function in **text** mode returned the block and passed: two reads of one
file disagreed. The mutant controls did **not** catch it and could not have.

Repaired by normalising CRLF to LF in one place after decoding; final run 14/14
checks with 14/14 controls firing. Recorded as claim `S26C-07`.

At revision 2 the clause was implemented as designed: `assert_read()` requires
no `\r`, the exact title prefix, at least four fence markers and all four of
`ξ₀`, `β`, `Γ`, `≤` before any check runs; and SECTION 3 re-reads the file
through three defective readers — binary-without-normalisation (the revision-1
defect reproduced exactly), latin-1, and truncated-at-2 KB. **All three are
caught**, on `\r`, on the missing `ξ₀`, and on the fence count respectively
(claim `S26C-17`).

## C.4 Why it is not redundant with any existing P0 line

| existing rule | what it catches | why it missed this |
|---|---|---|
| controls as assertions that can fail | checks that cannot fail | the check *could* fail and its mutants fired |
| mutant testing | wrong comparison logic | a broken reader rejects the mutant too |
| vacuity pre-check | observable not coupled to structure | the observable was fine; the bytes never arrived |
| basis degeneracy pre-check (Amendment A) | a degenerate search space | the space was fine; the input path was not |
| "read back what you wrote" | a script that wrote wrong | this script wrote nothing; it *read* wrong |

---

# Amendment D — deposited text is authoritative; the working tree may be behind it

## D.1 The gap in the existing rule

P0 currently says, under GOVERNANCE:

> Never invent file paths, session names, DOIs, coefficient values, or
> literature results. If something you need cannot be found in the repo, STOP
> and report exactly what is missing.

This is a rule about **invention**, and it works. What it does not address is
**staleness**: the case where the repository does contain the material, the
material is found, quoted accurately and cited correctly — and is simply **out
of date relative to what was actually published**.

A deposit is immutable and dated. A working tree is neither. For anything this
corpus has deposited, the deposited text is the **published state of the
claim**, and the repository holds at best a copy of some earlier draft of it.
The default assumption must therefore be inverted: **where the two disagree,
the record is right and the tree is stale**, until the reverse is shown.

The rule as written also has a second, sharper consequence. A repository-wide
search establishes absence **from the repository**, which is not absence from
the corpus — and a finding phrased as the latter on evidence of the former is
false, however carefully the search was run.

## D.2 The proposed clause

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

## D.3 The evidence

Channel Theory v1.4, v1.5 and v1.6 were **absent from this repository** — the
newest in-repo source is v1.3.1. Revision 1 of the v1.7 notice was drafted
against that tree. On the operator's instruction the deposited descriptions
were fetched (`refs/`, ten files, bytes and sha256 in `REFS-MANIFEST.md`), and
they corrected **five** statements the notice would otherwise have deposited:

1. `op:xi0-d3-direct` was **withdrawn as vacuous at v1.6**, not "subsumed".
2. `op:xi0-singularity-type` **exists**, created at v1.6. Revision 1 reported
   *zero occurrences* — **true of the repository, false of the corpus**. This
   is the general lesson, and it is the second instance in this corpus: the
   Odlyzko citation was likewise reported unsourced on a repository-wide search
   while the source lived outside the worktree.
3. `op:xi0-degree-d` had **already been restated at v1.6** with an analytic
   residual; revision 1's flat "CLOSED" over-claimed.
4. The Painlevé target was corrected at **v1.4** — `P-III(D₆)` → Painlevé V on
   the Sakai surface `D₅^(1)` — and marked **conjectural at v1.5**. **The
   repository's `P-III(D₆)` text is the stale copy, and the record had been
   right for two versions.** This is the sharpest instance: accurate quotation
   of a stale tree reproduces a premise the record retired.
5. The EBR supersession needed **scoping** — positive `b`, physical object,
   Lean layer `d = 2–5`, and by EBR's own §8 not a symbolic-degree formal
   proof. Superseded **in scope**, not withdrawn.

The fetch also **collapsed four of the six open questions** in `REPORT.md` §6,
including confirming the version number itself. None of the five corrections
required new mathematics; all five required reading the record.

## D.4 Why it is not redundant with any existing P0 line

| existing rule | what it catches | why it missed this |
|---|---|---|
| "never invent … DOIs, literature results" | fabricated citations | nothing was invented; the tree was quoted correctly |
| "if it cannot be found in the repo, STOP" | missing input | the material *was* found — an older version of it |
| "record exactly what file you read" | untraceable claims | the file was named; it was simply not current |
| artefact hashing (Amendment B) | a hash pointing at a moved artefact | the artefact never moved; it was superseded elsewhere |
| reader integrity (Amendment C) | a broken input path | the input path was fine; the input was old |

## D.5 Scope note

The cost of the rule is one fetch per version characterised, and the fetch is
read-only. Both Zenodo and DataCite serve the description without
authentication; a 504 writes a short HTML error page, so **size-check every
download and delete short bodies** rather than hashing them. Where the PDF
cannot be obtained — as here, for v1.5 and v1.6 — **point at the section by
version DOI and do not paraphrase what was not read**.
