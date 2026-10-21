# Load-bearing test for the three deferred claims

Operator ruling (review #9): *for each claim, ask — if it were false, would any
sentence in the notice change?* Load-bearing ⇒ cold-read before deposit.
Corroborating only ⇒ leave `self` and list it as such.

---

## `R1-56` — the `dim P = 0` reading — **LOAD-BEARING**

**Claim.** `P` is the *parameter* space of the family, so `dim P = 0` means
PIII(D₈) has no free parameters; that is expected, not a defect; and it says
nothing about the isomonodromic *time*, which still gives a one-dimensional
deformation. The link CT-S13 drew to C3's single-fibre concern is a conflation.

**Test.** C4 point 7 exists **only** to say this. If `R1-56` were false — if
`dim P = 0` did bear on the time variable, or if `P` were something other than
the parameter space — point 7 would not merely be softened, it would be wrong in
its main assertion, and the removed link to C3 would have to be restored.

Nothing else in the notice supplies point 7's content. The page-image quote
defining `P` is independently INSPECTED, but the quote alone does not establish
the *inference* from it, which is what `R1-56` is.

**Verdict: load-bearing. Cold-read before deposit.** → Statement 1 of
`PACKET-E-deferred.md`.

Worth noting: `R1-56` originated as an operator correction. That does not exempt
it. The P0 rule adopted at review #7 says findings are adopted claim by claim and
that a correct finding does not certify the reasoning around it; and the test
just applied is about load-bearingness, not authorship.

---

## `CT-S9-PVPARAMS-C014` — no Lax embedding from scalar data — **CORROBORATING ONLY**

**Claim.** The scalar local data alone do not exhibit a Jimbo Lax embedding or a
PV deformation time for System C.

**Test.** Suppose it were false — suppose the scalar local data *did* exhibit an
embedding. Which notice sentence changes?

* *"The Painlevé V time is fixed, not free… the operator is a single fibre."*
  This rests on the **affine-matching computation** (`k = 2/√3`, `t = ∓2i√33/9`),
  which is separately **cold** reviewed, not on `C014`.
* *"Whether it embeds in an isomonodromic Painlevé V deformation is **open**."*
  This asserts **openness**. If an embedding were later exhibited, the notice
  would not become false; it said the question was open, and someone would have
  closed it.

So no notice sentence rests on `C014` alone. Its role is to corroborate a
conclusion the notice states in the weaker, safer form.

**Verdict: corroborating only. May remain `self`, listed as such.**

---

## `R1-57` — quadratic-cover route to strong Riemann–Hilbert — **CORROBORATING ONLY**

Explicitly labelled CONJECTURED in the notice and introduced with the words
*"an open question, not a claim"* and *"no weight rests on it"*. If it were
false, the notice would still read correctly, because it asserts only that the
approach is unverified. **May remain `self`.**

---

## Disposition

`R1-56` requires a cold read. Per the operator's ruling that if either needs one
then both go in a single packet — *"it costs little, and a correction notice that
later needs its own correction would be the worst outcome here"* — `PACKET-E`
carries **both** `R1-56` (statement 1) and `CT-S9-PVPARAMS-C014` (statement 2),
dispatched as `CT-S15-COLDREAD-DEFERRED`. `R1-57` is not sent: it is CONJECTURED
on the face of the notice, so a cold read could not change any sentence.
