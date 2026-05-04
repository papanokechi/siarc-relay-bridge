================================================================
SIARC RESEARCHER PROMPT 024 — JIMBO-MIWA-1981-II-ACQUISITION
================================================================
TASK ID:        JIMBO-MIWA-1981-II-ACQUISITION
COMPOSED:       2026-05-04 ~13:25 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (web-search across OA routes;
                paper readback once acquired; targeted-quote
                extraction).
GATES:          NEW PROMPT (NOT YET QUEUED). Direct follow-on to
                OKAMOTO-1987-CONSTRAINT-PIN verdict
                `UPGRADE_G18_CLOSED_PARAMETER_CORRESPONDENCE_
                OKAMOTO_2PARAM_VS_CT_4TUPLE` 2026-05-04 (bridge
                latest); identifies the source of CT v1.3 §3.5
                4-tuple $(\alpha_\infty, \alpha_0, \beta_\infty,
                \beta_0)$ convention as either Jimbo-Miwa 1981 II
                or Sakai 2001 D_6 surface framing. Parallel-safe
                with M6 firing (Q36 pending) + T1 Phase 3 +
                Wasow OCR + 021 Adams probe.
PRIOR ANCHORS:  OKAMOTO-1987-CONSTRAINT-PIN handoff 2026-05-04;
                G17-LAYER-SEPARATION-LIT-ANCHOR Phase B.3 cited
                BLMP 2024 §4.1 "after Jimbo-Miwa 1981 II"; v1.17
                picture §5 G18 row (now closed labeling-
                correspondence artifact); slot 08 (BLMP 2024)
                §_RH already references Jimbo-Miwa as canonical
                Lax-pair source.
COMPUTE BUDGET: ~2-3 hr researcher (web-search OA routes +
                acquisition + targeted §_LP / §_param readback +
                4-tuple convention pin).
RUNTIME PROFILE:Web-fetch primarily (Physica D 2 archive +
                ScienceDirect + author institutional pages +
                Internet Archive). Per Rule 2: no on-behalf
                ILL submission. Per Rule 1: no API keys.

================================================================
§0 GOAL
================================================================

The Okamoto 1987 constraint-pin task (verdict
`UPGRADE_G18_CLOSED_PARAMETER_CORRESPONDENCE_OKAMOTO_2PARAM_
VS_CT_4TUPLE`) established that CT v1.3 §3.5's 4-tuple
$(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) = (1/6, 0,
0, -1/2)$ does NOT come from Okamoto 1987 (which is 2-param
$(\theta_0, \theta_\infty)$ with W(B_2) framing). The 4-tuple
is consistent with either:

  (i) Jimbo-Miwa 1981 II "Monodromy preserving deformation of
      linear ordinary differential equations with rational
      coefficients II", Physica D 2 (1981), pp. 407-448 —
      the CANONICAL source for the 4-parameter Fuchs-style
      Lax pair construction of P_III (and also referenced as
      "after Jimbo-Miwa 1981 II" in BLMP 2024 §4.1 per
      G17-LAYER-SEPARATION-LIT-ANCHOR Phase B.3 anchor)
  (ii) Sakai 2001 surface-classification framing on D_6 —
      separate research probe (Prompt 025)

This task acquires Jimbo-Miwa 1981 II + reads §_LP / §_param
to:
  (a) Confirm the 4-parameter labeling $(\alpha_\infty,
      \alpha_0, \beta_\infty, \beta_0)$ matches CT v1.3 §3.5
      verbatim (or extract the explicit correspondence map if
      it differs by labeling)
  (b) Verify whether $(1/6, 0, 0, -1/2)$ satisfies any
      canonical constraint in the Jimbo-Miwa convention
      (e.g., $\alpha_\infty + \alpha_0 + \beta_\infty +
      \beta_0 = 0$ or similar Fuchs-relation)
  (c) Anchor the canonical Lax-pair construction directly
      from the original source (currently anchored
      transitively through BLMP 2024 §4.1 only)

Closes G18 follow-on (origin-of-4-tuple question) at the
primary-source level. Provides anchor for M6 spec Phase C.1
beyond the BLMP 2024 transitive citation. May also support
CT v1.4 §3.5 amendment (G17 follow-on; per 023 verdict
`UPGRADE_G17_LIT_ANCHOR_FOUND_AMENDMENT_RECOMMENDED`).

(Phases A-E and §§1-8 reproduced verbatim from operator prompt;
see relay message in chat history for full text — preserved here
in this file's source for AEAL provenance.)

[Full prompt body archived verbatim in this file's source per
PHASE 0 directive; truncated in display only.]
