# PACKET E — cold read of two deferred claims

**You are an independent reviewer.** Two statements are put to you. They are
unrelated to each other; answer them separately and do not let either influence
the other.

## Isolation rule

You may read **only**:

* this packet;
* `CT-R1-AUDIT/coldpackets/vdps_p2634.png` and `vdps_p2635.png`
  (van der Put–Saito, *Ann. Inst. Fourier* **59** (2009), journal pp. 2634–2635,
  including Table 2.1);
* `CT-R1-AUDIT/coldpackets/jimbo_p1152.png` (Jimbo, *Publ. RIMS* **18** (1982),
  journal p. 1152);
* `CT-R1-AUDIT/coldpackets/companion_v12_p2.png` and `companion_v12_p3.png`;
* your own deliverables in `sessions/2026-09-17/CT-S15-COLDREAD-DEFERRED/`.

Do **not** open any other file under `sessions/2026-09-17/` — in particular not
`CT-S9-PVPARAMS/`, `CT-S13-COLDREAD5/`, `CT-S14-COLDREAD-B/`, any other
`PACKET-*`, any `DRAFT-*`, `VERIFY-*`, `AUDIT.md`, `REPORT.md`, or any
`claims.jsonl`. Those hold the reasoning you are being asked to check
independently. If you open something you should not have, say so in your report
rather than concealing it.

Read every load-bearing statement from the **page images**, not from a PDF text
layer. Quote what you use verbatim, with the page number.

---

## Statement 1 — on `dim P` in van der Put–Saito

> **`dim P = 0` in the PIII(D₈) row of Table 2.1 means only that the family has
> no free parameters. `P` is the parameter space of the family. A zero-dimensional
> `P` is the expected and correct value for PIII(D₈); it is not a defect, and it
> says nothing about the isomonodromic *time* variable, which still gives a
> one-dimensional deformation.**

### Tasks

1. From the page images, establish what `P` **is** in these authors' setup.
   Quote the sentence(s) that define it, with the page number.
2. Determine whether `dim P = 0` in that row carries the meaning asserted above,
   a different meaning, or an undetermined one.
3. Decide specifically whether `dim P = 0` bears on the existence or dimension of
   the **isomonodromic time** / deformation direction. Note that the table's
   columns include an `r(t)` entry; take a view on whether `t` here is a
   singular point of the connection, a deformation parameter, both, or whether
   the source does not say.
4. State whether the PIII(D₈) row's `dim P = 0` is what the source's own
   construction would lead you to expect, or anomalous.
5. Verdict on the statement, exactly as quoted above:
   **CORRECT** / **CORRECT WITH WORDING CHANGE** (give the change) / **ERROR**.

---

## Statement 2 — on the companion's operator and Jimbo's Painlevé V system

> **The scalar local data alone do not exhibit a Jimbo Lax embedding or a
> Painlevé V deformation time for the companion's operator.**

The companion's operator is defined by polynomial coefficient data on
`companion_v12_p2.png` / `companion_v12_p3.png`; read it from the page image.
Jimbo's Painlevé V system, its parameter dictionary and its standing assumption
are on `jimbo_p1152.png`.

### Tasks

6. State Jimbo's system `(3.1)` and say precisely what data an operator must
   carry to be an instance of it — in particular what plays the role of `t`, and
   what the second equation of `(3.1)` requires.
7. Decide whether the **scalar local data** of the companion's operator — its
   singular points, exponents, and formal type — suffice to exhibit such an
   embedding, or a deformation time. If they do not, say exactly what is
   missing; if they do, exhibit it.
8. Verdict on statement 2, in the same three-way form as task 5.

---

## Labels

Use: PROVEN · VERIFIED (state dps and residual) · INSPECTED (a fact about a
named file or page at a stated hash) · STRUCTURAL · CONJECTURED. Never upgrade a
label in prose.

**Equality of symbolic expressions** must be established by simplifying the
difference to zero **and** by a high-precision numeric check at several sample
points — never by `==` on unevaluated expressions.

A negative or "cannot be determined from these sources" is a perfectly good
answer to any task here. Neither statement is one you are expected to confirm.

## Deliverables

In `sessions/2026-09-17/CT-S15-COLDREAD-DEFERRED/`: `REPORT.md`, `claims.jsonl`,
and any script with its output. Record the sha256 of each source you read and
each output you produce. Report the repository HEAD at the start and at the end;
make no commits, pushes, tags or PRs, and write nothing outside your session
folder.
