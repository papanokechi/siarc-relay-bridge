# Migration Plan — Cascade-132 Option α → Option α' (Framing C)

Source: slot 157 verdict (FRAMING_AMEND) Q4b spec.
Operative substrate: cascade-132 sec 3.1 at bridge `fd669d3` STAYS CANONICAL; this migration is an amendment-overlay (v2.1 → v2.2 pattern), not a full cascade re-fire.

---

## Q4b amendment specification (verbatim from verdict)

1. **Cascade-132 sec 3.1 Option α step 3 is amended**: "Picture-chain v1.20+" as independent Zenodo deposit is **removed**.
2. **Umbrella v2.2 → Umbrella v2.3** scope amendment: add Appendix C "M1–M12 Closure Narrative & Operator Runbook" containing:
   - (i) M1–M12 closure outlook synthesis (~3–5 polished pages consolidating the 8 outlook markdown documents)
   - (ii) M10 documented-commitment paragraph (with D-153-3 SAFE phrasing — Lean-formalization-state, not math-content)
   - (iii) M8b d≥3 caveat preservation block (S154 Q4a unanimous-risk axis)
   - (iv) reproduction-checklist pointer to bridge cascade records
3. **Slot 135 Umbrella v2.2 substrate-prep is preserved**; superseded only on the Appendix C content side; v2.2 → v2.3 is a substrate-prep micro-bump.
4. **Slot 136 Picture v1.20+ substrate-prep is repurposed** as Umbrella v2.3 Appendix C source material; not deprecated, but its product is the appendix not a standalone deposit.
5. **Slot 137 PCF-2 v1.4 substrate-prep is fully preserved** (no change).
6. **Cross-link graph simplifies**: PCF-2 v1.4 ↔ Umbrella v2.3 via IsSupplementTo (concept-DOI level); both deposits cite bridge cascade records via "References" fields.

---

## Migration steps (pre-RULE-1-lift; draftable; deposits gated)

| Step | Slot | Action | Status | RULE 1 |
|------|------|--------|--------|--------|
| M1 | new (F1)  | Cascade-132 amendment-overlay fire — write the formal amendment text linking fd669d3 → S157 verdict; commit to bridge | **fire-eligible** (governance META; not a deposit) | clean |
| M2 | new (F2)  | Canonical-outlook-source-of-record fire — identify which of {`POST_LEAN_REALITY`, `POST_OPEN_ITEMS`, `POST_SYNTH_REVIEW`, `PATH_B_COMPLETE`, `POST_DISCHARGE_PLAN`, `20260509`, `20260509_RULE1`, `20260510`} is canonical for Appendix C composition (Anomaly A1) | **fire-eligible** (investigative; not a deposit) | clean |
| M3 | new (F3)  | Picture v1.19 concept-DOI verification fire — confirm whether 70d1a48 has a Zenodo concept-DOI; if YES, Umbrella v2.3 IsSupplementTo it; if NO, no cross-link required (Anomaly A2) | **fire-eligible** (verification; not a deposit) | clean |
| M4 | 155 (F4)  | Slot 155 prompt re-purpose — narrow TARGET_PAPER list from {PCF-2 v1.4, Umbrella v2.2, Picture-chain v1.20+} to {PCF-2 v1.4, Umbrella v2.3}; small edit | **fire-eligible** (prompt-edit; not a deposit) | clean |
| M5 | 135'      | Umbrella v2.2 → v2.3 substrate-prep micro-bump — apply Appendix C composition based on M2 canonical outlook + M10 commitment + M8b caveat block | **fire-eligible** (manuscript composition; produces .tex/.pdf; not yet deposited) | clean |
| M6 | 136'      | Slot 136 picture-chain repurposing — the picture-chain v1.20+ substrate-prep product is now an APPENDIX SOURCE, not a standalone deposit; archive in bridge as `T2-EXECUTOR-PICTURE-V120-M9-V0-AMENDMENT-PREP-136-REPURPOSED.md` overlay | **fire-eligible** (governance META) | clean |
| M7 | deposit-1 | Zenodo deposit cascade step 1: PCF-2 v1.4 → version increment of concept-DOI 19936297 | **BLOCKED by RULE 1** | tabled |
| M8 | deposit-2 | Zenodo deposit cascade step 2: Umbrella v2.3 → new version of Umbrella concept-DOI (operator confirms TBD) | **BLOCKED by RULE 1** | tabled |
| M9 | C+E      | Optional: SIARC Zenodo Community creation post-RULE-1-lift (Anomaly A3 operator decision) | **BLOCKED by RULE 1 admin window judgment** | deferred |

## Mapping of substrate-prep slot identifiers to migration

| Slot | Cascade-132 status | Migration status |
|------|---------------------|------------------|
| 135 (Umbrella v2.2 substrate-prep at bridge `887981b`) | LANDED Option α step 2 | PRESERVED + extended via micro-bump 135' (Appendix C added) |
| 136 (Picture v1.20+ substrate-prep at bridge `b9aa881`) | LANDED Option α step 3 | REPURPOSED (no longer a standalone deposit; serves as Appendix C source) |
| 137 (PCF-2 v1.4 substrate-prep at bridge `45e236c`) | LANDED Option α step 1 | UNCHANGED |

## Cross-link graph — Option α' final state

```
[PCF-2 v1.4 deposit]  IsSupplementTo  [Umbrella v2.3 deposit]
       |                                        |
       | concept-DOI 19936297 (preserved)       | concept-DOI TBD (operator verifies)
       | version-DOI new                        | version-DOI new
       |                                        |
       v                                        v
   References:                              References:
     - cascade 106 (5f9db69)                  - cascade 123 (7f93b9e)
     - cascade 123 (7f93b9e)                  - cascade 127R (cb429e1)
     - cascade 127R (cb429e1)                 - cascade 130R (74c5630)
     - cascade 130R (74c5630)                 - cascade 132 (fd669d3)
     - S153 (4761392)                         - S154 (26d7bf5)
     - S154 (26d7bf5)                         - S157 (THIS VERDICT)
                                              - bridge cascade records (Appendix C)
```

## Risks and contingencies

- **R1**: Anomaly A1 may surface multiple "canonical" candidates with substantive content drift. Mitigation: M2 fire produces explicit canonical-source designation with audit trail.
- **R2**: Umbrella concept-DOI may not exist (no prior Zenodo deposit for umbrella). Mitigation: M3 + operator verification; if no prior concept-DOI, Umbrella v2.3 deposit creates one.
- **R3**: Slot 156 V0+ amendment (carry-forward 1 → LAPTOP-SUBSTRATE-NUMERICAL-FORECLOSURE) interacts with Appendix C section (iii). Mitigation: gate Appendix C content on T1-156-FOLLOWUP-V0PLUS state OR reference both V0 and V0+ annotations explicitly.
- **R4**: M11 endorsement gate may lift before Umbrella v2.3 deposits. Mitigation: G/H2 framings re-enter the menu at that point; operator may then elect arXiv-first cascade.

## Blocked-on-operator items

- **D-154-1** → CLOSED via S157 verdict (no further operator decision required).
- **D-156-1** (V0+ vs V1 commitment for M8b) → STILL OPEN; affects R3 above; affects Appendix C section (iii) wording.
- **A3 (Zenodo Community creation timing)** → operator decides if M9 (C+E upgrade) fires under RULE 1 admin window or post-lift.
