# P0 addendum — citation hygiene rule (adopted, operator review #4)

Status: **adopted as a standing P0 rule.** Prepend to every future session
preamble alongside the existing GOVERNANCE / EPISTEMIC LABELS / AEAL RECORD /
PRE-REGISTRATION / HALT CONDITIONS blocks.

---

```text
CITATION HYGIENE
- At deposit time, re-fetch every external citation and record its sha256. Do
  not carry a citation forward from an earlier draft on the assumption that it
  is still correct.
- For any LOAD-BEARING statement taken from a source, read the rendered PAGE
  IMAGE, not an OCR text layer and not a search-result summary. Load-bearing
  means: the claim would change if the statement were different.
- This rule covers HYPOTHESES as well as theorem statements. A theorem quoted
  correctly but applied outside its hypotheses is the same defect as a
  misquotation.
- Record, for every external source actually used: title as shown at the
  source, authors, journal/volume/pages or DOI, the version or release read,
  the access date, and the sha256 of the retrieved file.
- Never obtain a paywalled source through a mirror or shadow library. If a
  source cannot be obtained legitimately, record it as NOT OBTAINED together
  with what would have been checked, and halt any claim that depends on it.
```

---

## Why this rule exists

It is not a precaution; it is a response to measured failure. In the
2026-09-17 run, **four citation-level defects** were found across one short
document and one agent report. **None** was a defect in any mathematical
argument.

| # | Defect | Found by | Would it have flipped a conclusion? |
|---|---|---|---|
| 1 | DLMF **(5.11.12)** quoted as though it were (5.11.13)'s `G_k` expansion | `CT-S7-COLDREAD` | No — the proof only needed (5.11.12) |
| 2 | DLMF bibliography said **Release 1.2.4**; actual **Version 1.2.8**, 2026-09-15 | `CT-S10-COLDREAD2` | No |
| 3 | Gautschi **(2.8)** OCR'd as `"ab 0; a, real"` — readable as "coefficient `a` is real" | `CT-R1-AUDIT` | **YES** — would have excluded complex `β_d` and voided the entire prior-art finding |
| 4 | Stale `\bibitem{Vquad}` version pin in a superseded draft | `CT-R1-AUDIT` | No — the deposit-ready path was already correct |

Defect 3 is the one that justifies the rule's two sharpest clauses. It was
invisible in the OCR text layer and was caught only by re-rendering journal
p. 34 from the PDF at 3×. It sat in a **hypothesis**, not in a theorem
statement — which is why the rule says so explicitly.

A fifth near-miss, recorded below, was a **bibliographic-numbering trap** rather
than a transcription error, and motivates the "title as shown at the source"
clause.

## The Wong–Li numbering trap

DLMF's own letter suffixes are counterintuitive, and getting them backwards
would send a librarian to the wrong paper:

| DLMF key | Actual paper | Cited at | Relevance |
|---|---|---|---|
| **Wong and Li (1992a)** | *Asymptotic expansions for second-order linear difference equations.* **II**. *Stud. Appl. Math.* **87**(4), pp. 289–324 | §2.9(ii), for **eq. (2.9.14)** | **This is our case** (`P = d`, `Q = 0`) |
| Wong and Li (1992b) | *Asymptotic expansions for second-order linear difference equations.* *J. Comput. Appl. Math.* **41**(1–2), pp. 65–94 | §2.9(i), §2.9(ii) | bounded-coefficient case; **not** ours |

So **"1992a" is the paper titled "II"**, and the one in *Studies in Applied
Mathematics*. Verified 2026-09-17 against `https://dlmf.nist.gov/bib/W`
(`refs/dlmf_bib_W.html`).

`CT-S8-LITCHECK`'s identification was **correct**; this entry records the check
because the suffix ordering invites exactly the error a rushed request would
make.

## Scope note

The rule applies to sources **used in a claim**. It does not require re-fetching
background reading that nothing depends on. The trigger is "load-bearing", and
when in doubt the cheaper action is to re-fetch.

---

## Companion rule — claim-by-claim adoption

Adopted under operator review #7, to sit alongside the citation rule.

> **Findings from a review are adopted claim by claim. A correct finding does
> not certify the reasoning around it; each adopted statement is verified on its
> own.**

### The evidence for it

`CT-S13-COLDREAD5` returned a genuine and valuable finding — that van der
Put–Saito exempt `(1/2, −, 1/2)`, object A's own type, from the strong
Riemann–Hilbert guarantee. In the **same** section of its report it also linked
`dim P = 0` to C3's single-fibre concern, which is a conflation: `P` is the
parameter space, and having no parameters is a different matter from having no
deformation written down.

I verified the first and adopted the second without challenge. The operator
caught it. The correct finding lent the surrounding reasoning a credibility it
had not earned.

### Interaction with the citation rule

The two rules address the same failure from opposite directions. The citation
rule says: do not trust a rendering of a source. This rule says: do not trust a
verdict on a source. Both reduce to verifying the specific statement you intend
to rely on, and nothing else by association.

### Practical form

When adopting a review's output:

1. List each statement to be adopted **separately**.
2. Verify each against primary evidence, independently of the others.
3. Record adopted and rejected statements, **with the reason**, so that a later
   reader can see which parts of a review were relied on. Rejections matter as
   much as adoptions: the Q5 notation caveat was declined on evidence, and that
   decision is recorded in `VERIFY-S13.md`.
4. Never adopt a block of reasoning because its headline conclusion is right.

---

## Companion rule — per-round record invariants

*Adopted, operator review #8.*

A record that is allowed to drift is not a record. The following invariants are
checked over **every** `claims.jsonl` in the session tree at the end of every
round, before the round's `AUDIT.md` section is written. The check is
`check_invariants.py`; it exits nonzero on any failure.

| # | Invariant | Why |
|---|---|---|
| 1(a) | No `file_inspection` claim carries the label **PROVEN**. | Reading a proof in a file is not proving it. This is the defect the R1 audit was opened to fix: twelve claims had been tagged PROVEN on the strength of a file that contained a proof, one of which had a load-bearing gap. |
| 1(b) | Every `claim_id` is **unique** across the corpus. | A duplicate ID silently destroys provenance: a later reference resolves to whichever line is found first, so a `cold` review can end up attached to a claim nobody reviewed. |
| 2 | Every claim carries exactly one recognised label. | P0. |
| 3 | Every claim with a `review` field also carries a `review_note`. | The `cold` definition is type-dependent (proof vs. computation); without the note the distinction cannot be re-checked. |
| 4 | `review` ∈ {`self`, `cold`, `lean`}. | P0, operator review #5. |

### The evidence for 1(b)

Invariant 1(b) was added because it caught a real defect in this run rather than
a hypothetical one. While assembling the deposit dependency list, **six
duplicate `claim_id`s** were found in `CT-R1-AUDIT/claims.jsonl`, created by
independent append batches that had each restarted the same numbering sequence.
Nothing had flagged them, because every individual append was well-formed. They
were repaired by `repair_claim_ids.py`; the corpus has been unique ever since.

The general lesson matches Rule 1(a)'s: **a defect that no single step can
detect has to be checked for globally, and on a schedule.** Both invariants
concern the integrity of the record rather than the correctness of any one
claim, and neither is visible from inside the operation that introduces it.

### Provenance of corroboration

Where a supporting claim is cleared because an independent cold session
recomputed it, the dependency audit must record **the specific `claim_id` it was
recomputed against**, not a prose description of the session. `deposit_deps2.py`
verifies that every such named claim actually exists in the corpus and reports a
**BROKEN LINK** if it does not, so the link can be re-checked later rather than
taken on trust.

---

## Companion rule — testing symbolic equality, and tools that fail silently

*Adopted, operator review #9.*

> **Equality of symbolic expressions is established by simplifying the
> difference to zero, together with a high-precision numeric check at several
> sample points. It is never established by `==` on unevaluated expressions.**

Structural equality (`==` in SymPy, and its effect on `set` membership and
dictionary keys) tests the *expression tree*, not the *value*. Two
mathematically identical radicals can compare unequal simply because one was
built by a different code path.

### The evidence for it

In round R11 a set comparison of the inverted roots of `z^2+z+3` against the
roots of `3x^2+x+1` printed **`False`** for two sets that are, elementwise,
identical -- `(-1 +/- i*sqrt(11))/6` on both sides. The printed values were
visibly the same; only the comparison disagreed. Had that `False` been taken at
face value it would have read as a **refutation of the central result of that
round**, namely the projective equivalence of objects **B** and **C**.

The elementwise check `simplify(expand(a - b)) == 0` returns `True`, and the two
sides also agree numerically. Both forms of confirmation are now required,
because each fails differently: `simplify` can return an unsimplified non-zero
form for an expression that *is* zero, while a numeric check at a single point
can pass for expressions that are not identically equal.

### The general rule this instance belongs to

> **A step that cannot fail cannot be trusted to report failure.**

Both defects found in R11 have this shape, and neither was detectable from
inside the operation that produced it:

* the symbolic comparison above returned a *well-formed answer* that was wrong
  for the question being asked;
* `append_r11_claims.py` deduplicated by `claim_id` and **silently dropped three
  of eleven claims** whose IDs had been reused from an earlier round -- the
  three carrying that round's central result. It exited **zero**. It was caught
  only because the scripted invariants forced a count to be printed and read.

Consequences, both now standing practice:

1. **Deduplication is not error handling.** A writer that encounters an existing
   key must **abort**, never skip. Silent idempotence is acceptable only where
   re-running is genuinely a no-op, and never where it can discard input.
2. **Every batch operation reports counts in and out, and the counts are
   checked.** A script that says only "done" hides exactly this failure.

---

## Amendment — what counts as *reading* a page image

*Adopted, operator review #9, after CT-S15.*

The citation rule says load-bearing statements are read from **page images**, not
from a PDF text layer. That wording proved insufficient.

`CT-S15-COLDREAD-DEFERRED` was supplied with page images and ran **OCR** on them,
reporting that *"the OCR retained the line imperfectly"*. OCR applied to a page
image is a *newly generated text layer* with the same failure mode as the one the
rule was written to exclude, and with no provenance at all. Supplying an image
does not satisfy the rule if the reader converts it straight back into text.

The rule is therefore amended:

> **A load-bearing statement is read by looking at the rendered page.** Machine
> transcription of a page image -- OCR included -- is a text layer and does not
> satisfy this rule. An agent that cannot view an image must **HALT and report
> that**, rather than OCR the page and proceed. Quoting from OCR output as though
> it were the page is a reportable defect.

### The evidence for it

Two errors in CT-S15's report trace directly to its OCR, and were caught only by
re-reading both pages directly:

| Printed on the page | CT-S15's transcription | Consequence |
|---|---|---|
| Jimbo (3.1): constant matrix `diag(1, 0)` | `(1/2) sigma_3` = `diag(1/2, -1/2)` | different matrices, differing by the trace shift `(1/2)I` |
| `(A1)_PV`:  `theta_0, theta_t not in Z` | "non-integrality of `theta_infinity`, `theta_0`, `theta_t`" | over-states a **load-bearing hypothesis**; C2 turns on this assumption being violated by `theta_0 = theta_t = 0` |

Neither reached the notice -- its `(A1)` line and PV dictionary had been verified
earlier by direct reading and are correct -- but the second is exactly the
Gautschi (2.8) near-miss repeating itself, on a hypothesis rather than a theorem
statement, one review after that lesson was written down.

### Corollary for packet design

A packet that requires page-image reading must say so in terms the reader cannot
satisfy mechanically, and must state the halt condition explicitly. Listing the
image files is not enough.

### Second amendment — confirm the image actually rendered

*Adopted after CT-S16-MEMBERSHIP-C.*

The review-#9 amendment closed the OCR route. A second route remained open, and
it opened in CT-S16.

The `view` tool accepts **one image per message**. Two `view` calls issued in a
single message returned `maximum number of images (1)` and displayed **nothing**.
The failure is quiet: the call does not error, and the surrounding reasoning can
proceed on "recalled" page content that was never seen. In CT-S16 it did proceed,
for two pages, before being caught and stopped; each page was then re-read alone
in its own message, and the conclusions were rebuilt from what was actually
displayed.

Reasoning from a page one has not seen is fabrication, whatever the intent. The
amendment:

> **Before a page image is used as evidence, confirm that it displayed.** Request
> one image per message and check the response actually contains it. A `view`
> that returns a limit notice, or returns without an image, is a **HALT**, not a
> prompt to continue from memory.

This is the same shape as every other defect recorded in this file -- *a step
that cannot fail cannot be trusted to report failure* -- and it is the third
instance of it caught by a control rather than by inspection.

---

## Third amendment (operator review #15) — sealed derivations in cold packets

**Rule.** When a cold packet asks a reader both to *derive* X independently and to
*rule on a drafted statement about* X, the drafted statement must be **sealed
behind a hash of the derivation**. The reader completes the derivation, writes it
up, records its sha256, and only then opens the statement. The derivation may not
be revised afterwards; if the seal changes the reader's mind, that belongs in the
verdict, where it is visible.

**Why.** Without this, the two tasks are in conflict. The drafted statement
contains the answer to the derivation, so a packet containing both converts an
independent check into a confirmation exercise — and does so silently, since the
reader has no way to know what it was supposed to have found on its own.

**Origin.** `CT-S18-COLDREAD-C3` was issued with tasks 1–3 (derive whether the
printed `b(z)` satisfies `det A(1)`; check the hypotheses; locate the point) and
task 4 (verdict on C3 as drafted) in one packet. The drafted C3 states the typo,
its residual's factorisation, and the membership conclusion. The packet was
re-staged before launch. Adopted as a standing pattern at operator review #15.

**Mechanics.** `packet/sealed/` holds the statement; `outputs/stage1.sha256` holds
the hash of the stage-1 write-up; the task file states the rule explicitly and
names both paths.

**Applies equally to** any packet that pairs "compute the value" with "is this
printed value right", or "find the errors" with "here is the list of errors".

## Fourth amendment (operator review #15) — free to read is not free to redistribute

**Rule.** No reference file is cleared for commit on the ground that its source is
"open access". Access and redistribution are separate permissions and must be
checked separately, **per file**, against the licence the publisher or repository
actually attaches to that item. Until each row of `REFS-LICENCE-REVIEW.md` is
checked individually, everything under any `refs/` directory stays **local and
uncommitted**.

**Specifically flagged.** arXiv licences are **per submission**. The default
(`arXiv.org perpetual, non-exclusive license`) grants arXiv the right to
distribute and grants the reader **no redistribution right at all**. An arXiv PDF
is therefore not clearable without reading the licence stamp on that submission's
abstract page.

**Origin.** `vanderPut-Saito-AIF-2009-59-7-2611.pdf` was assessed "likely safe"
because *Ann. Inst. Fourier* is open access. Its own title page reads
*"tous droits réservés"*. Corrected at review #14; generalised at review #15.

## Fifth amendment (operator review #16) — a write is not done until it is read back

**Rule.** Any script or command that writes or edits a file must verify its own
effect afterwards by reading back what it wrote, and must fail loudly if the
effect is absent. **An exit code of zero is never evidence that a write
happened.**

Minimum form for an append: record the count before, append, re-read, assert the
count rose by exactly the number intended, and assert each new identifier is
present. For an in-place edit: assert the new text is present and, where the
edit replaces something, assert the old text is gone.

**Origin — three instances of one failure, each with a different surface.**

1. The append path that exited zero while silently dropping exactly the three
   central claims. Caught by scripted invariants, not by the tool.
2. simplify(Pfam - Pfam) == 0 as a control in CT-S18: a check that cannot
   fail, so it cannot report failure.
3. python - @"..."@ in PowerShell: there is no heredoc, so the interpreter
   opened interactively, consumed the script as terminal input, did nothing, and
   **exited zero**. The backup in the same call succeeded, so the combined
   output looked clean. Caught only because the result was read back.

The operator's framing at review #16: these are *the same failure with different
surfaces*. The rule above is written against the failure, not against any one of
its surfaces.

**Corollary for this shell.** Prefer the editing tool over PowerShell
here-strings for prose. Inside `@'...'@` everything is literal; inside
`@"..."@` interpolation applies. Neither is a heredoc for piping to an
interpreter. Write a script file and run it.

**Extension at R21b — the rule covers counts, not only writes.** A quantity that
will be *reasoned from* is read back by re-deriving it in a separate invocation.
A count interpolated into a shell pipeline alongside other commands is not
evidence, and a plausible number is the dangerous case: an implausible one gets
checked.

Two failures in one round. A PowerShell statement that invoked `git add -n`
twice and counted the second reported **7** stageable paths for a tree whose
true count is **391**; it exited zero, and 7 would have supported the conclusion
that almost nothing was stageable — the exact opposite of the finding it had
been run to test. Separately, two counts stated to the operator (*71 files under
`refs/`, `pages/` and `packet/`*) were wrong before checking; the true figure is
**69** under `refs/` and `pages/`.

A second corollary from the same round: **a command's exit status is not its
answer.** `git check-ignore -v` printed the *negation* pattern for
`refs/parse_dlmf.py` while still exiting 0, which reads as IGNORED and is the
reverse of the truth. Where a tool's exit code and its output can disagree, the
question is settled by an operation whose *effect* is the answer — here
`git add --dry-run`, which stages nothing and is reversible.

## Sixth amendment (operator review #17) — name the component or the cyclic vector

**Rule.** Any packet, script or claim that compares, identifies or locates a
**scalar operator obtained from a rank-2 system** must name the component, or
equivalently the cyclic vector, under which the reduction is taken. "System C's
operator" does not name one.

A rank-2 system has two first-order scalar reductions, one per component. They
are both correct and they are not equal: their first-order coefficients differ
by `d/dz log(c/b)`, oriented as

    P(route 1, the y1 reduction) - P(route 2, the y2 reduction) = +d/dz log(c/b)
                                                                = c'/c - b'/b

and in general, before any convention is fixed, by `d/dz log(n21/n12)`; the two
agree only because `N = -A/D` divides both off-diagonal entries by the same `D`.
Comparing one route against the other produces a mismatch that looks like a
refutation. Where `b` is constant and `c` has a simple zero at `q`, as it does
in vdPS's chart `U₀`, that mismatch is exactly `-1/(z-q)`, which has no zero in
`z` — so the comparison cannot return a match at *any* sample point or parameter
value. A test of that shape does not fail loudly; it fails uniformly, which is
harder to notice.

*Orientation and proviso added at R20, from CT-S20B-COMPONENT.*

**Not affected.** A scalar second-order ODE given as such has a canonical
trace-free normal form, so claims about B, C and their normal forms carry no
component choice. See `COMPONENT-AMBIGUITY-SCAN.md`.

**Origin.** CT-S18 was asked to "locate System C in chart `U₀` and verify by
re-substitution". The packet did not say which reduction, the reader took the
`c`-route, vdPS's convention is the `b`-route, and the reader returned **ERROR**
on a deposit-gating claim. The fault was the packet's, not the reader's.

**Relation to C4.** This is the same defect class as C4's per-object ambiguity:
a name that the writer reads as denoting one object and the reader reads as
denoting another. C4 concerns three objects sharing a label; this concerns two
reductions sharing the phrase "the scalar equation". The remedy is the same —
name the object, do not rely on context to disambiguate it.

## Seventh amendment (operator review #19) — a test that cannot *succeed*

**Rule.** Before a negative result is reported as a finding, establish that the
test could have come out positive. State what input would have made it pass, and
either exhibit one or say why none exists.

This is the mirror of the rule already in force for positive results, that a
control must be able to fail. Both failure modes certify nothing, but they do
not look alike:

| | mechanism | how it presents |
|---|---|---|
| **cannot fail** | the check is satisfied by construction | a green tick that means nothing; quiet |
| **cannot succeed** | the comparison is against the wrong object, or the residual has no zero | **a confident negative verdict that reads as a discovery** |

The second is the more dangerous of the two, and it is the newer finding. A
result that cannot fail is merely empty. A result that cannot succeed is empty
*and* assertive: it arrives looking like a defect someone has found, and it
recruits the reader's scepticism to its own side.

**Origin.** `S17-22`. CT-S18 compared System C against the `c`-route reduction.
The residual is `-1/(z-q)`, which has no zero in `z`, so the comparison returns
a mismatch at every sample point, at every parameter value, for ever. Its
**ERROR** verdict on a deposit-gating claim therefore carried no information
whatever — but it read as a real defect **for two rounds**, was recorded as a
contested gate, and cost two further cold packets (CT-S19, CT-S20B) to clear.
Nothing in the verdict itself distinguished it from a genuine refutation.

**The diagnostic.** Ask of any negative result: *what would this test have
returned had the claim been true?* If the answer is "the same thing", the test
has not been run. In CT-S18's case one line would have settled it — evaluating
the mismatch at the located point rather than only at a generic sample, or
noticing that a residual with no zero cannot vanish for any member of the
family.

**Scope.** This applies to refutations, falsifier arms, and any pre-registered
threshold reported as breached. A falsifier that fires is a result only if a
non-firing outcome was reachable.

*Distinct from the fifth amendment.* That one concerns writes that did not
happen; this one concerns comparisons that happened and could only ever have
gone one way.

---

## Detector hygiene — two lines

Both from `S21-35`/`S21-36`, where the scanner written to catch escape damage
carried both defects at once.

- **A detector's coverage list is itself an unchecked assumption.** The escape
  scanner tested `\r \a \v \f` and omitted `\t` and `\b` — in a Painleve
  document full of `\theta` and `\beta`. Nothing flagged the omission, because a
  detector reports only on what it was told to look for.

- **A guard added to suppress false positives can suppress exactly the hits that
  matter.** Restricting the scan to line starts cut a real 4 down to a reported
  2; the survivors were the mangled sites inside the deposit object. This is the
  seventh amendment's *cannot fire* shape appearing inside the detector written
  to catch that shape.

- **Identify a rendered page by the number printed on it, never by the arithmetic
  that produced it.** A page index plus an offset is a guess about the front
  matter; the printed number is the page's own claim about itself. Two defects in
  `S21-42`/`S21-43` were the same shape — a renderer off by one, and a stored
  cold-packet image named by PDF position, which sent a cold reader (A3)_PV under
  the label (A1)_PV. Where the running head does not survive text extraction, the
  check is an eye read, not a script.


- **Never pass markdown through a double-quoted PowerShell string.** The
  backtick is PowerShell's escape character, so a code span opener followed by
  a, b, e, f, n, r, t, v or 0 is silently consumed. The damage is selective:
  most backticks in a document survive, and their survival reads as evidence
  that nothing is wrong. Write the text to a file and run the file. The rule is
  not "escape the backticks" - enumerating the affected letters is the
  coverage-list mistake this file already warns about. (R33.1, R33.2)
- **Route every write to a recorded file through an appender that refuses
  control characters**, and give that appender a two-sided control: one input
  it must reject, one it must accept. A control that fails for the same reason
  as the run it is controlling certifies nothing. (R33.1)
