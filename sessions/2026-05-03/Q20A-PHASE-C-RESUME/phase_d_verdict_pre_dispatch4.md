# Phase D — Final Verdict (Dispatch 3)

**Dispatch 3 timestamp:** 2026-05-03 (re-fire 3)
**Final verdict:** `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`
(prior dispatch 2 verdict archived at
`phase_d_verdict_pre_refire2.md`; dispatch 1 at
`phase_d_verdict_pre_refire.md`).

## Aggregation

| Phase | Result                          | Verdict signal                            |
|-------|---------------------------------|-------------------------------------------|
| A*    | PASS, cached, SHA-verified      | `A_DIRECT_IDENTITY_d10` (dispatches 1/2)  |
| C.0   | PASS (hash match, judgment on path) | `C0_GATE_PASS`                        |
| C.1   | HALT (image-only PDF)           | `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`          |
| C.2   | PARTIAL — (i) uniform, (ii) NIA | `C_BIRKHOFF_UNIFORM_FORMAL_ONLY`          |
| C.3   | BLOCKED (Wasow + Borel half)    | `C_LITERATURE_BLOCKED_AT_C1`              |
| E     | SKIPPED (gated on D)            | —                                         |

## Final verdict logic

Per Prompt 018 §2 step 7:
- `UPGRADE_FULL` requires `C_LITERATURE_UNIFORM`. Not achieved.
- `UPGRADE_PARTIAL_d_LE_d*` requires a finite d_W* / d_B* cap
  established. No finite cap is established (Wasow blocked;
  Birkhoff is uniform on the formal half).
- `UPGRADE_REJECTED` requires a literature-level disagreement
  with a Q20A claim. No disagreement; only an extraction gap.
- `HALT_Q20A_LITERATURE_DISAGREES_WITH_012` — no disagreement.
- `HALT_Q20A_REGRESSION_AT_PHASE_A` — Phase A* SHAs match
  exactly; no regression.

None of the §2 step 7 verdicts fit cleanly. The honest verdict
is a new halt code: `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`. The
verdict ladder of Prompt 018 §3 also does not list this
specifically; the closest is `HALT_Q20A_LITERATURE_NOT_LANDED`,
which is technically wrong because the literature **is**
landed (PDFs on disk, hashes verified) — the issue is purely
that the Wasow PDF carries no machine-readable text.

## Differences vs. dispatches 1/2

| Item                    | Dispatch 1                       | Dispatch 2                          | Dispatch 3                                    |
|-------------------------|----------------------------------|-------------------------------------|-----------------------------------------------|
| PDFs on disk            | No                               | No                                  | **Yes** (under runbook canonical path)        |
| SHA256SUMS.txt          | No                               | No                                  | **Yes** (operator runbook step ran)           |
| Phase C.0 result        | HALT (no files)                  | HALT (no files)                     | **PASS** (hash match)                         |
| Phase C.1 (Wasow)       | Skipped                          | Skipped                             | **HALT** (image-only PDF)                     |
| Phase C.2 (Birkhoff)    | Skipped                          | Skipped                             | **PARTIAL** — (i) uniform; (ii) NIA           |
| Verdict                 | UPGRADE_DEFERRED_PENDING_LIT_LDG | HALT_Q20A_LITERATURE_NOT_LANDED     | **HALT_Q20A_WASOW_PDF_IMAGE_ONLY**            |

Dispatch 3 strictly **strengthens** the prior dispatches:
Birkhoff §2 formal-series existence theorem is now extracted
and recorded as uniform-in-d AEAL evidence. Downstream
consumers gain the formal half regardless of whether Phase
C.1 ever closes.

## Downstream impact

- **PCF-2 v1.3 §3.3.A* (`xi_0(d) = d / β_d^{1/d}`):** the
  formal-series-existence half is now theorem-grade citable
  to Birkhoff 1930 §2 (uniform in d ≥ 1). The analytic / Borel
  identification half remains conjectural pending B–T 1933
  acquisition or Wasow §X.3 in readable form.

- **CT v1.4 §3.3 / D2-NOTE v1:** unchanged. No v2 D2-NOTE is
  drafted in this dispatch (Phase E gated on UPGRADE_*).

- **G1, G2:** unchanged. Q20a remains **OPEN** as a full
  upgrade target; one half is theorem-grade citable, the
  other half awaits readable Wasow §X.3 or B–T 1933.

- **M2 (proof of `xi_0(d) = d / β_d^{1/d}` as theorem):**
  upgraded from `PARTIAL` to **`PARTIAL_FORMAL_HALF_THEOREM`**
  — a finer status than dispatches 1/2 supported. M2 is not
  yet DONE.

- **M9 gating set:** unchanged. Still `{M2, M4, M6}` — M2 is
  not closed; the partial closure of its formal half does not
  remove the gating dependence per Prompt 018 §3.

## Phase E — D2-NOTE v2

**Skipped.** Phase E is gated on `UPGRADE_FULL` or
`UPGRADE_PARTIAL_d_LE_d*` per Prompt 018 §2 step 8. Neither
condition holds.

## Resumption checklist for dispatch 4

1. Operator re-acquires Wasow §X.3 in machine-readable form,
   or transcribes theorems X.3.1, X.3.2, X.3.3 (and any
   Borel-singularity content if it lives in chap X) into a
   text file under
   `tex/submitted/control center/literature/g3b_2026-05-03/`.
2. SHA256SUMS.txt updated.
3. Re-fire Q20A-PHASE-C-RESUME (dispatch 4). Phase A* cache
   re-validates in seconds; Phase C.0 hash check re-validates
   in seconds; Phase C.1 picks up from this halt; Phase C.2
   (ii) and Phase C.3 / D / E execute fresh.

Alternative: synthesizer drafts a separate
`Q20A-LIT-INDEPENDENT-PARTIAL-LANDING` prompt that lands
- `A_DIRECT_IDENTITY_d10` (uniform-in-d-2..10 sanity range), and
- Birkhoff 1930 §§2-3 formal-series existence theorem
  (uniform in d ≥ 1) for the `xi_0(d)` formal-direction claim,
into CT v1.5 / a D2-NOTE v1.5 as an extended-conjecture-with-
formal-half-theorem-grade landmark, independent of Wasow §X.3.
