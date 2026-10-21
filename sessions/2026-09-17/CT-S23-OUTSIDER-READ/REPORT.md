# CT-S23-OUTSIDER-READ — REPORT

Session `sessions/2026-09-17/CT-S23-OUTSIDER-READ/`.
Nothing committed, deposited or sent. Repo HEAD unchanged.

**Outcome in one line.** The packet did not exist and was assembled here; the
cold read was dispatched to two isolated contexts rather than performed by the
assembling agent; the instrument was shown to discriminate; and the return is
**NOT SELF-CONTAINED** — while simultaneously confirming the operator's premise,
because the reader reconstructed the main result and the method correctly from
the packet alone. Followability and self-containment came apart, and that
separation is the result of this session.

---

## 0. Two findings that precede the tasks

### 0.1 The packet did not exist

The task lists the packet under **PROVIDED**. There is no paper draft in this
repository and no assembled packet file. Every *source* the task names does
exist — `CT-S16-MEMBERSHIP-C`, `CT-S17-TRACEFREE-NORM`, `CT-S20B-COMPONENT`,
`CT-S22-STOKES`, the companion v1.3 correction notice — as do all the page
images: van der Put–Saito pp. 2634–2637 (Table 2.1 is on **p. 2635**) and
Jimbo p. 1152.

So this is not a halt for missing data. It is a mis-description of state, and
the packet had to be **assembled** before it could be read. `packet/PACKET.md`,
30,002 characters, sha256 `a62b7b86…`, is that assembly. (`S23-01`)

**The assembly rule, fixed before writing: faithful transcription, not repair.**
Definitions are carried where the sources give them and are *not* invented where
they do not. Had I written the best self-contained paper I could, the audit
would have tested my writing rather than the material. This rule is what makes
the return interpretable — and, as §4.3 shows, it is also what let one real
defect through, which the reader then caught.

### 0.2 I could not be the cold reader, so I was not

The task specifies a reader who is cold and isolated. The assembling agent holds
all five sources in context and cannot discard them. **A self-containment audit
performed by a reader who can silently supply every missing definition from
memory is structurally incapable of detecting the defect it is looking for.** It
would return a confident, fully-documented verdict for reasons having nothing to
do with the packet.

That is the Stage-5A shape: not a check that cannot fail, but a check that would
pass or fail *for the wrong reason*. Declaring the contamination in prose and
proceeding anyway would be a caveat standing where a control is required.

The read was therefore dispatched to **two separate contexts**, each given a
single path and instructed to read no other file, run no search outside the
packet directory, and consult no external source — with the instruction that if
tempted to look something up to fill a gap, the temptation is itself the datum
and must be recorded as a gap. The assembling agent assembles, controls and
adjudicates; it does not answer tasks 1–5. (`S23-02`)

---

## 1. The instrument was tested before its output was used

A verdict of NOT SELF-CONTAINED is worthless if the reader would have returned it
for anything. So a **control fragment** was dispatched under the *identical*
prompt: `packet/control/CONTROL-FRAGMENT.md`, the bare results table stripped of
all definitions, which is not self-contained by construction.

| | verdict | task-2 items |
|---|---|---|
| **packet** | NOT SELF-CONTAINED | **171** |
| **control** | NOT SELF-CONTAINED | 106 |

- **F1 — instrument validity — did not fire.** The control was required not to
  return SELF-CONTAINED and to list ≥ 5 task-2 items; it returned NOT
  SELF-CONTAINED with 106. (`S23-05`)
- **F2 — sensitivity — did not fire.** `scripts/jargon_index.py` computed, from
  the packet and *before either read was dispatched*, the set `G` of
  pre-declared core terms used before defined:
  **`{System C, K, Katz multiset, PV, D̃₅}`**. The main read's task-2 list
  contains **all five**: `5/5 = 1.00` against a threshold of `0.50`. (`S23-06`)

`G` and its threshold were hashed (`a4fd37ac…`) before dispatch, so neither could
be adjusted afterwards.

### 1.1 A pre-registered vacuity arm fired, and it is ill-posed

`PREREG` §4 arm (i) says the observable must move when the packet moves, and
encodes that as: **if both reads return the same verdict, the exercise is void.**

Both returned NOT SELF-CONTAINED. **Arm (i) fired.**

It is reported, not repaired. The arm was written on the assumption that the
packet would come back SELF-CONTAINED, so it treated *verdict divergence* as the
signal that the instrument reads its input. It cannot distinguish an insensitive
instrument from two documents that are **both genuinely not self-contained** —
which is what the item counts, 171 against 106, and the `G`-overlap indicate is
the actual situation. As written the criterion is **ill-posed**, and per P0 an
ill-posed threshold is a finding rather than something to adjust. (`S23-07`)

This is the same class as `S22-10`, where a pre-registered candidate set could
not represent the relation that actually held. It is also an internal
inconsistency in my own PREREG: §3's F1 and §4's arm (i) return opposite
verdicts on the same data. F1 and F2 survive it because both are independent of
the verdict.

**Net disposition:** the instrument discriminates and the read is sensitive, so
its **content is admissible**; its **verdict** is reported with the arm-(i)
qualification attached and is not treated as decisive on its own.

### 1.2 The classifier control failed first, and the classifier was right

`jargon_index.py`'s first run **halted before emitting `G`**. Its sentinel term —
"normal potential", assumed defined early and used late — came back UNDEFINED.

The sentinel was wrong, not the classifier: "normal potential" is first *used* in
§2 (Proposition 5) and only explained in §3. The correct verdict was UNDEFINED.
Recorded rather than quietly re-tuned, and the arm was replaced by four synthetic
arms exercising all three branches plus **two live hand-adjudicated arms** read
off the packet by hand (`U₀` → defined; `Katz multiset` → undefined). All six
pass. (`S23-03`)

The live arms are there because a constructed rehearsal checks the code against
the definition and never the definition against the material.

A **degeneracy pre-check on the term set itself** was also run, per the clause
proposed in `CT-S22-STOKES/P0-AMENDMENT.md`: 399 candidate alias pairs tested,
none found, so `|G|` is not inflated by terms that cannot be independently
missed. The pre-check asserts that it tested something, so it cannot pass
vacuously. (`S23-04`)

**One further catch, by the corpus checker rather than by a reader.** `S23-10`
was first emitted as **PROVEN** on `evidence_type: file_inspection`, and
`check_invariants.py` invariant 1(a) rejected it. The checker is right: that the
packet's `(A1)` conflates the source's `(A1)` and `(A2)` is established by
reading two documents, which is INSPECTED. Corrected before the report was
final; no other label moved.

---

## 2. Task 4 first, because it is the operator's actual question

The operator's premise was that *a reader unfamiliar with the corpus could now
follow the material end to end*. Task 4 is the only task that tests that
directly, so it is reported first.

**The reader reconstructed the result and the method correctly.** Unprompted, and
with no access to any session file, it returned:

> System C … **is shown by an overdetermined symbolic and numerical comparison to
> correspond to a point of the type-`(0,0,1)` rank-2 moduli space and hence to lie
> on a Painlevé V isomonodromic leaf.** … the packet explicitly limits this to
> confirmation at stated precision rather than a proof.

and a nine-step method that includes, correctly and in the right order:

- step 6, *"Verify exact equality of the scalar coefficients `(P,Q)`, **thereby
  removing the projective/rank-1-twist ambiguity**"* — the point of §6, which is
  the one step in the whole argument whose *purpose* is easiest to lose;
- step 7, *"Select monodromy/Stokes conventions by an **overdetermined** 16-way
  numerical test"* — carrying the word that distinguishes a convention *derived*
  from one *assumed*;
- the secondary result, that the branches are related algebraically while their
  Stokes data are computed separately, and that the `ζ*` constant has no closed
  form *in the stated search space*.

It also kept the precision-not-proof limit and the "stated search space"
qualifier without being asked. **The premise is confirmed.** (`S23-09`)

**This is the finding of the session: followability and self-containment are
different properties, and the material now has the first without the second.**
The task's five questions treat them as one. A reader can follow the argument end
to end and still be unable to reproduce it, because reproduction requires the
cited source and the omitted computations. That is the ordinary condition of a
paper, not a defect — but it means the verdict in task 5 must not be read as
"the material is not ready".

---

## 3. Tasks 1 and 3 — what the reader could not proceed on

The reader's task-1 and task-3 returns are in `outputs/coldread_main.txt`
(sha256 `8660122a…`), 31 items under task 3. They fall into four kinds, and the
distinction matters because only one kind is repairable by writing.

| kind | examples | repairable in the paper? |
|---|---|---|
| **(a) Omitted proofs** | Propositions 1–4 asserted without proof; the completeness of the two-branch solve; the theorem linking rational Riccati solutions to reducibility | **Yes** — these are proofs that exist in the corpus and were not transcribed |
| **(b) Omitted computations** | the five-equation solve, the `(P,Q)` comparison, the 16-convention test, the Taylor transport, the PSLQ search, the `det A(1)` typo check | **Partly** — by stating the algorithm and the residual; full reproduction needs the scripts |
| **(c) Imported from the cited source** | family `(4.1)` printed only in part; `H_V` `(4.5)` and the flow `(4.4)` never printed; the strong-Riemann–Hilbert positivity; `P` as the base of a cubic-surface fibration | **Yes, and cheaply** — these are short and the source is supplied |
| **(d) Undefined objects** | see §4 | **Yes** |

The sharpest item in kind (c): **the packet asserts that exactly one leaf passes
through the point because the vector field `(4.4)` is regular there, and never
prints `(4.4)` or `H_V`.** The reader flagged this twice, under both task 1 and
task 3 (item 15). The load-bearing object of §5.5 is not in the document.

---

## 4. Task 2 — used before defined

The reader produced **171 items**. Three groups are worth separating.

### 4.1 What the mechanical index also found

All five of `G` — `System C`, `K`, `Katz multiset`, `PV`, `D̃₅`. Of these, `Katz
multiset` and `D̃₅` are used in the §2 table with **no definition anywhere**, and
the Katz invariant is the quantity on which the entire object classification
turns.

### 4.2 What the index could not reach, and the reader did

The index scored a pre-declared list; the reader scored the document. It caught,
among others: `Γ`, `O(·)`, `o(1)`, `~`, `dps`, `mpmath`, `PSLQ`, "Richardson
levels", "formal solution", "action", "characteristic root", "Newton polygon",
"germ coefficient" (never defined), "amplitude", `c_±`, the ellipsis in the PSLQ
basis, and the meaning of "`N/2`-vs-`N` agreement".

The index and the reader are therefore not redundant: the index exists to
*score* the reader, and it caught nothing the reader missed.

### 4.3 A real defect the reader found, introduced in assembly

> "**(A1), (A3)** — labels are introduced, but **(A2)** is absent and never
> explained."

Checked against the source. `CT-S3B-RINF/DERIVATION.md` L22–27 carries **three**
hypotheses:

- `(A1)` `b(k) ≠ 0` for every integer `k ≥ 1`;
- `(A2)` no root `r_i` is a positive integer — equivalently `Γ(1 − r_i)` is
  finite;
- `(A3)` `r_∞` exists and is nonzero.

The packet's `(A1)` **silently conflates the source's `(A1)` and `(A2)`** and
leaves `(A3)` dangling after a missing label. `(A2)` is not decoration: it is
exactly what makes `Γ(1 − r_i)` finite, and therefore what makes `K` well-defined
at all. This defect was introduced by me in assembly, not present in the source,
and it was caught by a reader who had never seen the source. (`S23-10`)

### 4.4 A collision that *is* in the source material

> "`r_1,…,r_d` … defined there, but the notation conflicts with the earlier
> sequence `r_n`."

and, on the PSLQ basis, "`r₁` … ambiguous with the roots `r_i` and the sequence
term `r_1`". Three different objects share the letter `r`: the normalised
sequence `r_n`, the roots `r_1..r_d`, and the limit `r_∞`. The basis entry `r₁`
is genuinely ambiguous. This one is not an assembly artefact. (`S23-11`)

### 4.5 Four names the task asked about that are not in the packet

The task's task-2 list names `V_quad`, `Channel Theory`, `PCF` and the
`B1/B2/B3` tiers. The mechanical index reports all four **ABSENT** from the
packet. Three of them because the assembly named the objects
mathematically instead (`A`, `B`, `C`; "the quadratic recurrence"). The fourth is
different and is a genuine gap:

**`B₁, B₂, B₃` are not "tiers".** They are van der Put–Saito's monodromy matrices,
and on p. 2637 they carry `a_i = tr(B_i)` and
**`x₁ = tr(B₂B₃)`, `x₂ = tr(B₁B₃)`, `x₃ = tr(B₁B₂)`** — which is the *definition
of the packet's central observable*. The packet calls `x₁, x₂, x₃` "the
comparison quantities" and "trace coordinates" and **never says traces of what**.
The definition exists on a page image that was supplied, but the packet never
points at it.

---

## 5. Task 5 — verdict, adjudicated

The reader returned **NOT SELF-CONTAINED**.

Adjudicated: **the return is admissible as to content** (F1 and F2 both clear)
and **its verdict is qualified** by arm (i) having fired. On the evidence, the
correct disposition is:

> **SELF-CONTAINED AFTER LISTED REPAIRS**, where the repairs are the four kinds
> in §3 — of which kinds (c) and (d) are cheap and kind (a) is transcription of
> proofs that already exist — and **NOT SELF-CONTAINED as it currently stands.**

The two are not in tension: the reader was asked for the state of the document,
and the document as assembled omits the objects listed. I record my own
adjudication as **STRUCTURAL**, and the reader's verdict as what it is — the
return of an instrument whose discrimination was established in advance.

**No label is raised anywhere in this session on the strength of the reader
agreeing with anything.**

---

## 6. What was NOT established

- **Whether the sources are self-contained.** This session tested *an assembly*
  of them. A different assembly would return differently, and the `(A2)` defect
  of §4.3 shows the assembly can introduce gaps that the sources do not have.
- **Whether the repairs in §3 are sufficient.** They were not made and the read
  was not repeated. A second read after repair is the only thing that would
  establish it, and it must use a *fresh* context for the same reason §0.2 gives.
- **Correctness of any mathematics.** Both readers were instructed to assume the
  mathematics is right, and did.
- **Any claim about the reader's reliability beyond F1 and F2.** Those two
  measure discrimination and sensitivity. They do not measure whether the
  reader's 171 items are individually correct; two were checked by hand (§4.3,
  §4.4) and both held.

---

## 7. Open questions for the operator

1. **Does the paper print `(4.4)` and `H_V` `(4.5)`, or cite them?** §5.5's
   conclusion rests on regularity of a vector field the packet never shows. This
   is the single most load-bearing omission the read found.
2. **Where is `x₁ = tr(B₂B₃)` stated?** The central observable is undefined in
   the packet. The definition is on a supplied page image; a one-line pointer
   closes it.
3. **Is `(A2)` restored, and are the three `r`-objects renamed?** §4.3 is mine to
   fix; §4.4 is in the source material and affects the deposited text.
4. **Should the repaired packet be re-read cold?** If so it needs a fresh
   context and a new control, and arm (i) must be re-specified — see 5.
5. **Arm (i) needs replacing, not deleting.** The right form is probably a
   *graded* observable (task-2 item count, or `G`-overlap) rather than the
   verdict, since the verdict is three-valued and coarse. That is a change to a
   pre-registration and is the operator's call, not mine.

---

## 8. Uncommitted files

All under `sessions/2026-09-17/CT-S23-OUTSIDER-READ/`:

- `PREREG.md` — written before the packet was assembled and before either read
- `REPORT.md` — this file
- `claims.jsonl` — 11 claims
- `packet/PACKET.md` — the assembled packet, sha256 `a62b7b86…`
- `packet/control/CONTROL-FRAGMENT.md` — the instrument control
- `packet/pages/` — `vdps_p2634.png`, `vdps_p2635.png`, `vdps_p2636.png`,
  `vdps_p2637.png`, `jimbo_p1152.png`
- `scripts/jargon_index.py`, `scripts/adjudicate.py`, `scripts/emit_claims.py`
- `outputs/jargon_index.out.txt`, `outputs/adjudicate.out.txt`,
  `outputs/coldread_main.txt`, `outputs/coldread_control.txt`

Repo HEAD unchanged; nothing committed, deposited or sent.
