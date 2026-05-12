# Candidate Endorser Ranking v1 — Tunnell CNP cs.LO Endorsement Quest

> **Source:** Verdict 207 SECTION-(ii) per-candidate receptivity table + ranked priority order
> **Status:** v1 (post-verdict-absorption 2026-05-12); operator-verification gates **NOT YET CHECKED**
> **Bridge SHA at draft:** fb6907c (PROMPT-206-VERDICT-ABSORPTION pre-this-deposit)
> **Use:** Operator-facing artefact for round-1/2/3 dispatch sequencing. Pair with verdict_207.md SECTION-(iii) cadence.

---

## 🚦 Round-1 (Day 2-3 fire window) — three parallel asks

> ⚠️ **PRE-DISPATCH GATES** (do NOT fire any round-1 ask until ALL gates green):
> - `verdict-207-r1-abstract-rewrite` — abstract methodology-first reframe
> - `verdict-207-r3-readme-frontmatter` — GitHub README front-matter
> - `verdict-207-c6-carneiro-email-verify` — Carneiro email confirmed OR Massot substitution authorized
> - `verdict-207-zenodo-sync-verify` — Zenodo 10.5281/zenodo.19834824 confirmed = main.tex HEAD
> - `verdict-207-rule1-distribution-work-flag` — operator ack RULE 1 loose-reading for endorsement-quest fires

| Slot | Candidate | Score | Email status | Email | Ask-framing angle (verbatim from verdict) |
|---|---|---|---|---|---|
| **1** | **C6 Mario Carneiro** (CMU) | 7.5 / MEDIUM-HIGH | ⚠️ **NEEDS-VERIFY-24H** | _verify before send via:_ (a) Lean Zulip handle/email; (b) recent Mathlib commit-author email via `git log -1 --author='Carneiro'`; (c) CMU directory | **Code-first framing**: 2-sentence cover, 30-line Lean excerpt of involution lemma + axiom definition in email body, link to repo. Minimize prose. |
| **2** | **C3 Jeremy Avigad** (CMU) | 7.0 / MEDIUM-HIGH | PUBLIC-listed | `avigad@cmu.edu` (re-verify on CMU page) | **Meta-pattern framing**: lead with axiom isolation as general technique. **Cite his own writing on formalization principles** in the cover paragraph (e.g. his "Theorem Proving in Lean" reference; his essays on what formalization is for). |
| **3** | **C2 Kevin Buzzard** (Imperial) | 6.5 / MEDIUM-HIGH | PUBLIC-listed | `k.buzzard@imperial.ac.uk` (re-verify on Imperial page) | **Axiom-isolation pattern + FLT4 alignment**: 3-sentence cover max; include 10-line Lean snippet of `tunnell_conditional_on_BSD` definition. Reference FLT4's own axiom boundary as precedent. |

**Round-1 contingency (C6 email unresolvable within 24h):**
- Replace C6 Carneiro → **C4 Patrick Massot** (Paris-Saclay; `patrick.massot@universite-paris-saclay.fr` [PUBLIC-listed]; score 6.5/MEDIUM; framing: Mathlib-upstream `card_even_of_involution` pitch).
- Demote C6 to round-2 slot.

**Round-1 expected timeline:**
- Day 0-1: complete pre-dispatch gates (R1 abstract + R3 README + C6 verify + Zenodo sync + RULE 1 ack)
- Day 2-3: fire 3 parallel asks (3 separate emails, **NOT a CC**; each tailored to its framing angle)
- Day 2-14: silence-watch window
- Day 14: if all 3 silent → round-2 fire

---

## 🔄 Round-2 (Day 14 fire window) — three parallel asks if round-1 silent

| Slot | Candidate | Score | Email status | Email | Ask-framing angle |
|---|---|---|---|---|---|
| 4 | **C4 Patrick Massot** (Paris-Saclay) | 6.5 / MEDIUM | PUBLIC-listed | `patrick.massot@universite-paris-saclay.fr` | Mathlib-upstream candidate angle; lead with `card_even_of_involution` as upstream-contribution candidate; include lemma source verbatim; mention Mathlib-style idioms used. |
| 5 | **C5 Heather Macbeth** (Fordham) | 6.5 / MEDIUM | NEEDS-VERIFY | `hmacbeth1@fordham.edu` (re-verify on Fordham page) | Mathlib-upstream pitch + **explicit "I'm an independent researcher without institutional Lean contacts" framing** — her public behavior treats this as a positive signal. |
| 6 | **C7 Floris van Doorn** (Bonn) | 6.0 / MEDIUM | NEEDS-VERIFY | `vdoorn@math.uni-bonn.de` (re-verify on Bonn page) | Mathlib-upstream + axiom-isolation pattern; **mention HoTT-adjacent treatments of opaque definitions** as conceptual cousin. |

**Round-2 rationale diversity check** (per UF-207-8 portable principle): Massot=Mathlib-gatekeeper, Macbeth=outsider-mentor pattern, van Doorn=HoTT-conceptual-bridge — three orthogonal rationales. ✅

---

## 🔄 Round-3 (Day 28 fire window) — three parallel asks if rounds 1-2 silent

| Slot | Candidate | Score | Email status | Email | Ask-framing angle |
|---|---|---|---|---|---|
| 7 | **C9 Anne Baanen** (VU Amsterdam) | 6.0 / LOW-CONFIDENCE-MEDIUM | NEEDS-VERIFY | `t.baanen@vu.nl` (re-verify on VU page) | Standard Mathlib-upstream pitch; no special framing needed. |
| 8 | **C8 Johannes Hölzl** (VU Amsterdam) | 5.5 / MEDIUM | NEEDS-VERIFY | `j.r.holzl@vu.nl` (re-verify on VU page) | **Cross-system framing**: "does this axiom-isolation pattern translate to Isabelle's locale/sublocale machinery?" — invites engagement rather than yes/no. |
| 9 | **C10 Lawrence Paulson** (Cambridge) | 5.0 / MEDIUM | PUBLIC-listed | `lp15@cam.ac.uk` (re-verify on Cambridge page) | Cross-system + classical-mathematics framing; **reference his prime-number-theorem OR Gödel formalization as precedent** for "classical theorem, conjectural component" pattern. |

---

## 🚫 Skip / defer — three candidates explicitly excluded

| # | Candidate | Verdict | Re-evaluate at |
|---|---|---|---|
| C1 | **Asperti** (Bologna) | DEFER — active JFR pre-query (dual-role conflict if asked simultaneously) | After JFR verdict floor 2026-05-29 |
| C11 | **Cremona** (Warwick) | DEFER + structural caveat | After cs.LO primary endorsement lands. ⚠️ **Pre-contact check required:** verify Cremona has ≥3 cs.LO submissions before any cs.LO ask (he may only have math.NT endorsement privileges per UF-207-4). |
| C12 | **Cohen** (Bordeaux) | BLOCKED — R4 JNT suggested reviewer (cover letter §8 LIVE FIRE 2026-05-12) | After R4 verdict in (≥4-6 weeks) |

---

## 📋 Operator pre-flight checklist

Before firing **any** round-1 email:

- [ ] R1 done — abstract opening rewritten (methodology-first frame; +1.0 lift)
- [ ] R3 done — GitHub README front-matter updated with (a) zero-sorry count, (b) named axiom, (c) test count + OEIS scope, (d) 5-line Lean snippet (+1.0 lift)
- [ ] **C6 Carneiro email VERIFIED** (Lean Zulip / Mathlib commit log / CMU directory) — OR Massot substitution authorized
- [ ] Zenodo 10.5281/zenodo.19834824 confirmed = current main.tex HEAD (or accepted as v0.x historical with current release tag visible)
- [ ] RULE 1 distribution-work interpretation acknowledged by operator (loose reading by default per analogy with today's R7+R5+R4 fires)
- [ ] Lean toolchain pin in `congruent-relay/lean-toolchain` checked vs current Mathlib HEAD (optional polish; ~5 min)
- [ ] CI badge visible in README OR added (optional +0.5 lift; depends on GitHub Actions configured)

**Optional revisions** (pursue only if 48h budget permits):
- [ ] R2 — expand "Axiom-isolation pattern" contribution from 1 sentence to 2 with forward-reference to RH/Lindelöf/BSD-in-other-contexts (+0.5-1.0 lift)

---

## 📩 Round-1 dispatch tracking (operator fills post-fire)

| Slot | Candidate | Sent date/time JST | Email used | Subject line | Body SHA (for log) | Response | Response date |
|---|---|---|---|---|---|---|---|
| 1 | C6 Carneiro / C4 Massot (fallback) | _____ | _____ | _____ | _____ | _____ | _____ |
| 2 | C3 Avigad | _____ | _____ | _____ | _____ | _____ | _____ |
| 3 | C2 Buzzard | _____ | _____ | _____ | _____ | _____ | _____ |

Update this table post-fire; cross-link to submission_log.txt Pre-submission Inquiries §2 series (one subsection per candidate).

---

## 🧭 Strategy overlay reminders (from verdict SECTION-(iii))

1. **Primary category:** cs.LO. **Cross-list:** math.NT. **Explicitly NOT** math.LO primary (would be redirected to cs.LO).
2. **Cadence:** parallel-batches-of-three at 14-day intervals; not all-9-simultaneously, not one-at-a-time.
3. **DS873D math.NT chain** (PCF-1 v1.3 Zudilin→Mazzocco/Garoufalidis pivot) is **structurally orthogonal** to this cs.LO Tunnell quest — safe to run simultaneously.
4. **If a single endorser ends up redeeming both** chains (precautionary caveat only; current shortlists don't overlap): sequence with ≥30 days between asks.

---

**End candidate_endorser_ranking_v1.md.** Next version (v2) should be drafted post-round-1-fire with verification-status column updated to CONFIRMED/REJECTED and dispatch tracking populated.
