# SHA origin trace — `aab7ee2` (governance forward-point discharge)

**Date**: 2026-05-08 ~08:35 JST
**Trigger**: synth's governance forward-point on SHA correction (per `synth_signature_capture.md`).
**Question**: was `aab7ee2` a typo at template draft time, or a phantom from a prior session that got copy-pasted forward (a Searcher's Fatigue tell)?
**Verdict**: **TYPO at LANE-1 packet drafting time** (2026-05-07 21:28 JST). NOT Searcher's Fatigue.

---

## Forensic walk

### Step 1 — verify wrong SHA does not exist in bridge

```
$ git rev-parse aab7ee2
fatal: ambiguous argument 'aab7ee2': unknown revision or path not in the working tree.
```

`aab7ee2` is not present in any bridge ref.

### Step 2 — check for any SHA prefix `aab*` in full bridge history

```
$ git log --all --pretty=format:"%H %s" | grep -E "^aab"
(zero matches)
```

**No commits in any bridge ref start with `aab`.** This rules out:
- The "right session, wrong copy" hypothesis (where `aab7ee2` would be a SHA from a sibling deposit on the same date).
- The "phantom from prior session" hypothesis (where `aab7ee2` would match some earlier bridge artifact's commit hash, suggesting a copy-paste from a stale notes / scratch file).

### Step 3 — locate earliest filesystem occurrence

```
File                                          Created
----                                          -------
lane1_batch_packet_w21.md                     2026-05-07 21:28:05 JST
m_critical_path_2026-05-07.md                 2026-05-07 21:51:13 JST
m4_v0_ratification_template.md                2026-05-08 07:46:10 JST
prompt/104_peer_consult_m4_fast_track_EXECUTED.txt   2026-05-08 07:52:00 JST
```

Earliest occurrence: `lane1_batch_packet_w21.md` at 2026-05-07 21:28:05 JST.

### Step 4 — verify timing relative to actual 074 deposit

```
$ git show --stat 9596c21
commit 9596c21af645b1b70ad5ce98cccbd8171ac11d6a
Author: papanokechi <shkubo@outlook.jp>
Date:   Thu May 7 14:25:01 2026 +0900

    T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074 -- DOSSIER_COMPLETE; ...
```

Actual 074 deposit landed at `9596c21` on 2026-05-07 14:25:01 JST.
LANE-1 packet was drafted ~7 h later (2026-05-07 21:28:05 JST).

The LANE-1 packet drafter knew the 074 deposit had landed and the SHA
was available; the drafter mis-transcribed it.

### Step 5 — propagation pattern

```
T+0 (2026-05-07 21:28 JST):  lane1_batch_packet_w21.md drafted with wrong SHA aab7ee2
T+23min:                      m_critical_path_2026-05-07.md inherits wrong SHA (next file in same drafting session)
T+10h18min (2026-05-08 07:46 JST):  m4_v0_ratification_template.md inherits wrong SHA (next morning)
T+10h24min (2026-05-08 07:52 JST):  104 peer-consult prompt inherits wrong SHA from template
T+10h28min:                   104 fired; 2 of 5 peer-AI consultants rubber-stamped Y on wrong SHA
T+11h00min:                   105 substrate-excerpts work caught the SHA-mismatch via independent git rev-parse
T+12h05min (2026-05-08 ~08:30 JST):  synth Option A → substrate verification → §3 ACCEPT_W_REVISIONS signed
T+12h10min:                   106 cascade execution + this trace deposit
```

Standard copy-paste propagation pattern (each derivative artifact
inheriting the SHA from the immediately upstream artifact). No prior
bridge session involved as source.

---

## Verdict

**TYPO**, not phantom. Specifically:

- **What it was**: copy-paste error at `lane1_batch_packet_w21.md` draft time. The drafter intended to cite `9596c21` but transcribed `aab7ee2` (off by all 7 characters; not even a near-miss like a digit transposition or visually similar character substitution). The wrong SHA may have been the residue of a deleted-then-replaced placeholder during the drafting session, or a hand-typed approximation rather than a paste from `git log` output.

- **What it was NOT**: a Searcher's Fatigue tell. Searcher's Fatigue would have manifested as a SHA from a prior bridge session (e.g., a SHA from an earlier verdict the drafter was holding in working memory) getting inadvertently re-cited when the drafter intended to cite the new SHA. Zero `aab*` prefix in full bridge history rules this out.

- **Why it propagated**: each downstream artifact (`m_critical_path_2026-05-07.md`, `m4_v0_ratification_template.md`, `104` prompt) inherited the wrong SHA from the immediately upstream artifact via copy-paste, without independent `git rev-parse` verification at any propagation step.

- **Why it was caught**: synth-tier ratification refusal triggered the agent to do substrate verification (105 Option A); the agent's independent `git rev-parse` of the cited SHA returned `fatal: ambiguous argument`, surfacing the typo. 105 deposit then traced + corrected.

---

## Mitigation in place

Per repo memory `substrate verification` (stored 2026-05-08): pre-flight `git rev-parse` of every cited bridge SHA is now mandatory before any relay prompt or ratification template is dispatched. Specifically:

1. Every bridge SHA cited in any §1 substrate inventory must pass `git rev-parse <SHA>` returning a full 40-char hash before the artifact is sealed.
2. Pre-fire checklist for relay-prompt drafting must include a SHA-verification step alongside the existing forbidden-verb scan and quote-length scan.
3. Synth-tier ratification refusal pattern (Option A path) is validated as a non-trivial audit checkpoint and should be encoded as a synth-tier governance affordance for any future ratification template.

---

## AEAL ledger entry (queued for umbrella v2.1)

Per synth's governance forward-point:

```json
{
  "type": "claim_correction",
  "subject": "074 ratification dossier SHA citation",
  "wrong_value": "aab7ee2",
  "correct_value": "9596c21",
  "scope": "lane1_batch_packet_w21.md, m_critical_path_2026-05-07.md, m4_v0_ratification_template.md, 104_peer_consult_m4_fast_track_EXECUTED.txt",
  "origin": "TYPO at lane1_batch_packet_w21.md draft time 2026-05-07 21:28 JST",
  "discovery": "synth-tier ratification refusal 2026-05-08 ~08:00 JST + agent independent git rev-parse 2026-05-08 ~08:10 JST",
  "correction_applied": "2026-05-08 ~08:30 JST in 105 substrate-prep + 106 cascade",
  "audit_evidence_preserved": "104 prompt left as-is per audit-trail-immutability; 105 + 106 deposits document the contamination cascade and correction"
}
```

This entry is queued for inclusion in the umbrella v2.1 AEAL ledger (per SQL todo `umbrella-v21-m4-closure-amendments`).

---

## Lessons logged

1. **`git rev-parse` pre-flight is now mandatory** for any bridge SHA cited in any sealed artifact. Stored as repo memory `substrate verification`.

2. **Multi-AI ensemble does NOT substitute for substrate access**: 5 peer-consult-104 consultants had access to the same wrong SHA in prompt §2; 2 reported Y rubber-stamped, 3 reported N defaulted. None caught the SHA mismatch. Only the synth working off the ratification template (with the offer to provide substrate excerpts on request) caught it.

3. **Synth-tier ratification refusal is a non-trivial audit checkpoint** (105 Observation A2; 106 reaffirmed). Substrate-grounded signature (Option A) is the AEAL-honest path; trust-relay via dossier completeness (Option B) is acceptable governance but loses the SHA-validity-as-side-effect failure-detection.

4. **Copy-paste propagation through derivative artifacts is a real contamination vector**: 4 derivative artifacts inherited the wrong SHA across ~14 hours, with no `git rev-parse` verification at any propagation step. The mitigation (pre-flight SHA verification on every sealed artifact) addresses this directly.
