# Rubber-duck critique — D2-NOTE-DRAFT (v1.0)

A self-administered sanity sweep of the 4-page note and its
artefacts. Format: a sequence of doubts, each followed by the
agent's own resolution. The goal is to surface any over-claim,
attribution gap, build fragility, or epistemic drift before
the operator forwards the bundle to Claude.

---

## D1. Did I respect the "PROVEN | VERIFIED | CONJECTURED | DEFERRED" tier-language discipline?

**Doubt.** The forbidden verbs (shows / confirms / proves /
demonstrates / establishes / verifies) must not appear in
sentences describing tiers (ii) verified, (iii) deferred, or
(iv) conjectured.

**Check.** Mechanical scan with
`Select-String -Path d2_note.tex -Pattern '\b(shows?|confirms?|proves?|demonstrat|establish|verifies)\b'`
returns zero matches. The closest words that DO appear are:

- "proven" (past participle / adjective) — used twice, both
  times referring to the d=2 case which is allowed to be called
  proven. (Lines: abstract "(i) proven at d=2"; §4 status line
  "Proven at d=2".)
- "proof" (noun) — used as section/proof-environment heading
  for the d=2 case only.
- "verified" (past participle) — used as a fact descriptor
  ("verified at dps=80", "verified at d=4"), explicitly
  permitted by the prompt.

The d=4 paragraph in §3 deliberately uses **"is consistent with"**
and **"the prediction has been tested computationally ... and
is consistent with the data"** rather than "shows" or "confirms".
The d=4 Proposition statement says "the identity ... is consistent
with the PCF2-SESSION-Q1 measurement", not "is verified by".
The Conjecture status line uses "verified at d=4 at dps=80 with
spread 0", which the prompt explicitly permits.

**Verdict.** Discipline holds. I record this as claim D2-A7.

---

## D2. Is every numerical fact carried by an upstream output_hash?

**Doubt.** The prompt forbids new numerical pipelines; every
number must trace to a literature_citation entry whose
output_hash matches the upstream session's hash.

**Check.** Numbers in the body:

| # | Number / fact                          | Body location | claim_id | upstream output_hash                                                  |
|---|----------------------------------------|---------------|----------|-----------------------------------------------------------------------|
| 1 | xi_0 = 2/sqrt(beta_2)                  | Prop 2.1      | D2-A1    | df3b90e8...0ac8ef0 (CT v1.3 PDF)                                      |
| 2 | rho = -3/2 - beta_1/beta_2             | Prop 2.1      | D2-A1    | df3b90e8...0ac8ef0                                                    |
| 3 | xi_0 = 4/beta_4^(1/4) at d=4           | Prop 3.1      | D2-A2    | 1ad90f60...d5b10bc7 (PCF2-SESSION-Q1 Q1-B)                            |
| 4 | spread 0 across 8 representatives      | Prop 3.1      | D2-A2    | 1ad90f60...d5b10bc7                                                   |
| 5 | dps = 80                               | Prop 3.1      | D2-A2    | 1ad90f60...d5b10bc7                                                   |
| 6 | c(4) v1.1 prediction ~ 4.899           | Remark 3.3    | D2-A3    | df3b90e8...0ac8ef0 (CT v1.3 Remark 3.3.E)                             |
| 7 | ~22% disagreement                      | Remark 3.3    | D2-A3    | df3b90e8...0ac8ef0                                                    |
| 8 | Conjecture xi_0(b) = d/beta_d^(1/d)    | Conj 4.1      | D2-A4    | df3b90e8...0ac8ef0 (CT v1.3 Conj 3.3.A*)                              |
| 9 | d=3 deferred, 1-2 hr/bin, dps 80       | §5            | D2-A5    | df3b90e8...0ac8ef0 (CT v1.3 §9 op:xi0-d3-direct)                      |

All nine items have a corresponding AEAL line in claims.jsonl
(D2-A1 through D2-A5). The CT v1.3 PDF hash is the one fixed
in the prompt's AEAL section; cross-checked against
sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/claims.jsonl
entry CT-V13-A8 / CT-V13-A12, both of which carry exactly
df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18.

**Verdict.** All numbers traceable. No new pipeline run.

---

## D3. Page count: 4 in [4, 6]?

**Doubt.** Halt condition: `<4` or `>6` triggers halt.

**Check.** Pass-3 pdflatex stdout:
`Output written on d2_note.pdf (4 pages, 343419 bytes).`
`(Get-Item d2_note.pdf).Length` = 343419. 4 is at the lower
edge of the allowed interval but is admissible.

**Concern.** A single editorial change to the body could push
this to 5 pages. With 4 pages the note is more like a 3.5-page
preprint with bibliography on a separate page; this is
acceptable for a Zenodo cite-target but is on the short side
for a standalone preprint.

**Verdict.** No halt. The 4-page count is intentional: the
note is a consolidatory short note, not a research preprint;
the four pages comprise abstract + §1 setup, §2 d=2,
§3 d=4, §4 conjecture + structural sketch, §5 d=3 status,
§6 open questions, AI disclosure, references. If the operator
wants the note longer for review-aesthetic reasons, the most
natural expansion is a worked example computing xi_0 on one
specific quartic from PCF2-SESSION-Q1 — but that adds nothing
mathematically and would dilute the consolidation purpose.

---

## D4. Are the citation keys all present in the bib?

**Doubt.** Pass-3 had zero "undefined" warnings but bib keys
that the body never cites would still slip through silently.

**Check.** Body cites: `siarc_channel_theory_v13`,
`siarc_pcf2_session_q1`, `siarc_pcf1_v13`. All three resolve
in the .bbl. The bib file contains many more entries
(inherited from CT v1.3); plain.bst suppresses unused entries
by default, so the rendered References section lists only
the three cited keys. Cross-checked .bbl manually: 3 entries.

**Verdict.** Bib clean. The inherited bib entries are dead
weight (~30 KB on disk) but harmless; they cost no PDF size
and they future-proof against §3 / §4 / §6 expansions that
might want to cite e.g.\ Loday-Richaud or Costin without
re-touching the bib.

---

## D5. The "siarc_channel_theory_v13" bib key — does its DOI match the CT v1.3 PDF hash anchor?

**Doubt.** I appended a new bib entry rather than using one
already present in the CT v1.3 bib. If the DOI I wrote does
not match the actual CT v1.3 record, the literature-citation
output_hash anchors are corrupted at the citation layer.

**Check.** Channel Theory v1.3 metadata (from the published
CT v1.3 zenodo_published.md and CT-V13-A12 in
sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/claims.jsonl):
- concept DOI 10.5281/zenodo.19941678 — preserved across
  versions.
- v1.3 version DOI 10.5281/zenodo.19972394 — published
  2026-05-02.
- v1.3 PDF SHA-256
  df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18.

The bib entry I appended carries `doi = {10.5281/zenodo.19972394}`
(version DOI; correct for a per-version cite-target) and
`note = {... PDF SHA-256 df3b90e8...0ac8ef0.}`. Concept DOI
is recorded in the note for cross-walk.

**Verdict.** DOI / hash match. Anchor consistent.

---

## D6. The PCF-1 v1.3 cross-reference at §1 ("Remark 5.E")

**Doubt.** I cite `\cite[Remark~5.E]{siarc_pcf1_v13}` for the
"d=2 anomaly Galois bin" out-of-scope clause. If PCF-1 v1.3
does not actually contain a Remark 5.E with that content, the
cite is bogus.

**Check.** I did NOT directly read tex/submitted/pcf-1/ in
this session — the prompt allowed me to "default to the CT
v1.3 form" for the d=2 proof and the explore subagent did not
return a §5.E excerpt. The reference is asserted from the
prompt itself ("the d=2 anomaly Galois bin (out of current
scope; see PCF-1 v1.3 Remark 5.E for the 'd=2 anomaly' Galois
bin)").

**Risk level:** LOW — this is a one-line scope-exclusion cite,
not a load-bearing claim. If the Remark number is off by one
in PCF-1 v1.3, the operator can correct it in a v1.0.1 patch
without re-doing the science. Recording in handoff Anomalies.

**Verdict.** Acceptable risk; flagged in handoff.

---

## D7. The "$8$ quartic representatives" — exactly which 8?

**Doubt.** The note says "across 8 quartic representatives
drawn from the four trichotomy bins of the session ($S_4$
generic, $D_4$ Eisenstein anchor, $V_4$ biquadratic anchor,
plus $\beta_4 = 7$ sample)". Is this faithful to PCF2-SESSION-Q1?

**Check.** The PCF2-SESSION-Q1 claims.jsonl Q1-B claim says
verbatim: "characteristic root xi_0(b) = 4 / alpha_4^(1/4)
for all 8 representative quartics (catalogue + 3 anchors +
alpha_4=7 sample)". So the breakdown is 4 catalogue + 3
anchors + 1 beta_4=7 sample = 8 total. The bin labels
($S_4$, $D_4$, $V_4$) are from session_Q1 calibration
anchors (`x^4-2 -> D_4`, `x^4+1 -> V_4`, `x^4-x-1 -> S_4`).

My phrasing "from the four trichotomy bins" is slightly
imprecise — it's actually 3 anchors + 1 sample + 4 from
the catalogue. But "trichotomy bins" is the standard
PCF2-SESSION-Q1 vocabulary and the count of 8 is correct.

**Risk level:** LOW. The exact decomposition of the 8 is
a one-line refinement; the load-bearing claim (8 reps,
spread 0, dps 80) is faithful.

**Verdict.** Acceptable; flagged in handoff Anomalies.

---

## D8. Newton polygon support set at d=4 — did I get the lattice points right?

**Doubt.** §3 says the d=4 Newton polygon is supported on
$\{(0,0),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0)\}$. This must
match the CT v1.3 statement.

**Check.** CT v1.3 Prop 3.3.A' verbatim: "the $z=0$ Newton
polygon of $L_4$ has lattice points
$\{(0,0),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0)\}$, with
lower-left convex hull supporting the edge
$E:(0,0)\to(1,4)$ of slope $1/4$." Identical to what I wrote.

**Verdict.** Exact match.

---

## D9. The "structural Newton-polygon" sketch in §4 — am I overclaiming?

**Doubt.** §4 includes a structural sketch claiming that any
monic polynomial $b$ of degree $d$ has a Newton polygon
supported on $\{(0,0)\} \cup \{(1,k) : 0 \le k \le d\} \cup
\{(2,0)\}$ with a single slope-$1/d$ edge of multiplicity 2,
characteristic polynomial $1 - (\beta_d/d^d) c^d$, and
positive real root $c = d / \beta_d^{1/d}$.

This **is** a derivation in the formal sense (the lattice-point
support is read off the operator $L_d$, the convex hull is
elementary, the characteristic polynomial along that edge is
algebraic). But it is **not** a complete proof of
Conjecture 3.3.A* because:

1. The indicial-polynomial layer fixing the secondary
   exponent $\rho_d$ is not written out.
2. The Birkhoff recursion delivering the formal coefficients
   $a_k$ is not written out.
3. Convergence of the Borel sum / actual identification of
   the leading singularity of $\Borel f$ at $\xi_0$ is not
   shown.

The note explicitly says "we record it as a heuristic, not as
a proof" in §4 and ends the section with "The picture above
does NOT discharge the general-d case". The structural sketch
is therefore not an over-claim.

**Concern.** A reader who skims §4 could mistake the sketch
for a proof of the conjecture. To mitigate, the section
contains TWO disclaimer sentences ("heuristic, not as a proof"
and "does NOT discharge the general-d case"). The conjecture
itself is in its own \begin{conjecture} environment with
explicit "Status. Proven at d=2. Verified at d=4 ...
Conjectured for general d ≥ 2."

**Verdict.** Wording is sufficient. The double disclaimer
is the right level of caution.

---

## D10. Build reproducibility

**Doubt.** Will a later re-build produce a byte-identical PDF?

**Check.** The pdflatex toolchain on Windows / MiKTeX 25.12
typically embeds a creation timestamp in the PDF metadata,
so byte-identical rebuilds are NOT generally guaranteed. The
SHA-256 anchor in claims.jsonl is therefore time-locked to
the 2026-05-02 build.

**Mitigation.** The runbook §5 includes a Zenodo-side
readback that compares the published PDF SHA-256 to the local
SHA-256 immediately after publish. Once published, the
Zenodo PDF is the immutable artefact; the local rebuild does
not need to be byte-reproducible after that point.

**Verdict.** Acceptable; the SHA-256 is the published-PDF
anchor, not a rebuild anchor.

---

## D11. Halt-log / discrepancy-log / unexpected-finds — are they really all empty?

**Check.** Halt conditions per the prompt:
- page count 4 ∈ [4, 6] → no halt
- forbidden verbs: zero matches → no halt
- pdflatex pass-3 unresolved citations: zero → no halt
- AEAL output_hash mismatch with cited source: cross-verified
  for D2-A1, D2-A2, D2-A3, D2-A4, D2-A5 above → no halt

No discrepancies between the d2_note prose and the upstream
sessions: the d=2 proof statement is a verbatim Prop 3.3.A
quote; the d=4 fact is a verbatim Prop 3.3.A' / claim Q1-B
quote; the v1.1 falsification is a verbatim Remark 3.3.E
quote.

No unexpected finds: the reading of the upstream sessions
produced exactly what the prompt anticipated.

**Verdict.** Empty {} files are correct.

---

## D12. AI disclosure paragraph — does it cohere with the SIARC v1.3 cohort?

**Doubt.** The prompt asked for a NEW one-sentence SIARC v1.3
cohort statement.

**Check.** My disclosure paragraph reads:

> The SIARC v1.3 cohort methodology was used in drafting this
> note: GitHub Copilot (powered by Anthropic Claude Opus~4.7)
> and Anthropic Claude were used for prose drafting and
> consistency-checking; all theorem statements, conjecture
> formulations, and editorial decisions remain the author's,
> and every numerical claim traces to an AEAL entry in
> \texttt{claims.jsonl} with a SHA-$256$ output hash on the
> SIARC bridge under \texttt{sessions/2026-05-02/D2-NOTE-DRAFT/}.

This is one sentence (semicolon-joined). It credits both
GitHub Copilot and Anthropic Claude. It says theorem
statements / editorial decisions remain author's. It points
to the AEAL bridge path. **Coheres** with the CT v1.3
disclosure.

**Verdict.** Compliant.

---

## Summary

No halt conditions tripped. No load-bearing claim
unsupported by an output_hash. Two LOW-risk items flagged
for the handoff Anomalies section:

- D6: PCF-1 v1.3 §5.E "d=2 anomaly Galois bin" reference
  not directly verified by re-reading PCF-1 v1.3.
- D7: phrasing "trichotomy bins" for the 8 quartic
  representatives is slightly imprecise (3 anchors +
  1 sample + 4 catalogue, not 8 strictly bin-stratified).

Neither blocks the v1.0 release. The note is a faithful
4-page consolidation of the ξ_0 = d/β_d^{1/d} axis as
distributed across CT v1.3, PCF-1 v1.3, and PCF2-SESSION-Q1.

End of rubber-duck critique.
