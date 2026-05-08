# Handoff — T2-105-COPILOT-RESEARCHER-PROMPT-DRAFT-109
**Date:** 2026-05-08
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7 xhigh)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

User asked "help execute tier-A or provide prompt for copilot researcher" following the 069r2 §5 verdict packet absorption (bridge 108 LANDED at f840740). Agent produced a self-contained Copilot Researcher prompt (105) authoring CT v1.3 §3.5.1 sub-subsection "Okamoto-rename of the V_quad parameter point (η,θ)→(α,β)" — closing the QB.3 = Y_RENAME_REQUIRED resolution that gates ALL of M6.CC R1 closure Routes A/B/C/D. Companion skeletal .tex draft staged with 6 [TBD] markers as starting-point. Both files staged in `tex/submitted/control center/prompt/` (105_*) and bridge-deposited here for traceability. _INDEX.txt appended with prompt 105 entry.

## Key numerical findings

This session is governance / prompt-drafting only — no numerical claims advanced. Substrate verifications carried (no new digits):

- Okamoto 1987 §1 H_III display located at slot 07 .txt line 190 with parameters (η_∞, η_0, θ_∞, θ_0).
- KNY 2017 §8.5.17 d-P((2A_1)^(1)/D_6^(1)) Hamiltonian eq. (8.237) located at slot 14 .txt lines 7869-7922 with two free parameters (a_1, a_2).
- FW math-ph/0201051 bibliographic identifier pre-verified per repo standing rule (resolves correctly to Forrester+Witte 2002 CPA).
- CT v1.3 §3.5 source location at line 845 of `pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex` = "The locked WKB exponent identity" — independently valuable content; new §3.5.1 inserts AFTER line 891.

## Judgment calls made

1. **Companion skeletal .tex draft included.** User asked "help execute OR provide prompt"; agent provided BOTH — the prompt (primary deliverable) plus a candidate skeletal .tex with [TBD] markers (optional starting point). Researcher can use, edit, or discard. Reasoning: the substrate is so well-defined that providing a skeleton saves the researcher 30-60 min of structural plumbing while preserving full editorial freedom on the four equations + -1/3 attribution.

2. **Architectural recommendation: insert §3.5.1 after line 891, do NOT modify §3.5 main body.** Existing §3.5 ("WKB exponent identity") has live cite refs and downstream paragraphs. Modifying it would create cite-graph collisions. New §3.5.1 sub-subsection is cleaner.

3. **Symbol-collision footnote made mandatory in deliverable D4.** Three (α, β)-tuples coexist in CT v1.3 (WKB exponents, classical P_III ODE coefficients, Okamoto-rename); footnote disambiguating all three is non-optional.

4. **3 unexpected finds surfaced as research questions, not blockers.**
   - UF-109-1 (069r1 U1 forward-pointed citation): the §3.5 rewrite cited by U1 does not exist on disk. Documented in prompt §1.
   - UF-109-2 (Iwasaki 1991 / Ohyama 2006 unavailability): primary-literature sources for the (1/6, 0, 0, -1/2) convention are not currently in operator's slot library. Prompt instructs researcher to fall back to FW + Okamoto + KNY substrate and document the gap.
   - UF-109-3 (null-sum constraint provenance): the α_∞+α_0+β_∞+β_0=0 constraint is bridge-internal (058R B.3) without primary-literature cite. Skeletal draft has [TBD] marker for researcher to verify or weaken.

5. **Did NOT execute TIER-A directly.** User left the choice open ("help execute OR provide prompt"). Agent assessed: (i) the four equations require math judgment best done with full substrate access including Iwasaki/Ohyama if available; (ii) the -1/3 attribution among mechanisms (a)/(b)/(c) is genuinely a research question requiring deep substrate engagement; (iii) the operator may want particular notation/style matching their existing CT v1.3 voice. Producing the prompt + skeleton enables the operator to dispatch to Copilot Researcher (or Claude.ai web with extended thinking) with confidence.

## Anomalies and open questions

**Anomaly 1 — 069r1 U1 forward-pointing citation (UF-109-1).** 069r1 unexpected_finds.json U1 says "(α_∞, α_0, β_∞, β_0) is a project-side rename adopted in CT v1.3 §3.5 rewrite." Investigation 2026-05-08 confirmed this rewrite does not exist on disk. The "rewrite" is exactly what TIER-A creates. This is a benign forward-pointed citation, not a substrate gap, but it should be ledgered for AEAL hygiene.

**Anomaly 2 — Iwasaki 1991 + Ohyama 2006 not in slot library (UF-109-2).** CT v1.3 cites these two volumes as primary sources for the V_quad parameter point (1/6, 0, 0, -1/2). Neither is in `tex/submitted/control center/literature/g3b_2026-05-03/` slot library at draft time. If they ARE on disk elsewhere (operator filesystem outside the project tree), researcher should locate; otherwise fall back to FW + Okamoto + KNY substrate and document the gap.

**Anomaly 3 — Okamoto null-sum constraint provenance (UF-109-3).** The constraint α_∞+α_0+β_∞+β_0=0 is asserted in 058R B.3 but not source-cited there. It may originate from W(D_6) affine root sum, FW τ-function regularity, or be a project assumption. Researcher must source-cite or weaken in §3.5.1.

**Open question — what is the actual rename mechanism?** The candidate skeletal draft assumes TRIVIAL relabel (α ≡ η, β ≡ θ) as a placeholder. The -1/3 null-sum violation under trivial relabel suggests either (a) a t-linear Hamiltonian correction between KNY and Okamoto, (b) an additive shift in the rename, or (c) a Sakai surface artefact. The actual mechanism must be researcher-determined; prompt 105 enumerates all three with attribution-required.

**Open question — Route F surfacing risk.** If researcher's analysis lands on mechanism (c) Sakai surface artefact, this triggers HALT_105_ROUTE_F_PRECONDITION per prompt §7.C4 — Route F escalation requires operator authorization before proceeding into Sakai geometry.

## What would have been asked (if bidirectional)

1. **Operator preference: Iwasaki 1991 PDF location?** If operator has a copy outside `tex/submitted/control center/literature/`, paste the path so the prompt 105 substrate (S4) is fully closed.

2. **Operator preference: §3.5.1 sub-subsection vs §3.6 new subsection vs §3.5 footnote?** Agent recommended §3.5.1 (inserted after line 891). Operator may prefer alternative architecture.

3. **Operator preference: bib key naming for Okamoto/KNY/FW?** Agent flagged that prompt 105 instructs researcher to use UF-105-NEW-BIBKEY for any new keys; operator may prefer to pre-decide naming (`okamoto1987painleveIII`, `kajiwaranoumiyamada2017`, `forresterwitte2002` are agent's suggested keys).

## Recommended next step

**Operator dispatches prompt 105 to a Copilot Researcher session** (or Claude.ai web with extended thinking, or a fresh Copilot CLI session). Estimated 2-3 hr researcher-time. After 105 fires and lands, operator runs TIER-B substrate-paste round 1 with the new §3.5.1 as the 4th excerpt (Path B4a per cascade_plan.md) and dispatches to Claude.ai web for synth re-fire on QA + QB.1 + QB.4 + QE.

If operator prefers SHORTER cycle, fall back to Path B4b: dispatch TIER-B with current §3.5 (WKB identity) as 4th excerpt + operator note explaining the rename derivation is parallel-track. Synth gives Route E precondition assessment (QE) which informs the §3.5.1 authoring direction.

## Files committed

- sessions/2026-05-08/T2-105-COPILOT-RESEARCHER-PROMPT-DRAFT-109/
  - 105_copilot_researcher_route_e_okamoto_rename.txt (15083 B)
  - 105_skeletal_section_3_5_1_companion.tex.draft (9033 B)
  - claims.jsonl (7 entries)
  - halt_log.json (empty {})
  - discrepancy_log.json (empty {})
  - unexpected_finds.json (UF-109-1, UF-109-2, UF-109-3)
  - handoff.md (this file)

## AEAL claim count

7 entries written to claims.jsonl this session.
