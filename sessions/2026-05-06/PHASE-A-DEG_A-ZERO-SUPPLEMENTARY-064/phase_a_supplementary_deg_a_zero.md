# Phase A WZ-balance table — supplementary `deg_a = 0` row

**Task ID:** `PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064`
**Date:** 2026-05-06 (W20)
**Authoring tier:** T3 mechanical write-up (substrate already produced in
LANE-2 deposit `dee3c01`; no fresh symbolic re-derivation in this document).
**Authorisation:** LANE-2 Item 2 sub-task 3-A AUTHORIZE (write-up only;
verdict at `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/handoff.md` L162-164).
**Required revision implemented:** LANE-2 R3 — Phase A baseline framing
(verdict text at `lane2_meta_verdict.md` L79-99).

---

## 1. Scope and relationship to `bt_baseline_note` v1.0

This supplement extends the Phase A WZ-balance enumeration of
`bt_baseline_note.tex` v1.0 (file SHA-256
`6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B`,
38023 B; deposit at
`siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex`)
by one row corresponding to the corner $\deg_a = 0$ (i.e., $a_n \equiv 1$,
the canonical $(1, b)$ continued fraction used by every harvest script
enumerated in LANE-2 substrate P1). The `bt_baseline_note.tex` v1.0
source remains canonical and is unmodified by this supplement, per the
LANE-2 Item 3 verdict `LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE`
(verdict text at `lane2_six_item_verdict.md`). A separate Item 3
follow-up note (anticipated as relay 067) carries any retraction
language for v1.0 §4.2 (i'); the present document does not.

The required revision under R3 (LANE-2 meta-verdict L79-99) reads in
its operative form:

> "Phase A's WZ table at `phase_a_summary.md` L34-44 enumerates THREE
> SIARC conventions ($\alpha$/symmetric/$\delta$-direction) corresponding
> to $\deg_a \in \{d-1, d, d+1\}$. The $\deg_a = 0$ row was excluded by
> ASSUMPTION via this three-convention framing, not by oversight. Phase
> D's 'structural gap' verdict (gap framing of $A_{\rm fit} \approx 2d$
> vs $A_{\rm naive} \in \{1, 2, 3\}$ at $d=2$ etc.) is the proximate
> consequence of this assumption. Adding the $\deg_a = 0$ row
> ($\mu_{\rm dom} = d$, $\mu_{\rm sub} = -d$, $A_{\rm naive} = 2d$,
> $\gamma_{\rm sub} \propto -c_a/c_b$) closes the d=2 V_quad anomaly,
> the d=3 R1.1+B+C1 110/110 record, and the d=4 Q1 60/60 record
> simultaneously, WITHOUT invoking borderline mechanism (i') or
> exceptional locus (ii')."

The remainder of this supplement renders the extended four-row
enumeration as a self-contained reference; quotes the V6 derivation
that yields $A_{\rm naive} = 2d$ at $\deg_a = 0$; and notes the
row-membership consequence for V_quad. All claims cite primary
substrate via SHA + line range; no fresh symbolic computation appears.

---

## 2. Extended Phase A WZ-balance table (with $\deg_a = 0$ row)

### 2.1 Original Phase A nine-row enumeration (substrate citation)

The Phase A WZ table is rendered in
`siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_a_summary.md`
L34-44 (cited verbatim via LANE-2 P2 substrate at
`independent_depth_probe.md` L77-87, file SHA-256
`20764101FCDEA73A57EE92B80C97B3EA…`, 16698 B):

| d | Convention   | deg a | deg b | μ_dom | μ_sub | A_naive |
|---|--------------|-------|-------|-------|-------|---------|
| 2 | α-direction  | 1     | 2     | 2     | −1    | 3       |
| 2 | symmetric    | 2     | 2     | 2     |  0    | 2       |
| 2 | δ-direction  | 3     | 2     | 2     |  1    | 1       |
| 3 | α-direction  | 2     | 3     | 3     | −1    | 4       |
| 3 | symmetric    | 3     | 3     | 3     |  0    | 3       |
| 3 | δ-direction  | 4     | 3     | 3     |  1    | 2       |
| 4 | α-direction  | 3     | 4     | 4     | −1    | 5       |
| 4 | symmetric    | 4     | 4     | 4     |  0    | 4       |
| 4 | δ-direction  | 5     | 4     | 4     |  1    | 3       |

These nine rows enumerate the three SIARC conventions
$\alpha$/symmetric/$\delta$-direction at $\deg_a \in \{d-1, d, d+1\}$
for $d \in \{2, 3, 4\}$. The row-membership above is reproduced
verbatim from P2 substrate.

### 2.2 New $\deg_a = 0$ row (substrate citation: P2 + V6)

Applying balance (III) at $\deg_a = 0$ — the SIARC PCF corner used by
every harvest implementation per LANE-2 P1 — yields a fourth row at
each value of $d$. P2 substrate
(`independent_depth_probe.md` L121-126, SHA `20764101FCDEA73A…`)
records the three new rows verbatim:

| d | Convention            | deg a | deg b | μ_dom | μ_sub | A_naive |
|---|-----------------------|-------|-------|-------|-------|---------|
| 2 | (1, b) PCF-2 corner   | 0     | 2     | 2     | −2    | **4**   |
| 3 | (1, b) PCF-2 corner   | 0     | 3     | 3     | −3    | **6**   |
| 4 | (1, b) PCF-2 corner   | 0     | 4     | 4     | −4    | **8**   |

The numerical values $A_{\rm naive} = 2d$ at $\deg_a = 0$ are the
substrate of LANE-2 R3 and of LANE-2 V6 (`independent_substrate_verification.md`
L210-308, file SHA `56063BF7BA8AD6A0…`, 15695 B), where the
balance-III computation appears in full.

### 2.3 Combined twelve-row enumeration (sorted by $d$, then $\deg_a$ ascending)

| d | Convention          | deg a | deg b | μ_dom | μ_sub | A_naive |
|---|---------------------|-------|-------|-------|-------|---------|
| 2 | (1, b) PCF-2 corner | 0     | 2     | 2     | −2    | **4**   |
| 2 | α-direction         | 1     | 2     | 2     | −1    | 3       |
| 2 | symmetric           | 2     | 2     | 2     |  0    | 2       |
| 2 | δ-direction         | 3     | 2     | 2     |  1    | 1       |
| 3 | (1, b) PCF-2 corner | 0     | 3     | 3     | −3    | **6**   |
| 3 | α-direction         | 2     | 3     | 3     | −1    | 4       |
| 3 | symmetric           | 3     | 3     | 3     |  0    | 3       |
| 3 | δ-direction         | 4     | 3     | 3     |  1    | 2       |
| 4 | (1, b) PCF-2 corner | 0     | 4     | 4     | −4    | **8**   |
| 4 | α-direction         | 3     | 4     | 4     | −1    | 5       |
| 4 | symmetric           | 4     | 4     | 4     |  0    | 4       |
| 4 | δ-direction         | 5     | 4     | 4     |  1    | 3       |

Bold rows are those introduced by this supplement; all other rows are
reproduced verbatim from `phase_a_summary.md` L34-44 via P2.

The four-row enumeration $\deg_a \in \{0, d-1, d, d+1\}$ at each $d$
extends the original three-convention enumeration by the corner
case actually inhabited by the harvest scripts. Under this extended
enumeration, the column $A_{\rm naive}$ ranges over $\{1, 2, 3, 4\}$
at $d=2$; over $\{2, 3, 4, 6\}$ at $d=3$; and over $\{3, 4, 5, 8\}$
at $d=4$. The largest entry in each row-group is the $\deg_a = 0$
row, and equals $2d$.

---

## 3. Recessive-solution / Balance-III recap (V6 verbatim citation)

The $\deg_a = 0$ row entries $\mu_{\rm sub} = -d$ and
$A_{\rm naive} = 2d$ are derived in
`independent_substrate_verification.md` §V6, Step 3 (Recessive solution
(Balance III)) at L246-266, and §V6, Step 4 ($A_{\rm naive}$) at
L268-282 (file SHA `56063BF7BA8AD6A0…`, 15695 B). The relevant block
quotes verbatim (no re-derivation here):

> "The recessive $p_n^{\rm rec}$ has $r_n = r_+ \approx -b_n$, i.e.,
> $p_n^{\rm rec} / p_{n-1}^{\rm rec} \approx 1/r_+ \approx -1/b_n
> \approx -1/(c_b\,n^d)$. Then $p_n^{\rm rec} \sim (-1)^n\,c_b^{-n}\,(n!)^{-d}$,
> so $\log|p_n^{\rm rec}| = -d\,n\log n + (d - \log c_b)\,n -
> (d/2)\log n + \cdots$.
>
> $\mu_{\rm sub} = -d$ (the '$n\log n$' exponent of the recessive
> solution).
>
> $\gamma_{\rm sub} = -1/c_b \cdot e^d$ (with the SIGN coming from
> $r_+ < 0$ for $a_n, b_n > 0$)." (V6, L249-258)

> "$A_{\rm naive} = \mu_{\rm dom} - \mu_{\rm sub} = d - (-d) = 2d$
> (when deg_a = 0). … General formula:
> $A_{\rm naive} = 2d - d_a$." (V6, L274-282)

The dominant solution branch carries $\mu_{\rm dom} = d$ via Balance I
(V6, Step 2, L234-244):

> "By Stirling, $p_n \sim c_b^n\, n^{dn}\, e^{-dn}\, (2\pi n)^{d/2}$.
> In Birkhoff form $\log p_n = A\,n\log n + B\,n + C\,\log n + D + \cdots$:
> $\mu_{\rm dom} = A = d$ (the '$n\log n$' exponent of the dominant
> solution)." (V6, L240-244)

The sign $\gamma_{\rm sub} \propto -c_a/c_b$ noted in §2.2 above is
the rubber-duck-corrected leading-order observation recorded in V6,
Step 3, L260-266:

> "For the more general Wallis case $a_n \sim c_a\,n^{d_a}$ (deg_a = $d_a > 0$),
> the analogous derivation gives $r_+ \approx -b_n/a_n$ to leading order,
> hence $p_n^{\rm rec}/p_{n-1}^{\rm rec} \approx -a_n/b_n$, and
> $\gamma_{\rm sub} = -c_a/c_b \cdot (\text{Stirling cancellation factor})$.
> In the deg_a = 0 corner ($c_a = 1$, $d_a = 0$), this reduces to
> $\gamma_{\rm sub} = -1/c_b \cdot e^{d}$. The SIGN $-c_a/c_b$ at the
> leading 'geometric ratio' level is the robust observation; the
> Stirling-factor magnitude depends on convention." (V6, L260-266)

The above three blocks are the substrate underpinning the new $\deg_a = 0$
row entries in §2.2; this supplement does not repeat the derivation.

---

## 4. Consequence for Phase D's structural-gap framing

LANE-2 P2 substrate (`independent_depth_probe.md` L116-138, SHA
`20764101FCDEA73A…`) records the proximate-cause relation between the
omission of the $\deg_a = 0$ row in Phase A and the "structural gap"
language of Phase D. Quoting verbatim:

> "**P2 finding:** Phase A's omission of the deg_a = 0 row is the
> proximate cause of Phase D's 'structural gap' framing. When the
> deg_a = 0 row is admitted (corresponding to the (1, b) convention
> used by ALL harvest scripts per P1), the gap closes uniformly across
> $d \in \{2, 3, 4\}$ WITHOUT invoking borderline mechanism (i') or
> exceptional locus (ii'). This is INDEPENDENT corroboration of the
> synth-substitute's PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT verdict."
> (P2, L133-141)

Under the four-row enumeration $\deg_a \in \{0, d-1, d, d+1\}$ rendered
in §2.3, the records previously framed as "structurally above the
naive baseline" align with the $\deg_a = 0$ row at each $d$:

| $d$ | empirical $A_{\rm fit}$ | $\deg_a = 0$ row entry $A_{\rm naive} = 2d$ | row-membership |
|-----|------------------------|---------------------------------------------|----------------|
| 2   | $A = 4$ (V_quad)       | 4                                           | aligns         |
| 3   | $A_{\rm fit} \approx 5.978$ (R1.1+B+C1, 110/110) | 6                                | aligns         |
| 4   | $A_{\rm fit} \approx 7.954$ (Q1, 60/60)          | 8                                | aligns         |

(Empirical values cited from P2 L128-131; LANE-2 verdict body at
`lane2_meta_verdict.md` L93-98.) Under the extended four-row
enumeration, the d=2/3/4 gap closes WITHOUT invoking either of the
two mechanisms (i') (borderline locus) or (ii') (exceptional locus
where leading coefficients cancel) that Phase D had identified as
the only available routes under the original three-row enumeration.

The framing is neutral: this supplement records that the four-row
enumeration is consistent with the empirical records, that the
omission of the $\deg_a = 0$ row in the original three-row enumeration
explains why the records appeared structurally elevated under the
narrower framing, and that the LANE-2 R3 wording (block-quoted in
§1) is the operative framing going forward.

---

## 5. V_quad row-membership note

The $\deg_a = 0$ row at $d = 2$ has $A_{\rm naive} = 4$, matching
V_quad's empirical $A = 4$ (PCF-1 v1.3 §6 Theorem 5; V_quad declared at
`algebraic_independence_audit.py` L37-40 with `VQUAD_ALPHA = [1]`,
i.e., $a(n) \equiv 1$, $\deg_a = 0$ — see LANE-2 V5 substrate at
`independent_substrate_verification.md` L161-179, SHA `56063BF7BA8AD6A0…`).
Under the four-row enumeration of §2.3, V_quad is therefore the
$\deg_a = 0$ specimen at $d = 2$ as a matter of row-membership.

The framing here is **row-membership re-attribution under extended
enumeration**: under the original three-row enumeration ($\deg_a \in
\{1, 2, 3\}$ at $d = 2$), V_quad's $A = 4$ sits above the maximum row
entry ($A = 3$ at the $\alpha$-direction, $\deg_a = 1$); under the
four-row extension, V_quad's $A = 4$ aligns with the new $(1, b)$
corner row at $\deg_a = 0$. This is a row-membership observation that
follows from P1's source-code finding ($a_n \equiv 1$ in V_quad) and
from V6's $A_{\rm naive} = 2d$ at $\deg_a = 0$ derivation.

This row-membership re-attribution is the substrate for two downstream
items in the LANE-2 cascade:

- LANE-2 Item 2 sub-task 3-D (PCF-1 v1.3 V_quad row reframing;
  `lane2_six_item_verdict.md` Item 2 verdict; anticipated as relay 066).
- LANE-2 Item 3 follow-up note for `bt_baseline_note` v1.0 §4.2
  (anticipated as relay 067 in the cascade; verdict
  `LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE`).

The present supplement (064) is scoped to the Phase A table extension
only and does not author the §4.2 follow-up note. Per LANE-2 Item 3,
the v1.0 §4.2 attribution of V_quad's $A = 4$ to mechanism (i') remains
the canonical text of v1.0; the follow-up note (separate task) is the
artefact that records the row-membership re-attribution alongside v1.0,
without modifying v1.0's source.

---

## 6. AEAL claims log

All claims in this supplement are file-system facts (SHA + line range)
or verbatim transcriptions of LANE-2 substrate. Six AEAL entries are
written to `claims.jsonl` in the same deposit folder; see that file for
the structured list. Briefly:

- **064-C1** — `bt_baseline_note.tex` v1.0 SHA + bytes (P3 gate).
- **064-C2** — V6 substrate file SHA + cited line range (L210-308).
- **064-C3** — P2 substrate file SHA + cited line ranges (L77-87, L121-126,
  L116-138).
- **064-C4** — Extended 12-row WZ-balance table (data, rendered in §2.3).
- **064-C5** — Quoted formula $A_{\rm naive} = 2d$ at $\deg_a = 0$
  (verbatim from V6, L274-282).
- **064-C6** — Row-membership entries $A = 4$ at $d=2$ / $A = 6$ at $d=3$ /
  $A = 8$ at $d=4$ (data; the new rows of the extended table).
- **064-C7** (optional) — forbidden-verb scan PASS (zero hits in
  conjectural context); see `forbidden_verb_scan.md`.

---

## 7. Bibliography / SHA anchors

| Substrate | Path (relative to repo root) | SHA-256 (full) | Bytes | Lines cited |
|-----------|------------------------------|----------------|-------|-------------|
| `bt_baseline_note.tex` v1.0 (canonical, unmodified) | `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex` | `6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B` | 38023 | (referenced; not modified) |
| LANE-2 V6 substrate | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_substrate_verification.md` | `56063BF7BA8AD6A01A89FA30A3C61FCE…` (full hash in `substrate_anchor_shas.md`) | 15695 | L210-308 |
| LANE-2 P2 substrate | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_depth_probe.md` | `20764101FCDEA73A57EE92B80C97B3EA…` | 16698 | L77-87, L116-138 |
| LANE-2 anchor SHAs index | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/anchor_shas.md` | `9C44526E23C2FBFC5C63EE51C34D4F3D…` | 2170 | (whole file) |
| LANE-2 six-item verdict | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_six_item_verdict.md` | `541663C69A5CE86B4F5D3799B04A0334…` | 18890 | Item 2 sub-task 3-A |
| LANE-2 meta-verdict | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_meta_verdict.md` | `2F7FE03B519CEEEF47948871C889DDAF…` | 10606 | L79-99 (R3) |
| LANE-2 adoption audit | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/adoption_audit.md` | `4160A88F03FA75F9F695B459FF8492F6…` | 8027 | (whole file) |
| LANE-2 deposit commit | bridge `dee3c01` | (git commit hash) | — | T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4 ACCEPT_WITH_REVISIONS |
| Original Phase A summary | `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_a_summary.md` | (cited via P2 L77-87) | — | L34-44 |
| `algebraic_independence_audit.py` (V_quad declaration) | `algebraic_independence_audit.py` | (cited via V5) | — | L37-40 |

Full SHA-256 hashes for all LANE-2 files appear in
`substrate_anchor_shas.md` (companion deliverable in this deposit).

---

*End of `phase_a_supplementary_deg_a_zero.md`. The Phase A WZ-balance
extension by one row ($\deg_a = 0$) is the LANE-2 R3 required revision,
implemented as a write-up only per LANE-2 Item 2 sub-task 3-A
authorisation. The `bt_baseline_note` v1.0 source is unmodified.*
