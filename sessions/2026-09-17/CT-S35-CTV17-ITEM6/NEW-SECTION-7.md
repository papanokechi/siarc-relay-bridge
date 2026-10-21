## 7. The formal type of the generating-function operator

### 7.0 The object, and what it is not

Summing the recurrence against `z^n` gives, for the generating function
`f(z) = Σ_n Q_n z^n` of the **denominators**,

> `[ 1 − z·b(θ+1) − z²·a(θ+2) ] f = 1`,  `θ = z d/dz`,

with `a ≡ 1` in Channel Theory's own recurrence and general `deg a = e` allowed
below. Write `L_d := z·b(θ+1) + z²·a(θ+2) − 1`. The question asked here is the
**formal type of `L_d`** at `d = deg b = 2`: its singular points, their Newton
polygons, and the resulting Katz invariants, compared against the ten-row
classification of van der Put–Saito, Table 2.1. At `d = 2` the operator has
rank 2, which is the setting that table classifies; the comparison is made at
`d = 2` for that reason and **is not extended to other degrees**.

**This is not the object of §0 item 4.** That item concerns whether the
CC-channel **connection-coefficient ratio** matches the Riemann–Hilbert datum of
`P_V/D₅^(1)` at the `V_quad` τ-parameter — a statement about monodromy data of a
different object, carried under `op:cc-stokes-closed-form` and **conjectural**
since v1.5. `L_d` is the operator annihilating a generating function of
denominators. **Both are labelled by Painlevé equations; that is a shared
vocabulary, not a shared object**, and §6.0's prohibition applies here as it
does to `K` and `S_{ζ*}`. Whether the two determine one another is **open and
untagged**; none may be invented for it.

### 7.1 What the printed page says

Every quotation below was verified against a page image identified by the folio
**printed on the page**, not by index arithmetic.

**Folio 2634**, §2.2: the objects classified are local families `M(u)` of
differential modules represented by `d/dz + A(z,u)` with `A` a **2 × 2 matrix of
trace 0** on `P¹`; *"A singular point `p` with Katz invariant `r(p)`…"*; and
*"We will not number these ten families, but indicate them by their Katz
invariants, e.g., `(0,0,0,0)`, `(0,0,1)`, …, `(0,−,3/2)`, `(−,−,3)`,
`(−,−,5/2)`."* **The identification of the table's `r(·)` columns with Katz
invariants is therefore the source's own**, not an assumption imported here.

**Folio 2635**, Table 2.1, *Classification of Families*: ten rows, columns
`Dynkin | Painlevé equation | r(0) | r(1) | r(∞) | r(t) | dim P`. A printed dash
means no singular point in that column. The rows relied on below read, verbatim:

| Dynkin | Painlevé equation | `r(0)` | `r(1)` | `r(∞)` | `r(t)` | `dim P` |
|---|---|---|---|---|---|---|
| `D̃₄` | PVI | 0 | 0 | 0 | 0 | 4 |
| `D̃₅` | **PV** | **0** | **0** | **1** | **−** | **3** |
| `D̃₆` | PV_deg = PIII(D6) | 0 | 0 | 1/2 | − | 2 |
| `D̃₆` | PIII(D6) | 1 | − | 1 | − | 2 |
| `D̃₇` | PIII(D7) | 1/2 | − | 1 | − | 1 |
| `D̃₈` | PIII(D8) | 1/2 | − | 1/2 | − | 0 |
| `Ẽ₆` | PIV | 0 | − | 2 | − | 2 |
| `Ẽ₇` | PII | 0 | − | 3/2 | − | 1 |
| `Ẽ₇` | PII | − | − | 3 | − | 1 |
| `Ẽ₈` | PI | − | − | 5/2 | − | 0 |

### 7.2 Tier 1 — independently confirmed

**This paragraph is Tier 1: independently confirmed, VERIFIED.**

At `z = 0` the Newton polygon of `L_d` at `d = 2` gives Katz invariant **`1/2`
for every admissible coefficient vector** — the value does not depend on the
coefficients, only on the degrees and the non-vanishing of the leading ones.
The multiset of Katz invariants of `L_d` therefore **always contains `1/2`**.

The `D̃₅ / P_V` row of Table 2.1 prints `r(0) = 0`, `r(1) = 0`, `r(∞) = 1`,
`r(t) = −`. **No entry in that row is `1/2`.** Hence the multiset of `L_d` is
never that row's multiset, and

> **`D̃₅ / P_V` is not compatible with `L_d` for any admissible coefficient
> vector at `d = 2`** — not for a sampled family, for all of them.

The same one-line test disposes of six further rows, being exactly those whose
printed entries contain no `1/2`: `D̃₄/PVI` `(0,0,0,0)`, `D̃₆/PIII(D6)`
`(1,−,1,−)`, `Ẽ₆/PIV` `(0,−,2,−)`, `Ẽ₇/PII` `(0,−,3/2,−)`, `Ẽ₇/PII` `(−,−,3,−)`
and `Ẽ₈/PI` `(−,−,5/2,−)`. Seven of the ten rows go at once, and the three that
survive are precisely the three containing `1/2`.

**Confirmation.** This exclusion has been reached by **two readings of the
printed table**: one in this corpus, and one by an **isolated reader given only
the operator, its conventions, and page images of folios 2634–2637**, with no
access to this work, its conclusions or its vocabulary, which reached the
exclusion without being told it. A third, independent transcription of the ten
rows was made during preparation; all three agree in every row and column,
including which entries carry the printed dash.

### 7.3 Tier 2 — self-derived, not independently confirmed

**This paragraph is Tier 2: self-derived, and NOT independently confirmed.
STRUCTURAL.**

The three surviving rows are reached, and are selected by `deg a`:

| `e = deg a` | Katz multiset | surviving row |
|---:|---|---|
| 0 | `{1/2, 1/2}` | `D̃₈ / PIII(D₈)` |
| 1 | `{1/2, 1}` | `D̃₇ / PIII(D₇)` |
| 2 | `{0, 0, 1/2}` | `D̃₆ / PV_deg = PIII(D₆)` |

Channel Theory's own recurrence is `a ≡ 1`, i.e. `e = 0`, and so falls in the
`PIII(D₈)` line of this table. **The isolated reading covered `deg a = 2`
only**, so it confirms the Tier 1 exclusion but **not** this set; the single
multiset it reported, `{0,0,1/2}`, is the third line above and neither confirms
nor contradicts the other two. This tier rests on one derivation.

### 7.4 Tier 3 — self-derived by a contaminated re-derivation

**This paragraph is Tier 3: self-derived by a re-derivation that was
contaminated. It is the weakest statement in §7 and is NOT independently
confirmed. STRUCTURAL.**

Generically the surviving row depends only on `(α₂, α₁)`. On the
**codimension-3 locus `a(1) = a(2) = 0` and `b(1) = 0`** the point at infinity
becomes ordinary, and the resulting multiset **matches no row of Table 2.1** at
all. The derivation that produced this ran in a workspace another process was
writing into, and it corrected an earlier error of its own before arriving here;
neither isolated reading reaches this tier, and both state explicitly that they
did not classify the coefficient subloci on which an apparent singularity may be
removed by a common factor. **A reader should not assume the exceptional locus
has been characterised.**

### 7.5 A matching multiset is a necessary condition only

Equality of Katz multisets is **necessary, not sufficient**, for `L_d` to sit in
a given row's family. **The procedure of §7 therefore excludes rows and assigns
none.** A mismatch settles the question and is VERIFIED, being an equality check
against a printed table; a match does not, because it leaves open whether `L_d`
actually lies in the corresponding moduli family, which would need the
classification's sufficiency and not merely its invariants. That is why every
exclusion above is VERIFIED and every surviving row is STRUCTURAL. **Nothing in
§7 places `L_d` in any family, and no sentence of it may be restated as though
it did.**

### 7.6 The record's own Painlevé history, stated and not adjudicated

This record has carried two different Painlevé labels, and §7's surviving set
falls on both sides of the change. Both facts are stated here; **neither is
adjudicated.**

* **v1.0–v1.3 carried `P-III(D₆)`.** That label lies **inside** the surviving
  set of §7.3.
* **v1.4 replaced it** with the Painlevé V transcendent on the Sakai surface
  `D₅^(1)`, and **v1.5 marked that identification conjectural**. That label lies
  **outside** the surviving set, in the row §7.2 excludes.

It does not follow that the v1.4 correction was wrong, for two independent
reasons, either of which alone is sufficient:

1. **A row exclusion is not a row assignment** (§7.5). §7 removes `D̃₅/P_V` from
   the rows `L_d` can meet; it does not place `L_d` in `PIII(D₆)` or anywhere
   else, and a label that survives §7 is not thereby supported.
2. **The two labels are about a different object** (§7.0). They name the
   `V_quad` Borel-plane datum, not `L_d`, and the two have **not** been shown to
   determine one another.

**This notice asserts no Painlevé label for `V_quad`.** It repeats the record's
history, records where §7's surviving set falls relative to it, and stops there.
The stale `P-III(D₆)` wording still present in working material remains stale
and must not be copied forward on the strength of §7.

### 7.7 What §7 does not settle

* **It does not establish sufficiency** (§7.5), so it assigns no row.
* **It does not dispute, or support, the `V_quad` Painlevé-V identification**
  (§7.0, §7.6), and is **not evidence about it** in either direction.
* **It does not extend beyond `d = deg b = 2`**, where the rank-2 setting of the
  table applies (§7.0).
* **It rests on one published table**, read three times, not on an independent
  derivation of the classification.
* **Tiers 2 and 3 rest on one derivation each** (§7.3, §7.4); only Tier 1 has
  been reached twice.
