# Phase C — Literature verification (HALTED at gate C.0)

**Gate verdict:** `HALT_Q20_LITERATURE_MISSING`

## C.0 — Operator local-library gate

The Q20 prompt §2 Phase C requires Wasow 1965 §X.3, Adams
1928, Birkhoff 1930, and Birkhoff–Trjitzinsky 1933 to be in
the operator's local library at the start of Phase C, in a
form that allows opening cited sections and verifying
theorems hold uniformly in `d`.

**Status check (workspace + recent SIARC repo memory):**

| Source                              | Available to relay agent? | Notes |
|-------------------------------------|----------------------------|-------|
| Wasow 1965 (Asymp. Exp. for ODEs)   | **NO** — paraphrased only  | T1-BIRKHOFF-TRJITZINSKY-LITREVIEW (2026-05-02) handoff Q3: "agent could not pin from secondary sources alone whether SIARC's A matches Wasow 1965's σ or Adams 1928's 2σ"; Wasow §X.2–§X.3 explicitly named as `RECOMMENDED_NEXT_PHASE_T1` operator-acquisition target |
| Adams 1928 (Trans. AMS 30)          | **NO** — paraphrased only  | Same handoff §"Adams 1928": "Needed: the explicit second-order normal form" — implies primary text not consulted |
| Birkhoff 1930 (Formal theory…)      | **NO** — paraphrased only  | Same handoff: only secondary-source paraphrase available |
| Birkhoff–Trjitzinsky 1933 (Acta Math 60) | **NO** — paraphrased only | Same handoff §"recommended_next_phase_t1.md" line 18: "Birkhoff & Trjitzinsky, Acta Math 60 (1933), 1–89 — directly" listed as PHASE-2 acquisition target, not as available source |

**Conclusion:** all four primary sources are flagged in
T1-BIRKHOFF-TRJITZINSKY-LITREVIEW (2026-05-02) as needed-but-
not-yet-acquired.  The operator has paraphrased / secondary-
source readings of all four, but NO primary-source access at
the time this Phase C begins.

**Per Q20 prompt §4:** halt with `HALT_Q20_LITERATURE_MISSING`,
produce partial output (Phases A + B only), skip Phases C, D,
E in original form, output verdict
`UPGRADE_PARTIAL_PENDING_LITERATURE` with explicit "Phase C
deferred to literature acquisition" note.

## What the relay agent did NOT do (and why)

- C.1: did NOT open Wasow §X.3 / Adams 1928 §3 / B–T 1933
  §§4–6 to verify that the cited results hold at general
  `d ≥ 2` and not just at `d = 2`/`d ≤ 4`.  Reason: primary
  sources not in operator's library.
- C.2: did NOT compute the d-range intersection across
  M-tagged citations (L3, L8, L6-implicit from
  `phase_b_proof_diff.md`).  Reason: see C.1.
- The agent did NOT "read once and paraphrase from
  Wikipedia / Wimp 1984 / Loday-Richaud" to fabricate a
  Phase C verdict.  This was an explicit choice:
  paraphrased readings cannot discharge a proof-grade
  uniformity question, and a fabricated `C_LITERATURE_UNIFORM`
  verdict would violate AEAL hygiene (the resulting claim
  would not be reproducible by a future relay agent without
  the same secondary sources).

## What can be said about Phase C in the partial setting

The structural picture from T1-BIRKHOFF-TRJITZINSKY-LITREVIEW
(secondary-source paraphrase) is:

1. **Newton-polygon machinery (Wasow §X.3 + B–T 1933):**
   Newton-polygon edges of an irregular linear ODE at a
   point determine the leading exponential factors of the
   formal solutions there, with no upper bound on the slope
   denominator.  In the difference-equation parallel of
   B–T 1933 §§4–6, characteristic polynomials at slope edges
   determine leading exponential rates of the formal pair.
   Both are believed to extend uniformly in d, but the
   primary-source statement of the d-range has not been
   verified in this session.
   **Working hypothesis:** uniform in d (the Wasow reading).
   **Risk:** the Adams-vs-Wasow normalization ambiguity
   (T1 handoff Q3) could change the d-range from "all
   d ≥ 2" to "d ≥ d_0" for some d_0 > 2.  This is what the
   primary-source check is for.

2. **Borel summability of the slope-1/d trans-series at
   level 1 in `u = z^{1/d}`:** standard once Wasow §X.3
   gives Gevrey-d in z = Gevrey-1 in u; cited via Loday-
   Richaud–Marin "Divergent Series" textbook (paraphrased).
   Believed uniform in d.

3. **Indicial polynomial / ρ_d:** open at d ≥ 3 even at the
   structural level (see D2-NOTE v1 §3 last paragraph).
   This is independent of the literature gate; even if all
   four primary sources were available, the explicit ρ_d
   formula has not been computed.

The phase C summary at this partial level:

> If the four primary sources confirm the uniform-in-d
> reading of Wasow §X.3 + B–T 1933 (Working hypothesis 1),
> and if the standard Borel-summability theorem is
> uniform in d (Working hypothesis 2), then the Q20
> upgrade verdict UPGRADES from `UPGRADE_PARTIAL_PENDING_
> LITERATURE` to `UPGRADE_FULL` for the **ξ_0 only**
> scope (i.e., Conj 3.3.A* alone, not Prop 3.3.A in full).

This is the conditional that the operator-side literature
acquisition (T1 PHASE 2 in the T1 handoff §"recommended_
next_phase_t1.md") would discharge.

## Phase C verdict

`HALT_Q20_LITERATURE_MISSING` — partial output written;
Phase D will aggregate to `UPGRADE_PARTIAL_PENDING_LITERATURE`;
Phase E (D2-NOTE v2 draft) is **not** produced this session.
