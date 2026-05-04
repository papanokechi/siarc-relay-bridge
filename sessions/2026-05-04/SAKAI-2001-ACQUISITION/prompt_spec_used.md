# Prompt spec used — SAKAI-2001-ACQUISITION

This is a verbatim copy of the relay prompt body driving this session.
Composed 2026-05-04 ~13:30 JST. Drafted-by Copilot CLI (Claude Opus 4.7 xhigh).

================================================================
SIARC RESEARCHER PROMPT 025 — SAKAI-2001-ACQUISITION
================================================================
TASK ID:        SAKAI-2001-ACQUISITION
COMPOSED:       2026-05-04 ~13:30 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (web-search OA routes;
                paper readback; targeted-quote extraction across
                surface-classification + W(D_6) framing).
GATES:          NEW PROMPT (NOT YET QUEUED). Multi-purpose:
                supports OKAMOTO-1987-CONSTRAINT-PIN follow-on
                (G18 alternative origin), G17-LAYER-SEPARATION-
                LIT-ANCHOR amendment (CT v1.4 §3.5 deeper
                framing), and M6 spec Phase B.5 (W(B_2) ↔
                W(D_6) cross-walk literature anchor). Parallel-
                safe with all v1.17 / 024-batch tasks.
PRIOR ANCHORS:  G17-LAYER-SEPARATION-LIT-ANCHOR Phase B.4
                (mentioned Sakai 2001 as optional anchor, NIA
                this cycle); OKAMOTO-1987-CONSTRAINT-PIN
                verdict 2026-05-04 (W(B_2) confirmed; D_6
                framing requires Sakai); v1.17 picture §5 G18
                row (now closed labeling-correspondence
                artifact); M6 spec Phase B.5 (W cross-walk).
COMPUTE BUDGET: ~2-3 hr researcher (web-search OA routes +
                acquisition + targeted §_surfaces / §_W
                readback).
RUNTIME PROFILE:Web-fetch primarily (Springer + Project Euclid +
                CMP + author RIMS / U-Tokyo archive + Internet
                Archive). Per Rule 2: no on-behalf ILL. Per Rule
                1: no API keys.

§0 GOAL — acquire Sakai 2001 (CMP 220 (2001) 165-229) + read
§_surfaces (D_6 surface classification) + §_W (W(D_6) action)
for (a) G18 alt origin, (b) G17 framing deepening, (c) M6
Phase B.5 W(B_2)↔W(D_6) cross-walk anchor.

§1 ANCHOR FILES — primary acquisition target Sakai 2001 CMP
220:165-229 DOI 10.1007/s002200100446; literature workspace
literature/g3b_2026-05-03/{07,08} present; prior handoffs
OKAMOTO-1987-CONSTRAINT-PIN + G17-LAYER-SEPARATION-LIT-ANCHOR;
picture v1.17 §5 G17/G18 rows.

§2 PHASES — 0 provenance / A bibliographic / B OA-route survey
(SpringerLink, Project Euclid, arXiv, U-Tokyo, Internet Archive,
RIMS, ResearchGate-public-only) / C acquire+SHA+slot+SHA256SUMS
if any route succeeds / D pin convention + extract W(D_6)
generators + identify W(B_2)↔W(D_6) homomorphism / E verdict.

§3 AEAL ≥ 6 entries.

§4 HALT — DISAGREES_WITH_BLMP / TEXT_LAYER_BAD / ALL_OA_FAIL /
PAYWALL_RULE_1.

§5 hygiene per _RULES §D; verbatim ≤ 30 words.

§6 out of scope — modifying CT v1.3/v1.4, modifying M6 spec,
JM 1981 acquisition, Noumi-Yamada acquisition, browser-driven
submissions, API keys.

§7 outcome ladder — CT_TUPLE_D6_DIRECT_MATCH /
W_HOMOMORPHISM_FOUND / W_HOMOMORPHISM_NOT_IN_SAKAI /
NIA_ILL_RECOMMENDED / HALT_*.

§8 Standing final step B1-B5.
