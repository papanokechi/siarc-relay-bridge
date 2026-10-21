# PREREG.md — CT-S4-FORMAL-TYPE (P5)

## 0. Ordering disclosure

The computation in `formal_type.py` is fully symbolic and deterministic: it has
no tunable parameter, no precision setting, and no threshold. Its "result" is a
pole order — an integer — at each singular point. The script was written and run
before this file was finalised. Because there is no threshold that *could* have
been retuned, the ordering has no bearing on the result; the disclosure is made
anyway because P0 requires pre-registration.

## 1. Hypothesis under test

> **H(P5).** The formal type at each singular point of the linear system
> underlying the `D5^(1)` (Painlevé V) attribution for V_quad is **unramified**,
> whereas the Channel Theory object (the ODE annihilating `f(z) = Σ Q_n z^n`)
> has a **ramified**, slope-1/2 irregular point at `z = 0`. If both hold, the
> two are formally distinct objects unless related by a ramified change of the
> independent variable.

## 2. Observable

For a rank-2 scalar equation put in normal form `u'' = r(z) u` (which removes
the first-order term and is therefore **gauge-invariant** under the residual
scalar gauge freedom), the observable at a point `z₀` is

    m := ord_{z₀}(pole of r) ∈ ℤ.

The classification used is fixed **in advance** and is standard:

| `m` | formal type | ramification index | Katz invariant |
|---|---|---|---|
| `m ≤ 2` | regular singular | 1 | 0 |
| `m = 2k` even, `k ≥ 2` | irregular, **unramified** | 1 | `k − 1` |
| `m = 2k+1` odd, `m ≥ 3` | irregular, **ramified** | 2 | `m/2 − 1` |

This is the only classification rule used, and it is not adjusted afterwards.
The exponential parts are `S' ≈ ±√r`, hence `S ≈ ±√(lead)·(z−z₀)^{1−m/2}/(1−m/2)`.

`m` is an integer, so the observable cannot be "nearly" anything: there is no
numerical tolerance anywhere in this session.

## 3. Falsifier

**F1.** The transcription of `L_φ` from the paper is falsified if either
(a) the stated factorisation `q₂ = 4(2√3−3)z²(z²+z+3)` fails to expand to the
listed `q₂`, or (b) the normal-form potential recomputed from `(q₀,q₁,q₂)` via
`r = ¼a² + ½a′ − b` fails to equal the paper's printed
`r = (11z⁴+4z²+4z+12)/(4z⁴(z²+z+3)²)`.
Either failure means I mis-transcribed or the paper is internally inconsistent;
**halt and report**, do not proceed to classify.

**F2.** The derivation of System A's operator is falsified if the residual of
`3z³f'' + 10z²f' + (z²+5z−1)f + 1` against the truncated series
`Σ_{n≤40} Q_n z^n` is nonzero at any order `z^0 … z^38` (exact arithmetic, not
approximate). **Halt and report.**

**F3.** H(P5) is falsified if System A's pole order at `z = 0` is even
(i.e. unramified), or if System B's is odd (ramified).

## 4. Vacuity pre-check

The observable must move when the object moves. Pre-declared checks:

* `m` differs between the two systems under test (3 vs 4) — if the procedure
  returned the same `m` for both, it would be measuring nothing. *This is the
  substantive vacuity check and it is decided by the run itself.*
* The classification distinguishes all four qualitative outcomes actually
  present in the data: regular singular (`m = 2`), unramified irregular
  (`m = 4`), ramified irregular (`m = 3`), and the behaviour at `∞`, which is
  computed separately via `z = 1/t` with the normal-form correction
  `r_∞(t) = r(1/t)/t⁴ − (3/4)/t²`.
* The exponential parts recovered from `r` must reproduce the values already
  recorded independently in the repository (`c = ±2/√3` in `u = √z` from
  `CC-PIPELINE-G2/g2_pade_borel.py`; `exp(±(1/√3)/z)` from the period-rep paper).
  If they did not, the pipeline would be miscalibrated.

## 5. Hard stop (mandated by the prompt itself)

P5 step 3 requires comparison against an Ohyama–Kawamuko–Sakai–Okamoto-type
classification table of rank-2 linear systems for the Painlevé equations, and
says: *"use only a source available in the repo or supplied by the operator. If
no such table is available, STOP after step 2 and request it. Do not reconstruct
the table from memory."*

`CT-S0-INVENTORY/REPORT.md` §3 item 7 already records that **no such table
exists in this repository**. Therefore:

* steps 1 and 2 are executed;
* **step 3 is NOT executed**;
* the step-4 verdict is given only to the extent it follows from steps 1–2
  without the table, and is labelled **STRUCTURAL**.

No Painlevé classification table is reproduced from memory anywhere in this
session.

## 6. Additional standing constraints

* **Do not revise Conjecture 4.1 (or any conjecture) in any file.** Report to
  the operator only.
* Do not modify files from earlier sessions; read only.
* If the object named by the `D5^(1)` attribution cannot be identified
  unambiguously, analyse **both** candidate systems, as P5 step 1 directs.
