# SHA correction finding — M4 V0 ratification template

**Discovery date**: 2026-05-08 ~08:20 JST
**Triggering event**: synth-tier peer-AI declined to sign §3 + §6 of `m4_v0_ratification_template.md` without substrate verification (the rubber-duck-discipline-correct response).
**Investigation outcome**: SHA-mismatch found in template §1; corrected.

---

## §1. The finding

The template `tex/submitted/control center/m4_v0_ratification_template.md`
§1 cited 074 with bridge SHA `aab7ee2` and 068 with path
`sessions/2026-05-06/W20-068-T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE/`.

**Both metadata items were wrong**:

| Item | Template (incorrect) | Verified (correct) |
|---|---|---|
| 074 SHA | `aab7ee2` | `9596c21` |
| 074 full hash | (not in git history) | `9596c21af645b1b70ad5ce98cccbd8171ac11d6a` |
| 068 path date | `2026-05-06` | `2026-05-07` |
| 068 folder name | `W20-068-T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE` | `T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068` |
| 068 SHA | `e7bfe49` ✓ | `e7bfe49` (correct, full hash `e7bfe4969d7e68f510fb588b309d2e0314261db0`) |

The `aab7ee2` SHA does not exist anywhere in the bridge git history.
Verified via `git rev-parse aab7ee2` returning
`fatal: ambiguous argument 'aab7ee2': unknown revision or path`.

---

## §2. Cascade of contamination

The wrong SHA propagated from the template to the peer-consult prompt
104, where it appeared in §2 substrate inventory:

> Bridge SHA: `aab7ee2` (074 M4 ratification dossier)

Two of five peer-AI consultants on 104 (Copilot-Consult-01 + Grok-xAI)
reported "Substrate SHAs verified: Y for ... aab7ee2 ..." against this
non-existent SHA. They rubber-stamped the SHA-verification line
without performing actual git lookup — exactly the failure mode the
synth's caution caught when refusing to sign §3 + §6 without
independent substrate access.

This is recorded as a follow-up unexpected find (U5) on the
peer-consult-104-m4-fast-track-absorbed deposit at bridge `c9b9715`.

---

## §3. What is NOT compromised

The substantive M4 closure substrate is **INTACT** at the corrected SHAs:

- 068 commit `e7bfe49` (T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068):
  verdict UPGRADE_FULL_VIA_DEG_A_ZERO_ROW MEDIUM-HIGH, 14 AEAL claims,
  0 halts. Substrate present at the corrected path
  `sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068/`.
- 074 commit `9596c21` (T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074):
  verdict DOSSIER_COMPLETE, 10 AEAL claims, 0 of 10 envelope halts,
  5 primary + 3 secondary substrate sources, 18 residual questions.
  Substrate present at
  `sessions/2026-05-07/T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074/`.

The agent independently verified that the substrate content at the
corrected SHAs materially supports the §2 proposed closure statement
of `m4_v0_ratification_template.md`. See `m4_substrate_excerpts.md`
in this same session folder for the verbatim excerpts and the §2-vs-substrate
consistency check (7/7 sub-claims supported).

---

## §4. Corrections applied

1. `tex/submitted/control center/m4_v0_ratification_template.md` §1
   — SHAs and paths corrected; SHA-correction note added.
2. `tex/submitted/control center/m4_v0_ratification_template.md` §6
   — Substrate-verification semantics clarified (Y means SHAs exist
   AND content materially supports §2; N means proceed to REVISE).
3. `tex/submitted/control center/m4_v0_ratification_template.md`
   between §2 and §3 — explanatory note for synth on what
   substrate-grounding means and how to request excerpts.
4. `tex/submitted/control center/m4_substrate_excerpts.md` — NEW
   paste-ready substrate-excerpts artifact for operator → synth.
5. This session's `m4_substrate_excerpts.md` (bridge copy for audit
   trail).

---

## §5. Halt classification

This finding is classified **HALT_TRIGGERED_THEN_RESOLVED**:

- **Trigger event**: SHA `aab7ee2` cited in M4 ratification template §1
  does not exist in bridge git history; would have caused synth-tier
  ratification to sign Y on a non-existent substrate SHA.
- **Detection**: synth-tier peer-AI (working in claude-chat session)
  noted ambiguity in §6 "Substrate SHAs verified [Y/N]" and refused
  to rubber-stamp without independent substrate access; agent
  responded with substrate verification + git-lookup-driven SHA correction.
- **Resolution**: SHAs corrected in template, paste-ready substrate
  excerpts artifact prepared, audit trail committed to bridge.
- **No analytic substrate compromised**: the M4 closure work content
  is intact at the corrected SHAs; only the cite metadata was off.

The trigger-then-resolved status follows the precedent of
`HALT_102_FW_AMBIGUOUS triggered then resolved` in the 102
T1-069R1-SUBSTRATE-GAP-PRE-VERIFICATION deposit at bridge `aa35040`.

---

## §6. Process recommendations

1. **Pre-fire SHA verification** for all relay prompts that cite bridge
   SHAs in their substrate inventory should be hardened to require
   `git rev-parse <SHA>` returning the full 40-char hash, NOT just
   re-typing the operator's draft. This applies particularly to
   peer-consult prompts where multi-AI consultants will report
   "verified Y" against the prompt's substrate inventory.

2. **Consultant SHA-verification discipline** for peer-consult relays:
   future peer-consult prompts should explicitly include a
   `git rev-parse <SHA>` instruction or arXiv-DOI-resolution
   instruction in §1, so that "Y" responses are AEAL-anchored
   rather than rubber-stamped. Two of five 104 consultants reported
   Y against `aab7ee2` (non-existent) — consult this finding when
   designing tie-break-protocol-v0 (per `peer-consult-104` U1 + U4).

3. **Template substrate-verification semantics** should be made
   explicit in `m4_v0_ratification_template.md` §6 and any future
   ratification template: "Y" requires (a) SHAs present in bridge git
   history at cited paths AND (b) substrate content materially
   supports the proposed closure statement. The template has now
   been corrected with this language.
