# Endorsement-request template — PCF-1 v1.3 → Prof. {{ENDORSER_LASTNAME|Zudilin}}

> **Operator action.**  This is a populated template.  Before sending,
> the operator (a) verifies the endorser's institutional email at the
> public homepage of Radboud University, Nijmegen (do *not* paste an unverified address);
> (b) substitutes their own `{{OPERATOR_NAME}}` and `{{OPERATOR_ORCID}}`;
> (c) optionally attaches a copy of the Zenodo PDF.  Per arXiv help
> (https://info.arxiv.org/help/endorsement.html), the endorser receives
> a 6-character alphanumeric code once the operator starts a new
> submission in `math.NT` and is willing to provide endorsement;
> the endorser enters the code at https://arxiv.org/auth/endorse.
> Per arXiv etiquette, do **not** email large numbers of endorsers at
> once or repeat-email the same endorser.

---

**Suggested endorser (this populated template)**

- Full name:        Prof. {{ENDORSER_LASTNAME|Zudilin}}
- arXiv author id:  `{{ENDORSER_HANDLE|zudilin_w_1}}`  (https://arxiv.org/a/zudilin_w_1)
- Affiliation:      Radboud University, Nijmegen
- Email:            {{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}
- Research area:    primary math.NT, transcendence + irrationality measures + continued fractions

---

**Subject:** arXiv `math.NT` endorsement request — *{{TITLE|Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions}}*

---

Dear Prof. {{ENDORSER_LASTNAME|Zudilin}},

I am writing to request your endorsement for an arXiv submission to
the `math.NT` category, with cross-listing to `math.CA`.  The paper,
"{{TITLE|Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions}}" (Zenodo deposit {{DOI|10.5281/zenodo.19937196}}, version
{{VER|1.3}}, {{N_PAGES|see Zenodo record}} pp.), is part of
an independent research programme — the Self-Iterating Analytic Relay
Chain (SIARC) — on polynomial continued fractions and their analytic
/ Painlevé / number-theory consequences.

**Paper summary.** We propose a transcendence predicate for degree-two polynomial continued fractions (PCFs) based on the sign of the balanced discriminant Delta = beta^2 - 4*alpha*gamma of the denominator polynomial b_n = alpha*n^2 + beta*n + gamma. Working inside the Spec(K) classification framework of Papanokechi (2026), we present a v5 upgrade of the schema that fixes two cross-paper inconsistencies and adds the Stokes exponent and connection-coefficient proxy as components 6 and 7. Our central empirical finding is a sharp dichotomy across 30 degree-two families: 24 F(2,4) Trans-stratum families have Delta i…

**Why I am asking you.** Your published work in primary math.NT, transcendence + irrationality measures + continued fractions overlaps directly
with the present paper's subject and methods; if you are willing to
endorse and your `math.NT` endorsement privileges are currently
active, you are an excellent match per the arXiv guidelines.

**Practical step.** I will start a new submission at
https://arxiv.org/submit which will trigger arXiv to issue a
6-character endorsement code and send me an email containing
endorsement instructions to forward to you.  The endorser-side action
takes a few minutes and is one-time per category.

The Zenodo deposit at {{DOI|10.5281/zenodo.19937196}} contains the full PDF,
abstract, reproducibility metadata, and the SIARC bridge provenance
trail.  The arXiv submission will mirror that deposit byte-for-byte
(MD5 + SHA-256 + size + page count verified against the Zenodo API
on 2026-05-04).

If you are unable to endorse — for example, if your `math.NT`
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

- 034 session: `sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/`
- Endorser-handle source: ENDORSER-HANDLE-ACQUISITION 2026-05-04
  (Tier-1 confirmed-public arXiv handle).
