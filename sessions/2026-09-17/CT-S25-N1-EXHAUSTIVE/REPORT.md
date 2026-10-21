# CT-S25-N1-EXHAUSTIVE — REPORT

**Result: N1 CLOSES, inside its one-session time box.** The solution set of the
`CT-S16` matching system is **exactly** the two recorded points. `S16-12`'s "for
both sign branches" no longer rests on `sp.solve`.

**The pre-declared fallback was not taken**, and is recorded as unused.

*Governance: nothing was committed, pushed, tagged, deposited or sent. All files
below are uncommitted. HEAD remains `08aa0e2`.*

---

## 1. What was asked and what was done

`S16-12` asserts the solution set is two points, on the strength of
`sp.solve(eqs,[p,q,t,thi],dict=True)` at `CT-S16-MEMBERSHIP-C/locate_final.py:96`.
Two solutions returned is evidence they are **correct**, not that they are
**all**; no completeness argument existed anywhere in the corpus (`S24-05`).

Method: Gröbner elimination over `K = Q(i√11)`, the field the matching
equations' own coefficients live in, **saturated at `q(q−1) ≠ 0`** by a
Rabinowitsch variable — the equations were formed from *numerators*, so any
component inside `q = 0` or `q = 1` is an artefact of clearing denominators and
must be removed algebraically rather than by inspection.

`√3` was deliberately **not** adjoined. The prediction was that the two
solutions are conjugate over `K`; adjoining `√3` in advance would have split
them and made degree 2 appear as two degree-1 components for the wrong reason.

## 2. The result

| quantity | value |
|---|---|
| saturated ideal | **zero-dimensional** |
| degree of the quotient ring | **2** |
| lex eliminant in `θ_∞` | `θ_∞² + 4θ_∞ + 107/27` ∝ `27θ_∞² + 108θ_∞ + 107` |
| roots | `−2 − √3/9`, `−2 + √3/9` |
| lex basis shape | **triangular**: `u, p, q, t` each degree 1 given `θ_∞` |

**The eliminant was predicted in `PREREG.md` §4 before the computation ran**, so
the match is a prediction and not a description (`S25-02`).

**Established twice, independently:**
- **Counting.** Degree 2 bounds the points over the algebraic closure, with
  multiplicity, by two. V1 exhibits two **distinct** points in the variety, so
  each has multiplicity 1.
- **Constructive.** The lex basis is triangular, so each root of the eliminant
  determines **at most one** point. The eliminant has exactly two distinct
  roots. Back-substituting each returns exactly one point, matching the
  corresponding `CT-S16` solution **exactly** (`S25-06`).

**A structural consequence, free with the result.** The two branches are
**Galois conjugate over `K` under `√3 ↦ −√3`** — the same symmetry the operator
identified for `S22-20`. Here it is not an analogy: it is the eliminant's Galois
action, and it is exact.

**Scope, stated so it is not over-read.** This settles only whether `sp.solve`'s
two solutions were all of them. It says nothing about the *derivation* that
produced the six generators, which is `CT-S16`'s and is unchanged.

## 3. The methodological finding — two arms withdrawn, and why

**This is the most transferable part of the session, and it cost more than the
mathematics did.**

**V3** (`PREREG.md` §5) required the degree to move when `b₁ = 0` was dropped.
It did not move, and V3 fired. The main script **halted** and reported
`NOT CLOSED` — no exhaustiveness conclusion was drawn from the degree.

V3's inference was **invalid**: a weaker generating set defines the same variety
whenever the dropped polynomial lies in the **radical** of the others. V3 could
not distinguish **redundancy** from **insensitivity** — the `S23-07` class.

**V3b** (`PREREG-ADDENDUM.md`) was written specifically to discriminate the two,
by dropping each coefficient equation in turn. **It failed the same way**: no
single drop moved the degree. And its inference is **invalid for the same
reason** — six generators in four unknowns cutting out two points is
overdetermined by two, so no single generator need be load bearing.

> **Two arms, in one session, failing in the same class — the second authored
> with the first explicitly in mind.** Knowing about a failure mode did not
> prevent it. Only testing whether the specific check can fail does.

**The diagnosis, which generalises.** *Sensitivity is the wrong instrument test
for an overdetermined system*, because redundancy absorbs any single
perturbation and a null response is uninterpretable however the arm is phrased.

**The stopping rule that mattered.** I did **not** write a third sensitivity
arm. That would have been the start of a regress ending wherever the desired
answer first appeared. The approach was abandoned and replaced with a
**known-answer control** — the `CT-S22` Stage 1 pattern — which does not touch
the target system at all, so overdetermination cannot absorb it.

**`PREREG.md` and `PREREG-ADDENDUM.md` were left unedited**, with the withdrawn
arms and their outputs retained, per the Stage 5A handling.

## 4. The known-answer battery (`S25-05`)

Seven ideals of independently known degree, through the **identical** code path,
in the same ring and field, **with every expected value fixed in
`PREREG-ADDENDUM-2.md` §3 before running**: **7/7.**

Degrees **1, 2, 3, 4, 6** reproduced exactly — a **graded** observable, not a
binary verdict — plus one correctly-detected positive-dimensional case, plus
**row G**, which forces `q = 0` and correctly returns the **empty** variety.

Row G is the arm that matters most: it shows the **saturation is active**, not
inert. That is worth having, because arm **V4** found the *unsaturated* ideal
also has degree 2 — i.e. for this particular ideal the saturation removed
nothing, there being no spurious component on `q(q−1) = 0`. Without row G,
"saturation removed nothing" and "saturation does nothing" would be
indistinguishable.

## 5. A defect I introduced, and what caught it

The four N1 scripts printed a closing `sha256` computed from the **in-memory
string** rather than the bytes on disk. On Windows, text-mode writing translates
`\n` to `\r\n`, so **every printed hash disagreed with the file it named**.

Caught by `emit_claims.py`, which hashes the file **on disk** — the two values
disagreed immediately.

This is a violation of a clause **I wrote this same round**: P0 Amendment B,
"*the hash must be computed from the file on disk, not from the in-memory
string.*" Writing the rule did not stop me breaking it four times in the next
hour; hashing from disk at the point of record did.

**No artefact or claim was affected** — the hash line goes to stdout only and is
not part of any output file, and the claims carry disk hashes throughout. Fixed
in all four scripts. Verified by re-running one under a guard that would have
restored it on any change: printed hash now equals the claim hash
(`79cc5a53…`), and the artefact is **byte-identical**, so the claim remains
valid.

## 6. A mathematical finding beyond the headline (`S25-03`)

`b₁ = 0` lies in the **radical** of the ideal generated by the five coefficient
equations — in fact in the ideal itself, reducing to `0` modulo its Gröbner
basis, and independently confirmed by `1 − v·b₁` generating the unit ideal. The
membership test carries its own control: `θ_∞`, which vanishes nowhere on the
variety, is correctly reported as **not** in the radical.

**Stated positively: matching the two quartics already *forces* the
no-apparent-singularity condition.** It did not have to be imposed separately.
This began as the explanation of a failed arm; it is a result in its own right
and is available to the paper.

## 7. Claims

| id | label | content |
|---|---|---|
| `S25-01` | PROVEN | V1/V2 transcription controls; both recorded solutions annihilate all six generators exactly and lie off the saturation locus |
| `S25-02` | PROVEN | Saturated ideal zero-dimensional of degree 2 over `Q(i√11)`; eliminant matches the pre-registered prediction; branches Galois conjugate; V4 recorded |
| `S25-03` | PROVEN | `b₁ = 0` is in the radical of the coefficient ideal — the matching already forces it |
| `S25-04` | STRUCTURAL | V3 and V3b withdrawn as ill-posed; sensitivity is the wrong instrument test for an overdetermined system |
| `S25-05` | PROVEN | Known-answer battery 7/7 on a graded observable, including the saturation arm |
| `S25-06` | PROVEN | N1 closes: exactly two solutions, by counting and constructively |
| `S25-07` | STRUCTURAL | The paper has no new mathematics left; two operator-gated OUTLINE edits follow |

## 8. What was NOT established

- **Nothing about `CT-S16`'s derivation.** The six generators were taken as
  given and re-derived only to check transcription. If that derivation is wrong,
  this session inherits the error — it proves only that the solver found every
  solution of the system it was given.
- **Nothing about `θ_0 = θ_1 = 0`.** That specialisation is carried in from
  `CT-S16` and was not re-examined.
- **No claim that saturation was necessary here.** V4 says it removed nothing
  for this ideal. Recorded as a finding, not argued away.
- **V3's and V3b's outputs are retained but carry no positive content.** They
  are the record of two withdrawn arms.

## 9. Open questions for the operator

1. **Two `OUTLINE.md` edits, not applied.** §5 item **N1** should be restated as
   **closed**, citing this session; and the §3 line attributing the two branches
   to a solver should be restated as an exhaustiveness result. Both are edits to
   a deliverable already under operator ruling, so neither was made unilaterally.
2. **`S25-03` is new material available to the paper** — that the quartic
   matching already forces `b₁ = 0`. It tightens the exposition (one condition
   rather than two). Include or not?
3. **Should the Galois-conjugacy observation feed back into `S22-20`?** The
   operator's structural argument for the `x₁↔x₂` swap invoked `σ: √3 ↦ −√3`.
   Here that map is exhibited **exactly**, as the Galois action on a degree-2
   eliminant over `Q(i√11)`. It does not by itself prove the Stokes-data
   statement — the Stokes data is transcendental in the entries — but it settles
   that the two branches **are** a `√3`-conjugate pair at the level of the
   parameters, which was previously numerical.
4. **P0 Amendment B is still PROPOSED**, and §5 above is evidence for it from
   the very next session after it was drafted.

## 10. Uncommitted files

```
sessions/2026-09-17/CT-S25-N1-EXHAUSTIVE/
  PREREG.md
  PREREG-ADDENDUM.md              (V3 withdrawn; V3a/V3b declared)
  PREREG-ADDENDUM-2.md            (V3b withdrawn; known-answer battery declared)
  REPORT.md
  claims.jsonl                    (7 claims, S25-01 .. S25-07)
  refs/locate_final.py.copy       (copy; the CT-S16 original is untouched)
  scripts/n1_exhaustive.py
  scripts/n1_v3_adjudicate.py
  scripts/n1_known_answer.py
  scripts/n1_verdict.py
  scripts/emit_claims.py
  outputs/n1_exhaustive.out.txt       990db604…
  outputs/n1_v3_adjudicate.out.txt    3ea51f1d…
  outputs/n1_known_answer.out.txt     79cc5a53…
  outputs/n1_verdict.out.txt          bba7ad3a…
```

Also uncommitted from the same round, in other session folders:
`CT-S24-PAPER-OUTLINE/` (`OUTLINE.md` revision 3, `REPORT.md`, `claims.jsonl`
now 15 rows, `refs/odlyzko_asymptotic_enum.pdf`, `refs/odlyzko_p77.png`,
`scripts/verify_odlyzko_p77.py`, `scripts/emit_claims_rev3.py`,
`outputs/verify_odlyzko_p77.out.txt`, `outputs/verify_outline_rev3.out.txt`) and
`CT-S22-STOKES/P0-AMENDMENT.md` (**append-only**; Amendment B added, Amendment A
unaltered).
