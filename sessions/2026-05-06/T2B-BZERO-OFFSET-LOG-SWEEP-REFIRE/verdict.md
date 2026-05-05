# Verdict — T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE (044R)

**Outcome tag:** **`OUTCOME_B_AT_H7`**
**Date:** 2026-05-06 (UTC) / 2026-05-06 JST
**h-bound:** $h \le 10^7$ (PSLQ_HMAX_TRANS reduced from $10^9$ in 044)
**Anchor commit:** 042a1318 (044 halt, sessions/2026-05-08/T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10/)
**Wall:** 5,213.5 s (~1 h 27 min) — well under the 2.5-hr wall guard.
**Stage B/C:** 241,892 / 241,892 PSLQ classifications complete (100%)
**Stage D:** 2 / 2 deep-verifications complete (100%)
**Budget exceeded:** **False**

---

## Verdict statement (with required AT_H7 qualifier)

The 044R re-fire detected **exactly one off-orbit $n/\log 2$ hit at
$h \le 10^7$** in the b₁ ∈ {5, 8, 9, 10} corridor, satisfying the
relay 044R `OUTCOME_B_AT_H7` definition (1 off-orbit outlier with a
clean PSLQ relation at $h \le 10^7$).

> **Epistemic qualifier:** absence of additional outliers at
> $h \le 10^7$ is bounded evidence, **not** proof of absence at higher
> $h$. The verdict tag `OUTCOME_B_AT_H7` carries the `AT_H7` suffix
> per the relay 044R prompt; bare `OUTCOME_B` is forbidden by the
> harness self-check (key `VERDICT_OMITS_H_BOUND_QUALIFIER`).

---

## The single off-orbit outlier (b₁ = 10)

| Field | Value |
| --- | --- |
| **Coefficients** $(a_2, a_1, a_0, b_1, b_0)$ | $(-9, 0, 0, 10, 5)$ |
| **Ratio** $a_2 / b_1^2$ | $-9/100$ |
| **Stage A** $K_{500}$ float | $4.328085122666885$ |
| **Stage B/C** PSLQ ($N{=}600$, dps$=150$, $h_\max{=}10^7$) | $-3 + L \cdot \log 2 = 0$, residual $= 0$ |
| **Stage D** deep-verify ($N{=}1500$, dps$=300$, $h_\max{=}10^7$) | $-3 + L \cdot \log 2 = 0$, residual $= 0$, residual $< 10^{-200}$: **True** |
| **Extracted** $n$ | $\mathbf{n = 3}$ (so $L = 3/\log 2$) |
| **30-dps numeric** $L$ | $4.32808512266689022207977404301$ |
| **60-dps numeric** $L$ | $4.32808512266689022207977404300567641227993786245895780240635$ |
| **Bauer-orbit membership** | **off-orbit**: $a_2 = -k^2$ for $k = 3$, but $\lvert b_1 \rvert = 10 \ne 6k = 18$ |
| **Discriminant identity class** | `neither` (not on $9 a_2 + 2 b_1^2 = 0$ trans-stratum-proper, not on $4 a_2 - b_1^2 = 0$ Brouncker boundary) |

**Closed-form:** $L = 3 / \log 2 \approx 4.328085122666890\ldots$

This means at $h \le 10^7$ the off-orbit $n/\log 2$ family in
b₁ ∈ {5, 6, 7, 8, 9, 10} now contains **two** data points:

| b₁ | Coefficients | Ratio $a_2/b_1^2$ | $n/\log 2$ |
| --- | --- | --- | --- |
| 7 | $(8, -4, 0, 7, 4)$ | $8/49$ | $3/\log 2$ (v3.1 b₇ singular outlier; ratio with general $(a_1, a_0)$ shape) |
| **10** | $\mathbf{(-9, 0, 0, 10, 5)}$ | $\mathbf{-9/100}$ | $\mathbf{3/\log 2}$ (**044R discovery**; Bauer-shape numerator $a_2 = -k^2$, $a_1 = a_0 = 0$ but $b_1 \ne \pm 6k$) |

**Note (anomaly worth flagging to the Synthesizer):** both off-orbit
points produce the **same** value $3/\log 2$, despite radically
different numerator shapes. The 044R discovery has the Bauer
numerator shape $(a_2, a_1, a_0) = (-k^2, 0, 0)$ at $k = 3$ but
mismatched denominator $(b_1, b_0) = (10, 5)$ instead of the
on-orbit $(\pm 18, \pm 9)$. The b₇ singular has a generic numerator
$(8, -4, 0)$ and matching $(b_1, b_0) = (7, 4)$. Both yield
$n = 3$. This 2-point coincidence is the candidate-4th-law signal
that 044R was designed to surface.

---

## Other notable Stage B/C hits (not off-orbit)

One Trans hit at b₁ = 8 with discriminant identity class
`brouncker_boundary` (i.e. $4 a_2 - b_1^2 = 0$): 

| Field | Value |
| --- | --- |
| Coefficients | $(16, 0, 0, 8, 4)$ |
| Ratio | $1/4$ (Brouncker locus) |
| $n$ extracted | None (relation does not match $n / \log 2$ form) |
| Bauer-orbit | off-orbit (expected; $a_2 = 16 > 0$ violates $a_2 = -k^2$) |

This is consistent with the 1739 Brouncker-stratum result and is
**not** a $n/\log 2$ outlier. It is recorded for completeness.

---

## Stage B/C cell tallies at $h \le 10^7$

| b₁ | Enumerated | Convergent | Log | Trans | $n/\log 2$ on-orbit | $n/\log 2$ off-orbit |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 79,860 | 43,580 | 0 | 0 | 0 | 0 |
| 8 | 79,860 | 59,976 | 0 | 1 (Brouncker) | 0 | 0 |
| 9 | 79,860 | 66,475 | 0 | 0 | 0 | 0 |
| **10** | **79,860** | **71,861** | **1** | **0** | **0** | **1** |
| **Total** | **319,440** | **241,892** | **1** | **1** | **0** | **1** |

Total off-orbit $n/\log 2$ hits at $h \le 10^7$: **1**.

---

## Downstream routing (044R prompt §"DOWNSTREAM ROUTING")

`OUTCOME_B_AT_H7` triggers:

1. **044B contingency unblocks** — single-outlier tightened sweep
   centred on $(-9, 0, 0, 10, 5)$, b₁ = 10, ratio $-9/100$.
   Recommended next action: queue 044B prompt to the Synthesizer
   for arbitration of whether the new b₁ = 10 outlier joins the
   b₇ outlier in a structural family (both produce $3/\log 2$).
2. **047 / 048 schedule rolls per 044=B branch** (W19 closing fire
   plan).
3. **v3.1 absolute-claim wording** in T2B preprint may need a
   softening from "b₁ = 7 is the only off-orbit $n/\log 2$ data
   point" to "b₁ = 7 was the only off-orbit $n/\log 2$ data point
   known in v3.1; the 044R re-fire (h ≤ $10^7$) added a second at
   b₁ = 10, $(-9, 0, 0, 10, 5)$ → $3/\log 2$." Queue a Synthesizer
   task to verify wording compatibility with the T2B preprint
   submission status.
4. **`OUTCOME_C_AT_H7` did NOT trigger** — only one off-orbit hit,
   not ≥ 2, so the 044C E2 escalation cascade (047/048/049/050
   HALT) is **not** activated.

---

## Forbidden / not asserted

- This verdict does **not** claim "the off-orbit family contains
  exactly two points." It claims "exactly two off-orbit $n/\log 2$
  data points are now known at $h \le 10^7$ in the b₁ ∈ {5..10}
  corridor."
- This verdict does **not** claim "v3.1 stratification is refuted."
  v3.1 is a stratification of behaviour at finite-but-unspecified
  $h$; the 044R result tightens the b₇-singular claim into a
  b₇-singular plus b₁₀-discovery 2-point family **at $h \le 10^7$**.
- This verdict does **not** claim absence of further outliers at
  $h > 10^7$ in this same corridor; that question is open and would
  require a 044R2 re-fire at $h = 10^8$ or higher.

---

## AEAL provenance

- Refire script SHA-256:
  `99d2ce7ab28e16b70f298102e4f3be3bdd598e96b9b4c10c94b6ccfa28c18596`
- Source 044 sweep SHA-256:
  `718ea0e66bddeb401e36f6cb2687058c1a779ea6089b744d15548fe91539929d`
- Stage A cache SHA-256 (carried bit-for-bit from 044 / 042a1318):
  `dc081ca68f67296b29d56141da4add7c30f878fad5b813cece26f425e5f0a527`
- Stage A summary SHA-256:
  `89a694bc89cc6690438177fa6f09fde685c240c106997fd3e9070ed101aa9f53`
- 044 claims.jsonl SHA-256 (anchor):
  `94be8efb09edf472f7a48d4fdbc7386f35f342b7ac3df83b8fb9a920015ef7c9`
- 10 AEAL claims written to `claims.jsonl` (≥ 6 required by 044R).
