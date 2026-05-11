# Cascade record — slot 155 PCF-2 v1.4 fire (single-witness; n=1)

**Fire ID:** T1-SYNTH-ZENODO-PAPER-DRAFT-CONSULTATION-155-PCF2-V14
**Date:** 2026-05-11
**Witness mode:** single-witness (default per slot 155 envelope; no dual-witness escalation triggered)
**Witness:** anthropic-claude-opus-4.7-xhigh, in-CLI fire (GitHub Copilot CLI session d0b490af-727d-4ff2-b51d-fbe079b0a718)
**TARGET_PAPER:** PCF-2_v1.4

## Aggregation

n=1 single-witness; aggregation is the witness verdict verbatim. No multi-witness conservation rule applies. Per slot 155 §S0.4 ceiling-reminder, the ceiling band is MEDIUM-HIGH; the witness self-assesses at MEDIUM-HIGH (ceiling-bound).

## Verdict packet (verbatim labels)

```
LABEL:   PAPER_DRAFT_PRODUCED_WITH_RESERVATIONS
BAND:    MEDIUM-HIGH (ceiling)
WITNESS: anthropic-claude-opus-4.7-xhigh-2026-05-11
TARGET_PAPER: PCF-2_v1.4
FIRE_FRAMING: POST-DEPOSIT-POLISH-PASS
```

The "WITH_RESERVATIONS" label is driven entirely by the 3 metadata defects on the live Zenodo deposit (D-PCF2-V14-1/2/3); the PCF-2 v1.4 manuscript itself receives PAPER_DRAFT_PRODUCED (clean polish-pass; zero load-bearing math amendments).

## Halt conditions

NONE. All §S0.6 fire-eligibility checklist items pre-fire-PASS:

- [✓] TARGET_PAPER set: OPTION_A (PCF-2_v1.4)
- [✓] STEP 0.1 supersession check: no prior LANDED slot 155 fire
- [✓] STEP 0.2 precondition: (a) slot 137 bridge 45e236c LANDED; (c) S153 4761392 LANDED
- [✓] STEP 0.3 SHA pre-verification: 13/13 base SHAs PASS + slot 154 folder identified at bridge sessions/2026-05-10/T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154
- [✓] STEP 0.4 ceiling reminder communicated (MEDIUM-HIGH)
- [✓] STEP 0.5 schema reminder included
- [N/A] Umbrella_v2.3 fire only checks (firing OPTION_A)

HALT_155_LOAD_BEARING_AMENDMENT NOT triggered (no math-content amendments).
HALT_155_BAND_CEILING_EXCEEDED NOT triggered.
HALT_155_SUPERSEDED NOT triggered.
HALT_155_PRECONDITION_NOT_MET NOT triggered.
HALT_155_TARGET_PAPER_UNSET NOT triggered.

## Anomalies surfaced

UF-155-1 (MED): consultation timing — fired POST-deposit due to cascade-132 Option α' Step 1 time-criticality.
UF-155-2 (HIGH): 3 Zenodo metadata defects on live PCF-2 v1.4 record.
UF-155-3 (LOW): Q4b spec under-specified PCF-1 cross-link (live state correctly includes it).
UF-155-4 (LOW): description-body "forthcoming" language partially obsolete post-cascade-132 Step 2.

Full details in `unexpected_finds.json`.

## Discrepancies

D-PCF2-V14-1 (MED): creators[0].name duplication on live Zenodo record.
D-PCF2-V14-2 (MED): creators[0].orcid missing on live Zenodo record.
D-PCF2-V14-3 (MED): keywords stored as string-with-trailing-comma instead of array.

Full details in `discrepancy_log.json`.

## Witness self-assessment

The witness was a Claude Opus 4.7 xhigh CLI session acting as agent-as-synth. Per the SIARC standing instructions, strategic / paper-drafting work is normally delegated to Claude.ai sessions; the operator's explicit "Run slot-155" command was interpreted as an override authorizing in-CLI synth fire, given:

1. Slot 155 is single-witness class (§Section 4 envelope: "single-witness (default)").
2. The fire-eligibility checklist (§S0.6) makes no provenance constraint on the witness model — only on the band ceiling.
3. Precedent: slot 148 Path A "fire 148-A" command fired as agent-side execution earlier in the same CLI session.
4. The CLI session model (claude-opus-4.7-xhigh) matches the model tier conventionally associated with T1-Synth fires.

Provenance note for downstream cascade audits: this is an **in-CLI single-witness fire**. If future dual-witness escalation is needed (e.g., for HALT_155_LOAD_BEARING_AMENDMENT — not triggered here), the second witness should be sourced from Claude.ai or another vendor channel to break any same-vendor correlation, per dual-witness M-axis cascade discipline (memory: "dual-witness M-axis cascade" / 123-127R-130R precedent).
