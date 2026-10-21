# GATE 2 — verification of the CT-S13-COLDREAD5 cold read of C4

**Gate:** *"C4 has not had a cold read. […] Give it one cold packet with the van
der Put–Saito page image included."* (Operator review #5, gate 2.)

## Session conduct

The session **halted correctly on its first dispatch**. I sent it before its
packet existed, and rather than improvising or substituting other files, it
reported the missing named evidence and stopped. That is the behaviour the
governance rules ask for, and the ordering error was mine, not its.

On resumption it reported HEAD `08aa0e2…` unchanged at start and end, and
affirmed that it opened only the packet, the two named page images, the named
PDF, and its own deliverables. It recorded sha256 for all three sources.

## Verdict returned

| Item | Verdict |
|---|---|
| (A0) the ODE annihilates `Σ Qₙ zⁿ` | SOUND — verified to `z⁴³` in its own code |
| (A1) normal form `r_A = (−3z²−5z+3)/(9z³)` | SOUND |
| (A2)/(A3) Katz `1/2` at `0` and `∞`, ramified | SOUND |
| (A5) quadratic cover doubles both slopes to `1`, unramified | SOUND |
| (A4)/(A5) table lookups | SOUND WITH CAVEAT |
| **(A6) family membership** | **ERROR** |
| "neither is `D̃₅`/PV" | SOUND WITH CAVEAT |

## The finding that matters — independently verified

Q6 produced something this run did not previously have. I re-read journal
p. 2634 from the PDF myself rather than take it on report. **The quote is
verbatim correct:**

> "For a differential module `M` corresponding to one of the types, the strong
> Hilbert-Riemann problem has a positive answer, except possibly for
> `(1/2, −, 1/2)` and `(−, −, 5/2)` (see Definitions and examples 1.12). For
> these two types we only consider the modules `M(u)` for which the strong
> Riemann–Hilbert problem does have a positive answer."

**`(1/2, −, 1/2)` is object A's type.** Of ten families, exactly two are
exceptional in this way, and object A's is one of them. The authors do not
classify all modules with that Katz data; they **restrict** the row to those for
which the strong Riemann–Hilbert problem is solvable — a condition nothing in
this run has checked for object A.

This is a genuine defect in C4 as drafted, and it is the second time a cold read
has caught a load-bearing gap under a confident label. It has been written into
the notice as point **5**, together with the scalar-to-connection gap (point 6)
and `dim P = 0` (point 7), which the reader also raised.

## One caveat I do not accept, on evidence

The reader recorded Q5 as SOUND **WITH CAVEAT** on the ground that the
three-entry notation `(1/2, −, 1/2)` "suppresses the full four table columns and
should be read with the table's ordered-column convention".

The ordered-column point is right and has been adopted. But the premise that the
three-entry form is a contraction introduced by us is **incorrect**. On the same
page 2634, the authors write:

> "We will not number these ten families, but indicate them by their Katz
> invariants, e.g., `(0, 0, 0, 0)`, `(0, 0, 1)`, …, `(0, −, 3/2)`, `(−, −, 3)`,
> `(−, −, 5/2)`."

and then use `(1/2, −, 1/2)` in running text in the passage quoted above.
**The three-entry form is van der Put–Saito's own designation for the family.**
Using it is therefore correct practice, not a shorthand needing defence. Both
facts — their notation, and the four ordered columns of the printed table — are
now stated explicitly in the notice.

This is not a criticism of the reader: an isolated reader seeing a four-column
table and a three-entry tuple is right to flag it. Resolving it required the
running text, which confirms our usage.

## Effect on the deposit

C4 survives, **weakened and better supported**:

* the row matches themselves are independently reproduced;
* the sufficiency inference is removed, which was already the operator's
  stated position (*"a matching Katz multiset is necessary, not sufficient"*);
* a new, sharper restriction is added that is specific to object A's row.

C4's review status moves from `self` to **`cold`**, which was the object of the
gate.

## Labels

| Claim | Label | Review |
|---|---|---|
| The Katz data of object A and its cover, and the Table 2.1 row matches | STRUCTURAL | `cold` — recomputed in independent code, table read from page images |
| `(1/2, −, 1/2)` is one of two types for which vdP–Saito restrict the family by a strong Riemann–Hilbert condition | INSPECTED | `cold` — found by the cold reader, then independently re-read from the PDF by this session |
| `(1/2, −, 1/2)` is vdP–Saito's own notation for the family | INSPECTED | `self` |
| Family membership of object A in PIII(D₈) | **NOT ESTABLISHED** | — |
