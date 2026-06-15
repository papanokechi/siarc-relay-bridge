# Outline lock — VQUAD-PERIODREP-PAPER-001

**Slot:** VQUAD-PERIODREP-PAPER-001 · **Date:** 2026-06-15 · **Stage:** 1 (outline lock)
**Working title:** *An Explicit Exponential-Period Representation of the V_quad Connection
Coefficient*
**Source probe:** PERIOD-REP-VQUAD-003 (verdict VERIFIED) + parents 001/002.

---

## 1.1 Comparison to PERIOD-REP-VQUAD-003 `paper-outline.md`

The probe's Stage-7 sketch had **8 sections, 20–25 pp**. The task brief specifies a
**9-section, 25–30 pp** structure (splitting the probe's §6 "Galois + transcendence" into a
self-contained **§6 Fresán–Jossen application** and pulling the differential-Galois material
forward into **§2/§5**, and giving **§7 Discussion**, **§8 Appendix**, **§9 References** their
own headers). **Divergences, all in favour of the task brief:**

| item | probe sketch | locked (task brief) |
|---|---|---|
| section count | 8 | **9** (adds explicit References as §9; Discussion and Appendix split out) |
| Galois placement | bundled in §6 | **L_φ SL(2) in §2.3; G_V in §5.3/§6; full Kovacic run in §A.2** |
| Method-A convention enum. | §5.1 main text | **moved to §A.4** (per task 2.5) |
| finite-resurgence theorem | §2 bullet | **its own §2 subsection** (task §2) |
| target length | 20–25 pp | **25–30 pp** |

No mathematical content changes; only reorganisation and one added appendix (A.4).

## 1.2 Operator framing choices (defaults applied)

| choice | default | **locked** |
|---|---|---|
| one-paper vs two | ONE | **ONE** (single paper: integral identity + three verifications + conditional transcendence) |
| conditional vs integral lead | INTEGRAL LEAD | **INTEGRAL LEAD** — the headline is the *unconditional, verified* identity C = (\|Γ(β)\|/2π)∫_γ e^ξ B̂ dξ; conditional transcendence is a clearly-flagged corollary |
| Sakai context depth | STANDALONE-WITH-REFERENCE | **STANDALONE-WITH-REFERENCE** — define every object in-paper (L_φ, L_V, γ, B̂, M); cite the Sakai Stratification deposit for the program frame but do not require it |

These are the task defaults; no operator override was supplied, so they are locked as-is
(autopilot: decide and proceed).

## 1.3 Locked structure (9 sections, 25–30 pp)

- **§1 Introduction** (2–3 pp): V_quad PCF `1 + K_{n≥1} 1/(3n²+n+1)`; the coefficient C;
  Sakai frame (brief); main theorem; conditional-transcendence corollary (both
  conditionalities flagged: FJ Conj. 1.3.2 **and** G-MOTGALOIS); roadmap; CAS/SOTA paragraph.
- **§2 The operators L_φ and L_V** (5–7 pp): explicit L_φ (ord 2, deg 4, ℚ(√3)); singular
  structure/exponents; **SL(2) by Kovacic** (cert → §A.2); explicit L_V (ord 4, deg 2);
  Borel construction; singular locus {0 apparent, −2/√3 branch, ∞ irreg slope 1};
  **finite-resurgence corollary** (holonomicity ⇒ finite locus).
- **§3 The rapid-decay cycle γ** (3–4 pp): Hankel thimble; FJ relative homology H₁^{rd};
  rapid-decay verification; FJ class compatibility.
- **§4 The main theorem** (2–3 pp): statement; Γ(β) from the branch; K ↔ S = 2πK;
  ~46-digit numerics.
- **§5 Three verifications** (6–8 pp): §5.1 differential-equation (M = h(z)·L_φ); §5.2
  Borel–Laplace/Hankel; §5.3 Stokes-data; §5.4 cross-verification.
- **§6 Application to Fresán–Jossen** (3–4 pp): framework recall; application; **G-MOTGALOIS**
  acknowledgment; conditional transcendence (two conditionalities).
- **§7 Discussion** (2–3 pp): Sakai Part (ii)(a) d=2 completion; d≥3 program; Ramanujan
  Machine / CMF positioning; open problems; CAS comparison.
- **§8 Appendix** (4–6 pp): A.1 full coefficients; A.2 Kovacic run; A.3 numerical logs;
  A.4 four-convention enumeration; A.5 reproducibility statement.
- **§9 References**: V_quad deposit (Zenodo 20455090), Sakai Stratification deposit,
  Fresán–Jossen *Exponential Motives* (expmot.pdf), Kovacic 1986, van der Put–Singer,
  Hien 2009, Dingle/Berry–Howls/Écalle, etc.

**Total target: 25–30 pp; default class amsart** (no journal class — that is the VENUE-RELAY
downstream decision).

**Verdict 1: outline LOCKED (9 sections, integral-lead, standalone-with-reference, one paper).**
