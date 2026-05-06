# PCF-1 v1.3 §6 V_quad row reframing — forward substrate

**Task ID:** `PCF1-V13-V_QUAD-ROW-REFRAMING-066`
**Date:** 2026-05-07 (W20)
**Authoring tier:** T3 mechanical write-up (substrate already produced
in LANE-2 deposit `dee3c01` and 064 supplement at bridge `6a150b6`;
no fresh symbolic re-derivation in this document).
**Authorisation:** LANE-2 Item 1 verdict
`RATIFY_WITH_NARROW_REVISION` (HIGH) at
`siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_six_item_verdict.md`
L15-87, with R1 scope-expansion meta-verdict at
`lane2_meta_verdict.md` L32-55 (PCF-1 leg of R1 implementation).
**Cascade context:** Wave 2 of the post-LANE-2 cascade. PCF-2 leg of
R1 was implemented at the source-audit layer by relay 065
(`PCF2-CF_VALUE-AUDIT-9IMPLS-065`, bridge `6a150b6`). The PCF-1 leg
implemented here is a forward-substrate write-up; the actual PCF-1
v1.3 source `.tex` is **NOT MODIFIED** by this document.

---

## 1. Scope and relationship to PCF-1 v1.3 §6

This write-up is authorised under LANE-2 Item 1 R1 (PCF-1 leg) and
implements the row-membership re-attribution called for by the LANE-2
meta-verdict R1 wording (`lane2_meta_verdict.md` L42-46):

> "AND the PCF-1 v1.3 §6 Theorem 5 V_quad upper-branch row (per
> `algebraic_independence_audit.py` L37-40, V_quad uses $a(n) = 1$ at
> $d = 2$, yielding $A_{\rm naive} = 2d = 4$ via the WZ normal case
> deg_a = 0 row, NOT via the borderline mechanism (i') as currently
> attributed in `bt_baseline_note.tex` v1.0 §4.2 L481-487)."

The write-up has the following deliberate scope boundaries:

- **No `.tex` source edit.** The PCF-1 v1.3 `.tex` source
  (`p12_pcf1_main.tex` at SHA `E83BB377F297DBF0..`, 46349 B, 925 lines)
  remains canonical and is unmodified by this document. The Zenodo
  v1.3 deposit (concept DOI `10.5281/zenodo.19937196`; PDF SHA
  `63420DBF4ABB7124..`, 392886 B, 16 pp) is unmodified.
- **No `bt_baseline_note` v1.0 edit.** The `bt_baseline_note.tex` v1.0
  source (SHA `6746692C517DC2523847..`, 38023 B) remains canonical per
  LANE-2 Item 3 verdict
  `LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE`
  (`lane2_six_item_verdict.md` Item 3 L165-228). The §4.2
  mechanism-(i') open-content closure jurisdiction belongs to the
  follow-up note (anticipated as relay 067 in the cascade), not 066.
- **No v1.4 amendment fire.** A future PCF-1 v1.4 §6 row-table
  amendment may render this row-membership reading explicit at the
  source-prose level; this write-up provides only a forward pointer
  (§6 below). The actual amendment is gated on G12
  `PCF1-V13-RECONCILE` (separate operator-gated jurisdiction).
- **No fresh symbolic derivation.** All mathematical content cited
  here (the WZ Newton-polygon balance for deg_a = 0 yielding
  $A_{\rm naive} = 2d$, the row-membership of V_quad at deg_a = 0)
  is verbatim-quoted from LANE-2 V5 + V6 + 064 supplement substrate.

Within these boundaries, the write-up records the row-membership
re-attribution of V_quad's $A = 4$ entry under the extended four-row
Phase A enumeration of `phase_a_supplementary_deg_a_zero.md` (064;
SHA `80E28568FF142B1A..`, 16792 B). The framing throughout is
  **row-membership re-attribution under extended enumeration**;
  mechanism (i') open-content closure jurisdiction belongs to relay
  067 and is not addressed here.
## 2. PCF-1 v1.3 §6 Theorem 5 row table (verbatim quote)

**Substrate path:** P5 substrate (a) — canonical 16pp PCF-1 v1.3 source
at `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`,
SHA-256 `E83BB377F297DBF0837FACBA257F227DF4579E6A3518C139E3146F17174BE301`,
46349 B, 925 lines. The corresponding 16pp PDF
(`p12_pcf1_main.pdf` SHA `63420DBF4ABB7124..`, 392886 B; deposited
to Zenodo concept DOI `10.5281/zenodo.19937196`) renders the same
content at page 11 of the published 16pp PDF.

**Project shorthand vs section number.** The LANE-2 R1 wording
(`lane2_meta_verdict.md` L42), the 064 supplement
(`phase_a_supplementary_deg_a_zero.md` §5 L222), and relay 066
prompt body all reference this as "PCF-1 v1.3 §6 Theorem 5 row
table". In the canonical 16pp source, the WKB theorem and its row
table reside at `\section{The WKB Exponent Identity}\label{sec:wkb}`
(L516); the section index inside the .tex file's
`\section{...}` ordering is **§5** (not §6). The "§6" label is
a project shorthand inherited verbatim from the LANE-2 R1 wording
and 064 supplement. SHA + line-range anchoring below resolves the
shorthand precisely; see Discrepancy log D1.

### 2.1 Theorem statement (`thm:wkb`, L528-548)

Verbatim from `p12_pcf1_main.tex` L528-548 (see SHA above):

> ```
> \begin{theorem}[WKB exponent identity for degree-2 PCFs]\label{thm:wkb}
> Let $a_{n}=c_{a}n+\delta$ and
> $b_{n}=c_{b}n^{2}+\beta n+\gamma$ be the recurrence coefficients of
> a degree-two PCF in the scope of this paper, with leading
> coefficients $c_{a}\in\mathbb{Z}\setminus\{0\}$ and
> $c_{b}\in\mathbb{Z}_{>0}$. Then the Wallis convergent error
> $\delta_{n}=p_{n}/q_{n}-L$ admits the formal asymptotic expansion
> \begin{equation}\label{eq:wkb}
> \log|\delta_{n}| \;=\; -A\,n\log n \;+\; \alpha\,n
>   \;-\; \beta_{w}\log n \;+\; \gamma_{w}
>   \;+\; \sum_{k\ge 1}\frac{h_{k}}{n^{k}},
> \end{equation}
> with leading exponents
> \begin{equation}\label{eq:wkb-alpha}
> A\in\{3,4\},\qquad
> \alpha \;=\; A \;-\; 2\log c_{b} \;+\; \log|c_{a}|,
> \end{equation}
> where $A=4$ for $V_{\mathrm{quad}}$ and $A=3$ for the five
> quadratic-limit families QL01, QL02, QL06, QL15, QL26.
> \end{theorem}
> ```

The theorem is rendered under the amsart counter scheme
`\newtheorem{theorem}{Theorem}[section]` /
`\newtheorem{conjecture}[theorem]{Conjecture}` (preamble L19-20),
which resets the shared theorem/conjecture counter at each new
section and renders `\ref{thm:wkb}` as `Theorem~5.1` in the §5
namespace. In project shorthand (R1 wording, 064 supplement, this
relay prompt body) the same theorem is referred to as "Theorem 5";
both labels resolve to the same SHA-anchored statement.

### 2.2 Row table (`tab:wkb-exponents`, L566-577)

Verbatim from `p12_pcf1_main.tex` L566-577:

> ```
> \begin{tabular}{lccccc}
> \toprule
> Family & $\Delta$ & $A$ & $\alpha_{\mathrm{pred}}=A-2\log c_{b}+\log|c_{a}|$ & $\alpha_{\mathrm{obs}}$ & match digits \\
> \midrule
> $V_{\mathrm{quad}}$ & $-11$ & $4$ & $4-2\log 3 = 1.80277542266378$ & $1.8027754226638$ & $13$ \\
> QL01 & $-3$ & $3$ & $3 = 3.0$ & $3.0$ & exact \\
> QL02 & $-4$ & $3$ & $3 + \log 2 = 3.69314718055994$ & $3.6931471805599$ & $13$ \\
> QL06 & $-7$ & $3$ & $3-2\log 2 = 1.61370563888011$ & $1.6137056388801$ & $14$ \\
> QL15 & $-20$ & $3$ & $3-2\log 3 = 0.802775422663781$ & $0.80277542266378$ & $15$ \\
> QL26 & $-28$ & $3$ & $3-2\log 4 + \log 3 = 1.32602356642833$ & $1.3260235664283$ & $13$ \\
> \bottomrule
> \end{tabular}
> ```

Rendered (the **V_quad row** is bolded for visual emphasis only;
the source has no bold marker):

| Family | $\Delta$ | $A$ | $\alpha_{\rm pred} = A - 2\log c_b + \log|c_a|$ | $\alpha_{\rm obs}$ | match digits |
|--------|----------|-----|-------------------------------------------------|---------------------|--------------|
| **$V_{\rm quad}$** | **$-11$** | **$4$** | **$4 - 2\log 3 = 1.80277542266378$** | **$1.8027754226638$** | **$13$** |
| QL01 | $-3$ | $3$ | $3 = 3.0$ | $3.0$ | exact |
| QL02 | $-4$ | $3$ | $3 + \log 2 = 3.69314718055994$ | $3.6931471805599$ | $13$ |
| QL06 | $-7$ | $3$ | $3 - 2\log 2 = 1.61370563888011$ | $1.6137056388801$ | $14$ |
| QL15 | $-20$ | $3$ | $3 - 2\log 3 = 0.802775422663781$ | $0.80277542266378$ | $15$ |
| QL26 | $-28$ | $3$ | $3 - 2\log 4 + \log 3 = 1.32602356642833$ | $1.3260235664283$ | $13$ |

Caption (verbatim from `p12_pcf1_main.tex` L578-583):

> "WKB trans-series exponents for the six $\Delta<0$ degree-2
> PCFs. $\alpha_{\mathrm{pred}}$ is the closed-form prediction
> of~\eqref{eq:wkb-alpha}; $\alpha_{\mathrm{obs}}$ is extracted by
> least-squares fit to $\log|\delta_{n}|$ on $n\in[15,120]$ at
> $K=12$, $\mathrm{dps}=2200$. All six families match to
> $\ge 13$ digits."

### 2.3 Row entry of interest

The row entry at the head of the table (V_quad row): family
$V_{\mathrm{quad}}$ at $\Delta = -11$ has $A = 4$. The other five
rows (QL01, QL02, QL06, QL15, QL26) all have $A = 3$. The dichotomy
$A \in \{3, 4\}$ stated in the theorem corresponds row-by-row to the
table: the QL01--QL26 lower branch (five rows at $A = 3$) and the
V_quad upper branch (one row at $A = 4$).

The remainder of this write-up identifies the V_quad $A = 4$ row
entry as a deg_a = 0 row member at $d = 2$ under the extended
four-row Phase A enumeration of 064 supplement §2.3.

---

## 3. V_quad coefficient-array identity (V5 verbatim)

**Substrate:** LANE-2 V5
(`independent_substrate_verification.md` L161-179, file SHA-256
`56063BF7BA8AD6A01A89FA30A3C61FCE68F4AAB0BA0DC7C8E561A81188D7B1F5`,
15695 B). V5 quotes `algebraic_independence_audit.py` L37-40
verbatim:

> ```python
> # V_quad: GCF with a(n)=1, b(n)=3n²+n+1, backward mode
> # CF = b(0) + 1/(b(1) + 1/(b(2) + ...)) = 1 + 1/(5 + 1/(15 + ...))
> VQUAD_ALPHA = [1]          # a(n) = 1 for all n
> VQUAD_BETA = [1, 1, 3]    # b(n) = 3n²+n+1
> ```

V5 reading (`independent_substrate_verification.md` L181-198,
verbatim block):

> "- $a(n) = 1$ for all $n$ (deg_a = 0).
> - $b(n) = 3n^2 + n + 1$ (deg_b = 2).
> - 'GCF' = generalised continued fraction; backward-mode evaluator.
>
> **Independent finding (V5):** V_quad — the central transcendental
> candidate of PCF-1 v1.3 — uses $a_n \equiv 1$, i.e., **deg_a = 0**.
> This CONTRADICTS the PCF-1 v1.3 d=2 standard stratum (V4), which
> imposes $\delta \ne 0$ (deg_a = 1)."

The data claim for the present write-up: at the source-code declaration
level, V_quad's $a$-array is `VQUAD_ALPHA = [1]`, i.e., $a_n = 1$ for
all $n$, hence deg_a = 0 (a constant array of length 1 representing
the constant polynomial $1$). This is an observational finding about
file content, not a prediction; the V5 substrate identifies V_quad's
deg_a as 0 directly from the audit script source.

---

## 4. Extended four-row Phase A WZ-balance table (064 + V6)

**Substrate:** 064 supplement
(`siarc-relay-bridge/sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/phase_a_supplementary_deg_a_zero.md`,
SHA-256 `80E28568FF142B1A81C7C443368349A07A8235CE122D6C6140F88AA0D0706097`,
16792 B). The extended enumeration appears at §2.3 of 064 (the
combined twelve-row enumeration sorted by $d$, then deg_a ascending),
which itself draws on LANE-2 V6
(`independent_substrate_verification.md` L210-308, SHA
`56063BF7BA8AD6A0..`).

### 4.1 Twelve-row enumeration (064 §2.3 verbatim)

Reproduced verbatim from
`phase_a_supplementary_deg_a_zero.md` L102-118 (064 §2.3):

| $d$ | Convention          | deg a | deg b | $\mu_{\rm dom}$ | $\mu_{\rm sub}$ | $A_{\rm naive}$ |
|-----|---------------------|-------|-------|-----------------|-----------------|-----------------|
| 2   | (1, b) PCF-2 corner | 0     | 2     | 2               | $-2$            | **4**           |
| 2   | $\alpha$-direction  | 1     | 2     | 2               | $-1$            | 3               |
| 2   | symmetric           | 2     | 2     | 2               |  0              | 2               |
| 2   | $\delta$-direction  | 3     | 2     | 2               |  1              | 1               |
| 3   | (1, b) PCF-2 corner | 0     | 3     | 3               | $-3$            | **6**           |
| 3   | $\alpha$-direction  | 2     | 3     | 3               | $-1$            | 4               |
| 3   | symmetric           | 3     | 3     | 3               |  0              | 3               |
| 3   | $\delta$-direction  | 4     | 3     | 3               |  1              | 2               |
| 4   | (1, b) PCF-2 corner | 0     | 4     | 4               | $-4$            | **8**           |
| 4   | $\alpha$-direction  | 3     | 4     | 4               | $-1$            | 5               |
| 4   | symmetric           | 4     | 4     | 4               |  0              | 4               |
| 4   | $\delta$-direction  | 5     | 4     | 4               |  1              | 3               |

(Bold rows are the new $\deg_a = 0$ rows introduced by 064 supplement;
the other nine rows are reproduced verbatim from
`phase_a_summary.md` L34-44 via LANE-2 P2 substrate at
`independent_depth_probe.md` L77-87, file SHA `20764101FCDEA73A..`.)

### 4.2 Row at $d = 2$, deg_a = 0 (V6 derivation, verbatim)

The first row of the extended enumeration ($d = 2$, deg_a = 0) carries
$A_{\rm naive} = 4$. The derivation appears verbatim in 064 §3 (which
in turn quotes LANE-2 V6
`independent_substrate_verification.md` §V6 Step 4 L268-282):

> "$A_{\rm naive} = \mu_{\rm dom} - \mu_{\rm sub} = d - (-d) = 2d$
> (when deg_a = 0). … General formula:
> $A_{\rm naive} = 2d - d_a$." (V6, L274-282)

For $d = 2$, deg_a = 0: $A_{\rm naive} = 2 \cdot 2 - 0 = 4$. The
sign of the recessive root in the relevant computation is recorded
verbatim in V6 Step 3 (L260-266):

> "For the more general Wallis case $a_n \sim c_a\,n^{d_a}$
> (deg_a = $d_a > 0$), the analogous derivation gives
> $r_+ \approx -b_n/a_n$ to leading order, hence
> $p_n^{\rm rec}/p_{n-1}^{\rm rec} \approx -a_n/b_n$, and
> $\gamma_{\rm sub} = -c_a/c_b \cdot (\text{Stirling cancellation factor})$.
> In the deg_a = 0 corner ($c_a = 1$, $d_a = 0$), this reduces to
> $\gamma_{\rm sub} = -1/c_b \cdot e^{d}$. The SIGN $-c_a/c_b$ at the
> leading 'geometric ratio' level is the robust observation; the
> Stirling-factor magnitude depends on convention." (V6, L260-266)

The above two blocks are quoted as substrate citations; the present
write-up does not re-derive them.

---

## 5. V_quad row-membership re-attribution

**Combining §3 + §4.** V_quad's coefficient declaration
`VQUAD_ALPHA = [1]` (V5 verbatim) identifies V_quad as a deg_a = 0
specimen at $d = 2$. The extended four-row Phase A enumeration of
064 §2.3 records $A_{\rm naive} = 4 = 2d$ at the $(d = 2,\ \deg_a = 0)$
row. The V_quad entry $A = 4$ in PCF-1 v1.3 §6 Theorem 5 row table
(`p12_pcf1_main.tex` L566-577 verbatim, §2.2 above) is therefore
row-equivalent to the deg_a = 0 row member at $d = 2$ in the extended
enumeration.

Under the **original three-row** Phase A enumeration of
`bt_baseline_note.tex` v1.0 (deg_a $\in \{d - 1, d, d + 1\}$ at each
$d$), the $d = 2$ rows give $A_{\rm naive} \in \{1, 2, 3\}$, and
V_quad's empirical $A = 4$ sits above the maximum row entry $A = 3$
(at $\alpha$-direction, deg_a = 1). Under this narrower enumeration,
V_quad's $A = 4$ is consistent with the borderline-locus mechanism
(i') framing of `bt_baseline_note.tex` v1.0 §4.2 L481-487 (the
"upper branch" not recovered by the band $\{1, 2, 3\}$).

Under the **extended four-row** enumeration of 064 supplement §2.3
(deg_a $\in \{0, d - 1, d, d + 1\}$ at each $d$), the $d = 2$ rows
give $A_{\rm naive} \in \{1, 2, 3, 4\}$. V_quad's empirical $A = 4$
aligns with the new $(1, b)$ corner row at deg_a = 0. Under this
enumeration, V_quad is row-equivalent to the deg_a = 0 row member at
$d = 2$ as a matter of row-membership.

**Re-attribution statement.** PCF-1 v1.3 §6 Theorem 5 row table
entry "$V_{\rm quad}: A = 4$" is row-equivalent to the deg_a = 0
row member at $d = 2$ under the extended four-row enumeration. The
row entry is consistent with Balance III at the deg_a = 0 corner
under bt_baseline_note v1.0's Phase A framework, NOT with the
borderline-locus mechanism (i') as 064 supplement §5 + LANE-2 P3
substrate (`independent_depth_probe.md` L195-198) independently
identify.

The framing here is **row-membership re-attribution under the
extended four-row enumeration** of 064 §2.3. The mechanism (i')
open-content closure jurisdiction belongs to the follow-up note
(anticipated relay 067; LANE-2 Item 3 verdict
`LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE` at
`lane2_six_item_verdict.md` Item 3 L165-228); it is reserved for
that follow-up note and not addressed here.

For audit purposes, the supporting data points are:

| substrate | content | citation |
|-----------|---------|----------|
| V_quad declaration | `VQUAD_ALPHA = [1]` (deg_a = 0) | V5 L161-179 |
| V_quad table entry | $A = 4$ in row table at L568 | `p12_pcf1_main.tex` L566-577 |
| Extended row | $A_{\rm naive} = 4$ at $(d=2, \deg_a=0)$ | 064 §2.3 L102-118 |
| WZ derivation | $A_{\rm naive} = 2d - d_a$ general formula | V6 L268-282 |
| Mechanism (i') attribution | "V_quad upper branch consistent with borderline-locus mechanism (i')" | `bt_baseline_note.tex` v1.0 L481-487 |
| Mechanism (i') substrate finding | "§4.2's interpretation … is substrate-level WRONG" | LANE-2 P3 L195-198 |

The first four rows are the row-membership substrate; the last two
rows are referenced for cross-context but are reserved for relay 067
treatment.

---

## 6. Forward pointer to PCF-1 v1.4 §6 amendment (non-firing)

A future PCF-1 v1.4 §6 row-table amendment may rewrite the V_quad
row entry's footnote / accompanying commentary in the row-table
caption to render this row-membership reading explicit at the
source-prose level. Such an amendment would, for example:

- annotate the V_quad row with a brief footnote citing 064 §2.3 +
  V5 + V6 substrate;
- expand the row-table caption text to acknowledge the row-membership
  reading in addition to the WKB-exponent reading;
- or insert a short paragraph before/after `tab:wkb-exponents`
  recording the deg_a = 0 row-membership of V_quad under the
  extended four-row enumeration.

The selection among these renderings is reserved for G12
`PCF1-V13-RECONCILE` jurisdiction. **G12 reconciliation is
operator-gated** (separate task; jurisdiction includes the choice
between bumping to a PCF-1 v1.4 deposit or recovering v1.3 16pp
source from git/Zenodo). The present write-up provides forward
substrate only and does not propose, draft, or fire a v1.4
amendment; it provides a forward pointer.

The forward-substrate cites in this write-up are SHA-anchored
independently of the G12 reconcile path, so the substrate-level
re-attribution is portable across any G12 outcome (whether v1.4
dispatch, v1.3 source recovery, or any other path the operator
chooses).

---

## 7. AEAL claims log

Six AEAL entries are written to `claims.jsonl` in the same deposit
folder; see that file for the structured list. Briefly:

- **066-C1** — `bt_baseline_note.tex` v1.0 SHA + bytes (canonical
  unmodified; P4 gate).
- **066-C2** — 064 supplement SHA + bytes (extended four-row table
  substrate; P3 gate).
- **066-C3** — V5 substrate quotation (`VQUAD_ALPHA = [1]` verbatim
  from `algebraic_independence_audit.py` L37-40).
- **066-C4** — V6 substrate quotation (Balance III deg_a = 0
  derivation: $A_{\rm naive} = 2d$ at deg_a = 0 verbatim from V6
  L268-282).
- **066-C5** — PCF-1 v1.3 §6 Theorem 5 row table verbatim quote
  (substrate `p12_pcf1_main.tex` L566-577 + SHA anchor `E83BB377..`,
  46349 B).
- **066-C6** — V_quad row-membership re-attribution (data claim
  combining C3 + C4 + C5: V_quad's $A = 4$ row entry at $d = 2$ is
  row-equivalent to the deg_a = 0 row member at $d = 2$ with
  $A = 4 = 2d$ under the extended four-row enumeration).
- **066-C7** (optional) — forbidden-verb scan PASS (zero
  prediction-context hits in the draft markdown); see
  `forbidden_verb_scan.md`.
- **066-C8** (optional) — scope-discipline scan PASS (zero hits in
  authorial prose for the discipline-pattern enumerated in relay 066
  STEP 6); see `forbidden_verb_scan.md`.

---

## 8. Bibliography / SHA anchors

| # | Substrate | Path (relative to repo root) | SHA-256 (full) | Bytes | Lines cited |
|---|-----------|------------------------------|----------------|-------|-------------|
| B1 | PCF-1 v1.3 §6 Theorem 5 row table (canonical 16pp source) | `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex` | `E83BB377F297DBF0837FACBA257F227DF4579E6A3518C139E3146F17174BE301` | 46349 | L516 (sec:wkb), L528-548 (thm:wkb), L566-577 (tab:wkb-exponents), L578-583 (caption) |
| B2 | PCF-1 v1.3 PDF (16pp Zenodo deposit) | `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.pdf` | `63420DBF4ABB7124672F522C37FC04EBDB3F6694AC39959456B2890D9788FF5E` | 392886 | p. 11 (row table render); concept DOI `10.5281/zenodo.19937196` |
| B3 | 064 supplement (extended four-row WZ-balance table) | `siarc-relay-bridge/sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/phase_a_supplementary_deg_a_zero.md` | `80E28568FF142B1A81C7C443368349A07A8235CE122D6C6140F88AA0D0706097` | 16792 | §2.3 L102-118; §3 L222-282; §5 L222-251 |
| B4 | LANE-2 V5 substrate (V_quad declaration) | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_substrate_verification.md` | `56063BF7BA8AD6A01A89FA30A3C61FCE68F4AAB0BA0DC7C8E561A81188D7B1F5` | 15695 | L161-198 (V5 row); L210-308 (V6 row) |
| B5 | LANE-2 V6 substrate (Balance III deg_a = 0 derivation) | (same file as B4) | (same SHA as B4) | 15695 | L210-308 (V6 derivation); L240-244 (μ_dom); L249-258 (Balance III); L260-266 (sign); L274-282 (A_naive = 2d) |
| B6 | LANE-2 P3 substrate (bt_baseline_note v1.0 §4.2 mechanism-(i') finding) | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/independent_depth_probe.md` | `20764101FCDEA73A57EE92B80C97B3EAB87C579CEEBED611FF9D2E6087B3885D` | 16698 | L152-218 (P3 finding); L195-198 (substrate-level wrong wording); L77-87 (P2 phase_a_summary L34-44 transcription) |
| B7 | LANE-2 anchor SHAs index | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/anchor_shas.md` | `9C44526E23C2FBFC5C63EE51C34D4F3DA8FFC658B254F6E66A3108895B2B2668` | 2170 | (whole file) |
| B8 | LANE-2 six-item verdict | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_six_item_verdict.md` | `541663C69A5CE86B4F5D3799B04A0334C4A27E202DD9B3E2B80AFE16EE62B917` | 18890 | Item 1 L15-87 (RATIFY_WITH_NARROW_REVISION); Item 3 L165-228 |
| B9 | LANE-2 meta-verdict | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/lane2_meta_verdict.md` | `2F7FE03B519CEEEF47948871C889DDAF55B623CF0831F8643691EF2DDAE8391C` | 10606 | L32-55 (R1 PCF-1 leg) |
| B10 | LANE-2 adoption audit | `siarc-relay-bridge/sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/adoption_audit.md` | `4160A88F03FA75F9F695B459FF8492F6E2E63CC603C3EFB8A9BEAB7527368B15` | 8027 | (whole file) |
| B11 | `bt_baseline_note.tex` v1.0 (canonical, unmodified) | `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex` | `6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B` | 38023 | L457-487 (§4.2 d=2; mechanism (i') attribution) |
| B12 | LANE-2 deposit commit | bridge `dee3c01` | (git commit hash) | — | T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4 ACCEPT_WITH_REVISIONS |
| B13 | 064 deposit commit | bridge `6a150b6` | (git commit hash) | — | PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064 (064 + 065 shipped under same hash) |

Full SHA-256 hashes for the seven LANE-2 substrate files appear in
`substrate_anchor_shas.md` (companion deliverable in this deposit).

---

*End of `pcf1_v13_v_quad_row_reframing.md`. The PCF-1 v1.3 §6
Theorem 5 V_quad row entry (A = 4 at d = 2) is row-equivalent to
the deg_a = 0 row member at d = 2 under the extended four-row Phase
A enumeration (064 §2.3) by row-membership re-attribution. The
PCF-1 v1.3 .tex source and the bt_baseline_note v1.0 .tex source
remain canonical and are unmodified by this write-up. A future
PCF-1 v1.4 §6 row-table amendment is forward-pointed in §6 above
and is reserved for G12 PCF1-V13-RECONCILE jurisdiction; it is not
fired here.*
