# Portfolio inventory — 5-record × 3-endorser endorsement-chain consolidation

**Compiled:** 2026-05-04 ~18:00 JST
**Bridge session:** `sessions/2026-05-04/ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE/`
**Verdict:** `COMPLETE_INVENTORY_READY_FOR_OPERATOR_REVIEW`
**Source verdicts cross-referenced:** 034 ARXIV-MIRROR-RUNBOOK-REFIRE (6 templates) + 037 ARXIV-ENDORSEMENT-TEMPLATES-EXPAND (9 templates) = **15 templates total**.

---

## arXiv policy reality reminder

Per arXiv policy update **2025-12-10** (synthesizer-Claude verified
2026-05-04 ~17:55 JST against `blog.arxiv.org` 10 December 2025
post), auto-endorsement now requires **(1) institutional email
AND (2) prior arXiv math authorship**. Operator (independent
researcher, Yokohama, no institutional email, no prior arXiv math
authorship) meets neither — **all 5 records require personal
endorsement from established arXiv authors**.

Per arXiv help text, endorsement is granted **per category**: a
positive endorsement grants submission privileges in the endorser's
matched category for the operator's first submission, and once
**any** SIARC paper has landed on arXiv, the conversation
materially changes (independent researcher with arXiv presence
asking for a new-category endorsement vs first-time submitter
with no priors). The first endorsement is therefore strategically
load-bearing: subsequent endorsement requests for the remaining
4 records are categorically easier.

**Cross-listing note.** Cross-listed records may be endorsed by
anyone with privileges in **any** of the listed categories
(primary or cross). This widens the eligible-endorser pool for
multi-category records.

---

## DOI-consistency cross-check (spec §1 step 2)

All 5 records' concept and version DOIs verified consistent
across three independent sources:

| Record | Source: cheat-sheet (line) | Source: submission_log (count) | Source: 034 zenodo_metadata |
|---|---|---|---|
| umbrella v2.0 (concept 19885549, v2.0 19965041) | L38 ✓ | 4 + 5 ✓ | L9, L13-14 ✓ |
| PCF-1 v1.3 (concept 19931635, v1.3 19937196) | L40 ✓ | 4 + 9 ✓ | L26-27, L30-31 ✓ |
| PCF-2 v1.3 (concept 19936297, v1.3 19963298) | L41 ✓ | 7 + 7 ✓ | L46-47, L50-51 ✓ |
| Channel Theory v1.3 (concept 19941678, v1.3 19972394) | L42 ✓ | 9 + 3 ✓ | L64-65, L68-69 ✓ |
| T2B v3.0 (concept 19783311, v3.0 19915689) | L44 ✓ | 2 + 3 ✓ | L81-82, L85-86 ✓ |

**Result:** all 10 DOIs (5 records × {concept, version}) are
consistent across all 3 sources. **No `HALT_ENDORSEMENT_INVENTORY_DOI_INCONSISTENCY`** triggered.

---

## Master inventory table

| # | Label | Title | Concept DOI | Version DOI | arXiv primary (cross) | Endorser 1: Zudilin (fit) | Endorser 2: Mazzocco (fit) | Endorser 3: Garoufalidis (fit) | Anomalies |
|---|---|---|---|---|---|---|---|---|---|
| 1 | umbrella v2.0 | An Arithmetic Stratification of Polynomial Continued Fractions — v2.0 (Modular-Discriminant Framing) | 10.5281/zenodo.19885549 | 10.5281/zenodo.19965041 | math.HO | M (math.NT adjacency) | M (math-ph / Painlevé adjacency) | M (math.NT/math.GT/math.CA breadth) | none |
| 2 | PCF-1 v1.3 | Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions | 10.5281/zenodo.19931635 | 10.5281/zenodo.19937196 | math.NT (math.CA) | H (math.NT primary) | H (math.CA cross) | H (math.NT match) | none |
| 3 | PCF-2 v1.3 | PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant Transcendence Predicate | 10.5281/zenodo.19936297 | 10.5281/zenodo.19963298 | math.NT (math-ph) | H (math.NT primary) | H (math-ph cross) | H (math.NT match) | none |
| 4 | CT v1.3 | Channel Theory for Polynomial Continued Fractions: Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture | 10.5281/zenodo.19941678 | 10.5281/zenodo.19972394 | math-ph (math.DS, math.NT) | H (math.NT cross) | H (math-ph primary) | H (math.NT cross + Garoufalidis-Costin resurgence cite) | none |
| 5 | T2B v3.0 | Two arithmetic classes of degree-(2,1) Trans-stratum continued fractions: a Birkhoff–Trjitzinsky / Gauss-continued-fraction dichotomy | 10.5281/zenodo.19783311 | 10.5281/zenodo.19915689 | math.HO (math.NT) | H (math.NT cross) | M (Painlevé/asymptotic adjacency; math.NT cross-judgement plausible) | H (math.NT cross) | none |

**Fit distribution:**

|  | Zudilin | Mazzocco | Garoufalidis | Total |
|---|---|---|---|---|
| H (HIGH) | 4 | 3 | 4 | 11 |
| M (MODERATE) | 1 | 2 | 1 | 4 |
| L (LOW) | 0 | 0 | 0 | 0 |
| **per-endorser total** | **5** | **5** | **5** | **15** |

- 034 sub-distribution (records 2 + 3 = PCF-1 + PCF-2): 6H + 0M + 0L (every cell H since math.NT primary aligns directly with Zudilin/Garoufalidis primary and PCF-1/PCF-2 each cross-list to a Mazzocco-primary class — math.CA / math-ph respectively).
- 037 sub-distribution (records 1 + 4 + 5 = umbrella + CT + T2B): 6H + 3M + 0L (per 037's `subject_fit_matrix.md`).
- **Combined: 12H + 3M + 0L; no L cells; no record falls under `HALT_NO_SUBJECT_FIT_FOR_RECORD`.**

---

## Template inventory (15-row enumeration)

| # | Record | Endorser | Source session | Filename | Body addresses | Body DOI | DOI matches filename? |
|---|---|---|---|---|---|---|---|
| T01 | umbrella v2.0 | Zudilin | 037 | `endorsement_template_umbrella_v2.0_zudilin.md` | umbrella v2.0 (math.HO) | 10.5281/zenodo.19965041 | ✓ |
| T02 | umbrella v2.0 | Mazzocco | 037 | `endorsement_template_umbrella_v2.0_mazzocco.md` | umbrella v2.0 (math.HO) | 10.5281/zenodo.19965041 | ✓ |
| T03 | umbrella v2.0 | Garoufalidis | 037 | `endorsement_template_umbrella_v2.0_garoufalidis.md` | umbrella v2.0 (math.HO) | 10.5281/zenodo.19965041 | ✓ |
| T04 | PCF-1 v1.3 | Zudilin | 034 | `endorsement_template_pcf1_v1.3_zudilin.md` | PCF-1 v1.3 (math.NT, math.CA cross) | 10.5281/zenodo.19937196 | ✓ |
| T05 | PCF-1 v1.3 | Mazzocco | 034 | `endorsement_template_pcf1_v1.3_mazzocco.md` | PCF-1 v1.3 | 10.5281/zenodo.19937196 | ✓ |
| T06 | PCF-1 v1.3 | Garoufalidis | 034 | `endorsement_template_pcf1_v1.3_garoufalidis.md` | PCF-1 v1.3 | 10.5281/zenodo.19937196 | ✓ |
| T07 | PCF-2 v1.3 | Zudilin | 034 | `endorsement_template_pcf2_v1.3_zudilin.md` | PCF-2 v1.3 (math.NT, math-ph cross) | 10.5281/zenodo.19963298 | ✓ |
| T08 | PCF-2 v1.3 | Mazzocco | 034 | `endorsement_template_pcf2_v1.3_mazzocco.md` | PCF-2 v1.3 | 10.5281/zenodo.19963298 | ✓ |
| T09 | PCF-2 v1.3 | Garoufalidis | 034 | `endorsement_template_pcf2_v1.3_garoufalidis.md` | PCF-2 v1.3 | 10.5281/zenodo.19963298 | ✓ |
| T10 | CT v1.3 | Zudilin | 037 | `endorsement_template_ct_v1.3_zudilin.md` | CT v1.3 (math-ph; math.DS, math.NT cross) | 10.5281/zenodo.19972394 | ✓ |
| T11 | CT v1.3 | Mazzocco | 037 | `endorsement_template_ct_v1.3_mazzocco.md` | CT v1.3 | 10.5281/zenodo.19972394 | ✓ |
| T12 | CT v1.3 | Garoufalidis | 037 | `endorsement_template_ct_v1.3_garoufalidis.md` | CT v1.3 | 10.5281/zenodo.19972394 | ✓ |
| T13 | T2B v3.0 | Zudilin | 037 | `endorsement_template_t2b_v3.0_zudilin.md` | T2B v3.0 (math.HO, math.NT cross) | 10.5281/zenodo.19915689 | ✓ |
| T14 | T2B v3.0 | Mazzocco | 037 | `endorsement_template_t2b_v3.0_mazzocco.md` | T2B v3.0 | 10.5281/zenodo.19915689 | ✓ |
| T15 | T2B v3.0 | Garoufalidis | 037 | `endorsement_template_t2b_v3.0_garoufalidis.md` | T2B v3.0 | 10.5281/zenodo.19915689 | ✓ |

**Result:** 15/15 templates have body DOI matching filename
record-label. **No `HALT_ENDORSEMENT_INVENTORY_TEMPLATE_COUNT_MISMATCH`** triggered.

---

## Endorser dossier (Tier-1 candidates)

| Endorser | Affiliation (per ENDORSER-HANDLE-ACQUISITION 2026-05-04) | Verified institutional email | arXiv handle | Primary subject areas |
|---|---|---|---|---|
| **Wadim Zudilin** | Professor of Pure Mathematics, IMAPP, Radboud University Nijmegen | `w.zudilin@math.ru.nl` (verified 2026-05-04 ~17:50 JST against `math.ru.nl/~zudilin/` + `ru.nl/en/people/zudilin-v`) | `zudilin_w_1` | math.NT (transcendence, irrationality measures, continued fractions) |
| **Marta Mazzocco** | University of Birmingham (per 034 ENDORSER-HANDLE-ACQUISITION; operator should re-verify at send time per academic-mobility caveat) | placeholder (operator confirms institutional homepage) | `mazzocco_m_1` (per template default) | math.CA, math-ph, math.QA, math.AG (Painlevé equations, monodromy manifolds) |
| **Stavros Garoufalidis** | Southern University of Science and Technology (SUSTech), Shenzhen (per 034 ENDORSER-HANDLE-ACQUISITION) | placeholder (operator confirms institutional homepage) | `garoufalidis_s_1` (per template default) | math.GT, math.NT, math.CA (quantum topology, knot invariants, Bloch group, resurgence of Kontsevich-Zagier power series) |

**Email verification status:**

- Zudilin: pre-verified by synthesizer-Claude 2026-05-04 ~17:50 JST.
  Send-ready draft at
  `sessions/2026-05-04/ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE/endorsement_send_draft_pcf1_v1_3_zudilin.md`
  (bridge commit `bee90dc`).
- Mazzocco: not yet pre-verified; operator confirms at send time
  per template `{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}`
  placeholder pattern + applicable SOP `Bibliographic identifier
  pre-verification (lit-hunt prompts)` standing-rule (commit
  `7fbe30d` / workspace `79e7a22`).
- Garoufalidis: not yet pre-verified; operator confirms at send
  time per same pattern.

---

## Anomaly check results

### Step 5 — Zudilin Newcastle stale-address check

**Result: NEGATIVE** (synthesizer's premise falsified).

Full-text grep of both Zudilin templates (PCF-1 + PCF-2) at the
034 session for `newcastle` / `wadim.zudilin` / `@newcastle`:
**ZERO matches**. Both templates use the placeholder
`{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}` on line 22.
The 034 author had already implemented the placeholder-pattern
that the spec was attempting to enforce.

**`ADDRESS_FLAGGED_STALE_NEWCASTLE` count: 0.**

### Step 6 — Filename consistency check

**Result: NEGATIVE** (no filename anomalies; spec's framing was
based on a synthesizer-misread of the 034 inventory).

The 034 session contains TWO Zudilin templates, not one:

- `endorsement_template_pcf1_v1.3_zudilin.md` (4,923 B; body
  cites DOI 19937196 = PCF-1 v1.3) ✓
- `endorsement_template_pcf2_v1.3_zudilin.md` (4,927 B; body
  cites DOI 19963298 = PCF-2 v1.3) ✓

Body matches filename in both cases. The synthesizer's "filename
PCF-1 vs PCF-2 mismatch" framing assumed a single Zudilin template
existed; the actual inventory contains correctly-named
PCF-1-and-PCF-2 templates. Same body/filename consistency holds
for all 6 PCF templates from 034 and all 9 templates from 037
(15/15 ✓ — see template inventory table above).

**`FILENAME_ANOMALIES` count: 0.**

### Other observations

- Mazzocco affiliation may need re-verification at send time
  (academic-mobility caveat from 034 handoff anomaly #3).
- Mazzocco institutional email and Garoufalidis institutional
  email both still need pre-verification per the standing-rule
  SOP; this should be done before either of those endorsement
  emails fires.
- 034 handoff anomaly #2 noted that ALL 5 records require
  endorsement (not just records 2+3 as 002 originally specified).
  034's templates cover only PCF-1 + PCF-2; 037 closed the
  remaining 3 records (umbrella, CT, T2B) — combined coverage is
  now complete (15 templates × 5 records).

---

## Operator decision prompt (deferred to operator + synthesizer)

The following sequencing decisions are **operator-side** (per
spec §4 OUT OF SCOPE; synthesizer-side recommendation available
on separate-turn request, but not produced in this inventory):

1. **Which record leads the chain?** All 5 records have ≥3
   templates with H or M fit ratings; no record forces
   sequencing on its own merits. Strategic considerations:
   - First-endorsement-as-pivot: any positive endorsement on
     ANY math-cluster category eases subsequent endorsement
     requests across all categories. Record with lowest-friction
     send-target (Zudilin pre-verified) + highest-fit endorser
     pool may be the natural lead.
   - Operator's own ordering preference (e.g., publication
     priority, narrative-coherence with the SIARC stack) may
     trump fit-rating alone.
   - Note: Zudilin draft for **PCF-1 v1.3** is already
     send-ready at `sessions/2026-05-04/ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE/`.
     If operator's chosen lead is PCF-1 v1.3, send-action is
     unblocked immediately; if a different record leads,
     operator dispatches a sibling
     `*-ENDORSEMENT-DRAFT-FINALIZE` task for that record's
     chosen endorser-template pair.

2. **Which endorser within the leading record's 3-candidate
   slate is contacted first?** All three (Zudilin, Mazzocco,
   Garoufalidis) have non-L fit across all 5 records. Operator
   considers personal academic familiarity, response-rate
   priors, and topical-fit-judgement comfort.

3. **Wait-window between sends.** Per arXiv etiquette
   (`info.arxiv.org/help/endorsement.html`): do **not** email
   large numbers of endorsers at once or repeat-email the same
   endorser. Strict-sequence (one endorser at a time, with
   reasonable wait window before approaching the next if no
   reply) is the canonical-clean pattern. Operator decides
   wait-window length.

These three decisions are **NOT made in this inventory** — this
file is data-pull-only per operator request (spec §4).
Synthesizer-side sequencing recommendation is available on
separate-turn request.

---

## AEAL-claim summary (this session)

- 6 AEAL claims emitted to `claims.jsonl`:
  - `endorsement_inventory_consolidated` — 15 templates × 5 records cross-referenced
  - `arxiv_policy_post_dec2025_acknowledged` — auto-endorsement requirements documented
  - `zudilin_address_stale_newcastle_NULL_finding` — synthesizer premise falsified
  - `template_filename_body_consistency_15_of_15` — all 15 templates internally consistent
  - `doi_consistency_5_records_3_sources` — all 10 DOIs match across 3 sources
  - `endorser_email_pre_verification_status` — Zudilin verified; Mazzocco + Garoufalidis pending operator-side

- 0 halts triggered.
- 0 anomalies surfaced (both spec-expected anomalies returned
  null findings; both checks documented in claims.jsonl as
  null-finding records).

---

**End of inventory. Operator next-step: review 5×3 master table +
endorser dossier, decide leading-record + first-endorser-contact +
wait-window. Synthesizer arbitration available on separate request.**
