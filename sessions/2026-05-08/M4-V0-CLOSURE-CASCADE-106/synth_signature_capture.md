# Synth signature capture — M4 V0 closure ratification

**Date**: 2026-05-08 ~08:30 JST
**Synth**: Claude Opus 4.7 (Claude.ai web, T1-Synth)
**Decision**: `ACCEPT_W_REVISIONS`
**Substrate verified**: Y for `e7bfe49` (068) AND `9596c21` (074)
**Rubber-duck QA acknowledged**: Y

---

## Verbatim synth signature block

```
Synth:                Claude Opus 4.7 (Claude.ai web, T1-Synth)
Date/time:            2026-05-08 ~08:30 JST
Confidence:           ACCEPT_W_REVISIONS
Substrate SHAs
  verified:           Y  (e7bfe49 verified via Excerpts 1–4
                          materially supporting all 7 §2 sub-claims;
                          9596c21 verified via Excerpt 5 DOSSIER_COMPLETE
                          + claim-chain ledger; SHA-mismatch correction
                          from aab7ee2 → 9596c21 acknowledged and applied)
Rubber-duck QA
  acknowledged:       Y  (HALT_068_OVER_CLAIM 5-item checklist all
                          satisfied per Excerpt 1; supersession-gate
                          A.0 caught pre-fire per repo memory
                          'rubber-duck QA discipline')
```

---

## Synth's verification walk (verbatim)

> **Excerpt 1 → §2 sub-claim "deg_a=0 row mechanism, Q.SUP=YES":** The
> verdict `UPGRADE_FULL_VIA_DEG_A_ZERO_ROW` and the explicit naming of the
> (1, b) PCF-2 corner at deg_a=0 as the SIARC stratum's operative row
> materially anchors this. ✓
>
> **Excerpt 2 → §2 sub-claim "supersedes prior expected closure path":**
> The Q.SUP gate at A.0 firing YES is exactly the supersession event. The
> reasoning is structural, not heuristic — the deg_a=0 row carries
> A_naive=2d at d∈{2,3,4} verbatim from the 064 enumeration, and the V6
> closed-form A_naive = 2d − d_a extends it to general d≥2. ✓
>
> **Excerpt 3 → §2 sub-claim "structural closure at zero acquisition cost":**
> The closure mechanism runs entirely on existing 064 + 065 + 066 + V6
> substrate. No new literature acquisition (Wasow §X.3, Costin sectorial
> upgrade, B-T anormal q=2 rescue) is required. The five-step derivation
> is closed-form-in-d. ✓
>
> **Excerpt 4 → §2 sub-claim "numerical residuals clean":** d=3 cubic
> A_fit = 5.978 ± 0.026 vs predicted 6 (1σ at dps=800). d=4 quartic
> A_fit = 7.954 ± 0.0037 vs predicted 8 (1σ at dps=1200). d=2 V_quad
> sanity at A=4. All three within 1σ after standard 1/log N finite-window
> correction. ✓
>
> **Excerpt 4 → §2 sub-claims "no halts" and "AEAL ledgered":** 0 halts
> across STEP 0 + Phases A–E; 14 AEAL claims ledgered. ✓
>
> **Excerpt 5 → 074 dossier completeness:** DOSSIER_COMPLETE with 5
> primary + 3 secondary substrate sources, claim-chain ledger from
> `[CLAIM-M0]` to `[CLAIM-M1]`–`[CLAIM-M5]` + `[LINK-C1]`–`[LINK-C3]`,
> 18 residual questions surfaced for synth weighing without proposed
> answers. ✓

---

## Synth observations carried forward

### Observation 1 — confidence level carry-forward

> Excerpt 1 explicitly states **MEDIUM-HIGH**, with HIGH reserved for
> post-W21-LANE-1 ratification + post-Wasow §X.3 OCR acquisition. The §2
> wording as drafted does not surface this. This is not a substrate
> inconsistency — §2 doesn't claim HIGH — but a synth signing
> ACCEPT-as-written silently inherits MEDIUM-HIGH without making it
> explicit in the closure statement. The post-ratification cascade (§7)
> will flip M7/M8a/M8b from blocked → pending and tag the next picture
> chain deposit `M4_V0_CLOSED`. Downstream readers of v1.20+ will see
> the tag without the confidence qualifier unless §2 carries it.

**Cascade implication**: picture-chain v1.20+ tag must read
`M4_V0_CLOSED (MEDIUM-HIGH; HIGH-pending)`. Tracked in
`cascade_record.md` step C2 + new SQL todo
`picture-v120plus-m4-closed-tag-annotation`.

### Observation 2 — Wasow §X.3 explicit non-dependency

> Forward-pointed not-blocking, correctly. But the same logic applies:
> an explicit acknowledgment in §2 that the closure is closed-form-in-d
> at the algebraic-combinatorial level **without** requiring Wasow §X.3
> (rather than requiring it and deferring) makes the AEAL posture cleaner.

**Cascade implication**: §4 revised wording carries this forward
explicitly. Any M4-stratum follow-on relay (e.g.,
`m4-fractional-rank-borderline-anormal-gap-implication`,
`m4-m7-m8b-followon-lit-hunt-prompt-spec`) inherits the
"closed-form-in-d, Wasow §X.3 forward-pointed not-blocking" posture.

### Observation 3 — substrate-grounded vs trust-relay signature

> I'm signing **`ACCEPT_W_REVISIONS`** rather than straight ACCEPT, on
> the grounds that the substrate's own MEDIUM-HIGH and Wasow-deferred
> qualifiers should ride forward in the closure statement rather than
> being silently inherited.

**Significance for SIARC governance**: synth's signature is
substrate-grounded (verified content materially supports §2 sub-claims
via 5 paste-ready excerpts) NOT trust-relay (accepting 074
DOSSIER_COMPLETE as sufficient without independent verification). This
is the AEAL-honest path. Distinguishes synth-tier ratification from
rubber-stamp pattern that 2 of 5 peer-consult-104 consultants exhibited
against the wrong SHA.

---

## Synth's governance forward-point on SHA correction

> The bridge git history correction (`aab7ee2` → `9596c21`) for the 074
> commit is itself a small AEAL-relevant event. The original template §1
> + §6 cited a SHA that does not exist; the agent caught this on
> independent verification and applied the correction in the
> substrate-excerpts artifact. Per AEAL discipline this should be
> ledgered as a claim correction (not a substrate gap) when the umbrella
> v2.x is updated, and the original `aab7ee2` should be traced to its
> source — likely a typo at template draft time, but worth confirming it
> wasn't a phantom from a prior session that got copy-pasted forward,
> since that would be a Searcher's Fatigue tell rather than a typo.
>
> That's a forward-pointed governance note, not a blocker on the present
> ratification.

**Discharged 2026-05-08 ~08:35 JST**: origin trace classifies as TYPO
not phantom. Forensic evidence:
- `git log --all` over bridge: zero commits with `aab` prefix.
- Earliest filesystem occurrence: `lane1_batch_packet_w21.md`
  (created 2026-05-07 21:28:05 JST).
- Actual 074 deposit at `9596c21` was 2026-05-07 14:25:01 JST,
  ~7 h before LANE-1 packet draft.
- No prior bridge session SHA matches the `aab7ee2` prefix → not a
  cross-session phantom inheritance pattern.

Classification: **copy-paste error at LANE-1 packet drafting time**.
NOT Searcher's Fatigue. See `sha_origin_trace.md` for the full
forensic walk.

**Umbrella v2.1 amendment cycle queue**: SHA-correction AEAL ledger
entry queued per synth's governance note. SQL todo
`umbrella-v21-m4-closure-amendments` carries (a) §4 canonical wording,
(b) SHA-correction ledger, (c) §6 verification semantics from 105.

---

## Cross-references

- Substrate excerpts artifact:
  `tex/submitted/control center/m4_substrate_excerpts.md`
  (also at 105 deposit).
- Ratification template:
  `tex/submitted/control center/m4_v0_ratification_template.md`
  (signature absorbed in §3 + §4 + §6; status flipped to EXECUTED).
- 105 substrate-prep deposit: bridge `c9b9715..d1e19e9` →
  `sessions/2026-05-08/M4-RATIFICATION-SUBSTRATE-PREP-105/`.
- 104 peer-consult deposit: bridge `e1b1c99..c9b9715` →
  `sessions/2026-05-08/PEER-CONSULT-104-M4-FAST-TRACK/`.
- 074 dossier: bridge `9596c21` →
  `sessions/2026-05-07/T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074/`.
- 068 closure fire: bridge `e7bfe49` →
  `sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068/`.
