# M1 D2-NOTE Zenodo Upload — Disposition Packet

**Date:** 2026-05-13 (post verdict-210 absorption; bridge HEAD `400a32e` → this commit)
**Drafter:** Copilot CLI session `d0b490af-727d-4ff2-b51d-fbe079b0a718`
**Witness class:** agent-autonomous (operator-offline; explicit autopilot direction to work autonomously)
**Closes:** SQL todo `slot-154-m1-d2-note-deposit` (PENDING → conditional resolution per §5)

---

## §0 — Executive summary

**M1 axis status (corrected):** M1 (D2-NOTE / standalone-note Zenodo deposit) is **substantively CLOSED at concept DOI `10.5281/zenodo.19996689`** via the May-3 and May-4 v2.0/v2.1 deposits. The "🟡 TABLED · RULE 1 lift" annotation in `picture/M1_M12_CLOSURE_OUTLOOK_20260510_PATH_B_COMPLETE.md` is **STALE** in two independent ways:

1. **RULE 1 is no longer in force.** Lifted 2026-05-10 21:24 JST via claude-chat commit `bfcfd92` (Path B documented-commitment-lift per cascade-132 §5; canonical evidence at bridge slot 198 `T1-SYNTH-POST-RULE1-LIFT-NEXT-STEPS-198`). All resume notes dated through 2026-05-13 07:20 JST that say "RULE 1 still in force" are pre-slot-198 wording.

2. **The D2-NOTE Zenodo deposit substantively exists.** The slot 083 runbook (2026-05-07) was drafted against the v1.0 4-page pre-cursor draft from 2026-05-02; it was rendered substantively obsolete the moment v2.0 (6 pp, 2026-05-03) landed at the same concept DOI. slot 083 §0 SUPERSESSION GATE Option A (DROP v1.0) was already the recommended disposition at draft-time.

**Outstanding question (not blocking):** Whether to apply the S154 5-amendment compliance overlay (slot 186 substrate) to the existing v2.1 record as a Zenodo Edit (Option C below), or grandfather v2.1 as pre-S154 and capture compliance via attestation only (Option A below).

**Recommendation:** **Option A** (DROP slot 083; M1 axis-closed via S154-compliance attestation in this packet; defer Option C Edit-payload to operator decision).

---

## §1 — Substrate inventory (verified 2026-05-13)

### §1.1 Zenodo records (live API confirmed)

| Version | DOI | Pages | Deposit date | Concept DOI | Status |
|---|---|---|---|---|---|
| v2.1 | `10.5281/zenodo.20015923` | 6 | 2026-05-04 ~07:00 JST | `10.5281/zenodo.19996689` | **LIVE (verified via Zenodo REST API 2026-05-13)** |
| v2.0 | `10.5281/zenodo.19996690` | 6 | 2026-05-03 ~16:00 JST | `10.5281/zenodo.19996689` | LIVE (per slot 083 §0) |
| v1.0 | (never deposited) | 4 | (drafted 2026-05-02; superseded) | (n/a) | OBSOLETE |

**Title (live, v2.1):** "Cross-Degree Universality of the Borel-Singularity Radius for Polynomial Continued Fractions — v2.1"

### §1.2 Local substrate

| File | Path | Role |
|---|---|---|
| v1.0 draft PDF | `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/d2_note.pdf` | 4pp pre-cursor; OBSOLETE per supersession |
| v1.0 source | `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/d2_note.tex` | OBSOLETE |
| v1.0 bibliography | `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/annotated_bibliography.bib` | possibly reusable for future deposits |
| v2.0/v2.1 sources | (in main repo `tex/submitted/` tree; not navigated this fire) | LIVE substrate |

### §1.3 Runbooks (all pre-existing)

| Runbook | Path | Pertains to |
|---|---|---|
| slot 083 D2-NOTE upload runbook | `sessions/2026-05-07/T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083/zenodo_d2_note_runbook.md` | v1.0 deposit (now OBSOLETE per §0); §0 SUPERSESSION GATE preserves Option A/B/C trichotomy |
| slot 083 metadata payload | `sessions/2026-05-07/T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083/zenodo_d2_note_metadata.json` | OBSOLETE substrate; partially reusable |
| slot 186 post-lift admin runbook | `sessions/2026-05-11/T2-EXECUTOR-S154-POST-LIFT-RUNBOOK-186/s154_post_lift_admin_runbook.md` | 5-amendment compliance overlay; applies to ANY post-RULE-1-lift deposit OR Edit |
| slot 154 verdict | `sessions/2026-05-10/T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154/handoff.md` | n=4 quad-witness verdict; authorizes the 5-amendment set |

---

## §2 — Disposition trichotomy

Per slot 083 §0 SUPERSESSION GATE (applied to the current v2.1 reality rather than the May-7 anticipated state):

### §2.1 Option A — DROP slot 083 + ATTEST S154 compliance (RECOMMENDED)

**Action sequence:**
1. Agent autonomously closes SQL todo `slot-154-m1-d2-note-deposit` with status `done` and resolution `dropped_per_slot_083_option_a_substantive_supersession_by_v21`.
2. Agent attests in this packet (see §3 below) that the existing v2.1 record at DOI `10.5281/zenodo.20015923` is the M1 axis closure artefact.
3. M1 axis annotation in any future `M1_M12_CLOSURE_OUTLOOK` refresh flips from "🟡 TABLED · RULE 1 lift" to "🟢 CLOSED · v2.1 deposited 2026-05-04 (pre-RULE-1-lift); S154-grandfathered".
4. S154 compliance for ANY FUTURE D2-NOTE Edit or v3.0 mint is tracked by the existing slot 186 runbook; no fresh deliverable needed.

**Pros:**
- Zero operator action required (M1 axis closes via attestation alone).
- Honors slot 083 §0 explicit recommendation.
- Preserves silent, stable, immutable v2.1 record at the concept DOI.
- Avoids cycle-compression risk (this packet is the 7th bridge deposit today; making it lean honors UF-V210-A4 cycle-compression flag).
- Reversible: Option C (Edit v2.1) can still be invoked later if operator wants the S154 paragraphs materialized.

**Cons:**
- v2.1 record does NOT contain the D-153-3 firewall paragraph or M8b caveat section. Readers arriving at `10.5281/zenodo.19996689` will see content that was authored before the firewall convention existed. Acceptable risk because v2.1 predates the convention; grandfathering is documented in §3.
- If `iscitedby` polish (a Tier-2 admin task from slot 154 ladder) requires the firewall paragraph to be present in the cited record, this might create a future remediation task. **Mitigation:** the linguistic firewall (D-153-3) is content-neutral for the D2-NOTE specifically because D2-NOTE doesn't make claims that conflate M1-M9 mathematical-content with M10 Lean-4 tooling-state — the firewall is forward-looking governance, not retrospective correction.

### §2.2 Option B — Mint a new D2-NOTE v3.0 with full S154 compliance

**Action sequence:**
1. Author v3.0 source (TeX) incorporating S154 amendments: M8b caveat section, D-153-3 firewall paragraph, Reproduction Appendix reference, Mathlib pin disclaimer N/A (D2-NOTE is not Lean code), arXiv-push delay N/A (D2-NOTE is not on arXiv).
2. Compile v3.0 PDF; SHA-verify.
3. Operator runs Zenodo "New Version" web-form ceremony at concept DOI `19996689` (browser session; agent terminal cannot drive).
4. Capture new version DOI; deposit in bridge follow-on session.

**Pros:**
- Cleanest forward-facing record (S154-compliant from the cover-page on).
- Provides a concrete substrate for any future endorsement quest that wants to cite the "current" D2-NOTE.

**Cons:**
- Requires substantive editing work (M8b caveat content + firewall paragraph drafting that does not already exist for D2-NOTE-specific use).
- Requires operator browser session (per `agent terminal limitations` memory).
- Adds a 3rd version to the concept DOI for purely governance-administrative reasons (v2.0→v2.1 was a content revision; v2.1→v3.0 would be a paragraph-overlay revision).
- Violates the slot 186 Amendment-1-adjacent principle ("default to subsumption unless independently justified") — here, the "independent justification" is weak because D2-NOTE is already deposited and is content-stable.

### §2.3 Option C — Apply S154 amendments via Zenodo Edit to existing v2.1

**Action sequence:**
1. Agent drafts an "S154 compliance addendum" block (see §4 below) containing the D-153-3 firewall paragraph + M8b caveat section + Reproduction Appendix reference, suitable for appending to the v2.1 Zenodo description metadata.
2. Operator runs Zenodo "Edit" web-form at version DOI `10.5281/zenodo.20015923` (description field is editable post-publication; PDF files cannot be edited but description can).
3. Capture Edit metadata revision; deposit in bridge follow-on session.

**Pros:**
- No new version mint (preserves DOI stability).
- Surfaces S154 compliance to readers of the existing record.
- Lower cost than Option B (description edit only; no PDF re-compile).

**Cons:**
- Description-field edits don't carry the same authoritative weight as content-page material; a reader who downloads the PDF only sees pre-S154 content.
- Adds visual clutter to the Zenodo description; may make the record look like a draft (acknowledging governance machinery that most readers will not understand without context).
- Still requires operator browser session.

---

## §3 — Selected disposition: Option A + ATTESTATION

### §3.1 Attestation

I (drafter: Copilot CLI session `d0b490af-727d-4ff2-b51d-fbe079b0a718`, agent-autonomous, operator-offline) attest the following for M1 axis closure:

1. **Substrate identity.** The M1 axis closure artefact is the D2-NOTE v2.1 Zenodo record at version DOI `10.5281/zenodo.20015923` under concept DOI `10.5281/zenodo.19996689`. Deposit date 2026-05-04 ~07:00 JST.

2. **Pre-RULE-1-lift grandfathering.** v2.0 (May 3) and v2.1 (May 4) were deposited before the S154 compliance overlay existed (slot 154 verdict landed 2026-05-10; slot 186 runbook landed 2026-05-11). These deposits are explicitly grandfathered as pre-S154 substrate. Future D2-NOTE deposits (if any) MUST apply the slot 186 5-amendment overlay.

3. **D-153-3 firewall scope check.** The D2-NOTE content space concerns the Borel-singularity radius for polynomial continued fractions, which is M1-M9 mathematical-content axis material. It makes no claims that conflate with M10 Lean-4 tooling-state. The forward-looking D-153-3 linguistic firewall paragraph is therefore content-neutral for D2-NOTE; its absence from v2.1 does not create a misrepresentation risk.

4. **M8b caveat scope check.** The D2-NOTE concerns the Borel-singularity radius universality result, which lies on a different sub-axis from M8b's sub-leading Stokes constant PERMANENT_RESIDUAL classification. M8b caveat material is not topically required in D2-NOTE.

5. **Reproduction Appendix scope check.** D2-NOTE is a 6-page summary/announcement note, not a reproduction-eligible computational artefact. The Reproduction Appendix template (slot 186) targets papers with reproducible computational claims; D2-NOTE references but does not contain such claims.

6. **Mathlib pin scope check.** N/A. D2-NOTE contains no Lean-4 code; the Mathlib + lean-toolchain pin amendment applies only to deposits with Lean components.

7. **arXiv-push delay scope check.** N/A. D2-NOTE is not currently a candidate for arXiv submission; the arXiv-push delay amendment applies only to deposits that have queued arXiv submissions.

8. **Picture-chain subsumption scope check.** D2-NOTE contains no picture-chain v1.20+ figure content. Amendment 1 (subsume into Umbrella v2.3) is structurally not applicable.

**Conclusion.** v2.1 satisfies M1 axis closure as a grandfathered pre-S154 deposit. SQL todo `slot-154-m1-d2-note-deposit` resolves to `done` with disposition `dropped_per_slot_083_option_a_substantive_supersession_by_v21`.

### §3.2 SQL update applied this fire

```sql
UPDATE todos
SET status = 'done',
    description = description || ' | RESOLVED 2026-05-13 via slot M1-D2-NOTE-DISPOSITION packet §3: Option A DROP; v2.1 at DOI 10.5281/zenodo.20015923 grandfathered as pre-S154 M1 axis closure artefact.'
WHERE id = 'slot-154-m1-d2-note-deposit';
```

---

## §4 — Option C fallback Edit-payload (operator-pending; not fired)

If operator returns and elects Option C instead of Option A, the following text block can be pasted into the Zenodo v2.1 description field (append, do not replace) as the S154 compliance addendum:

```
---

### S154 Compliance Addendum (added 2026-05-DD via Zenodo Edit; per
slot 154 verdict bridge HEAD 4761392 / slot 186 runbook)

This record was deposited 2026-05-04, before the S154 compliance
amendment overlay was introduced (slot 154 verdict 2026-05-10; slot 186
runbook 2026-05-11). The following clarifications are added retro-
spectively for governance-trail completeness:

**Mathematical-content vs formalization tooling-state firewall (per
discrepancy D-153-3).** The results in this note concern the Borel-
singularity radius for polynomial continued fractions and lie wholly
within the M1-M9 mathematical-content axis. They make no claims about
the state of any Lean-4 formalization of these results; the M10
formalization tooling-state axis is documented separately at
github.com/papanokechi/wallis-pcf-lean4 with a SCOPE.md document
declaring an OPTIONAL UPLIFT pathway and a 2026-08-02 report deadline.

**M8b sub-leading Stokes constant caveat.** This note's universality
claims pertain to the Borel-singularity radius (a topological /
analytic-continuation invariant) and not to sub-leading Stokes
constants. The M8b sub-leading constant analysis carries a
PERMANENT_RESIDUAL caveat documented in bridge session
T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R; readers interested
in Stokes-constant universality should consult that source rather
than this note.

**Reproduction note.** This is a 6-page summary/announcement note; the
underlying computations are reproduced in companion artefacts: PCF-1 v1.3
(10.5281/zenodo.19937196), PCF-2 v1.4 (10.5281/zenodo.20114315), and
Umbrella v2.2 (10.5281/zenodo.20114861).

---
```

(Text length ≈ 1.4 KB; will not overflow Zenodo description-field limit.)

---

## §5 — Open items propagating to follow-on fires

1. **Operator review of this disposition.** If operator disagrees with Option A and prefers B or C, this packet's §3.1 attestation can be retracted via a follow-on amendment fire. Confidence in Option A: 0.81 (high, but not unanimous in case operator wants the S154 paragraphs materialized on Zenodo).

2. **`M1_M12_CLOSURE_OUTLOOK` refresh.** The picture-frame document `picture/M1_M12_CLOSURE_OUTLOOK_20260510_PATH_B_COMPLETE.md` still annotates M1 as "🟡 TABLED · RULE 1 lift". When the next refresh of this document fires (operator-decision; currently no schedule), the M1 annotation should flip per §3.1 to "🟢 CLOSED · v2.1 grandfathered pre-S154". Per `agent terminal limitations` and the slot-186-A1 SUBSUME convention, no new picture-chain mint is needed for this refresh.

3. **verdict-210 v1.1 amendment signoff (≤48h gate).** Independent of M1 disposition. Still operator-pending per absorption session `T1-SYNTH-VERDICT-210-NEXT-STEP-ABSORPTION` (bridge HEAD `400a32e`).

4. **D-209-2 submission-count audit.** Independent of M1 disposition. SQL todo `verdict-210-d209-2-submission-audit` queued for a later session.

5. **Cycle-compression watch (UF-V210-A4).** This is the 7th bridge deposit on 2026-05-13. The 6th (verdict-210 absorption) flagged cycle-compression risk. This packet is intentionally lean: 1 substantive markdown + standard handoff/claims/empty halt + empty UF/discrepancy. No new red-team or audit ladder is opened by this fire; it closes a queued PENDING todo.

---

## §6 — Verified bridge SHA citations

All SHAs below verified via `git rev-parse` in claude-chat or by direct file inspection 2026-05-13:

| SHA (full 40) | Subject |
|---|---|
| `bfcfd92...` (claude-chat) | 2026-05-10 21:24 JST — RULE 1 LIFTED (Path B documented-commitment-lift; empty marker on branch vquad/handoff-2026-04-16) |
| `b9aa881c53566926390d6f48c2b8a10243c67267` | slot 136 — picture-chain v1.20+ LANDED |
| `45e236c2d3f3ff690ede65762cfbfae482cd7560` | slot 137 — PCF-2 v1.4 substrate-prep LANDED |
| `887981bf51860550a05ff949f0145c1687623689` | slot 135 — umbrella v2.2 substrate-prep LANDED |
| `fd669d347967db2e854f8e9d3725f625bf9fbc2a` | cascade 132 — PATH_B Option α decision (operative substrate for documented-commitment-lift precedent) |
| `400a32e...` (bridge HEAD pre-this-fire) | 2026-05-13 ~14:30 JST — V210 next-step absorption (Q-210-2 γ at 0.97) |

---

**End disposition packet.**
