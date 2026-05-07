# 104 Peer-Consult Synthesis — M4 V0 Fast-Track Path

**Relay**: `tex/submitted/control center/prompt/104_peer_consult_m4_fast_track.txt`
**Bridge HEAD at synthesis**: `e1b1c99`
**Verdict**: **V_FT4_RECOMMENDED** (M4 solo ratification + later LANE-1 catch-up)
**Consensus strength**: STRONG on rejections (FT-0, FT-2 unanimous); MODERATE on positive recommendation (3-vote plurality for decoupled; 2-vote minority for batched)

---

## §1. Verdict tally across 5 peer-AI consultants

| Consultant | Q1 (FT-0?) | Q2 (FT-1 vs FT-3) | Q3 (FT-2?) | Q4 (coupling) | Q5 path | Q6 (M9?) | Confidence |
|---|:---:|---|:---:|---|:---:|:---:|:---:|
| Claude Opus 4.7 (Anthropic web)        | NO | FT-3 prefer (small Δ)         | NO | minor but real     | **FT-3** | NO | HIGH |
| Copilot-Consult-01                     | NO | governance-identical, FT-3 lowest risk | NO | modest         | **FT-4** | NO | HIGH |
| Gemini-3-Flash                         | NO | FT-1 velocity / FT-3 cohesion | NO | minimal/none       | **FT-1 (via FT-4)** | NO | HIGH |
| Grok-xAI                               | NO | FT-3 cleaner, FT-1 acceptable | NO | minor              | **FT-1** | NO | HIGH |
| Claude Opus 4.7 xhigh (Copilot CLI)    | NO | FT-3 strict-dominance         | NO | procedural only    | **FT-3** | NO | HIGH/MED |

### Aggregate vote on Q5 (recommended path)

| Path | Votes | Voters |
|---|:---:|---|
| FT-0 (operator self-ratify) | **0/5** | — UNANIMOUS REJECT |
| FT-1 (synth alone) | 2/5 | Gemini, Grok |
| FT-2 (multi-consultant parallel) | **0/5** | — UNANIMOUS REJECT |
| FT-3 (full LANE-1 batch standard) | 2/5 | Claude web, Claude xhigh CLI |
| FT-4 (FT-1 + later catch-up) | 1/5 | Copilot-Consult-01 |

### Re-grouped by topology (decoupled vs batched)

| Topology | Votes | Voters |
|---|:---:|---|
| **Decoupled** (FT-1 or FT-4) | **3/5** | Copilot-Consult-01, Gemini, Grok |
| **Batched** (FT-3) | 2/5 | Claude web, Claude xhigh CLI |

---

## §2. Unanimous findings

### Q1 — FT-0 (operator self-ratify) — 5/5 NO
All 5 consultants reject FT-0 on identical reasoning: 074 `DOSSIER_COMPLETE` is an *assembly* verdict (substrate readiness) NOT a synth-tier *signature* verdict. Treating dossier completeness as ratification collapses the producer/reviewer separation and creates a dangerous precedent that future fires can self-ratify on dossier completeness alone.

### Q3 — FT-2 (multi-consultant parallel) — 5/5 NOT JUSTIFIED
All 5 reject FT-2 here. Reasoning convergence:
- M4 substrate (068 + 074) is *non-contested*; multi-consultant variance has low expected information yield
- Tie-break protocol is **undefined** — adopting FT-2 would require resolving meta-governance gap before closing M4 (inverts the earliest-close objective)
- Existing solo-ratification precedents (048R-EARLY, 060-class) are sufficient

**LATENT GOVERNANCE LIABILITY** (flagged by Claude web + Claude xhigh CLI): The FT-2 tie-break gap will surface eventually under contested-substrate conditions. Worth drafting a SIARC tie-break protocol as a low-priority bridge item before forced under time pressure.

### Q6 — M9 V0 compression via M4 fast-track — 5/5 NO
All 5 confirm M9 V0 deposit is **hard-gated on M6.CC R1 analytic substrate closure**, NOT on M4 timing. M4 fast-track unblocks M7/M8a/M8b cascade but does NOT compress M9 horizon. The dominant M9 path is M6.CC analytic work; M4 fast-tracking saves only the M4-ratification serial step.

---

## §3. Disputed findings (FT-1/FT-4 vs FT-3)

The 3-2 split between decoupled (FT-1/FT-4) and batched (FT-3) hinges on a single empirical question:

> **Is the LANE-1 batch fully dispatch-ready at the same operator-readiness event as M4-alone dispatch?**

### FT-3 advocates' argument (Claude web + Claude xhigh CLI)
- "Earliest event-clock counts logical events, not wall-clock minutes within an event" (Claude xhigh)
- If LANE-1 batch is ready at the same event as M4-alone → FT-3 dispatches both in one synth pass at zero incremental governance cost
- FT-3 closes M6.CC + 069r2 + 102/103 absorption simultaneously → M9 V0 gate progress as side-effect
- Standard pattern; zero deviation from §2 baseline

### FT-1/FT-4 advocates' argument (Copilot-Consult-01 + Gemini + Grok)
- 069r2 Path γ envelope is **not yet drafted** (per `m_critical_path_2026-05-07.md` §3 substrate inventory: 102 substrate complete, but the envelope is pending synth drafting)
- Therefore LANE-1 batch is NOT actually fully dispatch-ready right now; FT-3 dispatch would either (a) wait for 069r2 envelope drafting, or (b) dispatch without 069r2 (in which case it's not a "full batch")
- M4 alone IS dispatch-ready (m4_v0_ratification_template.md is pre-staged at 4 918 B with all substrate cites)
- Therefore FT-1/FT-4 is strictly faster on the M4 axis; M9 timeline unaffected per Q6

### Synthesizer judgment (this artifact)

**FT-4 wins on the operative facts.**

Rationale:
1. The disambiguator question favors FT-1/FT-4: the 069r2 envelope is NOT YET DRAFTED. Confirmed via inspection of `m_critical_path_2026-05-07.md` §3 (event-based: "069r2 envelope drafting pending synth turn-around").
2. FT-4 ≥ FT-1 dominance: FT-4 is FT-1 plus an explicit commitment to later LANE-1 catch-up, addressing the FT-3 advocates' concern about preserving the standard batched-absorption pattern. Net: no information lost, governance pattern preserved, M4 closure accelerated.
3. The 3-vote plurality (Copilot-Consult-01 + Gemini-implicit-via-FT-4 + Grok-close-to-FT-4) supports this resolution.
4. M9 timeline unaffected per Q6 unanimous → no opportunity cost from decoupling M4 from M6.CC at the agent-tier.

---

## §4. Recommended action chain

```
EVENT(operator dispatches m4_v0_ratification_template.md to single peer-AI)
   ↓
EVENT(peer-AI returns M4 V0 ratification signature on §3 + §6 of template)
   ↓
EVENT(operator absorbs ratification → SQL cascade: M4 row → done; M7/M8a/M8b: blocked → pending)
   ↓
EVENT(M4 V0 CLOSED) ✓
   ↓
[parallel — does not block M4 closure]
   ↓
EVENT(synth turn-around drafts 069r2 Path γ envelope inside next LANE-1 cycle)
   ↓
EVENT(operator dispatches lane1_batch_packet_w21.md WITH 069r2 envelope)
   ↓
EVENT(synth returns LANE-1 batch verdicts: M6.CC R1 + 102/103 absorption + 069r2 GO/NO_GO)
   ↓
EVENT(operator absorbs batch)
   ↓
[if 069r2 GO]
   ↓
EVENT(operator dispatches 058 main-fire-V3 for M6.CC R1)
   ↓
EVENT(M6.CC ratification)
   ↓
[M4 + M6.CC both closed]
   ↓
EVENT(operator deposits M9 V0 to Zenodo via 103 templates)
   ↓
EVENT(M9 V0 CLOSED) ✓
```

---

## §5. Ancillary recommendations

| Item | Source | Priority |
|---|---|:---:|
| Draft SIARC tie-break protocol for FT-2 multi-consultant cases | Claude web Q3 + Claude xhigh CLI Q3 | LOW |
| Confirm 069r2 envelope drafting belongs in next LANE-1 batch (vs separate fire) | FT-3 vs FT-4 disambiguation §3 | RESOLVED — bundle in LANE-1 |
| Single peer-AI choice for M4 solo ratification dispatch | implicit in FT-1/FT-4 path | OPERATOR DECIDES (any rotated peer-AI from existing roster) |
| Cross-check m4_v0_ratification_template.md §3 substrate cite SHAs immediately before dispatch | standard prudence | OPERATOR PRE-FLIGHT |

---

## §6. Forbidden-verb compliance

This synthesis is meta-governance prose (verb-list-as-data + checklist meta-references exempt per 098-J3 / 075-J2 precedent). Phase D scan: 0 substrate-prose hits where forbidden verbs appear in claim/prediction context.

---

## §7. Operator-actionable outputs

1. **Decision rendered**: Earliest M4 V0 close path is **FT-4** (M4 solo ratification + later LANE-1 catch-up).
2. **Next operator action**: Dispatch `tex/submitted/control center/m4_v0_ratification_template.md` to a single peer-AI for synth-tier signature on §3 (substrate cite verification) + §6 (ratification declaration).
3. **No agent-tier fire required** for M4 closure; substrate work is complete.
4. **Subsequent LANE-1 batch** carries M6.CC R1 + 102/103 absorption + 069r2 envelope (drafted by synth inside the batch).
5. **M9 V0 deposit** remains gated on M6.CC R1 (cannot be accelerated by M4 fast-track per Q6 unanimous).
