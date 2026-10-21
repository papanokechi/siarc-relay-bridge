# PREREG — CT-S38-NOTATION-SYMBOLS

Written before `scripts/symbol_index.py` was run and before any candidate
letter was chosen. Three rulings are being executed:

1. build a symbol-collision index, then propose letters from it;
2. re-letter `theorem.tex` mechanically, with a rendered-text equivalence check;
3. close the genuine §1 collisions now, defer the rest.

---

## Part A — the symbol index

### Hypothesis

H-A: The names fixed at CT-S36 (`q_n`, `q_\infty`, `\lambda_1..\lambda_d`,
claim `S36-11`, label CONJECTURED) collide with meanings already carried by
those letters elsewhere in the corpus — `q` with the Okamoto chart coordinate
and `\lambda` with the indicial variable.

### Observable

`scripts/symbol_index.py` extracts every single-letter and letter-subscript
symbol occurrence from the declared sources, groups occurrences by a canonical
symbol key, and emits for each key: the number of occurrences, the sources it
appears in, and a bounded sample of verbatim contexts. **The index is the
deliverable.** Meanings are then adjudicated by reading those contexts, and the
adjudication is recorded as a table in `REPORT.md`.

### Falsifier, numeric threshold

H-A FAILS if the index shows `q` carrying only one meaning across all sources,
or `\lambda` carrying only one meaning. Threshold: a collision requires **at
least two distinct adjudicated meanings** for the same key, each evidenced by
at least one verbatim context from a **different** source file. Fewer than two
such meanings for both `q` and `\lambda` refutes H-A, and the renaming ruling
would then have to be reported as unsupported by the corpus.

### Vacuity pre-check

(i) **Sensitivity.** A symbol known to carry exactly one meaning
(`\Gamma`, Euler's Gamma) must be reported with one meaning, and a symbol
known to carry two (`B`, which §1 itself declares is used both for the
monodromy matrices `B_i` and for the product `B_n`) must be reported with at
least two contexts from different sources. If `B` does not separate, the
instrument cannot detect collisions and the session halts.

(ii) **Reader non-vacuity.** Before any count is reported the extractor
asserts, per source: the file decodes; it is at least 1000 bytes; and it yields
at least 20 symbol occurrences. Bounds, not fingerprints.

### Declared in advance

- **Sources.** `theorem.tex` and `section1.tex` (CT-S36), `OUTLINE.md`
  (CT-S24, revision 6), and the claim text of every claim id the outline
  cites. To these I add `section3.tex` and `section4.tex` (CT-S37-DRAFT-B),
  **marked as an addition to the instructed list**, because they are drafted
  paper prose and the operator names §3 as a place a collision would surface;
  excluding them would hide the evidence.
- The count of "6 genuine collisions in §1" is the operator's. It is **not**
  assumed. The index measures the number independently and the measured number
  is reported against 6, whichever way it falls.

---

## Part B — choosing the replacement letters

### Decision rule, fixed before the index is read

A candidate letter is **admissible** only if all hold:

1. its canonical key does not appear in the index with **any** adjudicated
   meaning;
2. it is not a Painlevé chart coordinate: not `p`, `q`, `t`, `\theta` (nor
   `\theta_0`, `\theta_1`, `\theta_\infty`);
3. it is not an exponent letter: not `\rho`, `\lambda`, `\mu`, `\sigma`,
   `\alpha`, `s`, `\kappa`;
4. it is not `r`, in any form, because `r(c)` is van der Put–Saito's Katz
   invariant and `r_n, r_\infty, r_1..r_d` are the deposited names;
5. it is not `h` (the G1 argument), `a` (the numerator polynomial), `b`,
   `\beta`, or `c` / `c_\pm` (the actions).

`scripts/check_proposal.py` enforces 1–5 **mechanically against the emitted
index**, and rejects any proposal failing any clause. A proposal I like but the
checker rejects is discarded; the checker is not adjusted to admit it.

### Falsifier

If no admissible pair of letters exists, that is a finding and the session
halts rather than relaxing a clause.

---

## Part C — re-lettering `theorem.tex` and `section1.tex`

### Hypothesis

H-C: The rename changes symbols and nothing else.

### Observable

Both files are renamed by a **scripted** substitution. Both PDFs are rebuilt.
The rendered text of the pre-rename PDF and of the post-rename PDF is extracted
and compared as follows:

- **Equivalence arm.** Apply the same symbol substitution to the *rendered text
  of the OLD PDF*; require the result to equal the rendered text of the NEW
  PDF, after whitespace squeezing only.
- **Non-vacuity arm.** Require the *unsubstituted* old rendered text to
  **differ** from the new rendered text. If they are already equal, the rename
  did nothing and the equivalence arm passes vacuously.

Whitespace is squeezed because a glyph-width change re-breaks lines; comparing
on a representation the renderer may legitimately rewrite is the CT-S35 defect
and is not repeated. A non-whitespace character count is reported on both sides
as a guard against squeezing having destroyed the comparison.

### Falsifier, numeric threshold

H-C FAILS if the equivalence arm shows any difference, or if the non-vacuity
arm shows zero difference. Threshold: zero differing characters on the
equivalence arm; strictly more than zero on the non-vacuity arm.

### Second, differently-implemented reader

Any difference reported by `pdftotext` is confirmed with **PyMuPDF** before it
is treated as real. A reader that invents a defect fails like one that misses
it, and the same `re.sub`-style artefact has already produced 85 phantom
findings once in this corpus.

### Preservation

`theorem.tex` carries a cold-read PROVEN status. The pre-rename file is copied
to `refs/theorem-pre-S38.tex` **with its sha256 recorded before anything is
edited**, and the post-rename build is required to have the same page count and
to contain no undefined references.

---

## Part D — controls

`scripts/mutants_s38.py`. Each arm must be CAUGHT **for the stated reason**:
non-zero exit, output naming the expected condition, and no `Traceback`,
`SyntaxError` or `NameError` in the output.

1. a proposal using `q` — must be rejected by clause 2;
2. a proposal using `\lambda` — clause 3;
3. a proposal using `r` — clause 4;
4. a proposal using a letter that *is* in the index with a meaning — clause 1;
5. a rename that also changes a word of prose — the equivalence arm must fire;
6. a rename that changes nothing — the **non-vacuity** arm must fire;
7. a source file emptied — reader integrity must refuse, not report "no
   collisions";
8. the index with the `B` sensitivity control removed — the vacuity pre-check
   must fire.

Arms 1–4 are drawn from letters that are *not* in the checker's own forbidden
list where possible, so that no arm is rejected merely because the checker
consults its own constants: arm 4 in particular uses a letter discovered from
the index at run time, not a hard-coded one.

---

## Part E — scope, fixed in advance

Ruling 3 is executed as stated: only the genuine §1 collisions are repaired in
this session. The remaining CT-S23 residue is left to the sections that will
define it, and items belonging to the cut §9 are left to retire with it. **No
section outside §1 is re-drafted**, and `theorem.tex` is changed only by the
symbol substitution. A second notation pass after Group E is recommended, not
performed.

## Halt conditions specific to this session

- `q` or `\lambda` fails to show two distinct meanings (Part A falsifier).
- No admissible letter pair exists (Part B falsifier).
- The equivalence or non-vacuity arm fires and a second reader confirms it.
- The re-lettered `theorem.tex` fails to build, or its page count changes.
