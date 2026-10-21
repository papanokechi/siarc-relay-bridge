# REPORT — CT-S41-DRAFT-C (Group C: §5 and §6)

Draft only. Nothing committed, pushed, tagged, deposited or submitted. No
network call. All writes are inside this folder.

---

## 1. What was done

Drafted §5 *Locating the point* and §6 *Removing the projective ambiguity* as
paper prose, from `OUTLINE.md` revision 6 **and from the claim texts
themselves**. Built a drafting gate with nine control arms, repointed the
assembly gate and its seven arms, assembled §0–§6, and emitted twelve claims.

Sections 0–4 are inputs. They were copied into `refs/` and not rewritten.
§0 and §2 were taken from **CT-S40's repaired copies**, not CT-S39's, because
CT-S39's still carry the `sec:local` defect.

| gate | result |
|---|---|
| `check_group_c.py` | **PASSED** — 33 citations, 31 literals, 0 failures, **9/9 arms CAUGHT** |
| `check_assembly.py` | **PASS** — 89 labels, 62 targets, 0 dangling, 0 duplicate, R3 clean |
| `mutants_assembly.py` | **7/7 arms CAUGHT** |
| build `combined_0to6.tex` | **23 pages**, 0 errors, 0 undefined, 0 multiply-defined |
| `claims.jsonl` | 12 claims, **12/12 cited digests resolve**, 20/20 pre-write checks |

The gate's output is **byte-identical before and after emission**, proving the
self-exclusion holds and that no claim cites a digest it invalidated.

---

## 2. Claims, with labels

| id | label | subject |
|---|---|---|
| `S41-01` | VERIFIED | §5 drafted, five subsections, all ids resolved at writing time |
| `S41-02` | VERIFIED | §6 drafted, five subsections |
| `S41-03` | VERIFIED | gate PASSED: 33 citations, 31 literals, 0 failures, 9/9 arms |
| `S41-04` | VERIFIED | **reader defect**: a false C5 hit on `1e-3` |
| `S41-05` | VERIFIED | **two mis-built arms** that could not reach their mutation site |
| `S41-06` | VERIFIED | assembly §0–§6 clean; stub shrunk 6 → 4 entries |
| `S41-07` | STRUCTURAL | both pre-declared drafting hazards honoured and checked positively |
| `S41-08` | STRUCTURAL | **correction**: the outline's "§4.1" is its own numbering, i.e. the paper's §10 |
| `S41-09` | VERIFIED | label census of the Group C citations: 20/4/5/0/0 |
| `S41-10` | STRUCTURAL | what the gate cannot see, stated as a limit |
| `S41-11` | VERIFIED | **the self-exclusion does not extend across sessions** |
| `S41-12` | VERIFIED | **a vacuous reader of my own**, caught while checking `S41-11` |

Label census of the 29 ids the outline assigns to Group C, resolved from the
corpus at writing time: **20 PROVEN, 4 VERIFIED, 5 STRUCTURAL**, 0 superseded,
0 duplicated, 0 unresolved. With the four supporting reads (`S16-01`, `S16-03`
INSPECTED; `S22-20` VERIFIED; `S17-07` CONJECTURED) all five labels of
Amendment F appear in the two sections.

---

## 3. The four defects found

### 3.1 A false C5 hit — the check's reader, not the prose (`S41-04`)

The gate's first run reported that `$10^{-3}$` in §6.2 traced to no claim cited
there. **The prose was correct.** `S17-04` records *"a q perturbed by 1e-3 is
rejected"* — in its `review_note` field, while the checker's pool was built
from the `claim` field alone. PREREG F2 says *"the text of a claim"*; the note
is part of that text, so the check was narrower than the rule it implemented.

This is the third appearance in the record of a check reporting **absence**
when its reader could not see the content. It was diagnosed by reading the raw
claim record **before** editing anything, per Amendment C's symmetry clause,
rather than by repairing the prose until the gate went green — which would have
replaced a correct sentence with a worse one. Both C5 arms still fire after the
widening, because a transposed digit is in neither field.

### 3.2 Two arms that could not reach their mutation site (`S41-05`)

`A-control` searched for `\textbf{PROVEN} (\texttt{S16-07})`; §5 writes the id
first. `A-bounds` commented out `\section`, which does not shorten a file, so
the byte floor never moved. Both scored **MISSED** — for a *staging* reason,
not a detection reason. In a summary line that is indistinguishable from a rule
that does not work. The harness reports `SKIPPED (mutation site absent)`
explicitly, which is the only reason the first was legible; the second was not,
and was found by reading the failure rather than the score.

### 3.3 The self-exclusion does not extend across sessions (`S41-11`)

Emitting this session's `claims.jsonl` changed the output of **CT-S40's**
`draft_check.py`: `451 files / 1411 ids` became `452 / 1421`. CT-S40's gate
walks `sessions/` and prints the census, so every later session moves it.

- **No citation is stranded.** CT-S40's recorded output file on disk is
  untouched; 11/11 CT-S40, 8/8 CT-S39 and 10/10 CT-S41 `output_hash` values
  resolve to a file in their own session.
- **What is lost is reproducibility of the recorded bytes.** Re-running CT-S40's
  gate today no longer reproduces what its claims cite.
- **Verdicts are unchanged.** The diff is exactly the two census lines; both
  upstream gates still exit 0, and CT-S39's output is still byte-identical
  because its gate does not print a corpus census.

**Recorded, not repaired.** Repairing it means either editing CT-S40's recorded
output — append-only forbids it — or removing the census from the gate's
output, which is the non-vacuity statement that makes its self-exclusion check
readable. Both are worse than the defect.

### 3.4 A vacuous reader of my own (`S41-12`)

Checking 3.3, my first confirmation script iterated the upstream claim rows,
read an `output` field, and skipped rows lacking one. **Neither session's
schema has an `output` field** — they carry `script` and `output_hash` only.
Every row was skipped, and the script printed `0/11 cited digests still
resolve`, which reads as total failure and is in fact a count of *zero tests
performed*. This is `S16-11`'s defect in a new place, and §5 quotes that claim
four screens above where I committed it. Repaired by resolving each
`output_hash` against a hash of every file in the session tree, which assumes
no schema.

---

## 4. The two pre-declared drafting hazards (`S41-07`)

Both were written into `PREREG.md` **before drafting**, and both are checked
positively by C6 with an arm that removes each marker.

1. **`θ∞ = −2 ± √3/9`, not `−1 ± √3/9`.** §5.1 names the naive dictionary entry
   `t·θ∞/2`, records that it *failed* all three probes, gives the actual entry
   `t(θ∞+1)/2`, and says the `+1` is the scalar-reduction shift. A reader
   carrying the naive entry finds the value off by one and looks in the wrong
   place. The same shift reappears in §6 as the cause of a self-caught defect
   (`S17-25`), where it produced `√3/9` — wrong by exactly 2.
2. **`ℚ(i√11)`, with `√3` not adjoined.** §5.4 names the field, gives the
   reason (it is where the matching equations' own coefficients live, via `s₊`
   and `δ`), and states what pre-adjoining `√3` would destroy: a degree-2 ideal
   would present as two degree-1 components and the Galois statement would
   evaporate.

The Galois-conjugacy remark states explicitly that it does **not** close the
`z`-dependent gauge question, names it as `S17-07` (CONJECTURED) in §10, and
warns against inferring a connection between two `√3`-flavoured statements.

---

## 5. A correction to the commissioning text (`S41-08`)

`OUTLINE.md` twice says the Galois conjugacy "does not close the gauge question
(**§4.1**)". That `§4.1` is the outline's **own open-questions numbering** —
`OUTLINE.md:678`, *"4.1 The z-dependent gauge, and uniqueness of the
representative"* — and it becomes the **paper's §10**, not the paper's §4,
which is the moduli space.

A drafter following the cross-reference literally would have pointed §5 at
`sec:moduli`. That reference resolves, builds clean, and says something false.
Two numbering schemes share the string "§4.1" in one document; this is the
CT-S26 ambiguity in a different guise, and it is flagged rather than silently
resolved.

---

## 6. What was NOT established

- **No formula was re-derived.** C5 is a *transcription* test. It cannot see a
  value that is wrong in the corpus, and it cannot see a transposition inside a
  numeral of fewer than three digits — which includes **every coefficient of
  `Q_C` in §6.2** (22, 22, 54, 5) and the eliminant's 27. A transposed digit
  there passes 33 citation checks, 31 literal checks and a clean 23-page build.
  This is `S41-10` and it is the argument for the formula re-derivation pass.
- **§6 does not close the gauge question.** `S17-07` remains CONJECTURED.
- **§5's membership remains STRUCTURAL** (`S16-14`). §6 withdraws the *rank-1
  twist* qualifier (`S17-06`) and nothing else; the pre-registered
  monodromy-and-Stokes falsifier at 30 digits was **not run**, and §5 says so.
- **`S17-24`'s limit is carried into the prose**: the separately commissioned
  computation was handed its point, so it is **not** a second independent
  location of a point of `U₀`.
- **`S17-23` is corroboration, not an independent constraint**, and §6 says so
  rather than counting it twice.

---

## 7. Open questions for the operator

1. **`S41-11`** — is a corpus-walking gate allowed to print a census it cannot
   keep stable? The alternatives are a stale recorded digest (current state), a
   silent check, or a census pinned to a frozen manifest. I have recorded the
   defect and changed nothing.
2. **Which wrapper is authoritative at assembly** (carried from CT-S40, still
   open). §3–§6 need `hyperref` for `\texorpdfstring`; Group A's wrapper omits
   it. The combined wrapper loads it. Two standalone builds that are each
   correct and cannot be concatenated without this decision.
3. **The `(P,Q)` versus `(a,b)` letter clash.** §3 writes the projective
   invariant as `R = ¼a² + ½a′ − b` while also using `a(x) = 3x²+x+1` for
   System C's leading coefficient; §6 writes the same invariant as
   `R = P²/4 + P′/2 − Q`. I drafted §6 in `(P,Q)` and did not touch §3. This
   belongs on the **second notation pass** list, which now stands at ten.
4. **`S41-08`** — should `OUTLINE.md`'s two "§4.1" cross-references be
   corrected to "§10", or left as outline-internal numbering with this
   correction standing as the record?

---

## 8. Uncommitted files

All under `sessions/2026-09-17/CT-S41-DRAFT-C/`:

```
PREREG.md                          REPORT.md
section5.tex                       section6.tex
combined_0to6.tex                  forwardrefs_DE.tex
claims.jsonl                       (12 claims, 12295 B)
scripts/check_group_c.py           scripts/check_assembly.py     (repointed)
scripts/mutants_assembly.py        (repointed)
scripts/claim_index.py             scripts/emit_claims_s41.py
refs/section0.tex refs/section1.tex refs/section2.tex            (from CT-S40)
refs/section3.tex refs/section4.tex                              (from CT-S40)
outputs/check_group_c.out.txt      outputs/check_assembly.out.txt
outputs/mutants_assembly.out.txt   outputs/claims_s5.txt  outputs/claims_s6.txt
outputs/build/combined_0to6.{pdf,log,aux,out}
```

Nothing outside this folder was written or modified. `git status` shows only
untracked files under `sessions/2026-09-17/`.

---

## 9. Next

Group **D** — §7 monodromy and Stokes data, §8 leaf transport — then Group
**E**. `forwardrefs_DE.tex` must shrink again as D lands, and `check_assembly`
R2 fails automatically if it does not.
