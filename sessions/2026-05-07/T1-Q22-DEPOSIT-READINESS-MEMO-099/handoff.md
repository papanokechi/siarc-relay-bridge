# Handoff — T1-Q22-DEPOSIT-READINESS-MEMO-099
**Date:** 2026-05-07
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~70 minutes
**Status:** COMPLETE_PATH_A_RECOMMENDED

## What was accomplished

Drafted a 1-page PCF-2 v1.4 Q22 deposit-readiness threshold-sufficiency
memo that converts Q22 from operator-deferred (1 of 6 deferrals at the
W19/W20 hand-off) to operator-ratification-only. The memo recovers the
|delta| envelope from the path-(a) substrate (3.08904186542e-23 at
K_FIT=7 / dps=25000 / N up to 1200, max across the four j=0 cubic
families Q_30..Q_33), assembles a 4-anchor comparable-paper precedent
table with all identifiers pre-verified at fire time per the post-031
rule, concludes path-(a) is deposit-eligible NOW under all four
precedent rows, and reclassifies path-(b) (K_FIT=9, N=2400, ~24-hr
high-compute fire) as a POST-deposit stretch goal rather than a deposit
gate. Three production deliverables were authored (precedent_table.md,
threshold_sufficiency_analysis.md, q22_deposit_readiness_memo.md) plus
the AEAL quartet (claims.jsonl, halt_log.json, discrepancy_log.json,
unexpected_finds.json). All halts checked PASS; 5 AEAL claims logged
(>=4 floor); forbidden-verb scan PASS (0 hits) on all 3 production
files.

## Key numerical findings

- |delta_path_a| = 3.08904186542e-23 (substrate verbatim from
  pcf2_v1.4_amendment.md SHA16 88845089434F96EF, 11-parameter LIN
  refit; verdict label PASS_A_EQ_6_ONLY at sessions/2026-05-02/T25D-RETRY-13PARAM/)
- |delta_path_b| = unrealized; substrate-derived theoretical
  truncation floor at K_FIT=9, N=2400 is ~ 2400^-10 ~= 1.7e-34
  (~11-order improvement over path-(a))
- Chowla-Selberg PSLQ at maxcoeff = 10^50, tol = 10^-40 on H6 basis
  B19+ returns no non-trivial Gamma(1/3) relation in any of the four
  families (substrate verbatim)
- Per-family A_lin readouts: 5.99999999999999999999999 (fam30, fam31),
  5.99999999999999999999998 (fam32), 5.99999999999999999999996 (fam33)
  at dps=25000 (load_log.txt L11/L14/L17/L20 substrate)
- Reviewer A (peer-AI synthesis 4-of-4, 2026-05-07): "23-digit
  agreement is roughly 10^8 beyond what PSLQ-style identifications
  usually require for publication" (HIGH confidence on this clause)
- Reviewer D (peer-AI synthesis 4-of-4, 2026-05-07): HIGH confidence;
  "move to deposit Path-a immediately" verbatim recommendation

## Judgment calls made

**J1.** Pre-verification of relay-099 PHASE C suggested-anchor C1
revealed the BBP / Broadhurst arXiv conflation (D1 in
discrepancy_log.json). The relay prompt suggests `arXiv math.CA/9803067`
is the BBP 1997 paper, but it actually resolves to Broadhurst 1998.
Judgment call: cite both papers as separate genre-precedents in
precedent_table.md (BBP by Math. Comp. DOI; Broadhurst by arXiv ID),
and surface the conflation in handoff Anomalies rather than substituting
or omitting either anchor. Both are legitimate genre-precedents
independently. This follows the post-031 verdict procedure
("either substitute a verified identifier for the same intended paper,
or substitute a different paper that serves the same purpose"); here
both intended papers are available verbatim, so no substitution was
needed.

**J2.** Relay-099 D1 wording '~10^21000 precision improvement' and
Reviewer D '10^-44300' figure are mutually inconsistent and neither
is derivable from substrate truncation-floor estimates. Judgment call:
record both verbatim in unexpected_finds.json U1-U2 as substrate-quoted
framings, and use only the substrate-derived ~1.7e-34 truncation-floor
estimate (~11 orders over path-(a)) as the load-bearing path-(b)
precision number. The threshold-sufficiency verdict does not depend
on the path-(b) figure; this judgment call is conservative.

**J3.** Memo length: relay-099 PHASE E asks for a "1-page memo".
The drafted q22_deposit_readiness_memo.md is 6215 B / 98 lines, which
is ~1 typeset page in standard markdown rendering but exceeds a
strict 1-page printed boundary if the precedent-table block is
formatted wide. Judgment call: kept the 4-row precedent table inside
the memo for self-containment, and treated the supporting full
precedent_table.md and threshold_sufficiency_analysis.md as the
"appendix" the memo points back to. This matches Reviewer C's
"compact deposition readiness dossier" framing (Q1 reasoning).

**J4.** Borwein-Bailey 1st-edition year drift (relay says 2003;
Wikipedia + ISBN registry say 2004). Judgment call: cite 2004 per
the verified record in the memo and precedent table; surface the
relay-099 wording as discrepancy D2; do not modify relay-099 or
treat as a halt.

**J5.** Path-(a) K_FIT realization is K_FIT=7 (11-param) per substrate
load_log.txt, not K_FIT=9 (13-param) as the 014 prompt title
"RETRY-13PARAM" suggested. Judgment call: cite 11-param consistently
in all deliverables (matches verdict.md headline "At 11-parameter
refit (7 1/n correction terms)..."), and document the K_FIT=7
realization in discrepancy_log.json D3. The verdict label
PASS_A_EQ_6_ONLY is unaffected.

## Anomalies and open questions

**A1 — Two mutually-inconsistent path-(b) precision figures in upstream
substrate.** Relay-099 says `~10^21000`; Reviewer D says `10^-44300`;
the substrate truncation-floor calculation says `~1.7e-34` (11-order
gain). All three figures are internally inconsistent. The memo does
not depend on which is correct. **Open question for synthesizer:** if
operator chooses (O) override and commands path-(b), what is the
target |delta_path_b| acceptance criterion?

**A2 — BBP arXiv ID hallucination in the relay-099 prompt body
itself.** The relay prompt's PHASE C list of suggested anchors contains
a hallucinated identifier (`arXiv math.CA/9803067` is not the BBP
paper). Pre-verification at fire time per post-031 rule caught it.
**Open question:** does the relay-099 prompt-drafting trail (CLI-Synth)
need a re-fire or amendment to correct the hallucinated identifier?
Verdict here uses both papers correctly, so no agent-side action is
required. **Note:** this is a within-prompt hallucination, not within
substrate; the prompt's own pre-verification disclaimer ("agent may
verify at fire time") anticipated this exact path.

**A3 — Path-(a) realized at K_FIT=7, not K_FIT=9 as 014 prompt
target.** The 014 prompt title is "RETRY-13PARAM" but the actual
fired refit was 11-param. The amendment substrate is internally
consistent on this; only the prompt title is misleading. **Open
question:** is the operator's understanding of "path-(a) at
K_FIT/N currently-realized" calibrated to 11-param, or to a 13-param
that was never actually fired? The memo cites 11-param consistently
to remove ambiguity. **If the operator reads "K_FIT/N currently-realized"
as 13-param, recommend re-fire of the prompt with explicit K_FIT=7
substrate citation.**

**A4 — Stretch-goal compute envelope unanchored.** The relay-099
prompt body cites "K_FIT=9 N=2400 ~24-hr high-compute fire" but
provides no peak-RAM or maxcoeff envelope for the path-(b) PSLQ
search. **Open question:** if operator chooses (O) override, what is
the path-(b) PSLQ basis (presumably H6 B19+ as path-(a)) and the
maxcoeff/tol floor? The memo does not attempt to scope path-(b)
beyond citing the operator-supplied "~24-hr" number.

**A5 — Reviewer-supplied venue precedents are genre-only.** Row 4
of the precedent table cites Ramanujan J. / Exp. Math. / Res. Number
Theory by venue name only (per Reviewer A 2026-05-07), not by specific
deposited-paper anchor. **Open question:** if the operator wants
specific paper-by-paper venue precedents in the deposited PCF-2 v1.4
appendix, a follow-up envelope to harvest 2-3 specific
PSLQ-no-relation deposits from each venue (~1 hr) would close this
gap. Not a deposit blocker.

## What would have been asked (if bidirectional)

1. "The path-(a) realization is K_FIT=7 (11-param), not K_FIT=9 (13-param)
   as 014's prompt title 'RETRY-13PARAM' suggests. Confirm this is
   path-(a) as understood by the operator, OR confirm a re-fire at
   K_FIT=9 / N=1200 (without the N=2400 stretch) is the real
   path-(a) intended."
2. "Relay-099 D1 says path-(b) gains ~10^21000 in precision; Reviewer
   D says 10^-44300; substrate-derived truncation floor at K_FIT=9
   N=2400 says ~1.7e-34 (~11-order gain). Which is the operator's
   understanding of path-(b) target, and is the gap material for the
   deposit decision?"
3. "Should the deposited PCF-2 v1.4 appendix include 2-3 specific
   deposited-paper anchors per venue (Ramanujan J., Exp. Math., Res.
   Number Theory) as concrete precedent, or is the genre-name citation
   sufficient?"

## Recommended next step

If the operator picks (R), the next relay prompt should be a Zenodo
deposit-substrate envelope for PCF-2 v1.4 path-(a). Pattern: mirror
the 017 / 018 splice envelope, with the path-(b) stretch documented
as an appendix and explicitly flagged "post-deposit, optional, not
deposit-blocker". The amendment text (1151 B at SHA16 88845089434F96EF)
is small enough to inline in the deposit substrate verbatim.

If the operator picks (O), the next relay prompt should specify the
path-(b) target |delta| acceptance criterion and the PSLQ search
parameters explicitly (resolving Anomalies A1 and A4 above).

If the operator picks (D), the next relay prompt should specify which
precedent row was inadequate and what additional precedent is needed.

## Files committed

Bridge path `siarc-relay-bridge/sessions/2026-05-07/T1-Q22-DEPOSIT-READINESS-MEMO-099/`:

- `precedent_table.md`  (5154 B / 54 lines / SHA16 F34C3096F8484B77)
- `threshold_sufficiency_analysis.md`  (6631 B / 111 lines / SHA16 137A7DAF718D18D1)
- `q22_deposit_readiness_memo.md`  (6215 B / 98 lines / SHA16 9594A0FFBC46FED0)
- `claims.jsonl`  (2886 B / SHA16 91495A64CA140DE9; 5 AEAL entries)
- `halt_log.json`  (925 B / SHA16 48C16BF541EB7484)
- `discrepancy_log.json`  (3338 B / SHA16 87C73928B35BC6D3; 4 entries D1-D4)
- `unexpected_finds.json`  (2084 B / SHA16 84AFD9A85624C494; 2 entries U1-U2)
- `handoff.md`  (this file)

## AEAL claim count

5 entries written to `claims.jsonl` this session (099-B-1 / 099-C-1 /
099-D-1 / 099-E-1 / 099-F-1). Suggested floor was 5; actual = 5.
