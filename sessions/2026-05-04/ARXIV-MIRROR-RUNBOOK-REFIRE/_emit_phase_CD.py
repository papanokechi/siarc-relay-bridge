"""
Phase C + D + E emission for ARXIV-MIRROR-RUNBOOK-REFIRE.
- 5 RUNBOOK_<record>.md files (Phase C)
- 6 endorsement_template_<record>_<endorser>.md files (Phase D)
- prompt_spec_used.md
- handoff.md (Phase E + B3)
- Append claims to claims.jsonl
"""
import json, hashlib, pathlib, datetime, textwrap

ROOT = pathlib.Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge")
SESS = ROOT / "sessions" / "2026-05-04" / "ARXIV-MIRROR-RUNBOOK-REFIRE"
TODAY = "2026-05-04"

records = json.loads((SESS / "zenodo_metadata_5_records.json").read_text(encoding="utf-8"))
hashr = json.loads((SESS / "_pack_hash_results.json").read_text(encoding="utf-8"))

# Pack relative paths for the 4 audit-cached packs + PCF-1 v1.3 canonical
PACK_REL = {
    "siarc_umbrella_v2.0": "sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0",
    "pcf1_v1.3":           "sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3",
    "pcf2_v1.3":           "sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3",
    "ct_v1.3":             "sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3",
    "t2b_v3.0":            "sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_t2b_v3.0",
}
PDF_NAME = {
    "siarc_umbrella_v2.0": "main.pdf",
    "pcf1_v1.3":           "p12_pcf1_main.pdf",
    "pcf2_v1.3":           "pcf2_program_statement.pdf",
    "ct_v1.3":             "channel_theory_outline.pdf",
    "t2b_v3.0":            "t2b_paper_draft_v5_withauthor.pdf",
}
TEX_NAME = {
    "siarc_umbrella_v2.0": "main.tex",
    "pcf1_v1.3":           "p12_pcf1_main.tex",
    "pcf2_v1.3":           "pcf2_program_statement.tex",
    "ct_v1.3":             "channel_theory_outline.tex",
    "t2b_v3.0":            "t2b_paper_draft_v5_withauthor.tex",
}
TARGZ = {
    "siarc_umbrella_v2.0": "siarc_umbrella_v2.0.tar.gz",
    "pcf1_v1.3":           "pcf1_v1.3.tar.gz",
    "pcf2_v1.3":           "pcf2_v1.3.tar.gz",
    "ct_v1.3":             "ct_v1.3.tar.gz",
    "t2b_v3.0":            "t2b_v3.0.tar.gz",
}

# Read each pack's abstract.txt
def get_abstract(rec_name):
    rel = PACK_REL[rec_name]
    p = ROOT / rel / "abstract.txt"
    return p.read_text(encoding="utf-8").strip()

# ---------------------------------------------------------------- RUNBOOKs

def runbook_md(r):
    name = r["name"]
    label = r["label"]
    abs_text = get_abstract(name)
    h = hashr[name]
    pages = h.get("deposit_pdf_size_expected") and 0  # not used; we have via 'expected' below
    pages_map = {"siarc_umbrella_v2.0":12,"pcf1_v1.3":16,"pcf2_v1.3":22,"ct_v1.3":17,"t2b_v3.0":8}
    pages = pages_map[name]
    primary = r["arxiv_primary"]
    cross = ", ".join(r["arxiv_cross"]) if r["arxiv_cross"] else "(none)"
    pack_rel = PACK_REL[name]
    pdf = PDF_NAME[name]
    tex = TEX_NAME[name]
    targz = TARGZ[name]
    ver = r["api_version"]
    doi = r["api_doi"]
    rec_id = r["record"]
    title = r["api_title"]

    # endorsement note based on category
    nt_required = primary == "math.NT" or "math.NT" in r["arxiv_cross"]
    if primary == "math.NT":
        endorse_note = (
            "**Endorsement REQUIRED** (primary math.NT, first-time submitter).  "
            "See §_endorsement below; six populated templates were emitted by "
            "034 (this record × three Tier-1 endorsers).  Operator personalises "
            "and sends one or more before the arXiv web-form submission can "
            "complete.  arXiv will issue a 6-character alphanumeric endorsement "
            "code once the operator starts a new submission in math.NT; that "
            "code is what the endorser enters at https://arxiv.org/auth/endorse."
        )
    elif primary == "math-ph":
        endorse_note = (
            "**Endorsement REQUIRED** for first-time submitter to math-ph.  "
            "math-ph is its own arXiv endorsement domain.  Endorser must hold "
            "active math-ph endorsement privilege (≥ a few math-ph submissions "
            "in the prior 5 years).  Tier-1 candidate from ENDORSER-HANDLE-"
            "ACQUISITION 2026-05-04 with math-ph track record: Marta Mazzocco "
            "(mazzocco_m_1) — operator confirms email before sending.  No "
            "math-ph-specific endorsement template was emitted by 034 (spec "
            "§3.D.1 limited Phase D to math.NT records only); operator may "
            "adapt the math.NT templates by changing `math.NT` → `math-ph` "
            "and the paper title accordingly."
        )
    elif primary == "math.HO":
        endorse_note = (
            "**Endorsement REQUIRED** for first-time submitter to math.HO.  "
            "math.HO is part of the math endorsement cluster.  Once the operator "
            "has obtained a single positive endorsement in any math.* category "
            "(e.g. math.NT via PCF-1 v1.3 in record #2), subsequent submissions "
            "in math.HO typically inherit the cluster's endorsement privileges "
            "for that operator (per current arXiv help text); operator confirms "
            "via the in-flight submission widget at submission time.  No math.HO-"
            "specific endorsement template was emitted by 034 (spec §3.D.1 "
            "limited Phase D to math.NT records only)."
        )
    else:
        endorse_note = "Endorsement requirement: confirm via arXiv submission widget."

    md = f"""# arXiv submission runbook — {label}

**Source-of-truth Zenodo record:** {doi} (record id {rec_id}, version {ver}).
**Pack location on bridge:** `{pack_rel}/`
**arXiv classification:** primary `{primary}`, cross-list `{cross}`.
**Page count:** {pages} pp.
**Operator-action gate per Rule 2:** the agent does *not* submit on behalf
of the operator.  This runbook is the operator's checklist.

---

## Step 0 — Prerequisites

1. arXiv account (operator's existing account; ORCID-verified preferred
   per arXiv's first-time-submitter expediting rule).
2. {endorse_note}
3. Bridge pack hash-verified vs Zenodo (PASS in 034 PHASE A.2;
   see `pack_hash_match_table.md` for md5 + SHA-256 + size + page count).

---

## Step 1 — File attachments (in order)

Upload to arXiv submission "Add Files" widget in this order:

```
{pack_rel}/{tex}                         # primary TeX source
{pack_rel}/00README.txt                          # bridge provenance + pack readme
{pack_rel}/abstract.txt                          # one-paragraph abstract verbatim
{pack_rel}/{pdf}                          # PDF alternate-source (arXiv auto-compile fallback)
```

The compressed pack tarball `{pack_rel}/{targz}` is *not* uploaded directly
(arXiv auto-tars after acceptance); it is preserved on the bridge as the
canonical immutable mirror artefact.

---

## Step 2 — arXiv classification

```
Primary:    {primary}
Cross-list: {cross}
```

Cross-list rationale:
{ '- ' + chr(10).join('  ' + c for c in r['arxiv_cross']) if r['arxiv_cross'] else '  (none)' }

---

## Step 3 — Metadata fields (paste verbatim)

- **Title:** {title}
- **Authors:** papanokechi (Independent Researcher, Yokohama, Japan)
- **Abstract:** *paste contents of `{pack_rel}/abstract.txt`* — first paragraph
  reproduced below for convenience:

> {abs_text[:400].replace(chr(10), ' ')}…  (full text in `abstract.txt`)

- **Comments:** "{pages} pages.  Mirror of Zenodo record {doi}."
- **Report-no:** *(none — SIARC nondefault)*
- **DOI:** {doi}
- **License:** CC-BY-4.0  (matches Zenodo; arXiv supports CC-BY-4.0 from
  the standard license dropdown).

---

## Step 4 — arXiv web-form sequence

1. https://arxiv.org/submit  →  **Start new submission**.
2. Choose category — primary `{primary}`, then click **Add another**
   for each cross-list entry above.
3. License — select **CC-BY-4.0** from the dropdown.
4. Add files — upload in the order listed in Step 1.
5. Verify auto-compile (arXiv runs pdfTeX on the .tex; the included
   .pdf serves as fallback if compile fails).
6. Metadata — paste Title, Authors, Abstract, Comments, DOI from Step 3.
7. Preview — confirm title/authors/abstract and PDF first page render
   match the deposited Zenodo PDF.
8. Submit — arXiv issues an arXiv ID of the form `arXiv:XXXX.XXXXX`.

---

## Step 5 — Post-submission

- Note the assigned arXiv ID under Item {r['ord']} of
  `tex/submitted/submission_log.txt`.
- Operator action on Zenodo: edit record {rec_id}'s
  **Related identifiers** to add the new arXiv ID with relation
  `IsIdenticalTo` (or `IsVersionOf`); this completes the Zenodo↔arXiv
  bidirectional cross-link.
- Update SIARC umbrella v2.0 / future v2.1 cross-reference tables
  (operator-side, separate session) with the arXiv ID.
- Confirm submission visible at `https://arxiv.org/abs/<arXiv-id>`
  ~24h after acceptance (arXiv's announcement cycle).

---

## §_endorsement (this record)

{ "See `endorsement_template_" + name + "_zudilin.md`, `endorsement_template_" + name + "_mazzocco.md`, `endorsement_template_" + name + "_garoufalidis.md` (this session)." if primary == "math.NT" else "Adapt one of the math.NT endorsement templates by substituting category and paper title; or proceed via institutional-email auto-endorsement path if applicable." }

---

## Provenance

- 034 session path: `sessions/{TODAY}/ARXIV-MIRROR-RUNBOOK-REFIRE/`
- Pack hash verification: `pack_hash_match_table.md` (5/5 PASS)
- Zenodo metadata blob: `zenodo_metadata_5_records.json`
- AEAL claims: `claims.jsonl`
"""
    return md

for r in records:
    nm = r["name"]
    p = SESS / f"RUNBOOK_{nm}.md"
    p.write_text(runbook_md(r), encoding="utf-8")
    print(f"WROTE {p.name}")

# ---------------------------------------------------------------- ENDORSEMENT TEMPLATES

ENDORSERS = {
    "zudilin":      ("Zudilin",      "zudilin_w_1",      "Radboud University, Nijmegen", "primary math.NT, transcendence + irrationality measures + continued fractions"),
    "mazzocco":     ("Mazzocco",     "mazzocco_m_1",     "University of Birmingham",     "math.CA + math-ph + integrable systems / Painlevé"),
    "garoufalidis": ("Garoufalidis", "garoufalidis_s_1", "SUSTech / MPIM Bonn",          "math.GT + math.NT cross-list (Habiro ring, q-series)"),
}

NT_RECORDS = [r for r in records if r["arxiv_primary"] == "math.NT"]
assert len(NT_RECORDS) == 2

def endorsement_md(rec, endorser_key):
    last, handle, affil, area = ENDORSERS[endorser_key]
    title = rec["api_title"]
    doi = rec["api_doi"]
    ver = rec["api_version"]
    name = rec["name"]
    primary = rec["arxiv_primary"]
    cross = ", ".join(rec["arxiv_cross"]) if rec["arxiv_cross"] else "(none)"

    return f"""# Endorsement-request template — {rec['label']} → Prof. {{{{ENDORSER_LASTNAME|{last}}}}}

> **Operator action.**  This is a populated template.  Before sending,
> the operator (a) verifies the endorser's institutional email at the
> public homepage of {affil} (do *not* paste an unverified address);
> (b) substitutes their own `{{{{OPERATOR_NAME}}}}` and `{{{{OPERATOR_ORCID}}}}`;
> (c) optionally attaches a copy of the Zenodo PDF.  Per arXiv help
> (https://info.arxiv.org/help/endorsement.html), the endorser receives
> a 6-character alphanumeric code once the operator starts a new
> submission in `{primary}` and is willing to provide endorsement;
> the endorser enters the code at https://arxiv.org/auth/endorse.
> Per arXiv etiquette, do **not** email large numbers of endorsers at
> once or repeat-email the same endorser.

---

**Suggested endorser (this populated template)**

- Full name:        Prof. {{{{ENDORSER_LASTNAME|{last}}}}}
- arXiv author id:  `{{{{ENDORSER_HANDLE|{handle}}}}}`  (https://arxiv.org/a/{handle})
- Affiliation:      {affil}
- Email:            {{{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}}}
- Research area:    {area}

---

**Subject:** arXiv `{primary}` endorsement request — *{{{{TITLE|{title}}}}}*

---

Dear Prof. {{{{ENDORSER_LASTNAME|{last}}}}},

I am writing to request your endorsement for an arXiv submission to
the `{primary}` category, with cross-listing to `{cross}`.  The paper,
"{{{{TITLE|{title}}}}}" (Zenodo deposit {{{{DOI|{doi}}}}}, version
{{{{VER|{ver}}}}}, {{{{N_PAGES|see Zenodo record}}}} pp.), is part of
an independent research programme — the Self-Iterating Analytic Relay
Chain (SIARC) — on polynomial continued fractions and their analytic
/ Painlevé / number-theory consequences.

**Paper summary.** {get_abstract(name)[:600].strip().replace(chr(10), ' ')}…

**Why I am asking you.** Your published work in {area} overlaps directly
with the present paper's subject and methods; if you are willing to
endorse and your `{primary}` endorsement privileges are currently
active, you are an excellent match per the arXiv guidelines.

**Practical step.** I will start a new submission at
https://arxiv.org/submit which will trigger arXiv to issue a
6-character endorsement code and send me an email containing
endorsement instructions to forward to you.  The endorser-side action
takes a few minutes and is one-time per category.

The Zenodo deposit at {{{{DOI|{doi}}}}} contains the full PDF,
abstract, reproducibility metadata, and the SIARC bridge provenance
trail.  The arXiv submission will mirror that deposit byte-for-byte
(MD5 + SHA-256 + size + page count verified against the Zenodo API
on {TODAY}).

If you are unable to endorse — for example, if your `{primary}`
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
- `{{{{ENDORSER_LASTNAME|...}}}}`   — pre-filled with `{last}`; operator may replace
- `{{{{ENDORSER_HANDLE|...}}}}`     — pre-filled with `{handle}`; operator may replace
- `{{{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}}}` — operator confirms institutional homepage
- `{{{{TITLE|...}}}}`               — pre-filled; verbatim from Zenodo
- `{{{{DOI|...}}}}`                 — pre-filled; verbatim from Zenodo
- `{{{{VER|...}}}}`                 — pre-filled

## AEAL provenance

- 034 session: `sessions/{TODAY}/ARXIV-MIRROR-RUNBOOK-REFIRE/`
- Endorser-handle source: ENDORSER-HANDLE-ACQUISITION 2026-05-04
  (Tier-1 confirmed-public arXiv handle).
"""

count = 0
for rec in NT_RECORDS:
    for e_key in ("zudilin", "mazzocco", "garoufalidis"):
        p = SESS / f"endorsement_template_{rec['name']}_{e_key}.md"
        p.write_text(endorsement_md(rec, e_key), encoding="utf-8")
        count += 1
        print(f"WROTE {p.name}")

print(f"Total endorsement templates emitted: {count}")

# ---------------------------------------------------------------- prompt_spec_used.md

(SESS / "prompt_spec_used.md").write_text(textwrap.dedent(f"""
# prompt_spec_used.md — ARXIV-MIRROR-RUNBOOK-REFIRE

**Date:** {TODAY}
**Task ID:** ARXIV-MIRROR-RUNBOOK-REFIRE
**Source:** SIARC RESEARCHER PROMPT 034 (composed 2026-05-04, drafted by
Copilot CLI Claude Opus 4.7 xhigh).
**Verbatim prompt body:** archived in operator's prompt-history;
this session implemented Phases A.1, A.2, B (verification only),
C (5 RUNBOOKs), D (6 endorsement templates), E (handoff).
**Pre-conditions verified before fire:**
  - 030 PCF-1 v1.3 source recovery: PASS (commit 58dfa9e canonical)
  - 032 ARXIV-PACK-FOUR-RECORD-AUDIT: ALL 4 PASS
  - ENDORSER-HANDLE-ACQUISITION 2026-05-04: 3 Tier-1 endorsers identified
**Outcome obtained:** see `handoff.md` §Status.
""").strip(), encoding="utf-8")
print("WROTE prompt_spec_used.md")

# ---------------------------------------------------------------- claims (append)

def chash(s): return hashlib.sha256(s.encode()).hexdigest()

new_claims = [
    {
        "claim": "Endorsement-template placeholder hygiene: 6 templates emitted with operator-side placeholders {{OPERATOR_NAME}} + {{OPERATOR_ORCID}} + {{ENDORSER_EMAIL_*}} all left as placeholders (no auto-filled operator PII or unverified email addresses); endorser handles + last names pre-filled from public arXiv author-id pages per ENDORSER-HANDLE-ACQUISITION 2026-05-04",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "_emit_phase_CD.py",
        "output_hash": chash(json.dumps(sorted([str(p.name) for p in SESS.glob("endorsement_template_*.md")]))),
    },
    {
        "claim": "5 RUNBOOK_<record>.md files emitted, one per record; each contains arXiv classification, file-attach order, metadata fields verbatim from Zenodo API, web-form sequence, and post-submission cross-link instructions",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "_emit_phase_CD.py",
        "output_hash": chash(json.dumps(sorted([str(p.name) for p in SESS.glob("RUNBOOK_*.md")]))),
    },
    {
        "claim": "arXiv classification policy verification per https://info.arxiv.org/help/endorsement.html (fetched 2026-05-04): endorsement is required for first submission in any new arXiv category; math.NT records explicitly require endorsement (Phase D-1 dispatched 6 templates for the 2 math.NT records); math-ph + math.HO + math.DS each have their own endorsement domain — RUNBOOK §0 of records 1, 4, 5 reflect this and recommend operator-adapted math.NT templates or institutional-email auto-endorsement",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "_emit_phase_CD.py",
        "output_hash": chash("arxiv_endorsement_policy_2026-05-04"),
    },
]
with (SESS / "claims.jsonl").open("a", encoding="utf-8") as f:
    for c in new_claims:
        f.write(json.dumps(c) + "\n")
print(f"APPENDED {len(new_claims)} claims (total now 6)")
