# SIARC Strategic Picture — Revised
**Date:** 2026-05-02 18:05 JST
**Operator:** papanokechi
**Supersedes:** `20260502_picture.docx` (preserved as the historical
introspective draft; this document is the formal snapshot for
synthesizer review)
**Audience:** Synthesizer agent (Claude, claude.ai) — strategic /
epistemic review pass before the next firing cycle.

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

### 2.3 In-flight (queued but not yet fired)

- 7 prompts staged at `tex/submitted/control center/prompt/`
  (001 – 007). See §6.
- 12 SQL todos pending; 14 done (26 total).
- T1 Phase 1 (Birkhoff–Trjitzinsky lit review) is the gating
  KEYSTONE for P-B4. Prompt 003 is ready to fire.

### 2.4 Recently closed (this cycle)

- ✅ Zenodo "New version" upload of CT v1.3 (operator).
- ✅ Post-publish metadata polish (TIER 1 description supersede
  line + TIER 2 stale related-identifier cleanup).
- ✅ Submission-log Items 17 + 18 spliced (PCF-2 v1.3 + umbrella
  v2.0).
- ✅ RESUME cheat-sheet updated.
- ✅ Strategic prompt queue drafted (4 new prompts 004–007).

---

## 3. Programs to Prove (six)

| Tag | Program | Closes via | Status |
|-----|---------|------------|--------|
| **P-NP**  | Newton-polygon universality $\xi_0=d/\beta_d^{1/d}$ at all $d \ge 2$ | D2-NOTE (Prompt 004) for $d=2,4$; downstream proof for general $d$ | $d=2$ PROVEN; $d=4$ VERIFIED; $d=3$ DEFERRED; general-$d$ CONJECTURED |
| **P-B4**  | Conjecture B4: $A_n(b) = 2d$ unsplit at $d \ge 3$ | T1 Phase 1 lit review (003) → Phase 2 B-T application | EMPIRICAL d=3,4; PROOF GAP |
| **P-CC**  | $V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$ formal closure (channel theory) | H4 execution (Prompt 005) closes the Stokes side | algebraic identity DONE (CT v1.3 §3.5); Stokes-side PENDING |
| **P-PET** | Petersson modular discriminant axis as the canonical $d=3$ stratification coordinate | T2 PASSED; T2.5d (Prompt 006) closes the $j=0$ endpoint | PASSED; $j=0$ AMBIGUOUS-AT-FINITE-N |
| **P-PIII** | Painlevé reduction landscape at $d=2$ and $d=3$ (per-family classification) | Conte–Musette test (Prompt 007) | $d=2$ AMBIGUOUS (H3); $d=3$ partial |
| **P-MC**  | Master conjecture: $\Phi$ classifies PCF asymptotics | Gated on P-NP + P-B4 + P-CC | NOT YET FORMALLY STATED |

---

## 4. Milestones to Reach

```
                     ┌─────────────────────────── M1 ──────────────────┐
                     │                                                   │
                     │ M1: D2-NOTE published (xi_0 universality)         │
                     │     d=2 (PROVEN) + d=4 (VERIFIED) citable        │
                     │     [Prompt 004]                                  │
                     │                                                   │
M2: General-d xi_0 proof in print     ◀──── (downstream)
    [post-D2-NOTE; not yet a prompt]

M3: T1 Phase 1 — B-T lit review + gap-prop A in [psi_lower, psi_upper]
    [Prompt 003]
                          │
                          ▼
M4: T1 Phase 2 — B-T applied to delta_n recurrence
    proves Conjecture B4 at d >= 3
    [conditional Prompt 008, gated on M3]
                          │
                          ▼
M5: V_quad -> P_III(D_6) algebraic identity              [DONE — CT v1.3]
                          │
                          ▼
M6: V_quad alien amplitude S_{zeta*} measured at 30+ digits
    [Prompt 005]
                          │
                          ▼
M7: j=0 Chowla–Selberg Gamma(1/3) closure (or A=6 artefact ruled out)
    [Prompt 006]
                          │
                          ▼
M8: D=2 Painlevé classification table (per-family, ~10 families)
    [Prompt 007]
                          │
                          ▼
M9: SIARC-MASTER-V0 announcement — Phi formally stated and the
    master classification result conditional on P-NP + P-B4 + P-CC
    [downstream; gated on M2 + M4 + M6]
```

Each milestone has a hash-anchored AEAL exit criterion (claim
lines added to `claims.jsonl`, `output_hash` = SHA-256 of the
canonical artefact).

---

## 5. Gaps to Mitigate

| ID | Gap | Severity | Closes via |
|----|------|---------|------------|
| **G1**  | $\xi_0$ universality not proven at general $d$ (only $d=2$ proven; $d=4$ verified) | HIGH | Prompt 004 (cites + conjectures); downstream M2 |
| **G2**  | $\xi_0$ at $d=3$ not directly verified at high dps (`op:xi0-d3-direct`) | MED  | Future prompt; deferred in 004 |
| **G3**  | Conjecture B4 ($A_n = 2d$) lacks proof at $d \ge 3$ | HIGH | Prompts 003 → 008 |
| **G4**  | $V_{\mathrm{quad}}$ alien amplitude $S_{\zeta_*}$ is a *theoretical prediction* (H4), not a measurement | HIGH | Prompt 005 |
| **G5**  | $j=0$ amplitude finite-$N$ ambiguity (`op:j-zero-amplitude-h6`); $A \to 6$ vs $\Gamma(1/3)$ closure | MED  | Prompt 006 |
| **G6**  | $d=2$ PCF Painlevé reduction ambiguous (H3 = `D=2_REDUCTION_AMBIGUOUS`); not algorithmically classified | MED  | Prompt 007 |
| **G7**  | Master functor $\Phi$ (P-MC) not formally stated | HIGH | Downstream (gated on M2+M4+M6) |
| **G8**  | D2-NOTE not yet a citable artefact ($\xi_0$ result scattered across PCF-1 + CT) | LOW–MED | Prompt 004 |
| **G9**  | arXiv mirroring not done (5 records); visibility gap | LOW  | Prompts 002 (after 001) |
| **G10** | AEAL methodology paper (D7) not drafted; the program's epistemic discipline is undocumented externally | LOW  | Future Prompt 009 (deferred) |

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

| # | Prompt | Closes gap | Advances milestone | Runtime | Compute | Independent? |
|---|--------|------------|--------------------|---------|---------|--------------|
| 001 | submission-log Item 19 splice | — (admin) | (post-publication hygiene) | ~10 min | low | needs CT v1.3 DOI on chat line 1 (`10.5281/zenodo.19972394`) |
| 002 | arXiv mirror runbook (5 records) | G9 | (visibility) | ~2–3 hr | low | depends on 001 |
| 003 | T1 Phase 1 — B-T lit review + gap-prop | G3 | M3 | ~3–4 hr | low (lit work) | INDEPENDENT |
| 004 | D2-NOTE — Newton-polygon universality | G1, G8 | M1 | ~4–6 hr | low (drafting + AEAL re-derivation) | INDEPENDENT |
| 005 | H4 / `op:cc-median-resurgence-execute` | G4 | M6 | ~6–12 hr | **HIGH** (mpmath dps 250, $N=5000$) | INDEPENDENT |
| 006 | T2.5d — $j=0$ Chowla–Selberg closure | G5 | M7 | ~6–10 hr | **HIGH** (mpmath dps≥8000, $N\ge 1200$) | INDEPENDENT |
| 007 | T3 — Conte–Musette Painlevé test on $d=2,3$ catalogues | G6 | M8 | ~4–8 hr | medium (symbolic) | INDEPENDENT |

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

**Recommended firing layout (single laptop, 4–6 cores):**
- Slot 1: **001** (10 min, fire-and-forget once DOI is in chat line 1).
- Slot 2: **003** (3–4 hr, lit review).
- Slot 3: **004** (4–6 hr, D2-NOTE drafting).
- Slot 4: **007** (4–8 hr, symbolic test).
- Slot 5: **005** (6–12 hr, compute-heavy).
- After 005 lands: **006** in slot 5 (compute-heavy, serialized).
- After 001 lands: **002** in any free slot (lap-around hygiene).

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
3. **003 is the one HIGH-severity gap that does not have a
   downstream prompt yet.** Phase 2 (T1 Phase 2 = B-T applied
   to $\delta_n$) waits on 003's gap-proposition formalisation.
   Without 003, P-B4 has no defined target.
4. **006 + 007 are independent closures.** They do not gate
   anything else; they're program-internal cleanup that
   strengthens P-PET and P-PIII respectively, without which
   P-MC's invariant triple has visible holes.
5. **001 + 002 are admin** (submission-log + arXiv visibility).
   Mechanical hygiene; cheap and uncontroversial.

**What this cycle CANNOT do** (and therefore is correctly
deferred):
- Prove P-MC (gated on M2 + M4 + M6).
- Prove general-$d$ $\xi_0$ (M2; downstream of D2-NOTE).
- Apply B-T to $\delta_n$ (M4; downstream of 003).
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

Bridge head at snapshot time: `8be2f17`
("CHANNEL-THEORY-V13-RELEASE — operator applied post-publish
edits; verify TIER 1 + TIER 2 clean on Zenodo readback").

---

*End of revised picture.*
