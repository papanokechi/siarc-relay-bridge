# Operator dispatch checklist — P11 Math.Comp. defensive re-submit
# Bridge: sessions/2026-05-06/P11-COVERLETTER-MATHCOMP-DEFENSIVE/
# For:    Relay-046 STEP 5
# Status: defensive — execute ONLY IF JTNB returns a negative verdict.
#         Discard if JTNB returns accept / minor-revision.

This file is a pre-flight checklist for the operator at the moment a
JTNB negative verdict lands. Each unchecked box is a blocking item;
the submission cannot fire until every box is checked. Boxes are
ordered roughly by the order in which they will need to be resolved.

---

## A. Verdict + closure (¶4 of cover letter)

[  ] A1. JTNB editorial verdict text saved verbatim to a bridge
        session (suggested name: sessions/<YYYY-MM-DD>/
        P11-JTNB-VERDICT-RECEIVED/verdict_email_verbatim.md).

[  ] A2. JTNB consideration confirmed CLOSED — no further response
        owed, no automatic re-review window open.  Confirmation
        method: ack email from JTNB editorial office, OR explicit
        decision letter language "the manuscript is no longer
        under consideration".

[  ] A3. ¶4 of `p11_coverletter_mathcomp.txt` filled in with
        actual JTNB verdict outcome + verdict date + closure date
        (three placeholders flagged in the draft).

## B. Suggested referees vs Math.Comp. policy (¶5 — IMPORTANT)

[  ] B1. **POLICY-FIT DECISION (operator must make this).**
        Math.Comp. submission portal asks for a *suggested Editor*
        from the Math.Comp. editorial board, not a referee list.
        See https://www.ams.org/publications/journals/journalsframework/mcomsubmit
        Two options:

        Option B1a (RECOMMENDED): replace ¶5 of the cover letter
        with a suggested-Editor paragraph naming one or two
        Math.Comp. board members whose interests cover PCF /
        experimental number theory / PSLQ / computational
        Diophantine problems. Operator should browse the
        current editorial board at
        https://www.ams.org/journals/mcom/mcomedit
        and pick 1-2 names.  Candidate profile: a Math.Comp.
        editor with publications in computational number theory
        and either PSLQ-adjacent algorithms or PCF/Apéry-style
        irrationality.

        Option B1b: keep ¶5 as drafted (3 suggested referees),
        and note that this is unusual for Math.Comp.  Some
        editors may treat the list as informational; others may
        ignore it.  Lower-information path; works but suboptimal.

[  ] B2. Suggested-referee email verification (only if Option
        B1b chosen, OR if Option B1a is augmented with referees):
        - Zudilin: `w.zudilin@math.ru.nl` is verified working as
          of 2026-05-04 (bridge ZUDILIN-SEND-EVENT-LOG; the
          arXiv endorsement email landed and was acknowledged).
          Re-confirm at submission time at
          https://www.ru.nl/en/people/zudilin-w
        - Mazzocco: confirm institutional email at
          https://www.birmingham.ac.uk/staff/profiles/mathematics/mazzocco-marta.aspx
          Replace `[operator to confirm]` placeholder with the
          email surfaced there.
        - Garoufalidis: confirm institutional email at SUSTech
          faculty page (https://faculty.sustech.edu.cn/?orderby=year&iscss=1&ctype=1&id=stavrosgar)
          OR MPIM faculty page (https://www.mpim-bonn.mpg.de/people).
          Replace placeholder with the email surfaced there.

[  ] B3. If any of {Zudilin, Mazzocco, Garoufalidis} has an
        active CoI with the manuscript (e.g., recent
        co-authorship on the F(2,4) topic, or an arXiv
        endorsement that they completed for this paper's author
        — Zudilin DOES — note that this typically does not
        disqualify a referee suggestion for Math.Comp., but
        AMS editorial board will weigh it; flag it explicitly
        in the cover letter or in a short side-note in the
        submission portal cover field).

[  ] B4. **Zudilin endorsement-pair flag.** Zudilin endorsed the
        author's arXiv math.NT submission (PCF-1 v1.3) on
        2026-05-04. This is a known asymmetric relationship.
        Operator should disclose this in the cover letter ¶5
        (e.g., "Prof. Zudilin completed an arXiv math.NT
        endorsement for the author in 2026-05; this is an
        endorsement, not a co-authorship, but is disclosed in
        the spirit of full transparency").

## C. Submission-portal preconditions

[  ] C1. Math.Comp. submission portal account credentials known
        and tested.  Portal URL:
        https://ams.msp.org/submit_new.php?j=mcom
        Login is the operator's AMS member account (or a
        non-member account; AMS membership is not required for
        submission).

[  ] C2. AMS three-submission-per-12-months author limit checked.
        Confirm: how many AMS-published-or-under-review
        submissions has the author had in the prior 12-month
        rolling window? (P11 itself doesn't count yet.)
        If at limit, operator must wait — Math.Comp. portal
        will reject auto-submitted excess.

[  ] C3. Manuscript PDF current.  At submission, re-build
        f1_mathcomp_submission/main_R1.pdf from the current
        main_R1.tex with `pdflatex` + `bibtex` (twice) and
        confirm SHA-256 matches the cover letter's anchor.
        If the manuscript needs further revision (e.g., the
        SICF-reported four fatals were addressed since 2026-
        05-06), produce main_R2.tex and re-anchor the cover
        letter accordingly.  Re-run this checklist for the new
        manuscript SHA.

## D. arXiv pre-print + Zenodo

[  ] D1. arXiv pre-print landed.  Recommended: post the F(2,4)
        manuscript to arXiv math.NT before clicking Math.Comp.
        submit, so that the cover letter ¶3 reproducibility
        section can cite the arXiv ID as a stable URL.  If
        arXiv is not yet possible (endorsement window not yet
        passed), schedule + flag.

[  ] D2. Zenodo deposit fresh.  Confirm
        f1_mathcomp_submission/main_R1.pdf has a Zenodo DOI
        from a recent deposit (P7-P11 series; latest version
        within the prior 30 days).  Update DOI in cover letter
        ¶3 if needed.

## E. AEAL claim chain integrity (¶3)

[  ] E1. f1_mathcomp_submission/supplementary/claims.jsonl
        readable + valid JSON Lines.  Wc -l count matches the
        manuscript abstract's "35 AEAL-logged numerical
        claims" assertion.  If count drifted, update either
        the cover letter or the manuscript abstract for
        consistency.

[  ] E2. f1_mathcomp_submission/supplementary/f1_base_certificate.json
        reachable + readable + matches the SHA-256 referenced
        in the manuscript.

[  ] E3. github.com/papanokechi/siarc-relay-bridge bridge link
        in ¶3 resolves to a public-readable URL.  If the
        repository is private at submission time, switch to
        public OR replace the link with a Zenodo DOI of the
        bridge session tarball.

## F. Final pre-flight (operator-only)

[  ] F1. Strategyzer / Synthesizer review of this packet
        (CLI-tier review of the assembled cover letter +
        manuscript + suggested-Editor or referee block).
        DO NOT submit without this review.

[  ] F2. Operator click-confirmation moment.  Per rule2
        (no AI auto-submission), the agent layers stand by;
        only the operator clicks the Math.Comp. submission
        portal "submit" button.

---

## Anti-pattern check (one-shot, mandatory before submit)

[  ] X1. Confirm no concurrent submission elsewhere.  Search
        submission_log.txt for any active P11 submission line;
        the JTNB line should be `withdrawn` or `rejected` with
        a closure date PRIOR to the Math.Comp. submission date.

[  ] X2. Confirm same-author-same-venue anti-pattern not
        triggered.  Per the W19 SYNTHESIZER-Q38 portfolio
        collision flag, simultaneous P-papers at the same
        venue is the avoid-pattern.  Currently no other
        P-paper is active at Math.Comp.  Re-check at fire
        time.

---

## Estimated time-to-submit if checklist clears

If JTNB verdict lands negative AND every box above is checked
within a single working day, the Math.Comp. re-submit can fire
that same day (~4-6 hours of operator effort: verdict
transcription, B-block decisions, manuscript re-build, portal
session).  If items are blocked (e.g., D1 arXiv endorsement
still pending), the time stretches to 2-3 working days.

This compresses a typical multi-week "venue pivot" into a
1-day or 2-3-day operation, which is the entire point of the
defensive polish.
