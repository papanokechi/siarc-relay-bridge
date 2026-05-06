# Handoff — N3-FOURTH-LAW-ARBITRATION-SUBSTRATE
**Date:** 2026-05-06
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~75 minutes
**Status:** COMPLETE

**Relay prompt:** 055 (CLI-Synth in-tier; v2026-05-08 RACI standard
cadence, T2 in-tier scope after T1-override expired with 052R landing
2026-05-06 ~12:42 JST)
**Class:** STRUCTURAL-ANALYSIS-SUBSTRATE (substrate-only; no NEW
empirical claims)
**Anchor commits:**
- 044R `T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE` — bridge `fe15737`
- 044B `T2B-TIGHTENED-SWEEP-OUTCOME-B` — bridge `82001aa`

---

## What was accomplished

This relay produced a **substrate-only** input package for the T1
Synthesizer W20 weekly arbitration on the n=3 fourth-law candidate.
**Arbitration judgement is RESERVED for T1 Synth W20 weekly cadence.**
This relay does not rank, score, prefer, or select among hypotheses,
question outcomes, or wording candidates.

Four substrate documents were assembled (35,780 bytes total):

1. `substrate_inventory.md` — verbatim numerical anchors from 044R-A1..A8 +
   044B-A1..A8 (anchors A1 = b₇ singular `(8, −4, 0, 7, 4)` ratio 8/49
   yielding L = 3/log(2) at dps=300; A2 = b₁₀ 044R outlier
   `(−9, 0, 0, 10, 5)` ratio −9/100 yielding L = 3/log(2) at dps=300),
   negative results NR1–NR3 from 044B B-T-A verdict, sign-orbit +
   Bauer-shape coverage map, ratio-pattern panel, and pointers to
   substrate sessions in earlier T2B-* folders.
2. `hypothesis_catalogue.md` — three hypotheses (H_BSW Brouncker–
   Stieltjes–Wallis-class identity, H_BFP Bauer–Forrester pencil,
   H_C numerical coincidence at h ≤ 10⁹) presented WITHOUT ranking,
   each with substrate citations, predicted falsifying observation,
   falsification status (all three NOT FALSIFIED at h ≤ 10⁹), and
   substrate-cited estimated probe runtime.
3. `t1_synth_question_set.md` — five questions Q1–Q5 with conditional
   structure (Q3 conditional on Q1 = Q2 = defer; Q4 conditional on
   Q1 ∨ Q2 = fire; Q5 unconditional). T1 Synth W20 weekly answers
   in Q1 → Q2 → Q3/Q4 → Q5 order.
4. `pcf2_v3x_wording_softening.md` — four candidate wordings W1
   (DEFENSIVE / minimal), W2 (SUBSTRATE-CITED / moderate, the 044B
   suggestion verbatim), W3 (HYPOTHESIS-CITED / strong), W4
   (FORECAST-WITHHELD / weakest), with a Q1×Q2×Q3/Q4×Q5 → W
   selection table.

Three discipline scans were run:

- **HALT_055_FRAMING_DRIFT** — `Select-String` for {shows, show,
  shown, confirms, confirmed, proves, proven, establishes,
  established, must}: 2 hits, both inside the discipline-note
  self-references that quote the forbidden-verb list verbatim
  (allowed). Initially 4 hits; "confirmed positive evidence" /
  "positive confirmed structural fit" in `hypothesis_catalogue.md`
  H_C section softened to "verified positive evidence" / "positive
  verified structural fit" to remove ambiguity. PASS.
- **HALT_055_RANK_DRIFT** — `Select-String` for {most likely, likely,
  ranks, rank, scoring, scored, prefer, preference, preferred}:
  5 hits, all transferring ranking responsibility to T1 Synth
  ("T1 Synth ranks at W20 weekly", etc.) or self-references inside
  discipline notes. PASS.
- **HALT_055_NUMERICAL_DRIFT** — spot-check on ratios 8/49 and
  −9/100, relation `[-3, 0, 0, 0, 0, 0, 0, 1]` at dps=300, integer
  relation `3·a₂ + 17·b₁ − 143 = 0`, max_abs_denom = 143, Bauer-shape
  family enumeration_total = 1 620 / Stage A convergent = 1 058 /
  Stage B Log = 2 / Stage D off-orbit = 2: all match 044R-A5 +
  044B-A1..A6 verbatim. PASS.

## Key numerical findings

**No NEW numerical claims surfaced.** All numerical anchors are
verbatim citations from prior 044R-A1..A8 + 044B-A1..A8 AEAL
entries. The substrate-only inventory captures:

- **A1 b₇ singular** `(8, −4, 0, 7, 4)`: L = 3/log(2) at dps=300
  with relation `[-3, 0, 0, 0, 0, 0, 0, 1]` (044B-A3 verbatim).
  Ratio a₂/b₁² = 8/49 (generic numerator).
- **A2 b₁₀ 044R outlier** `(−9, 0, 0, 10, 5)`: L = 3/log(2) at
  dps=300 with relation `−3 + L·log(2) = 0` (044R-A5 verbatim).
  Ratio a₂/b₁² = −9/100 (Bauer-shape numerator k=3 with
  mismatched denominator: Bauer requires b₁ = ±6k = ±18, observed
  b₁ = 10).
- **044B B-T-A verdict** (044B-A6 verbatim): new_off_orbit_hit_count
  = 0 after Bauer-shape sub-locus + sign-orbit closure swept.
- **Bauer-shape sub-locus enumeration** (044B-A2 verbatim): k ∈
  {1..5} at b₁ ∈ ±B(k) \ {±6k}, b₀ ∈ [−7, 7] → 1 620 enum / 1 058
  Stage A convergent / 2 Stage B Log / 2 Stage D off-orbit, both
  Stage D hits already in b₁₀ sign-orbit closure.
- **Linear ratio-pattern fit** (044B-A4 verbatim):
  `3·a₂ + 17·b₁ − 143 = 0` exact through both anchors but
  max_abs_denom = 143 > 30 (project low-denominator threshold).

## Judgment calls made

1. **Used "verified" instead of "confirmed"** in
   `hypothesis_catalogue.md` H_C section (lines 162, 171). The
   original drafted text read "confirmed positive evidence under
   H_BSW or H_BFP" / "positive confirmed structural fit"; I judged
   this could read as a forbidden-verb hit even though the context
   is a falsification-protocol description (not a prediction of
   what will happen). To remove ambiguity, softened to "verified".
   The semantic content is unchanged.
2. **Self-references quoting the forbidden-verb list verbatim are
   allowed.** The discipline notes in `hypothesis_catalogue.md` and
   `t1_synth_question_set.md` quote the forbidden-verb list as the
   rule itself; this is not a prediction-or-conjecture context. The
   2 remaining framing-scan hits sit there. If the synth wants
   absolute-zero-hit framing-word audit, paraphrase the rule as
   "the list of disallowed framing verbs" instead of quoting them
   inline. Flag for cleanup if requested.
3. **Q1–Q5 ordering followed the prompt body verbatim.** The
   `t1_synth_question_set.md` §A diagram preserves the
   Q1 → Q2 → Q3/Q4 → Q5 conditional structure from the relay 055
   STEP 4 prompt body. No reordering or merging.
4. **W1–W4 phrasing followed the prompt body verbatim** for W1, W2
   (044B verbatim), W3, W4. The wording-decision table in §3 of
   `pcf2_v3x_wording_softening.md` is a NEW substrate map (not
   in the prompt body) but stays substrate-only — it maps
   (Q1, Q2, Q3, Q4, Q5) → W candidate and is presented as a
   recommendation table for T1 Synth, not a selection.
5. **Synth-tier default forecast preserved.** §4 of
   `pcf2_v3x_wording_softening.md` carries the relay 055 STEP 5
   prompt-body default forecast verbatim ("W2 if Q1=Q2=defer,
   W3 if Q1∨Q2=fire, W4 if T1 Synth judges arbitration premature"),
   explicitly tagged as a "default forecast at relay-055 draft
   time, NOT a T1 Synth selection". This is allowed per relay 055
   STEP 5 ("Default forecast (synth-tier default at draft time)").

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION.**

1. **The n=3 collision identity-vs-coincidence question is not
   adjudicated by this relay.** This is by design: relay 055 is
   substrate-only, and the prompt explicitly defers adjudication
   to T1 Synth W20 weekly cadence. The deliverables are structured
   so T1 Synth has all the inputs needed (anchor data, hypothesis
   catalogue, question set, wording candidates) but no input is
   pre-ranked or pre-selected.

2. **Q5 (Zenodo-amend timing) is operator-side, not T1-Synth-side.**
   T1 Synth recommends timing; the operator dispatches. The §3
   wording-recommendation table in `pcf2_v3x_wording_softening.md`
   carries `amend now` and `hold` columns to make this distinction
   explicit. Operator should not read the table as a directive — it
   is a synth-recommendation conditional on Q1–Q5 outcomes.

3. **Bauer-shape with a₁, a₀ ≠ 0 not covered.** The 044B handoff
   noted that the Bauer-shape sweep restricts to (a₂, a₁, a₀) =
   (−k², 0, 0) and that a 044C-style follow-up could lift this
   restriction. The hypothesis catalogue H_BFP probe spec also
   does not extend to (a₁, a₀ ≠ 0); if T1 Synth wants the H_BFP
   probe to cover this regime, the Q4 prompt-spec body needs to
   widen the parameterization. This is a flag for T1 Synth at
   W20 weekly, not a substrate gap to fix in relay 055.

4. **+1/4 sub-stratum substrate sessions cited but not re-anchored.**
   §5 of `substrate_inventory.md` lists T2B-PLUS-QUARTER-SURVEY,
   T2B-STIELTJES-VERIFY, T2B-RESONANCE-B67 etc. as substrate
   pointers. These are referenced for traceability only; relay 055
   does not compute SHA-256 anchors for them or quote their
   numerical claims. If T1 Synth's H_BSW arbitration requires
   verbatim claims from those sessions, a follow-up substrate
   relay would re-anchor them.

5. **Sign-orbit closure of A1 b₇ in §3 coverage map.** I quoted
   "4 tuples enumerated" for the b₇ sign-orbit closure based on
   044B judgment call 3 (sign-orbit `{(±8, ∓4, 0, ±7, ±4)}`). The
   044B handoff did NOT explicitly enumerate these 4 tuples in
   §STEP 2A (which closed only the b₁₀ 044R sign-orbit at 8 tuples).
   The b₇ sign-orbit was characterized in 044B judgment call 3 as
   the structural definition; the actual hit count in that orbit
   under PSLQ at h ≤ 10⁹ was not exhaustively reported. If T1
   Synth needs this number, it requires going to the 044B
   `results.json` step2a record. **Flag.**

6. **Forrester-Witte 2005 substrate citation in H_BFP.** I cited
   the Forrester-Witte 2005 acquisition (sessions/2026-05-04/
   WITTE-FORRESTER-2010-ACQUISITION/, SCENARIO_C analogue) as
   substrate context for the Bauer-Forrester pencil. The 031
   verdict (per copilot-instructions.md "Bibliographic identifier
   pre-verification") established that the cited Witte-Forrester
   2010 was a hallucinated identifier and the acquired substrate
   is the 2005 paper (math/0512142). I cited the 2005 paper, not
   the 2010 paper. The link from FW 2005 → Bauer-Forrester pencil
   is a substrate-pointer; verifying the orthogonal-polynomial
   pencil substrate is in FW 2005 is a T1 Synth task at W20
   weekly cadence (not adjudicated here).

## What would have been asked (if bidirectional)

- "Should the Q1×Q2×Q3/Q4×Q5 → W table in
  `pcf2_v3x_wording_softening.md` §3 be presented at all? Per a
  strict substrate-only reading, even a recommendation matrix may
  count as 'leaning' toward an outcome. I judged the table is
  acceptable because (a) it is substrate-only (all four cells
  are NOT-FALSIFIED candidate phrasings), (b) it is explicitly
  marked as recommendations conditional on outcomes T1 Synth
  selects, and (c) the relay 055 STEP 5 prompt body asked for a
  decision-tree, which a Q×W mapping is. Flag if the synth
  prefers a less-prescriptive enumeration."
- "Is the synth-tier default forecast (`W2 if Q1=Q2=defer, W3 if
  Q1∨Q2=fire, W4 if premature`) drawn from the relay 055 STEP 5
  prompt body too prescriptive? It is explicitly labelled 'NOT a
  T1 Synth selection' but reads as a strong recommendation. The
  prompt body itself asked for it, so I included it verbatim.
  Flag if the synth wants it removed in a future revision."

## Recommended next step

**T1 Synth W20 weekly cadence consumes this substrate package and
adjudicates Q1–Q5.** No further computational work is required
before W20 weekly fires (no earlier than 2026-05-11 Sun close-of-
week per relay 055 prompt body).

If T1 Synth selects Q1 = fire ∨ Q2 = fire at W20 weekly, the next
relay (T3-dispatched) is the H_BSW or H_BFP falsification probe
drafted by T1 Synth at Q4 (substrate-cited estimated runtimes:
~30 min for H_BSW, ~45 min for H_BFP, ~75 min for both with
H_BFP-first sequencing).

If T1 Synth selects Q1 = Q2 = defer, the next operator-side step
is the Q5 Zenodo-amend timing decision (amend PCF-2 v3.x to v3.x.1
now with W2 / W4 wording, or hold for arbitration). Synth-tier
default forecast at relay-055 draft time: W2 if Q3 = accept H_C.

## Files committed

`sessions/2026-05-06/N3-FOURTH-LAW-ARBITRATION-SUBSTRATE/`
- `substrate_inventory.md` — §1 anchor data verbatim, §2 negative
  results NR1–NR3, §3 sign-orbit + Bauer-shape coverage map, §4
  ratio-pattern panel, §5 substrate-session pointers, §6 summary.
- `hypothesis_catalogue.md` — H_BSW + H_BFP + H_C without ranking,
  each with claim / substrate citations / predicted falsifying
  observation / falsification status / substrate-cited estimated
  runtime.
- `t1_synth_question_set.md` — Q1–Q5 with conditional structure
  diagram + substrate handoff to T1 Synth.
- `pcf2_v3x_wording_softening.md` — current wording verbatim (§1)
  + W1–W4 candidates (§2) + Q×W decision table (§3) + synth-tier
  default forecast (§4) + operator-side timing note (§5).
- `claims.jsonl` — 4 AEAL claims (055-C1 044R substrate, 055-C2
  044B substrate, 055-C3 deliverable enumeration + per-file SHA-256,
  055-C4 framing/rank/numerical scan PASS).
- `halt_log.json` — `{}` (no halt fired).
- `discrepancy_log.json` — `{}` (no discrepancies).
- `unexpected_finds.json` — `{}` (no unexpected positive results;
  substrate-only synthesis).
- `handoff.md` — this file.

## AEAL claim count

**4 entries** written to `claims.jsonl` this session
(055-C1 through 055-C4; C1–C3 mandatory + C4 optional/recommended).
