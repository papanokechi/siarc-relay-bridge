### C3. The fixed Painlevé V time is determined by the configuration

Jimbo normalises the irregular part at infinity so that its exponent difference
is exactly the independent variable. Matching the operator of Conjecture 4.1 by
an affine change `z = k(x − s₀)` therefore **forces** `k = 2/√3`, and the two
finite singular points then sit at `0` and

```
    t = ∓ 2i√33 / 9 ,      |t| = 2√33/9 .
```

**The Painlevé V time is not a free parameter.** In van der Put–Saito's
framework the three singular points are normalised to `0`, `1`, `∞` and the time
is the **scale of the irregular type at infinity** — an invariant computed from
the configuration, not a coordinate that can be varied independently. An object
of this type therefore *arrives* with a definite `t`, and the absence of a
written deformation is a matter of presentation rather than a defect.

The honest restatement is:

> **System C** has the **local formal type** of the Painlevé V / `D̃₅` family,
> and its trace-free connection is a point of the van der Put–Saito moduli space
> for that row, where the Painlevé V time is determined by the configuration
> rather than chosen. The value `t = ∓2i√33/9` printed in v1.2 is consistent
> with this. Membership on a single isomonodromic leaf **follows from the
> framework**; it has **not** been confirmed by an independent computation of
> the monodromy and Stokes data (**open**).

This restatement does not credit v1.2 with an argument it did not make: the
framework supplies the leaf, and the companion supplies neither the framework
nor the verification.

> **Disclosure — a corrected published formula is load-bearing here.** The
> identification of System C with a point of the moduli space was carried out
> against van der Put–Saito's explicit family. The entry `b(z)` of that family,
> as printed on p. 2655 of the journal version **and** on p. 34 of arXiv:0902.1702v5,
> appears to contain a typographical error: its first term prints
> `(p + ½(q−1)q)²`, with no `t`, while the parallel second term carries
> `(q−1)qt`. As printed, the family fails the paper's own constraint
> `det A(1) = −θ₁²/4`, by a residual carrying the factor `(t − 1)` — vanishing
> exactly where the two readings agree. With `(p + ½(q−1)qt)²` the constraint
> holds identically. The corrected reading is what has been used. No published
> erratum is known to us. *[Deposit-day: state the actual status of the author
> notification here — it had not been sent when this draft was written.]*

Two limitations attach to the affine matching and should be stated with it: the
identification of the two finite singular points with Jimbo's `0` and `t` is an
**assumption**, legitimate for placing a two-finite-singularity,
one-irregular-singularity problem into Jimbo's normalisation, but not proved by
the scalar equation alone; and the conclusion is conditional on that
identification.

**Recommendation:** replace Remark 2.2 with the lemma of **C1**, re-ground
Conjecture 4.1 on the Katz-multiset match rather than on apparency, restate it
in the form above, and **keep it a conjecture**.

**Scope of the open question.** Because **B** and **C** are projectively
equivalent under `z ↦ 1/x` (see **C4**), the embedding question need only be
posed **once**: any deformation constructed for one, transported by that
equivalence, settles the other. It is natural to pose it for **C**, which
already carries the companion's printed normalisation and the fixed time above.
This reduces two open questions to one. What remains open is not the existence
of a deformation — the framework supplies that — but the **verification**: an
independent computation of the monodromy and Stokes data along the leaf. Anyone attempting the transport should check that `z ↦ 1/x`
carries **C**'s time `t = ∓2i√33/9` to a consistent time for **B**. That check
has **not** been performed here and is recorded as part of the future problem,
not as a result of this notice.

