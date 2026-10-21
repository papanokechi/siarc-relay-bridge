# CT-S45-FORMULA-A — formula re-derivation pass, Appendix A

Session folder: `sessions/2026-09-17/CT-S45-FORMULA-A/`
Status: **draft only.** Nothing committed, pushed, tagged, deposited or submitted.
Repository HEAD unchanged at `08aa0e2`.

First instalment of the formula re-derivation pass, the run's one standing gap:
*a transposed digit inside a displayed formula passes every citation check and
the clean build.* Appendix A was taken first, as ruled — its formulas came from
page images, they concern a misprint in someone else's published paper, and they
are the most consequential thing in the document to get wrong.

**It was the right place to start. A displayed formula there was wrong.**

---

## 1. The equation ledger

Every displayed expression in Appendix A, with exactly one route and a verdict.

| # | Expression | Route | Verdict |
|---|---|---|---|
| E1 | `A = z(z−1)(A∞ + A₀/z + A₁/(z−1)) = [[a,b],[c,−a]]` | **P** p. 2655 | MATCHES (appendix prints the expansion; equivalent) |
| E2 | `a(z) = p + ½(−2qt+t−θ∞)(z−q) − ½t(z−q)²` | **P** p. 2655 | MATCHES |
| E3 | `b(z)` first bracket, as printed: `(p+½(q−1)q)²`, no `t` | **P** p. 2655 | MATCHES — the misprint is real |
| E4 | `b(z)` second term carries `(q−1)qt` in both factors | **P** p. 2655 | MATCHES |
| E5 | `c(z) = −(z−q)/(q−1)` | **P** p. 2655 | MATCHES |
| E6 | `det A_i = −θ_i²/4` | **P** p. 2637 | **DIFFERS** — page restricts to `i = 0,1`; repaired |
| E7 | `det A(1)` residual `−¼(q−1)(t−1)(4p+q²t+q²−qt−q)` | **S** | MATCHES |
| E8 | residual at `p=2/7, q=5/3, t=11/4, θ₀=θ₁=0, θ∞=3/5` is `−223/144` | **S** | MATCHES |
| E9 | `B = zB₀ + (1/t)B₁`; `B₁(1,2)` prints `(p+½(q−1)qt)²` **with** `t` | **P** p. 2655 | MATCHES |
| E10 | corrected first term of `b(z)` `= z·B₁[1,2]` | **S** | MATCHES |
| E11 | difference, unfactored, `¼z(4pqt−4pq−4pt+4p+q³t²−…)` | **S** | MATCHES |
| **E12** | **difference, factored, `−¼z(q−1)(t−1)(4p+q²t+q²−qt−q)`** | **S** | **DIFFERS — WRONG SIGN; repaired** |
| E13 | the two tests "agree on the correction term for term" | **S** | MATCHES (ratio is exactly `−z`) |
| E14 | residual vanishes precisely at `t = 1` | **S** | MATCHES |
| E15 | the two readings coincide at `t = 1` | **S** | MATCHES |
| E16 | `c(0) = q/(q−1)` | **S** | MATCHES |
| E17 | arXiv v5 p. 34 prints the same first term, no `t` | **P** p. 34 | MATCHES |
| E18 | arXiv v5 p. 34 `B₁` prints it **with** `t` | **P** p. 34 | MATCHES |
| E19 | `U₀ = C × (C∖{0,1})`, inside quotation marks | **P** p. 2655 | **DIFFERS** — page prints `≅`; repaired |
| E20 | `p = a(q)`, `q` the unique zero of `c(z)` (quoted) | **P** p. 2655 | MATCHES word for word |

**20 expressions: 11 route P, 9 route S, 0 with no route.** Three differed.

---

## 2. The defect

`S16-R18-02`, the appendix's **only `PROVEN`** remark, displayed

```
        printed:   −¼ z(q−1)(t−1)(4p + q²t + q² − qt − q)
        true:      +¼ z(q−1)(t−1)(4p + q²t + q² − qt − q)
```

and the wrong sign sat four lines below the *same quantity written unfactored*,
`¼z(4pqt − 4pq − 4pt + 4p + …)`, which is correct. The two displays in one
remark contradicted each other.

**The cause is diagnosable.** The difference between the readings is exactly
`−z` times the `det A(1)` residual, and that residual genuinely carries a
leading `−¼`. The sign was carried across from the residual without the flip
that the factor `−z` introduces. The appendix's own sentence — that the two
independent tests "agree on the correction term for term" — is true, and is
precisely what made the wrong sign look right.

Nothing downstream depends on it: the correction factor `(q−1)(t−1)(4p+q²t+q²
−qt−q)` is what the argument uses, and it is unchanged. The defect is in the
display, which is exactly the class no citation check and no clean build can
reach.

---

## 3. Claims

Fourteen claims, `S45-01` … `S45-14`, in `claims.jsonl`
(sha256 `7415c3b32a295d42f6190ac5278c443fa95baee15f7f1a969aaadb8423466cc6`),
emitted under 115 pre-write checks against the in-memory buffer.

| id | label | substance |
|----|-------|-----------|
| S45-01 | INSPECTED | The appendix's closing scope note denied it contained any computation; it contains nine |
| S45-02 | VERIFIED | The factored difference carried the wrong sign under a PROVEN label |
| S45-03 | VERIFIED | Cause: the sign copied from the residual without the `−z` flip |
| S45-04 | VERIFIED | Non-vacuity: V1 = 0, V2 ≠ 0, V4 = 0 both readings, 5 bogus variants rejected |
| S45-05 | VERIFIED | Every other computational display re-derives exactly |
| S45-06 | VERIFIED | 8/8 control arms, including a sign-flip arm and two reader-attack HALT arms |
| S45-07 | VERIFIED | Repair verified with the pre-repair file as a discriminating control |
| S45-08 | INSPECTED | The LaTeX reader failed and said so rather than concluding |
| S45-09 | INSPECTED | Folio 2655 read off the page; the misprint confirmed |
| S45-10 | INSPECTED | p. 2637 restricts `det A_i = −θ_i²/4` to `i = 0,1` |
| S45-11 | INSPECTED | Folio 34 read off the page; misprint persists in v5 |
| S45-12 | INSPECTED | `≅` transcribed as `=` inside a quotation |
| S45-13 | INSPECTED | What this pass does not establish |
| S45-14 | VERIFIED | The repaired paper builds at 39 pages, clean |

### Gate results

```
route_s          1 of 16 checked displays DIFFER: E12   (the finding)
                 V1=0, V2≠0, V4=0 both readings, 5/5 bogus variants rejected
mutants_route_s  8 CAUGHT, 0 SKIPPED, 0 MISSED of 8 arms
verify_repair    PASS — repaired matches, pre-repair control rejected
build            39 pages, 0 errors / 0 undefined / 0 multiply-defined / 0 unresolved
```

---

## 4. Findings

**1. A `PROVEN` label does not protect a display.** The wrong sign was inside the
appendix's only `PROVEN` remark. The label attaches to the *argument*, which was
sound; the *typeset expression* was not, and no label mechanism distinguishes
them. This is the concrete instance of the gap that motivated the pass.

**2. Internal inconsistency is detectable without any external source.** The
unfactored and factored forms of one quantity, four lines apart, disagreed.
A check that compared a paper's displays *against each other* would have caught
this with no page image and no corpus script. Cheap, and not currently done
anywhere in the run.

**3. The appendix asserted it contained no computation, and contained nine.**
Its closing scope note told a reader to check it against the page — correct for
eleven expressions, wrong for the nine that are symbolic outputs, including the
one that was wrong. **A scope note that misroutes the reader is a defect in the
check, not in the prose:** it directs verification effort away from the only
expressions a page cannot verify.

**4. The reader failed and said so.** `verify_repair`'s LaTeX parser could not
handle whitespace-separated implicit multiplication and reported `READER
FAILED` for *both* files, returning no verdict. Had it silently parsed a prefix
it would have compared something that was not the display. Repaired by one rule
covering both spellings, not a special case for the string that failed.

**5. The strongest available control for a repair is the pre-repair file.**
`verify_repair` passes the repaired appendix *and is rejected by the text it was
built to catch*. A checker that only passes the repaired text has shown that it
can read, not that it can discriminate.

**6. The emitter's figure rule, tightened per `S44-17`, refused immediately.**
Requiring each figure to resolve to a line that also carries a named anchor
caught that `route_s` never actually *printed* the count `5`. Fixed by making
the evidence report the figure — never by weakening the rule.

**7. CRLF, again — and the post-write assertion was too late.** `write_text`
applied Windows newline translation, so the digest taken over the LF buffer did
not describe the bytes on disk. The read-back caught it, but *after* writing:
the corrupt artefact was on disk, which is the failure the pre-write rule exists
to prevent. Repaired by validating the encoded bytes before writing and using
`write_bytes`.

---

## 5. What was NOT established

- **Route P is eye-inspection of a rendered image**, labelled `INSPECTED`
  throughout and never promoted. A second reader could disagree.
- **Route S establishes that the appendix's computational displays follow from
  *my transcription* of the page.** It does not independently establish that the
  printed page is correct — which is the very thing the appendix disputes for
  one entry. The argument for the correction rests on the source's own
  determinant constraints, not on this pass.
- **Only Appendix A is routed.** Sections 0–10 are untouched by this pass.
- **No check compares the paper's displays against each other** (finding 2),
  though this pass shows that would be productive.
- The transcription itself is not machine-checked against the PDF text layer;
  that was deliberate, since `pdftotext` reorders fraction glyphs by width
  (`S44`'s finding 4) and is not trustworthy for exactly this material.

---

## 6. Open questions for the operator

1. **The `PROVEN` label on `S16-R18-02`.** The argument is sound and the
   corrected display now matches, so the label can stand. But it carried a wrong
   display for the whole run. Should the corpus record that a `PROVEN` claim's
   *typeset form* was defective — a supersession noting the display, not the
   result?
2. **Should a display-consistency check be added** (finding 2)? It is cheap, it
   needs no external evidence, and it would have caught this defect alone.
3. **Appendix A's `≅`/`=` and the `i = 0,1` restriction** were repaired in place
   rather than superseded, since `appendixA.tex` is a draft file and not a cited
   record. Confirm that is the wanted treatment.
4. **Remaining scope.** Sections 0–10 still need routing. The ruled split holds:
   script-derived compared symbolically, page-derived compared against the
   image. Known to have no corpus script: family (4.1), (4.4), `H_V`. Note that
   `H_V` appears on journal p. 2656, for which an image is already in the tree.

---

## 7. Uncommitted files

All inside `sessions/2026-09-17/CT-S45-FORMULA-A/`. Nothing written outside it;
no earlier session modified.

**Record** — `PREREG.md`, `REPORT.md`, `claims.jsonl`

**Repaired** — `appendixA.tex` (sha256 `bdd53f1f…`; pre-repair `43b9e4f2…`)

**Scripts** — `route_s.py` (symbolic re-derivation + vacuity pre-checks),
`mutants_route_s.py` (8 arms), `verify_repair.py` (parses LaTeX to sympy,
pre-repair control), `route_p.py` (page readings with digests and folios),
`emit_claims_s45.py`

**Outputs** — `route_s.out.txt`, `route_p.out.txt`, `mutants_route_s.out.txt`,
`verify_repair.out.txt`, `paper_build.out.txt`

**Build** — `paper.pdf` (39 pp, sha256 `d72c74a4…`) and the section sources
copied from CT-S44 with the repaired Appendix A substituted

**Evidence, copied never referenced in place** — `refs/vdps_p2655.png`,
`refs/vdps_p2637.png`, `refs/arxiv_v5_p34_bz_LOOK.png`,
`refs/arxiv_v5_p34_B1_LOOK.png`, further unused page images,
`refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`, and `refs/appendixA.tex`
(pre-repair; the control for `verify_repair` — never edit)
