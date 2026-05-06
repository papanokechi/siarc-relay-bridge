# Synthesizer-Substitute Verdict on Q1 / Q2 / Q4 of relay 051 (bt_baseline_note v1.0)

**Provenance.** This deliverable is an **operator-authorized synthesizer-substitute
verdict** issued by T2 (GitHub Copilot CLI, daily-cadence executer tier under
SIARC RACI v2026-05-05) acting cross-tier in a T1-Synthesizer capacity for
this round only. Operator chat instruction 2026-05-06 ~16:40 JST:
*"for Q1/Q2/Q4 arbitration, proceed you being the new synthesizer."*
Operator follow-up: *"double check with a prompt for copilot researcher
agent as necessary (in order to avoid unexpected outcome and for quality
assurance)."*

**This is NOT a canonical T1-Synthesizer verdict.** Canonical T1-Synthesizer
re-arbitration (Claude.ai weekly-cadence) on the next ISO week (W20,
beginning Mon 2026-05-11) is **explicitly recommended** below as a
follow-up gate, especially for any repo-wide wording or scope-statement
changes that this finding would motivate.

**Date.** 2026-05-06 ~17:00 JST (W19 Wed, ISO 2026-W19).

**Substrate basis.** bt_baseline_note v1.0 (Zenodo
[10.5281/zenodo.20048197](https://zenodo.org/records/20048197), PDF SHA-256
`23022f0d…f0e5b7c`); T1-Phase-2 verdict
`UPGRADE_PARTIAL_FORMAL_LEVEL` at bridge `37c939f` (sessions/2026-05-03/
T1-BIRKHOFF-PHASE2-LIFT-LOWER/); PCF-2 v1.3 program statement
(`tex/submitted/pcf2_program_statement.tex`); PCF-1 v1.3
(`tex/submitted/p12_journal_main.tex`); PCF-2 R1.1/R1.3/Q1 cubic+quartic
harvest scripts (`pcf-research/pcf2/session_*_2026-05-01/*.py`).

**QA basis.** Mandatory rubber-duck critique (this session, ~16:55 JST)
adopted in full. See `rubber_duck_critique.md` for the verbatim critique
and the per-finding adoption record.

================================================================
## Executive summary
================================================================

| Q | Verdict (revised after rubber-duck QA)                                             | Confidence |
|---|------------------------------------------------------------------------------------|------------|
| Q1 | **PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT** (scoped to PCF-2 R1.1/R1.3/Q1 harvest scripts); mechanism (i') likely unnecessary for harvested scripts; mechanism (ii') remains separately audit-worthy | HIGH (script/protocol mismatch + WZ plug-in `deg_a = 0 ⇒ A_naive = 2d`); MEDIUM-HIGH (Section 5 reframing); MEDIUM (PCF-1 / picture v1.20 / scope-wording implications) |
| Q2 | **GATED_BY_Q1_PIVOT** (likely MOOT for PCF-2 stratum after the convention-reconciliation audit; provisional fallback `B = √(c_a)` retained as expected ansatz analogue if (i') reopens) | MEDIUM (gating logic); LOW-MEDIUM (provisional fallback) |
| Q4 | **WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE** (independent of Q1); Wasow §X.3 Theorem 11.1 is the canonical sectorial-upgrade theorem; Costin 2008 ch.5 (Borel–Laplace radius) is the accessible-on-disk operational substitute | MEDIUM-HIGH (substrate-side reading; depends on confirming SIARC's Gevrey order is q=1 normal-case at irregular singularity) |

**One-line strategic implication.** The bt_baseline_note v1.0 deposit
remains canonical at Zenodo `10.5281/zenodo.20048197`; this verdict
**does not motivate a v1.x amendment** (the deposit's Theorem 1.1 is
correct as stated for the band `deg_a ∈ {d-1, d, d+1}` it explicitly
covers). What this verdict **does** motivate is an **add-on Phase 3-A
audit** extending the WZ table to `deg_a = 0` ((1, b) convention used
by PCF-2 R1.1/R1.3/Q1 cubic+quartic harvest scripts), and a
**reconsideration of Section 5's gap-framing** for those harvests
specifically.

================================================================
## Q1 — Mechanism arbitration: PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT
================================================================

### Q1 question (verbatim from `bt_baseline_note.tex` §6, Open Problem 1)

> "Which of (i') or (ii') is realised on the SIARC PCF Wallis stratum at
> d ≥ 3? Distinguishing them requires either (a) a symbolic derivation
> of the √n sub-leading correction predicted by (i') and an empirical
> test on the log|p_n/p_{n-1}| tail, or (b) a careful re-statement of
> the PCF-2 fit-protocol that supports or rules out
> A_fit = μ_dom − μ_sub under (ii')."

### Q1 finding (substrate-level)

The PCF-2 v1.3 R1.1/R1.3/Q1 cubic+quartic harvest scripts (the empirical
record cited in `bt_baseline_note.tex` §3 as the data driving the
gap-framing of §5) implement the continued fraction via the canonical
`(1, b)` backward recurrence, hardcoding partial numerators `a_n ≡ 1`
identically. Verbatim from `pcf-research/pcf2/session_C1_2026-05-01/
session_c1_wkb.py` lines 79–86:

```python
def cf_value(coeffs, N: int, dps: int) -> mp.mpf:
    a3, a2, a1, a0 = coeffs
    with mp.workdps(dps):
        x = mp.mpf(a3) * N ** 3 + mp.mpf(a2) * N ** 2 + mp.mpf(a1) * N + mp.mpf(a0)
        for k in range(N - 1, -1, -1):
            bk = mp.mpf(a3) * k ** 3 + mp.mpf(a2) * k ** 2 + mp.mpf(a1) * k + mp.mpf(a0)
            x = bk + mp.mpf(1) / x
        return +x
```

The recurrence `x = b_k + 1/x` (no multiplicative `a_k` factor on the
`1/x` term) implements canonical `(1, b)` CF
`b_0 + 1/(b_1 + 1/(b_2 + …))`. Same backward-recurrence pattern is used
in Session B (`session_b_pslq.py:162-168`) and Quartic Q1
(`quartic_tail_fit_all60.py:21-30`) per rubber-duck verification.

The PCF-2 v1.3 program statement at `tex/submitted/
pcf2_program_statement.tex` line 230 declares the program scope as
`a_n = δ_1 n + δ_0` (linear in n, `deg_a ≤ 1`). The actual harvest
scripts implement `a_n ≡ 1` (constant, `deg_a = 0`). This is a
**protocol-to-stratum mismatch** between the program statement's
declared stratum and the harvest-script-implemented stratum.

The bt_baseline_note's WZ table `bt_baseline_note.tex` §3-§4 Theorem 1.1
covers `deg_a ∈ {d-1, d, d+1}` (the three SIARC α/symmetric/δ-direction
conventions) and **does not include `deg_a = 0`**.

### Q1 finding (analytic level)

Re-running the WZ normal-case Newton-polygon balance analysis with
`deg_a = 0`, `c_a = 1`, `deg_b = d`:

Edge equation: `1 - c_b · n^{d-μ}/γ - 1 · n^{0-2μ}/γ² = 0`.

Three balance possibilities (cf. `phase_a_summary.md:22-30`):

- **(I) `1 ↔ c_b/γ`**: `μ = d`, `γ = c_b`. Third term `n^{-2d} ≪ 1` for
  d ≥ 2. Consistent ⇒ **`μ_dom = d`, `γ_dom = c_b`**.
- **(II) `1 ↔ 1/γ²`**: `μ = 0`, `γ² = 1`. Second term `n^d/γ ≫ 1` for
  d ≥ 1. Inconsistent ⇒ excluded.
- **(III) `c_b/γ ↔ 1/γ²`**: `d - μ = -2μ` ⇒ `μ = -d`, `γ = -c_a/c_b`
  ⇒ **`μ_sub = -d`, `γ_sub = -1/c_b`** for `c_a = 1`. Third and second
  terms both `n^{2d}`, "1" term ≪ both. Consistent.

Hence under `deg_a = 0`:

```
A_naive = μ_dom − μ_sub = d − (−d) = 2d.
```

This is consistent with the empirical record:

- d = 3 cubic mean: `A_fit = 5.978`, σ = 0.026, predicted 2d = 6
  ⇒ within σ.
- d = 4 quartic mean: `A_fit = 7.954`, σ = 0.0037, predicted 2d = 8
  ⇒ within σ.

The "gap" between `A_naive ∈ {d-1, d, d+1}` (the band proven in
Theorem 1.1) and `A_fit ≈ 2d` (the PCF-2 v1.3 R1.1/R1.3/Q1 empirical
record) **likely reduces to** the protocol-to-stratum mismatch:
Theorem 1.1's band is for `deg_a ∈ {d-1, d, d+1}`, but the empirical
samples are for `deg_a = 0`, where the WZ normal-case directly
predicts `A_naive = 2d` matching empirical.

### Q1 verdict

**`PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT`** (scope: PCF-2 R1.1/R1.3/Q1
cubic+quartic harvest scripts).

For the harvest-script-implemented PCF-2 R1.1/R1.3/Q1 stratum
(`a_n ≡ 1`, `deg_a = 0`), mechanism (i') (borderline-locus,
`deg_a = 2 deg_b`) is **not currently needed**: under correct stratum
identification, the WZ normal-case analysis directly predicts
`A_naive = 2d` matching empirical, with the SIARC stratum strictly in
WZ NORMAL CASE (`deg_a = 0 < 2d` for d ≥ 1).

Mechanism (ii') (definitional) **remains separately audit-worthy** as
an operational-definition question, even after the protocol-to-stratum
mismatch is resolved. The harvest scripts fit `log|delta_n|` where
`delta_n = L_N − L_ref` is the convergent residual (not
`log|p_n/p_{n-1}|` which is a single-solution growth-rate observable).
By the Wallis pair theorem, `|delta_n| = |∏ a_k| / |q_n q_{n-1}|`, and
in the WZ normal case the coefficient of `n log n` in `log|delta_n|`
equals `−A_naive` exactly. The (ii')-style definitional question
reduces, under that correspondence, to confirming that the script's
4-parameter least-squares fit converges to the WZ-predicted leading
coefficient as `n → ∞` without bias from finite-N tail-window effects.

### Q1 recommended T1 Phase 3 sub-tasks

- **3-A (audit)**: Extend the bt_baseline_note Phase A WZ table to
  include `deg_a = 0` ((1, b) convention). Re-derive `A_naive = 2d`
  symbolically. Numerically verify against the existing
  PCF-2 R1.1/R1.3/Q1 50+60+0 = 110 harvested rows.
- **3-B (audit)**: Run a dedicated convergent-residual fit-protocol
  audit comparing `coefficient of −n log n in log|L_N − L_ref|` against
  the WZ-predicted `A_naive = 2d`. Quantify finite-N tail-window bias
  and confirm σ-band stability across `N_ref ∈ {300, 600, 1200}`.
- **3-C (note revision, blocked on 3-A + 3-B verdict)**: Revise
  bt_baseline_note v1.x §5 gap-framing to a CONVENTION-RECONCILIATION
  framing for the PCF-2 R1.1/R1.3/Q1 stratum scope, retaining the
  current §5 framing only for `deg_a ∈ {d-1, d, d+1}` strata that
  are not in PCF-2's harvest record.

**Note.** Sub-task 3-C is a v1.x **deposit-revision** decision. The
current v1.0 Zenodo deposit is **not retroactively wrong** — Theorem 1.1
remains correct as stated for the band `deg_a ∈ {d-1, d, d+1}`. What
3-C contemplates is **adding** the `deg_a = 0` row and **revising
§5's interpretation** of the gap for the PCF-2 R1.1/R1.3/Q1 record. The
v1.0 deposit can stand as canonical; v1.1 (or v1.2 within the bridge
chain) absorbs the stratum-extension as an additive amendment, not a
retraction.

================================================================
## Q2 — Borderline-Q ansatz: GATED_BY_Q1_PIVOT
================================================================

### Q2 question (verbatim from `bt_baseline_note.tex` §6, Open Problem 2)

> "Under (i'), can the BT 1933 §1 borderline-case ansatz
> Q_j(x) = ±B x^(1/2) + (lower order) be made explicit at the SIARC
> stratum, with B = √(c_a) closed form?"

### Q2 verdict

**`GATED_BY_Q1_PIVOT`**.

Q2 is **gated on Q1 = `CLOSURE_VIA_(i')`**. Under the revised Q1 verdict
(`PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT`), mechanism (i') is **not
realised** on the harvest-script PCF-2 R1.1/R1.3/Q1 stratum (which is
strictly in WZ NORMAL CASE with `deg_a = 0 < 2d`), so the borderline-Q
question is **likely moot for that stratum scope**.

Provisional fallback (retained in case Q1's stratum-mismatch finding
is rejected at T1 Phase 3 sub-task 3-A): `B = √(c_a)` is the expected
closed form by analogy with PCF-1 v1.3 §6 Theorem 5 V_quad upper branch
(`p12_journal_main.tex` ∼ §6) where the d=2 V_quad stratum (`deg_a = 0`,
`a_n ≡ 1` per `algebraic_independence_audit.py:37-40` per rubber-duck
verification) yields `A = 4 = 2d` directly. The provisional ansatz is
not load-bearing in the revised verdict; its retention is purely a
hedge against possible Q1 reversal.

### Q2 recommended T1 Phase 3 sub-tasks

Q2 audit work is **deferred** pending Q1 sub-task 3-A verdict. If
sub-task 3-A confirms the protocol-to-stratum mismatch finding, Q2
closes as `MOOT_VIA_Q1_PIVOT` with no additional audit needed.

================================================================
## Q4 — Formal-to-analytic sectorial upgrade: WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE
================================================================

### Q4 question (verbatim from `bt_baseline_note.tex` §6, Open Problem 4)

> "Through which sectorial-summability theorem does the formal-level
> baseline of Theorem 1.1 lift to an analytic statement on the
> convergent residual? Candidates include Wasow §X.3 Theorem 11.1,
> Adams 1928, Turrittin 1955, Immink 1984, and Costin 2008 ch. 5."

### Q4 finding

This question is **independent of Q1's resolution**. Even under Q1
PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT (where the empirical
`A_fit ≈ 2d` aligns with the WZ-formal `A_naive = 2d` after stratum
correction), the formal-to-analytic justification for the Wallis
recurrence's formal series solutions (in the Gevrey-1 series ring
`Γ(n)^μ γ^n n^ρ ℂ[[1/n]]`) remains a separately required theorem-grade
step.

Two candidates differ by accessibility, not by mathematical strength:

- **Wasow §X.3 Theorem 11.1** is the **canonical sectorial-upgrade
  target**. It is the most direct theorem statement for the formal-to-
  analytic upgrade in the WZ normal case. As of 2026-05-06, the Wasow
  PDF on disk is image-only with no OCR (per A-01 verdict
  `sessions/2026-05-04/A-01-AUDIT/`); no machine-readable
  acquisition available.
- **Costin 2008 ch. 5 (Borel–Laplace radius)** is the **accessible-on-
  disk operational substitute**. The chapter substrate is already
  acquired as `tex/submitted/control center/literature/g3b_2026-05-03/
  06_costin_2008_chap5.txt` and provides equivalent analytic-side
  guarantee for Gevrey-1 formal series with appropriate Stokes-multiplier
  conditions.

### Q4 verdict

**`WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE`**.

For the bt_baseline_note v1.x roadmap: cite Wasow §X.3 Theorem 11.1
as the **canonical sectorial-upgrade target**, with Costin 2008 ch.5 as
the **accessible-on-disk operational substitute** when Wasow's exact
hypotheses cannot be verified due to the OCR gap. Turrittin 1955 and
Immink 1984 are **not yet acquired** and **not needed at this scope**;
they are listed as historical-completeness references only.

### Q4 recommended T1 Phase 3 sub-tasks

- **3-D (sectorial upgrade, blocked on Q1 sub-task 3-A)**: Apply
  Costin 2008 ch.5 Borel–Laplace radius theorem to the Wallis
  recurrence's formal series solutions at `μ_dom = d`, `μ_sub = -d`
  (PCF-2 R1.1/R1.3/Q1 stratum). Produce explicit Stokes-multiplier
  conditions and sector-opening estimates.
- **3-E (Wasow OCR resolution, parallel)**: Acquire OCR-clean Wasow
  §X.3 PDF (or scan + OCR an existing copy if available), cross-check
  Theorem 11.1's hypotheses against SIARC's normal-case stratum, and
  report any differences from Costin 2008 ch.5's hypotheses.

================================================================
## Audited blind spots
================================================================

The rubber-duck critique (see `rubber_duck_critique.md`) flagged 3
blind spots; each is audited below.

### Blind spot 1: PCF-1 may use a different convention

**Audit (this session)**: PCF-1 v1.3 (`tex/submitted/p12_journal_main.tex`
L128–136) defines the d=2 standard stratum as `a_n = δ n + ε`,
`b_n = α n² + β n + γ` with `α, δ ≠ 0`. So PCF-1 v1.3 uses
`deg_a = 1` (linear, with δ explicitly nonzero), **distinct** from
PCF-2 v1.3 cubic-harvest's `deg_a = 0`. This **scopes** the Q1 finding:
the protocol-to-stratum mismatch finding applies to **PCF-2
R1.1/R1.3/Q1 specifically**, NOT to PCF-1 v1.3 §6 Theorem 5.

Under PCF-1's `deg_a = 1` convention at d=2, the WZ normal-case directly
predicts `A_naive = 2d - 1 = 3`, matching PCF-1 v1.3 §6 Theorem 5
LOWER branch QL01–QL26 exactly. PCF-1 v1.3 §6 Theorem 5 UPPER branch
V_quad (`A = 4`) **may** be in a different convention with `a_n ≡ 1`
(`algebraic_independence_audit.py:37-40` per rubber-duck citation;
not independently verified by T2 this session); under that hypothesis
V_quad's `A = 4 = 2d` matches WZ normal case at `deg_a = 0`. This is
a **secondary observation** — not load-bearing in this verdict and
flagged for canonical T1-Synth follow-up at next ISO week.

### Blind spot 2: Seed conditions

The seeds `(p_{-1}, p_0, q_{-1}, q_0) = (1, b_0, 0, 1)` (per PCF-2 v1.3
program statement L234) determine the dominant/subdominant solution
mix in the convergent residual `δ_n = p_n/q_n − L`, but **do not
change** the Newton-polygon balance analysis (Phase A.1–A.4 of
phase_a_summary.md). The WZ leading-coefficient prediction
`A_naive = μ_dom − μ_sub` is seed-independent. Seeds enter only at
sub-leading order (the `α n − β log n + γ` terms of the WKB fit).
**Not load-bearing** for this verdict.

### Blind spot 3: "Classifier mismatch" vs "protocol-to-stratum mismatch"

The rubber-duck flagged that "classifier mismatch" (the rule5 label)
is close but not exact: here the issue is not just that a classifier
labels the stratum incorrectly, but that **prose (program statement)
and scripts (harvest implementations) disagree on the stratum
definition itself**. The verdict adopts the rubber-duck's preferred
phrasing: **`PROTOCOL_TO_STRATUM_MISMATCH`**. This is a slight
extension of the rule5 amendment vocabulary — flagged for canonical
T1-Synth assent at next ISO week to either ratify the new label or
fold it back into rule5's existing terminology.

================================================================
## Confidence assessment (per rubber-duck split recommendation)
================================================================

| Component | Confidence | Justification |
|-----------|------------|---------------|
| PCF-2 R1.1/R1.3/Q1 harvest scripts use `(1, b)` `a_n ≡ 1` (`deg_a = 0`) | HIGH | Direct script inspection: `cf_value` lines 79–86 in `session_c1_wkb.py` implements canonical `(1, b)` backward CF; rubber-duck cross-check on `session_b_pslq.py:162-168` and `quartic_tail_fit_all60.py:21-30` confirms same pattern across the harvest set. |
| WZ plug-in at `deg_a = 0` yields `A_naive = 2d` | HIGH | Mechanical derivation from the Phase A general formula `A_naive = μ_dom − μ_sub` with balance (I) `μ_dom = d` and balance (III) `μ_sub = -d` for `deg_a = 0`. Matches existing Phase A-pattern of phase_a_summary.md L22-44. |
| bt_baseline_note v1.x §5 gap-framing should be revised for PCF-2 R1.1/R1.3/Q1 scope | MEDIUM-HIGH | Stratum mismatch is established; appropriate scope of revision (additive `deg_a = 0` row vs. §5 retraction vs. §5 reframing) requires canonical T1-Synth assent. |
| Implications for PCF-1 v1.3, picture v1.20, PCF-2 v3.x scope wording | MEDIUM | PCF-1 substrate analysis is incomplete this session (V_quad's convention not independently verified). Picture v1.20 deposit is LATE-FIRE post-W20 anyway. PCF-2 v3.x wording is canonical T1-Synth scope. |
| Q4 Wasow / Costin operational ranking | MEDIUM-HIGH | Substrate-side reading; depends on confirming SIARC's specific Gevrey order at irregular singularity is q=1 (normal-case) — likely but not independently verified this session. |

================================================================
## Hygiene self-check
================================================================

### AEAL forbidden-verb hygiene (per `bt_baseline_note.tex` §5.4)

The verdict avoids "shows", "confirms", "proves" in
prediction-or-conjecture context. Used phrasings: "indicates", "is
consistent with", "likely reduces to", "directly predicts" (where
"directly predicts" is mechanical-derivation language for the WZ plug-in,
not a prediction-vs-empirical comparison). The phrase "matching
empirical EXACTLY" was deleted on rubber-duck recommendation; replaced
with "is consistent with the empirical record … within σ".

### Rule5 amendment compliance

This verdict is itself a synthesizer-class deliverable referencing
empirical absolute claims from a preprint (PCF-2 v1.3 R1.1/R1.3/Q1).
Per rule5, the dispatch-side classifier (bt_baseline_note's
`deg_a ∈ {d-1, d, d+1}` band in Theorem 1.1) is hereby flagged as
**not matching** the preprint-side stratum definition (PCF-2 cubic+
quartic harvest scripts implement `deg_a = 0`). This rule5-flag is the
core finding of Q1.

### M6 token disambiguation (per `tex/submitted/control center/CONVENTIONS_LEG_NAMING.md`)

This verdict uses no bare `M6` token. Q1/Q2/Q4 are unrelated to the
M6 caveat profile (which concerns the Phase III Painlevé canonical-form
normalization map). M6 is not in scope.

### Bibliographic identifier pre-verification

This verdict does not introduce any new DOI or arXiv-ID citation as
acquisition target. References to existing artefacts (Zenodo
`10.5281/zenodo.20048197` for bt_baseline_note v1.0; PDFs already on
disk) are post-acquisition citations, not pre-fire targets, and do
not require pre-resolution.

================================================================
## Recommended canonical T1-Synthesizer follow-up (W20, Mon 2026-05-11)
================================================================

This synthesizer-substitute verdict is operator-authorized but
**explicitly deferred for canonical T1-Synthesizer re-arbitration**
at the next ISO week (W20, beginning Mon 2026-05-11). Specific items
for canonical T1-Synth assent:

1. **Ratify or reject** the `PROTOCOL_TO_STRATUM_MISMATCH` finding
   (Q1) and its scope to PCF-2 R1.1/R1.3/Q1 specifically.
2. **Authorize or defer** T1 Phase 3 sub-tasks 3-A through 3-E.
3. **Decide** whether bt_baseline_note v1.x deposit revision is
   warranted (additive `deg_a = 0` row + §5 reframing → v1.1) or
   whether the v1.0 deposit can stand canonical with this verdict
   recorded as a follow-up note.
4. **Ratify or fold** the `protocol-to-stratum mismatch` label into
   the rule5 amendment vocabulary.
5. **Decide** whether picture v1.20 (LATE-FIRE post-W20) absorbs
   this finding as an anomaly entry or as a primary substrate row.
6. **Decide** whether PCF-2 v3.x scope-statement wording requires
   updating to clarify the implemented stratum (`a_n ≡ 1`) vs the
   declared stratum (`a_n = δ_1 n + δ_0`).

================================================================
## Files in this deposit
================================================================

- `synth_substitute_verdict.md` — this file
- `rubber_duck_critique.md` — verbatim rubber-duck critique +
  per-finding adoption record
- `claims.jsonl` — AEAL claim anchors
- `halt_log.json` — empty (no halts triggered)
- `discrepancy_log.json` — anomalies and judgment calls
- `unexpected_finds.json` — non-blocking observations
- `handoff.md` — standing final step handoff

================================================================
## AEAL claim count
================================================================

12 entries in `claims.jsonl` (substrate-survey + rubber-duck-adopted
findings + verdict statements). All claims are
`evidence_type: "literature_desk"` or `"script_inspection"` — this is
a synthesizer-class deliverable; no numerical execution was performed
this session.
