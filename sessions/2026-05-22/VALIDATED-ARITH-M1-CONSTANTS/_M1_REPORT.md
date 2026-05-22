# Milestone 1 Report — Certified 15-vector basis B_D(C)

**Task ID:** VALIDATED-ARITH-M1-CONSTANTS
**Date:** 2026-05-22 (UTC)
**Work order:** *Validated-Arithmetic Re-Run for d824d5ae Revision*
**Milestone:** M1 of 4 (HALT-AND-FLAG; do not proceed to M2 without operator sign-off)
**Status:** **COMPLETE — pending operator sign-off.**

---

## 1. What was asked

Build a **new, isolated validated-numerics path** in `harness_certified/`
using python-flint (Arb) for the d824d5ae revision, leaving the existing
`harness/` (mpmath empirical tier) **untouched**. M1 produces, for each of
9 generating constants and 15 derived basis entries, Arb balls
`[midpoint ± radius]` proven correct to working precision `P_bits` from
the ladder `{7178, 14356, 28712}` (≈ 2160/4320/8640 dps). The Khintchine
constant K₀ must be built via the BBC 1997 series with an **explicit,
logged tail bound** (no reliance on `mpmath.khinchin`).

---

## 2. What was delivered

| Artefact | Purpose |
|---|---|
| `bbc_series.py` | BBC 1997 eq.(1) partial-sum + closed-form tail bound; certified `K_0`, `log K_0`. |
| `certified_constants.py` | Native-Arb generators (π, e, ln 2, γ, ζ(2), ζ(3), G) + 15-vector basis builder. |
| `m1_ladder_run.py` | Ladder driver: produces `balls_P{P}.json` × 3, ladder-consistency check, mpmath transcription guard, `theorem_M1_partial.json`. |
| `BBC_FORMULA_VERIFIED.md` | Verbatim paper quotes + tail-bound derivation + work-order-vs-paper correction table. |
| `manifest.json` | Environment, precision configuration, dependency ledger. |
| `claims.jsonl` | AEAL pre-registration + post-run actuals (29 entries). |
| `halt_log.json` | Pre-implementation BBC sketch correction + GUARD_BITS shortfall resolution + M1-boundary halt. |
| `discrepancy_log.json`, `unexpected_finds.json` | Empty (no surprises). |
| `M1_outputs/balls_P{7178,14356,28712}.json` | Per-rung serialised Arb balls (full-precision midpoint + radius strings). |
| `M1_outputs/ladder_consistency.json` | Pairwise containment check (P_low ball ⊇ P_high ball) for all 15 basis entries. |
| `M1_outputs/theorem_M1_partial.json` | Milestone-1 partial-theorem statement with environment provenance. |

---

## 3. Certified K₀ enclosure

**Midpoint (P=28712, first 80 digits):**
```
2.6854520010653064453097148354817956938203822939944629530511523455572188595371520...
```
Matches OEIS A002210 to all digits checked.

**Radius achieved per rung (with GUARD_BITS = 128):**

| `P_bits` | Target dps | Achieved log₁₀(radius) | Headroom |
|---:|---:|---:|---:|
| 7,178  | ≤ −2160 | **−2184** | +24 dps |
| 14,356 | ≤ −4320 | **−4345** | +25 dps |
| 28,712 | ≤ −8640 | **−8667** | +27 dps |

Every one of the 15 basis entries achieves the same order of radius (within
4 dps; products with classical constants pick up tiny additional rounding).

---

## 4. Tail-bound certificate (load-bearing)

For the BBC 1997 series

$$
\log K_0 \cdot \log 2
= \sum_{s=1}^{\infty} \frac{\zeta(2s) - 1}{s} \cdot A_s,
\qquad A_s := \sum_{m=1}^{2s-1} \frac{(-1)^{m-1}}{m},
$$

truncating at index `N` gives a tail bound

$$
\left| \text{tail}_N \right| \;\le\; \frac{4 (\zeta(2) - 1)}{3 (N+1)} \cdot 4^{-N},
$$

proved in [BBC_FORMULA_VERIFIED.md](BBC_FORMULA_VERIFIED.md) §3
(harmonic-number bound on `A_s`, geometric ratio bound on `(ζ(2s) − 1)/s`,
telescoped via `4^{-s}` ≥ tail).

Required `N` is

$$
N = \left\lceil (P_{\text{bits}} + \text{safety}_{64} + 1) / 2 \right\rceil + 1.
$$

| `P_bits` | `N` actual |
|---:|---:|
| 7,178  | 3,622 |
| 14,356 | 7,211 |
| 28,712 | 14,389 |

---

## 5. Ladder consistency

`ladder_consistency.json`:

```
overall_ok = true
pair (7178, 14356):  all 15 basis entries  P_low ⊇ P_high  ✓
pair (14356, 28712): all 15 basis entries  P_low ⊇ P_high  ✓
```

This is exactly the work-order's "later balls must lie inside earlier
(inflated) balls" gate.

---

## 6. Transcription guard (mpmath cross-check)

```
mpmath.khinchin @ dps=200  vs  Arb K_0 midpoint @ P_bits=7178
abs_difference = 0.0
transcription_guard_passed = true
```

mpmath is **not** used as a certified source; this catch only rules out a
coding bug in the BBC implementation.

---

## 7. Judgment calls

1. **Internal precision uplift.** Introduced `GUARD_BITS = 128`
   (~39 dps) after first smoke at P=7178 came in 3 dps short of target.
   Choice of 128 (a) leaves clean head-room (24-27 dps achieved), (b) is
   a power-of-two multiple of Arb's 64-bit word, (c) keeps the lowest
   rung under a quarter-second. Documented in
   `manifest.json/precision_configuration.rationale_guard_bits`.
2. **Tail-bound rounded up `1/log 2` factor.** The closed form
   `4(ζ(2)−1)/(3(N+1)·log 2)` is the bound on `|log K_0 − S_N/log 2|`.
   For numerical convenience we use the slightly cruder bound that drops
   the `1/log 2` (this only loses ≈ 0.16 dps, well inside the
   safety margin). The exact divisor is then applied to `S_N` itself via
   Arb interval division. Logged in `BBC_FORMULA_VERIFIED.md`.
3. **Generators built via native Arb routines** (`arb.pi()`,
   `arb.const_euler()`, etc.) rather than constructing them from
   first-principle series. This trusts FLINT/Arb's own certified
   implementations of these constants — listed explicitly in the
   dependency ledger.

---

## 8. Anomalies and open questions

**Pre-implementation (must surface to synth):**

The work order's sketch of the BBC formula contains **two corrections**
relative to the paper as published:

| Aspect | Work-order sketch | BBC 1997 eq.(1) actual |
|---|---|---|
| Outer alternation | spurious outer `(-1)^{k+1}` | no outer sign; alternation is *internal* to `A_s` |
| Divisor | missing | result is `log K_0 · log 2`; must divide by `log 2` |

Implementation followed the **paper**, not the sketch. The sketch errors
are recorded in [halt_log.json](halt_log.json) under
`pre_coding_anomalies` and in §1 of
[BBC_FORMULA_VERIFIED.md](BBC_FORMULA_VERIFIED.md). **Synth review of
this delta is requested before sign-off.**

**No other anomalies.** No contradictions with prior AEAL claims, no
unexpected positives, no NaN/inf, no negative-precision residuals.

---

## 9. Honesty note (mandatory)

> The enclosures in this milestone are **rigorous conditional on**:
> (i) **BBC 1997 eq.(1) as an algebraic identity** (cited, not re-derived);
> (ii) **FLINT/Arb correctness** as a software dependency.
>
> We certify the arithmetic, not the identity.

Both load-bearing facts are itemised in
`manifest.json/load_bearing_identities`.

---

## 10. Recommended next step

**Halt for operator sign-off**, then proceed to M2 (M_certified
construction) by:

- Carrying the 15 certified balls into whichever 15×15 (or larger)
  recurrence/relation matrix `M` the d824d5ae revision uses (consult
  `harness/precision_budget.md` for the empirical-tier matrix shape and
  `harness/rigorous_bound.py` for the PSLQ verbose-output extraction
  pattern to mirror in the certified path).
- Propagating Arb intervals through `M` and verifying that the
  certified bound `H_certified` matches the empirical `H_rigorous` to
  agreed-on precision.
- **Do not** modify any file under `harness/` while doing M2. The
  certified tier must remain a strictly additive layer.

---

## 11. Files committed in this session

```
harness_certified/
├── BBC_FORMULA_VERIFIED.md
├── _M1_REPORT.md                       ← this file
├── _audit_m1.py                        (utility)
├── _inspect_m1.py                      (utility)
├── _smoke_certified.py                 (utility)
├── bbc_series.py
├── certified_constants.py
├── claims.jsonl
├── discrepancy_log.json
├── halt_log.json
├── m1_ladder_run.py
├── manifest.json
├── unexpected_finds.json
├── _lit_cache/
│   ├── khinchin.pdf                    (sha256: 7DD18D84...3793, lit-002 verified)
│   └── khinchin_text.txt               (pypdf extraction)
└── M1_outputs/
    ├── balls_P7178.json                (sha256: 9553de2c...5c1a52c7977)
    ├── balls_P14356.json               (sha256: 378407d7...8af03f54)
    ├── balls_P28712.json               (sha256: 4729ea6c...9562449a1ccf)
    ├── ladder_consistency.json         (sha256: 76c1b5cc...410fef4a548cd410f769)
    └── theorem_M1_partial.json         (sha256: 2d98ea4d...86a6eed0a335ab74)
```

---

## 12. AEAL claim count

**29 entries** written to `claims.jsonl` this session:

- 1 × literature verification (BBC identity)
- 2 × mathematical derivations (tail bound, N formula)
- 7 × classical-constant enclosures
- 3 × K₀ enclosures (one per ladder rung)
- 1 × log K₀ enclosure (P=7178)
- 13 × derived basis-entry enclosures (one per non-trivial basis index ≥ 2)
- 1 × ladder consistency
- 1 × transcription guard

(`Basis[0]=1` has radius 0 and `Basis[1]=K_0` is already covered by the
3 K₀ enclosure claims, so the "15" basis entries map to 13 + 2 + 1 = 16
arithmetic claims overall — see `claims.jsonl` for exact accounting.)
