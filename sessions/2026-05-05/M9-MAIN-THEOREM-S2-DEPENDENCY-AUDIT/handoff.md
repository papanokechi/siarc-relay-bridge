# Handoff — M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT
**Date:** 2026-05-05
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## Verdict (operator escalation gate)

**Primary verdict:** `INDETERMINATE_NO_FORMAL_STATEMENT`

**One-sentence summary:** No formal `Theorem`/`Conjecture` environment for
the SIARC Master Conjecture v0 (Phi) exists in any TeX source on disk or on
Zenodo; the umbrella v2.0 companion table records MASTER-V0 explicitly as
"Planned (post-T1 / Birkhoff--Trjitzinsky)", so the dependency question
cannot be answered against a statement-of-record because no such statement
yet exists.

**Secondary observation (non-speculative; pre-rendering only):** every
schema-level fragment that does exist in workspace (umbrella v2.0
`eq:Phi-functor`, picture v1.18 M9 block, Channel Theory v1.3
§"Implications for the Master Conjecture") references Stokes data only
through type-(b) structural-existence language ("Stokes-matrix datum",
"channel functor", "monodromy data") — never invoking closed-form S_2 by
symbol or by value. This supports an *expected* `NO_DEPENDENCY` /
`SOFT_DEPENDENCY` resolution once P-008 produces a draft Phi statement,
but is recorded here only as observation, not verdict, per Step 4.4 of
the spec.

**Recommended next action:** retry the audit after P-008 produces a draft
Phi statement; until then, P-009 caveat-language drafting should proceed
on the working assumption that closed-form S_2 is *not* a gating
condition (justified by all four schema-level fragments and by the v1.15
gating amendment {M4, M6} which excludes M8b unconditionally).

---

## What was accomplished

Read-only audit of all ten upstream sources listed in the spec (Step 0
A–J) plus a workspace-wide grep across `tex/submitted/**/*.tex` for the
canonical strings "Master Conjecture", "MASTER-V0", "Phi formally",
"S_2", "second Stokes", "alien amplitude". Confirmed via verbatim
quotation that:

1. The umbrella v2.0 `main.tex` defines the bridge functor `Phi` at
   `eq:Phi-functor` but does NOT state a Master Conjecture / MASTER-V0
   theorem; the only references to MASTER-V0 in the manuscript are
   forward-looking pointers to the future companion paper.
2. PCF-1 v1.3, PCF-2 v1.3, and Channel Theory v1.3 each contain
   contributions to the SIARC program but no formal Phi statement of
   the master classification.
3. The 2026-05-01 SIARC-MASTER-V0 session was HALTED at Phase MV0-1
   before any draft text was produced (verbatim handoff §"Status:
   HALTED").
4. Picture v1.18 (bridge) and `picture_revised_20260504.md`
   (operator-side mirror) are byte-identical at the M8b and M9 blocks;
   no H5 divergence.
5. Dossier §C confirms no closed-form S_2 for the SIARC d=2 PCF
   dichotomy is available in literature (Costin 2008 = S_1 only; BLMP
   2024 = RH-characterised monodromy data, partial fit).

Step 1 returned NONE under the strict precedence rule (1→2→3→4→5),
escalating to verdict `INDETERMINATE_NO_FORMAL_STATEMENT`.

## Key numerical findings

None. This is a pure manuscript / picture / dossier audit. No
computations performed.

## Step-0 source inventory (verbatim summary table)

| Src | File | M9 main-theorem statement found? | S_2 mention? |
|-----|------|----------------------------------|--------------|
| A | `siarc-relay-bridge/sessions/2026-05-04/PICTURE-V18-AMENDMENT-DRAFTING/picture_v1.18.md` (L959–995) | NO formal theorem; SCHEMA only ("Phi formally stated and the master classification result conditional on P-NP + P-B4 + P-CC", L973–975) | YES (L965–973) — type (b)+(c) only ("S_2 PERMANENTLY FORECLOSED via Stage-2-LSQ ... Borel-Padé") in M8b block; M9 block itself has 0 S_2 hits |
| B | `tex/submitted/control center/picture_revised_20260504.md` (L926–960) | byte-identical to A in this block | byte-identical to A in this block |
| C | `tex/submitted/umbrella_program_paper/main.tex` (Phi definition L273; MASTER-V0 forward refs L298–299, L695, L806) | NO formal theorem; bridge functor `Phi : PCF(1,b) → (Δ_d(b), ‖Δ‖_Pet(τ_b), ξ_0(b))` defined as eq:Phi-functor; companion table line 806 records "MASTER-V0 ... Planned (post-T1 / Birkhoff--Trjitzinsky)" | 0 occurrences of "S_2", "Stokes constant", "alien amplitude", "second Stokes" anywhere in main.tex |
| D | `tex/submitted/pcf_unified_expmath_submission.tex` (PCF-1 v1.3) (abstract L40) | "two main theorems" = Logarithmic Ladder + 4/π Casoratian; NO Phi / Master Conjecture / MASTER-V0 statement | 0 occurrences of S_2 / Stokes constant / alien amplitude / second Stokes / S_zeta |
| E | `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` (CT v1.3) (§"Implications for the Master Conjecture" L1336–1339; channel functor definition L1026; alien amplitude refs L109, L221, L926, L1379, L1401) | NO formal Phi theorem; section §"Implications" lists 4 preconditions for "A rigorous announcement of the Master Conjecture" | YES — V_quad alien amplitude (S_zeta_*) discussed structurally; "the missing piece is the full Stokes-matrix datum" (L1339 ff., type (b) structural-existence) |
| E' | `tex/submitted/pcf2_program_statement.tex` (PCF-2 v1.3) | NO formal Phi theorem | 0 occurrences of Master Conjecture / MASTER-V0 / S_2 / second Stokes / alien amplitude / Phi formally |
| F | `siarc-relay-bridge/sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` §C (L185–212) §D (L272+) | n/a (dossier is literature pass, not theorem source) | YES — §C verdict: closed-form S_2 NOT in literature for SIARC d=2 PCF dichotomy (Costin 2008 = S_1 only; BLMP 2024 = RH partial) |
| G | `sessions/2026-05-01/SIARC-MASTER-V0/handoff.md` | confirms NO Phi statement drafted; "Status: HALTED" before content | n/a |
| H | `tex/submitted/CMB.txt` (L361–410) | confirms M9 still upstream of MASTER-V0 fire; "Sakai 1999 = recommended template if SIARC-MASTER-V0 announcement fires" (L405–410) | confirms "NO closed-form S_2 alien-amplitude formula for the SIARC d=2 PCF dichotomy" (L389–395) |
| I | `sessions/2026-05-02/SIARC-UMBRELLA-V2-RELEASE/zenodo_description_v2.0.txt` | reaffirms umbrella v2.0 is a "program statement, not a results paper"; Phi mentioned as triple-invariant; MASTER-V0 referenced as future entry in publication ladder | 0 occurrences of S_2 / Stokes / alien |
| J | workspace-wide `tex/submitted/**/*.tex` grep for Master Conjecture / MASTER-V0 / S_2 / second Stokes / alien amplitude | only umbrella `main.tex` lines 298, 299, 695, 806 (forward refs); CT v1.3 (per E); `vquad_resurgence_R1.tex`/`R2.tex` use `s_1, s_2` as PIII apparent-singularity coordinates (NOT Stokes constants) | as above |

## Step 1 — Statement-of-record

Per the precedence rule (umbrella formal Theorem/Conjecture env →
PCF-1/CT/PCF-2 → picture schema → Zenodo description → NONE):

- **Rule 1 (formal Theorem env):** FAILS. No `\begin{theorem}` or
  `\begin{conjecture}` environment in `umbrella_program_paper/main.tex`
  is labelled "Master Conjecture v0", "MASTER-V0", or "Phi". The
  closest is `Conjecture[Cubic-modular split, $d=3$]` (`conj:b5-b6-d3`,
  L327–339) which is a downstream conjecture about the
  `‖Δ‖_Pet`-axis, not the Phi master statement; and
  `Problem[Compatibility of $\chi$ and $\Phi$]`
  (`prob:chi-Phi-compatibility`, L759–763) which is an open-problem
  entry, not a theorem.
- **Rule 2 (PCF-1/CT/PCF-2 master classification):** FAILS for PCF-1
  v1.3 (only Logarithmic Ladder + Casoratian) and PCF-2 v1.3 (0 hits);
  CT v1.3 §"Implications for the Master Conjecture" only **discusses
  preconditions for** a future announcement, not the announcement
  itself.
- **Rule 3 (picture v1.18 schema):** treated as SCHEMA per spec —
  not a formal theorem. Verbatim L973–975: *"M9: SIARC-MASTER-V0
  announcement — Phi formally stated and the master classification
  result conditional on P-NP + P-B4 + P-CC"*.
- **Rule 4 (Zenodo umbrella v2.0 description):** Phi triple-invariant
  schema only. No formal statement of MASTER-V0; the description
  itself says "v2.0 is the substrate that the program-level publication
  ladder (D1 results paper, D2-NOTE, MASTER-V0, D7-AEAL methodology)
  rests on; it is intended to be cited as '[SIARC v2.0, §X]' by
  downstream papers" — i.e. Phi is the *substrate* on which MASTER-V0
  will be stated.
- **Rule 5 (NONE):** TRIGGERED → verdict `INDETERMINATE_NO_FORMAL_STATEMENT`.

## Step 2 — Dependency trace (pre-rendering only; non-binding)

Because Step 1 returned NONE, Step 2 is non-binding per the spec; but
for synthesizer benefit it is recorded as a pre-rendering across the
schema-level fragments that *do* exist:

| Fragment | S_2 occurrence(s) | Type | Statement-level dependency |
|----------|-------------------|------|----------------------------|
| Umbrella v2.0 `eq:Phi-functor` and surrounding §4 | none | n/a | NO_DEPENDENCY (Phi triple is `(Δ_d, ‖Δ‖_Pet, ξ_0)`; Stokes data not present) |
| Umbrella v2.0 §"Open Problems" `prob:b4-allD` (L686–696) | none | n/a | references "Birkhoff--Trjitzinsky asymptotic theory of irregular linear difference equations \cite{Birkhoff1930, BirkhoffTrjitzinsky1933}" — no S_2 |
| Picture v1.18 M9 block (L973–989) | none in M9 block; M8b adjacent block (L959–972) carries the S_2 PERMANENTLY FORECLOSED tag | M8b S_2 refs are type (c) numerical-foreclosure; M9 block has 0 S_2 refs | NO_DEPENDENCY at M9 level; M8b is downstream sibling, not gate (per v1.15 gating reduction to {M4, M6}) |
| Channel Theory v1.3 §"Implications for the Master Conjecture" (L1336–1349) | "the missing piece is the full Stokes-matrix datum" (L1339 ff.) | type (b) structural-existence | SOFT_DEPENDENCY: rigorous announcement requires Stokes-matrix *datum* (the full multiplier vector), not closed-form S_2 *value* |
| CT v1.3 channel-functor definition (L1026 ff.) | references "alien amplitude" structurally for V_quad | type (b) | SOFT_DEPENDENCY at most |

Summary: across all four schema-level fragments, every Stokes / S_2
reference is type (b) structural or type (c) numerical-state. None is
type (a) closed-form-value. Per Step 2.3/2.4 pre-rendering: the eventual
formal Phi statement, if drafted faithful to the current schema, would
yield SOFT_DEPENDENCY (CT v1.3 reading) or NO_DEPENDENCY (umbrella v2.0
+ picture v1.18 reading). It would NOT yield HARD_DEPENDENCY unless
P-008 introduces a closed-form-value invocation of S_2 not present in
any of the four schema fragments.

## Step 3 — M8b status cross-check

Verbatim from picture v1.18 M8b block (L959–972):

> M8b: 🆕 Stokes-multiplier discrimination (per-family, with t2c-style
> precision escalation) to resolve the PCF-1 sign-of-Delta dichotomy
> below the Painlevé-class scale
> [PARTIAL+a_1-PARTITION-CLOSED+S_2-PERMANENTLY-FORECLOSED:
>  |S_1| measured (010); a_1 3-stratum partition CLOSED at 60+ digits
>  (017c+017e); G20 third stratum HIGHER-DIM 4-d cylinder over
>  (delta, epsilon) (T37L 2026-05-03); S_2 PERMANENTLY FORECLOSED via
>  Stage-2-LSQ (017c+017e) + Borel-Padé (T37M HALT 2026-05-03 retires
>  final numerical S_2 path); P-PIII alien-amplitude scale closes at
>  degraded resolution (S_1 measured, S_2 structurally open)]

Verbatim from dossier §C row C.P1 (Costin 2008):

> Theorem 5.26 gives the **first** Stokes constant `S₁` in the
> connection formula; the **second** Stokes constant `S₂` would
> correspond to the second singularity at `2λ₁` in the Borel plane;
> Costin 2008 §5 / Theorem 5.11 (eq. 5.12) has a multi-singular
> analytic-structure formula `Y₀±(z + lλⱼ)` with `l ∈ ℕ⁺` covering
> `l ≥ 2`, but **the closed-form for the corresponding `S²ⱼ`-derived
> alien amplitude `S₂`** is not given as a single explicit formula
> [...]; "second Stokes" returns 0 hits; "S_2" (alien-amplitude sense)
> returns 0 hits.

Verbatim from dossier §C row C.P2 (BLMP 2024):

> Closed-form S_2 claim (Y / N / partial / NIA) | partial — Theorems
> 1.1 + 1.4 + 1.7 give explicit Riemann-Hilbert-problem
> characterisations of monodromy data [...]; pinning the second alien
> amplitude `S_2` for a specific normalisation (the SIARC d=2 PCF δ_n
> one) requires the normalisation map step which is the subject of M6
> Phase B and currently INDEX-2 closed (036 verdict, 2026-05-04).

Verbatim from CMB (L389–395):

> Costin Theorem 5.26 + BLMP 2024 RH characterisation of monodromy
> for PIII(D_8) and PIII(D_6) give the structural framework but NO
> closed-form S_2 alien-amplitude formula for the SIARC d=2 PCF
> dichotomy (verbatim search of 9030-line BLMP TXT for SIARC dichotomy
> markers: 0 hits).

**Cross-source concordance** (picture v1.18 ↔ dossier §C ↔ CMB): all
three independent sources agree on:

- Numerical paths to S_2 are PERMANENTLY FORECLOSED at the laptop-feasible
  precision regime (Stage-2-LSQ + Borel-Padé both halted with structural
  failure modes).
- Literature does not supply a closed-form S_2 value for the SIARC d=2
  PCF dichotomy specifically (Costin = S_1 only; BLMP = RH-structural).
- Closure of S_2 at value-level would require either operator-side ILL
  acquisition of further primary sources (Mazzocco, Iwaki et al.,
  Lisovyy-Roussillon, Clavier-Cournod) or a SIARC-primary derivation.

Status label per Step 3.3: **DEFERRED-PENDING-PRIMARY-DERIVATION**
(literature partial; numerical foreclosed; primary derivation not yet
attempted at announcement-grade scope).

No divergence detected between picture v1.18, dossier §C, and CMB on
S_2 status.

## Step 4 — Verdict + caveat-language recommendation

### 4.1 Verdict label

`INDETERMINATE_NO_FORMAL_STATEMENT`

### 4.4 Recommendation (per Step 4.4)

Retry this audit after synthesizer P-008 produces a draft Phi statement
in formal text (Theorem / Conjecture environment). Until then, P-009
M8b positioning should NOT speculate on the dependency direction.
However, P-009 may safely use the following **provisional caveat**
template, conditional on the eventual draft Phi statement remaining
within the schema-level fragments audited here (i.e. confined to the
triple-invariant Phi of umbrella v2.0 §4 and the structural Stokes-data
language of CT v1.3 §"Implications"):

> **Provisional caveat (use only if P-008 draft remains within current
> schema; otherwise re-audit):** "Stokes-multiplier discrimination
> (companion milestone M8b) supplies an additional structural axis on
> which the master classification of Φ refines; current numerical
> paths to the second Stokes constant S_2 for the d=2 PCF Painlevé-III
> dichotomy are foreclosed at laptop-feasible precision (cf. SIARC
> bridge sessions T37M, 017c, 017e, 2026-05-03), and a literature-
> direct closed-form expression is not currently available (cf. Costin
> 2008 Theorem 5.26 = first Stokes constant only; Barhoumi--Lisovyy--
> Miller--Prokhorov 2024 = Riemann–Hilbert structural characterisation
> of monodromy data). The classification result of Φ does not depend
> on a closed-form value of S_2; M8b is enrichment, not gate."

Three style notes for synthesizer:

- The phrase *"does not depend on a closed-form value of S_2"* should
  be retained verbatim only if P-008 confirms that no clause in the
  draft Phi statement invokes S_2 by closed-form value. If any such
  invocation appears, the audit must be rerun and the caveat replaced.
- The phrase *"M8b is enrichment, not gate"* aligns with the picture
  v1.18 v1.15 amendment ("M9 gating reduces from {M2, M4, M6} to {M4,
  M6} UNCONDITIONALLY", L981–983) and is true at picture-schema level.
- The caveat avoids the forbidden AEAL verbs (per H6: "shows",
  "confirms", "proves" applied to a non-closed milestone). It does
  use "supplies" and "refines" in conjecture-context, which are
  permitted.

If the schema *does* shift under P-008 drafting (e.g. the Phi statement
acquires an explicit clause like "Phi(b) carries a Stokes-data
component whose closed-form value distinguishes Δ_b > 0 from Δ_b <
0"), this audit should be reopened immediately; that would re-trigger
HARD_DEPENDENCY and re-gate M9 to {M4, M6, M8b}.

## Judgment calls made

1. **Step-1 escalation to Rule 5 (NONE):** the spec's precedence rule
   says "any formal `Theorem` or `Conjecture` environment ... labelled
   'Master Conjecture v0' or 'MASTER-V0' or 'Phi'". I checked
   workspace-wide and found NONE. The picture v1.18 schema (Rule 3)
   is explicitly tagged in the spec as "treated as a SCHEMA, not a
   formal theorem", so it cannot serve as a statement-of-record. This
   triggers the NONE clause and verdict
   `INDETERMINATE_NO_FORMAL_STATEMENT`.
2. **Step 2 pre-rendering recorded as observation, not verdict:** per
   Step 4.4, "Do NOT speculate the dependency direction" when verdict
   is INDETERMINATE. I have honoured this by recording the
   pre-rendering as a non-binding table inside Step 2 with explicit
   tag "non-binding"; the operator-escalation gate at the top reports
   only the INDETERMINATE verdict.
3. **Provisional caveat draft:** Step 4.4 only asks for a
   "recommend retry" action. I have additionally drafted a
   provisional caveat for synthesizer P-009 use, conditional on the
   schema not shifting under P-008. This is judgment-call territory
   (the spec does not explicitly request it), but the synthesizer
   originally asked for caveat language; providing a conditional
   draft unblocks P-009 partial work without committing the audit
   verdict. If the operator considers this overreach, the
   provisional caveat can be discarded with no impact on the verdict.
4. **TODAY_DATE = 2026-05-05** rather than the spec's candidate slot
   2026-05-06: the relay prompt explicitly allows "any slot before
   P-008 / P-009 fire", and the system date at session-start was
   2026-05-05. Using 2026-05-05 keeps the bridge folder consistent
   with actual session date.

## Anomalies and open questions

- **None at audit-verdict level.** No HALT triggered (H1–H6 all clear:
  no mutually-inconsistent multiple statements; no HARD_DEPENDENCY; no
  unauthorised post-2026-05-01 Phi draft; all sources A–J readable;
  pictures A and B byte-identical; provisional caveat free of
  forbidden AEAL verbs).
- **Operator-side note (not an anomaly):** the picture v1.18
  M9 gating amendment history records v1.15 as the moment M9 reduced
  unconditionally to {M4, M6} (with M8b excluded). The current verdict
  is consistent with that amendment: closed-form S_2 is not on the
  M9 critical path. If P-008 inadvertently introduces a closed-form
  S_2 dependency, that would *contradict* the v1.15 amendment and
  should trigger an immediate re-audit + picture v1.19 amendment.

## What would have been asked (if bidirectional)

- "If the verdict is `INDETERMINATE_NO_FORMAL_STATEMENT`, does the
  operator want me to draft a *minimal* Phi statement skeleton based
  on the umbrella v2.0 + CT v1.3 schemas as a non-binding starting
  point for P-008, or strictly defer all drafting to synthesizer?"
  Default chosen: defer (per Step 4.4 do-not-speculate clause).

## Recommended next step

1. Synthesizer fires P-008 (M9 V0 announcement draft, Sakai-1999
   template) using the umbrella v2.0 §4 Phi triple as substrate and
   the four CT v1.3 §"Implications" preconditions as the
   announcement's caveat backbone.
2. Once P-008 produces a formal `\begin{conjecture}[SIARC Master
   Conjecture v0]` environment, this audit is rerun in a single relay
   pass against the new statement-of-record. Expected re-verdict:
   SOFT_DEPENDENCY (if Stokes-data clause uses CT v1.3 phrasing) or
   NO_DEPENDENCY (if Phi clause stays at the triple-invariant level).
3. P-009 (M8b positioning) may use the provisional caveat above as a
   parsed starting point, with the explicit understanding that it is
   contingent on the P-008 draft remaining within the audited schema.

## Files committed (this session, local-only — no push)

- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/dependency_trace.md`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/verdict.json`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/claims.jsonl`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/halt_log.json`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/discrepancy_log.json`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/unexpected_finds.json`

## AEAL claim count

5 entries written to claims.jsonl this session (C1–C5).

## Push status

**LOCAL-ONLY.** Not pushed. Per spec Step 6: INDETERMINATE verdict →
"push as informational; flag P-008 as the next-action prerequisite."
Operator gates the actual `git push`.
