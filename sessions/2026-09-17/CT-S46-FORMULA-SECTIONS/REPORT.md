# REPORT — CT-S46-FORMULA-SECTIONS

The second and final instalment of the formula re-derivation pass, covering
sections 0–10. Appendix A was done first, in CT-S45-FORMULA-A, where a
displayed formula was found to be wrong.

**Sections 0–10 required no repair.** Every displayed formula that could be
re-derived or re-read agrees with its source. That is the result, and it is
worth stating plainly alongside CT-S45's, because the pass was commissioned on
the premise that a transposed digit would be invisible — and in Appendix A one
was.

---

## 1. What was done

1. Copied all 15 paper sources into `refs/` and confirmed they are
   byte-identical to the CT-S45 assembly (`S46-16`).
2. Extracted every display in sections 0–10 — **56** — with a reader that
   rejects inline math, rejects LaTeX line-break spacing, and refuses if it
   finds fewer than ten (`S46-01`).
3. Wrote `PREREG.md` **before** any symbolic work, registering falsifier **F5**
   as an advance prediction reached by hand.
4. Re-derived 38 symbolic identities across the displays (`S46-03`–`S46-08`).
5. Built a **routing manifest** assigning each of the 56 displays exactly one
   route, with coverage asserted against the census (`S46-11`).
6. Verified all 9 route-P displays against page images, each folio read off
   the page (`S46-13`).
7. Ran 14 control arms, mutation-tested the emitter, and emitted 17 claims.

---

## 2. Claims

| id | label | in one line |
|---|---|---|
| S46-01 | INSPECTED | 56 displays in sections 0–10 |
| S46-02 | VERIFIED | the `\\[2pt]` extractor defect, and why no count could see it |
| S46-03 | VERIFIED | 38 route-S identities, all residual 0 |
| S46-04 | VERIFIED | `eq:QC`'s 22/22/54/5 correct, **predicted in advance** |
| S46-05 | VERIFIED | `eq:rA` from `eq:sysA` |
| S46-06 | VERIFIED | `eq:rB` routed via `z=1/x`, though System B's ODE is never displayed |
| S46-07 | VERIFIED | section 5's located constants, nine checks |
| S46-08 | VERIFIED | seven restatement checks, incl. §9's reprint of `eq:PC`/`eq:QC` |
| S46-09 | VERIFIED | 14/14 control arms |
| S46-10 | VERIFIED | refusals exited 1, indistinguishable from a finding; now 2 |
| S46-11 | INSPECTED | manifest covers 56/56, 0 unrouted |
| S46-12 | VERIFIED | every cited claim id resolves (1493 corpus ids, positive control) |
| S46-13 | INSPECTED | 9 route-P displays agree with their pages |
| S46-14 | VERIFIED | `jimbo_p1152.png` is folio **1153** — a defect in the tree |
| S46-15 | VERIFIED | DLMF 2.9.6 mechanically confirmed, both controls |
| S46-16 | INSPECTED | no paper file modified this session |
| S46-17 | VERIFIED | the arms overwrote the gate output they are a control for |
| S46-18 | STRUCTURAL | the standing gap is closed for sections 0–10 |
| S46-19 | VERIFIED | the corpus census moved when emission added to the tree it walks |

---

## 3. Findings

### 3.1 The extractor defect that no count could catch

A naive `\[…\]` display pattern matches LaTeX's line-break spacing `\\[2pt]`.
In `section6.tex` this **invented** a display at L69 *and* **hid** a real one at
L92 — the factorisation `3x²+x+1 = 3δ²z(z−1)`. Section 6's total was **6 before
and 6 after**. A check on the count would have confirmed the defect rather than
found it. Only reading the extracted text showed it. Repaired with a negative
lookbehind and locked by a negative control arm.

*Generalisation: when a reader defect can both add and remove, a total is not
an observable.*

### 3.2 A refusal that was indistinguishable from a finding

`route_s_sections.py` used `sys.exit("VACUITY …")`, which exits **1** — the
same code the script uses for "a display DIFFERS". A caller could not tell a
broken instrument from a real defect in the paper. Three halt arms reported
MISSED and exposed it; refusals now exit **2**. The arms were right and my
expectation was right; the script was wrong. Fixed the script, not the arm.

### 3.3 A page image whose filename disagrees with its folio

`jimbo_p1152.png` carries printed folio **1153**, and its content is the
Stokes/connection parametrisation — not the `(α,β,γ,δ)` dictionary that §4
cites to p. 1152. The correct page is held separately as
`jimbo_printed1152.png`, whose folio reads **1152** and which carries all four
parameters exactly as printed.

Had the filename been trusted, `eq:jimbo` would have been reported
**unverifiable** — a false finding against correct prose. This is the S39-02
lesson recurring from a new direction: *resolve the target positively, off the
artefact, never by its path.* The defect is in the tree, not in the paper.

### 3.4 `eq:rB` is routable after all

System B's ODE is **never displayed** in the paper — §3 gives only `r_B` and a
factorisation of `q₂`. So `eq:rB` looked like a route-S-corpus item. But §3
itself states that under `z = 1/x` System B has exactly System C's normal
potential; `z = 1/x` is Möbius, so its Schwarzian vanishes and the potential
transforms as a quadratic differential. `r_B(1/x)/x⁴` is `r_C(x)` exactly.

*A display with no visible source may still be determined by a statement made
about it elsewhere.*

### 3.5 The restatement check, and what the textual one cannot see

CT-S45's headline defect was two displays of one quantity, four lines apart,
disagreeing. The census's near-duplicate check is **textual** and flagged only
one benign pair. It did **not** flag §6's `eq:PC`/`eq:QC` against §9's reprint,
because one is an `align` with `\label` and the other a `\[…\]` — the strings
differ, the mathematics must not. Seven **mathematical** restatement checks now
cover those pairs, with two arms that alter §9's reprint alone.

Pairs whose two printings are textually identical are deliberately **not**
listed: a check comparing an expression with itself passes for no reason.

### 3.6 The advance prediction

`eq:QC`'s `22/22/54/5` is the display the operator named as the
transposed-digit risk. PREREG F5 recorded, by hand expansion and before the
script existed, that it would **MATCH**. It did. A check written after seeing
the answer can only confirm; the prediction is what makes the agreement
informative.

### 3.7 A source that disagrees with itself

Table 2.1 (p. 2635) prints `PIII(D6)` **without** a tilde; p. 2656 prints
`PIII(D̃₆)` **with** one. §1 follows Table 2.1, which is what it says it does.
The variance is van der Put–Saito's own and is not a defect in the paper.

### 3.8 A control harness that overwrote the evidence it controls

`mutants_route_s_sections.py` ran each mutated copy of the real script with the
session root as its working directory. The real script writes
`outputs/route_s_sections.out.txt` — so **every arm overwrote the gate's own
output**, and after a full gate run the file left on disk was the *last arm's*,
reporting `R1 eq:PC == sec9 L39 DIFFERS` for a display that does not differ.

The claims cite that file by digest. Had the emitter not re-read its evidence,
`S46-03` would have carried the digest of a **mutant's** output while asserting
that all 38 displays match.

It was caught because the emitter refused to write. The arms now run in a
scratch directory, and the gate output is byte-identical before and after they
run.

*A control must not be able to touch the artefact it is a control for.*

### 3.9 A census that moved because emitting changed the tree it walks

The manifest's claim-id resolver walked `sessions/**/claims.jsonl` — including
this session's. Emitting 17 claims added 17 ids, so the census printed at
emission time no longer matched the file, and the emitter refused. Repaired by
the CT-S41 precedent: the walk excludes its own output.

This closes the trap **within** the session only. Any later session's
`claims.jsonl` will still move the figure, so `S46-12` asserts no cross-session
reproducibility for it — which is the operator's standing ruling on
corpus-walking censuses.

### 3.10 Three defects, one mechanism

3.1, 3.8 and 3.9 were all surfaced by a check **re-reading its evidence**
rather than trusting an exit code — twice by the emitter refusing to write, and
once by reading extracted text rather than a total. None would have been
visible to a gate that checked only exit status. Each is recorded rather than
quietly repaired.

---

## 4. The routing ledger

| route | count | meaning |
|---|---|---|
| **S-here** | 21 | re-derived symbolically in this session |
| **S-corpus** | 15 | computed by a named corpus claim, not re-run here |
| **P** | 9 | transcribed from a page, verified against the image |
| **DEF** | 11 | the display *is* a definition; nothing determines it |
| **UNROUTED** | **0** | — |

Full per-display table: `outputs/manifest.out.txt`.

Page images read, folio off each page: **2655**, **2656**, **2635** (van der
Put–Saito), **1152** (Jimbo). DLMF 2.9.6 checked mechanically against held
source text.

---

## 5. What was NOT established

- **The 15 route-S-corpus displays were not re-derived.** Their printed forms
  were checked to trace to a resolving claim id, not recomputed. This includes
  every numerical value in §5 (`q`, `p` as exact algebraic numbers), §7's trace
  numerics, `ψ∞`'s 48 digits, `eq:K`, and `eq:gauge`. A transposed digit inside
  one of those remains possible; they are named individually in the manifest so
  the exposure is explicit rather than implied.
- **No proof was checked.** Route S verifies that a display follows from other
  displayed material, not that the surrounding argument is valid.
- **Section 8 and section 10 contain no displays**, so neither was exercised.
- **The paper was not rebuilt** in this session, since no file changed.
- `eq:Ainf` and `det A_i = −θ_i²/4` rest on CT-S45's reading of p. 2637; that
  page was not re-read here.

---

## 6. Open questions for the operator

1. **CT-S45's four questions stand**, chiefly whether the corpus should record
   a supersession noting that a `PROVEN` claim's *typeset display* was
   defective while its result was not.
2. **Should the 15 route-S-corpus displays be re-derived in a third
   instalment?** They are the residue of the standing gap. Re-deriving §5's
   exact algebraic `q` and `p` is the largest single item and the one where a
   transposed digit would be hardest to notice.
3. **`jimbo_p1152.png` is misnamed** (folio 1153). Renaming it would be an edit
   to an earlier session's tree, which the append-only rule forbids. Recorded
   here instead. Does the operator want a rename, or is the record sufficient?
4. **Should the restatement check be adopted run-wide**, as CT-S45's finding 2
   proposed? It is now implemented twice, textually in the census and
   mathematically in route S, and only the mathematical form found anything.

---

## 7. Uncommitted files

All under `sessions/2026-09-17/CT-S46-FORMULA-SECTIONS/`. Nothing was
committed, pushed, tagged or deposited, and no file outside this folder was
modified.

```
PREREG.md
REPORT.md
claims.jsonl
scripts/display_census.py
scripts/route_s_sections.py
scripts/mutants_route_s_sections.py
scripts/manifest.py
scripts/route_p.py
scripts/emit_claims_s46.py
outputs/display_census.out.txt
outputs/route_s_sections.out.txt
outputs/mutants_route_s_sections.out.txt
outputs/manifest.out.txt
outputs/route_p.out.txt
refs/  (15 .tex sources, byte-identical to CT-S45; 6 page images; dlmf_2_9.txt)
```
