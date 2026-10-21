# VERIFY-S14 — claim-by-claim adoption of CT-S14-COLDREAD-B

Per the P0 rule adopted at operator review #7: *findings from a review are
adopted claim by claim; a correct finding does not certify the reasoning around
it.* CT-S14's headline verdict is right, and two of its six task answers still
needed correction. Both are recorded below.

My re-check is `verify_s14.py` → `verify_s14.out.txt`, written from the primary
data only (object B's printed normal form; the companion's printed polynomial
coefficients), without reading CT-S14's scripts.

Isolation held: CT-S14 reported reading only the packet and the four permitted
page images, and its file list is consistent with that. HEAD unchanged at
`08aa0e2381b3dc37ee54a3200b7272755ca11d59` at both ends of its run.

---

## The result that matters

CT-S14 found something the earlier work had not established, and it **resolves**
rather than confirms the worry that prompted this cold read.

> Under `z = 1/x`, object **B**'s trace-free normal form is **exactly** the
> companion operator's trace-free normal form. Not "matches up to a twist" —
> identically equal.

My independent re-derivation:

```
r_B(1/x) / x⁴  =  (12x⁴ + 4x³ + 4x² + 11) / (4(3x² + x + 1)²)
r_C(x)         =  (12x⁴ + 4x³ + 4x² + 11) / (4(3x² + x + 1)²)
difference      =  0        [exact, symbolic]
```

Two details make this clean rather than coincidental:

* the pullback's first-order term `2/x` contributes **nothing** to the normal
  potential — `(2/x)²/4 + (2/x)′/2 = 1/x² − 1/x² = 0` — so inversion alone lands
  on the trace-free form, with no twist required;
* the long-standing root puzzle dissolves. B's finite singular points are at
  `(−1 ± i√11)/2` and the companion's at `(−1 ± i√11)/6`; `x = 1/z` carries the
  first set **exactly onto** the second. (My script's set comparison printed
  `False` here; that was a SymPy hashing artefact on unevaluated radicals, and an
  elementwise check confirms the match. Recorded because it would otherwise read
  as a discrepancy.)

**Consequence for the operator's question.** You asked whether the twist that
makes B match System C takes B out of the trace-free class Table 2.1 classifies.
The literal answer is **yes, it does** — but the twist is **not needed for B's
row**. B reaches its trace-free normal form by inversion alone; the twist belongs
to the companion's choice of *printed scalar presentation*, not to B's
classification. So the row survives, and the drafted sentence was wrong to
invoke a twist at all.

---

## Task-by-task adoption

| # | CT-S14's finding | Adopted? | My check |
|---|---|---|---|
| 1 | B has three singular points (`z=0` Katz 1; two regular singular); `z=∞` is **ordinary** in the normal form; tuple `(0,0,1)` | **adopt** | `r̃(0) = 11/4`, finite, with series `11/4 − 11x/2 − 29x²/4 + O(x³)` — analytic, so ordinary |
| 2 | Inversion identifies B's and C's trace-free normal forms; a further rank-1 twist `h = A^(−1/2)` reaches C's printed operator | **adopt**, strengthened to an exact identity | difference is exactly `0`; twist verified |
| 3 | The integer-difference points do not become ordinary after the twist | **adopt the substance, reject one word** | see below |
| 4 | The twist alters the trace and lies outside Table 2.1's normalisation | **adopt, with a material qualification** | see below |
| 5 | Row `D̃₅ / PV / (0,0,1)` at face value and after inversion; no row in the twisted scalar basis | **adopt**, STRUCTURAL, necessary only | row quoted from the page image |
| 6 | CORRECT WITH WORDING CHANGE | **adopt the verdict, rewrite the wording** | see below |

### Task 3 — the word "apparent" is wrong

CT-S14 concluded those points are *"apparent/regular singular in the printed
scalar equation, not ordinary."* The conclusion **not ordinary** is right. The
word **apparent** is not, and it contradicts our own C1.

My check reproduces the hypotheses exactly: at each root of `A`,
`residue(P) = 1` and `lim (x−β)² Q = 0`, giving indicial polynomial `λ²` and
exponents `[0,0]`. Those are precisely the hypotheses of the C1 lemma, whose
conclusion is that **a log term is forced**, so the point is *never* apparent.
CT-S14 was isolated from C1 by design and could not have known this; the error is
in the adoption, not in the reviewer.

Adopted form: *the points are regular singular and non-apparent, with exponents
`[0,0]` and a forced log term in the printed basis, and `[1/2,1/2]` in the
trace-free normal form.* Katz invariant `0` either way, so **no row is affected**.

### Task 4 — right, but it does not bite

The trace computation is correct and I reproduce it: `2 dlog(h) = −dlog(A) =
−(6x+1)/(3x²+x+1) ≠ 0`, and p. 2634 does require `trace 0`. So a trace-altering
twist does leave the classified class.

The qualification is that **this does not put B's row in doubt**, because B never
needs the twist. CT-S14 states this correctly in its own task 5 ("re-normalising
restores the trace-free normal form") but its task 4 verdict is phrased as
though something were at risk. Adopted as: *the twist to the companion's printed
scalar operator is trace-altering and hence outside Table 2.1's class; B's row is
read from its trace-free normal form, which inversion alone reaches, so the row
is unaffected.*

### Task 6 — verdict adopted, wording rewritten

CT-S14's replacement sentence is accurate but packs a three-clause argument into
a table cell. The table should carry the claim; the argument belongs in the text.

---

## Effect on earlier claims

* **`R1-20` (STRUCTURAL, previously unreviewed) is now cold-confirmed** on its
  central assertion — that `z=∞` is not a genuine extra singular point, so the
  tuple is `(0,0,1)`. It is upgraded to `review: cold`.
* **`R1-09` (CONJECTURED)** raised the worry that a four-point multiset
  `(1,0,0,0)` is not a row of Table 2.1. That worry is now **retired**: there is
  no fourth singular point. `R1-09` was a correct observation about a multiset
  that does not arise.
* **`S4-06` and `S5B-C6`**, the two `self` gaps on row B in
  `DEPOSIT-DEPENDENCIES.md`, are cleared by an independent cold read.
* **`S6-C7`** — superseded, as previously recorded; the apparency framing was
  the wrong test, and C1 now explains why.
* **`R1-57`** (the quadratic-cover route to the strong Riemann–Hilbert
  condition) is untouched and remains CONJECTURED.

## What is still not established

* **Family membership for B remains open.** The row match is STRUCTURAL and a
  necessary condition only. Nothing here shows B lies in an isomonodromic PV
  deformation.
* CT-S14 did not, and was not asked to, examine whether the companion explains
  its scalar-basis singularities elsewhere in its own text.
* Nothing in this run is machine-checked.
