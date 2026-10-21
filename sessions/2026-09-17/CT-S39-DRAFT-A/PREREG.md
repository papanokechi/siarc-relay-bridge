# PREREG — CT-S39-DRAFT-A (Group A: §0 introduction, §2 growth with §2.0)

Written before the gate `check_group_a.py` was run. The artefact-location work
that preceded it was file inspection — establishing *which* sources are held —
not measurement, and it is reported as such.

## 1. Hypothesis

Every citation that §2.0 makes can be verified **against the held page image or
PDF**, and every claim id that §0 and §2 cite resolves in the corpus with the
label the prose gives it.

The operator's rule for this group is stronger than the usual one and is the
reason the gate exists:

> Every one of those has been corrected at least once during this run, so the
> drafting check for Group A should verify each citation against the held page
> image rather than against a prior draft or a claim text.

So `OUTLINE.md` §2.0 and the claim texts of `S24-10`/`S24-12`/`S24-13` are
**not** admissible evidence here. They are the thing under test.

## 2. Observables

For each of the eight cited sources:

- **O1** — the source resolves to a held artefact in the corpus, by path, with
  a sha256;
- **O2** — the printed folio resolves to a PDF index by *locating the folio in
  the page's own text*, never by assuming an offset;
- **O3** — each quoted fragment occurs on that page, compared on a
  **whitespace-free, ligature- and dash-normalised** invariant;
- **O4** — each claim id cited by the drafted prose resolves to exactly one
  corpus claim, and the label printed in the prose equals the corpus label.

O3's normalisation is pre-declared because the Odlyzko PDF's text layer
**drops inter-word spaces**. Comparing on raw text would report a false absence
for every fragment on that page. The normalisation removes exactly the
representation the extractor fails to preserve, and nothing else: no character
is added, dropped or substituted apart from whitespace, ligature expansion,
quote and dash folding, and case.

## 3. Falsifiers, with thresholds

The gate FAILS, and drafting halts, if any of:

- **F1** any cited source has **no** held artefact — threshold: 8 of 8 must
  resolve, 7 is a failure;
- **F2** any printed folio fails to resolve by locating its own folio marker;
- **F3** any quoted fragment is absent from its stated page — threshold: 0
  absences tolerated;
- **F4** any cited claim id resolves 0 times or more than once;
- **F5** any label printed in the prose differs from the corpus label for that
  id — threshold: 0 mismatches;
- **F6** the prose asserts a Painlevé label for `V_quad`, or states the upper
  bound on `ψ_∞` citing `S1-02`, or leads the method paragraph with Pincherle.

F6 encodes three standing rulings as machine-checkable conditions rather than
as intentions.

## 4. Vacuity pre-check — the observable must move when the data moves

Declared before the run. Each arm mutates the thing the hypothesis is about and
must be **CAUGHT**:

- **A1** a fragment altered by one word must be reported ABSENT (else O3 is
  matching something other than the fragment);
- **A2** a fragment sought on a **decoy page** — the leaf before and the leaf
  after — must be reported ABSENT (else O3 is searching the whole document, and
  the folio resolution is doing no work);
- **A3** an **impossible folio** must fail to resolve (else O2 accepts any
  number);
- **A4** a **fabricated near-miss** — the Odlyzko sentence with its negation
  removed — must occur nowhere in the 192-page document (else O3's matching is
  too loose to distinguish a claim from its opposite);
- **A5** a **deliberately wrong label** inserted into the prose must be caught
  by O4. This is the control the operator asked for by name;
- **A6** a **deliberately unresolvable claim id** must be caught by O4;
- **A7** the three F6 prohibitions must each fire when their forbidden text is
  injected.

**A2 and A3 are the ones that matter**, because without them O3 degenerates
into "the fragment is somewhere in the book", which is not what a page citation
asserts.

## 5. Known-answer control

`S26-05` records that CT-S26's own known-answer control fired because the
registered answer was itself wrong. Accordingly the known-answer arm here is
stated with its expected value **before** the run:

- Gautschi Thm 2.3 is attributed on its own page to **Perron and Kreuser**, and
  Thm 1.1 to **Pincherle**. If the gate reports the attribution of either
  theorem differently from this, the gate is believed over this PREREG and the
  discrepancy is reported, not silently corrected.

## 6. What this gate does NOT establish

Stated now so it cannot be claimed later. The gate verifies **citations and
labels**. It does **not** verify that a formula transcribed into the prose is
the formula the corpus proves: a transposed digit inside an equation would pass
every check above. That gap is the operator's own scoping note for a later
pass once all sections exist, and it is recorded here rather than discovered
afterwards.
