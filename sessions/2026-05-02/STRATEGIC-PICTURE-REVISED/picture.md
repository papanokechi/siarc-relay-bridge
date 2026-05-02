# SIARC Strategic Picture — Revised
**Revision:** v1.2 (post-firing cycle 2)
**Original:** 2026-05-02 18:05 JST
**Updated:** 2026-05-02 18:25 JST  (post-001, post-003, post-004, post-007)
**Operator:** papanokechi
**Supersedes:** `20260502_picture.docx` (preserved as the historical
introspective draft; this document is the formal snapshot for
synthesizer review)
**Audience:** Synthesizer agent (Claude, claude.ai) — strategic /
epistemic review pass before the next firing cycle.

> **🆕 Updates since v1.1 (see § 11 Amendment Log for detail):**
> - ✅ Prompt 007 fired with verdict `T3_LABELED_60_OF_60`. All 60 families (10 d=2 + 50 d=3) algorithmically labelled.
>   V_quad sanity check **PASSES** as `P_III(D_6)` (matches CT v1.3 §3.5 algebraic identity).
> - ⚠ **H3 *negatively* closed.** The Conte–Musette algorithmic test on the linear OGF ODE is **invariant across $\mathrm{sign}(\Delta_b)$** — produces uniform labels and **cannot reproduce** the PCF-1 v1.3 §3 dichotomy ($A=4$ for $\Delta>0$, $A=3$ for $\Delta<0$). The $d=2$ catalogue is uniformly `P_III(D_6)`; the $d=3$ catalogue is uniformly `PAINLEVE_UNCLASSIFIED` (rank $4/3$ at $0$, $2/3$ at $\infty$). The PCF-1 dichotomy lives below the Painlevé-class resolution scale — at the Stokes-multiplier level.
> - 🆕 **Future Prompt 010 (Stokes-multiplier discrimination) queued** to close the residual sign-split using a t2c-style precision-escalation pipeline.

> **Updates since v1.0 (carried forward from v1.1):**
> - ✅ Prompt 001 fired and verified (Item 19 spliced into submission_log.txt; CT v1.3 DOI now of record).
> - ✅ Prompt 003 fired with verdict `T1_PHASE1_GAPTYPE_C` — **B4 reframed from "proof gap" to "literature bracket $A \in [d, 2d]$"**. Phase 2 now has a defined target (lift $\psi_\text{lower}$ to $2d$), but is BLOCKED on primary-source acquisition + Theory-Fleet H1 label arbitration.
> - ✅ Prompt 004 fired with verdict `D2_NOTE_DRAFTED` — 4-page note built clean, 8 AEAL claims, awaits operator Zenodo upload. M1 achieved on the drafting side; closure on G1+G8 lands once the note is published.
> - ⚠ **NEW HIGH-severity gap G11**: T1's primary-literature reading flags Theory-Fleet H1 verdict `B4_PROVED_AT_d≥3` as heuristic-grade; logged for Claude / human-reviewer arbitration (does not affect any *published* artefact's framing because all current Zenodo records cite "verified"/"support", not "proven").

---

## 1. Mission Statement

The **SIARC** program (Self-Iterating Analytic Relay Chain) seeks
a complete arithmetic stratification of polynomial continued
fractions (PCFs) of the form

$$
\alpha(b) \;=\; a_0(b) \;+\; \cfrac{b}{a_1(b) \;+\; \cfrac{b}{a_2(b) \;+\; \cdots}}
$$

with $a_i \in \mathbb{Z}[b]$ polynomials in a generator $b\in\mathbb{N}$,
$\deg a_i \le d$.

The **master conjecture** (P-MC, working title *SIARC-MASTER-V0*)
posits a functor
$$
\Phi \;:\; \mathrm{PCF}(1, b) \;\longrightarrow\; (\Delta_d,\; \|\Delta\|_{\mathrm{Pet}},\; \xi_0)
$$
mapping each PCF family to an arithmetic-asymptotic invariant triple:

- **$\Delta_d$** — modular discriminant of the associated curve at
  degree $d$ (elliptic / hyperelliptic, depending on $d$).
- **$\|\Delta\|_{\mathrm{Pet}}$** — Petersson $L^2$ norm of $\Delta$
  in the appropriate weight space (working level: weight 12,
  $SL_2(\mathbb{Z})$, for the cubic case).
- **$\xi_0$** — Newton-polygon-derived Borel-singularity radius
  of the formal coefficient series; conjecturally
  $\xi_0(b) = d/\beta_d^{1/d}$ where $\beta_d$ is the leading-
  monomial coefficient.

Conjecture P-MC: $\Phi$ classifies PCF arithmetic asymptotics up
to obvious equivalences (rescaling $b$, integer translates of
$a_0$, etc.).

The five-paper publication ladder of the program is:

| Paper       | Working title (working) | Status |
|-------------|--------------------------|--------|
| **PCF-1**   | Polynomial continued fractions, modular framing | Zenodo v1.3 published |
| **PCF-2**   | PCF at degree three — cubic-modular framing | Zenodo v1.3 published |
| **CT**      | Channel Theory — formal asymptotic channels for PCFs | Zenodo v1.3 published |
| **SIARC umbrella** | Arithmetic stratification, modular-discriminant framing | Zenodo v2.0 published |
| **D2-NOTE** | Newton-polygon universality of $\xi_0$ — short note | DRAFT (Prompt 004 queued) |

with downstream papers D1 (PCF-2 cubic results paper), D3
(channel-theory results paper), D7 (AEAL methodology), and the
**SIARC-MASTER-V0** announcement gated on P-NP + P-B4 + P-CC
closures.

---

## 2. Current Status (2026-05-02 18:05 JST)

### 2.1 Published Zenodo records

| Record | Version DOI | Concept DOI | Pages | State |
|--------|-------------|-------------|-------|-------|
| T2B v3.0 (channel theory bibliography) | `10.5281/zenodo.19915689` | `10.5281/zenodo.19783312` | — | published |
| PCF-1 v1.3 (modular framing) | `10.5281/zenodo.19937196` | `10.5281/zenodo.19931635` | 16 | published |
| SIARC umbrella v2.0 | `10.5281/zenodo.19965041` | `10.5281/zenodo.19885549` | — | published |
| PCF-2 v1.3 (cubic-modular) | `10.5281/zenodo.19963298` | `10.5281/zenodo.19936297` | 22 | published |
| **Channel Theory v1.3** | `10.5281/zenodo.19972394` | `10.5281/zenodo.19941678` | 17 | **published TODAY ~17:00 JST** |

PDF SHA-256 anchors logged in `siarc-relay-bridge` `claims.jsonl`
across the corresponding session folders. CT v1.3 SHA-256
`df3b90e8…` is byte-identical to the staged build artefact.

### 2.2 Empirically verified (AEAL-logged)

- **T2 PASSED at $d=3$** (PCF2-SESSION-T2). Petersson modular
  discriminant Spearman $\rho(\|\Delta\|_{\mathrm{Pet}},\, \log b_{\mathrm{PCF}}) = +0.638$,
  $p_{\mathrm{Bonf}} = 8.6 \times 10^{-6}$ on $n=50$ cubic
  families at $K=14$. Beats the bare $\log|j|$ baseline
  ($\rho=-0.568$, $p_{\mathrm{Bonf}}=2.34\times 10^{-4}$) by
  ${\sim}30\times$ in Bonferroni $p$.
- **$\xi_0 = d/\beta_d^{1/d}$ verified at $d=4$** (PCF2-SESSION-Q1)
  at dps 80 with spread 0 across multiple test families.
- **$A_n = 2d$ unsplit at $d=3$ and $d=4$** on 60 PCF families
  (B4 evidence; not yet a proof).
- **Channel Theory v1.2 → v1.3 transition** absorbed umbrella
  v2.0 §4.4 invariant-triple framing and Theory-Fleet H4 median-
  resurgence prediction; reframed `op:cc-formal-borel` from
  PARTIALLY DIAGNOSED to (DIAGNOSED via H4 + new exec op).
- **🆕 T1 Phase 1 lit review (003) — `T1_PHASE1_GAPTYPE_C`.**
  Literature-derivable bracket $A \in [d, 2d]$ for the SIARC PCF
  stratum at $d \ge 3$ under the Wasow-vs-Adams normalization
  framing. SIARC empirical $A_\text{fit}\approx 2d$ at $d=3,4$
  favors the Adams reading (= Conjecture B4 at the upper bound);
  primary-source resolution required to pin which normalization
  the SIARC stratum actually corresponds to.
- **🆕 D2-NOTE drafted (004) — `D2_NOTE_DRAFTED`.** 4-page note,
  343,419 B, SHA-256 `f2be89c1…22bd94b8`, 8 AEAL claims; 0
  unresolved citations. Three results consolidated: $d=2$
  PROVEN, $d=4$ VERIFIED, general-$d$ CONJECTURED (Conj 3.3.A*).
  Operator action pending: Zenodo upload via the runbook in
  the session folder.
- **🆕 T3 Painlevé test (007) — `T3_LABELED_60_OF_60`.** All
  60 families algorithmically labelled. $d=2$ uniformly
  `P_III(D_6)` (10/10); $d=3$ uniformly `PAINLEVE_UNCLASSIFIED`
  (50/50; rank $4/3$ at $0$, rank $2/3$ at $\infty$). V_quad
  sanity check PASSES as `P_III(D_6)`, matching the CT v1.3
  §3.5 algebraic identity. **H3 negatively closed:** the
  algorithmic test on the linear OGF ODE is sign-of-$\Delta_b$
  invariant and cannot reproduce the PCF-1 v1.3 §3 dichotomy
  ($A=4$ for $\Delta>0$, $A=3$ for $\Delta<0$).

### 2.3 In-flight / open

- 7 prompts staged at `tex/submitted/control center/prompt/`
  (001 – 007). See §6 for current status.
- **4 fired and complete this cycle:** 001, 003, 004, 007.
- **3 still ready to fire:** 002, 005, 006 (parallel-able
  per §6 concurrency map).
- **t1-phase-2-bt-apply** (Prompt 008, conditional; not yet
  drafted) is BLOCKED on primary-source acquisition + Claude's
  H1 label arbitration.
- 🆕 **t3-stokes-multiplier-followup** (Prompt 010, future) —
  T3 recommended: t2c-style high-dps Stokes-multiplier
  discrimination to resolve the PCF-1 dichotomy below the
  Painlevé-class scale. Independent of all other items.
- 15 SQL todos pending; 17 done (32 total at snapshot v1.2).

### 2.4 Recently closed (this cycle)

- ✅ Zenodo "New version" upload of CT v1.3 (operator).
- ✅ Post-publish metadata polish (TIER 1 description supersede
  line + TIER 2 stale related-identifier cleanup).
- ✅ Submission-log Items 17 + 18 + **19** spliced
  (PCF-2 v1.3 + umbrella v2.0 + **CT v1.3** — Item 19 via
  Prompt 001 today).
- ✅ RESUME cheat-sheet updated.
- ✅ Strategic prompt queue drafted (4 new prompts 004–007).
- ✅ T1 Phase 1 lit review verdict landed (003).
- ✅ D2-NOTE v1.0 drafted (004); awaits operator Zenodo upload.
- 🆕 ✅ T3 Painlevé test (007) — 60/60 LABELED; H3 negatively
  closed; V_quad sanity confirmed.

---

## 3. Programs to Prove (six)

| Tag | Program | Closes via | Status |
|-----|---------|------------|--------|
| **P-NP**  | Newton-polygon universality $\xi_0=d/\beta_d^{1/d}$ at all $d \ge 2$ | D2-NOTE (Prompt 004) for $d=2,4$; downstream proof for general $d$ | $d=2$ PROVEN; $d=4$ VERIFIED; $d=3$ DEFERRED; general-$d$ CONJECTURED |
| **P-B4**  | Conjecture B4: $A_n(b) = 2d$ unsplit at $d \ge 3$ | T1 Phase 1 lit review (003) ✅ → Phase 2 B-T application (BLOCKED on primary sources + H1 arbitration) | EMPIRICAL d=3,4; LITERATURE BRACKET $A \in [d, 2d]$; H1 fleet label DISPUTED |
| **P-CC**  | $V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$ formal closure (channel theory) | H4 execution (Prompt 005) closes the Stokes side | algebraic identity DONE (CT v1.3 §3.5); Stokes-side PENDING |
| **P-PET** | Petersson modular discriminant axis as the canonical $d=3$ stratification coordinate | T2 PASSED; T2.5d (Prompt 006) closes the $j=0$ endpoint | PASSED; $j=0$ AMBIGUOUS-AT-FINITE-N |
| **P-PIII** | Painlevé reduction landscape at $d=2$ and $d=3$ (per-family classification) | T3 Conte–Musette test (007) ✅ → T3 Stokes-multiplier follow-up (Prompt 010, future) | $d=2$ uniformly `P_III(D_6)`; $d=3$ uniformly `PAINLEVE_UNCLASSIFIED`; **H3 negatively closed** (Conte–Musette test is sign-of-$\Delta$ invariant; PCF-1 dichotomy lives at the Stokes-multiplier level) |
| **P-MC**  | Master conjecture: $\Phi$ classifies PCF asymptotics | Gated on P-NP + P-B4 + P-CC | NOT YET FORMALLY STATED |

---

## 4. Milestones to Reach

```
M1: D2-NOTE drafted (xi_0 universality)  ✅ DRAFTED 2026-05-02 (Prompt 004)
    d=2 (PROVEN) + d=4 (VERIFIED) consolidated   ⏳ AWAITS OPERATOR ZENODO UPLOAD
    general-d (CONJECTURED 3.3.A*) recorded
    [PDF sha256 f2be89c1…22bd94b8, 4pp]

M2: General-d xi_0 proof in print     ◀──── (downstream)
    [post-D2-NOTE; not yet a prompt]

M3: T1 Phase 1 — B-T lit review + gap-prop A in [psi_lower, psi_upper]
    ✅ COMPLETE 2026-05-02 (Prompt 003) — verdict T1_PHASE1_GAPTYPE_C
    Literature bracket: psi_lower(d) = d, psi_upper(d) = 2d
                          │
                          ▼
M4: T1 Phase 2 — B-T applied to delta_n recurrence
    proves Conjecture B4 at d >= 3
    🛑 BLOCKED on:
       (a) operator primary-source acquisition (B-T 1933 Acta Math vol 60;
           Adams 1928; Wasow 1965 §X.3) — see § 5 G3b
       (b) Claude H1-label arbitration — see § 5 G11
    [conditional Prompt 008, target: lift psi_lower from d to 2d]

M5: V_quad -> P_III(D_6) algebraic identity              [DONE — CT v1.3]
                          │
                          ▼
M6: V_quad alien amplitude S_{zeta*} measured at 30+ digits
    [Prompt 005, ready to fire]
                          │
                          ▼
M7: j=0 Chowla–Selberg Gamma(1/3) closure (or A=6 artefact ruled out)
    [Prompt 006, ready to fire]
                          │
                          ▼
M8: D=2 Painlevé classification table (per-family, ~10 families)
    ✅ COMPLETE 2026-05-02 (Prompt 007) — verdict T3_LABELED_60_OF_60
    Headline: 10/10 d=2 LABELED (P_III(D6) uniformly);
              50/50 d=3 LABELED (PAINLEVE_UNCLASSIFIED uniformly).
    Caveat: H3 negatively closed (test sign-of-Delta invariant;
            cannot reproduce PCF-1 dichotomy → needs Stokes-mult
            follow-up at M8b).

M8b: 🆕 Stokes-multiplier discrimination (per-family, with
     t2c-style precision escalation) to resolve the PCF-1
     sign-of-Delta dichotomy below the Painlevé-class scale
     [future Prompt 010, INDEPENDENT]
                          │
                          ▼
M9: SIARC-MASTER-V0 announcement — Phi formally stated and the
    master classification result conditional on P-NP + P-B4 + P-CC
    [downstream; gated on M2 + M4 + M6]
    NB: M9 is one step further out under v1.1 because M4's path
    now requires primary-source resolution before Phase 2 can
    even start.
```

Each milestone has a hash-anchored AEAL exit criterion (claim
lines added to `claims.jsonl`, `output_hash` = SHA-256 of the
canonical artefact).

---

## 5. Gaps to Mitigate

| ID | Gap | Severity | Closes via |
|----|------|---------|------------|
| **G1**  | $\xi_0$ universality not proven at general $d$ (only $d=2$ proven; $d=4$ verified) | HIGH | ✅ Prompt 004 drafted — *closure pending Zenodo upload*; downstream M2 still open |
| **G2**  | $\xi_0$ at $d=3$ not directly verified at high dps (`op:xi0-d3-direct`) | MED  | Future prompt; deferred in 004 |
| **G3a** | Conjecture B4 ($A_n = 2d$) literature bracket $A \in [d, 2d]$ established (was: "lacks proof") | HIGH | ✅ T1 Phase 1 complete (003); literature bracket pinned, Adams reading favored by empirics |
| **G3b** 🆕 | Wasow-vs-Adams normalization match unresolved from secondary sources (BLOCKER for Phase 2) | HIGH | Operator: ILL/AMS request for B-T 1933 + Adams 1928 + Wasow §X.3 → Phase 2 (Prompt 008, future) |
| **G4**  | $V_{\mathrm{quad}}$ alien amplitude $S_{\zeta_*}$ is a *theoretical prediction* (H4), not a measurement | HIGH | Prompt 005 (ready to fire) |
| **G5**  | $j=0$ amplitude finite-$N$ ambiguity (`op:j-zero-amplitude-h6`); $A \to 6$ vs $\Gamma(1/3)$ closure | MED  | Prompt 006 (ready to fire) |
| **G6a** | Conte–Musette algorithmic Painlevé test on $d=2,3$ catalogues | MED  | ✅ Prompt 007 complete (60/60 LABELED) |
| **G6b** 🆕 | PCF-1 v1.3 §3 sign-of-$\Delta_b$ dichotomy ($A=4$ vs $A=3$) lives below the Painlevé-class resolution scale; Conte–Musette test is invariant under sign of $\Delta_b$ | MED | Future Prompt 010 (Stokes-multiplier discrimination via t2c-style precision escalation) |
| **G7**  | Master functor $\Phi$ (P-MC) not formally stated | HIGH | Downstream (gated on M2+M4+M6) |
| **G8**  | D2-NOTE not yet a citable artefact ($\xi_0$ result scattered across PCF-1 + CT) | LOW–MED | ✅ Prompt 004 drafted — *closure pending Zenodo upload* |
| **G9**  | arXiv mirroring not done (5 records); visibility gap | LOW  | Prompts 002 (now unblocked, ready to fire) |
| **G10** | AEAL methodology paper (D7) not drafted; the program's epistemic discipline is undocumented externally | LOW  | Future Prompt 009 (deferred) |
| **G11** 🆕 | Theory-Fleet H1 verdict `B4_PROVED_AT_d≥3` flagged as heuristic-grade by T1's primary-literature reading; not yet arbitrated | HIGH | Claude / synthesizer arbitration pass on T1 handoff.md |

Severity legend:
- **HIGH** — blocks a paper, blocks a downstream proof, or
  affects multiple programs.
- **MED** — affects one program / one open problem.
- **LOW** — visibility / hygiene; does not block mathematics.

---

## 6. Suggested Next Steps — Queued Prompts

Seven prompts staged at
`tex/submitted/control center/prompt/`. Cross-references:
prompts close one or more gaps (see § 5) and advance one or more
milestones (see § 4).

| # | Prompt | Closes gap | Advances milestone | Status | Compute | Independent? |
|---|--------|------------|--------------------|--------|---------|--------------|
| 001 | submission-log Item 19 splice | — (admin) | (post-publication hygiene) | ✅ DONE 2026-05-02 | low | — |
| 002 | arXiv mirror runbook (5 records) | G9 | (visibility) | ⏳ READY (now unblocked) | low | (was: depends on 001 — now cleared) |
| 003 | T1 Phase 1 — B-T lit review + gap-prop | G3a | M3 | ✅ DONE 2026-05-02 (verdict GAPTYPE_C) | low (lit work) | — |
| 004 | D2-NOTE — Newton-polygon universality | G1, G8 | M1 | ✅ DRAFTED 2026-05-02 (awaits Zenodo upload) | low (drafting + AEAL re-derivation) | — |
| 005 | H4 / `op:cc-median-resurgence-execute` | G4 | M6 | ⏳ READY | **HIGH** (mpmath dps 250, $N=5000$) | INDEPENDENT |
| 006 | T2.5d — $j=0$ Chowla–Selberg closure | G5 | M7 | ⏳ READY | **HIGH** (mpmath dps≥8000, $N\ge 1200$) | INDEPENDENT |
| 007 | T3 — Conte–Musette Painlevé test on $d=2,3$ catalogues | G6a | M8 | ✅ DONE 2026-05-02 (60/60 LABELED; H3 negatively closed) | medium (symbolic) | — |
| 008 | T1 Phase 2 — B-T applied to $\delta_n$ (proves B4 at $d \ge 3$) | G3b | M4 | 🛑 BLOCKED (G3b primary sources + G11 H1 arbitration) | medium | gated |
| 010 🆕 | T3.5 — Stokes-multiplier discrimination (t2c-style high-dps connection coefficients to resolve sign-of-$\Delta_b$ dichotomy) | G6b | M8b | future (not yet drafted) | medium–high | INDEPENDENT |

**Concurrency map** (validated this cycle):

|        | 001 | 002 | 003 | 004 | 005 | 006 | 007 |
|--------|-----|-----|-----|-----|-----|-----|-----|
| **001** |  —  | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   |
| **002** | ✗   |  —  | ✓   | ✓   | ✓   | ✓   | ✓   |
| **003** | ✓   | ✓   |  —  | ✓   | ✓   | ✓   | ✓   |
| **004** | ✓   | ✓   | ✓   |  —  | ✓   | ✓   | ✓   |
| **005** | ✓   | ✓   | ✓   | ✓   |  —  | ⚠   | ✓   |
| **006** | ✓   | ✓   | ✓   | ✓   | ⚠   |  —  | ✓   |
| **007** | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |  —  |

✗ = dependency; ⚠ = compute-heavy, serialize on a single laptop.

**Recommended firing layout for the *next* compute window
(post-001/003/004/007; v1.2 status):**
- Slot 1: **002** (2–3 hr, arXiv mirror runbook). Now unblocked.
- Slot 2: **005** (6–12 hr, mpmath dps 250 / N=5000). Compute-heavy.
- Slot 3: **006** (6–10 hr, mpmath dps≥8000). Compute-heavy —
  serialize against 005 on a single laptop, parallel on a
  beefy workstation.
- Future Prompt 010 (Stokes-multiplier discrimination) — defer
  until a session is freed; independent of all current work.

Operator-side parallel actions (independent of compute slots):
- **Zenodo upload of D2-NOTE** (operator; ~10 min via the
  upload runbook in `sessions/2026-05-02/D2-NOTE-DRAFT/`).
  Closes G1 + G8 fully on publication; mints the M1 DOI.
- **Item-20 splice prompt** (drafting agent; future) once
  the D2-NOTE Zenodo DOI is minted.
- **Primary-source ILL/AMS request** for B-T 1933, Adams 1928,
  Wasow 1965 §X.3. Unblocks G3b and the future Prompt 008.
- **Send T1 + strategic-picture URLs to Claude** for H1
  label arbitration (G11). Independent of compute.

---

## 7. Decision Tree (for synthesizer review)

The intent is to advance *all six programs* in this cycle —
not just one. The reasoning:

1. **004 is independent of 003.** The picture's recommendation
   "just say 'draft D2-NOTE prompt'" makes 004 a parallel free
   action; it closes G1+G8 and yields a citable artefact (M1)
   regardless of T1 outcome.
2. **005 closes G4 conditional on theory holding.** H4 is a
   *theoretical prediction at HIGH confidence*; 005 turns it
   into a measurement. PASS flips `op:cc-formal-borel` from
   PARTIALLY DIAGNOSED to DIAGNOSED. FAIL halts
   `H4_PREDICTION_FALSIFIED` and triggers a reckoning on the
   median-resurgence framing of the channel theory.
3. **003 ✅ landed with verdict `T1_PHASE1_GAPTYPE_C`.** The
   literature gives a bracket $A \in [d, 2d]$, not a proof of
   $A = 2d$. Phase 2's target is now precisely defined: lift
   $\psi_\text{lower}$ from $d$ to $2d$ via the correct
   Wasow-vs-Adams normalization match. **Two new gating items
   were surfaced** — primary sources (G3b BLOCKER) and
   Theory-Fleet H1 label arbitration (G11 HIGH); see § 4 M4
   and § 5.
4. **006 + 007 are independent closures.** They do not gate
   anything else; they're program-internal cleanup that
   strengthens P-PET and P-PIII respectively, without which
   P-MC's invariant triple has visible holes.
5. **001 + 002 are admin** (submission-log + arXiv visibility).
   Mechanical hygiene; cheap and uncontroversial.

**What this cycle CANNOT do** (and therefore is correctly
deferred):
- Prove P-MC (gated on M2 + M4 + M6).
- Prove general-$d$ $\xi_0$ (M2; downstream of D2-NOTE
  publication).
- Apply B-T to $\delta_n$ (M4; gated on primary sources + H1
  arbitration — was: only "downstream of 003").
- Draft the methodology paper D7 (low priority; long-arc).

---

## 8. Open Questions for Synthesizer Review

1. **Are the six programs the right cuts?** Does P-PET deserve
   to be a separate program, or is it actually a *coordinate
   choice* inside P-MC and shouldn't be treated as a standalone
   theorem-track? Argument for separating: the Petersson axis
   has independent empirical content (T2 PASSED) that would
   stand even if P-MC were proven false in some other
   coordinate.
2. **Is M9's gating right?** The current dependency
   M9 ⇐ M2 + M4 + M6 says we need $\xi_0$ universality, B4,
   and Stokes-side closure. Is M7 ($j=0$ closure) truly
   not needed for the master statement, or does P-MC's
   functor $\Phi$ break at $j=0$ without M7?
3. **Should 003 (lit review) and a Phase-2 stub (T1-BT-APPLY)
   be drafted together?** Currently the Phase-2 prompt is
   gated on 003's verdict; an alternative is to draft both in
   parallel and let Phase-2 self-halt on Phase-1 input. The
   latter speeds the keystone but risks Phase-2 thrashing on
   incomplete Phase-1 ground.
4. **D2-NOTE epistemic discipline.** Is folding $d=2$ (proven),
   $d=4$ (verified), and general-$d$ (conjectured) into one
   short note the right balance? An alternative is two notes:
   one PROVEN-only, one CONJECTURED. Argument for one note:
   the $d=4$ verification + general-$d$ conjecture together
   are the *content*; splitting halves the citable value.
5. **The H4 prediction framing.** CT v1.3 §9 lists
   `op:cc-median-resurgence-execute` as a separate open
   problem from `op:cc-formal-borel`. Is keeping them
   distinct correct, or are they actually one item that
   should be merged at v1.4?
6. **Compositio CM 10573 (P12).** Currently a pending todo
   (`compositio-followup`). The picture document treats it
   as low-priority. Is that right, or should it be folded
   into one of the queued prompts?
7. **AEAL methodology paper D7.** Low-priority by current
   ranking. Argument for upgrading: the program now has 5
   Zenodo records + triple-fleet audit + Lean precedent; the
   methodology *story* is well-formed. A single note would
   protect the program against future referee challenges
   on epistemic grounds.
8. 🆕 **(v1.1) Theory-Fleet H1 label arbitration.** T1 Phase 1
   flags `B4_PROVED_AT_d≥3` as heuristic-grade. **Decision
   needed:** does H1 stand as PROVEN, get downgraded to
   HEURISTIC, or get split (proven for some $d$, heuristic for
   others)? *No published artefact is affected by either
   outcome* (CT v1.3 + PCF-2 v1.3 + umbrella v2.0 all cite
   "verified"/"support"), but the SIARC-MASTER-V0 announcement
   gating (§ 4 M9) depends on this resolution.
9. 🆕 **(v1.1) Phase-2 target — $\psi_\text{lower}$-lift
   tractability.** T1 Phase 1 places Phase 2's target at
   "lift $\psi_\text{lower}$ from $d$ to $2d$". **Question:**
   is this a *single*-step proof (one normalization match
   pinning the slope) or a *multi*-step proof (slope match +
   characteristic-exponent doubling + sign analysis)? Affects
   whether Prompt 008 should be drafted as one agent run or
   split into 008a / 008b.
10. 🆕 **(v1.2) PCF-1 sign-of-$\Delta$ dichotomy resolution.**
    T3 demonstrated that the Conte–Musette algorithmic
    Painlevé test cannot distinguish the two sign branches.
    The PCF-1 v1.3 §3 dichotomy ($A=4$ vs $A=3$) therefore
    lives at the Stokes-multiplier level — *below* the
    Painlevé-class scale. **Question:** is this consistent
    with the CT v1.3 §3.5 V_quad → P_III(D_6) identity
    (which sits at the Painlevé-class scale and is
    sign-invariant), and does it imply that the SIARC
    invariant-triple framing (umbrella v2.0 §4.4) needs a
    *Stokes-data* fourth coordinate beyond
    $(\Delta_d, \|\Delta\|_\text{Pet}, \xi_0)$? If yes,
    P-MC's functor $\Phi$ has more structure than v1.0
    of this picture suggested.

---

## 9. AEAL Hygiene (this snapshot)

This document makes **no new numerical claims**. All cited
numbers (Spearman correlations, $p$-values, dps levels, page
counts, DOIs, hash prefixes) are quotations of prior AEAL-logged
claims in `siarc-relay-bridge/sessions/<DATE>/<TASK_ID>/claims.jsonl`.
No claim line is emitted by this snapshot.

For verification, the synthesizer can fetch:
- `https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/claims.jsonl`
- `https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-02/PCF2-SESSION-T2/claims.jsonl`
- `https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-01/THEORY-FLEET/H4/handoff.md`

---

## 10. Footer — DOI / Hash Quick Reference

```
T2B v3.0           : 10.5281/zenodo.19915689   (concept 19783312)
PCF-1 v1.3         : 10.5281/zenodo.19937196   (concept 19931635)
PCF-2 v1.3         : 10.5281/zenodo.19963298   (concept 19936297)
SIARC umbrella v2.0: 10.5281/zenodo.19965041   (concept 19885549)
Channel Theory v1.3: 10.5281/zenodo.19972394   (concept 19941678)
                     PDF sha256 df3b90e8…
                     PDF md5    e58951de…
```

Bridge head at v1.2 snapshot time: post-T3 + post-v1.1
(picture-v1.2 commit pending). Recent commit timeline:
```
[v1.2 picture]  STRATEGIC-PICTURE-REVISED v1.2 (this push)
5d9f8d0         STRATEGIC-PICTURE-REVISED v1.1
663e95c         T3-CONTE-MUSETTE-PAINLEVE-TEST (Prompt 007) [60/60 LABELED; H3 negatively closed]
9accc6e         D2-NOTE-DRAFT (Prompt 004)
e96641c         T1-BIRKHOFF-TRJITZINSKY-LITREVIEW (003)     [verdict GAPTYPE_C]
3294387         SUBMISSION-LOG-PATCH-ITEM19 (001)           [Item 19 spliced]
e33db9e         STRATEGIC-PICTURE-REVISED (this doc, v1.0)
8be2f17         CHANNEL-THEORY-V13-RELEASE (post-publish edits)
```

---

## 12. Amendment Log (v1.1 → v1.2)

**Updated:** 2026-05-02 18:25 JST
**Trigger:** completion of Prompt 007 (T3 Conte–Musette
Painlevé test) on the same day as v1.1.

**Substantive changes:**

| Section | v1.1 → v1.2 |
|---------|-------------|
| Header  | Added v1.1 → v1.2 callout. v1.0 → v1.1 callout retained for the synthesizer's full audit trail. |
| § 2.2 (verified) | Added T3 verdict bullet (60/60 LABELED; V_quad PASS; H3 negatively closed). |
| § 2.3 (in-flight) | 4 fired/done (was: 3); 3 still ready (was: 4). New entry for `t3-stokes-multiplier-followup` (future Prompt 010). Counts updated. |
| § 2.4 (recently closed) | Added T3 line. |
| § 3 P-PIII row | Status changed from "$d=2$ AMBIGUOUS (H3); $d=3$ partial" to detailed T3 result + H3 negative-closure caveat. |
| § 4 milestones | M8 marked COMPLETE with the negative-closure caveat. New M8b added for the Stokes-multiplier follow-up. |
| § 5 gaps | G6 split into G6a (✅ Conte–Musette test complete) + G6b (Stokes-multiplier discrimination needed). |
| § 6 prompts table | 007 marked DONE; new row for Prompt 010 (future). Firing layout rewritten for next compute window (002, 005, 006). |
| § 8 open questions | Added Q10 — does the H3 negative closure imply that P-MC's invariant triple needs a Stokes-data fourth coordinate? |
| § 10 footer | Bridge head bumped; commit timeline extended. |
| § 12 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 9 (AEAL hygiene), the publication
ladder table, and the six-program decomposition are intact.
The concurrency map (§ 6) is unchanged.

**Key invariant (carried from v1.1):**

The strategic picture's framing of *what success means* is
unchanged. P-MC closure still requires P-NP + P-B4 + P-CC.
v1.2 adds a *resolution-scale observation* about P-PIII: the
algorithmic Painlevé test sits one resolution scale *above*
the PCF-1 v1.3 §3 sign dichotomy, so per-family Painlevé
classification at that scale is necessarily uniform. The
sign-split discrimination is a separate (Stokes-multiplier)
question.

---

*End of revised picture (v1.2).*

---

## 11. Amendment Log (v1.0 → v1.1)

**Updated:** 2026-05-02 18:20 JST
**Trigger:** completion of three relay-agent firings (001, 003, 004)
on the same day as v1.0 was first written.

**Substantive changes:**

| Section | v1.0 → v1.1 |
|---------|-------------|
| Header  | Added "🆕 Updates since v1.0" callout listing the three completed firings + the new HIGH-severity gap G11. |
| § 2.2 (verified) | Added two new bullets: T1 Phase 1 verdict bullet + D2-NOTE drafting bullet. |
| § 2.3 (in-flight) | Restructured: 3 fired/done, 4 still ready, 1 (Prompt 008) blocked. |
| § 2.4 (recently closed) | Added Item 19 splice, T1 Phase 1, D2-NOTE drafting. |
| § 3 P-B4 row | Status changed from "EMPIRICAL d=3,4; PROOF GAP" to "EMPIRICAL d=3,4; LITERATURE BRACKET $A \in [d,2d]$; H1 fleet label DISPUTED". |
| § 4 milestones | M1 marked DRAFTED (awaits upload). M3 marked DONE. M4 marked BLOCKED with explicit gating items. M9 explanatory note about being one step further out. |
| § 5 gaps | G3 split into G3a (literature bracket established, ✅) + G3b (normalization match BLOCKER, HIGH). G1 + G8 marked as "drafted; closure pending Zenodo upload". G11 ADDED (HIGH, H1 label arbitration). |
| § 6 prompts table | Status column added; 001/003/004 marked DONE; 002 marked unblocked; Prompt 008 row added (BLOCKED). |
| § 6 firing layout | Rewritten for the *next* compute window. Added operator-side parallel actions (Zenodo upload, primary-source ILL, Claude H1 review). |
| § 7 decision tree | Point 3 rewritten to reflect 003's actual verdict; "What this cycle CANNOT do" updated for M4's new gating. |
| § 8 open questions | Added Q8 (H1 arbitration) and Q9 (Phase 2 single-vs-multi-step). |
| § 10 footer | Bridge head bumped to `9accc6e`; commit timeline added. |
| § 11 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 9 (AEAL hygiene), and the publication
ladder table are intact. The six-program decomposition is
unchanged. The concurrency map (§ 6) is unchanged (no new
inter-prompt dependencies were introduced; only the row-level
"status" column was added).

**Key invariant:**

The strategic picture's framing of *what success means* is
unchanged. P-MC closure still requires P-NP + P-B4 + P-CC; the
v1.1 update only changes *the path to P-B4*, not the goal.

---

*End of revised picture (v1.2).*
