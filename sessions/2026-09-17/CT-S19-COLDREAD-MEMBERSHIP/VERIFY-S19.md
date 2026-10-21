# VERIFY-S19 — adopting `CT-S19-COLDREAD-MEMBERSHIP` claim by claim

Verdict returned: **CORRECT WITH WORDING CHANGE**. Adopted, with one part of the
proposed rewrite declined and the reason recorded.

Adjudication script: `../CT-S17-TRACEFREE-NORM/adjudicate_s19.py`,
output `outputs/adjudicate_s19.out.txt`, sha256
`7b6c6b75e5c82f422faa4e41166e32054c7ecbd9b9b2091d1bf77e44a6a33f1d`.
Stage-1 seal: `D193E1A1A407DA2B2AF57B9669C70D56E164BB1ECCE4FBE77234B5E55113D1B5`.

---

## The packet worked

It was reissued because `CT-S18` had silently chosen a component. Named as task 1,
the question was answered correctly and, better, **from the source**:

> [INSPECTED] *"The first basis vector is chosen as cyclic vector and following
> Subsection 4.1, `q` is the unique zero of `c(z)` and `p = a(q)`."* — p. 2655

I confirmed this quotation by rendering and **looking at** the page myself. It is
verbatim. This settles the component question by the authors' own stated
convention, and is **stronger than the structural argument** used in `VERIFY-S18`
(that System C has no third finite singular point). Adopted, and it supersedes
my reasoning while confirming my conclusion.

The reader also noticed, unprompted, that `q` being read off `c(z)` bears on the
*second*-component reduction — the precise trap `CT-S18` fell into.

## Adopted claims

| Claim | Status |
|---|---|
| `S19-001`, `S19-002` | **ADOPTED.** Both reductions derived independently; agrees with `S17-09`. |
| `S19-003` | **ADOPTED**, and it is the packet's best result — see above. |
| `S19-004` | **ADOPTED.** Same affine map and `P_C = (2z−1)/(z(z−1))` as prior work, re-derived. |
| `S19-005` | **ADOPTED.** A third independent confirmation of the `b(z)` correction. |
| `S19-006` | **ADOPTED, and re-verified in my own code.** See below. |
| `S19-007` | **ADOPTED.** Confirms the second-component reduction is not System C. |
| `S19-008`, `S19-009` | **ADOPTED.** Controls fire; the system-solve route gives max residual `4.0e-208` at dps 100 over 3 points × 3 seeds. |
| `S19-010`, `S19-011` | **ADOPTED**, including its honest **UNDECIDED** on `s₃ ∈ C*`, which the packet could not decide because it contained no monodromy data. |
| `S19-012` | **ADOPTED IN PART** — see "the declined part". |

## The independently derived point, and a corroboration nobody designed

`CT-S19` derived its own point of `U₀` with no sight of `CT-S16`/`CT-S17`. It
landed on the **opposite branch**:

| | `t` | `θ∞` | `√33` term of `q` |
|---|---|---|---|
| CT-S17 | `−2i√33/9` | `−2 − √3/9` | `+281700·i/122408` |
| CT-S19 | `+2i√33/9` | `−2 + √3/9` | `−281700·i/122408` |

Re-verified in independent code: **both** points give `db/dz = 0`, `q ∉ {0,1}`,
`P − P_C = 0`, `Q − Q_C = 0` exactly, and `t² = −44/27`. The relation is exact:
`t₁₉ = −t₁₇`, and `q₁₉`, `θ∞,₁₉` are `q₁₇`, `θ∞,₁₇` with `√33 ↦ −√33`,
`√3 ↦ −√3`. Controls fired on 3/3 perturbations (`q` nudged, `p` nudged, `t` sign
alone).

So two isolated sessions, between them, exhibited **both signs** of the
companion's printed `t = ∓2i√33/9`. That was not designed, and it is a stronger
corroboration of the `∓` than either session alone.

## The declined part of the wording change

The reader recommended replacing *"Membership on a single isomonodromic leaf
follows from the framework"*, on the ground that it *"overstates what I
established because I did not compute the monodromy/Stokes data or identify the
leaf."*

**That is a statement about the scope of its own check, not a defect in the
sentence.** The sentence attributes the leaf to vdPS's framework — their theorem
that PV is the isomonodromy foliation on `M` — which was read from page images in
`CT-S16` task 1. `CT-S19` was not asked to verify that, and its packet contained
no monodromy data, so it could not have. The sentence already says the
computation has **not** been done and marks it **open**, which is exactly the
reader's point.

Declining this is a judgement, and it is recorded as one. What **is** adopted
from `S19-012` is the sharper locution: the connection is located **in the chart
`U₀`**, which is where the verification actually happened.

## Wording adopted

`U₀` is a chart *of* the moduli space, so locating a point in `U₀` **is**
exhibiting a point of `M`; the two formulations agree, and naming the chart says
where the check was done. C3 now reads "*is a point of the van der Put–Saito
moduli space for that row, exhibited explicitly in the chart `U₀` of that space*",
with a footnote recording the two branches.

The reader's full alternative sentence is preserved verbatim in its `VERDICT-5.md`
for the operator, who drafted the original wording and may prefer it.

## Effect on the deposit

| Support row | Before | After |
|---|---|---|
| `C3 moduli-space membership` | `self` | **`cold`** |

The row clears. The chart location was independently re-derived from scratch by a
reader that also, unprompted, produced the source quotation justifying the
component choice — the exact point on which the previous cold read had erred. The
one hypothesis it could not settle, `s₃ ∈ C*`, is a monodromy condition, and it is
the same monodromy/Stokes computation that C3 already names as **open**.

**48 of 49 supporting claims now clear.** The remaining one is `R1-57`, which is
CONJECTURED on the face of the notice and carries no weight.
