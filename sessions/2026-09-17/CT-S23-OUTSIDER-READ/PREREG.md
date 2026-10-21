# CT-S23-OUTSIDER-READ — PREREG

Written **before** the packet was assembled and before any cold read was
dispatched. Nothing in this file was changed after any result was seen.

---

## 0. A finding that precedes the task, and changes how it must be run

The packet named in the task as **PROVIDED** does not exist. There is no paper
draft in this repository and no assembled packet file. The task's own sources —
`CT-S16-MEMBERSHIP-C`, `CT-S17-TRACEFREE-NORM`, `CT-S20B-COMPONENT`,
`CT-S22-STOKES`, and the companion v1.3 correction notice — all exist, as do
every page image the task names. So this is not a HALT for missing data: it is a
**mis-description of state**. The packet has to be *assembled* first, and its
assembly is a deliverable of this session, not a precondition of it.

**The second finding is the one that governs the method.**

The task specifies a reader who is *cold* and *isolated* — one with graduate
background in ODEs, isomonodromy and Painlevé theory but **no knowledge of this
author's previous work**. The agent assembling the packet has all five source
sessions in context and cannot discard them. A self-containment audit performed
by a reader who can silently supply every missing definition from memory is
**structurally incapable of detecting the defect it is looking for**. It would
return a confident, fully-documented SELF-CONTAINED for reasons having nothing
to do with the packet.

This is the same shape as the Stage-5A degeneracy: not a check that cannot fail,
but a check that *can* fail and would fail *for the wrong reason* — or here,
pass for the wrong reason. Declaring the contamination in prose and proceeding
anyway would be the C4 defect: a caveat where a control is required.

**Therefore the read is dispatched to a separate context that receives the
packet path and nothing else**, and is instructed to read no other file. The
assembling agent does not answer tasks 1–5. It assembles, controls, and
adjudicates. This division is recorded here, in advance, as part of the method.

---

## 1. Hypothesis

**H.** The assembled packet `packet/PACKET.md`, together with the page images in
`packet/pages/`, is self-contained for the stated reader: every object it uses
is defined within it, and every claim it makes rests only on facts stated in it
or in the supplied page images.

## 2. Observable

The cold reader's returns for tasks 1–5:

- `T1` — ordered list of points where it could not proceed;
- `T2` — list of terms/symbols/objects used before definition;
- `T3` — list of claims resting on facts not in the packet;
- `T4` — its statement of the main result and the method;
- `T5` — verdict in {SELF-CONTAINED, SELF-CONTAINED AFTER LISTED REPAIRS,
  NOT SELF-CONTAINED}.

## 3. Falsifier, with a numeric threshold

**F1 (the instrument).** A **control fragment** is dispatched to a second,
equally isolated reader under the *identical* prompt. The control is
`packet/control/CONTROL-FRAGMENT.md`: the CT-S22 claims table alone, stripped of
all surrounding definitions. It is not self-contained by construction — it uses
`S16-15`, `vdPS`, `x₁,x₂,x₃`, `α`, `θ_∞`, `Γ(1/6)`, `PSLQ`, `V_quad` and
`S_{ζ*}` with no definition of any of them.

> **F1 fires if the control reader returns SELF-CONTAINED, or returns fewer
> than 5 items in `T2`.** If F1 fires the instrument cannot discriminate, the
> main read is **VOID rather than negative**, and this session halts and reports
> that instead of a verdict.

**F2 (sensitivity of the main read).** `scripts/jargon_index.py` computes, by
first-occurrence position and mechanically, which of a **pre-declared core term
set** are used in `PACKET.md` before any definition of them appears. The core
set is fixed **now**, before the packet is written:

```
V_quad, Channel Theory, System A, System B, System C, PCF,
xi_0, rho, K, r_inf, S_zeta_star, zeta_star,
B1/B2/B3, Q_n, theta_infty, U_0, the (0,0,1) row,
Katz multiset, PV / P-V, D5-tilde, Stokes constant, trace coordinates
```

Let `G` be the set the index reports as used-before-defined. F2 is recorded, not
fired, if `|T2 ∩ G| / |G| < 0.5` — a read that misses more than half of a
mechanically-detectable list is recorded as **low-sensitivity**, and its
SELF-CONTAINED verdict, if any, carries no weight.

`G` is computed **after** the packet is written and **before** the read is
dispatched, and its value is hashed into `outputs/` at that time so it cannot be
adjusted afterwards.

## 4. Vacuity pre-check

Two arms, both required, both able to fail:

- **(i) The observable must move when the packet moves.** The control fragment
  and the full packet are dispatched under the identical prompt. If the two
  reads return the same verdict and comparable `T2` lengths, then the observable
  is not reading the packet, and the exercise is void. This is arm F1 above,
  stated as the vacuity condition it also is.
- **(ii) The instrument must be able to return each verdict.** The prompt offers
  three verdicts. The control is constructed so that NOT SELF-CONTAINED is the
  only defensible one; the packet is assembled with the honest intention of
  being self-contained. If *both* reads return the same verdict, (i) fires.

**Degeneracy pre-check on the core term set** (per the clause proposed in
`CT-S22-STOKES/P0-AMENDMENT.md`): the core set is checked for internal
redundancy before use — no term in it may be a substring alias of another such
that one match mechanically forces another (e.g. `zeta_star` inside
`S_zeta_star`). Aliasing pairs are collapsed and the collapse is recorded, so
that `|G|` is not inflated by terms that cannot be independently missed.

## 5. What would make this session HALT

- F1 fires (control reader cannot discriminate).
- A source named in the task cannot be found. *(Checked: all five sources and
  all named page images were located before this file was written.)*
- The cold reader reports having read a file outside `packet/`.

## 6. Labels

`INSPECTED` for anything read off a source file or page image. `STRUCTURAL` for
the adjudication of a cold return. **The cold reader's verdict is evidence, not
a label** — it is recorded as the return of an instrument whose discrimination
is established by F1, and nothing in it is upgraded.

## 7. Budget

≤ 1 day. Assembly is the expensive step; the reads are single passes.
