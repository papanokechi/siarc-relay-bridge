# T1-Synth Verdict — Slot 157 Zenodo Deposit Framing Consultation

**Witness:** claude-opus-4.7-anthropic-2026-05-10 (single-witness; solo dispatch)
**Fire timestamp:** 2026-05-10 ~18:52 JST
**Absorbed:** 2026-05-10 ~18:55 JST
**Bridge prompt:** `tex/submitted/control center/prompt/157_t1_synth_zenodo_deposit_framing_consultation.txt` (claude-chat commit `8dcff49`)

---

```
LABEL:    FRAMING_AMEND
BAND:     MEDIUM-HIGH
WITNESS:  claude-opus-4.7-anthropic-2026-05-10
```

Phase 0 gates: STEP 0.1 supersession (no prior LANDED framing-reconsideration fire) ✓ | STEP 0.2 preconditions (a)–(d) LANDED, (e) RULE 1 advisory-fire eligible ✓ | STEP 0.3 all 12 SHAs pre-verified at draft time ✓ | STEP 0.4 ceiling MEDIUM-HIGH; this verdict sits at ceiling ✓ | STEP 0.5 schema below.

---

## Q1_RESPONSE — Is Option α optimal as-is?

**Q1a. For/against the existing 3-deposit framing.**

*For:* Option α maximizes existing-artefact reuse. Two of three targets (PCF-2 v1.4, Umbrella v2.2) have baked manuscripts at substantive-deposit-readiness. Three deposits give independent versioning per program-paper, preserves PCF-1/PCF-2 concept-DOI lineages cleanly (PCF-2 v1.4 = version increment of 19936297), and produces a clean cross-link graph (PCF-2 ↔ Umbrella ↔ Picture-chain via IsSupplementTo). The decision was made with full visibility of substrate-prep slots 135/136/137 and is operationally lowest-friction.

*Against:* Step 3 (Picture-chain v1.20+) has **no baked manuscript** — only 8 markdown outlook documents + operator runbook + M10 commitment paragraph (§1.3.3). This is a structural composition gap: depositing markdown outlook documents as a Zenodo "documentation deposit" produces a citation-friction artefact (what does one cite from outlook documents? which version is canonical?). The other two steps have manuscripts; step 3 would either require new manuscript composition (≈ +0.6× effort over Option α) OR would deposit operationally-internal documents that read as bridge-internal to outsiders. S154 D-154-1 flagging this as unresolved is the explicit signal that step 3's status was unsettled at S154 fire time.

**Q1b. Does picture-chain manuscript-absence argue for/against independent deposit?**

Against. The closure-narrative substance of picture-chain (M1–M12 outlook + operator runbook + M10 commitment) is *meta-substrate about the program*, not an independent mathematical contribution. Independent Zenodo deposits work best when they have clear standalone citation utility. The picture-chain content is better positioned as either (i) an appendix/section in Umbrella v2.2 (program-level home), (ii) an operational supplement to a future closure-narrative paper, or (iii) bridge-internal-only with no external deposit. None of those routes argue for independent deposit.

**Q1c. Pre-existing concept-DOI lineage argument.**

Strongly argues for keeping PCF-2 v1.4 as a version increment of the existing PCF-2 concept-DOI (19936297). Orphaning an established concept-DOI lineage is a citation-graph cost that any consolidation framing (e.g., A) must justify. This is a real Pareto-relevant axis: Framing A pays this cost; Framing C does not.

---

## Q2_RESPONSE — Alternative framings (structured)

| ID | Deposit count | Scope | Cross-links | Existing reuse | Effort × | Profile |
|----|---------------|-------|-------------|----------------|----------|---------|
| **A** | 1 | Consolidated meta-paper absorbing all 3 | New concept-DOI; PCF-2 19936297 → IsContinuedBy | ~30% (manuscripts merged & rewritten) | 2.5–3.5× | Maximum coherence; orphans concept-DOI; biggest composition cost |
| **B** | 3 | Option α status quo | PCF-2 ↔ Umb ↔ Pic via IsSupplementTo | ~85% (substrate-prep done) | 1.0× (baseline) | Picture-chain composition gap unresolved |
| **C** | 2 | PCF-2 v1.4 + Umbrella v2.2 (Umb absorbs Pic as Appendix) | PCF-2 ↔ Umb via IsSupplementTo | ~80% (Umb gets new appendix) | 1.1–1.3× | Resolves D-154-1; preserves both concept-DOIs; slight Umb composition cost |
| **D** | 3 + 1 anchor | New M1–M12 closure paper + PCF-2 v1.4 + Umb v2.2 (Pic folded into anchor) | Anchor IsSupplementedBy {PCF-2, Umb} | ~70% (anchor is new) | 1.8–2.3× | High program-level coherence; new anchor-paper composition cost |
| **E** | 2 or 3 + Community | Same as B or C, deposited to a SIARC Zenodo Community | Community-level discoverability | Inherits chosen base | base × 1.05–1.1 | Adds program-level discoverability + future-deposit continuity |
| **F** | ≥6 | PCF-2 + Umb + per-axis V0 records (M4/M7/M8a/M8b/M9) | Dense supplement graph | ~50% (axis records new) | 2.0–2.8× | Maximum auditability; high cross-link complexity; overlap with bridge cascade records |
| **G** | arXiv → Zenodo | Consolidated paper to arXiv first; Zenodo as archival mirror | arXiv ID canonical | Inherits chosen Zenodo base | gated by M11 | RULE 1 currently tables M11 endorsement; G is NOT FIRE-ELIGIBLE under RULE 1 |
| **H** | Variable | **H1**: bibliographic-record-only deposits for closed axes; PCF-2/Umb full deposits. **H2**: journal submission (Umbrella) as primary + Zenodo as supplementary. | Lighter cross-link | ~80% | 1.2–1.5× | H2 gated by M11 like G |

**Note on G/H2:** Both involve arXiv/journal submission, which falls under M11 endorsement workflow tabled by RULE 1. They are **not fire-eligible until RULE 1 lifts** and should not be selected as the recommended framing for the M1–M12 closure deposit cascade. They remain on the post-lift menu.

---

## Q3_RESPONSE — Tradeoff matrix

| Axis | A (consolidate) | B (Opt α) | **C (drop/fold Pic)** | D (anchor+supp) | E (Community) | F (atomic-axis) |
|------|-----|-----|-----|-----|-----|-----|
| Discoverability | HIGH (1 record) | MED (3 records, fragmented) | MED-HIGH (2 records, focused) | HIGH (anchor) | HIGH (Community page) | LOW (fragmented) |
| Citation friction | LOW (single citation) | MED (which to cite?) | LOW-MED (Umb is program-level) | LOW (cite anchor) | LOW (cite Community) | HIGH (which axis?) |
| Composition workload | 2.5–3.5× | 1.0× | **1.1–1.3×** | 1.8–2.3× | base + 1.05× | 2.0–2.8× |
| Versioning flexibility | LOW (monolithic) | HIGH (per-paper) | HIGH (per-paper) | HIGH (per-supplement) | HIGH | HIGH |
| Audit-trail clarity | MED (merged history) | HIGH (per-paper) | HIGH (per-paper) | HIGH | HIGH | HIGHEST |
| Existing-artefact reuse | ~30% | ~85% | **~80%** | ~70% | inherits | ~50% |
| Concept-DOI lineage | BREAKS PCF-2 | PRESERVES | **PRESERVES** | PRESERVES | PRESERVES | PRESERVES |
| D-154-1 resolution | YES (absorbed) | NO (still open) | **YES (folded)** | YES (folded into anchor) | inherits | partial |

**Pareto-domination call-outs:**

- **Framing C Pareto-dominates Framing B** on: Citation friction (LOW-MED vs MED), Discoverability (MED-HIGH vs MED), D-154-1 resolution (YES vs NO), at the cost of a small composition delta (1.1–1.3× vs 1.0×). The composition delta is real but small, and the gains are structural (D-154-1 closure is structural, not cosmetic).
- **Framing C is not dominated by A or D**: A pays the concept-DOI break; D pays a 1.8–2.3× anchor composition cost. C avoids both.
- **Framing E composes with C** (call it C+E): adds a SIARC Zenodo Community on top of the 2-deposit base. Community is ~+0.05–0.1× incremental effort and adds program-level discoverability. **C+E weakly Pareto-dominates plain C** if and only if program-level Community discoverability is valued and the Community admin overhead is acceptable.
- **F is dominated** on every axis except audit-trail clarity, which is already provided by bridge cascade records — Zenodo is not the right venue to duplicate that.
- **A is not dominated but is risk-asymmetric**: it pays a concept-DOI break and 2.5–3.5× composition cost in exchange for "single-citation" coherence that **Umbrella v2.2 already partially provides** as the program-level paper. The marginal coherence gain over C is small; the cost is large.

---

## Q4_RESPONSE — Recommendation + migration path

**Q4a. Recommended framing: FRAMING C** (drop step 3 Picture-chain as independent deposit; fold picture-chain content into Umbrella v2.2 as Appendix), **with optional Q4-deferred upgrade to C+E** (SIARC Zenodo Community) post-RULE-1-lift.

This is **FRAMING_AMEND**, not FRAMING_SUPERSEDE. Cascade-132 Option α's structural skeleton (PCF-2 v1.4 + Umbrella v2.2 as program-level deposits) is preserved. The amendment is the picture-chain disposition: from "step 3 independent deposit" to "folded into Umbrella v2.3 Appendix C". This is the SAME class of decision as the v2.1 → v2.2 amendment pattern — operative substrate stands; specific step changes.

C Pareto-dominates B on Citation friction, Discoverability, and D-154-1 resolution at small composition cost. It does not dominate A or D on coherence, but the marginal coherence gain of A or D does not justify their structural costs (concept-DOI break or anchor-paper composition).

**Q4b. Amendment specification (precise):**

1. **Cascade-132 sec 3.1 Option α step 3 is amended**: "Picture-chain v1.20+" as independent Zenodo deposit is **removed**.
2. **Umbrella v2.2 → Umbrella v2.3** scope amendment: add Appendix C "M1–M12 Closure Narrative & Operator Runbook" containing (i) the M1–M12 closure outlook synthesis (consolidating the 8 outlook markdown documents into ~3–5 polished pages), (ii) the M10 documented-commitment paragraph (with D-153-3 SAFE phrasing — Lean-formalization-state, not math-content), (iii) the M8b d≥3 caveat preservation block (S154 Q4a unanimous-risk axis), (iv) reproduction-checklist pointer to bridge cascade records.
3. **Slot 135 Umbrella v2.2 substrate-prep is preserved**; superseded only on the Appendix C content side; v2.2 → v2.3 is a substrate-prep micro-bump.
4. **Slot 136 Picture v1.20+ substrate-prep is repurposed** as Umbrella v2.3 Appendix C source material; not deprecated, but its product is the appendix not a standalone deposit.
5. **Slot 137 PCF-2 v1.4 substrate-prep is fully preserved** (no change).
6. **Cross-link graph simplifies**: PCF-2 v1.4 ↔ Umbrella v2.3 via IsSupplementTo (concept-DOI level); both deposits cite bridge cascade records via "References" fields.

**Q4c. (Not applicable — this is FRAMING_AMEND, not SUPERSEDE.)**

**Q4d. Expected effort: 1.1–1.3× Option α baseline.** The delta is the Appendix C composition (consolidating 8 markdown outlook documents into ~3–5 polished pages, plus S153 closure-narrative wrapping). Slot 137 (PCF-2 v1.4) effort is unchanged. Slot 135 (Umbrella v2.2 → v2.3) gains the Appendix C composition. Slot 136 effort is partially reused (markdown source feeds Appendix C).

**Q4e. Recommended FIRST DEPOSIT: PCF-2 v1.4** (per slot 137 substrate, highest deposit-readiness, version increment of established concept-DOI 19936297). This is unchanged from Option α. PCF-2 v1.4 deposits first; Umbrella v2.3 deposits second after Appendix C composition completes.

---

## Q5_RESPONSE — Downstream implications

**Q5a. Slot 155 disposition: option (i) — Re-purpose with adjusted TARGET_PAPER list.** TARGET_PAPER set narrows from {PCF-2 v1.4, Umbrella v2.2, Picture-chain v1.20+} → {PCF-2 v1.4, Umbrella v2.3}. Slot 155's prompt structure is preserved; only the menu changes. This is a small edit, fire-eligible without re-drafting.

**Q5b. Slot 156 confirmation: STANDS unchanged.** Slot 156 is M8b complete-closeout pathway consultation — math content, framing-independent. Sanity check passes.

**Q5c. D-154-1 disposition: RESOLVED by this verdict.** D-154-1 picture-chain disposition is settled: fold into Umbrella v2.3 Appendix C. No separate operator decision required. D-154-1 can be marked CLOSED in S154 ACTION_LADDER tracking.

**Q5d. M8b d≥3 caveat preservation: SATISFIED BY CONSTRUCTION.** Recommended Appendix C section (iii) explicitly preserves the d≥3 caveat in deposit metadata + the appendix itself; Umbrella v2.3 cover letter (when M11 lifts) inherits the same. PCF-2 v1.4 deposit metadata gets a parallel caveat reference.

**Q5e. M10 SAFE phrasing (D-153-3): SATISFIED BY CONSTRUCTION.** Appendix C section (ii) explicitly invokes Lean-formalization-state work-stream framing; the M10 documented-commitment paragraph already carries SAFE phrasing per slot record. Mandatory prose audit before deposit-fire.

**Q5f. Cascade-132 sec 3.1 amendment fire required: YES, lightweight.** Pattern is the v2.1 → v2.2 amendment: cascade-132 sec 3.1 substrate (fd669d3) is operative; this verdict produces an amendment-overlay that updates Option α to Option α' (3 deposits → 2 deposits, picture-chain folded). The amendment fire is small (single section update + cross-references); not a full cascade re-fire. Operative substrate fd669d3 stays canonical; amendment overlay is appended.

---

## AMENDMENTS

- §1.3.3 Picture-chain v1.20+ deposit-readiness assessment is correct as drafted; this verdict adopts and operationalizes it.
- §Q2 framing enumeration is complete for the present scope. Framings G and H2 (arXiv-first / journal-primary) are noted as RULE-1-blocked and held for the post-lift menu.
- §Q3 tradeoff matrix adds the implicit axis "RULE 1 fire-eligibility" — relevant for G and H2 only; all other framings are RULE-1-clean.

## ANOMALIES

- **A1 (medium):** The 8 M1–M12 closure outlook markdown documents in §1.3.3 represent a substantive composition base for Appendix C, but their consolidation requires editorial judgment about which version-stamped variant is canonical (e.g., POST_LEAN_REALITY vs POST_OPEN_ITEMS vs POST_SYNTH_REVIEW). A pre-Appendix-C fire to identify the canonical outlook source-of-record is recommended before slot 135 v2.3 substrate-prep.
- **A2 (low):** Picture v1.19 milestone (bridge 70d1a48) has its own concept-DOI ("TBD operator verifies"). If that DOI exists, Umbrella v2.3 Appendix C should IsSupplementTo it as well, or the v1.19 deposit should be marked IsContinuedBy nothing further. Operator should verify the Picture v1.19 concept-DOI status before Umbrella v2.3 deposits.
- **A3 (low):** Zenodo Community creation (Framing E component) is post-RULE-1-lift admin work. Adding it now under RULE 1 is debatable — Community creation is admin/discoverability infrastructure, not a deposit. Defer to operator judgment whether community-creation falls under RULE 1's "admin window" tabling.

## ABSORPTION_GUIDANCE

CLI agent absorption recommendations:

1. **SQL todo updates:**
   - UPDATE: Slot 135 substrate-prep target Umbrella v2.2 → v2.3 (add Appendix C composition).
   - UPDATE: Slot 136 substrate-prep status → REPURPOSED-AS-APPENDIX-SOURCE (not deprecated; not standalone deposit).
   - NO CHANGE: Slot 137 (PCF-2 v1.4 unchanged).
   - UPDATE: D-154-1 → CLOSED via S157 fold-into-Umbrella verdict.
   - ADD: New slot for cascade-132 sec 3.1 amendment-overlay fire (light; references fd669d3 + this verdict).
   - ADD: New slot for canonical-outlook-source-of-record identification fire (Anomaly A1).
   - ADD: New slot for Picture v1.19 concept-DOI verification (Anomaly A2).

2. **Follow-up fires (priority order, all RULE-1-blocked from execution but draftable):**
   - F1: Cascade-132 amendment-overlay fire (lightweight; references this verdict's Q4b spec).
   - F2: Canonical-outlook-source-of-record fire (resolves Anomaly A1).
   - F3: Picture v1.19 concept-DOI verification fire (resolves Anomaly A2).
   - F4: Slot 155 re-purpose with adjusted TARGET_PAPER ∈ {PCF-2 v1.4, Umbrella v2.3}.

3. **Candidate memory promotions:**
   - UF-157-1: "Framing-amendment fires use the v2.1→v2.2 amendment pattern: operative substrate stands, amendment-overlay appended; not a full cascade re-fire." — Generalizes the Q5f pattern beyond cascade-132.
   - UF-157-2: "Picture-chain meta-substrate (outlook documents, operator runbooks) is appendix material to a program-level paper, not standalone deposit material. Independent Zenodo deposits require standalone citation utility." — Generalizes the Q1b reasoning.
   - UF-157-3: "RULE 1 fire-eligibility is a tradeoff-matrix axis when M11-gated framings (arXiv/journal) compete with Zenodo-only framings." — Generalizes the §Q2 G/H2 caveat.

4. **Slot 155 disposition:** Re-purpose with adjusted TARGET_PAPER list (option i). Lightweight prompt edit; no full re-draft.

5. **D-154-1 disposition:** CLOSED — fold picture-chain content into Umbrella v2.3 Appendix C per Q4b. Mark in S154 ACTION_LADDER tracking.

6. **Dual-witness escalation: NOT REQUIRED.** This verdict is FRAMING_AMEND at MEDIUM-HIGH band, ceiling-compliant, not FRAMING_SUPERSEDE. Single-witness is sufficient per Section 4 aggregation rule. Operator may elect dual-witness for additional confidence given the matrix's Q3 Pareto analysis is the load-bearing argument.

## ONE-LINE TAKEAWAY

Keep cascade-132 Option α's two manuscript deposits (PCF-2 v1.4, Umbrella) and fold picture-chain into Umbrella v2.3 as Appendix C — this Pareto-dominates the status quo on citation friction, discoverability, and D-154-1 resolution at ~1.1–1.3× composition cost, while preserving the PCF-1/PCF-2 concept-DOI lineages and avoiding the 2.5–3.5× consolidation tax of Framing A.
