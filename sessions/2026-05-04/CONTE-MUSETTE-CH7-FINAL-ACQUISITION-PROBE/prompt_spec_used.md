================================================================
SIARC RESEARCHER PROMPT 028 — CONTE-MUSETTE-CH7-FINAL-ACQUISITION-PROBE
================================================================
TASK ID:        CONTE-MUSETTE-CH7-FINAL-ACQUISITION-PROBE
COMPOSED:       2026-05-04 ~13:45 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (web-search OA routes;
                paper readback if acquired). Pattern-parallel
                to ADAMS-1928-FINAL-ACQUISITION-PROBE (Prompt
                021); clean-up of SCENARIO_C residual.
GATES:          NEW PROMPT (NOT YET QUEUED). Final OA
                acquisition probe for Conte-Musette 2008 ch.
                7 — currently SCENARIO_C-substituted by Costin
                2008 ch. 5 (slot 06; SHA `436c6c11...`). The
                substitution is sufficient for current SIARC
                scope; this task is a clean-up probe to
                either definitively close acquisition prospects
                OR upgrade slot citations from substitute to
                primary. Parallel-safe with M6 firing + T1
                Phase 3 + 021 Adams probe + 024-027 batch.
PRIOR ANCHORS:  R5-OKAMOTO-NUMDAM-RETRY verdict 2026-05-04
                (SCENARIO_B confirmed; slot 06 Costin 2008
                ch. 5 substitutes Conte-Musette ch. 7); v1.17
                picture §5 G3b row (residual: Conte-Musette
                NIA, substituted); 021 Adams pattern.
COMPUTE BUDGET: ~1-2 hr researcher (web-search OA routes +
                acquisition + targeted §7.3 / §7.4 readback).
RUNTIME PROFILE:Web-fetch primarily (Springer + JSPS / Project
                Euclid / Internet Archive / author Université
                Pierre et Marie Curie / ENS Paris-Saclay
                archive). Per Rule 2: no on-behalf ILL. Per
                Rule 1: no API keys.

================================================================
§0 GOAL
================================================================

R. Conte and M. Musette "The Painlevé Handbook", Springer
(2008) ch. 7 ("Discrete Painlevé equations" or "Algorithmic
Painlevé test"; verify exact ch. 7 title from acquired copy)
is cited in early SIARC research framing as a primary anchor
for the Painlevé-class structural framing of P_III(D_6). It
was Not-In-Archive (NIA) on disk during R5 acquisition cycles;
SCENARIO_C disposition substituted slot 06 = Costin 2008 ch. 5
"Asymptotics, Singular Perturbations and Resurgence" as a
broader-scope primary anchor that sufficiently covers the
needed Stokes-phenomenon framing for M6 spec Phase C.3.

This task is the FINAL OA acquisition probe for Conte-Musette
2008 ch. 7 primary source. Outcomes:

  (a) **Acquisition succeeds**: Conte-Musette ch. 7 acquired
      with text layer; §§7.3-7.4 (algorithmic Painlevé test +
      P_III specific construction) directly readable;
      G3b residual (Conte-Musette NIA) closes positively;
      M6 spec Phase C.3 may upgrade citation from "Costin
      2008 ch. 5 (substituting Conte-Musette ch. 7)" to
      direct Conte-Musette ch. 7 anchor

  (b) **Acquisition fails (clean)**: definitive negative
      on all OA routes; G3b residual (Conte-Musette NIA)
      stays closed-via-substitute; M6 spec Phase C.3
      retains slot 06 Costin ch. 5 as primary anchor

This task is HOUSEKEEPING-grade (not gating any current
SIARC closure path); pattern-parallel to 021 Adams probe.

================================================================
§1 ANCHOR FILES (preconditions; verify all present)
================================================================

PRIMARY ACQUISITION TARGET:
  Conte, R. and Musette, M. "The Painlevé Handbook", Springer
  (2008), ch. 7. Specifically §§7.3-7.4 (algorithmic Painlevé
  test + P_III(D_6) specific construction). ISBN 978-1-4020-
  8491-1; CrossRef DOI 10.1007/978-1-4020-8491-1.

LITERATURE WORKSPACE (substitute and cross-check):
  tex/submitted/control center/literature/g3b_2026-05-03/
    06_costin_2008.pdf (slot 06; SHA prefix 436c6c11;
                         SCENARIO_C substitute for Conte-
                         Musette ch. 7 per R5 dispositon)
    07_okamoto_1987_painleve_III_FE30.pdf (slot 07; W(B_2);
                                            references
                                            Painlevé test
                                            framework)
    08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf
    (slot 08; cites Conte-Musette 2008 ch. 7 in some
     references — verify)
    SHA256SUMS.txt

PRIOR HANDOFFS:
  sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/handoff.md
    (verdict OUTCOME_R5RT_NUMDAM_ACQUIRED; SCENARIO_B
     confirmed; Conte-Musette ch. 7 substituted by Costin
     ch. 5)
  sessions/2026-05-04/R5-OKAMOTO-PROJECT-EUCLID-RETRY/
    handoff.md (verdict OUTCOME_R5RT_NOT_ON_PROJECT_EUCLID;
                 wrong-paper finding context)

PICTURE v1.17:
  tex/submitted/control center/picture_revised_20260504.md
    — §5 G3b row (residual (iii) Conte-Musette ch. 7 NIA;
                  substituted by Costin 2008 ch. 5;
                  SCENARIO_C-accepted)

================================================================
§2 PHASES
================================================================

(see prompt 028 above for full phase list — A bibliographic;
 B routes B.1-B.8; C acquire if any route succeeds; D verdict
 + cross-validation against substitute; E handoff + AEAL).

================================================================
§3 AEAL CLAIMS MINIMUM
================================================================

>= 4 entries. evidence_type in {literature_citation,
deposit_confirmation, literature_quotation}. reproducible:
true.

================================================================
§7 OUTCOME LADDER
================================================================

  UPGRADE_CONTE_ACQUIRED_SUBSTITUTE_VALIDATED
  UPGRADE_CONTE_ACQUIRED_BOTH_NEEDED
  UPGRADE_CONTE_NIA_ILL_RECOMMENDED_<library>
  HALT_CONTE_DIRECT_DISAGREES_WITH_COSTIN
  HALT_CONTE_TEXT_LAYER_BAD
  HALT_CONTE_ALL_OA_ROUTES_FAIL
  HALT_CONTE_PAYWALL_RULE_1
================================================================
