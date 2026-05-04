        # Endorsement-request template — Channel Theory v1.3 → Prof. {{ENDORSER_LASTNAME|Garoufalidis}}

        > **Operator action.**  This is a populated template.  Before sending,
        > the operator (a) verifies the endorser's institutional email at the
        > public homepage of Southern University of Science and Technology (SUSTech), Shenzhen; secondary Max Planck Institute for Mathematics, Bonn (do *not* paste an unverified
        > address — homepage hint: https://faculty.sustech.edu.cn/garoufalidis/en/ ; https://www.mpim-bonn.mpg.de/de/garoufalidis);
        > (b) substitutes their own `{{OPERATOR_NAME}}` and `{{OPERATOR_ORCID}}`;
        > (c) optionally attaches a copy of the Zenodo PDF.  Per arXiv help
        > (https://info.arxiv.org/help/endorsement.html), the endorser receives
        > a 6-character alphanumeric code once the operator starts a new
        > submission in `math-ph` and is willing to provide endorsement;
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

        **Subject:** arXiv `math-ph` endorsement request — *{{TITLE|Channel Theory for Polynomial Continued Fractions: Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture}}*

        ---

        Dear Prof. {{ENDORSER_LASTNAME|Garoufalidis}},

        I am writing to request your endorsement for an arXiv submission to
        the `math-ph` (with cross-listing to `math.DS`, `math.NT`) category.  The paper, "{{TITLE|Channel Theory for Polynomial Continued Fractions: Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture}}"
        (Zenodo deposit {{DOI|10.5281/zenodo.19972394}}, version {{VER|1.3}}),
        is part of an independent research programme — the Self-Iterating
        Analytic Relay Chain (SIARC) — on polynomial continued fractions
        and their analytic / Painlevé / number-theory consequences.

        **Paper summary.** Channel Theory v1.3 proposes, defines, and
catalogues *asymptotic channels* for sequences arising from
polynomial continued fractions (PCFs). Each channel is a
triple (D, T, S) specifying a formal-series space D, an
asymptotic gauge T, and an analytic-continuation section S;
three concrete channels appear in the SIARC stack — the
recurrence-parameter channel L(t), the Borel-of-trans-series
channel BoT, and the connection-coefficient channel CC.
The keystone result is a Newton-polygon proof that for every
in-scope degree-2 PCF (1, b) with b(n) = β₂ n² + β₁ n + β₀
the leading Borel-plane singularity of the generating
function f(z) = Σ Q_n z^n sits at radius ξ₀ = 2/√β₂, with
secondary exponent ρ = −3/2 − β₁/β₂. As a corollary the
V_quad ⇝ P_III(D₆) reduction is recovered in the CC channel
as an exact algebraic identity to 200 digits, modulo a
residual Borel–Laplace summation step that v1.3 reframes
(op:cc-formal-borel) and partially diagnoses by a theoretical
prediction of median Écalle resurgence at 5000 coefficients
(op:cc-median-resurgence-execute, 108-digit pass).

        **Why I am asking you.**  Channel Theory v1.3 cross-lists `math.NT`. CT's annotated bibliography includes your collaboration with Costin on resurgence of Kontsevich–Zagier power series, which is the direct citation chain for the BoT channel; your Habiro-ring / Bloch-group work in math.NT supplies the broader arithmetic context CT v1.3 attempts to engage with.

        **Practical step.**  I will start a new submission at
        https://arxiv.org/submit which will trigger arXiv to issue a
        6-character endorsement code and send me an email containing
        endorsement instructions to forward to you.  The endorser-side action
        takes a few minutes and is one-time per category.

        The Zenodo deposit at {{DOI|10.5281/zenodo.19972394}} (concept DOI
        10.5281/zenodo.19941678) contains the full PDF, abstract, reproducibility
        metadata, and the SIARC bridge provenance trail.  The arXiv submission
        will mirror that deposit byte-for-byte (file blob: channel_theory_outline.pdf | 581459 bytes | md5 e58951de5cbf1be7cdd26f335bc359af;
        MD5 + SHA-256 + size + page count verified against the Zenodo API on
        2026-05-04 per ARXIV-PACK-FOUR-RECORD-AUDIT and ARXIV-MIRROR-RUNBOOK-
        REFIRE).

        If you are unable to endorse — for example, if your `math-ph`
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
