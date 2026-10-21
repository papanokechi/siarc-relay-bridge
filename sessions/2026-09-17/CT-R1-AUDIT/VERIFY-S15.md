# VERIFY-S15 — claim-by-claim adoption of CT-S15-COLDREAD-DEFERRED

Verdicts returned: **statement 1 CORRECT WITH WORDING CHANGE**, **statement 2
CORRECT**. Both are adopted. Two transcriptions in the report are **rejected**,
and the method that produced them is a P0 finding in its own right.

HEAD unchanged at `08aa0e2381b3dc37ee54a3200b7272755ca11d59`. Source hashes in
the report match those of the packet files as dispatched.

---

## Method finding: the cold reader used OCR on the page images

CT-S15's file list includes `ocr_allowed_sources.py`,
`ocr_jimbo_top_variants.py` and `ocr_jimbo_lower_variants.py`, and its report
says *"The OCR retained the line imperfectly"*.

**This defeats the purpose of the P0 citation rule.** That rule exists because a
PDF text layer once rendered a hypothesis in a way that would have reversed a
conclusion. OCR applied to a page image is a *newly generated* text layer, with
the same failure mode and no provenance at all. Supplying page images does not by
itself satisfy the rule if the reader converts them straight back into text.

I therefore re-read both pages **directly** before adopting anything. The rule as
written says "read page images, not the text layer"; it must also say **what
counts as reading one**. That is now recorded in `P0-CITATION-RULE.md`.

Two defects were found, both caused by the OCR, neither affecting the verdicts.

### Rejected 1 — the constant matrix in Jimbo's (3.1)

CT-S15 transcribed the system as

> `∂Y/∂x = (A₀(t)/x + A_t(t)/(x−t) + (1/2)σ₃) Y`.

The printed page carries a 2×2 matrix with entries `1` and `0` on the diagonal —
that is, **`diag(1, 0)`**, not `(1/2)σ₃ = diag(1/2, −1/2)`. The two differ by
`(1/2)I`, a trace shift, so they are genuinely different matrices.

Nothing in the notice quotes `(3.1)`, so this did not propagate. **Not adopted**,
and it must not be reused.

### Rejected 2 — the content of (A1)_PV

CT-S15 reported the standing assumption as *"non-integrality of the theta
parameters (`θ_∞`, `θ₀`, `θ_t`)"*. The printed line is exactly

> **(A1)**`_PV`  `θ₀, θ_t ∉ Z`.

`θ_∞` does **not** appear in it. This one matters: **C2** turns on `(A1)_PV`
being violated by `θ₀ = θ_t = 0`, and a notice that over-stated the assumption
would be citing the source incorrectly on a load-bearing hypothesis.

I re-read the page image directly and confirm the notice already states it
correctly at line 116, with no `θ_∞`. The dictionary in the notice —
`α = ⅛(θ₀−θ_t+θ_∞)²`, `β = −⅛(θ₀−θ_t−θ_∞)²`, `γ = 1−θ₀−θ_t`, `δ = −½` — also
matches the page exactly. **Neither defect reached the notice.**

---

## Statement 1 — `dim P = 0` — **ADOPTED with the wording change**

CT-S15's refinement is a real improvement and is adopted: `P` should not be
called simply "the parameter space of the family". The source's own
characterisation is narrower, and I confirmed both quotes from the page images:

* p. 2634 — *"The space `R` is mapped to a space of parameters `P` (related to the
  parameters spaces of the Painlevé equations) consisting of traces or eigenvalues
  of the matrices involved in the construction of `R`."*
* p. 2635 — *"It turns out that `R → P` is a family of affine cubic surfaces."*

So `P` is the base of a cubic-surface fibration on the **monodromy** side — a
space of trace/eigenvalue parameters — not a parameter space of the differential
equations in any looser sense.

### A stronger ground than we had

CT-S15 located a sentence that settles the question far more directly than the
inference `R1-56` was previously resting on. Immediately after Table 2.1, on
p. 2635:

> **"We will also describe the corresponding one-dimensional families of
> differential modules `M(t)`."**

I verified this verbatim from the page image. The source therefore describes
**one-dimensional families `M(t)`** for the rows of the same table in which
PIII(D₈) carries `dim P = 0`. That is direct textual evidence — not an inference
— that `dim P = 0` does not negate a one-dimensional deformation direction.

Also confirmed from the image: `r(t)` is a **Katz-invariant column for a singular
point** labelled `t`, present only when the singular set contains one. The PVI
row `(0,0,0,0)` has `r(t) = 0` with `S = {0,1,∞,t}`, while the PIII(D₈) row has
`r(t) = −`, i.e. no such point — and yet the `M(t)` families are still described.
The letter `t` is doing two different jobs on that page, which is precisely the
confusion `R1-56` was written to prevent.

**Effect on `R1-56`:** upgraded from an inference to a claim with direct textual
support, and `review: cold`. C4 point 7 is rewritten to use the sharper
definition of `P` and to quote the `M(t)` sentence.

## Statement 2 — no Lax embedding from scalar data — **ADOPTED**

Verdict **CORRECT**, and the reasoning is sound independently of the two rejected
transcriptions. To be an instance of `(3.1)` an object must supply `A₀(t)` and
`A_t(t)` as explicit `t`-dependent matrices, the singular points `x = 0` and
`x = t`, the eigenvalue data `±θ_ν/2`, and crucially the **second** equation
`∂Y/∂t = −A_t(t)/(x−t) Y`. Scalar local data — singular points, exponents,
formal type — supply none of these.

CT-S15 also verified the companion's local data in its own code at 100 dps
(`b = a′`, roots `(−1 ± i√11)/6`, `disc = −11`, indicial `ρ²`,
`lim c/a = −1/3`), independently reproducing values already in the record.

This does **not** change `CT-S9-PVPARAMS-C014`'s disposition in the dependency
audit — it was assessed *corroborating only*, and still is, since the notice
asserts openness. But it is now `review: cold` rather than `self`, which is
strictly better than the ruling required.

---

## Not established

* Neither statement's cold read bears on whether any of the three objects lies in
  an isomonodromic family. That remains open.
* CT-S15 could not recover `(A1)_PV`'s exact typography by OCR; I supplied it by
  reading the image directly.
* Nothing here is machine-checked.
