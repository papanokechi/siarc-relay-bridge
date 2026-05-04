# Handoff — PCF2-V13-AFIT-DEFINITION-READBACK

**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7)
**Session duration:** ~45 minutes
**Status:** COMPLETE
**Verdict:** `UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL`

---

## What was accomplished

Phase 0–E of the §2 ladder were executed as a paper-readback
(no mpmath; no symbolic re-derivation). The PCF-2 v1.3 PDF was
anchored at `tex/submitted/pcf2_program_statement.pdf`
(SHA-256 `87B845A8…D81D263F`, 22 pp, MiKTeX pdfTeX-1.40.28
build 2026-05-02 07:52:39 +09:00); the empirical $A_\text{fit}$
definition was extracted verbatim from §5
(Conjecture B4, eq. (B4)) of the workspace `tex` source
(`pcf2_program_statement.tex` SHA-256 `82FE2315…61F2C8541`,
75 098 B); and the convention was reconciled against the T1
Phase 2 (`T1-BIRKHOFF-PHASE2-LIFT-LOWER`, bridge `37c939f`)
naive Wimp-Zeilberger baseline. The conventions match: PCF-2
v1.3 measures $A$ as the (negative) coefficient of $n\log n$
in the asymptotic expansion of $\log|\delta_n|$ where
$\delta_n = p_n/q_n - L$, which is structurally
$\mu_\text{dom} - \mu_\text{sub}$ — the same quantity Phase A
computes from Newton-polygon balance.

## Key numerical findings

- **PCF-2 v1.3 PDF anchor**: 22 pp, 558 153 B,
  SHA-256 `87B845A8E382F3C124906ACE0C1A6763CE54BD14C5F9593BBADC77BDD81D263F`
  (matches V13-RELEASE 2026-05-02 build per
  `sessions/2026-05-02/PCF2-V13-RELEASE/build.log` line 300
  and `claims.jsonl` entry V13-A3).
- **PCF-2 v1.3 .tex anchor**: 75 098 B, SHA-256
  `82FE2315CFDA2047249D4978D7AE487C21D9BE16A35F15827CE132561F2C8541`
  at `tex/submitted/pcf2_program_statement.tex`.
- **A_fit definition (eq. (B4))**:
  $\log|\delta_n| = -A\,n\log n + \alpha\,n - \beta\,\log n
  + \gamma + o(1)$, $n\to\infty$, with $\delta_n =
  p_n/q_n - L$ (`tex/submitted/pcf2_program_statement.tex`
  L460–L463).
- **Sharp identification**: $A = 2d$ (boxed, `pcf2_program_statement.tex` L465).
- **Empirical anchors**: cubic mean $A_\text{fit}=5.978$,
  $\sigma=0.026$ at $d=3$ (50/50 families); quartic mean
  $A_\text{fit}=7.954$, $\sigma=0.0037$ at $d=4$ (60/60
  families) (`pcf2_program_statement.tex` L470–L472).

## Verbatim quotes (Phase B.2; ≤ 30 words each)

**Quote 1** — definition of $\delta_n$ and the form of (B4)
(`pcf2_program_statement.tex` L459–L466):

> "the convergent residual $\delta_{n}=p_{n}/q_{n}-L$ has
> leading WKB asymptotic … $\log|\delta_{n}| = -A\,n\log n
> + \alpha n - \beta \log n + \gamma + o(1)$ ($n\to\infty$),
> with the sharp identification $A = 2d$"

(28 words excluding inline LaTeX; the equation is
labelled `eq:B4`, the conjecture `conj:B4`).

**Quote 2** — empirical $A_\text{fit}$ harvest at
$d \in \{3,4\}$ (`pcf2_program_statement.tex` L470–L473):

> "empirical, $110/110$; cubic mean $A_{\mathrm{fit}}=5.978$,
> $\sigma=0.026$; quartic mean $A_{\mathrm{fit}}=7.954$,
> $\sigma=0.0037$ … In particular, $A=6$ for every cubic
> and $A=8$ for every quartic PCF in scope."

(29 words; surfaces the 2d identification as observed exponent).

**Quote 3** — d=2 base case relation
(`pcf2_program_statement.tex` L480–L484):

> "PCF-1 v1.3 Theorem 5 (WKB exponent identity, degree two)
> proves the form (B4) at $d=2$ with $A\in\{3,4\}$ split by
> $\mathrm{sgn}(\Delta_{2})$"

(22 words; locates PCF-1 Theorem 5 as same-form anchor at $d=2$).

**Quote 4** — fit precision and window for the Q1 (quartic)
catalogue (`pcf2_program_statement.tex` L644 + paragraph
context at L640–L645):

> "Session~Q1 (quartic, $d=4$) … At $\mathrm{dps}=2000$, fit
> window $N\in[200,800]$"

(brief factual quote; locates the Q1 high-precision regime
under which $A_\text{fit}=2d$ is reported).

## Classification per Phase B.3

The PCF-2 v1.3 $A_\text{fit}$ corresponds to choice **(a)**:
the $n\log n$ coefficient in the asymptotic of $\log|\delta_n|$,
which equals $\mu_\text{dom} - \mu_\text{sub}$ when $\delta_n$
is read as the subdominant-over-dominant ratio of the recurrence
solution pair. This is the SAME quantity Phase A
(`T1-BIRKHOFF-PHASE2-LIFT-LOWER` Phase A) computes.

Justification (cross-check via PCF-1 v1.3 Theorem 5 anchor):
Phase A α-direction at $d=2$ predicts $A_\text{naive}=3$,
which matches PCF-1 v1.3 Theorem 5's lower branch QL01–QL26
($A=3$, $\Delta_2 < 0$). Since PCF-1 v1.3 Theorem 5 uses the
same equation form (B4) (Quote 3 above), and Phase A
α-direction at $d=2$ recovers one of its branches, the
conventions agree at $d=2$ and propagate uniformly to $d \ge 3$.

## Phase C reconciliation

Phase A naive baseline (T1 Phase 2 handoff
`sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/
phase_a_summary.md` table):

| d | α-direction | symmetric | δ-direction | A_fit (PCF-2 v1.3) |
|---|------------:|----------:|------------:|-------------------:|
| 2 | 3 | 2 | 1 | {3, 4} (PCF-1 Thm 5) |
| 3 | 4 | 3 | 2 | 6 (= 2d) |
| 4 | 5 | 4 | 3 | 8 (= 2d) |

The drift between $A_\text{naive}$ (≤ d+1 in α-direction) and
$A_\text{fit} = 2d$ is **NOT** a definition mismatch —
**it is the structural Phase 2 finding** that the SIARC PCF
stratum sits at the borderline case `deg_a = 2 deg_b` of
Wimp-Zeilberger 1985, where the standard normal-case ansatz
$y(n) \sim \Gamma(n)^\mu \gamma^n n^\rho$ requires modification
(P2.1 + P2.2 + P2.3 of the gap proposition). G24 resolution
candidate (ii) (definition mismatch) does **NOT** explain the
gap; G23 resolution candidate (i) (borderline ansatz) is the
remaining live route, to be closed by T1 Phase 3.

## Page-count check (Phase A.1 third bullet)

The §1 prompt body asserts "PCF-2 v1.3 is 16 pp on Zenodo per
v1.16 picture". The workspace v1.3 PDF is 22 pp; the
V13-RELEASE 2026-05-02 build log
(`sessions/2026-05-02/PCF2-V13-RELEASE/build.log` L300) and
claim V13-A3 record 22 pp at v1.3 release; the v1.17 picture
(`tex/submitted/control center/picture_revised_20260504.md`)
contains no "16 pp PCF-2 v1.3" string. The "16 pp" in the
prompt body is a prompt-drafting confusion with PCF-1 v1.3
(G12 source-drift row, picture L983, where the 16-pp claim
applies to PCF-1, not PCF-2). **No HALT_G24_PAGE_COUNT_DRIFT**
fires; the workspace 22-pp build is the authoritative v1.3
artefact.

## Judgment calls made

- Treated `tex/submitted/pcf2_program_statement.tex` (the
  workspace TeX source) as the authoritative readback target,
  rather than fetching the Zenodo deposit, because (i) the
  workspace .pdf SHA matches the V13-RELEASE
  build-log-recorded hash and (ii) §6 of the spec rules out
  browser-driven Zenodo fetches.
- Did not perform OCR or pypdf full-text extraction on the
  PDF; relied on the source .tex L460–L500 (Conjecture B4
  block) for verbatim equation text. The .tex equation
  `eq:B4` is what pdflatex typesets at PDF page corresponding
  to §5 Conjecture B4.
- Diagnosed the prompt's "16 pp on Zenodo" assertion as a
  cross-paper confusion with PCF-1 v1.3 G12 rather than
  triggering HALT_G24_PAGE_COUNT_DRIFT; this is a non-trivial
  call (the alternative is to halt and surface to operator).
  Surfacing under Anomalies for Claude review.

## Anomalies and open questions

- **Prompt drafting drift (PCF-1 vs PCF-2 conflation)**: the
  relay-prompt body §1 + §4 references "PCF-2 v1.3 is 16 pp
  on Zenodo" appear inherited from PCF-1 v1.3 G12 framing;
  PCF-2 v1.3 has been 22 pp since 2026-05-02 release. The
  picture v1.17 row for PCF-2 carries no page count claim.
  Recommend: synthesizer audit cross-paper page-count
  references in next picture revision.
- **Phase 2 Anomaly 2 closure path narrowed, not closed**:
  G24 closes negatively. The empirical-vs-formal gap is real
  and must close through G23 + T1 Phase 3. M6
  (CC-VQUAD-PIII-NORMALIZATION-MAP) and Wasow §X.3 OCR remain
  parallel-safe.
- **Borderline-case structural insight reaffirmed**: PCF-2
  v1.3 contemplates the d=2 split (Open
  Problem `op:d2-anomaly`, `pcf2_program_statement.tex`
  L495–L497) as "the locus of an anomaly that does not
  persist at d ≥ 3". Phase A α-direction recovers exactly the
  d=2 lower branch (A=3, QL families) but not the upper
  branch (A=4, V_quad). This pattern — naive baseline
  recovers one of two empirical branches at d=2 and neither
  branch (in absolute number) at d ≥ 3 — is consistent with
  the stratum sitting at a Wimp-Zeilberger borderline locus.
  Already framed in v1.17 G23.
- **Q1 (quartic) fit precision**: PCF-2 v1.3 reports Q1 at
  dps=2000 with fit window N ∈ [200, 800] for the d=4
  harvest. R1.1 (cubic, j-invariant signal upgrade) records
  $A_\text{fit} = 6$ to within $10^{-3}$ at "R1.1 working
  precision" without naming a dps; the 5.978 ± 0.026 mean
  in §5 is at unspecified single-precision-of-fit. This is
  internally consistent but worth noting if a fresh
  re-measurement task is composed (out of scope here).

## What would have been asked (if bidirectional)

- Should HALT_G24_PAGE_COUNT_DRIFT fire on the prompt's "16
  pp" claim, or should the diagnosis (PCF-1 conflation) be
  trusted and the verdict proceed? (Resolved here by
  proceeding; flagged.)
- Are the four Phase B.3 alternatives (a)–(d) exclusive in the
  G24 framing, or could PCF-2 v1.3 simultaneously use
  convention (a) AND a sub-convention difference within
  (a) (e.g., `α-direction` vs `symmetric` vs `δ-direction`)?
  The Phase A table shows that within convention (a), the
  recurrence-direction matters: PCF-2 v1.3's $\delta_n =
  p_n/q_n - L$ does NOT specify which recurrence polynomial
  pair $(a, b)$ it presumes. If PCF-2 v1.3 implicitly uses
  the symmetric or δ-direction baseline rather than
  α-direction, the gap becomes 3 or 4 at d=3 (instead of 2).
  Surfacing as a sub-question: which recurrence-direction
  does PCF-2 v1.3 use? The answer is implicit in PCF-1 v1.3
  §6 (cited but not quoted here) and is the natural follow-up
  if any cross-direction subtlety is suspected.

## Recommended next step

G24 closes negatively as a definition-mismatch resolution
candidate; do not retire G23. Recommend two parallel firings:

1. **T1 Phase 3 (G23 closure)** — borderline-case anormal
   ansatz at SIARC stratum + Wasow §X.3 sectorial upgrade.
   This is the live G23 path. Already DRAFT-PENDING in v1.17
   §6.
2. **v1.18 picture revision** — retire G24 row (verdict
   recorded as `UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL`),
   leave G23 row open, no change to M4 closure path.

Optional follow-up (out of scope here): if a sub-convention
recurrence-direction subtlety is suspected, compose a
**PCF1-V13-SECTION6-RECURRENCE-DIRECTION-READBACK** task
(Tier-3, ~30 min) to pin which of α / symmetric / δ direction
is used in the empirical fit pipeline.

## Files committed

- `prompt_spec_used.md` — Phase 0 deposit
- `handoff.md` — this document (Phase E)
- `claims.jsonl` — 6 AEAL entries
- `halt_log.json` — empty {} (no HALT condition fired)
- `discrepancy_log.json` — 1 entry (page-count diagnosis)
- `unexpected_finds.json` — empty {} (no unexpected finds)

## AEAL claim count

6 entries written to `claims.jsonl` this session
(Phase A: 2; Phase B: 2; Phase C: 1; Phase D: 1).
