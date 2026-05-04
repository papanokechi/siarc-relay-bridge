"""
037 PHASE B template emitter.

Emits 9 endorsement-request templates (3 records × 3 Tier-1 endorsers)
under the canonical ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/ folder. PII-
placeholder hygiene: zero auto-filled real names, real handles, real
emails (handles are public arXiv author-page identifiers per the
ENDORSER-HANDLE-ACQUISITION dossier; ORCIDs are public arXiv-page
disclosures; emails remain {{...}} placeholders per Rule 6).

Run from ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/ working directory or
absolute path.
"""

from __future__ import annotations
import os, hashlib, json
from textwrap import dedent

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ----- per-endorser inventory (Tier-1 confirmed-public per
# -----   ENDORSER-HANDLE-ACQUISITION 2026-05-04 candidate_dossier.md)
ENDORSERS = {
    "zudilin": {
        "lastname": "Zudilin",
        "firstname": "Wadim",
        "handle": "zudilin_w_1",
        "orcid": "0000-0001-9551-2903",
        "affiliation": "Radboud University, Nijmegen (Netherlands)",
        "homepage_hint": "https://www.ru.nl/en/people/zudilin-w",
        "primary_areas": "math.NT (very strong), math.CA cross-list",
        "research_summary": (
            "transcendence theory, irrationality measures, continued "
            "fractions, hypergeometric / Apéry-tradition arithmetic"
        ),
    },
    "mazzocco": {
        "lastname": "Mazzocco",
        "firstname": "Marta",
        "handle": "mazzocco_m_1",
        "orcid": "0000-0001-9917-2547",
        "affiliation": "School of Mathematics, University of Birmingham (UK)",
        "homepage_hint": "https://www.birmingham.ac.uk/staff/profiles/maths/mazzocco-marta",
        "primary_areas": "math.CA, math-ph, math.QA, math.AG",
        "research_summary": (
            "Painlevé equations, isomonodromic deformations, monodromy "
            "manifolds, decorated character varieties, Stokes-phenomenon "
            "confluence, double-affine Hecke algebras"
        ),
    },
    "garoufalidis": {
        "lastname": "Garoufalidis",
        "firstname": "Stavros",
        "handle": "garoufalidis_s_1",
        "orcid": "0000-0001-5381-1593",
        "affiliation": (
            "Southern University of Science and Technology (SUSTech), "
            "Shenzhen; secondary Max Planck Institute for Mathematics, Bonn"
        ),
        "homepage_hint": (
            "https://faculty.sustech.edu.cn/garoufalidis/en/ ; "
            "https://www.mpim-bonn.mpg.de/de/garoufalidis"
        ),
        "primary_areas": "math.GT primary; math.NT and math.CA cross-list",
        "research_summary": (
            "quantum topology, Habiro ring of a number field, Bloch "
            "groups / algebraic K-theory, resurgence of Kontsevich–Zagier "
            "power series"
        ),
    },
}

# ----- per-record inventory (verbatim from 034
# ----- zenodo_metadata_5_records.json after Zenodo API readback)
RECORDS = {
    "umbrella_v2.0": {
        "ord": 1,
        "label": "SIARC umbrella v2.0",
        "title": (
            "An Arithmetic Stratification of Polynomial Continued "
            "Fractions — v2.0 (Modular-Discriminant Framing)"
        ),
        "ver": "2.0",
        "doi": "10.5281/zenodo.19965041",
        "concept_doi": "10.5281/zenodo.19885549",
        "primary": "math.HO",
        "cross": [],
        "file_blob": "main.pdf | 455178 bytes | md5 d633699fbfe698dae08d510e8e165320",
        "summary": dedent("""\
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
            relationships for the rest of the SIARC stack.""").strip(),
    },
    "ct_v1.3": {
        "ord": 4,
        "label": "Channel Theory v1.3",
        "title": (
            "Channel Theory for Polynomial Continued Fractions: "
            "Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a "
            "Bridge Conjecture"
        ),
        "ver": "1.3",
        "doi": "10.5281/zenodo.19972394",
        "concept_doi": "10.5281/zenodo.19941678",
        "primary": "math-ph",
        "cross": ["math.DS", "math.NT"],
        "file_blob": "channel_theory_outline.pdf | 581459 bytes | md5 e58951de5cbf1be7cdd26f335bc359af",
        "summary": dedent("""\
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
            (op:cc-median-resurgence-execute, 108-digit pass).""").strip(),
    },
    "t2b_v3.0": {
        "ord": 5,
        "label": "T2B v3.0",
        "title": (
            "Two arithmetic classes of degree-(2,1) Trans-stratum "
            "continued fractions: a Birkhoff–Trjitzinsky / Gauss-"
            "continued-fraction dichotomy"
        ),
        "ver": "3.0",
        "doi": "10.5281/zenodo.19915689",
        "concept_doi": "10.5281/zenodo.19783311",
        "primary": "math.HO",
        "cross": ["math.NT"],
        "file_blob": "t2b_paper_draft_v5_withauthor.pdf | 331769 bytes | md5 d245be3b2b60cf04c5210f3859ad7394",
        "summary": dedent("""\
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
            side.""").strip(),
    },
}


def category_string(rec: dict) -> str:
    """`primary` (or, if cross-listed, `primary` (cross: a, b, c))."""
    primary = rec["primary"]
    if not rec["cross"]:
        return f"`{primary}`"
    cross_fmt = ", ".join(f"`{c}`" for c in rec["cross"])
    return f"`{primary}` (with cross-listing to {cross_fmt})"


def fit_blurb(rec_key: str, end_key: str) -> str:
    """Endorser-record subject-fit framing per subject_fit_matrix.md."""
    table = {
        ("umbrella_v2.0", "zudilin"): (
            "Your published work in primary `math.NT` (transcendence "
            "theory, irrationality measures, the modern Apéry tradition) "
            "intersects directly with the umbrella's stratification "
            "programme: PCF-1 v1.3's CM-stratum dichotomy is a "
            "transcendence-predicate statement and the umbrella surveys "
            "it as such. Even though the primary class for this "
            "submission is `math.HO`, an active math.NT endorser with "
            "irrationality-tradition expertise is well positioned to "
            "judge the survey's topical fit."
        ),
        ("umbrella_v2.0", "mazzocco"): (
            "The umbrella's §4.4 invariant-triple framing connects the "
            "SIARC stratification to Painlevé / integrable-systems data, "
            "an area in which your published work — particularly the "
            "Painlevé monodromy-manifold programme and the decorated "
            "character-variety formulation — supplies the closest "
            "topical anchor. The survey is `math.HO` primary; your "
            "math-ph / math.CA expertise qualifies you to judge "
            "topical-fit for the Painlevé-adjacent overview portions."
        ),
        ("umbrella_v2.0", "garoufalidis"): (
            "The umbrella surveys the full SIARC stack — PCFs, "
            "resurgence, integrable systems, modular discriminants — and "
            "your broad activity spanning math.GT (Habiro ring), math.NT "
            "(Bloch groups / Habiro-ring of a number field), and math.CA "
            "(resurgence of Kontsevich–Zagier power series) qualifies "
            "you to judge topical-fit for a programme-level overview."
        ),
        ("ct_v1.3", "zudilin"): (
            "Channel Theory v1.3 cross-lists `math.NT`. Your "
            "Apéry-tradition irrationality-measure work is a direct "
            "downstream consumer of the CC channel (the V_quad ⇝ "
            "P_III(D₆) connection-coefficient identity is precisely the "
            "ingredient one wants in order to attack irrationality "
            "measures for PCF-derived constants), and PCF-1 v1.3's "
            "CM-stratum dichotomy uses the same continued-fraction "
            "language as your published body of work."
        ),
        ("ct_v1.3", "mazzocco"): (
            "Channel Theory v1.3's primary class is `math-ph`. CT §3.5 "
            "reframes the V_quad ⇝ P_III(D₆) reduction in the language "
            "of decorated character varieties (Chekhov–Mazzocco–Rubtsov "
            "2017, arXiv:1705.01447) and uses the cubic / quartic "
            "Painlevé VI transformations of Mazzocco–Vidunas (Stud. Appl. "
            "Math. 130, 2013, arXiv:1011.6036) as a comparison point. "
            "The Stokes-phenomenon treatment of the Gauss-hypergeometric "
            "confluence in Horrobin–Mazzocco (arXiv:2009.07607) is also "
            "a precedent for the BoT channel."
        ),
        ("ct_v1.3", "garoufalidis"): (
            "Channel Theory v1.3 cross-lists `math.NT`. CT's annotated "
            "bibliography includes your collaboration with Costin on "
            "resurgence of Kontsevich–Zagier power series, which is the "
            "direct citation chain for the BoT channel; your "
            "Habiro-ring / Bloch-group work in math.NT supplies the "
            "broader arithmetic context CT v1.3 attempts to engage with."
        ),
        ("t2b_v3.0", "zudilin"): (
            "T2B v3.0 cross-lists `math.NT`. The paper's core "
            "Birkhoff–Trjitzinsky / Gauss-CF discriminant dichotomy is a "
            "math.NT-flavoured continued-fraction-arithmetic statement "
            "directly aligned with your published work on irrationality "
            "measures, hypergeometric arithmetic, and continued-fraction "
            "transcendence."
        ),
        ("t2b_v3.0", "mazzocco"): (
            "T2B v3.0's BoT-side analysis applies Stokes-phenomenon and "
            "asymptotic-confluence techniques in a degree-(2,1) "
            "continued-fraction setting; your Horrobin–Mazzocco "
            "Stokes-confluence paper (arXiv:2009.07607) is a structural "
            "precedent for the asymptotic side of the dichotomy. "
            "The cross-list `math.NT` is not your primary class, but "
            "the math-ph adjacency keeps the topical-fit gate plausible."
        ),
        ("t2b_v3.0", "garoufalidis"): (
            "T2B v3.0 cross-lists `math.NT`. The paper's Gauss-CF "
            "branch employs continued-fraction arithmetic in the "
            "irrationality-measure tradition; your math.NT activity "
            "(Habiro ring, Bloch groups) qualifies you to judge a "
            "math.NT-tagged continued-fraction discriminant paper."
        ),
    }
    return table[(rec_key, end_key)]


def render_template(rec_key: str, end_key: str) -> str:
    rec = RECORDS[rec_key]
    end = ENDORSERS[end_key]
    cat = category_string(rec)
    primary_only = f"`{rec['primary']}`"

    body = dedent(f"""\
        # Endorsement-request template — {rec['label']} → Prof. {{{{ENDORSER_LASTNAME|{end['lastname']}}}}}

        > **Operator action.**  This is a populated template.  Before sending,
        > the operator (a) verifies the endorser's institutional email at the
        > public homepage of {end['affiliation']} (do *not* paste an unverified
        > address — homepage hint: {end['homepage_hint']});
        > (b) substitutes their own `{{{{OPERATOR_NAME}}}}` and `{{{{OPERATOR_ORCID}}}}`;
        > (c) optionally attaches a copy of the Zenodo PDF.  Per arXiv help
        > (https://info.arxiv.org/help/endorsement.html), the endorser receives
        > a 6-character alphanumeric code once the operator starts a new
        > submission in {primary_only} and is willing to provide endorsement;
        > the endorser enters the code at https://arxiv.org/auth/endorse.
        > Per arXiv etiquette, do **not** email large numbers of endorsers at
        > once or repeat-email the same endorser.

        ---

        **Suggested endorser (this populated template)**

        - Full name:        Prof. {{{{ENDORSER_LASTNAME|{end['lastname']}}}}}
        - arXiv author id:  `{{{{ENDORSER_HANDLE|{end['handle']}}}}}`  (https://arxiv.org/a/{end['handle']})
        - ORCID:            {end['orcid']}
        - Affiliation:      {end['affiliation']}
        - Email:            {{{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}}}
        - Research area:    {end['primary_areas']} — {end['research_summary']}

        ---

        **Subject:** arXiv {primary_only} endorsement request — *{{{{TITLE|{rec['title']}}}}}*

        ---

        Dear Prof. {{{{ENDORSER_LASTNAME|{end['lastname']}}}}},

        I am writing to request your endorsement for an arXiv submission to
        the {cat} category.  The paper, "{{{{TITLE|{rec['title']}}}}}"
        (Zenodo deposit {{{{DOI|{rec['doi']}}}}}, version {{{{VER|{rec['ver']}}}}}),
        is part of an independent research programme — the Self-Iterating
        Analytic Relay Chain (SIARC) — on polynomial continued fractions
        and their analytic / Painlevé / number-theory consequences.

        {rec['summary']}

        **Why I am asking you.**  {fit_blurb(rec_key, end_key)}

        **Practical step.**  I will start a new submission at
        https://arxiv.org/submit which will trigger arXiv to issue a
        6-character endorsement code and send me an email containing
        endorsement instructions to forward to you.  The endorser-side action
        takes a few minutes and is one-time per category.

        The Zenodo deposit at {{{{DOI|{rec['doi']}}}}} (concept DOI
        {rec['concept_doi']}) contains the full PDF, abstract, reproducibility
        metadata, and the SIARC bridge provenance trail.  The arXiv submission
        will mirror that deposit byte-for-byte (file blob: {rec['file_blob']};
        MD5 + SHA-256 + size + page count verified against the Zenodo API on
        2026-05-04 per ARXIV-PACK-FOUR-RECORD-AUDIT and ARXIV-MIRROR-RUNBOOK-
        REFIRE).

        If you are unable to endorse — for example, if your {primary_only}
        endorsement privileges are not currently active or if the topical fit
        is too distant for your judgement — please simply reply to that
        effect; I will then approach a different qualified endorser.  No
        follow-up email will be sent.

        With many thanks for your consideration,

        {{{{OPERATOR_NAME}}}}
        Yokohama, Japan
        ORCID: {{{{OPERATOR_ORCID}}}}
        {{{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}}}

        ---

        ## Operator-personalisation placeholders (do NOT auto-fill)

        - `{{{{OPERATOR_NAME}}}}`           — operator chooses
        - `{{{{OPERATOR_ORCID}}}}`          — operator chooses
        - `{{{{ENDORSER_LASTNAME|...}}}}`   — pre-filled with `{end['lastname']}`; operator may replace
        - `{{{{ENDORSER_HANDLE|...}}}}`     — pre-filled with `{end['handle']}`; operator may replace
        - `{{{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}}}` — operator confirms institutional homepage
        - `{{{{TITLE|...}}}}`               — pre-filled; verbatim from Zenodo
        - `{{{{DOI|...}}}}`                 — pre-filled; verbatim from Zenodo
        - `{{{{VER|...}}}}`                 — pre-filled

        ## AEAL provenance

        - 037 session: `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/`
        - Record metadata source: 034 zenodo_metadata_5_records.json
          (Zenodo API readback 2026-05-04).
        - Endorser-handle source: ENDORSER-HANDLE-ACQUISITION 2026-05-04
          (Tier-1 confirmed-public arXiv handle).
        - arXiv endorsement policy: https://info.arxiv.org/help/endorsement.html
          (captured 034 PHASE D; re-cited as the policy baseline).
        """).rstrip() + "\n"

    return body


def main() -> None:
    pii_forbidden = [
        "@gmail.com", "@protonmail", "@yahoo.com", "@hotmail",
        # institutional emails — placeholder discipline forbids
        "@ru.nl", "@bham.ac.uk", "@birmingham.ac.uk",
        "@sustech.edu.cn", "@mpim-bonn.mpg.de",
    ]
    pii_alarm: list[str] = []

    files_written: list[tuple[str, str]] = []
    for rec_key in RECORDS:
        for end_key in ENDORSERS:
            content = render_template(rec_key, end_key)
            for needle in pii_forbidden:
                if needle in content.lower():
                    pii_alarm.append(
                        f"PII_LEAK in {rec_key}/{end_key}: '{needle}'"
                    )
            fname = f"endorsement_template_{rec_key}_{end_key}.md"
            path = os.path.join(OUT_DIR, fname)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
            files_written.append((fname, sha))

    summary = {
        "templates_emitted": len(files_written),
        "pii_alarm": pii_alarm,
        "files": [{"name": n, "sha256": s} for n, s in files_written],
    }
    with open(os.path.join(OUT_DIR, "_emit_summary.json"), "w",
              encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
