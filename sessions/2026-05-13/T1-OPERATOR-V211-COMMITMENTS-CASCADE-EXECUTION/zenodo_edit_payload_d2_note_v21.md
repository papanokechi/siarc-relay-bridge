# Zenodo Edit payload — D2-NOTE v2.1 S154 Compliance Addendum

**Target record:** D2-NOTE v2.1
**Version DOI:** `10.5281/zenodo.20015923`
**Concept DOI:** `10.5281/zenodo.19996689`
**Deposited:** 2026-05-04 ~07:00 JST
**Edit type:** Description-field append (S154 Compliance Addendum)
**Status:** ✅ READY-TO-PASTE · 🟡 OPERATOR BROWSER ACTION PENDING

**Anchored to:** V211 Q-211-2 β (axis-local effects only); M1 disposition
packet §4 (Option C fallback Edit-payload, bridge `1f48c69b52e3100d4f35ebd06b04a2044e7dd3f1`)

---

## §1 — Why this payload is staged but not fired

Per the `agent terminal limitations` memory, Zenodo Edit operations
require an interactive browser session (operator credential, MFA, page
navigation, paste, Save Draft + Publish). The Copilot CLI agent cannot
drive a Zenodo browser ceremony.

This file stages the ready-to-paste payload + browser steps. The operator
executes the actual Edit when convenient. After Edit lands, the operator
should reply in a future session with the new version DOI (Zenodo may
mint a new version on description edit) so the SQL todo
`opportunistic-option-c-d2-note-edit` can be closed.

---

## §2 — Browser steps for operator

1. Navigate to `https://zenodo.org/records/20015923` while logged in as the
   record owner.
2. Click **Edit** (top-right of record header).
3. Scroll to the **Description** field.
4. Place cursor at the END of the existing description content.
5. Paste the block in §3 verbatim (Markdown is rendered by Zenodo's HTML
   sanitizer; `---` horizontal rules render correctly).
6. **Replace `2026-05-DD`** in the addendum heading with the actual date you
   click Publish (e.g. `2026-05-13`).
7. Click **Save Draft**.
8. Review the rendered preview; confirm horizontal rules and section headers
   display.
9. Click **Publish** (this may mint a new version DOI; record both the new
   version DOI and the unchanged concept DOI for the SQL close note).
10. Reply in a future Copilot CLI session with:
    - new version DOI (or "no new version minted")
    - actual edit-publish timestamp (JST)

---

## §3 — Ready-to-paste addendum block

Copy everything BETWEEN the BEGIN PAYLOAD and END PAYLOAD markers below:

```
=== BEGIN PAYLOAD ===

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

=== END PAYLOAD ===
```

Payload length: ≈1.4 KB (well under Zenodo description-field limit).

---

## §4 — Verification checklist for operator post-Publish

After Publish, verify on the Zenodo public page:

- [ ] Addendum heading renders as **bold H3** (`### S154 Compliance Addendum...`)
- [ ] Three horizontal rules render correctly (one before heading, one between
      "Reproduction note" paragraph and the closing rule, one after)
- [ ] Three bolded sub-section labels render: "Mathematical-content vs...",
      "M8b sub-leading Stokes constant caveat.", "Reproduction note."
- [ ] The date placeholder `2026-05-DD` was replaced with the actual date
- [ ] The three companion-artefact DOIs (PCF-1 / PCF-2 / Umbrella) render as
      plain text (Zenodo does not auto-link DOIs in descriptions; that's OK)
- [ ] Record's concept DOI `10.5281/zenodo.19996689` is unchanged
- [ ] If a new version DOI was minted, note it for the follow-on SQL close

---

## §5 — Fallback / abort criteria

If during browser ceremony the operator observes:

1. **Zenodo error preventing Save Draft.** Halt; report error text in a
   future Copilot CLI session; we'll diagnose (typical causes: stale
   browser session, MFA expiry, transient API outage).
2. **Description preview shows mojibake or HTML-encoded characters.** Halt;
   the payload contains only ASCII + `---` and should sanitize cleanly. If
   not, abort the Edit and report so we can debug the sanitizer interaction.
3. **A new version DOI is minted, but you want to preserve `20015923` as
   the canonical M1 grandfather artefact.** No action required; the M1
   axis grandfathering is per-concept-DOI (`19996689`), not per-version-DOI.
   Future references should cite the new version DOI; old references to
   `20015923` remain valid but pre-S154-compliant.

---

## §6 — Post-Edit follow-up actions

After operator confirms the Edit landed:

1. SQL close: `UPDATE todos SET status='done' WHERE id='opportunistic-option-c-d2-note-edit';`
2. If new version DOI minted: update `M1_M12_CLOSURE_OUTLOOK_CURRENT.md` via
   `python scripts/outlook_emit.py --out ...` to pick up the new version.
3. If the concept DOI's "latest version" pointer changes: no action; the
   outlook generator queries by version-ID, which is stable.
4. Optional bridge follow-up slot `T2-EXECUTOR-M1-D2-NOTE-S154-ADDENDUM-LANDED`
   if operator wants a tracked audit-trail entry. Otherwise close-in-place
   via SQL update only.

---

**End Zenodo Edit payload.**
