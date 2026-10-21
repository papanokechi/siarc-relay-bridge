# REPORT — CT-S43-DRAFT-E (Group E)

**Draft only.** Nothing committed, pushed, tagged, deposited or submitted.
All changed files are listed in §8.

---

## 1. What was done

The last drafting session. It wrote §9 *Scope and limits*, §10 *Open
questions*, **Appendix A** (the misprint in the published family) and
**Appendix B** *Computational methods*; retired the build stub; and assembled
and built **the complete paper for the first time**.

| artefact | size | content |
|---|---|---|
| `section9.tex` | 9 930 B | 4 subsections, `\label{sec:limits}` |
| `section10.tex` | 6 428 B | 2 subsections, `\label{sec:open}` |
| `appendixA.tex` | 7 480 B | 6 subsections, `\label{app:typo}` |
| `appendixB.tex` | 7 647 B | 5 subsections, `\label{app:methods}` |
| `paper.tex` | 401 B | the whole document: preamble, §0–§10, both appendices |
| `paper.pdf` | **37 pages** | 0 errors, 0 undefined, 0 multiply-defined |

**26 claim ids** are cited, all resolving, none superseded, **26 of 26**
carrying a label in the prose and **0 bare**.

Appendix B discharges the debt §7 incurred: `app:methods` was a real
dependency, not a placeholder, and `S22-04`/`S22-05` are stated there with the
operator's required wording that the corrected identity is a *dependent*
restatement. Repair **R-(b)** is discharged in the stated form — the appendix
says plainly that reproduction requires the scripts.

**The stub is retired.** `forwardrefs_E.tex` carried exactly three entries —
`sec:limits`, `sec:open`, `app:methods` — and Group E supplies all three, so it
is not carried forward. This makes rule R1 **stronger**, not vacuous: with no
stub in the resolution set, every reference must resolve to a real `\label`.

---

## 2. Gates

| gate | result |
|---|---|
| `check_group_e.py` | **PASSED** — 26 citations, 87 literals, 0 failures, **15/15 arms CAUGHT** |
| `check_assembly.py` | **PASS** — 13 files, 124 labels, 76 targets, all resolving, 0 duplicated, 0 stub entries |
| `mutants_assembly.py` | **7/7 arms CAUGHT** |
| `pdflatex` ×2 | 37 pages, 0 errors / 0 undefined / 0 multiply-defined |

Gate output is **byte-identical** across pass 3 and a pass-4 re-run
(`50cdfc4c…`), and **15/15** recorded `output_hash` values resolve to the file
they name.

The **E3 control the packet required** is `S16-15` relabelled VERIFIED. That is
the precise error §9 exists to prevent: `S16-15` is **CONJECTURED** and names a
falsifier that was never run. A second label arm sells `S16-21`'s corroboration
as proof. Both fire.

Two rules are new to this group, because both are whole-paper questions that
could not be asked until the paper was complete:

- **E8 — excluded framing.** Fails on a Group E file; **reports** hits
  elsewhere.
- **E9 — orphaned definitions.** §1 was written to define every term before
  first use; the paper has since *lost* a section, so a defined term may now be
  used nowhere.

---

## 3. Claims

15 claims, `S43-01` … `S43-15`: **9 INSPECTED, 5 VERIFIED, 1 CONJECTURED**.

| id | label | subject |
|---|---|---|
| S43-01 | INSPECTED | §9 drafted; caution stated **before** its discharge |
| S43-02 | INSPECTED | §10 drafted; exactly two questions |
| S43-03 | INSPECTED | Appendix A drafted; mathematics, not errata history |
| S43-04 | INSPECTED | Appendix B drafted; §7's forward reference discharged |
| S43-05 | VERIFIED | gate PASSED, 15/15 arms |
| S43-06 | VERIFIED | stub retired; assembly clean |
| S43-07 | VERIFIED | the whole paper builds, 37 pages |
| S43-08 | INSPECTED | excluded-framing census: 3 hits, all in §1 |
| S43-09 | VERIFIED | orphan census: 28 terms, 5 orphaned |
| S43-10 | INSPECTED | *Newton polygon* vs *Newton–Puiseux*: a terminology mismatch |
| S43-11 | INSPECTED | an inherited reader bound was ill-posed for §10 |
| S43-12 | VERIFIED | the raw/squashed arm defect recurred; given a mechanism |
| S43-13 | CONJECTURED | the §9/§10 split is an interpretation, flagged |
| S43-14 | INSPECTED | a label collision caught before the first build |
| S43-15 | INSPECTED | what the gate cannot see |

---

## 4. Findings — reported, not repaired

### 4.1 Three excluded-framing hits, all in §1 (`S43-08`)

| pattern | where | adjudication offered, not applied |
|---|---|---|
| `Channel Theory` | `section1.tex:50` | inside the **operator-mandated correspondence footnote**, naming a deposit the paper cites by concept DOI. Citing a deposit is not importing its framing. |
| `PCF` | `section1.tex:25` | a **genuine conflict**: the outline's §3.2 excludes it; the §1 packet explicitly ordered it defined. §1 expands it on first use. |
| ρ as an indicial exponent in `u=√z` | `section1.tex:138` | the same conflict, and the outline's exclusion is verbatim this phrase. |

Editing a drafted section is outside this group's remit and the standing rule
is report-don't-repair. **The operator decides.** Note that `PCF` is *also*
orphaned (§4.2), so removing it from §1 would resolve both findings at once.

### 4.2 Five orphaned §1 definitions (`S43-09`, `S43-10`)

Of 28 terms §1 was commissioned to define, 23 are used outside §1. Orphaned:
**Newton polygon, germ coefficient, `c_±`, PCF, `r_∞`**.

`r_∞` is orphaned **by design** — §1 renames it `ψ_∞` and its footnote is the
only place the deposited name may appear. The other four are residue of the
section the paper lost.

**`Newton polygon` is more than an orphan.** §2 writes *Newton–Puiseux
diagram* for the same object, so the paper **defines one name and uses
another**. That belongs in the notation pass as a **unification**, in the same
class as the `R` item the operator ruled should unify rather than separate.

---

## 5. Three defects found in this session's own instruments

**(1) The orphan census first reported EIGHT orphans; three were my reader's
fault.** *System A*, *System B*, *System C* were reported ORPHANED because the
pattern required `\mathsf` immediately after `System`, while the prose writes
`System~$\mathsf C$`. Caught by confirming **every** ORPHANED verdict against
the raw sources with a second, differently-implemented read *before reporting
any of them*: a search for `System` alone returns **84** hits. A check
reporting absence cannot distinguish *the paper does not use this* from *my
reader cannot see it*, and this is the fourth appearance of that shape in the
run.

**(2) An inherited reader bound was ill-posed for §10 (`S43-11`).** Group D's
gate used one bound for every file — ≥4 subsections, ≥8 citations. §10 has
**two** subsections and four citations, and has them because the pre-registered
hazard **requires exactly two questions**. A bound that fails on the structure
the specification mandates is measuring the wrong thing. Repaired by stating
bounds **per file**, and recorded here rather than closed by lowering one
global number until it passed. The truncation arm still fires, so the bound is
not vacuous.

**(3) A documented defect recurred, and was given a mechanism (`S43-12`).**
Arms mutate **raw** text while rules compare **whitespace-squashed** text, so
an arm needle straddling a line break cannot reach its site. CT-S42 recorded
this as `S42-07` and worked around it by hand-picking single-line needles; it
recurred here on the first arm whose needle happened to wrap, and was reported
as **SKIPPED**, not MISSED — which is the only reason it was legible. Repaired
structurally: the arm substitution helper now compiles its needle to a regex
tolerating any whitespace run. **14/15 with one SKIPPED → 15/15 CAUGHT**, with
no change to any drafted file. *A defect that recurs after being documented
needs a mechanism, not another note.*

A fourth, caught before it could become a defect: §9's first subsection was
drafted as `ssec:membership-verdict`, which **§5 already defines and §8 already
references** (`S43-14`). Assembled, it would have been a multiply-defined label
and §8's cross-reference would have pointed into §9. Found by enumerating §0–§8's
labels *before* building rather than by reading the log afterwards.

---

## 6. What was NOT established

- **No displayed formula was re-derived** (`S43-15`). A transposed digit inside
  an equation, or a value wrong in the corpus itself, passes every rule here
  and the clean build. This is the third group report to state this gap.
- **Appendix A is the sharpest case.** Its formulas were transcribed from page
  images and have **no corpus script** to be re-derived against; they can be
  verified only **against the page**. The appendix says so in its closing
  paragraph, and the formula pass must report which route each equation took.
- **Membership remains STRUCTURAL.** The monodromy-and-Stokes falsifier at 30
  digits is still unrun, and no threshold was weakened.
- The gate does not check that a cited claim's text *supports the sentence it
  is attached to* — only that the id resolves and the label matches.

---

## 7. Open questions for the operator

1. **The §9/§10 split (`S43-13`).** Outline §4 lists three items; §10 is to
   carry "two questions, not three". I read the surviving two as outline §4.1
   (the gauge) and §4.3 item 3 (convention independence), placing §4.3's first
   two items in §9 as *limits*, since §9 is titled *Scope and limits*. **That
   reading is not stated in the outline.** Confirm or overturn.
2. **The three §1 exclusion hits (§4.1).** Two are genuine conflicts between
   the outline's §3.2 exclusion list and the §1 drafting packet. Which
   instruction governs?
3. **`Newton polygon` vs `Newton–Puiseux diagram`.** Unify in the notation
   pass — and in which direction?
4. **The notation pass now has twelve items**, not eleven: the nine deferred §1
   collisions, the `R` unification, the `P` separation, and `Newton polygon`.

---

## 8. Uncommitted files

All under `sessions/2026-09-17/CT-S43-DRAFT-E/`. **Nothing outside the session
folder was written.** `git HEAD` unchanged at `08aa0e2`.

```
PREREG.md                       section9.tex        appendixA.tex
REPORT.md                       section10.tex       appendixB.tex
claims.jsonl                    paper.tex           preamble.tex
paper.pdf  paper.log  paper.aux  paper.out
scripts/check_group_e.py        scripts/emit_claims_s43.py
scripts/check_assembly.py       scripts/mutants_assembly.py
scripts/claim_index.py          scripts/check_group_d.py   (template, unrun)
scripts/emit_claims_s42.py      (template, unrun)
outputs/check_group_e.out.txt   outputs/check_assembly.out.txt
outputs/mutants_assembly.out.txt
outputs/claims_s9s10.txt  outputs/claims_appA.txt
outputs/claims_rest.txt   outputs/claims_s25.txt
refs/section0.tex … refs/section8.tex   (staged copies, unmodified)
```

`forwardrefs_E.tex` is deliberately **absent**: every label it declared is now
defined by a section.

---

## 9. Next, in the operator's ruled order

1. **Notation pass** — twelve items (see §7.4).
2. **Formula re-derivation pass** — against final symbols. Equations with no
   corpus script, because they were transcribed from a page image — family
   (4.1), (4.4), `H_V`, and **all of Appendix A** — are verified against the
   **page**, and the pass must report which route each equation took.
