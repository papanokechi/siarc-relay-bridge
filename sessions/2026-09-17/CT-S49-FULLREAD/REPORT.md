# REPORT — CT-S49-FULLREAD

**The end-to-end read.** The paper read as a document, in order, once.

---

## 0. What was done

All fifteen source files were copied into `refs/` from the live tree
(`CT-S45-FORMULA-A`), hashed, and read continuously in build order:
`paper.tex`, §0–§10, `appendixA.tex`, `appendixB.tex`. Nothing was edited.

Every observation from that read was then reduced to a **decidable predicate
over the source bytes** and confirmed by `scripts/check_read_findings.py`:

```
READ CHECK: 14 findings, all predicates confirmed; 9 controls, 9 FIRED
```

The confirmation step exists because of the standing hazard — *a reader that
invents a defect fails like one that misses it, worse if acted on.* Two
predicates failed on the first run, and **both failures were in the reader, not
the paper**:

- **F3b** asked whether the phrase `for both sign branches` is absent, using a
  needle that the quotation *reporting* the phrase satisfies. It found itself.
  Replaced by the decidable question: does the phrase occur anywhere **other
  than** inside the sentence that quotes it? (It does not.)
- **F8e** looked for `$(0,0,1,-)$` with maths delimiters; §1 writes it inside a
  display, so the control went **DEAD** and the script refused (exit 2) rather
  than reporting. Reading the raw line fixed the needle — and made the finding
  sharper than the read had it.

That is the third and fourth instance in this run of the reader being wrong
where the page was right, and in both cases the refusal — not the check —
is what caught it.

### What this session is not

The operator commissioned this read on the ground that *"a person reading is
worth more than any instrument"*. That judgement is accepted. **This is an
instrument-assisted read and it does not replace the operator's own.** What it
produces is a list of candidates with evidence, ordered by what a human reader
should look at first. The findings below are facts about the bytes; the
severity ordering is judgement.

---

## 1. Findings, grouped as the operator framed them

### A paragraph that no longer fits the page before it

**1. The paper disclaims, in two places, the gap that CT-S45–S47 closed — and
Appendix A says so.** `INSPECTED`

- §9.4 item 6, `section9.tex:183–184`: among "what this paper does not claim" —
  *"none has been symbolically re-derived here, and the formulas of
  Appendix~\ref{app:typo} were transcribed from page images rather than
  computed."*
- Appendix B §B.5 item 3, `appendixB.tex:139`: *"No displayed formula in this
  paper has been re-derived here from the script that computed it."*
- Appendix A closing note, `appendixA.tex:147`: *"Both routes were exercised
  for this appendix in `CT-S45-FORMULA-A`, **per equation**, and the factored
  form of the difference was found to carry the wrong sign and corrected."*

`CT-S45-FORMULA-A` is named **exactly once** in the paper. The closure is
recorded in one place and denied in two — and the denial in §9 names
`app:typo`, the very appendix that reports the work. A reader reaching §9.4
after reading Appendix A is told the opposite of what they just read.

This is the largest find of the read, and **no instrument in this run could
have caught it**: it builds, every reference resolves, every citation checks,
and every formula was routed. It is a defect visible only to someone holding
two sections in mind at once.

*It is also the one whose repair is a decision, not an edit.* The disclaimers
were true when §9 and Appendix B were drafted. The question for the operator is
whether "re-derived **here**" means *in this document* (in which case they are
literally true and misleading) or *for this work* (in which case they are
false). Appendix A's wording forces the second reading.

**2. A sentence that contradicts itself.** `INSPECTED` — `section8.tex:210–211`

> *"This is the second place in the paper where a structural argument for a
> numerically solid fact has been sought and not found --- the first being the
> twist question of §6.1, **where one was found**."*

Sought-and-not-found, first instance: where one was found. The sentence
destroys its own count in its own subordinate clause.

**3. A phrase quoted from a section that does not contain it.** `INSPECTED`

`section5.tex:148` writes *"The phrase ``for both sign branches'' in
§\ref{ssec:located}…"*. The phrase occurs nowhere in the paper **outside that
quotation** — §5.3 says *"On the branch"*, twice. The quotation marks assert a
verbatim source that does not exist.

### A result stated more than one way

**4. One formula, four typographies.** `INSPECTED`

| where | as printed |
|---|---|
| `section1.tex:211` | `R=\tfrac14P^2+\tfrac12P'-Q` |
| `section3.tex:43` | `R=\tfrac14P^2+\tfrac12P'-Q` |
| `section6.tex:59` | `R=\frac{P^2}{4}+\frac{P'}{2}-Q` |
| `section9.tex:36` | `R=P^2/4+P'/2-Q` |

The operator ruled that `R` unify into §1's form. §3 complied; **§6 and §9 did
not.** The notation pass reported the unification as done.

**5. The Katz-multiset shape is inconsistent across three sections.**
`INSPECTED`

`section1.tex:282–284` fixes the convention as the ordered quadruple
`(r(0),r(1),r(∞),r(t))` *"with a dash in the r(t) position"*, and at
`section1.tex:290` writes the PV row `(0,0,1,-)` — four slots. Then:

- `section4.tex:161` writes **the same PV row** as `(0,0,1)` — three slots;
- `section3.tex:203` `(0,0,1)`, `section3.tex:210` `(1,0,0,0)`;
- `section3.tex:214` `(\tfrac12,-,\tfrac12)` — a dash in the **r(1)** position,
  which the declared convention does not allow.

The 4-slot form occurs **once** in the paper, in the table that declares the
convention. Everywhere the convention is used, it is not followed.

**6. A counterexample stated at full length twice.** `INSPECTED`

`S17-02`'s counterexample appears complete in §6.1 (`section6.tex:25–27`) and
again in §10.1 (`section10.tex:25–26`), down to the identical witness sentence
*"with rational witness $w=z$ satisfying $2f+w'/w=0$"*. Two copies that can
drift. Likewise `section9.tex:40` re-displays `P_C` and `Q_C` as fresh
unnumbered displays instead of `\eqref`-ing `eq:PC`/`eq:QC` at
`section6.tex:69`.

### Defines one name and uses another

**7. §1 fixes a scalar form the paper never writes.** `INSPECTED`

`section1.tex:205` declares *"a scalar equation written $A\,W''+A'\,W'+C\,W=0$
… which is a different use of the same letters and **occurs only in that
displayed form**."* The paper's only equation of that shape,
`section3.tex:53`, is `(3x^2+x+1)W''+(6x+1)W'-x^2W=0`, and `section3.tex:55`
names its coefficients **lowercase**: `a(x)`, `b(x)`, `c(x)`. The declared form
occurs once — in its own declaration.

This is the **Newton polygon / Newton–Puiseux class** again: define one name,
use another, and nothing catches it.

**8. The letter `b` carries four meanings and §1's reuse list omits it.**
`INSPECTED`

| meaning | where |
|---|---|
| the recurrence polynomial `b(n)=Σβ_k n^k` | `section1.tex:22` |
| the System-C coefficient `b(x)=6x+1` | `section3.tex:55` |
| the matrix entry `b` of `A=[[a,b],[c,-a]]` | `section4.tex:56` |
| the coefficient `b_1` of that entry | `section5.tex:112` |

`section1.tex:225` lists *"Six further letters … reused"* — `M`, `A`, `L`, `u`,
`β`, `r`. `b` is not among them, nor are `a` and `c`. `section1.tex:14` claims
*"This section fixes every symbol, name and hypothesis used in the paper."*

**9. `s_1, s_2` are used once and declared nowhere.** `INSPECTED`

`section7.tex:208`: *"is singular because $s_1=s_2=2$ places it on two
resonance divisors"*. `section1.tex:130–133` enumerates exactly two uses of
`s` — the bare growth exponent, and the subscripted `s_±`, *"a different
object, and the subscript is what distinguishes them"*. `s_1` appears nowhere
in §1.

The quantity §7 calls `s_i` is declared in §1 as `a_i = tr(B_i)`. So this is
most likely a **surviving symbol from an earlier draft**, not a new object —
which makes it worse, not better: it reads as a third meaning of `s` in a paper
whose notation section says there are two.

### An argument arriving before its motivation

**10. `b_1` is used in §5 and only becomes intelligible in §6.** `INSPECTED`

`section5.tex:112` writes *"the no-apparent-singularity condition $b_1=0$"*
with no definition, and uses it four times (`:112, :138, :207, :212`).
`section6.tex:100` — *"these coincide exactly when $b$ is constant --- that is,
when $b_1=0$"* — is the first place it is tied to anything. §1 promises every
symbol is fixed before first use.

---

## 2. Queries for the operator (not reported as defects)

**11. One discrepancy, two page attributions.** `INSPECTED` / severity
`CONJECTURED`

`section4.tex:84` places a second van der Put–Saito discrepancy *"in the same
neighbourhood"* — the neighbourhood being p. 2655 (`section4.tex:59`).
`section7.tex:88` attributes what appears to be the same discrepancy to
**p. 2629**, and 2629 occurs exactly once in the paper. One of these sends a
checking reader to the wrong page. I could not determine from the text alone
whether they are the same discrepancy; *"neighbourhood"* may be loose.

**12. §10 says machinery is absent that §1 and §3 set up.** `INSPECTED` /
severity `CONJECTURED`

`section10.tex:7` declines to restate the Borel-plane constant question
*"because stating it would require machinery that no section above sets up"*.
But `section1.tex:108` defines *Stokes constant*, `section1.tex:136` sets up
the Borel plane and `ξ₀`, and `section3.tex:108` gives the actions `2/√3` and
`4/√3`. Whether this is wrong depends on which constant is meant — if it is a
specific connection coefficient, the sentence may be right and merely
overstated.

**13. §7.1 says §6 "performed" a trace-free gauge reduction for System C**,
which §6.3 arguably contradicts (*"there is no twist to insert between them"*).
Low confidence; a query, not a defect.

**14. Minor.** §5's `.tex` carries no `% ====` provenance header, the only
section without one. `section8.tex` writes `t=+2\sqrt{33}\,i/9` where §5 writes
`t=+2i\sqrt{33}/9` — the same number, two orderings.

---

## 3. What the read confirmed as *correct*

Worth recording, because a read that only finds faults is not calibrated:

- Appendix A prints the **`+¼`** factored form — CT-S45's sign repair landed.
- §1's `ρ` paragraph states all three senses, and no object in the paper is
  written `r_1` — CT-S38's re-lettering held.
- `−det A` is named in §8.7 — the `P` separation landed.
- `ξ₀ = 2/√β₂` is correctly the `d=2` case of `d/|β_d|^{1/d}`, and
  `ρ_± = 1/s_∓` are consistent under `z ↦ 1/x`.

---

## 4. What was NOT established

- **The paper has still not been read by a person.** This read is assisted and
  its findings are of a kind an instrument can confirm once a human has named
  them. What it cannot find is the thing it was not looking for.
- **No repair was made.** Every finding above is a candidate awaiting a ruling.
- **Findings 11–13 are queries**, not defects; I could not decide them from the
  text.
- **Prose quality was not assessed** — only consistency. Whether §2 is well
  written, whether §7 is too long, whether the introduction motivates the
  paper, are questions this session did not ask.

## 5. Open questions for the operator

1. **Finding 1 is a decision, not an edit.** Do §9.4(6) and §B.5(3) come out,
   get rewritten to say *"re-derived in the recorded sessions but not restated
   here"*, or stand as drafted with Appendix A softened?
2. **Finding 9**: is `s_1=s_2=2` meant to be `a_1=a_2=2`? If so it is a
   one-word repair; if not, §1 needs a third entry for `s`.
3. **Findings 4 and 5** show the notation pass reported unification it did not
   achieve. Worth a re-run, or a per-item confirmation check of its own claims?
4. **Finding 11** needs the page images to settle; should that be a task?

---

## 6. Uncommitted files

All new. **No file outside this session was created or modified.**

```
sessions/2026-09-17/CT-S49-FULLREAD/
  PREREG.md
  REPORT.md
  claims.jsonl
  refs/                              15 .tex copies of the live tree
  scripts/check_read_findings.py
  scripts/emit_claims_s49.py
  outputs/check_read_findings.out.txt
```
