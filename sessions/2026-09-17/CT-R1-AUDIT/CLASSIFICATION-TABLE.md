# CLASSIFICATION-TABLE.md — the rank-2 source for P5 step 3, verified and extracted

Session: `sessions/2026-09-17/CT-R1-AUDIT/`

## 1. Citation, verified

The operator proposed van der Put & Saito as the rank-2 classification source
for P5 step 3, and required that the citation be verified rather than trusted.
It was. Bibliographic details confirmed against the publisher:

> Marius **van der Put** & Masa-Hiko **Saito**, *Moduli spaces for linear
> differential equations and the Painlevé equations*, **Annales de l'Institut
> Fourier, Tome 59, no. 7 (2009), pp. 2611–2667**.
> DOI `10.5802/aif.2502`.

**STRUCTURAL — citation verified.** A copy is in this session folder:

* `refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`
* 1 058 380 bytes, 58 pages (consistent with pp. 2611–2667)
* sha256 `1666BD6BE824A99FC0B48ADBE48233A9B2A520FD7E8ADF187E98D22525473605`
* Title page verbatim: *"ANNALES DE L'INSTITUT FOURIER … Marius VAN DER PUT &
  Masa-Hiko SAITO, Moduli spaces for linear differential equations and the
  Painlevé equations, Tome 59, no 7 (2009), p. 2611-2667."*
* Open access via Centre Mersenne / cedram.

**It is the right source.** From the Introduction (p. 2612): *"a systematic
construction of the ten isomonodromic families of connections of rank two on P1
inducing Painlevé equations … Our method extends the work of Jimbo, Miwa and
Ueno, since we allow all possible irregular singularities including
**ramification** and resonance."* This matters: P5's whole question is about
ramification, and Jimbo–Miwa–Ueno's tables exclude it.

> Note for anyone re-running the search: the PDF uses the **`ﬁ` ligature**, so a
> naïve grep for `ramified` or `unramified` returns *zero* hits. Search for
> `rami` instead. This cost one false negative here.

## 2. Table 2.1, extracted verbatim (p. 2635)

The paper identifies the ten families **by their Katz invariants**, not by
number (p. 2634): *"We will not number these ten families, but indicate them by
their Katz invariants, e.g., (0,0,0,0), (0,0,1), …, (0,−,3/2), (−,−,3),
(−,−,5/2)."* A dash means the point is absent from the singular set.

| Dynkin | Painlevé equation | r(0) | r(1) | r(∞) | r(t) | dim P |
|---|---|---|---|---|---|---|
| D̃4 | PVI | 0 | 0 | 0 | 0 | 4 |
| **D̃5** | **PV** | **0** | **0** | **1** | **-** | **3** |
| D̃6 | PVdeg = PIII(D6) | 0 | 0 | 1/2 | - | 2 |
| D̃6 | PIII(D6) | 1 | - | 1 | - | 2 |
| D̃7 | PIII(D7) | 1/2 | - | 1 | - | 1 |
| D̃8 | PIII(D8) | 1/2 | - | 1/2 | - | 0 |
| Ẽ6 | PIV | 0 | - | 2 | - | 2 |
| Ẽ7 | PII | 0 | - | 3/2 | - | 1 |
| Ẽ7 | PII | - | - | 3 | - | 1 |
| Ẽ8 | PI | - | - | 5/2 | - | 0 |

Selection rule behind the list (p. 2634): a singular point `p` contributes
`r(p)` to the fibre dimension if `r(p) ∈ Z≥0`, and `½ + r(p)` if
`r(p) ∈ ½ + Z≥0`; the positions contribute `max(−3 + #S, 0)`; the fibre is
required to have dimension 1.

**Half-integer Katz invariant ⇔ ramified.** So rows with a `1/2` or `3/2` or
`5/2` entry are exactly the ramified families — PIII(D7), PIII(D8), PVdeg,
PII(FN), PI.

**The D̃5 / PV row is `(0, 0, 1)`:** two regular singular points and **one
irregular point of Katz invariant 1, i.e. UNRAMIFIED.** This confirms, from a
verified primary source, the premise P5 was given and that CT-S4 had to take on
trust.

## 3. Matching our systems against the table — STRUCTURAL, and preliminary

This is the comparison P5 step 3 was halted for. It is now possible. I record
the matches, but I have **not** run the full step-3 analysis, and the apparency
question below is unresolved.

**System A** (the `f = Σ Q_n z^n` ODE, `b(n) = 3n²+n+1`). CT-S4 computed, in
exact arithmetic: ramified Katz **1/2** at `z = 0`, ramified Katz **1/2** at
`z = ∞`, and **no other singular point**, so `#S = 2`.

> Katz multiset `(1/2, −, 1/2)` ⇒ **D̃8, PIII(D8)**.

**π\*(System A)** under the ramified double cover `z = w²` (CT-S5B-COVER,
re-derived by hand in `AUDIT.md` §5): unramified Katz **1** at `w = 0`,
unramified Katz **1** at `w = ∞`, `#S = 2`.

> Katz multiset `(1, −, 1)` ⇒ **D̃6, PIII(D6)**.

Both matches are exact, and they are **mutually consistent**: PIII(D8) and
PIII(D6) are adjacent in the degeneration hierarchy, and a quadratic cover is
the classical relation between them. So the cover computation lands somewhere
coherent rather than nowhere.

**Neither is D̃5 / PV.**

**System B** (`L_φ`, the operator the D5⁽¹⁾ attribution is actually about).
CT-S4 computed: unramified Katz **1** at `z = 0`; regular singular at
`ρ± = (−1 ± i√11)/2`; regular singular at `z = ∞`. Taken at face value that is
one irregular Katz-1 point plus **three** regular singular points, which is
**not a row of Table 2.1** — the table allows `#S = 4` only with all `r(p) = 0`.

The resolution is almost certainly **apparent singularities**, which carry no
moduli and are not counted in the classification. VQ-N1 records apparent indices
`[0,0]`. If exactly one of `{ρ+, ρ−, ∞}` is apparent, the effective
configuration becomes one Katz-1 irregular point plus two regular singular
points — Katz multiset `(0, 0, 1)` — which **is** the D̃5 / PV row.

> **This is the open hinge, and I am not closing it here.** CT-S5B-COVER
> explicitly did **not** recompute VQ-N1's apparent indices, and neither did I.
> Until the apparency of `ρ±` and of `z = ∞` is settled by direct computation,
> the D̃5 / PV match for System B is **CONJECTURED**, not established.

## 4. What this does and does not settle

* **Does settle:** P5 step 3's missing input. The table is verified, in the
  repo, and extracted verbatim. P5's halt condition is lifted.
* **Does settle:** the PV / D5⁽¹⁾ target really is unramified Katz 1 — the
  premise is correct, from a primary source.
* **Does not settle:** whether System B is the D̃5 row. That needs the apparency
  computation named above.
* **Does not settle:** CT-S4's verdict **(c)** and CT-S5B-COVER's sharpening of
  it. But it adds a concrete, checkable datum: System A is **PIII(D8)**-shaped
  and its quadratic pullback is **PIII(D6)**-shaped, so if the D5⁽¹⁾ attribution
  is about System B rather than System A, then *"two objects, two surfaces"* is
  not merely a coordinate artefact — the two objects sit in **different rows of
  Table 2.1**, and no change of variable moves between rows, because the Katz
  multiset is an invariant of the family.

**No conjecture in any repo file was revised.** This is reported to the operator
only, as P5 requires.

---

## 5. Operator caveats (review R2) — binding on any use of §3

These two limits are **why §3 stays STRUCTURAL and is not a relabelling.**

### 5.1 A matching Katz multiset is necessary, not sufficient

Table 2.1 classifies **families of connections**, indexed by an invariant of the
family. A single fixed operator whose Katz multiset matches a row is therefore
*consistent with* that row, but is **not thereby a member of that isomonodromic
family**. Membership requires the **deformation parameter** to be exhibited: one
must show the operator sits in a one-parameter isomonodromic deformation whose
monodromy data are constant and whose time variable is the row's. That is the
well-posedness problem this whole line of work started from, and it is untouched.

Consequence for wording: write *"System A's Katz multiset is that of the
PIII(D8) row"*, never *"System A is PIII(D8)"*.

### 5.2 The cover lands on special, not generic, PIII(D6) parameters

The PIII(D8) ↔ PIII(D6) relation is the classical quadratic cover, and covers of
this kind land on a **codimension-positive locus** of PIII(D6) parameter space,
not on generic parameters. Any statement derived from §3 must therefore say
**"a special PIII(D6) family"**.

### 5.3 The `−` slot in `(1/2, −, 1/2)` — RESOLVED

A `−` slot in Table 2.1 marks a point **absent from the effective singular
configuration**. `CT-S6-APPARENCY` settled which kind of absence applies to
System A: it is an **absent singular point**, not a point dropped as regular or
apparent (claim S6-C9, PROVEN; finite affine singular candidates outside `z = 0`
were NOT FOUND by exact factorisation, claim S6-C8). The premise flagged here is
therefore discharged, and it required no removal to be justified.

Caveats 5.1 and 5.2 remain fully in force.

## 6. Conjecture 4.1 is about neither System A nor System B

Settled in R2 from the primary source (companion v1.2, Zenodo
`10.5281/zenodo.20481592`, in `refs/`; see `AUDIT.md` §R2).

Conjecture 4.1 concerns a **third ODE, System C**: `a(x)y'' + b(x)y' + c(x)y = 0`
with `a = 3x² + x + 1`, `b = 6x + 1`, `c = −x²` (companion §2.2, eq. (6)–(7)).
Because `b = a'` it is exact: `d/dx[a y'] + cy = 0`. Its finite singular points
are the roots of `a`, namely `(−1 ± i√11)/6` — **exactly** the points CT-S5B
found for the *inverted* System B, which is strong evidence that System C and
System B are related by `z ↦ 1/z` up to gauge (not yet proved).

Two further facts from the same source bear directly on §3:

1. **Companion Remark 2.2** asserts as a general principle that for any
   PCF-derived ODE of this shape the finite singularities — the roots of `χ` —
   *"are always apparent."* If true, System C's effective configuration is
   `x = ∞` alone, which is **not a row of Table 2.1**. Under test in
   `CT-S6-APPARENCY`.
2. **Conjecture 4.1's own stated weakness**, verbatim: the surface-type
   determination D5⁽¹⁾ *"rests on a match against the Jimbo–Miwa–Ueno
   classification table [5] and is not yet corroborated by an independent Lax-pair
   derivation (see Remark 4.5)."* The JMU tables **exclude ramified cases**, and
   ramification is precisely the phenomenon at issue here. So the conjecture's
   evidential base cannot, by construction, see the alternative that §3 raises.

None of this revises Conjecture 4.1 or any repo file. Reported to the operator only.

---

## 7. The apparency computation has returned (`CT-S6-APPARENCY`, spot-checked)

Full independent re-derivation in `VERIFY-S6.md`; script `verify_s6.py`.
Nothing below is taken on CT-S6's word — each item was rebuilt from the
companion's eq. (6)–(7) and from CT-S5B's normal form, and also done by hand.

### 7.1 §3's open hinge is closed, and it closed the other way

§3 conjectured that System B would reach the D̃5 / PV row **if** one of
`{ρ+, ρ−, ∞}` turned out to be apparent. That conjecture is now settled, but not
as posed:

* `ρ±` are **NOT APPARENT** (PROVEN). Their exponents are `[0,0]` — repeated —
  and a repeated exponent at a genuine regular singular point always forces a
  log term. No twist can separate a repeated exponent.
* `z = ∞` **does** drop out, by a mechanism the apparency test was not looking
  for. Its exponents `1 − √3/18`, `2 − √3/18` are non-integers, so CT-S6's test
  ruled it NOT APPARENT. But they **differ by exactly 1**, and the rank-1 twist
  implicit in the normal-form reduction shifts them to `{0, 1}` with no log
  term. Under `z ↦ 1/x` the point becomes `x = 0`, where the normal form takes
  the finite value `11/4` — an **ordinary point**. It carries no moduli.

So the effective multiset is `(0, 0, 1)` — the **D̃5 / PV row, p. 2635** — and
the route there was the fourth point becoming ordinary, not one of the three
becoming apparent. CT-S6's own `(1,0,0,0)` / "no matching row" (claim S6-C7) is
**superseded**: it contradicts CT-S6's *own* PROVEN equivalence of System B with
System C, and the defect is an apparency test that disallows twisting.

### 7.2 System C = inverted System B, exactly

Both normal forms are **identically** `(12x⁴+4x³+4x²+11) / (4(3x²+x+1)²)`
(PROVEN, re-derived here independently). The relation suspected in §6 from the
coincident singular points is therefore established. System C's `x = ∞` is
unramified **Katz 1** (pole order 4).

### 7.3 Companion Remark 2.2 is false — in general, not just in examples

CT-S6 refuted it with two counterexamples. The refutation is actually complete:

> For `χ y'' + χ' y' + c y = 0` at **any** simple root `s` of `χ` with `c(s) ≠ 0`,
> `p = χ'/χ` has residue exactly `1` and `(x−s)²q → 0`, so the indicial
> polynomial is `λ²` for **every** such `χ` and `c`. The exponents are always
> `0,0`, so there is always a log term, so the point is **never apparent**.

Label **PROVEN**. Note the irony: the exactness identity `b = a'` that the
companion highlights is exactly what forces the residue to be `1`, and hence
forces the repeated exponent. The structure appealed to implies the **opposite**
of the assertion.

### 7.4 Net effect on Conjecture 4.1: right row, wrong reason

* Its **conclusion** — Sakai surface `D5^(1)`, PV — is **consistent** with the
  van der Put–Saito row for System C. The better source does not contradict it.
* Its **argument** does not survive. It derives `β = γ = 0` from the claim that
  *"both finite singularities are apparent"*, and that claim is now refuted.
* Its **parameter values** do not survive either — this is stronger than the
  earlier position and is the result of ruling 4 (`CT-S9-PVPARAMS`, audited in
  `VERIFY-S9.md`). Re-deriving them from the *correct* local data
  (`θ₀ = θ_t = 0`, repeated exponents with logs) through Jimbo's dictionary
  (PRIMS p. 1152) gives `γ = 1`, not `0`, and `β = −α`, so `β = 0` forces
  `α = 0` and contradicts `α = 1/6`. Only `δ = −1/2` survives, and only because
  it is Jimbo's normalisation. The contradiction is **not** a units artefact:
  holding `δ = −1/2` under `z ↦ cz` forces `c = ±1`, so `γ` cannot be rescaled.
* Jimbo's standing assumption **(A1)_PV (`θ₀, θ_t ∉ ℤ`) is violated** here. The
  dictionary is stated before it and is unconditional, so the parameter
  computation stands; but nothing Jimbo derives after that line covers this case.
* **Membership remains open** regardless, by caveat 5.1: a matching Katz multiset
  is necessary, not sufficient, until the deformation parameter is exhibited.
  For System C this is now concrete rather than rhetorical: its PV time is
  **fixed** at `t = ∓2i√33/9` by the normalisation at `∞`, so System C is a
  single fibre. A membership claim must exhibit an isomonodromic *family* with
  that fibre. **NOT FOUND** in the inspected sources by the methods used.

### 7.5 System A is untouched by any of this

System A's multiset `(1/2, −, 1/2)` is **ramified**. Half-integer Katz invariants
are invariant under rank-1 twisting, so no normalisation of the kind used in
§7.1 can move System A into the `(0,0,1)` row. System A and System C therefore
sit in **different rows of Table 2.1**, and *"two objects, two surfaces"* stands
— now with the third object, System C, identified and placed.

**No conjecture file was edited.** Reported to the operator only.
