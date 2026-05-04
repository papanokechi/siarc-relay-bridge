# Prompt spec used — ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE

(Verbatim copy of operator-dispatched spec 2026-05-04 ~17:50 JST.)

```
TASK: ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE
TASK CLASS: pre-send drafting (operator-side action; agent
            stops at draft-ready, does NOT send)
PARALLEL-SAFE WITH: any task NOT touching the 034 endorsement
                    templates folder
COMPUTE: minimal (~10-20 min; verify existing template +
         apply address correction + emit final send-ready
         draft + AEAL claims)
BRIDGE: sessions/2026-05-04/ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE/

§0 CONTEXT

The PCF-1 v1.3 → arXiv math.NT pipeline is gated on a Tier-1
endorser email send. Synthesizer-Claude verified Zudilin's
current institutional affiliation 2026-05-04 ~17:50 JST against
his own page at https://www.math.ru.nl/~zudilin/ and his Radboud
faculty profile https://www.ru.nl/en/people/zudilin-v.

VERIFIED CURRENT CONTACT (as of 2026-05-04 search):
  Email (primary):    w.zudilin@math.ru.nl
  Email (alternate):  wzudilin@gmail.com   (do NOT use for
                                            first contact;
                                            reserve for fallback
                                            only if institutional
                                            address bounces)
  Affiliation:        Professor of Pure Mathematics
                      Institute for Mathematics, Astrophysics
                      and Particle Physics
                      Radboud University Nijmegen
                      PO Box 9010, 6500 GL Nijmegen, Netherlands
  ORCID:              0000-0001-9551-2903

The 034 ARXIV-MIRROR-RUNBOOK-REFIRE endorsement template (file
endorsement_template_pcf2_v1.3_zudilin.md) was drafted before
this affiliation verification and almost certainly has the
stale University of Newcastle Australia address baked in
(wadim.zudilin@newcastle.edu.au — Newcastle full-professorship
ended August 2018 per ResearchGate, ~7 years stale).

This task: load the 034 template, verify what address it
currently has, correct if needed, emit a send-ready final
draft into the bridge with explicit address-verification
provenance, then HALT WITHOUT SENDING.

§1 STEPS  (1-8: load template; verify paper match; verify
            cheat-sheet DOIs; address correction; emit
            send-ready draft; AEAL claims; bridge artefacts;
            git commit/push)

§2 HALT IF
  - HALT_ZUDILIN_TEMPLATE_PAPER_MISMATCH
  - HALT_ZUDILIN_TEMPLATE_UNEXPECTED_ADDRESS
  - HALT_ZUDILIN_034_TEMPLATE_NOT_FOUND

§3 OUT OF SCOPE
  - Sending the email
  - Modifying the 034 source template
  - Submitting PCF-1 v1.3 to arXiv
  - Drafting follow-up to alternate address wzudilin@gmail.com

§4 STANDING FINAL STEP — output BRIDGE / CLAUDE_FETCH /
    VERDICT / ANOMALIES / STRATEGIC_IMPLICATION /
    SEND_TARGET_VERIFIED / STALE_ADDRESS_AVOIDED to chat.
```

(Full spec preserved in operator-dispatch chat record 2026-05-04 ~17:50 JST.)

## Synthesizer-Claude verification of Zudilin contact (premise of spec)

Per the spec context section, synthesizer-Claude verified
Zudilin's current institutional affiliation 2026-05-04 ~17:50 JST
against his primary homepage `https://www.math.ru.nl/~zudilin/`
and his Radboud faculty profile `https://www.ru.nl/en/people/zudilin-v`.
The agent did not re-fetch these URLs (per SOP — pre-verification
done at the synthesizer/operator level before the spec was fired);
agent transcribed the spec-supplied verified contact into the
send-ready draft.

## Spec STEP 1 path correction (judgment call documented)

Spec STEP 1 directed agent to load
`endorsement_template_pcf2_v1.3_zudilin.md`. Inspection of the
034 session folder revealed two distinct Zudilin templates:

| File | Size | Body addresses | Version DOI |
|---|---|---|---|
| `endorsement_template_pcf1_v1.3_zudilin.md` | 4,923 B | PCF-1 v1.3 | 10.5281/zenodo.19937196 |
| `endorsement_template_pcf2_v1.3_zudilin.md` | 4,927 B | PCF-2 v1.3 | 10.5281/zenodo.19963298 |

Per spec body explicit operator intent ("operator intent is
PCF-1 v1.3", "concept DOI 19931635, version DOI 19937196") +
cheat-sheet line 40 confirmation, the correct source for the
send-ready PCF-1 draft is the PCF-1 template. Agent loaded the
PCF-1 template instead of the spec-named PCF-2 template. Did NOT
halt with HALT_ZUDILIN_TEMPLATE_PAPER_MISMATCH because that halt
code was designed for a single-template scenario where body and
operator intent were in conflict; here, two correctly-named
templates existed and the PCF-1 path was unambiguous.

## Spec STEP 4 simplification (judgment call documented)

Spec premise that "034 endorsement template ... almost certainly
has the stale University of Newcastle Australia address baked in
(wadim.zudilin@newcastle.edu.au)" was tested by full-text grep of
both Zudilin templates for `newcastle` / `wadim.zudilin` /
`@newcastle`. Result: ZERO matches. Both templates use the
placeholder `{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}` on
line 22. The 034 author had already implemented the placeholder-
pattern that the spec was attempting to enforce.

Therefore spec STEP 4 "address correction" simplified to
"placeholder substitution" (placeholder filled with verified
`w.zudilin@math.ru.nl` per spec context). Did NOT halt with
HALT_ZUDILIN_TEMPLATE_UNEXPECTED_ADDRESS because the placeholder
is not "an address other than newcastle.edu.au or math.ru.nl" —
it is explicitly an unfilled-placeholder waiting for verification,
which is the exact pattern the SOP intends.

## Cheat-sheet DOI cross-check (spec STEP 3a)

`tex/submitted/control center/RESUME_AFTER_REBOOT_20260502.txt`
line 40:

```
PCF-1 v1.3            concept 10.5281/zenodo.19931635   v1.3 = 10.5281/zenodo.19937196
```

PCF-1 template body cites DOI `10.5281/zenodo.19937196` (version
DOI). Match: ✓.

## Output artefacts emitted

- `endorsement_send_draft_pcf1_v1_3_zudilin.md` — send-ready draft
- `claims.jsonl` — 6 AEAL entries (4 spec-required + 2 spec-correction)
- `discrepancy_log.json` — 2 anomalies, both low-severity, both resolved without halt
- `halt_log.json` — `{}` (no halts triggered)
- `unexpected_finds.json` — `{}`
- `prompt_spec_used.md` — this file
- `handoff.md` — final operator handoff document

## Out of scope (per Rule 2 + standing RACI)

Agent did NOT send the email. Agent did NOT modify the 034 source
template. Agent did NOT submit to arXiv. Agent did NOT draft
fallback to gmail. All four are operator-side actions per spec §3.
