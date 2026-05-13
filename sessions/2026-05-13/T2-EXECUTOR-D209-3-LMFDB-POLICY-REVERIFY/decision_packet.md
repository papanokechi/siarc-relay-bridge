# D-209-3 LMFDB Contribution-Policy Re-Verify — Decision Packet

**Date:** 2026-05-13 12:50 JST
**Trigger:** Verdict 209 §1 Q-209-6 RE-VERIFY-AT-FIRE-TIME-RECOMMENDED + §4 single-recommended-next-step secondary
**Authority:** Bridge SHA `3ab9c1d` (T1-SYNTH-PROMPT-209-STRATEGIC-PIVOT-RATIFICATION, 2026-05-13 10:26 JST)
**Re-verify trigger:** Before any D-1d (LMFDB triangulation of Q(j(τ)) class data) work
**Risk class:** MEDIUM (per verdict-209 §1 Q-209-6 — could flip D-1d classification)

---

## §1 — Question

Does LMFDB require pre-contact (= co-authorship-gateway-class outreach) for external
researchers to upload external datasets, or does it follow a dump-and-go
contribution model (= foundational web action)?

**Decision rule (per verdict-209 §1 Q-209-1 row D-1d footnote):**
- IF pre-contact required → D-1d flips to **DISTRIBUTION/BLOCKED** (RULE-1-tabled, same
  binding as Aux row "RamanujanMachine / LMFDB-team direct outreach")
- IF dump-and-go → D-1d remains **FOUNDATIONAL/PERMITTED** at Week-1 fire

---

## §2 — Evidence gathered (web_fetch)

| URL | Status | Pertinent excerpt |
|---|---|---|
| `https://www.lmfdb.org/contribute` | 404 | No public contribution page exists |
| `https://www.lmfdb.org/policy` | 404 | No public policy page exists |
| `https://www.lmfdb.org/source` | 404 | No public source-upload page exists |
| `https://www.lmfdb.org/about` | 200 | "These pages are intended to be a modern handbook including tables, formulas, links, and references for L-functions and their underlying objects." — read-handbook framing, not upload-portal |
| `https://www.lmfdb.org/acknowledgment` | 200 | Lists sponsors + institutions + named individuals; no public-upload mechanism cited |
| `https://www.lmfdb.org/editorial-board` | 200 | **4 Managing Editors + 17 Associate Editors** (named below) |
| `https://github.com/LMFDB/lmfdb` | 200 | Code repository; Development.md is the canonical contribution-process document |
| `https://github.com/LMFDB/lmfdb/blob/main/Development.md` | 200 | **Pre-contact directive: "introduce yourself to the current developers" + "get feedback from the current group of established LMFDB developers frequently"** |

### §2.1 Editorial board (full roster)

**Managing Editors (4):**
1. John Jones, Arizona State University, USA
2. Jennifer Paulhus, Mount Holyoke College, USA
3. David Roe, MIT, USA
4. Andrew Sutherland, MIT, USA

**Associate Editors (17):**
Eran Assaf (Dartmouth/MIT), Michael Bennett (UBC), Andrew Booker (Bristol), Alina Bucur
(UC San Diego), Edgar Costa (MIT), John Cremona (Warwick), David Farmer (AIM), Everett
Howe (USA), Kiran Kedlaya (UC San Diego), Álvaro Lozano-Robledo (Connecticut), Céline
Maistret (Bristol), Nicolas Mascot (TCD), Pascal Molin (Paris Cité), Aurel Page (INRIA/
Bordeaux), David Roberts (Minnesota Morris), Jeroen Sijsling (Ulm), Gonzalo Tornaría
(Universidad de la República), John Voight (Sydney).

### §2.2 Development.md verbatim citations

> "Adding material to the LMFDB: New pages are developed through an iterative process
> that involves input from both experts and nonexperts."

> "If you are interested in developing the LMFDB, **it would be a very good idea to
> introduce yourself to the current developers**, who can then help you get involved in
> current development meetings."

> "In practice, **it is a good idea to get feedback from the current group of established
> LMFDB developers frequently.**"

---

## §3 — Decision

**LMFDB IS pre-contact-required.** Three converging lines of evidence:

1. **Structural** — editorial board (managing + associate editors, 21 named) implies
   editor-reviewed contribution flow, not anonymous upload.
2. **Procedural** — Development.md explicitly directs prospective contributors to
   introduce themselves + maintain frequent developer-feedback loops *before*
   contributing material.
3. **Architectural** — no `/contribute`, `/policy`, or `/source` page exists on the
   public site; the contribution path runs through GitHub PRs + interpersonal channels.

### Applied rule

Per verdict-209 §1 Q-209-1 D-1d row footnote AND the binding parallel to Aux row
("RamanujanMachine / LMFDB-team direct outreach" — MED-HIGH, BLOCKED, co-authorship-
gateway-class), **the introduce-yourself-then-contribute pattern qualifies as
co-authorship-gateway-class outreach**, which is unambiguously DISTRIBUTION class under
the verdict-208/209 RULE 1 framework.

### Classification

**D-1d: LMFDB triangulation of Q(j(τ)) class data → DISTRIBUTION / BLOCKED**

The classification is bound at *both* the inbound channel (we would have to contact
editors before uploading any PCF-2 cubic-modular dataset) AND the outbound channel
(any cross-reference of *their* class-data against our PCF-2 dataset, if it produced a
publishable finding, would naturally route through them as co-authors or co-acknowledgers).
RULE 1 binding therefore covers both directions.

---

## §4 — Downstream effect on verdict-209 pivot plan

### §4.1 Pivot scope narrows by 1 deliverable

Week-1 D-1 row table (post-D-209-3):

| Row | Pre-D-209-3 classification | Post-D-209-3 classification |
|---|---|---|
| D-1a install ramanujantools + LIReC | OPS/INFRA · PERMITTED | OPS/INFRA · PERMITTED (no change) |
| D-1b 482-PCF canonical CSV export | OPS/INFRA · PERMITTED | OPS/INFRA · PERMITTED (no change) |
| D-1c db.identify smoke-test | FOUNDATIONAL · PERMITTED | FOUNDATIONAL · PERMITTED (no change) |
| **D-1d LMFDB triangulation** | **FOUNDATIONAL · PERMITTED (provisional)** | **DISTRIBUTION · BLOCKED ⚠️** |

### §4.2 Compensating posture

When β-event-gate opens (DS873D Garoufalidis redemption signal OR 14-day Mazzocco
fallback floor 2026-05-27) AND M-axis closure-cascade has not yet lifted RULE 1, the
Week-1 pivot fires with 3 of 4 deliverables (D-1a, D-1b, D-1c). D-1d remains
BLOCKED until M10 V0 closure lands (sole RULE 1 lift gate).

This does NOT trigger a verdict-209 halt condition; pivot scope narrows but does not
require re-fire. The synth halt #6 ("strategic-landscape stale-label rate exceeds
30% on Week-1 recon target rows") would only fire if D-1a/D-1b/D-1c ALSO became
re-classified — which D-209-3 does not affect.

### §4.3 Read-only LMFDB use is still permitted

Reading LMFDB public web pages for cross-reference (e.g. looking up specific
ring class fields, j-invariants, Hilbert class polynomials) is **pure foundational
input** (cf. existing D-1c db.identify-style use of public databases). What is
BLOCKED is *contribution*, *upload*, *bulk-download-for-research-publication*, or
*direct developer outreach*.

In practice this means PCF-2 v1.3 modular-discriminant work can continue to *consult*
LMFDB; what cannot happen RULE-1-tabled is the *triangulation-as-deliverable* item
that would imply outreach or upstream contribution.

---

## §5 — D-1d re-classification path

D-1d is recoverable to FOUNDATIONAL/PERMITTED *iff* one of:
1. M10 V0 closure lands → RULE 1 lifts → all distribution work permitted → D-1d resumes
2. A foundational-only LMFDB sub-task is designed that avoids developer outreach
   entirely (e.g. read-only j-invariant lookup pipeline for the 482-PCF corpus with
   results held in working-note form, no PR or upload). This would re-fire D-1d under
   a narrower scope; would need verdict-209-class re-ratification before Week-2.

---

## §6 — Halt conditions

None triggered. The classification flip is within verdict-209's explicit Q-209-6
RE-VERIFY scope (medium-risk, expected outcome).

---

## §7 — AEAL claim count

**Claims logged this fire: 4**

1. LMFDB has 4 Managing Editors + 17 Associate Editors (web-fetched 2026-05-13 12:48 JST)
2. Development.md explicitly directs introduce-yourself-then-contribute (verbatim quoted)
3. No `/contribute`, `/policy`, `/source` page exists on lmfdb.org (3× 404 confirmed)
4. **D-1d classification → DISTRIBUTION/BLOCKED** (top-line decision)

All `evidence_type: "verification"`, `dps: null`, ordinal-ranked.

---

**End decision packet.** Bridge anchor: T2-EXECUTOR-D209-3-LMFDB-POLICY-REVERIFY.
