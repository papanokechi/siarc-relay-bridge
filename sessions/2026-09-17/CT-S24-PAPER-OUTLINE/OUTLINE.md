# OUTLINE — paper on the quadratic recurrence and its Painlevé V leaf

Session `CT-S24-PAPER-OUTLINE`. Outline only; no prose was drafted, and no
computation was run. Repairs referenced as **R-(a)**…**R-(d)** are the four
kinds in `CT-S23-OUTSIDER-READ/REPORT.md` §3, plus the named items in §4.3–4.5
and §7.

> **Revision 6 — the last open drafting item is closed.**
> The upper bound `r_∞ ≤ exp Σ_{k≥1} 1/(b(k)b(k+1))`, carried at revision 5 as
> an unfolded addition **with no claim id**, is **proved** in
> `CT-S26-UPPER-BOUND` (Proposition U, `S26-01` PROVEN, `PROOF.md`), so §1 ¶2's
> "two-sided bound" needs no weakening and the pre-declared fallback was not
> taken. Three things travel with it into §2: the **positivity hypothesis is
> load-bearing** (three of six sign-changing `b` violate the inequality,
> `S26-04`), the upper half **must not cite `S1-02`**, and the proof uses no
> Pincherle or Perron–Kreuser input so §2.0's undertaking extends to it. The
> insertion into `theorem.tex` is a drafting action and is **not** done —
> `theorem.tex` belongs to an earlier session.
> Also recorded there, and relevant to §2.0's drafting-discipline note: the
> session's own known-answer control **fired**, because the Bessel closed form
> registered in its PREREG was wrong by an index shift (`S26-05`). A
> known-answer test is only as good as the known answer.
>
> **Revision 5 — two stale spots, one of them substantive.**
> I. **§1 ¶2 misdescribed its own proof.** It read "Growth is obtained from a
>    Pincherle/minimal-solution argument". `theorem.tex` does not work that way:
>    `prop:exists` gets convergence unconditionally under (A1) by telescoping,
>    `prop:positive` gets `r_∞ ≠ 0` from monotonicity, and `rem:pincherle` is
>    labelled STRUCTURAL with "nothing below depends on this remark". The
>    paragraph credited the result to an argument the paper deliberately does
>    **not** rest on — and a method paragraph led by Pincherle invites exactly
>    the Birkhoff–Trjitzinsky rigour question §2.0 was written to pre-empt.
>    Replaced; a guard against the same conflation added to §2.0 item 1; and the
>    §2 claim line now labels `S1-05` as interpretive rather than listing it flat
>    beside four PROVEN propositions.
> II. **The two-sided bound is an unfolded addition**, not an existing result.
>    `prop:positive` proves `r_∞ ≥ 1` only. The companion
>    `r_∞ ≤ exp Σ 1/(b(k)b(k+1))` is recorded in §2 as a one-line drafting
>    addition **carrying no claim id**, to be proved and emitted at drafting or
>    else dropped back to the one-sided statement. It must not be written citing
>    `S1-02`.
> III. **§5 N2 said "put the question in §11".** Sections were renumbered at
>    revision 2 (old §11 → §10). Corrected, with the renumbering noted inline.
>
> **Revision 4 — N1 closed; three rulings applied.**
> I. **N1 is CLOSED** (`CT-S25-N1-EXHAUSTIVE`). §5 N1 restated as a proved
>    result, with the mis-pricing finding retained as history because it was
>    true when written. §5's summary line and heading follow.
> II. **The solver sentence is restated as exhaustiveness proved** in §1 ¶2 and
>    in the §5 entry of §2 — the located points are the **complete** solution
>    set, by elimination over **`ℚ(i√11)`**. The field is named explicitly, with
>    a drafting warning: the visible radicals pull toward `ℚ(√3, √11)`, which is
>    wrong, and this outline itself made that error before this revision.
> III. **`S25-03` enters the paper** as a remark in §5: the system is
>    overdetermined **by two**, since `b₁ = 0` lies in the radical of the
>    coefficient ideal. Carried with it, the **Galois conjugacy** under
>    `√3 ↦ −√3`, now exhibited exactly by the eliminant — cross-referenced from
>    §8 and §10, and explicitly **not** a resolution of the gauge question.
>
> **The paper now has no new mathematics left. It is a drafting job.**
>
> **Revision 3 — operator rulings applied.**
> A. **Odlyzko p. 77 re-obtained and VERIFIED from a page image**, and written
>    into §2.0 item 4 **alongside Nemes**, not in place of it. The revision-2
>    "zero occurrences" finding was correct about the repository and wrong as a
>    conclusion: the citation originated in `CT-S22-DEPENDENCE-LIT`, whose
>    record was stored **outside the worktree** and whose PDFs were deleted at
>    close. Two refinements the page image forced are recorded in §2.0 item 4.
> B. **Open questions confirmed at two** — the `z`-dependent gauge and the
>    scope limits on membership. `S_{ζ*}` travels with the Borel material.
> C. **The Borel material's destination is now named: Channel Theory v1.7**,
>    not "v1.7 or a short note". See §3.4, which now also carries the
>    **transit manifest** — the two items the ruling flags as liable to be lost
>    in transit.
>
> **Revision 2 — operator rulings applied.**
> 1. **Attribution paragraph added** as §2.0, the gap identified in review.
>    **All five citations are now sourced to held, hashed artefacts**; the
>    fifth, Odlyzko p. 77, was blocked at revision 2 and was cleared at
>    revision 3 — see §2.0 item 4.
> 2. **N1 ruled: attempt once, time-boxed**, with the fallback pre-declared
>    before any algebra. See §5 N1.
> 3. **§9 cut** (option iii). The Borel material, the `ξ₀`/`ζ*` prohibition and
>    the PSLQ-basis repair travel to Channel Theory v1.7 or a short note. See
>    §3.4 — and note the **consequence the ruling implies: the paper's open
>    questions drop from three to two** (**outline** §4.2).
> 4. **`r`-objects renamed in the paper only**, with one footnote giving the
>    correspondence to the deposited names; deposits untouched.
> 5. **Title fixed** to the first candidate.
>
> Sections renumbered after the cut: old §10 → **§9**, old §11 → **§10**.

---

## 1. Title and statement

**Title — RULED.** *A quadratic three-term recurrence and a Painlevé V
isomonodromic leaf*

The alternate that foregrounded the growth theorem is dropped: the growth
theorem is the attributed part, and leading with it would advertise the paper's
least novel content.

### Statement of the result (paragraph 1)

For a polynomial `b` of degree `d ≥ 1` with `b(k) ≠ 0` for every integer
`k ≥ 1`, the three-term recurrence `Q_n = b(n) Q_{n-1} + Q_{n-2}` has
normalised terms `r_n = Q_n / ∏_{k≤n} b(k)` converging to a limit `r_∞`, and
under `r_∞ ≠ 0` the terms satisfy
`Q_n / Γ(dn+1) = K (β_d/d^d)^n n^s (1 + O(1/n))` with
`s = β_{d-1}/β_d + (d-1)/2` and `K` given in closed form by `r_∞` and
`∏_i Γ(1 − r_i)` over the roots of `b`. For the quadratic case
`b(n) = 3n² + n + 1` the generating function satisfies a second-order linear ODE
whose connection — after an explicit scalar reduction — is shown to be the
differential module of a specific member of van der Put–Saito's rank-2 family
of type `(0,0,1)`, at an explicit point of the chart `U₀` of the moduli space
`M_{t,λ}`. The identification is of the full operator, not merely its
projective class. Since Painlevé V is the isomonodromy foliation of that space
and the deformation vector field is regular at the point, exactly one PV leaf
passes through it; transport along that leaf leaves the trace coordinates
`x₁, x₂, x₃` of the monodromy and Stokes data invariant to better than 90
decimal digits, at two step sizes and on both branches of a sign pair related
by an explicit Galois automorphism.

### Statement of the method (paragraph 2)

The method is a chain of identifications, each one checked by a control that
could have failed. Growth follows from an elementary argument: the normalised
terms `r_n = Q_n / ∏_{k≤n} b(k)` satisfy an exact recurrence whose increments
are absolutely summable, giving convergence under `(A1)` by telescoping, with
positivity of `b` supplying `r_∞ ≠ 0` together with a two-sided bound.
**Pincherle's theorem supplies the minimal-solution interpretation but is not
used.** The result is confirmed numerically at `d = 2, 3, 4`. The ODE's local data —
pole orders, Katz invariants, local exponents and the non-apparency of the two
finite singular points — are computed exactly and matched against the
hypotheses under which van der Put–Saito construct `M_{t,λ}`. The point of
`U₀` is located by matching projective normal forms, an overdetermined system
of five coefficient equations plus one non-apparency condition in four
unknowns — **overdetermined by two, not one**, since the non-apparency
condition lies in the radical of the ideal generated by the five coefficient
equations and is therefore already forced by the matching (`S25-03`). **The two
located points are the complete solution set**, proved by Gröbner elimination
over **`ℚ(i√11)`** rather than reported as what a solver returned: the
saturated ideal is zero-dimensional of degree 2, and its eliminant
`27θ_∞² + 108θ_∞ + 107` is triangular over the remaining unknowns, so the
solution set is exactly the two points exhibited (`S25-02`, `S25-06`).
The projective ambiguity is then removed by comparing the pair
`(P, Q)` of the scalar operator directly, which a rank-1 twist does not fix.
Monodromy and Stokes data are computed by numerical analytic continuation with
a solver first validated against the closed-form Stokes multipliers of Kummer's
equation to 32 of 32 digits; the sectorial and orientation conventions are not
assumed but *selected*, as the unique one of sixteen candidates satisfying four
independent consistency conditions. Leaf membership is then tested by
integrating PV in `t`, rebuilding the linear system from `(q(t), p(t))` and
recomputing the trace coordinates, with a pre-registered sensitivity check
confirming the observable moves under displacement off the leaf and a
deliberately-wrong vector field confirming the test discriminates.

---

## 2. Sections

Each row: heading, one line of content, and where the material lives. Session
folders are under `sessions/2026-09-17/`.

### §0. Introduction

One line: states the recurrence, the result, and the two limits — the
identification is exact but leaf membership is confirmed numerically, not proven.

*Draws on:* the statement above. No new claims.

### §1. Notation and standing conventions  ⟵ **new section; most repairs land here**

One line: fixes every symbol and object the reader is otherwise asked to supply
— `Γ`, `O(·)`, `o(1)`, `~`, the three `r`-objects renamed, `(A1)–(A3)`, Katz
invariant and Katz multiset, `D̃₅`, Painlevé V, the names `A`, `B`, `C` for the
three systems, `K` and the amplitude, `c_±`, the Newton polygon and the germ
coefficient, and the numerical vocabulary (`dps`, Richardson extrapolation,
PSLQ, the `N/2`-vs-`N` agreement criterion).

**The `r`-rename carries a footnote**, by ruling: the paper's names, and their
correspondence to the names in the deposited record, which is left unchanged.

*Repairs:* **R-(d)** in full; `CT-S23` §4.1, §4.2, §4.3 (`(A2)`), §4.4 (the
`r`-collision).
*Draws on:* `CT-S3B-RINF/DERIVATION.md` L22–27 for `(A1)`, `(A2)`, `(A3)`;
`CT-S23-OUTSIDER-READ/outputs/coldread_main.txt` task 2 for the inventory of
171 items; `CT-S23-OUTSIDER-READ/outputs/jargon_index.out.txt` for the five
terms `G`.

### §2. Growth of the recurrence

One line: convergence of `r_n`, the radius `|β_d|/d^d`, the exponent `s`, and
the closed form for `K`, with the scope remark that the statement reads only
`β_d` and `β_{d-1}`.

*Claims:* `S1-01` (convergence of `r_n`, unconditional under `(A1)`, by
telescoping — PROVEN), `S1-02` (`b > 0` ⇒ `r_n ↑`, `r_n ≥ 1`, so `r_∞ ≥ 1` and
`(H)` is automatic — PROVEN), `S1-03`, `S1-04` (radius and growth — PROVEN);
`S1-05` **(Pincherle — STRUCTURAL and interpretive only; `theorem.tex`
`rem:pincherle` says in terms "nothing below depends on this remark", and the
paper must present it the same way)**;
`S3B-01`–`S3B-09` (`r_∞` for the quadratic case to 2317.8 digits, the closed
form for `K` and its `109`-digit agreement, and the `∏Γ(1−r_i)`-omitted vacuity
control); `S2-01`–`S2-04` (numerical confirmation of `s` at `d = 4` over eight
representatives, both vacuity arms); `S26-01` (the **upper** bound on `r_∞`,
PROVEN) with `S26-02`–`S26-04` (its numerical check, its engine controls, and
the counterexamples showing the positivity hypothesis is load-bearing).

*Artefacts:* `CT-S1-THEOREM/REPORT.md` §3 (incl. §3.5, the scope remark);
`CT-S1-THEOREM/theorem.tex`; `CT-S3B-RINF/DERIVATION.md`; `CT-S2-RHO-D4/`;
`CT-S26-UPPER-BOUND/PROOF.md` and `CT-S26-UPPER-BOUND/REPORT.md`.
*Repairs:* **R-(a)** — Propositions 1–4 are `S1-01`…`S1-04`, all PROVEN; the
proofs exist and need transcription only.

> **The upper bound in `prop:positive` — NOW PROVED, `S26-01`.** The source
> proposition establishes `r_∞ ≥ 1` only. The two-sided statement wanted by
> §1 ¶2 needs the companion bound `r_∞ ≤ exp Σ_{k≥1} 1/(b(k)b(k+1))`, which is
> proved in full in `CT-S26-UPPER-BOUND/PROOF.md` (Proposition U) under (A1)
> **together with `b(n) > 0` for every `n ≥ 1`** — the same hypothesis as
> `prop:positive`. Four steps: `r_{n−2} ≤ r_{n−1}` from `S1-02`, substituted
> into `r_n = r_{n-1} + r_{n-2}/(b(n−1)b(n))` to give
> `r_n ≤ r_{n−1}(1 + ε_n) ≤ r_{n−1} exp(ε_n)`, iterated down to `r_1 = 1`, then
> passed to the limit using the summability `prop:exists` already has.
>
> - **`S26-01` PROVEN**; checked numerically at dps 60 to `n = 20000` over ten
>   positive `b` (`S26-02` VERIFIED), with a can-fail arm and an engine
>   known-answer arm (`S26-03`).
> - **The positivity hypothesis is load-bearing**, not decorative: three of six
>   sign-changing `b` violate the inequality outright (`S26-04`). State the
>   hypothesis; do not quietly inherit it from context.
> - **Do not write the two-sided form citing `S1-02`.** `S1-02` supplies the
>   lower bound and the monotonicity step only. The upper half carries
>   `S26-01`.
> - **Drafting action:** insert Proposition U after `prop:positive` in
>   `theorem.tex`, hypothesised identically, ~15 lines. It is *not* inserted
>   there yet — `theorem.tex` belongs to `CT-S1-THEOREM` and this corpus does
>   not edit earlier sessions (`CT-S26-UPPER-BOUND/REPORT.md` §6 item 1).
> - The proof uses **no** minimal-solution, Pincherle or Perron–Kreuser input,
>   so §2.0's undertaking extends to it unchanged.

#### §2.0 Attribution — a required paragraph, placed first in the section

**Without this paragraph §2 reads as a claim of novelty it does not make.** It
is the one place in the paper where the material could appear to claim something
classical. The adaptable draft already exists at
`CT-S8-LITCHECK/PRIOR-ART.md` §2, and the verdict table there is §1. The
paragraph must carry, in this order:

1. **The radius is prior art** — an immediate corollary of the **Perron–Kreuser
   theorem** with **Pincherle**'s minimal/dominant dichotomy supplying `(H)`.
   Write the recurrence as `Q_{n+1} + a_n Q_n + b_n Q_{n-1} = 0` with
   `a_n = −b(n+1) ~ −β_d n^d`, `b_n = −1`; the Newton–Puiseux vertex
   `P₁ = (1,d)` lies above `P₀P₂`, so case (a) applies.
   *Cited to:* Gautschi, *SIAM Rev.* **9** (1967), Thm. 2.3(a) p. 35 for
   Perron–Kreuser and Thm. 1.1 p. 31 for Pincherle; DLMF §3.6(ii) for the same
   dichotomy. Held: `CT-S8-LITCHECK/refs/gautschi1967.pdf`,
   `g1967_p35_mid.png`, `refs/dlmf_3_6.txt`.
   > **Do not let this paragraph migrate into the method statement.**
   > Perron–Kreuser-plus-Pincherle is the *classical* route to the radius, and
   > it is cited here as prior art. The paper's own `(H)` comes from
   > `prop:positive` (`S1-02`), not from Pincherle, and `rem:pincherle` is
   > interpretive. §1 ¶2 was corrected at revision 5 for exactly this
   > conflation; a method paragraph led by Pincherle would also invite the
   > Birkhoff–Trjitzinsky rigour question that the box below exists to close.
2. **DLMF (2.9.5)–(2.9.6) for the bounded case, and why it does not apply.**
   (2.9.6) gives the exponent explicitly as
   `α_j = (f₁ρ_j + g₁)/(f₀ρ_j + 2g₀)`, with `ρ_j` the roots of (2.9.5) — **but
   only** under `f(n) ~ Σ f_s n^{−s}`, `g(n) ~ Σ g_s n^{−s}`, `g₀ ≠ 0`. Our
   `f(n) = −b(n+2)` grows like `n^d`, so for every `d ≥ 1` that expansion — and
   with it `f₀` — **does not exist**, and those clauses do not apply. DLMF then
   routes exactly our class elsewhere: at (2.9.14), "in which `P` and `Q` are
   any integers see Wong and Li (1992a)."
   *Held and verified:* both equation numbers and the (2.9.14) deferral are
   present in the hashed capture `CT-S8-LITCHECK/refs/dlmf_2_9.txt` (lines 127,
   143, 327, 343).
3. **Wong–Li II: NOT OBTAINED, stated plainly.** *Asymptotic Expansions for
   Second-Order Linear Difference Equations, II*, *Stud. Appl. Math.* **87**
   (1992) 289–324, DOI `10.1002/sapm1992874289` — paywalled, HTTP 403, not
   consulted. State it as a line, not a footnote. The asymmetry must be stated
   with it: the unread article **cannot reach `s`**, which is derived and
   verified here independently, and **cannot reach the framing**; it could bear
   only on a closed form for `K`.
   *Source:* `CT-R1-AUDIT/AUDIT.md` R35; `CT-S8-LITCHECK/PRIOR-ART.md` §1 row R2.
4. **The connection constant.** Classical difference-equation asymptotics fixes
   solutions only up to a multiplicative connection coefficient; that is exactly
   what `K` supplies, with the single transcendental input `r_∞` isolated into
   `(H)`.
   *Cited to two independent sources, both held and verified:*
   - **Odlyzko, *Asymptotic Enumeration Methods*, p. 77.** Re-obtained from the
     author's site and verified from a page image, not from the session record
     that first reported it. Verbatim: "*Wimp and Zeilberger point out that it
     is usually easy to show that the largest of the terms of the form (9.35)
     does show up with a nonzero coefficient, and so determines the asymptotics
     of `a_n` up to a multiplicative constant. However, the
     Birkhoff–Trjitzinsky method does not in general provide any techniques for
     determining that constant.*"
     Held: `CT-S24-PAPER-OUTLINE/refs/odlyzko_asymptotic_enum.pdf` (sha256
     `d0b58928…`), page image `refs/odlyzko_p77.png` (sha256 `f9843a43…`),
     checker `scripts/verify_odlyzko_p77.py` at 5/5 controls. VERIFIED,
     `S24-12`.
     > **Two refinements the page forces, which the intermediate record had
     > compressed and which must survive into the paper.**
     > **(i) Split the attribution.** The "up to a multiplicative constant"
     > half is Odlyzko *reporting Wimp and Zeilberger* [384]; only the second
     > sentence — that the method supplies no technique for the constant — is
     > Odlyzko's own. Citing the whole passage to Odlyzko would misattribute
     > the first half.
     > **(ii) The same page objects to Birkhoff–Trjitzinsky.** Immediately
     > below: "*The major objection to the use of the Birkhoff–Trjitzinsky
     > results is that they may not be rigorous, since gaps are alleged to
     > exist in the complicated proofs.*" A referee who checks p. 77 reads this
     > too, so the paper must pre-empt it: **nothing here rests on B–T.** The
     > growth rate is Perron–Kreuser via Gautschi, the exponent `s` is derived
     > directly, and B–T is cited only for the provenance of the normal-solution
     > *shape* (see the closing note of this section). State that in the same
     > breath as the B–T citation, not in a later section.
   - **Nemes (2026), arXiv:2508.15246v2**, abstract and §1 p. 3, on connection
     coefficients being "often treated as unknowns in other methods" and at
     best computed numerically (`CT-S8-LITCHECK/refs/nemes2025.pdf`,
     INSPECTED). **Retained alongside Odlyzko, not replaced by it** — two
     independent sources for one statement, and Nemes is the more recent.
     Odlyzko is the stronger of the two for *this* point because it is about
     Birkhoff–Trjitzinsky specifically.
5. **The contribution, stated narrowly:** the exponent
   `s = β_{d−1}/β_d + (d−1)/2` written at coefficient level for this recurrence,
   and the amplitude `K = r_∞ (2π)^{(d−1)/2} / (√d ∏_i Γ(1 − r_i))` made
   explicit through `r_∞`. The Borel framing of the radius is an expository
   repackaging of the classical statement and should be presented as one.

*Also from `PRIOR-ART.md`:* the *shape* `ρ^n n^s (1+O(1/n))` is
Birkhoff–Trjitzinsky's normal-solution shape (*Acta Math.* **60** (1933),
Fundamental Theorem §9 p. 69), which gives existence and shape but no formula
for `s` in the `β_k`.

> **Drafting discipline for this section — cite at the page, not from the
> summary.** Three citations in this corpus needed narrowing once the page was
> read: Ibrahim–Salvy ("do not know how to compute", not "is not computable"),
> the Wong–Li title, and now Odlyzko p. 77, where the attribution splits between
> Wimp–Zeilberger and Odlyzko. In each case a compressed paraphrase had survived
> into a session record. **Every §2.0 citation must be checked against the held
> page image or PDF before it is drafted**, not against a prior note.

### §3. The differential systems and their local data

One line: derivation of System A from the generating function, the scalar
reductions to Systems B and C, their exact formal types at `0` and `∞`, and the
proof that the two finite singular points have exponents `[0,0]` but are **not**
apparent.

*Claims:* `S4-03`–`S4-07` (System A and B certified; formal types; action
differences from the ODEs alone), `S4-09` (Katz mismatch in a fixed coordinate);
`S5B-C1`–`S5B-C10` (the `z = w²` pullback that removes the local mismatch, with
its vacuity control `S5B-C3`); `S6-C3`–`S6-C19` (non-apparency at both finite
points, the log coefficient `√11 i/11`, the effective Katz multiset, and the
`z ↦ 1/x` identification of B and C); `CT-S9-PVPARAMS-C005`–`C012`.

*Artefacts:* `CT-S4-FORMAL-TYPE/`, `CT-S5B-COVER/`, `CT-S6-APPARENCY/`,
`CT-S9-PVPARAMS/`.
*Note:* `S6-C19` is the corrected form of a statement the companion paper got
wrong. The **mathematics** belongs here; the errata history does not — see §4.

### §4. The moduli space of type `(0,0,1)` and the family (4.1)

One line: van der Put–Saito's `M_{t,λ}`, the chart `U₀`, the family `(4.1)`
printed **in full**, the Hamiltonian `H_V` `(4.5)` and the deformation vector
field `(4.4)`, and the statement that PV is the isomonodromy foliation.

*Claims:* `S16-01`–`S16-04` (type `(0,0,1)`, resonance, the packet's task 1(b),
and the identification of `t` as the scale of the irregular type at infinity);
`CT-S9-PVPARAMS-C002`, `C003`, `C004` (the DLMF 32.2.5 and Jimbo p.1152
conventions, and Table 2.1).

*Artefacts:* van der Put–Saito pp. 2634–2637 and p. 2655 (page images in
`CT-S23-OUTSIDER-READ/packet/pages/`); Jimbo p. 1152.
*Repairs:* **R-(c)** in full. This is the section that closes `CT-S23` open
question 1 — `(4.4)` and `H_V` `(4.5)` must be **printed**, not cited, because
§5's uniqueness conclusion rests on regularity of `(4.4)`.

### §5. System C is a point of `U₀`

One line: verification of the three hypotheses, location of the point by the
overdetermined solve, **completeness of that solve**, independent
re-substitution into the general formula, and the consequence that exactly one
PV leaf passes through it.

> **Remark (ruled in; `S25-03`, `S25-02`, `S25-06`). Two things to state here,
> both free and both strengthening the method paragraph.**
>
> **(a) The system is overdetermined by two, not one.** The non-apparency
> condition `b₁ = 0` lies in the **radical** of the ideal generated by the five
> coefficient equations — it reduces to `0` modulo their Gröbner basis — so the
> quartic matching **already forces** it. This is a cleaner statement than
> "five equations plus one condition in four unknowns", and it is why no single
> generator in the system is load-bearing.
>
> **(b) The solution set is complete, and the two branches are Galois
> conjugate.** Elimination over **`ℚ(i√11)`** gives a saturated ideal that is
> zero-dimensional of **degree 2**, with triangular lex basis and eliminant
> `27θ_∞² + 108θ_∞ + 107`, whose roots are `θ_∞ = −2 ± √3/9`. So the two
> branches are **exactly the Galois conjugates under `√3 ↦ −√3`**, exhibited by
> the eliminant rather than observed numerically. This is the structural content
> the branch relation previously lacked; it does **not** close the gauge
> question (the paper's §10; **outline** §4.1 below), and the paper must not
> claim that it does. Cross-reference
> from §10.
>
> **Name the field `ℚ(i√11)` explicitly, and say why.** The visible radicals in
> the solutions are `√33`, `√11` and `√3`, which pulls a reader toward
> `ℚ(√3, √11)`. That is the wrong base field and it is a pull the drafting
> stage must actively counter: `i√11` is the field the matching equations' own
> coefficients live in, via `s₊ = −1/6 + i√11/6` and `δ = −i√11/3`, and **`√3`
> must not be adjoined** — it is generated by the eliminant, which is the whole
> content of the conjugacy statement. Adjoining it in advance would split the
> two points and make degree 2 look like two degree-1 components for the wrong
> reason.

*Claims:* `S16-06`–`S16-11` (normal potential; `H-c`, `H-a`, `H-b`; `H-a`
satisfied *against* pre-registration; irreducibility over `C(x)` by the Riccati
test, and `S16-11`, the void first script, if a methods remark is wanted);
`S16-12`, `S16-13` (the solve, both branches, and the independent check);
`S16-14` (membership, with the regularity conditions `q(q−1) ≠ 0` and `t ≠ 0`);
**`S25-01`–`S25-03`, `S25-06` (completeness of the solve, and the remark
above)**.

*Artefacts:* `CT-S16-MEMBERSHIP-C/locate_final.py`,
`irreducibility2.py`, `outputs/pq_solution.txt`;
**`CT-S25-N1-EXHAUSTIVE/scripts/n1_exhaustive.py`, `n1_verdict.py`,
`n1_known_answer.py`.**
*Open cost:* **none — closed.** The completeness of the solve was the outline's
one mis-priced item; it is now proved. See §5 N1.

### §6. The identification is exact, not projective

One line: `R` is blind to a rank-1 twist but `(P, Q)` is not; comparing both
coefficients gives `P_F − P_C = 0` and `Q_F − Q_C = 0` identically, so the
modules are isomorphic and the twist caveat is withdrawn.

*Claims:* `S17-01`, `S17-02` (trace-freeness is **not** sufficient — the
operator's own argument corrected), `S17-03` (the self-caught defect),
`S17-04` (T3, the decisive result), `S17-05` (the structural reason it is not a
coincidence), `S17-06` (the caveat withdrawn, and why);
`S17-09`–`S17-11` (the two scalar reductions, route 1 reproducing System C
exactly, and the ordinary-point control); `S17-20`–`S17-26` (the b-route/c-route
question and the `−1/(z−q)` residual).

*Artefacts:* `CT-S17-TRACEFREE-NORM/`, `CT-S20B-COMPONENT/scripts/task2.py`,
`CT-S20B-COMPONENT/scripts/task2b.py`.

### §7. Monodromy, Stokes data, and the character variety

One line: the solver, its known-answer validation, the *selection* of
conventions, and the trace coordinates of System C at `t₀` with an error
estimate from step-size halving.

*Claims:* `S22-01` (Kummer, 32 of 32), `S22-02`, `S22-03` (orientation);
`S22-04`, `S22-05` (two checks that were vacuous as first written — methods
appendix, not main text); `S22-06`–`S22-08` (the printed `(4.1)` at the point;
the `(A_0+A_1)_{11}` sign discrepancy with vdPS p. 2629 prose; `α = e^{±iπθ_∞}`
in closed form); `S22-09` (optimal truncation); `S22-10`, `S22-11` (the 8→16
widening, and the unique surviving convention); `S22-12` (the values);
`S22-13` (a smooth point of a singular cubic fibre); `S22-14` (sensitivity).

*Artefacts:* `CT-S22-STOKES/PREREG.md` §2.3, `scripts/`, `outputs/`.
*Repairs:* **R-(d)**, `CT-S23` §4.5 — `x₁ = tr(B₂B₃)`, `x₂ = tr(B₁B₃)`,
`x₃ = tr(B₁B₂)` must be **stated** here, with `a_i = tr(B_i) ≡ 2`. This closes
`CT-S23` open question 2; the definition is on vdPS p. 2637, already supplied.

### §8. Transport along the leaf, and the second branch

One line: integrating PV in `t` and rebuilding the system leaves `x₁, x₂, x₃`
invariant to 90.81 and 91.83 digits at two step sizes; the wrong-vector-field
control fails as it must; branch 2 passes independently and is related to
branch 1 by an explicit Galois automorphism.

*Claims:* `S22-15` (the result, with its own "not a proof" sentence),
`S22-16` (the discriminating control), `S22-17` (dps 320: the agreement is not a
round-off artefact), `S22-18` (branch 2), `S22-19` (the Galois relation,
PROVEN), `S22-20` (same point of the character variety up to relabelling),
`S22-23`, `S22-24` (the invariance of `D(z)` and the non-existence of an
analytic equivalence of the assumed shape).

*Artefacts:* `CT-S22-STOKES/scripts/branch_relation.py`,
`branch_symmetry.py`, `outputs/`.

> **Upgrade available here (`S25-02`).** The two branches are now known to be
> **Galois conjugate at the level of the parameters**, exhibited exactly by the
> degree-2 eliminant over `ℚ(i√11)` whose roots are `θ_∞ = −2 ± √3/9` — the
> `√3 ↦ −√3` automorphism is the eliminant's own Galois action, not an observed
> coincidence. **State the scope precisely:** this is the structural content
> `S22-20` lacked, but it is a statement about the **parameters**, not about
> the Stokes data, which is transcendental in the entries. The branch relation
> is therefore **no longer purely numerical**; it is not thereby proved at the
> level of the character variety, and the paper must not elide the difference.

### ~~Former §9. The Borel plane: `ξ₀`, `ζ*`, and the Stokes constant~~ — **CUT, not renumbered**

**Removed from the paper by ruling (option iii).** The outline's own diagnosis
decided it: this material is connected to §§4–8 by object and not by argument,
and a section joined by subject matter breaks the chain of identifications that
is the paper's strength. Retained here as a record of what was cut and where it
goes; see §3.4.

*Material, with its home:* `S3A-01`–`S3A-05` (`ξ₀` and `ζ*` are different
singularities, `ζ*` being the action difference `2ξ₀`; the located halving; the
`~1.7%` residual accounted for); `S3B-07` (the leading Borel-singular germ);
`S22-21` (the degenerate Stage-5A basis — `Γ(1/6)` through `Γ(1/3)` and `√π`);
`S22-22` (the corrected space and the NOT FOUND).
*Destination:* **Channel Theory v1.7** (ruled; no longer "or a short note").
The reason is the same test this section failed for the paper: in v1.7 the
material connects **by argument, not by object**, because `ζ*` and
`op:cc-median-resurgence-execute` already live there. **This material must not be lost**; the degeneracy
finding in particular is methodologically valuable independently of the result.
*Artefacts:* `CT-S3A-ZETA-AUDIT/`, `CT-S22-STOKES/PREREG-STAGE5B.md`,
`CT-S22-STOKES/scripts/gamma16_identity.py`.

### §9. Scope and limits  *(was §10; §9 cut — see §3.4)*

One line: what each result does and does not say — exact identification,
numerically confirmed leaf membership, and the convention-dependence of the
trace coordinates.

*Claims:* `S16-14` (caution on strength, now superseded by `S17-04` — state
both and the order); `S16-15` (the gap, and that it is closed *numerically* by
`S22-15`); `S17-08` (the membership claim was deliberately not upgraded);
`S22-15` final sentence.
*Must contain the referee sentence:* membership is confirmed **for the trace
coordinates `x₁, x₂, x₃` under the one convention of sixteen that passed**, and
the convention selection is itself a result (`S22-11`), not an assumption.

### §10. Open questions  *(was §11)*

See §4 of this outline. **Two questions, not three** — see **outline** §4.2.

*Cross-reference to add:* the `√3 ↦ −√3` Galois conjugacy of the two branches
is now exhibited exactly (§5 remark (b), `S25-02`). It **does not close** the
`z`-dependent gauge question (the paper's §10; **outline** §4.1 below), and
this section should say so explicitly
rather than leaving a reader to infer a connection between two `√3`-flavoured
statements.

### Appendix A. A typographical error in van der Put–Saito's family (4.1)

One line: the first term of the `b(z)` entry on p. 2655 is missing a factor `t`;
under the corrected reading it equals exactly `z · B₁[1,2]`, the printed reading
fails a discriminating test whose residual carries a factor `(t−1)`, and the
error persists in arXiv:0902.1702v5 p. 34.

*Claims:* `S16-05`, `S16-18`, `S16-19`, `S16-20`, `S16-21`, `S16-R18-01`,
`S16-R18-02`; `S17-17`.
*Artefacts:* `CT-S16-MEMBERSHIP-C/`, page image p. 2655.
*Note:* this is **mathematics the paper depends on**, not errata history — the
located point is computed under the corrected reading.

### Appendix B. Computational methods

One line: precision, step control, the convergence criteria, the solver
validation, and where each script and hashed output lives.

*Claims:* `S22-01`, `S22-09`, `S22-17`; `S3B-09`; `S2-01`.
*Repairs:* **R-(b)** — the algorithms and residuals are stated here; full
reproduction still requires the scripts, which is the ordinary condition of a
paper and should be said plainly.

---

## 3. What is NOT in the paper, and why

### 3.1 The vacuity finding

**Excluded as a citation; retained as mathematics.**

The prompt material that originated this work asked the scope remark to cite
`op:xi0-singularity-type` and "the v1.6 vacuity finding". **Neither exists in
this repository** — the identifier has zero occurrences, and the newest in-repo
Channel Theory source is v1.3.1 (`CT-S0-INVENTORY/REPORT.md` §3 items 4–5;
`CT-S1-THEOREM/REPORT.md` §3.5 point 3; `S3A-06`). No citation was fabricated
and none may be.

What is retained is the *mechanism*, which is in-repo and is ordinary
mathematics: the radius depends only on `β_d` and the exponent only on `β_d`
and `β_{d-1}`, so the lower coefficients enter **only** through `K`, and any
test inspecting only the radius or only the exponent is insensitive to
`β_0 … β_{d-2}` and returns the same verdict across a whole family of `b`
(`CT-S1-THEOREM/REPORT.md` §3.5 point 2). That sentence belongs in §2 of the
paper. The external finding it was supposed to cite does not.

### 3.2 The Channel Theory framing

**Excluded.** The names `V_quad`, `Channel Theory`, `PCF`, the tier labels, the
numbering `Proposition 3.3.A` / `Conjecture 3.3.A★`, and the definition of `ρ`
as an indicial exponent in `u = √z` are private to the corpus or belong to an
unpublished external document. `CT-S23`'s mechanical index already reports
`V_quad`, `Channel Theory` and `PCF` **ABSENT** from the assembled packet, and
the material survived a cold read without them: the objects are named
mathematically (`A`, `B`, `C`; "the quadratic recurrence"). Note also that
"Proposition 3.3.A" does not exist even in the corpus — the object is
**Conjecture 3.3.A★**, proven only at `d = 2` (`S3A-06`). Importing that
numbering would import an error.

One exception, which is *not* framing: the prohibition on conflating `ξ₀` and
`ζ*` is mathematics. **With §9 cut it travels with the Borel material** — `ζ*`
no longer appears in the paper, so no prohibition is needed there, and the
prohibition must be carried wherever that material lands.

### 3.3 The corpus errata history

**Excluded.** The companion's v1.1, v1.2 and v1.3 correction notices, the
refutation of the apparency claim as a *correction to a published record*, the
retraction `RETRACT-01`, the Zenodo deposit and its DOIs, the letter to the
van der Put–Saito authors, and every cold-read and adjudication session are
publication and process history. A reader needs none of it.

Two things that look like errata and are **not**, and must stay:
- the **vdPS p. 2655 typo** → Appendix A, because the located point depends on
  the corrected reading;
- the **corrected non-apparency statement** (`S6-C19`) → §3, stated positively
  as what is true, with no reference to what a previous version said.

Also excluded: the AEAL labels themselves (PROVEN / VERIFIED / STRUCTURAL /
INSPECTED / CONJECTURED), all claim ids, all session names, and the Lean
scoping (`S1-06`, `S1-07`). The epistemic distinctions must survive **in
ordinary mathematical prose** — "proved", "verified numerically to N digits",
"we do not know" — which is the harder discipline and the one the paper is for.

### 3.4 The Borel-plane material  ⟵ **added by ruling**

**Cut** (option iii). Not because it is weak — the Stage-5B negative and the
basis-degeneracy finding are among the better results in the corpus — but
because `S22-22` records that the constant is in the native normalisation of
the recurrence and the map to P-III(D₆) **remains open**, so the section is
joined to the rest by object and not by argument. Keeping it invites a referee
question that cannot be answered without that map.

**Destination: Channel Theory v1.7** — named by ruling, no longer "or a short
note". The test §9 failed for the paper is the test v1.7 passes: there the
material connects **by argument rather than by object**, because `ζ*` and
`op:cc-median-resurgence-execute` already live in that document. Two things
v1.7 can then do that nothing else can:
- **restate `op:cc-median-resurgence-execute` with the `ζ* = 2ξ₀` finding**,
  which changes what that open problem is asking; and
- **record the Stage-5B NOT FOUND against its stated search space** — a
  negative result is meaningful only against a stated space, and that space is
  stated there.

With this, **v1.7 carries five things**, which makes it a substantial version
note rather than a thin one: (1) the Perron–Kreuser attribution; (2) the
exponent; (3) `K` through `r_∞`; (4) the vacuity explanation; (5) the
Borel/`S_{ζ*}` material with its restated open problem.

> **TRANSIT MANIFEST — the two items flagged as liable to be lost in transit.**
> Both are method, not result, which is exactly why they go missing. Neither is
> carried by any claim id that travels automatically; each must be written into
> v1.7 explicitly.
> 1. **The PSLQ basis-ellipsis repair.** The basis must be printed **in full**,
>    with no ellipsis. Source: `CT-S23-OUTSIDER-READ/REPORT.md` §3.
>    Accompanying it, the reason it matters: `S22-21` — the Stage-5A basis was
>    **degenerate**, `Γ(1/6)` being expressible through `Γ(1/3)` and `√π`, so
>    PSLQ returned that identity with **zero coefficient on `log C`** for the
>    target and every decoy alike, and the vacuity pre-check **passed for the
>    wrong reason**. A printed basis is what lets a reader check this; an
>    elided one is what hid it.
> 2. **The `ξ₀`/`ζ*` naming prohibition.** `K` is the amplitude at `ξ₀`;
>    `S_{ζ*}` is at the action difference `2ξ₀`. They are a factor of two apart
>    in the action and **must never share a name at any point**. Source: §3.2
>    and the `CT-S22-STOKES` Stage-5 scoping.

**Two consequences to carry forward, neither of them silent:**
- the paper's open-questions section now has **two** items, not three — the
  closed form for `S_{ζ*}` leaves with the material (**outline** §4.2);
- `CT-S23`'s repair "expand the PSLQ basis ellipsis" no longer applies to this
  paper. It still applies wherever the material lands, and must not be dropped
  on the way.

---

## 4. The open-questions section, as it would appear

> **Numbering convention, added after `S41-08`.** The headings in *this* part
> of the outline (`4.1`, `4.2`, …) are the **outline's own** numbering and are
> written **outline §4.1** wherever they are cross-referenced. They are *not*
> the paper's section numbers: the material below becomes the paper's **§10**.
> A bare "§4.1" in an outline that also cites the paper's §4 produces a
> reference that resolves, builds clean and says something false — which is
> exactly what `S41-08` caught before it landed in §5.

### 4.1 The `z`-dependent gauge, and uniqueness of the representative

Trace-freeness alone does not force a projective class to have a unique
representative in van der Put–Saito's normalised form (`S17-02`). A 2-torsion
twist shifts local exponents by `1/2`, but individual local exponents depend on
the choice of lattice, so whether the normalisation "local exponents `±θ_i/2`"
excludes such twists is **not settled**. The membership result does not depend
on it, because `S17-04` verifies the full operator directly rather than
inferring uniqueness (`S17-07`).

*State as:* what a proof would have to establish, so that obtaining it
supersedes this paragraph rather than rewrites it.

### 4.2 A closed form for the Stokes constant at `ζ*` — **LEAVES THE PAPER**

**This question travels with the Borel material cut at §3.4.** It is recorded
here, not deleted, because it must appear wherever that material lands — and
because the ruling that produced the cut was made on §9's structure, so this
consequence should be visible rather than inferred.

`C = 8.1273367954950723671…` is known to 100 decimal digits. In the space of
6-vectors over `{2, 3, π, Γ(1/3)}` — first shown free of internal relations by a
degeneracy pre-check — **no** multiplicative relation
`C = ± 2^a 3^b π^c Γ(1/3)^d e^f` exists with `|coeff| ≤ 10⁶`, `1 ≤ |m| ≤ 12` and
digit cost `≤ 40`; three decoys were rejected and the positive control
`4π²/(3Γ(1/3))` was recognised at cost 1.51 (`S22-22`). **This excludes that
space and is not evidence that `C` has no closed form.**

*State as:* the search space in full, then the negative. A negative result is
meaningful only against a stated space — which is why the basis ellipsis must be
expanded wherever this lands.

### 4.3 Scope limits on membership

Three distinct limits, which the paper must not merge:
1. **Exactness of the identification** is settled — `(P,Q)` agree identically,
   so the modules are isomorphic, with no twist qualifier (`S17-04`, `S17-06`).
2. **Leaf membership** is confirmed numerically to > 90 digits at two step sizes
   on both branches, and is **not proven** (`S22-15`, `S22-18`). What is missing
   is an exact isomonodromy argument, not more precision — `S22-17` shows the
   agreement is stable under a 120-digit change in working precision.
3. **Convention-dependence.** The trace coordinates are computed in the unique
   convention of sixteen that satisfies four independent conditions. That
   selection is a *result* (`S22-11`); but the paper should say what it would
   take to show the conclusion is convention-independent, which it does not
   currently establish.

---

## 5. Which of P1's repairs require new mathematics

**Settled. Nothing on this list is now a live cost.** N1 was the only item that
required new mathematics and was not avoidable; it is **closed**. N2 and N3 are
declined, N4 resolved by the §9 cut. The four assessments are retained in full,
since each records a decision and its reasons.

### N1. Completeness of the two-branch solve — **CLOSED. Was: new mathematics, time-boxed.**

> **STATUS: PROVED.** Attempted once and closed inside its one-session box by
> `CT-S25-N1-EXHAUSTIVE`. The pre-declared fallback was **not taken** and is
> recorded as unused. This item is **no longer a live cost**; the history below
> is retained because it was true when written.

**The result.** The solution set of the matching system, saturated at
`q(q−1) ≠ 0`, is **exactly** the two points recorded in `CT-S16`. Proved twice
and independently: the saturated ideal is zero-dimensional of **degree 2** over
**`ℚ(i√11)`**, bounding the points against two exhibited distinct ones; and the
lex basis is **triangular** with eliminant `27θ_∞² + 108θ_∞ + 107`, whose two
roots each back-substitute to exactly one point, matching `CT-S16`'s exactly
(`S25-02`, `S25-06`). The eliminant was **registered as a prediction before the
computation was run**.

Two things came free and are ruled into the paper — see the §5 remark:
**`b₁ = 0` lies in the radical** of the coefficient ideal, so the system is
overdetermined **by two** (`S25-03`); and the two branches are **Galois
conjugate under `√3 ↦ −√3`**, exhibited by the eliminant (see also §8).

**Note for drafting: the base field is `ℚ(i√11)`, not `ℚ(√3, √11)`.** The
ruling that commissioned this work named the latter, as did this outline before
revision 4, and the visible radicals `√33, √11, √3` pull that way. It is the
wrong field: `√3` is *generated* by the eliminant, which is the entire content
of the conjugacy statement.

---

*History, retained — this was the outline's one mis-priced item, and the
mis-pricing was a real finding when written.*

The paper says "for both sign branches" (`S16-12`), which asserts the solution
set is exactly two points. That rested on `sp.solve(eqs, [p,q,t,thi])` at
`CT-S16-MEMBERSHIP-C/locate_final.py:96` returning *all* solutions of a
polynomial system. The system is overdetermined (five coefficient equations plus
`b₁ = 0` in four unknowns) and consistent, and two independent sessions landed
on the two branches separately (`S17-15`, `S17-16`, `S17-20`) — all of which is
evidence of **correctness**, none of which is evidence of **exhaustiveness**.

A search of the whole `sessions/2026-09-17/` tree for `groebner`, `resultant` or
`exhaustiv` returned **zero hits**. No completeness argument existed.

> **`CT-S23` §3 filed this under kind (a), "proofs that exist in the corpus and
> were not transcribed". That classification was wrong: the proof did not
> exist.** It was the one item on the repair list that was mis-priced, and it is
> kept here as a finding rather than silently re-filed now that it is closed.

The reason to attempt it rather than default to the cheap line was specific:
this run had twice caught sympy behaving unexpectedly — `subs` treating
`sqrt(33)` as an atom (`S22-19` route), and the `nan` from `subs` in
`CT-S16-MEMBERSHIP-C/irreducibility.py` (`S16-11`). Replacing trust in
`sp.solve` with a proof was worth more here than it usually would be. **That
judgement was vindicated only in the weak sense that the proof went through;
`sp.solve`'s two solutions were in fact correct and complete.**

**The pre-declared fallback, now unused:** had elimination not closed inside the
box, the paper would have stated that the solver returned exactly two solutions
with **exhaustiveness unproven**, and the box would not have been extended.

### N2. Uniqueness of the normalised representative — **NEW MATHEMATICS, avoidable**

`S17-07`, the `z`-dependent gauge question. Required **only** if the paper
asserts that the representative is unique. It need not: `S17-04` exhibits the
isomorphism directly. *Recommendation:* do not pay this; state the result as
exhibited-not-unique and put the question in **§10** (the open-questions
section; this line read "§11" until revision 5 — the sections were renumbered
at revision 2, old §11 → §10, when §9 was cut).

### N3. Any upgrade of leaf membership to a proof — **NEW MATHEMATICS, large**

`S22-15` is a numerical confirmation, and says so itself. Stating the main
result as a *theorem* about leaf membership, rather than as an exact
identification plus a verified transport, requires an exact isomonodromy
argument. *Recommendation:* do not pay this. The honest statement is already
strong, and `S22-17` shows the limit is structural rather than one of precision.

### N4. The `V_quad → P-III(D6)` map — **RESOLVED: not paid; §9 cut**

`S22-22` ends: the constant `C` is in the native normalisation of the quadratic
recurrence, and **the map to P-III(D6) remains open, so `C` is not comparable
with the Stage 1–4 quantities.** §9 was therefore a *parallel strand* —
connected to the rest by object, not by argument.

**RULED: cut §9 (option iii).** The map is not obtained and not attempted. The
Borel material moves to **Channel Theory v1.7** (destination named at revision
3); see §3.4 for what travels with it, including the transit manifest. A clean chain of identifications beats a chain with a declared
appendage, and the cut removes a referee question that cannot be answered
without the map.

### Everything else on the repair list is exposition

Explicitly, and with the source of each:

| repair | why it is only writing |
|---|---|
| Print `(4.4)`, `H_V` `(4.5)`, family `(4.1)` in full | source supplied; **regularity at the point is already established** — `S16-14` records `q(q−1) ≠ 0` and `t ≠ 0` |
| State `x₁ = tr(B₂B₃)`, `x₂ = tr(B₁B₃)`, `x₃ = tr(B₁B₂)` | vdPS p. 2637, already supplied as a page image |
| Restore `(A2)` | `CT-S3B-RINF/DERIVATION.md` L22–27; and `S3B-03` *proves* no root of `3n²+n+1` is a positive integer |
| Rename the three `r`-objects | **RULED: rename in the paper only.** Fix the notation in the paper and note the correspondence to the deposited names in **one footnote**; leave the deposited records alone. Renaming across published records to fix a collision a footnote resolves is not worth the churn |
| Define Katz multiset, `D̃₅`, PV, `K`, `A`/`B`/`C` | standard, or defined in the cited source |
| Define `Γ`, `O`, `o`, `~`, `dps`, PSLQ, Richardson, Newton polygon, germ coefficient, amplitude, `c_±` | standard vocabulary |
| Expand the PSLQ basis ellipsis; state the `N/2`-vs-`N` criterion | values exist in `S22-22`, `S3B-09` |
| Transcribe proofs of Propositions 1–4 | `S1-01`–`S1-04`, all PROVEN |
| Riccati solutions ⇒ reducibility | standard; cite van der Put–Singer |
| State algorithms and residuals for the six computations | `S16-12`, `S17-04`, `S22-11`, `S22-15`, `S22-22`, `S16-20` |

**Summary for the operator.** **The paper has no new mathematics left to do. It
is a drafting job.** **N1** was the single remaining item and is **closed**, its
fallback unused. **N2** and **N3** are declined by stating results as they
stand. **N4** is resolved by cutting §9. Drafting is now §1 absorbing most of
the 171 items, §2.0 carrying the attribution, and the §5 remark carrying the two
results that came free with N1.

**Revision 6.** The one **drafting** decision that survived N1's closure — prove
the upper bound on `r_∞` or weaken §1 ¶2 to the one-sided form — is also
settled: it is **proved** (`S26-01`, `CT-S26-UPPER-BOUND/PROOF.md`), the
fallback again unused, and the only residue is the ~15-line insertion into
`theorem.tex` at drafting, plus the requirement to state the positivity
hypothesis explicitly because it is load-bearing (`S26-04`). Nothing on this
list is now a live cost of any kind.

*History: this line previously read "one piece of mathematics left to attempt".
The mis-pricing finding that produced it stands — it was true when written, and
is retained in N1 above.*

**No citation is now blocked.** The Odlyzko p. 77 reference was blocked at
revision 2 and was **cleared at revision 3**: re-obtained from the author's
site and verified from a page image at 5/5 controls (`S24-12`), and written
into §2.0 item 4 **alongside Nemes** rather than in place of it. Every citation
in §2.0 is sourced to a held, hashed artefact.
