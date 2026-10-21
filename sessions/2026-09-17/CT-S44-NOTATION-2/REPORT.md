# CT-S44-NOTATION-2 — second notation pass

Session folder: `sessions/2026-09-17/CT-S44-NOTATION-2/`
Status: **draft only.** Nothing committed, pushed, tagged, deposited or submitted.
Repository HEAD unchanged at `08aa0e2`.

---

## 1. What was done

The operator commissioned the second notation pass — twelve ruled items, applied to
the assembled thirteen-file paper after group E, "when every section exists and the
residue is real rather than pending."

The pass was executed as: copy the assembled paper into the session root, keep a
pristine pre-pass copy of every file in `refs/`, apply the ruled repairs to the root,
and certify the result with a purpose-built **rendered token-sequence diff** between
the two builds, under a declared manifest of intended changes and eight control arms.

### The ruled items, as applied

| # | Ruling | Applied |
|---|--------|---------|
| N1 | ρ: remove, don't import | §1's Borel-exponent definition deleted; replaced by a paragraph stating ρ is *not* a paper symbol, plus the senses that do occur; ρ added to the correspondence footnote as the deposited convention |
| N2 | Unify Newton polygon | §2 L22 `Newton--Puiseux diagram` → `Newton polygon`, following §1 and the cited sources |
| N3 | Unify R | §3's `R = ¼a² + ½a′ − b` → the general `R = ¼P² + ½P′ − Q` of §1, at `(P,Q) = (a,b)` |
| N4 | Separate P | §8 writes `−det A` and names it; the determinant sense no longer shares the letter with §3/§6's operator coefficient |
| N5–N8b | Symbol-index residue | `M`, `A`, `L`, `u`, `β`, `r` — see §3 below |

**The unify-R ruling was applied in the opposite direction to the one stated,
because the premise was wrong.** The operator ruled "§6's is the general form;
§3's is it with (P,Q) = (a,b)", expecting §3 to be folded into §6. §1 already
carries the general form at L194. §3 was the outlier, and it was unified into §1.
Reported rather than silently reconciled.

### Source edits (all in the session root; no earlier session modified)

`section0.tex` ×2 · `section1.tex` (most edited) · `section2.tex` L22 ·
`section3.tex` L43 · `section5.tex` ×2 · `section7.tex` · `section9.tex` ×1.

---

## 2. Claims

Seventeen claims, `S44-01` … `S44-17`, in `claims.jsonl`
(sha256 `579725f1b72d22735c4ed3ccdde0111d293181d9ccf9fac564f92b4ed8836030`),
emitted under 136 pre-write checks against the in-memory buffer.

| id | label | substance |
|----|-------|-----------|
| S44-01 | INSPECTED | ρ of the deposited record is not a paper symbol; it moves to the correspondence footnote |
| S44-02 | VERIFIED | §1's "ρ carries two meanings" was false; the paper uses ρ in four senses, none of them §1's |
| S44-03 | INSPECTED | §7 used ρ as an undefined step-size scale; replaced by the step counts the claim supports |
| S44-04 | INSPECTED | §2 unified to Newton polygon |
| S44-05 | INSPECTED | §3's normal potential unified to §1's general form |
| S44-06 | VERIFIED | P separated: determinant vs first-order coefficient |
| S44-07 | INSPECTED | Moduli space unified to `\mathcal M_{t,λ}`, vdPS's own form |
| S44-08 | INSPECTED | §5's `r_1` — a fifth sense of an already-ambiguous letter — retired |
| S44-09 | INSPECTED | §5's bare scalar `A` renamed κ |
| S44-10 | INSPECTED | §1 gains the six-bullet conventions paragraph |
| S44-11 | VERIFIED | Residue re-measured: 13 files, 138 537 chars, 185 occurrences, 61 of them `A` |
| S44-12 | VERIFIED | The gate compares token *sequence*, not the anagram-blind multiset used at CT-S38; 20 regions, 8/8 arms |
| S44-13 | VERIFIED | Repaired paper builds at 39 pages, 0 errors, 0 undefined, 0 multiply-defined |
| S44-14 | VERIFIED | CT-S43's 37 pages is not reproducible — `supersedes: S43-07` |
| S44-15 | INSPECTED | The gate's declaration is not blind; two declarations were found wrong by the gate itself |
| S44-16 | VERIFIED | The first census measured a transient half-repaired tree; corpus now resolved positively, 3/3 arms |
| S44-17 | INSPECTED | The emitter's numeric check is satisfied by any occurrence, including a line number |

Two claims supersede rather than edit: `S44-14` (CT-S43's page count) and the
corrected text of `S44-11`. No earlier session's files were touched.

### Gate results

```
rendered_diff      GATE PASSED: 20 differing regions, all accounted for;
                   no undeclared numeric change in 13 source files
rendered_diff      --arms   8 CAUGHT, 0 SKIPPED, 0 MISSED of 8
check_assembly     VERDICT: PASS   (13 sections, 124 labels, 76 targets, 0 stub entries)
mutants_assembly   7/7 arms CAUGHT
mutants_census     3 CAUGHT, 0 SKIPPED, 0 MISSED of 3
build              39 pages, 0 errors / 0 undefined / 0 multiply-defined, converged over 4 passes
```

`claims.jsonl` is byte-identical across the emit → re-run-all-gates → re-emit cycle.

---

## 3. Findings

The ones worth carrying. Each cost a wrong answer first.

**1. A repaired false sentence can still be false.** §1 said "the letter ρ carries
two meanings". That was already CT-S38's repair of the stronger false claim "ρ is
never used for anything else". The paper uses ρ in four senses — characteristic
roots (§2), growth base (§2), System B's singular points (§3), and an entirely
undefined step-size scale (§7) — and **none of them is the Borel-plane exponent §1
defined as primary.** Re-measure after a repair; the repair is not evidence.

**2. CT-S43's 37 pages is not reproducible.** Its own byte-identical inputs, layout
and jobname rebuild to 38. Verified by reconstructing CT-S43's exact tree in
`outputs/scratch_s43/`. Its gate read `paper.log` instead of rebuilding, so it could
not see this. Superseded, not edited.

**3. A count rendered as a finding is not a finding.** The diff's first run gave 48
failures; they were one cause — the document gained a page, so every page number
shifted. Stripped per page, deliberately *not* by filtering integers globally, which
would hide exactly the digits the formula pass exists to check.

**4. `'12'→'21'` was not a transposition.** `pdftotext` positions `\tfrac12`'s glyphs
by width; renaming `A` → `κ` (wider) reorders them. PyMuPDF shares that sensitivity,
so it is **not an independent second extractor for this failure mode** — independence
is about the failure mode, not the implementation. Resolution: move the question to
the LaTeX source, where `\tfrac12` is `\tfrac12` and the question is decidable.

**5. Declaring a delta you have not computed is guessing.** §5's numeric delta was
declared `{1:+2, 9:+2}`; measured `{1:−1, 9:+1}`. The check caught its author.
Redesigned around the invariant that matters — no numeric literal may be *lost or
altered* — since a transposition turns one literal into another and so registers as
an undeclared loss. Gains from new prose are a reported census, not a failure.

**6. The unchanged-source excuse had a hole.** An inserted word sits beside untouched
prose exactly as a relocated superscript does. Found by arm A1; fixed by requiring
the hunk's *own* words to occur in untouched source; locked by new arm A8.

**7. Raw-vs-squashed, a third time** (S42-07 → S43-12 → here). Arms mutate raw
extracted text; rules compare joined tokens; a needle straddling a line wrap yields
SKIPPED. Fixed structurally, not by hand-picking single-line needles.

**8. Pre-pass copies in `refs/` are a live hazard.** Both `paper.tex` and
`check_assembly.py` arrived pointing at them. Unrepointed, each would have certified
the *unrepaired* document — the operator's own ruling-2 hazard, "a check passing on a
document nobody will build."

**9. A census that names its corpus by path certifies whatever is at that path.**
The first census ran mid-pass, against a tree some repairs had reached and others had
not. It reported figures matching neither corpus, and that state no longer exists.
This was invisible until the script was re-run and **its own output changed underneath
a claim that quoted it.** The census now names `prepass` or `repaired` and resolves it
*positively* by a marker each tree carries and the other does not. Three arms,
including a negative arm where a neutral edit must *not* fire the guard.

**10. A numeral in a file does not evidence that quantity.** The emitter confirms
numbers by searching the evidence file for the digit string anywhere. S44-11's
superseded text cited a count for `A` that passed **solely because the same digits
occur as a line number in the census listing** — the right verdict for the wrong
reason, on a figure that was in fact unreproducible. Same shape as the proximity
finding already recorded. Reported as a limit, not silently patched.

**11. CT-S38's index measured a smaller object** — theorem.tex, §1 and OUTLINE.md,
before §2–§10 existed. §5's `r_1`, §5's scalar `A`, §7's undefined ρ and the
three-way moduli spelling were all invisible to it. The deferred residue had to be
re-measured, not inherited.

---

## 4. What was NOT established

- **No displayed formula was re-derived.** This remains the run's one standing gap:
  a transposed digit inside an equation passes every check here and the clean build.
  The formula pass is the commissioned next step.
- **The gate is not blindly pre-registered.** Its `REPAIRS`/`ACCOUNTED` manifest was
  completed iteratively against the diff it certifies. Stated in `PREREG.md` §0 and
  claimed as a limit at `S44-15`; its authority rests on 8/8 arms, not on the
  declaration.
- **Punctuation is unpoliced** by the diff, by an explicitly stated artefact class.
- **Fraction glyph order is undecidable in the PDF** — see finding 4. The numeric
  invariant is enforced on the source instead.
- **Why CT-S43's log says 37** is established as a fact but not diagnosed;
  presumably a build predating the label-collision rename or the stub retirement.
- **The emitter's numeric check** is weaker than its pass rate suggests (finding 10).

---

## 5. Open questions for the operator

1. **`S43-13`** — the §9/§10 split interpretation, CONJECTURED — has never been
   ruled on. Carried forward unresolved rather than settled silently.
2. **The unify-R ruling's premise was wrong** (§1, not §6, carries the general form).
   Applied to §1. Confirm that is what was intended.
3. **CT-S43's page count** is superseded by `S44-14`. Confirm supersession rather
   than amendment is the wanted treatment for a build-artefact figure.
4. **Formula pass ordering** is as ruled: Appendix A first, one page image per
   message, folio read off the page, since its formulas concern a misprint in
   someone else's published paper and came from page images rather than any script.
   Known to have no corpus script: family (4.1), (4.4), `H_V`, and all of Appendix A.

---

## 6. Uncommitted files

All inside `sessions/2026-09-17/CT-S44-NOTATION-2/`. Nothing written outside it.

**Record** — `PREREG.md`, `REPORT.md`, `claims.jsonl`

**Paper (repaired)** — `section0.tex` … `section10.tex`, `appendixA.tex`,
`appendixB.tex`, `preamble.tex`, `paper.tex`, `paper_prepass.tex`

**Builds** — `paper.pdf` (39 pp, sha256 `065967c0…`), `paper_prepass.pdf` (38 pp,
sha256 `64deab2f…`), plus `.aux` / `.log` / `.out` for both

**Scripts** — `rendered_diff.py` (the pass's main instrument), `symbol_census.py`,
`mutants_census.py`, `check_assembly.py`, `mutants_assembly.py`,
`emit_claims_s44.py`, `claim_index.py`

**Outputs** — `rendered_diff.out.txt`, `rendered_diff_arms.out.txt`,
`check_assembly.out.txt`, `mutants_assembly.out.txt`, `symbol_census.out.txt`,
`symbol_census_prepass.out.txt`, `mutants_census.out.txt`, `emit.out.txt`,
`scratch_s43/paper.log`

**Baseline** — `refs/*.tex`, fifteen pristine pre-pass copies, byte-identical to
CT-S43. Never edit; never let a gate point at them.
