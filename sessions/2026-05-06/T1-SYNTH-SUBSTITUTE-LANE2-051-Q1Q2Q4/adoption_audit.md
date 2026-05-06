# Rubber-duck adoption audit — STEP 3

**Audit method:** For each of 8 rubber-duck findings (C1-C8) in
`rubber_duck_critique.md` per-finding adoption table, locate the
corresponding revision in `synth_substitute_verdict.md` and verify
landing.

**Verdict body anchor:** A1 SHA `AE5CC42A...041F` (read-only, this session).

---

## C1 — `cf_value()` finding scoped to PCF-2 R1.1/R1.3/Q1 specifically

**Rubber-duck Verdict:** YES (per `rubber_duck_critique.md` adoption table).

**Verdict-body landing:**
- L74: "**`PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT`** (scope: PCF-2 R1.1/R1.3/Q1 cubic+quartic harvest scripts)."
- L286-294: dedicated "Audited blind spots § Blind spot 1: PCF-1 may use a different convention" section addresses PCF-1 v1.3 separately, scoping the mismatch finding to PCF-2 v1.3 strictly.

**Status:** **ADOPTED_AND_LANDED** at L74 + L286-294.

---

## C2 — Sign correction for balance (III): `γ = -c_a/c_b`

**Rubber-duck Verdict:** YES.

**Verdict-body landing:**
- L137-141 (verbatim): "(III) `c_b/γ ↔ 1/γ²`: `d - μ = -2μ` ⇒ `μ = -d`,
  `γ = -c_a/c_b` ⇒ **`μ_sub = -d`, `γ_sub = -1/c_b`** for `c_a = 1`."
- The pre-revision draft (per rubber_duck_critique.md final section) had
  `γ = +1/c_b`; the post-revision verdict has `γ = -1/c_b`.

**LANE-2 cross-check:** Independent V6 derivation in `independent_substrate_verification.md`
yields the SAME sign: $\gamma_{\rm sub} \propto -c_a/c_b$ at leading order
(recessive root $r_+ < 0$ for positive $a_n, b_n$).

**Status:** **ADOPTED_AND_LANDED** at L137-141. Sign verified.

---

## C3 — Don't fully kill mechanism (ii'); leave audit-worthy

**Rubber-duck Verdict:** YES.

**Verdict-body landing:**
- L156-167 (verbatim): "Mechanism (ii') (definitional) **remains separately
  audit-worthy** as an operational-definition question, even after the
  protocol-to-stratum mismatch is resolved."
- Followed by a paragraph (L160-167) explaining why (ii') remains live
  via the convergent-residual fit-protocol question.
- Pre-revision draft phrasing per rubber_duck_critique.md final section
  was "neither (i') nor (ii') is realised" (absolute); post-revision is
  "Mechanism (i') likely unnecessary for harvested scripts; mechanism (ii')
  remains separately audit-worthy" (executive summary, L48).

**Status:** **ADOPTED_AND_LANDED** at L48 + L156-167. Pivot softened.

---

## C4 — Q4 ranking softened: canonical-target / operational-substitute

**Rubber-duck Verdict:** YES.

**Verdict-body landing:**
- L262 (verdict label): "**`WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE`**".
- L256-260: distinguishes "canonical sectorial-upgrade target" (Wasow §X.3 Theorem 11.1, 
  inaccessible via OCR gap) from "accessible-on-disk operational substitute" (Costin 2008
  ch.5 Borel-Laplace radius, on-disk at `tex/submitted/control center/literature/g3b_2026-05-03/06_costin_2008_chap5.txt`).
- Pre-revision label was "WASOW_PRIMARY_WITH_COSTIN_SECONDARY"; post-revision is the
  canonical-vs-substitute distinction by accessibility, not strength.

**Status:** **ADOPTED_AND_LANDED** at L262. Ranking re-cast.

---

## C5 — Three blind spots audited

**Rubber-duck Verdict:** YES.

**Verdict-body landing:**
- L283-310: "Audited blind spots" section.
- §Blind spot 1 (L286-294): PCF-1 v1.3 convention; cites
  `p12_journal_main.tex:128-136` (linear `a_n = δ n + ε`, `α, δ ≠ 0`)
  — distinct from PCF-2 R1.1/R1.3/Q1's `a_n ≡ 1`.
- §Blind spot 2 (L296-302): seed conditions `(p_{-1}, p_0, q_{-1}, q_0) = (1, b_0, 0, 1)`
  do not change the Newton-polygon balance.
- §Blind spot 3 (L304-310): "classifier mismatch" (rule5 label) vs
  "protocol-to-stratum mismatch" (rubber-duck-preferred label); verdict
  adopts protocol-to-stratum phrasing.

**Status:** **ADOPTED_AND_LANDED** at L283-310. All three blind spots audited.

---

## C6 — AEAL forbidden-verb hygiene

**Rubber-duck Verdict:** YES (Fix: use softer phrasings).

**Verdict-body audit (LANE-2 grep scan):**

Forbidden verb pattern: `\b(shows|confirms|proves|establishes|must)\b` and
`matching empirical EXACTLY`.

**Matches found in verdict body (excluding meta-discussion):**

| Line | Match | Context | Verdict |
|------|-------|---------|---------|
| L221 | "confirms" | "if sub-task 3-A **confirms** the protocol-to-stratum mismatch finding, Q2 closes as MOOT" | **ACCEPTABLE** — conditional/gating logic, NOT prediction-or-conjecture context (the "confirms" verb describes a future hypothetical audit outcome, not a current claim about empirical reality). |
| L339 | "confirms" | "rubber-duck cross-check on session_b_pslq.py:162-168 and quartic_tail_fit_all60.py:21-30 **confirms** same pattern across the harvest set" | **ACCEPTABLE** — describes a script-inspection factual finding (mechanical match), not a prediction. The pattern IS literally identical across all three scripts (verified independently in V2). |
| L351 | "shows", "confirms", "proves" | "The verdict avoids 'shows', 'confirms', 'proves' in prediction-or-conjecture context." | **ACCEPTABLE** — meta-discussion declaring avoidance, not predicate use. |

**No matches:** "establishes", "must", "matching empirical EXACTLY".

**Pre-revision draft per rubber_duck_critique.md final section had:**
"correctly predicts", "matching exactly", "gap is artefact",
"neither (i') nor (ii') is realised". All four softened in the
post-revision verdict.

**Status:** **ADOPTED_AND_LANDED**. Forbidden verbs absent from
prediction-or-conjecture context. C2 of HALT_061_AEAL_FORBIDDEN_VERB_FOUND
does NOT trigger.

---

## C7 — Defer to canonical T1-Synth re-arbitration

**Rubber-duck Verdict:** YES.

**Verdict-body landing:**
- L386-396: dedicated section "Recommended canonical T1-Synthesizer follow-up (W20, Mon 2026-05-11)" with 6 specific items for canonical assent.
- Section opens (L387-389): "This synthesizer-substitute verdict is operator-authorized but
  **explicitly deferred for canonical T1-Synthesizer re-arbitration** at the next ISO week
  (W20, beginning Mon 2026-05-11)."

**Status:** **ADOPTED_AND_LANDED** at L386-396. Six follow-up items enumerated (the basis for STEP 5 of this LANE-2 review).

---

## C8 — Split confidence reporting

**Rubber-duck Verdict:** YES.

**Verdict-body landing:**
- L327-340: "Confidence assessment (per rubber-duck split recommendation)" section.
- Table with 5 rows. Distinct confidence levels present:
  - HIGH (2 rows: script-protocol mismatch + WZ plug-in)
  - MEDIUM-HIGH (2 rows: §5 reframing + Wasow/Costin Q4 ranking)
  - MEDIUM (1 row: PCF-1 / picture v1.20 / scope wording implications)

**Distinct levels: 3 (HIGH, MEDIUM-HIGH, MEDIUM).** Meets the ≥3-level
floor specified by the relay 061 prompt for C8 verification.

**Status:** **ADOPTED_AND_LANDED** at L327-340. Three distinct levels present.

---

## Aggregate adoption record

| Finding | Rubber-duck verdict | Verdict-body landing line(s) | Adoption status |
|---------|---------------------|------------------------------|-----------------|
| C1 — scope to PCF-2 R1.1/R1.3/Q1 | YES | L74, L286-294 | ADOPTED_AND_LANDED |
| C2 — sign $\gamma = -c_a/c_b$ | YES | L137-141 | ADOPTED_AND_LANDED |
| C3 — don't fully kill (ii') | YES | L48, L156-167 | ADOPTED_AND_LANDED |
| C4 — Q4 canonical-target / operational-substitute | YES | L262, L256-260 | ADOPTED_AND_LANDED |
| C5 — three blind spots | YES | L283-310 | ADOPTED_AND_LANDED |
| C6 — AEAL forbidden-verb hygiene | YES | absent (zero violations in prediction context) | ADOPTED_AND_LANDED |
| C7 — defer to canonical T1-Synth | YES | L386-396 | ADOPTED_AND_LANDED |
| C8 — split confidence | YES | L327-340 (3 levels) | ADOPTED_AND_LANDED |

**Aggregate:** 8 of 8 ADOPTED_AND_LANDED. 0 of 8 NOT_ADOPTED. 0 of 8 ADOPTED_BUT_INCOMPLETE.

**HALT_061_AEAL_FORBIDDEN_VERB_FOUND:** does NOT trigger (C6 PASS).
