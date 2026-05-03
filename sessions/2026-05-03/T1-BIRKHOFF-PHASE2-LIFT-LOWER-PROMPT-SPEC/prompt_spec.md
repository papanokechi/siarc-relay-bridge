# T1-BIRKHOFF-PHASE2-LIFT-LOWER — Synthesizer-Drafted Prompt Spec

**Session:** `T1-BIRKHOFF-PHASE2-LIFT-LOWER-PROMPT-SPEC`
**Date deposited:** 2026-05-04 (JST)
**Source:** Synthesizer chat 2026-05-03 (timestamp recorded in operator-side
  relay paste 2026-05-04T06:53:26.787+09:00 — see picture v1.15 §10
  trail bbc905d → 62c917d)
**Purpose:** AEAL-anchor the synthesizer-drafted Phase 2 prompt spec at
  deposit time per the QS-2 / QS-3 pattern (parallel to the execution
  session at `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/`).

> **Chronology note (AEAL-honest):** This spec deposit is **post-hoc**.
> The relay agent fired the spec **before** this deposit landed
> (execution session opened 2026-05-03 ~ JST and produced verdict
> `UPGRADE_PARTIAL_FORMAL_LEVEL` 2026-05-04 ~07:25 JST; bridge commit
> `37c939f`). This deposit anchors the spec text as fired, retrieved
> verbatim from the operator-side relay paste; it does not back-date
> the deposit. See execution session
> `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/prompt_spec_used.md`
> for the matching Phase 0.0 provenance file written inside the
> execution session.

---

## Verbatim spec body (as fired)

```
TASK: T1-BIRKHOFF-PHASE2-LIFT-LOWER
TASK CLASS: relay agent invocation (AEAL-compliant)
PARALLEL-SAFE WITH: any task NOT touching M4 closure path
COMPUTE: medium-high (~3-5 hr agent runtime; literature reading
         + symbolic derivation + verdict drafting)

═══════════════════════════════════════════════════════════════
§0 CONTEXT
═══════════════════════════════════════════════════════════════

SIARC program critical path: SIARC-MASTER-V0 announcement (M9)
gates on {M4 = Conjecture B4 at d ≥ 3 proof-grade,
M6 = canonical-form Stokes constant at 30+ digits}.

Post-v1.15 picture state (2026-05-03):
  - M2 ✅ FULLY DONE (D2-NOTE v2.1 UPGRADE_FULL; Theorem 4.1
    proof-grade at all d ≥ 2 via Wasow §19 + B-T 1933 §§4-6 +
    Phase A symbolic derivation; G1 ✅ no residual)
  - M9 gating reduces unconditionally to {M4, M6}
  - M4 status: EMPIRICAL d=3,4 + LITERATURE BRACKET A in [d, 2d]
    holds at d ≥ 3 (T1 Phase 1 / 003); A01 verdict 2026-05-03
    confirmed Wasow / Birkhoff / B-T / Adams sigma share mu-units
    (no factor-of-2 ambiguity at normalisation level)
  - H1 label: PHASE_2_GATED (synthesizer ruling 2026-05-03;
    held pending this Phase 2 verdict)

This task is **Phase 2 of T1**: lift the lower bound A = d
established by Phase 1 literature anchoring, to the upper
bound A = 2d via non-resonance / non-degeneracy of the
Birkhoff-Trjitzinsky reduction at irregular singularities of
fractional rank q.

If Phase 2 lands UPGRADE_FULL: M4 ✅; M9 gating reduces from
{M4, M6} to {M6 only}; H1 graduates from PHASE_2_GATED to
PROVEN at all d ≥ 3.

If Phase 2 lands UPGRADE_PARTIAL_d_LE_d*: M4 partial; H1
becomes PROVEN at d ≤ d*, empirical at d > d*.

If Phase 2 HALTS: surfaces a structural gap requiring
additional literature; M4 stays empirical+bracket; H1 retains
PHASE_2_GATED label.

═══════════════════════════════════════════════════════════════
§1 ANCHOR FILES (preconditions; verify all present)
═══════════════════════════════════════════════════════════════

LITERATURE PDFs (under literature/g3b_2026-05-03/; verify
hashes against SHA256SUMS.txt):

  1. Birkhoff 1930 (Acta Math 54): formal-series existence at
     irregular singular points, §§2-3 (uniqueness)
     PDF: 01_birkhoff_1930_acta54.pdf
     SHA prefix: aeb5291e...
     Alias: birkhoff_1930.pdf

  2. Birkhoff-Trjitzinsky 1933 (Acta Math 60): Borel-summability
     machinery, §§4-6 (structurally novel relative to 1930
     paper); §§7-9 (rank-q non-resonance / non-degeneracy
     conditions for the specific reduction Phase 2 targets)
     PDF: 03_birkhoff_trjitzinsky_1933_acta60.pdf
     SHA prefix: dcd7e3c6...
     Alias: birkhoff_trjitzinsky_1933.pdf

  3. Wasow 1965: asymptotic existence theorem at irregular
     singular points, §X.3 + §19 (Theorem 19.1, eq. 19.3,
     §19.3 ramification)
     PDF: 04_wasow_1965_dover.pdf
     SHA prefix: e84b3e48... (or f59d6835... per re-capture
     — operator confirms current SHA)
     Alias: wasow_1965_chap_X.pdf

  4. Adams 1928: NOT IN ANCHOR; transitive evidence via
     Birkhoff/B-T sufficient per A-01 verdict. If Phase 2
     surfaces a specific dependency on Adams's original
     argument, halt with HALT_T1P2_ADAMS_GAP and surface
     to operator for acquisition decision.

PHASE 1 DELIVERABLES (under
sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/):

  5. T1 Phase-1 dossier:
     - descendants_synthesis_matrix.md (AMENDED 2026-05-03 per
       A-01 verdict; bridge commit bbc905d)
     - gap_proposition_for_d_ge_3.md (AMENDED 2026-05-03 per
       A-01 verdict; bridge commit bbc905d)
     - Establishes lower bound A ≥ d via literature bracket;
       upper bound A ≤ 2d is THIS task's job

  6. A-01 verdict handoff:
     sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/handoff.md
     - Confirms Wasow / Birkhoff / B-T / Adams sigma share
       mu-units (no factor-of-2 ambiguity)
     - Two residuals (non-blocking):
       (i) bracket-derivation upper bound mu ≤ 2d from Wasow
           §X.3 itself remains paraphrase-grade (DISC-1, DISC-2)
       (ii) Adams 1928 NIA on disk

PCF-1 v1.3 + PCF-2 v1.3 + CT v1.3 (concept DOIs in v1.15
picture §10):
  Reference for prior empirical verifications and the d=2
  proof; not consumed in Phase 2 reading but cited in any
  produced verdict.

D2-NOTE v2.1 (PDF SHA a8b6026a...; published Zenodo deposit
2026-05-03 if O2 fired): citable artifact for Theorem 4.1
upon which the Phase 2 argument layers. Phase 2 cites D2-NOTE
v2.1 as the universality-radius-of-Borel-singularity result
the Phase 2 lift extends to A = 2d.

═══════════════════════════════════════════════════════════════
§2 PHASES
═══════════════════════════════════════════════════════════════

PHASE 0.0 — provenance write-out (mandatory pre-step)
  Write the relay-prompt body to:
    sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/prompt_spec_used.md
  This anchors the exact spec the relay agent saw at fire time
  for AEAL provenance.

PHASE 0.5 — bibkey collision preflight
  Verify that any new bibliography entries Phase 2 introduces
  don't collide with existing entries in the project's
  bibliography files. If collision detected, halt with
  HALT_T1P2_BIBKEY_COLLISION.

PHASE A — symbolic derivation of indicial polynomial in
          Birkhoff-Trjitzinsky reduction
  Goal: derive the indicial polynomial chi_d(c) for the
  rank-q irregular singularity at z=0 of the operator L_d
  (homogeneous part of equation (1) in PCF-1 v1.3 §6).

  Method:
    A.1 — Set up the formal solution f(z) = z^c sum_{n>=0}
          a_n z^{-n} per Birkhoff 1930 §2 Theorem I (using
          mu-units consistent with A-01 verdict)
    A.2 — Apply L_d to this ansatz; collect the leading-order
          terms in z^c
    A.3 — Derive chi_d(c); compute its degree in c
    A.4 — Identify the indicial exponents (roots of chi_d)
    A.5 — Verify against the d=2 proof in PCF-1 v1.3 §6
          Theorem 5 (which sets A=2 at d=2)
    A.6 — At d=3: extract chi_3(c); verify roots match the
          empirical d=3 verification in PCF-2 v1.3 / Q1
    A.7 — At d=4: same for chi_4(c)

  Verdict signal: A_INDICIAL_VERIFIED_AT_d_le_4 (if A.5+A.6+A.7
  all pass) or A_INDICIAL_DRIFT_AT_d* (if any d ∈ {2,3,4}
  shows mismatch). The latter is HALT_T1P2_INDICIAL_DRIFT.

  Output: phase_a_symbolic_derivation.py + phase_a_summary.md

PHASE B — extended Phase A* sweep at d ∈ {3, 4, ..., d_max}
  Default d_max = 8 (extends Q20a's d ≤ 10 sweep to the
  Phase 2 specific question — non-resonance verification).
  At each d, verify:
    B.1 — chi_d(c) computed symbolically
    B.2 — Indicial exponents extracted (degree ≤ deg(chi_d))
    B.3 — Non-resonance condition: indicial exponents differ
          modulo Z (no two integers in their differences)
    B.4 — Non-degeneracy condition: leading coefficient of
          chi_d nonzero

  This sweep is the Phase 2-specific addition; Q20a's sweep
  established the constant value, while this sweep verifies
  the structural non-resonance / non-degeneracy.

  Verdict signal: B_NONRESONANCE_VERIFIED_AT_d_le_d_max (all
  d in [3, d_max] pass non-resonance + non-degeneracy);
  B_NONRESONANCE_FAILS_AT_d* (specific d* fails); the latter
  is a verdict-level finding, not a halt — Phase 2 should
  understand whether this is a generic algebraic failure or
  a numerical artefact.

  Output: phase_b_extended_sweep.py + phase_b_summary.md

PHASE C — literature anchoring (B-T 1933 §§7-9 reading)
  Goal: anchor the Phase 2 argument in B-T 1933's specific
  treatment of the rank-q non-resonance condition.

  C.0 gate — verify B-T 1933 PDF on disk + SHA256SUMS.txt
              entry; halt with HALT_T1P2_BT_NOT_LANDED if
              missing.

  C.1 — Read B-T 1933 §§7-9 in full. Extract:
    (i) The specific non-resonance condition required for
        the Borel-summability extension to upper-bound A = 2d
    (ii) The specific non-degeneracy condition (typically
         ensures the leading coefficient is non-zero)
    (iii) The verdict's stated d-range / q-range applicability
    (iv) Any condition on the mu-units that affects the
         conclusion (per A-01 verdict, this should be empty;
         verify)

  Each extraction records: theorem/proposition number, verbatim
  statement (≤30 words per quote per hygiene), stated
  applicability range.

  C.2 sub-gates (verification of conditions Phase A+B
                 produced match B-T's stated conditions):
    C.2.1 — Phase A's non-resonance from chi_d ↔ B-T's
            stated non-resonance: structural match? halt with
            HALT_T1P2_NONRESONANCE_MISMATCH otherwise
    C.2.2 — Phase A's non-degeneracy ↔ B-T's stated
            non-degeneracy: structural match? halt with
            HALT_T1P2_NONDEGENERACY_MISMATCH otherwise
    C.2.3 — d-range applicability: B-T's stated range covers
            d ∈ [3, d_max]?
    C.2.4 — mu-units: A-01 verdict consistency confirmed?

  Verdict signal: C_LITERATURE_UNIFORM (all four checks pass
  + d-range covers d ∈ [3, d_max]); C_LITERATURE_BOUNDED_AT_d*
  (range capped at d* < d_max); C_LITERATURE_DISAGREES_WITH_AB
  (Phase A+B produced something B-T doesn't support — surface
  for synthesizer review).

  Output: phase_c_literature_verification.md

PHASE D — verdict aggregation
  Combine Phase A + B + C signals:
    D.1 — If A_VERIFIED + B_VERIFIED at d ∈ [3, d_max] +
          C_LITERATURE_UNIFORM → UPGRADE_FULL
    D.2 — If partial (e.g., B fails at d* > 3) →
          UPGRADE_PARTIAL_d_LE_d*-1
    D.3 — If A halts → HALT_T1P2_INDICIAL_DRIFT
    D.4 — If B halts → HALT_T1P2_NONRESONANCE_FAILS_GENERIC
    D.5 — If C halts → HALT_T1P2_LITERATURE_NOT_LANDED or
          HALT_T1P2_LITERATURE_DISAGREES_WITH_012
    D.6 — If all pass but d-range bounded → UPGRADE_PARTIAL

  Output: phase_d_verdict.md

PHASE E — D2-NOTE v2.1-style upgrade artifact (optional)
  Conditional on UPGRADE_FULL or UPGRADE_PARTIAL with d-range
  ≥ 4, draft a citable upgrade note (T2-NOTE v1.0 / B4-NOTE
  v1.0) that:
    E.1 — States the proven Conjecture B4 at d ∈ [d_min,
          d_max] (full or partial range)
    E.2 — Cites Phase A symbolic derivation, Phase B sweep,
          Phase C literature anchoring (B-T 1933 §§7-9)
    E.3 — Cites D2-NOTE v2.1 as the universality-radius
          result this lift extends
    E.4 — Includes A-01 verdict provenance for mu-units
          consistency

  Build clean with pdflatex passes 1, 2, 3 if drafted.

  Output: t2_note_or_b4_note_v1.tex + .pdf (if drafted)

  Note: a v1 draft can be 5-7 pp; full ~10-15 pp expansion is
  separate task post-deposit.

PHASE F — handoff + AEAL claims
  Write handoff.md (full session report):
    - Verdict (Phase D output)
    - Phase A + B + C summary tables
    - Anomalies noted
    - SHA-256 of all build artifacts
    - Bridge commit hash
    - Next-task recommendations

  Append AEAL claims to claims.jsonl (do NOT overwrite):
    - Phase A indicial polynomial verifications (≥3 entries)
    - Phase B non-resonance + non-degeneracy at d ∈ [3, d_max]
      (≥6 entries)
    - Phase C literature reads (≥3 entries)
    - Phase D verdict (≥1 entry)
    - Phase E build artifact provenance (≥1 entry if E ran)

  Total: ≥ 14 entries.

  git commit + push.

═══════════════════════════════════════════════════════════════
§3 AEAL CLAIMS MINIMUM
═══════════════════════════════════════════════════════════════

Recommend ≥ 14 claims.jsonl entries:
  - 3 Phase A entries (chi_d at d ∈ {2,3,4})
  - 6 Phase B entries (non-resonance + non-degeneracy at
    d ∈ [3,8])
  - 3 Phase C entries (B-T 1933 §§7-9 verbatim quotes with
    page anchors)
  - 1 Phase D verdict entry
  - 1+ Phase E artifact provenance entries (if E runs)

═══════════════════════════════════════════════════════════════
§4 HALT CONDITIONS
═══════════════════════════════════════════════════════════════

HALT_T1P2_INDICIAL_DRIFT — Phase A's chi_d at d=2 doesn't
  recover the proven d=2 result, OR at d=3 / d=4 the indicial
  polynomial doesn't match the empirical d=3 / d=4
  verifications. Investigate Phase A method; possibly
  recursively apply Phase A* normalization-resolution.

HALT_T1P2_NONRESONANCE_FAILS_GENERIC — Phase B finds
  non-resonance fails at multiple d values in a way that
  suggests it's a generic algebraic property, not specific to
  one d. This means the upper bound A ≤ 2d may not hold
  universally; only at specific d values where non-resonance
  is satisfied.

HALT_T1P2_BT_NOT_LANDED — B-T 1933 PDF not at expected path
  + SHA verification failure. Operator confirms acquisition
  workflow.

HALT_T1P2_NONRESONANCE_MISMATCH — Phase A's stated
  non-resonance condition doesn't match B-T 1933's. Phase A
  reading or Phase C reading needs review.

HALT_T1P2_NONDEGENERACY_MISMATCH — analogous; non-degeneracy
  condition doesn't match.

HALT_T1P2_BIBKEY_COLLISION — Phase 0.5 detects bibkey
  collision in any new bibliography entry. Surface to
  operator for renaming.

HALT_T1P2_ADAMS_GAP — Phase 2 surfaces a specific dependency
  on Adams 1928 that transitive evidence does NOT cover. Per
  A-01 verdict, this is unlikely; if it does occur, surface
  to operator + halt for Adams acquisition decision.

HALT_T1P2_LITERATURE_DISAGREES_WITH_012 — Phase C's reading
  contradicts the empirical d=3 / d=4 verifications. Phase A
  or Phase C reading needs revision.

═══════════════════════════════════════════════════════════════
§5 FORBIDDEN-VERB HYGIENE
═══════════════════════════════════════════════════════════════

Per CT v1.4 / Q20a hygiene rules:
  - "trivial" / "trivially" / "obvious" / "clearly" — forbidden
    in artifact LaTeX; replace with explicit derivation or
    cite location
  - "easily seen to" — forbidden; replace with explicit
    derivation
  - "Wasow §X.3" — DEPRECATED per Q20a anomaly 4; use
    "Wasow §19 (Theorem 19.1, eq. 19.3)" or
    "Wasow §X.3 (Theorem 11.1)" depending on which result
    is cited
  - "We claim" / "It is clear that" — forbidden; replace
    with explicit derivation or citation

═══════════════════════════════════════════════════════════════
§6 OUTCOME LADDER
═══════════════════════════════════════════════════════════════

UPGRADE_FULL_d_LE_d_max — Phase A + B + C all pass at
  d ∈ [3, d_max=8] with full literature anchoring. M4 ✅
  closes; H1 → PROVEN at d ≥ 3; M9 gating → {M6 only}.
  Best-case outcome.

UPGRADE_PARTIAL_d_LE_d* — Phase 2 lands but d-range bounded
  at d* < d_max. M4 partial; H1 → PROVEN at d ∈ [3, d*],
  empirical at d > d*; M9 gating remains {M4-partial, M6}.

UPGRADE_PARTIAL_PAGECOUNT — Phase E build at non-canonical
  page range (e.g., 5-6 pp instead of 7-8). Operator decides
  whether to deposit.

HALT_T1P2_* — see §4.

═══════════════════════════════════════════════════════════════
§7 STANDING FINAL STEP
═══════════════════════════════════════════════════════════════

Output to chat (mandatory):

  BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/
          tree/main/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/

  CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/
                siarc-relay-bridge/main/sessions/2026-05-03/
                T1-BIRKHOFF-PHASE2-LIFT-LOWER/handoff.md

  VERDICT: <one of UPGRADE_FULL_d_LE_d_max /
           UPGRADE_PARTIAL_d_LE_d* / UPGRADE_PARTIAL_PAGECOUNT /
           HALT_T1P2_INDICIAL_DRIFT /
           HALT_T1P2_NONRESONANCE_FAILS_GENERIC /
           HALT_T1P2_BT_NOT_LANDED /
           HALT_T1P2_NONRESONANCE_MISMATCH /
           HALT_T1P2_NONDEGENERACY_MISMATCH /
           HALT_T1P2_BIBKEY_COLLISION /
           HALT_T1P2_ADAMS_GAP /
           HALT_T1P2_LITERATURE_DISAGREES_WITH_012>

  ANOMALIES: <numbered list if any>

  STRATEGIC_IMPLICATION: <verdict's effect on M4 / M9 / H1>

═══════════════════════════════════════════════════════════════
§8 OUT OF SCOPE
═══════════════════════════════════════════════════════════════

  - Closing M6 (canonical-form Stokes constant; separate
    CC-VQUAD-PIII-NORMALIZATION-MAP task; gated on R5
    acquisition)
  - Modifying CT v1.3 / CT v1.4 / D2-NOTE v2.1 / PCF-1 v1.3 /
    PCF-2 v1.3 / umbrella v2.0
  - Submitting to arXiv or any journal portal (per Rule 2)
  - Generating any artifact requiring API key input
    (per Rule 1)
  - Acquiring Adams 1928 (operator-side task; surface via
    HALT_T1P2_ADAMS_GAP only if Phase 2 specifically requires it)
  - Reading Loday-Richaud 2016 / Costin 2008 / Okamoto 1987 /
    Conte-Musette / Lisovyy-Roussillon (these are for D2-NOTE
    v2.1 / Q21 / Prompt 019 / Prompt 015; not Phase 2 anchors)
  - Tier-2 arbitrations (Q-CLAUDE-30-31, Q20-proof-upgrade,
    G17, Q21, Q22, Q23, Q24) — defer to v1.16 cycle
```

---

## Synthesizer notes (Note 1–5)

Per the deposit-task spec §2.1, the synthesizer chat ordinarily
appends "Note 1–5" framing the spec. Those side-notes were not
retained in the operator-side relay paste used to deposit this
spec; the verbatim spec body above is the load-bearing artifact.
For AEAL completeness, the cross-deposit anchors Note 1–5 normally
cover are:

- **Note 1 (M9 critical-path framing):** captured in §0 CONTEXT.
- **Note 2 (literature-PDF SHA hashes + Phase 1 dossier
  references):** captured in §1 ANCHOR FILES.
- **Note 3 (AEAL claims minimum):** captured in §3.
- **Note 4 (forbidden-verb hygiene + Wasow §X.3 → §19
  vocabulary correction):** captured in §5.
- **Note 5 (out-of-scope items, Tier-2 arbitration deferral):**
  captured in §8.

So Note 1–5 are structurally inlined into the spec body itself; no
separate appendix is missing.

---

End of spec; the relay agent has already executed this spec
(verdict `UPGRADE_PARTIAL_FORMAL_LEVEL`, bridge commit `37c939f`).
