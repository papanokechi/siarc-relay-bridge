# CT-S21 addendum — the two attributions, resolved from the PDFs

Both items were filed in §R24 as the operator's own readings, one of them
CONJECTURED. Both PDFs are now in `refs/` under CC-BY-4.0, so both could be
checked rather than left attributed. This file records the result.

---

## 1. arXiv:2306.05930 — LOCATED, and the paraphrase overstates it

**Where.** Ibrahim & Salvy, *Positivity certificates for linear recurrences*,
printed **p. 5**, §2.3 "Asymptotics" — read from a rendered page image
(`pages/salvy_printed5_idx4.png`, dpi 190), not from the text layer.

**Verbatim, as printed:**

> While we know how to compute a basis of formal asymptotic expansions that are
> solutions of linear recurrences (by the results of Birkhoff-Trjitzinsky
> improved by Immink [BT32; Imm84]), we do not know how to compute the leading
> coefficient exactly in general. Currently, the closest we have is a certified
> numerical approximation in the form of an interval that can be made
> arbitrarily small, but 0 cannot be excluded. This is known as the *connexion
> problem* for linear differential equations.

**Status of the operator's description: substantively MATCHES.** The certified
interval, the inability to exclude 0, and the name *connexion problem* are all
there as described.

**It is background, as surmised — confirmed structurally, not just by feel.**
The passage sits in §2.3, inside the preliminaries. The authors' own
contribution begins at **§3 "Positivity certificates"**, Definition 3, on
printed p. 6. So the remark is a statement of the standard situation and must
be **cited as such, not as a theorem of theirs**.

**One correction the paraphrase needs.** The paper says *"we do not know how to
compute the leading coefficient exactly in general"* — a claim about the state
of the art. It does **not** say the leading coefficient *is not computable*,
which would be a claim about the world. For the v1.7 contribution framing around
K and r_∞ that distinction is load-bearing in both directions: "nobody currently
knows how" leaves room for a contribution, whereas a non-computability theorem
would foreclose one. Cite the weaker, printed form.

**Two further details worth carrying.** The sentence attributes the *basis* of
formal expansions to Birkhoff–Trjitzinsky as improved by **Immink**. And the
name is applied to "the connexion problem **for linear differential
equations**", while the context is recurrences — quote it as printed rather than
silently transposing it.

Adjacent, and directly analogous to this project's situation: Example 3 on the
same page computes a leading coefficient, `1/(2√(eπ))`, but only "by exploiting
a closed-form expression of the generating function"; the authors then add,
flatly, **"In general, this is not available."**

Label: **INSPECTED** (located and quoted from a page image).

---

## 2. Wong & Zhao §3 — the equation class is FOUND; the growth law is NOT FOUND

§3 "Difference equations" spans **PDF pp. 12–20** (fixed from the PDF outline:
`3 Difference equations → 12`, `4 Riemann-Hilbert approach → 21`, both asserted
in the script). Full text of those nine pages was extracted and read.

**FOUND — the equation class.** §3 discusses Wong & Li [99] and [100], the
latter being equation **(3.2)**:

> y(n + 2) + n^p a(n) y(n + 1) + n^q b(n) y(n) = 0

with `p, q` integers and `a(n), b(n)` having `1/n` expansions with nonzero
leading coefficients. That is this project's class. The operator's reading of
§3 on this point is **confirmed**.

**NOT FOUND — the growth law.** By full-text read of §3, pp. 12–20, there is no
statement of `Q_n/Γ(dn+1) ~ K·(β_d/d^d)^n·n^s`, no exponent of the form
`s = β_{d-1}/β_d + (d-1)/2`, no `Γ(dn+1)`-type normalisation, and no explicit
formula for a leading constant. Recorded as an **absence claim** in the
operator's own INSPECTED form — "NOT FOUND in §3 by full-text read" — and not
as "the survey does not state it".

**Vacuity guard (S17-22).** A bare absence test cannot fail: if the extraction
were empty or mis-scoped every pattern would read "absent" and the verdict would
look like a finding. Six **positive controls** therefore ran first over the same
extracted string — section heading, "Wong and Li", equation (3.2), "turning
point", "Theorem 3.3", and the `K_{n+1}/K_{n-1} = c_n` normalisation. **All six
fired**; had any failed the script emits VOID and no absence verdict. 19,012
characters extracted.

**A structural reason the law is absent, which is better than the absence.**
§3's machinery *normalises the growth away before it begins*. At (3.23) it
defines `{K_n}` by `K_{n+1}/K_{n-1} = c_n` and sets `x_n = y_n/K_n`, so `K_n`
absorbs precisely the product growth, and Theorems 3.1–3.3 then describe `x_n`
by uniform Airy-, Bessel- and modified-Bessel-type expansions near transition
points. The survey is a **turning-point theory in a parameter**, not a theory of
the dominant solution's growth constant — and `K_0`, `K_1` are left "depending
on the particular sequence". So the growth law is not merely missing from §3;
the section's normalisation removes the quantity from view.

That dovetails exactly with Ibrahim–Salvy above: the constant is the part tied
to the initial conditions, and it is the part nobody computes. **The purchase of
Wong & Li 1992a remains warranted** — and the two references together sharpen
why.

Label: **INSPECTED** (absence, stated with scope, method and controls).

---

## Method note

Text layer was used for **location only**. The one passage quoted was read from
a rendered page image. The absence claim rests on extracted text, which is
stated in the claim, and is guarded by controls rather than asserted bare.
