        # Endorsement-request template — SIARC umbrella v2.0 → Prof. {{ENDORSER_LASTNAME|Zudilin}}

        > **Operator action.**  This is a populated template.  Before sending,
        > the operator (a) verifies the endorser's institutional email at the
        > public homepage of Radboud University, Nijmegen (Netherlands) (do *not* paste an unverified
        > address — homepage hint: https://www.ru.nl/en/people/zudilin-w);
        > (b) substitutes their own `{{OPERATOR_NAME}}` and `{{OPERATOR_ORCID}}`;
        > (c) optionally attaches a copy of the Zenodo PDF.  Per arXiv help
        > (https://info.arxiv.org/help/endorsement.html), the endorser receives
        > a 6-character alphanumeric code once the operator starts a new
        > submission in `math.HO` and is willing to provide endorsement;
        > the endorser enters the code at https://arxiv.org/auth/endorse.
        > Per arXiv etiquette, do **not** email large numbers of endorsers at
        > once or repeat-email the same endorser.

        ---

        **Suggested endorser (this populated template)**

        - Full name:        Prof. {{ENDORSER_LASTNAME|Zudilin}}
        - arXiv author id:  `{{ENDORSER_HANDLE|zudilin_w_1}}`  (https://arxiv.org/a/zudilin_w_1)
        - ORCID:            0000-0001-9551-2903
        - Affiliation:      Radboud University, Nijmegen (Netherlands)
        - Email:            {{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}
        - Research area:    math.NT (very strong), math.CA cross-list — transcendence theory, irrationality measures, continued fractions, hypergeometric / Apéry-tradition arithmetic

        ---

        **Subject:** arXiv `math.HO` endorsement request — *{{TITLE|An Arithmetic Stratification of Polynomial Continued Fractions — v2.0 (Modular-Discriminant Framing)}}*

        ---

        Dear Prof. {{ENDORSER_LASTNAME|Zudilin}},

        I am writing to request your endorsement for an arXiv submission to
        the `math.HO` category.  The paper, "{{TITLE|An Arithmetic Stratification of Polynomial Continued Fractions — v2.0 (Modular-Discriminant Framing)}}"
        (Zenodo deposit {{DOI|10.5281/zenodo.19965041}}, version {{VER|2.0}}),
        is part of an independent research programme — the Self-Iterating
        Analytic Relay Chain (SIARC) — on polynomial continued fractions
        and their analytic / Painlevé / number-theory consequences.

        **Paper summary.** SIARC umbrella v2.0 is a programme-level
history-of-mathematics statement / overview surveying the
Self-Iterating Analytic Relay Chain (SIARC) arithmetic
stratification of polynomial continued fractions (PCFs).
v2.0 adds the modular-discriminant invariant-triple framing
(§4.4) and consolidates the Trans-stratum / CM-stratum
dichotomy results from PCF-1 v1.3 (Zenodo 10.5281/zenodo.19937196)
and the cubic-extension programme statement PCF-2 v1.3
(Zenodo 10.5281/zenodo.19963298). The umbrella does not
contain new theorems; it is a survey-style document
establishing notation, programme scope, and citation
relationships for the rest of the SIARC stack.

        **Why I am asking you.**  Your published work in primary `math.NT` (transcendence theory, irrationality measures, the modern Apéry tradition) intersects directly with the umbrella's stratification programme: PCF-1 v1.3's CM-stratum dichotomy is a transcendence-predicate statement and the umbrella surveys it as such. Even though the primary class for this submission is `math.HO`, an active math.NT endorser with irrationality-tradition expertise is well positioned to judge the survey's topical fit.

        **Practical step.**  I will start a new submission at
        https://arxiv.org/submit which will trigger arXiv to issue a
        6-character endorsement code and send me an email containing
        endorsement instructions to forward to you.  The endorser-side action
        takes a few minutes and is one-time per category.

        The Zenodo deposit at {{DOI|10.5281/zenodo.19965041}} (concept DOI
        10.5281/zenodo.19885549) contains the full PDF, abstract, reproducibility
        metadata, and the SIARC bridge provenance trail.  The arXiv submission
        will mirror that deposit byte-for-byte (file blob: main.pdf | 455178 bytes | md5 d633699fbfe698dae08d510e8e165320;
        MD5 + SHA-256 + size + page count verified against the Zenodo API on
        2026-05-04 per ARXIV-PACK-FOUR-RECORD-AUDIT and ARXIV-MIRROR-RUNBOOK-
        REFIRE).

        If you are unable to endorse — for example, if your `math.HO`
        endorsement privileges are not currently active or if the topical fit
        is too distant for your judgement — please simply reply to that
        effect; I will then approach a different qualified endorser.  No
        follow-up email will be sent.

        With many thanks for your consideration,

        {{OPERATOR_NAME}}
        Yokohama, Japan
        ORCID: {{OPERATOR_ORCID}}
        {{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}

        ---

        ## Operator-personalisation placeholders (do NOT auto-fill)

        - `{{OPERATOR_NAME}}`           — operator chooses
        - `{{OPERATOR_ORCID}}`          — operator chooses
        - `{{ENDORSER_LASTNAME|...}}`   — pre-filled with `Zudilin`; operator may replace
        - `{{ENDORSER_HANDLE|...}}`     — pre-filled with `zudilin_w_1`; operator may replace
        - `{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}` — operator confirms institutional homepage
        - `{{TITLE|...}}`               — pre-filled; verbatim from Zenodo
        - `{{DOI|...}}`                 — pre-filled; verbatim from Zenodo
        - `{{VER|...}}`                 — pre-filled

        ## AEAL provenance

        - 037 session: `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/`
        - Record metadata source: 034 zenodo_metadata_5_records.json
          (Zenodo API readback 2026-05-04).
        - Endorser-handle source: ENDORSER-HANDLE-ACQUISITION 2026-05-04
          (Tier-1 confirmed-public arXiv handle).
        - arXiv endorsement policy: https://info.arxiv.org/help/endorsement.html
          (captured 034 PHASE D; re-cited as the policy baseline).
