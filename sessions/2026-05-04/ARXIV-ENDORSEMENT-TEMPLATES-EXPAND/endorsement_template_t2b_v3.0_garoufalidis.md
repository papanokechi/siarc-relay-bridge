        # Endorsement-request template — T2B v3.0 → Prof. {{ENDORSER_LASTNAME|Garoufalidis}}

        > **Operator action.**  This is a populated template.  Before sending,
        > the operator (a) verifies the endorser's institutional email at the
        > public homepage of Southern University of Science and Technology (SUSTech), Shenzhen; secondary Max Planck Institute for Mathematics, Bonn (do *not* paste an unverified
        > address — homepage hint: https://faculty.sustech.edu.cn/garoufalidis/en/ ; https://www.mpim-bonn.mpg.de/de/garoufalidis);
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

        - Full name:        Prof. {{ENDORSER_LASTNAME|Garoufalidis}}
        - arXiv author id:  `{{ENDORSER_HANDLE|garoufalidis_s_1}}`  (https://arxiv.org/a/garoufalidis_s_1)
        - ORCID:            0000-0001-5381-1593
        - Affiliation:      Southern University of Science and Technology (SUSTech), Shenzhen; secondary Max Planck Institute for Mathematics, Bonn
        - Email:            {{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}
        - Research area:    math.GT primary; math.NT and math.CA cross-list — quantum topology, Habiro ring of a number field, Bloch groups / algebraic K-theory, resurgence of Kontsevich–Zagier power series

        ---

        **Subject:** arXiv `math.HO` endorsement request — *{{TITLE|Two arithmetic classes of degree-(2,1) Trans-stratum continued fractions: a Birkhoff–Trjitzinsky / Gauss-continued-fraction dichotomy}}*

        ---

        Dear Prof. {{ENDORSER_LASTNAME|Garoufalidis}},

        I am writing to request your endorsement for an arXiv submission to
        the `math.HO` (with cross-listing to `math.NT`) category.  The paper, "{{TITLE|Two arithmetic classes of degree-(2,1) Trans-stratum continued fractions: a Birkhoff–Trjitzinsky / Gauss-continued-fraction dichotomy}}"
        (Zenodo deposit {{DOI|10.5281/zenodo.19915689}}, version {{VER|3.0}}),
        is part of an independent research programme — the Self-Iterating
        Analytic Relay Chain (SIARC) — on polynomial continued fractions
        and their analytic / Painlevé / number-theory consequences.

        **Paper summary.** T2B v3.0 is a Theory-Fleet H1 history-of-
mathematics record establishing a sharp two-class arithmetic
dichotomy for degree-(2,1) Trans-stratum polynomial continued
fractions: every in-scope family resolves either as a
Birkhoff–Trjitzinsky asymptotic case or as a Gauss-continued-
fraction case, with explicit decision criteria stated in
terms of the discriminant invariants of the underlying
recurrence. The dichotomy aligns with PCF-1 v1.3's degree-2
Trans-stratum classification and supplies a self-contained
history-of-math entry into the SIARC stratification programme
for readers approaching from the irrationality-theory
side.

        **Why I am asking you.**  T2B v3.0 cross-lists `math.NT`. The paper's Gauss-CF branch employs continued-fraction arithmetic in the irrationality-measure tradition; your math.NT activity (Habiro ring, Bloch groups) qualifies you to judge a math.NT-tagged continued-fraction discriminant paper.

        **Practical step.**  I will start a new submission at
        https://arxiv.org/submit which will trigger arXiv to issue a
        6-character endorsement code and send me an email containing
        endorsement instructions to forward to you.  The endorser-side action
        takes a few minutes and is one-time per category.

        The Zenodo deposit at {{DOI|10.5281/zenodo.19915689}} (concept DOI
        10.5281/zenodo.19783311) contains the full PDF, abstract, reproducibility
        metadata, and the SIARC bridge provenance trail.  The arXiv submission
        will mirror that deposit byte-for-byte (file blob: t2b_paper_draft_v5_withauthor.pdf | 331769 bytes | md5 d245be3b2b60cf04c5210f3859ad7394;
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
        - `{{ENDORSER_LASTNAME|...}}`   — pre-filled with `Garoufalidis`; operator may replace
        - `{{ENDORSER_HANDLE|...}}`     — pre-filled with `garoufalidis_s_1`; operator may replace
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
