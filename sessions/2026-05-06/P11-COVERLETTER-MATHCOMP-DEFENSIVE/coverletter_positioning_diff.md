# JTNB-cover vs Math.Comp.-cover positioning diff
# Session: P11-COVERLETTER-MATHCOMP-DEFENSIVE
# Date:    2026-05-06
# For:     Relay-046 STEP 2

---

## Source substrate

**JTNB cover-letter substrate (existing):** the "Cover letter to the
handling editor" block at the head of
`f1_mathcomp_submission/main_R1_response_template.tex`
(SHA-256 `A340C4A338887196338F734C47551CB9AE9AD8B0F28259AC393F83531973FBA4`).
This is *not* the original 2026-04-26 JTNB submission cover letter
(no standalone copy of which was preserved at
`tex/submitted/p11_jtnb_cover_letter.txt` — see ANOMALY in handoff).
It is the closest in-workspace JTNB-style cover for P11 — a response-
to-referee skeleton addressed to Prof. Boris Adamczewski, JTNB
handling editor.

**Math.Comp. expectations (anchor):** AMS Math. Comp. Submission page
snapshot at `mathcomp_author_instructions_snapshot.md`, source URL
`https://www.ams.org/publications/journals/journalsframework/mcomsubmit`,
fetched 2026-05-06. Plus 4–5 recent Math.Comp. published papers
selected as profile-matched precedents (listed in ¶2 of the cover).

---

## Per-paragraph diff

### ¶1 — Title + AMS subjects + result statement

**JTNB version (substrate):**
> "The manuscript proves the Completeness Conjecture for the F(2,4)
> family of degree-2 polynomial continued fractions and identifies
> the 24 transcendental-stratum families as Möbius transforms of π
> ... all sharing the structural coefficient ratio a₂/b₁² = -2/9
> and exhibiting Apéry-like recurrence structure."

**Math.Comp. shift:**
- Lead with the **algorithmic + classification statement**, not
  the transcendence theorem. The latter remains the headline
  *result*, but on a Math.Comp. cover letter the *method* —
  exhaustive 531,441-family enumeration + three-stage PSLQ-based
  pipeline at dps 300–500 + machine-checkable certificate — is
  the foreground.
- Include 2020 MSC primary + secondary classes (manuscript
  declares 11A55 / 11J70 / 11Y65 / 11J81; Math.Comp. expects
  primary + secondary in the cover too, for editor routing).
- Keep the result statement to ONE sentence.

### ¶2 — Why this venue (largest delta)

**JTNB version (substrate):** the JTNB substrate does not
contain a "why JTNB" paragraph at all (response-template
substrate is scoped to revision dialogue). The original
2026-04-26 JTNB cover letter (now lost) presumably argued
fit on number-theoretic-flavoured grounds: π-Möbius transcendence,
Apéry-style irrationality, completeness conjecture for an explicit
PCF family.

**Math.Comp. shift (largest reframing):**
- Foreground: experimental-mathematics methodology + reproducibility
  + algorithmic classification.
- Cite 4–5 Math.Comp. precedents from 2018–2025 with similar
  profile. Selected (all open in MathSciNet, all DOI-resolvable):
  - **Enge & Streng**, *"Schertz style class invariants for higher
    degree CM fields"*, Math. Comp. (2025), DOI 10.1090/mcom/4118
    — computational class-field invariants, algorithm + number
    theory mix, *direct profile match*.
  - **Tao, Trudgian, Yang**, *"New exponent pairs, zero density
    estimates, and zero additive energy estimates: A systematic
    approach"*, Math. Comp. (2025), DOI 10.1090/mcom/4138 —
    systematic computational enumeration of a number-theoretic
    parameter space; same shape as our F(2,4) sweep.
  - **Bellotti, Wong & Fiori**, *"Improved estimates for the
    argument and zero-counting function of the Riemann
    zeta-function"*, Math. Comp. (2025), DOI 10.1090/mcom/4133 —
    high-precision computational number theory; precedent for
    dps-level reporting + machine-checkable certificate.
  - **Luo & Zhou**, *"The classification and representations of
    positive definite ternary quadratic forms of level 4N"*,
    Math. Comp. (2025), DOI 10.1090/mcom/4130 — direct enumerate-
    and-classify of an arithmetic family, exactly P11's shape.
  - **Bettin, Grenié, Molteni & Sanna**, *"A lower bound for the
    number of Egyptian fractions"*, Math. Comp. (2026), DOI
    10.1090/mcom/4190 — recent (Jan 2026) precedent for an
    enumerative bound + AEAL-style auxiliary computation.

### ¶3 — Computational reproducibility (largest absolute add)

**JTNB version (substrate):** mentions dps 300–500 once, in the
context of the result statement. No standalone reproducibility
paragraph. No AEAL claim count. No Zenodo/arXiv link in the
template's cover block.

**Math.Comp. shift:**
- Add a reproducibility paragraph that Math.Comp. cover letters
  routinely include (cf. Bellotti–Wong–Fiori; Tao–Trudgian–Yang).
- Reference: 35 AEAL-logged numerical claims (per manuscript
  abstract); claim ledger at f1_mathcomp_submission/supplementary/
  claims.jsonl; certificate at f1_base_certificate.json;
  enumeration driver at f1_base_computation.py; bridge audit-trail
  link to the SIARC relay-bridge repository session record;
  Zenodo preprint DOI (per Zenodo deposits P7–P11).

### ¶4 — Prior submission disclosure (Math.Comp.-MANDATED add)

**JTNB version:** N/A (the JTNB submission had no prior submission
to disclose; F(2,4) base case was first submitted there).

**Math.Comp. shift (REQUIRED per AMS submission policy):**
- Math.Comp. requires explicit prior-submission disclosure: "No
  paper that has been previously published, or is being considered
  for publication elsewhere, should be submitted to the American
  Mathematical Society."
- For a JTNB-rejected re-submit, the disclosure must state:
  (a) prior submission to JTNB (ID JTNB-2400, submitted 2026-04-26);
  (b) JTNB editorial verdict (date + outcome);
  (c) confirmation that JTNB consideration is closed before the
      Math.Comp. submission goes in (no concurrent consideration).
- The template leaves verdict-date and outcome as plain-text
  placeholders for the operator to fill at fire time.

### ¶5 — Suggested referees (or, more accurately, suggested editor)

**JTNB version (substrate):** addresses Adamczewski directly as
handling editor; no "suggested referees" block in the substrate.

**Math.Comp. shift — and IMPORTANT POLICY-FIT WARNING:**
- The relay-046 prompt §3 directs ¶5 = "Suggested referees: 3
  names with affiliations + emails". This is the JTNB / Elsevier
  / Springer norm.
- Actual Math.Comp. policy: AMS expects authors to **suggest an
  appropriate Editor** from the Math.Comp. editorial board for
  the paper, NOT a list of suggested referees. (See:
  https://www.ams.org/publications/journals/journalsframework/mcomsubmit
  — quote: "The author should suggest an appropriate Editor to
  review the paper".)
- The defensive cover letter as drafted follows the relay
  prompt's structure (3 referees) BUT the operator should
  replace ¶5 at submission time with a suggested-Editor
  paragraph pointing to a Math.Comp. board member whose interests
  cover PCF / experimental number theory / PSLQ algorithmics.
  Candidate editors are flagged in `operator_dispatch_checklist.md`.
- Suggested-referee substrate (when ¶5 is retained as referees):
  the PCF-1 v1.3 arXiv endorser-track {Zudilin, Mazzocco,
  Garoufalidis} from bridge session
  `2026-05-04/ENDORSER-HANDLE-ACQUISITION/candidate_dossier.md`
  — three Tier-1 candidates with confirmed arXiv handles, ORCIDs,
  and recent math.NT or math.CA activity overlapping the F(2,4)
  bibliography.

### ¶6 — Author info + ORCID + funding

**JTNB version (substrate):**
> "Papanokechi / Independent researcher, Yokohama, Japan / ORCID:
> 0009-0000-6192-8273 / https://github.com/papanokechi"

**Math.Comp. shift (minimal):**
- Same identity block.
- Add: explicit "no funding to disclose" + "no conflict of
  interest" lines, which Math.Comp. cover letters routinely
  include (Math.Comp. is funded by AMS subscription revenue;
  authors disclose only what's actual).
- Add: corresponding-author mailing address (per AMS portal
  requirement for paper submissions; can be P.O. or institutional
  proxy).
