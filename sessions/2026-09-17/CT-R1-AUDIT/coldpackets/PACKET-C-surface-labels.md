# Cold packet C — a claimed surface-type classification

You are given a chain of claims. Decide whether each is correct. Nothing in this
packet is asserted to be true except the published table in §1, which you must
read yourself from the supplied page images.

## 1. The published classification table

The source is:

> M. van der Put and M.-H. Saito, *Moduli spaces for linear differential
> equations and the Painlevé equations*, **Annales de l'Institut Fourier 59**
> (2009), no. 7, pp. 2611–2667.

A copy is in the repository at
`sessions/2026-09-17/CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`.
You may open **that PDF**. Rendered page images are also provided:

* `sessions/2026-09-17/CT-R1-AUDIT/coldpackets/vdps_p2634.png` (journal p. 2634)
* `sessions/2026-09-17/CT-R1-AUDIT/coldpackets/vdps_p2635.png` (journal p. 2635)

Read the table **from the page image**, not from an OCR text layer. Quote the
rows you use verbatim, with the page number and the table's number as printed.
Also record what the table's columns mean, and in particular what the entries
`r(0), r(1), r(∞), r(t)` and `dim` denote, quoting the surrounding text.

## 2. The object under study ("System A")

Let `b(n) = 3n² + n + 1` and define `Q_n` by

```
    Q_n = b(n) Q_{n-1} + Q_{n-2},     Q_{-1} = 0,  Q_0 = 1,
```

so `Q = 1, 5, 76, 2361, 125209, 10144290, ...`. Let `f(z) = Σ_{n≥0} Q_n zⁿ`.

**Claimed (A0):** `f` satisfies

```
    3z³ f'' + 10z² f' + (z² + 5z − 1) f  =  −1 ,
```

i.e. the homogeneous operator is `L_A = 3z³D² + 10z²D + (z² + 5z − 1)`.

## 3. The claimed chain

**(A1)** The normal-form potential of `L_A` is
`r_A = (−3z² − 5z + 3) / (9z³)`.

**(A2)** At `z = 0`, `r_A` has pole order `3`, which is **odd**, so `z = 0` is an
**irregular ramified** singular point with ramification index `2` and **Katz
invariant `1/2`**, with exponential parts `exp(∓(2/√3) z^{−1/2})`.

**(A3)** `z = 0` is the **only finite** singular point, and at `z = ∞` the pole
order is `3`, so `z = ∞` is also irregular ramified with **Katz invariant `1/2`**.

**(A4)** Hence System A's Katz multiset is `(1/2, −, 1/2)`, and looking this up
in the table of §1 places System A in the **PIII(D₈)** row (Dynkin type `D̃₈`).

**(A5)** Under the ramified double cover `z = w²`, the pullback `π*(System A)`
has **unramified** Katz invariant `1` at `w = 0` and `1` at `w = ∞`, giving Katz
multiset `(1, −, 1)`, which the table places in the **PIII(D₆)** row
(Dynkin type `D̃₆`).

**(A6)** Therefore the object that a certain body of work computes on — namely
`f = Σ Qₙ zⁿ` — sits in the PIII(D₈) row, and its quadratic cover sits in the
PIII(D₆) row. In particular **neither is `D̃₅` / PV**.

## 4. What you are asked to do

Answer each numbered question with a verdict of SOUND / SOUND WITH CAVEAT /
ERROR, and give reasons.

1. **Verify (A0)** by exact computation: generate `Qₙ` from the recurrence in
   exact integer arithmetic, substitute the series into the claimed ODE, and
   confirm the residual vanishes to as many orders as you can manage (at least
   `z⁰` through `z³⁰`). Report the order reached.
2. **Verify (A1)** symbolically from `L_A`. State the normal-form convention you
   use (e.g. `y'' + p y' + q y = 0` with `r = p²/4 + p'/2 − q`, or whichever you
   adopt), since the sign convention affects the expression.
3. **Verify (A2) and (A3)** by exact computation: pole orders at `0` and at `∞`
   (transform to `t = 1/z` carefully and state the weight/Jacobian convention
   you use), the parity argument for ramification, the ramification index, the
   Katz invariant, and the exponential parts. Confirm there is no other finite
   singular point.
4. **Verify (A5)**: pull back along `z = w²` and recompute. Confirm the Katz
   invariant doubles and the ramification index drops from `2` to `1`, at both
   `w = 0` and `w = ∞`.
5. **Check the table lookups (A4) and (A5)** against the page image. Quote the
   matching rows verbatim with the page number. Confirm the multiset ordering
   convention you are using matches the table's column headings, and say whether
   the `−` entries in the claimed multisets correspond to the table's `−`
   entries in the way the claim assumes.
6. **Assess (A6) critically.** In particular:
   - Is a matching row a **necessary** condition, a **sufficient** condition, or
     both, for the object to belong to the corresponding family? Quote whatever
     the paper says about what the table classifies.
   - Does the table classify **families** of connections, or individual
     operators? Does the claim respect that distinction?
   - The table lists a `dim` column. What is the dimension for the PIII(D₈) row,
     and does that value have any bearing on whether a single fixed operator can
     be said to "sit in" that row?
   - Note that `L_A` is a **scalar** operator while the table concerns rank-2
     **connections**. Is the passage between them addressed? Does it need a
     twist, a gauge transformation, or a cyclic-vector construction, and would
     any of those change the Katz data? State what would have to be checked.
7. Give an **overall verdict** on the chain, and state separately whether the
   final sentence of (A6) — "neither is `D̃₅` / PV" — is justified.

## 5. Rules

- Work only inside `sessions/2026-09-17/CT-S13-COLDREAD5/` (create it).
- Under `sessions/2026-09-17/` read **only** this packet, the two page images
  named in §1, and the van der Put–Saito PDF. Do not open anything else in that
  tree — in particular not the other files in `coldpackets/`, not
  `CT-R1-AUDIT/CLASSIFICATION-TABLE.md`, `AUDIT.md`, `REPORT.md`, any
  `VERIFY-*.md` or `DRAFT-*.md`, and not any other session folder such as
  `CT-S4-FORMAL-TYPE` or `CT-S5B-COVER`. This is a cold read.
- Do not reconstruct any published table or result from memory. If you need a
  source you cannot obtain, say what is missing and stop.
- Do not commit, push, tag, or open a PR. Leave everything uncommitted.
- Use exact symbolic computation (SymPy). Include your scripts and outputs.
- If the packet is ambiguous, say so rather than guessing.
