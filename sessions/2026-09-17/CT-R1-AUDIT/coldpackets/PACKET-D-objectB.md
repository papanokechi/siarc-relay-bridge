# PACKET D — cold read of object B's formal type and its Table 2.1 row

**You are an independent reviewer.** This packet is self-contained by design.
Everything you need is either stated below or in the named files. Nothing else
under `sessions/2026-09-17/` may be opened.

## Isolation rule

You may read **only**:

* this packet;
* `CT-R1-AUDIT/coldpackets/vdps_p2634.png` and `vdps_p2635.png` (van der
  Put–Saito, journal pp. 2634–2635, including Table 2.1);
* `CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`;
* `CT-R1-AUDIT/coldpackets/companion_v12_p2.png` and `companion_v12_p3.png`
  (companion v1.2, the pages defining the System C operator);
* your own deliverables in `sessions/2026-09-17/CT-S14-COLDREAD-B/`.

Do **not** open any other file in that tree — in particular not
`CT-S4-FORMAL-TYPE/`, `CT-S5B-COVER/`, `CT-S6-APPARENCY/`, any other
`coldpackets/PACKET-*`, `CLASSIFICATION-TABLE.md`, any `DRAFT-*`, `VERIFY-*`,
`AUDIT.md`, `REPORT.md`, or any `claims.jsonl`. Those hold the derivation you are
being asked to check independently. **If you open something you should not have,
say so in your report rather than concealing it.**

Read the published table and any load-bearing sentence from the **page images**,
not from a PDF text layer. Quote what you use verbatim, with the page number.

## Object B — `L_φ`, as given

`L_φ` is a second-order scalar operator whose **normal form** — the form
`y'' = r(z) y`, printed in the source paper — is

```
                11 z⁴ + 4 z² + 4 z + 12
    r(z)  =  ──────────────────────────────
              4 z⁴ ( z² + z + 3 )²
```

That expression is given to you as data. You may recompute anything you like
from it, but do not assume any classification of it.

## Object C — the companion's operator, for step 2

Companion v1.2 defines its ODE with polynomial coefficients; read them from
`companion_v12_p2.png` / `companion_v12_p3.png` (there is a table of polynomial
data on the second of those). Take the operator from the page image, not from
any restatement.

## Tasks

1. **Face-value formal data for `L_φ`.** At **every** singular point, including
   `z = ∞`, compute exactly: the local exponents, the Newton polygon, the
   ramification, and the Katz invariant. State the resulting multiset **in the
   authors' own notation** (see p. 2634 for how they designate families).

2. **Relation between B and C.** Determine whether `L_φ` and the companion's
   operator are related by `z ↦ 1/z`, by a rank-1 twist, or by both. Give each
   transformation **explicitly** and verify the equivalence **symbolically, with
   a script**. If they are not equivalent, say so.

3. **Integer-difference points.** For any point whose exponents differ by an
   integer, decide **exactly** whether it becomes an ordinary point after the
   twist. Show the computation; do not argue by analogy.

4. **The question this packet exists for.** Decide whether the twist used in
   step 2 is **compatible with van der Put–Saito's normalisation** — that is,
   with the class of connections Table 2.1 actually classifies. Their table
   concerns rank-2 connections **normalised to be trace-free**. A rank-1 twist
   changes the trace. So:

   * Quote, from the page image, the sentence(s) that define the class Table 2.1
     classifies.
   * Determine whether a trace-altering twist takes an object **into or out of**
     that class, and whether the row is preserved under it.
   * If the answer depends on a condition (for example on the twist's
     determinant, or on it being by a rational/regular function), state the
     condition precisely.

   A clear negative or "cannot be determined from this source" is more useful
   than a strained positive.

5. **Row lookup.** Give the Table 2.1 row, if any, for `L_φ` **at face value**
   and for `L_φ` **after** the transformations of step 2. Quote each row
   verbatim with its page number. If either has no row, say so explicitly and
   explain what in the table's construction excludes it.

6. **Verdict on the drafted sentence.** A draft correction notice contains this
   table row, describing object B:

   > | **B** | `L_φ` | `(0,0,1)`, up to inversion and twist | PV / `D̃₅` |

   Answer exactly one of: **CORRECT** / **CORRECT WITH WORDING CHANGE** (give the
   change) / **ERROR**. Justify from your own computations and from the page
   images.

## Labels

Use: PROVEN (complete proof or machine-checked) · VERIFIED (numerically checked,
with dps and residual) · INSPECTED (fact about a named file or page at a stated
hash, valid only for that commit) · STRUCTURAL · CONJECTURED. Never upgrade a
label in prose.

**A Table 2.1 row match is STRUCTURAL at most, and is a necessary condition
only.** Matching a row does not establish membership of the corresponding
isomonodromic family.

## Deliverables

In `sessions/2026-09-17/CT-S14-COLDREAD-B/`: `REPORT.md`, `claims.jsonl`, and
every script with its output. Record sha256 for each source you read and for
each output file. Report the repository HEAD at the start and at the end; make
no commits, pushes, tags or PRs, and write nothing outside your session folder.
