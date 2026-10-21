# CT-S26-UPPER-BOUND — ADDENDUM 1

**Written after arm V1 fired, before the corrected run. `PREREG.md` is left
unedited: the arm fired, and the evidence that it fired is the point.**

---

## 1. What happened

`PREREG.md` §5 registered the known-answer control V1 as:

> `y_n = (-1)^n I_n(2)` satisfies `y_n = n y_{n-1} + y_{n-2}` exactly, because
> the modified Bessel functions obey `I_{ν-1}(2) - I_{ν+1}(2) = ν I_ν(2)`.

The first run reported **0.30103 digits of agreement at `n = 2`** — that is, no
agreement at all — and **F2 fired**, halting the session with `VERDICT: FAIL`.
The artefact is `outputs/upper_bound.out.txt`, retained unchanged.

## 2. The defect is in the control, not in the engine

Substituting `y_n = (-1)^n I_n(2)` into `y_n = n y_{n-1} + y_{n-2}` and
dividing by `(-1)^n` gives

```
I_n = -n I_{n-1} + I_{n-2} ,   i.e.   I_{n-2} - I_n = n I_{n-1} .
```

The Bessel identity `I_{ν-1}(2) - I_{ν+1}(2) = ν I_ν(2)` at `ν = n-1` gives

```
I_{n-2} - I_n = (n-1) I_{n-1} .
```

The two differ by `n` against `n-1`. **The closed form registered in the PREREG
was wrong by an index shift.** The recurrence engine was never implicated; the
0.30103 digits is `-log10(1/2)`, the size of exactly that one-unit discrepancy
at `n = 2`, not the signature of a broken iteration.

## 3. The correction, derived here

Take the identity at `ν = n`:

```
I_{n-1}(2) - I_{n+1}(2) = n I_n(2) .
```

Put `y_n := (-1)^n I_{n+1}(2)`. Then

```
n y_{n-1} + y_{n-2} = n(-1)^{n-1} I_n + (-1)^n I_{n-1}
                    = (-1)^n ( I_{n-1} - n I_n )
                    = (-1)^n I_{n+1}
                    = y_n .
```

So the correct known-answer solution is **`y_n = (-1)^n I_{n+1}(2)`**, and V1
is re-run against it. The **threshold is unchanged at 40 digits**, as are every
other threshold and every other arm. Nothing was adjusted to fit a result: the
only change is the closed form the control compares against, which was
misderived when the PREREG was written.

## 4. Why this is recorded rather than quietly fixed

Three reasons, in increasing order of weight.

1. It is a **firing of a registered falsifier**, and the corpus rule is that a
   falsifier that fires is reported, not edited away.
2. It is the **third time in this run** that a closed form or citation of mine
   needed narrowing or correcting at the point of contact with the source
   (`S24-12`, `S24-13`, and now this). The pattern is the same each time:
   something derived once, remembered in compressed form, and reproduced from
   the compressed memory rather than from the source. That is precisely the
   provenance defect this whole session exists to remove for the upper bound —
   and it recurred inside the session written to remove it.
3. Most usefully: **the arm did its job.** V1 exists to catch a wrong
   recurrence. It instead caught a wrong control, which is the harder case,
   because a wrong control that happens to *agree* would have certified a
   broken engine. The arm is worth keeping for exactly that reason.

## 5. Artefact discipline (P0 Amendment B)

`outputs/upper_bound.out.txt` (the FAIL run) is **retained unchanged** and is
cited by the claim recording this addendum. The corrected run writes to a
**new** path, `outputs/upper_bound_rev2.out.txt`. No hash is taken until its
output is final.
