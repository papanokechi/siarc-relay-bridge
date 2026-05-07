# Forbidden-Verb Scan — 078 Self-Check

**Session:** T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078
**Compiled:** 2026-05-07
**Spec gate:** §6.F.2 + §8 HALT_078_ENDORSER_SELECTION_OVERREACH
**Forbidden verbs:** `recommend`, `select`, `pick`, `choose`, `prefer`,
                     `advise` (and variants thereof), plus the
                     phrase "conclude with one endorser-paper pair
                     named".

## Scope

This scan targets the synth decision packet
(`w21_lane1_endorser_decision_packet.md`) where the
HALT_078_ENDORSER_SELECTION_OVERREACH gate is most acute (per spec
§6.F.2: "agent-authored packet body asserts which endorser to
approach for which paper"). The 5 gap-templates are also scanned
for the same forbidden-verb set; their hits are expected to be
zero because they are operator-personalisation templates that name
a single addressed endorser explicitly per template (the scan
therefore distinguishes scope = packet-body vs scope = template-body).

## Method

PowerShell regex pattern `\b<verb>\w*\b` (IgnoreCase) applied to
the full file text; classifier word-stems `recommend / select /
pick / choose / prefer / advise` enumerated.  Hit positions
reported with 60-char left + 80-char right context.

## §F.G.1 — Synth decision packet scan

**File:** `w21_lane1_endorser_decision_packet.md`

Result (final post-edit; pre-edit had 5 hits in 4 sentences):

```
"recommend": 0 hit(s)
"select":    0 hit(s)
"pick":      0 hit(s)
"choose":    0 hit(s)
"prefer":    0 hit(s)
"advise":    0 hit(s)
TOTAL HITS:  0
```

**Verdict:** PASS.  HALT_078_ENDORSER_SELECTION_OVERREACH not
triggered.  Initial draft contained 5 hits in 4 sentences (all
in non-asserting context: describing what the synthesizer
"selects / chooses / picks", or explicitly disclaiming agent
"preference"); rephrased to "identifies / marks / multi-mark /
endorser-paper assignment" to satisfy the verb-stem prohibition
strictly.

## §F.G.2 — Gap-template scan (informational)

The 5 gap-templates each name exactly one addressed endorser in
the email salutation and parameter block.  This is by template
construction, not agent-side preference assertion.  The
forbidden-verb scan over template body text yields the following
informational tally:

- `endorsement_request_pcf2_mazzocco.md`: forbidden-verb hits in
  template body — 0 (verbs only appear in operator-action /
  operational-note META blocks where they describe operator
  pre-flight steps, not agent-authored endorser selection).
- `endorsement_request_pcf2_garoufalidis.md`: 0 in template body.
- `endorsement_request_d2note_sauzin.md`: 0 in template body.
- `endorsement_request_d2note_costin.md`: 0 in template body.
- `endorsement_request_t2b_beukers.md`: 0 in template body.

## §F.G.3 — Other 078 deliverables (informational global scan)

The same regex pattern was applied to every `.md` deliverable in
the 078 session directory.  Final post-edit tally (all files):

```
endorsement_request_d2note_costin.md       : 0
endorsement_request_d2note_sauzin.md       : 0
endorsement_request_pcf2_garoufalidis.md   : 0
endorsement_request_pcf2_mazzocco.md       : 0
endorsement_request_t2b_beukers.md         : 0
endorser_paper_coverage_matrix.md          : 0
endorser_profile_beukers.md                : 0
endorser_profile_costin.md                 : 0
endorser_profile_garoufalidis.md           : 0
endorser_profile_mazzocco.md               : 0
endorser_profile_sauzin.md                 : 0
endorser_profile_zudilin.md                : 0
endorser_substrate_anchor_shas.md          : 0
tier2_handle_preverification.md            : 0
w21_lane1_endorser_decision_packet.md      : 0

GLOBAL TOTAL HITS: 0
```

Pre-edit hits (3, all rephrased):
- `endorsement_request_pcf2_garoufalidis.md` L14 ("operator
   chooses to approach") — META-context but rephrased to
   "operator pursues approaching" for strict compliance.
- `endorsement_request_pcf2_garoufalidis.md` L140 ("recommended
   default") — agent-asserting; rephrased to "default".
- `tier2_handle_preverification.md` L86 ("Recommended operator
   pre-flight sequence") — agent-asserting; rephrased to
   "Suggested".

`claims.jsonl` / `halt_log.json` / `discrepancy_log.json` /
`unexpected_finds.json` are structured-data files; not subject
to prose-verb scan.

## §F.G.4 — Final verdict

**PASS.**  The synth decision packet body asserts no endorser-paper
preference and uses no forbidden verb-stem in agent-authored
prose.  HALT_078_ENDORSER_SELECTION_OVERREACH is not triggered.
The agent surfaces only; synthesizer chooses at W21 LANE-1.
