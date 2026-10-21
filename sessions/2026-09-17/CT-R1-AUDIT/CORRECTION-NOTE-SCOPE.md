# Scope for a surface-type correction note

Prepared under operator review #3, ruling 3. **Scoping only — nothing here has
been written into any paper, and no conjecture file has been edited.**

The ruling: *yes, revisit the v1.4 `D₅⁽¹⁾` "correction" — but the note must not
simply revert to PIII(D₆).*

## 1. The diagnosis

The v1.4 error was **treating "the V_quad surface type" as one label.** There are
three distinct objects, and the label is per object. `D₅⁽¹⁾` fits the
*companion's* object; v1.4 attached it to the object *Channel Theory computes on*.

## 2. The three objects, named distinctly

| Object | What it is | Katz multiset | Table 2.1 row |
|---|---|---|---|
| **System A** | Channel Theory's `f(z) = Σ Qₙ zⁿ` ODE | `(1/2, −, 1/2)` — **ramified** | **PIII(D₈)**; its quadratic cover sits in the **PIII(D₆)** row |
| **System B** | `L_φ` | `(0,0,1)`, **up to inversion and rank-1 twist** | **PV / D₅⁽¹⁾** |
| **System C** | the ODE of companion Conjecture 4.1, eq. (6)–(7) | `(0,0,1)` | **PV / D₅⁽¹⁾** |

System B and System C have **identical normal forms** under `z = 1/x`
(PROVEN, `VERIFY-S6.md` §1). System A is ramified, and half-integer Katz
invariants survive twisting, so System A **cannot** be moved into the `(0,0,1)`
row by any change of variable or twist.

## 3. What the note must say

Four points, all mandated by the operator:

1. **Labels are per object.** Name the three objects distinctly in all future
   text. *"V_quad" alone is ambiguous* and is what produced the v1.4 error.
2. **All row matches are necessary conditions only.** Family membership is
   **still open for every object**. Verbatim: *a matching Katz multiset is
   necessary but not sufficient; Table 2.1 classifies families of connections,
   and a single fixed operator matching a row does not make it a member of that
   isomonodromic family until the deformation parameter is specified.*
3. **The PIII(D₆) match is at special parameters** — a codimension-positive
   locus, not generic. Phrase it *"a special PIII(D₆) family"*.
4. **The source of the v1.0–v1.3 PIII(D₆) label is NOT established.** Nothing in
   this run shows which object that label was derived for. **Do not claim the
   old label was right.** The earlier reading in this session — that the old
   label "may have been closer to right than the correction" — is *withdrawn* as
   unsupported: it presumes the old label was about System A, which has NOT been
   shown.

## 4. What the note must NOT say

* Not that System A "is" PIII(D₈) — only that its Katz multiset is that row's.
* Not that the v1.4 correction was simply wrong; it was **misattributed**. The
  `D₅⁽¹⁾` label is defensible *for the companion's object*.
* Not that any of this is machine-checked. Nothing is.

## 5. Evidence base

* `CLASSIFICATION-TABLE.md` §2–3 (Table 2.1 verbatim, p. 2635), §5 (caveats),
  §7 (the CT-S6 results).
* `VERIFY-S6.md` (independent re-derivation).
* `refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`, `refs/vquad_resurgence_v1.2_*.pdf`.

## 6. Status

Scoped, not drafted. Whether this becomes a Channel Theory v1.7 section or part
of the standalone note is an **authoring decision reserved to the operator**.
