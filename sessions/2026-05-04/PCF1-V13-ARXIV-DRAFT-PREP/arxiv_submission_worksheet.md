# arXiv submission worksheet — PCF-1 v1.3

**Date prepared:** 2026-05-04 (~18:18 JST)
**Purpose:** consolidated copy-paste sheet for the operator's
arXiv web-form submission corresponding to the Zudilin
endorsement request sent 2026-05-04.
**Per Rule 2:** the agent does NOT submit on the operator's
behalf. This worksheet exists so the operator can fill in
arxiv.org/submit field-by-field with verified content.

---

## §0 Workflow at a glance

```
┌──────────────────────────────────────────────────────────────┐
│ 1. Operator: arxiv.org/submit  →  Start new submission       │
│ 2. arXiv:    issues 6-character endorsement code XXXXXX      │
│ 3. Operator: forwards code to Zudilin (template in §6)       │
│ 4. Zudilin:  arxiv.org/auth/endorse  →  enters code XXXXXX   │
│ 5. arXiv:    notifies operator endorsement granted           │
│ 6. Operator: returns to draft, completes upload + metadata   │
│ 7. arXiv:    issues arXiv ID arXiv:YYMM.NNNNN                │
│ 8. Operator: cross-link Zenodo record 19937196 (relIdent)    │
│ 9. Operator: append arXiv ID to submission_log Item 23       │
└──────────────────────────────────────────────────────────────┘
```

The operator can start at step 1 NOW (before Zudilin replies).
Starting the draft is what generates the endorsement code that
Zudilin needs. The draft can sit at "awaiting endorsement"
indefinitely; arXiv does not auto-expire incomplete drafts.

---

## §1 arXiv account prerequisites

- Operator's existing arXiv account
- ORCID-verified preferred (operator has ORCID
  0009-0000-6192-8273 — confirm linked in arXiv profile)
- This is a first-time submission to math.NT (and to arXiv
  more generally for SIARC), so personal endorsement is
  required (auto-endorsement is not an option per arXiv policy
  update 2025-12-10: requires institutional email AND prior
  arXiv math authorship; operator meets neither).

---

## §2 File-attach checklist (in order)

Upload to arXiv "Add Files" widget in this order. **All paths
absolute on operator's local disk:**

```
C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\PCF1-V13-ARXIV-DRAFT-PREP\pack\p12_pcf1_main.tex
C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\PCF1-V13-ARXIV-DRAFT-PREP\pack\00README.txt
C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\PCF1-V13-ARXIV-DRAFT-PREP\pack\abstract.txt
```

**Do NOT upload `p12_pcf1_main.pdf`** as primary source. arXiv
requires .tex source for math papers; uploading the PDF
alongside the .tex can cause "PDF detected, source ambiguous"
errors. The .pdf is preserved in the pack only as a local
verification artefact.

If arXiv's auto-compile fails (very rare for a self-contained
amsart .tex with inline thebibliography), the operator can
re-attempt with `p12_pcf1_main.pdf` as the only source, marking
the submission as "PDF-only — TeX compile failed". This is a
fallback, not the default.

### Pack hash verification (run at submit time if desired)

```powershell
Get-FileHash "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\PCF1-V13-ARXIV-DRAFT-PREP\pack\p12_pcf1_main.tex" -Algorithm SHA256
# Expected: E83BB377F297DBF0837FACBA257F227DF4579E6A3518C139E3146F17174BE301

Get-FileHash "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\PCF1-V13-ARXIV-DRAFT-PREP\pack\p12_pcf1_main.pdf" -Algorithm SHA256
# Expected: 63420DBF4ABB7124672F522C37FC04EBDB3F6694AC39959456B2890D9788FF5E
```

---

## §3 arXiv classification

```
Primary:    math.NT          (Number Theory)
Cross-list: math.CA          (Classical Analysis and ODEs)
```

Cross-list rationale (paste into arXiv's optional rationale
field if asked):

> The paper's central object is the balanced discriminant
> Δ = β² − 4αγ of degree-2 polynomial continued fractions, a
> number-theoretic invariant in math.NT. The Stokes-exponent
> diagnostic and Painlevé III(D₆) prototype place the work
> equally in classical analysis (math.CA), where Painlevé
> transcendents and connection-coefficient asymptotics are
> studied.

MSC 2020 codes (already in TeX line 59; restate if arXiv asks):
- Primary: 11J70, 11J81
- Secondary: 34M55, 11G15

---

## §4 Metadata fields (paste verbatim into arXiv form)

### Title

```
Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions
```

### Authors

```
Papanokechi
```

(Single author. Affiliation field: "Independent Researcher,
Yokohama, Japan".)

### Abstract (single paragraph, paste as-is)

```
We propose a transcendence predicate for degree-two polynomial continued fractions (PCFs) based on the sign of the balanced discriminant Delta = beta^2 - 4*alpha*gamma of the denominator polynomial b_n = alpha*n^2 + beta*n + gamma. Working inside the Spec(K) classification framework of Papanokechi (2026), we present a v5 upgrade of the schema that fixes two cross-paper inconsistencies and adds the Stokes exponent and connection-coefficient proxy as components 6 and 7. Our central empirical finding is a sharp dichotomy across 30 degree-two families: 24 F(2,4) Trans-stratum families have Delta in {+1, +8} and admit elementary closed forms, whereas 6 candidates with Delta in {-3, -4, -7, -11, -20, -28} all return PSLQ non-detection against an 18-element constants basis at working precision 220 digits and integer bound 10^10. The V_quad family (Delta = -11) is the explicit Painleve III(D_6) prototype with parameters alpha = 1/6, beta = gamma = 0, delta = -1/2. For QL01 (Delta = -3) the Eisenstein-root deformation yields a Stokes exponent S in {0.770, 0.819} < 1, a fractional-power singularity that is the qualitative signature of a Painleve / Stokes obstruction. Conjecture A v5 formalises the dichotomy. Version 1.3 folds in the WKB exponent identity (Theorem 5.bis) and the revised Conjecture A part (iv) per Sessions D, E, and E'. The session chain that produced these results is itself an instance of the AEAL four-class evidence gate methodology.
```

(arXiv strips LaTeX from abstracts; this plain-text version
matches the .tex `\begin{abstract}` content with math symbols
expanded.)

### Comments

```
16 pages. Mirror of Zenodo record 10.5281/zenodo.19937196.
```

### Report-no

```
(leave blank)
```

### DOI

```
10.5281/zenodo.19937196
```

### License

```
CC-BY-4.0
```

(matches Zenodo deposit; arXiv supports CC-BY-4.0 from the
standard license dropdown.)

### Journal-ref

```
(leave blank — manuscript is on Zenodo, not in a journal)
```

---

## §5 arXiv web-form click-through

1. https://arxiv.org/submit → **Start new submission**
2. **Choose category** — primary `math.NT`, then click
   **Add another** for cross-list `math.CA`
3. **License** — select CC-BY-4.0 from the dropdown
4. **Add files** — upload in the order listed in §2
5. **Verify auto-compile** — arXiv runs pdfTeX on the .tex.
   The compiled PDF should be 16 pages, byte-similar (not
   byte-equal — different `/CreationDate`) to the local
   `p12_pcf1_main.pdf`. If page count differs from 16, halt
   and review.
6. **Metadata** — paste Title, Authors, Abstract, Comments,
   DOI, License from §4
7. **Endorsement page** — arXiv displays a 6-character
   endorsement code (alphanumeric, e.g. `XX1234`). **Copy
   this code** — it is what Zudilin needs in the follow-up
   email of §6.
8. **Save draft** — leave the submission in draft state until
   Zudilin endorses. Do NOT click "Submit" yet.
9. After Zudilin enters the code at arxiv.org/auth/endorse and
   arXiv emails the operator confirming endorsement, return to
   the draft and click **Submit**.
10. arXiv assigns an ID `arXiv:YYMM.NNNNN`. Note this for §7.

---

## §6 Follow-up email to Zudilin (forwarding endorsement code)

Send this AFTER step 7 of §5 above (after arXiv issues the
6-character code), as a reply to the original 2026-05-04
endorsement-request thread. **Do NOT send before arXiv issues
the code — there is no code to forward yet.**

```
To:       w.zudilin@math.ru.nl
Subject:  Re: arXiv math.NT endorsement request — Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions
Date:     {{OPERATOR_FILLS_AT_SEND_TIME}}
```

---

Dear Prof. Zudilin,

Thank you again for considering my endorsement request of
2026-05-04. I have now started the arXiv submission and have
the endorsement code:

  **Endorsement code: XXXXXX**

  (where XXXXXX is the 6-character alphanumeric code arXiv
  displayed to me; please replace with the actual code)

To complete the endorsement, please visit:

  https://arxiv.org/auth/endorse

Sign in to your arXiv account, enter the code above, and
confirm the endorsement for the math.NT category. The action
takes approximately one minute.

The submission, once endorsed and posted, will be a verbatim
mirror of Zenodo record 10.5281/zenodo.19937196 (PCF-1 v1.3,
16 pages, CC-BY-4.0). I am happy to send you the PDF directly
if it is helpful for your endorsement decision.

If for any reason you would prefer not to endorse — for
example, if your math.NT endorsement privileges are not
currently active or if you have reconsidered the topical fit —
please simply reply to that effect. No follow-up will be sent.

With many thanks,

{{OPERATOR_NAME}}
Yokohama, Japan
ORCID: 0009-0000-6192-8273
{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}

---

## §7 Post-submission checklist

Once arXiv assigns `arXiv:YYMM.NNNNN`:

1. **Append to submission_log Item 23** (PCF-1 v1.3 was Item
   23? — recheck; PCF rational-contamination was Item 23,
   F&A-rejected. PCF-1 v1.3 is currently a Zenodo-only record
   and may not have a submission_log entry yet. If not, add a
   new entry for the arXiv submission, mirroring Item 23
   format.)

2. **Update tex/submitted/submission_log.txt
   ENDORSEMENT-EVENTS section** — close out EVENT 1 with:
   ```
   STATUS UPDATE 2026-{MM}-{DD}: Endorsement granted by
   Zudilin; arXiv ID arXiv:YYMM.NNNNN issued.
   ```

3. **Update Zenodo record 19937196 → Related identifiers** —
   add a row:
   ```
   Identifier: arXiv:YYMM.NNNNN
   Relation:   IsIdenticalTo
   ```
   This completes the Zenodo↔arXiv bidirectional cross-link
   per arXiv's recommended practice.

4. **Update tex/submitted/CMB.txt** — change SUBMISSION
   PORTFOLIO row P-PCF1-v13 status from "arXiv endorsement
   requested 2026-05-04 (Zudilin)" to "Published (Zenodo +
   arXiv:YYMM.NNNNN)".

5. **Update _INDEX.txt** with the post-submission event entry.

6. **Confirm submission visible** at
   https://arxiv.org/abs/YYMM.NNNNN ~24h after posting (arXiv's
   standard announcement cycle).

7. **Strategic implication** — the math.NT endorsement applies
   to the operator-account-as-a-whole for math.NT, so PCF-2
   v1.3 (also math.NT primary) can be submitted next without
   a fresh endorsement. Likewise math-ph (CT v1.3) and math.HO
   (umbrella, T2B) still require their own first-time
   endorsements per ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE
   inventory.

---

## §8 Halt conditions during submission

If any of the following occurs during the arXiv web-form
flow, halt and consult before proceeding:

- Auto-compile produces page count ≠ 16
- arXiv flags missing macros, undefined references, or font
  errors in the .tex
- arXiv's PDF preview shows visibly different content from
  the local `p12_pcf1_main.pdf` (e.g., abstract truncated,
  missing sections)
- arXiv rejects CC-BY-4.0 license (should not happen; arXiv
  has supported CC-BY-4.0 for years)
- arXiv issues an endorsement code that the operator's
  follow-up email cannot deliver to Zudilin (delivery failure
  bounce); fallback to alternate endorsers per
  ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE inventory (Mazzocco
  or Garoufalidis)

---

## §9 Provenance + AEAL chain

- **Pack source:** PCF1-V13-ARXIV-DRAFT-PREP session (this
  session) — fresh copy of canonical 16pp pack from
  `sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3/`
  + canonical PDF from
  `sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/`
- **00README erratum applied:** original pack's 00README.txt
  contained PCF-2 v1.3 DOIs (concept 19941678; record 19963298)
  in error; corrected here to PCF-1 v1.3 DOIs (concept
  19931635; record 19937196). Hash of corrected README:
  `708a537e1dc512b4...`
- **TeX SHA-256:** `e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301`
  (byte-equal to canonical 2026-05-01 source per 030/034 manifests)
- **PDF SHA-256:** `63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e`
  (byte-equal to Zenodo deposit per 034 PHASE A.2 5/5 PASS audit)
- **Zenodo source-of-truth:** 10.5281/zenodo.19937196
  (concept 10.5281/zenodo.19931635; PCF-1 v1.3, 16 pp, 2026-05-01)
- **Endorsement-request email send event:** ZUDILIN-SEND-EVENT-LOG
  bridge commit 65dd9aa (operator confirmed send 2026-05-04
  ~18:12 JST to w.zudilin@math.ru.nl)
- **Send-target verification chain:** Zudilin contact verified
  against math.ru.nl primary homepage + Radboud faculty profile
  on 2026-05-04 ~17:50 JST (synthesizer-Claude pre-verification)

---

## §10 Out of scope

- Submitting on operator's behalf (Rule 2)
- Forwarding the endorsement code to Zudilin on operator's
  behalf (the §6 template is for operator's mail client;
  agent does NOT operate the mail client per Rule 2)
- Modifying the .tex source (manuscript content is frozen at
  v1.3 / 2026-05-01; any further changes would constitute a
  v1.4 and would re-trigger the AEAL deposit cycle)
- Pre-staging arXiv tarballs for the OTHER 4 records
  (umbrella, PCF-2, CT, T2B); deferred until Zudilin endorses
  and the math.NT pivot lands. PCF-2 v1.3 will be the natural
  next math.NT submission per §7 step 7.
