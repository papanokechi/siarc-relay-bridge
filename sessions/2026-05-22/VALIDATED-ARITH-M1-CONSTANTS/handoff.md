# Handoff — VALIDATED-ARITH-M1-CONSTANTS

**Date:** 2026-05-22
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7)
**Session duration:** ~75 minutes (incl. literature pre-flight, tail-bound proof, implementation, ladder run, AEAL, reporting)
**Status:** COMPLETE — halt-and-flag at M1 boundary; awaiting operator sign-off before M2.

## What was accomplished

Built a **brand-new, isolated validated-numerics path** at
`siarc/unsolved-relay-staging/harness_certified/` using python-flint
(FLINT 3.3.1, Arb) for the d824d5ae revision. Milestone 1 delivers the
15-vector certified basis $B_D(\mathcal C)$ for $D=6$,
$\mathcal C = \{\pi, e, \ln 2, \gamma, \zeta(2), \zeta(3), G\}$, as
Arb balls `[midpoint ± radius]` at the precision ladder
`P_bits ∈ {7178, 14356, 28712}` (≈ 2161/4322/8643 dps). The Khintchine
constant $K_0$ is built rigorously from the BBC 1997 eq.(1) series with
an explicit, paper-verified, closed-form tail bound; **no reliance on
`mpmath.khinchin`** in the certified path. The existing mpmath
`harness/` empirical tier is **untouched** (strict additivity).

## Key numerical findings

- **$K_0$ enclosure midpoint (P=28712, first 80 dps):**
  `2.6854520010653064453097148354817956938203822939944629530511523455572188595371520`
  — matches OEIS A002210 to all certified digits.
- **Achieved radii (with `GUARD_BITS = 128`):**
  | `P_bits` | $\log_{10}(\text{rad}(K_0))$ | Target | Headroom |
  |---:|---:|---:|---:|
  | 7,178  | **−2184** | −2160 | +24 dps |
  | 14,356 | **−4345** | −4320 | +25 dps |
  | 28,712 | **−8667** | −8640 | +27 dps |
  Script: `m1_ladder_run.py` and `certified_constants.py`.
- **Tail bound (script: `bbc_series.py`):**
  $\lvert \text{tail}_N \rvert \le \tfrac{4(\zeta(2)-1)}{3(N+1)} \cdot 4^{-N}$,
  giving `N = ceil((P_bits + 64 + 1)/2) + 1` → `N ∈ {3622, 7211, 14389}`.
- **Ladder consistency** (script: `m1_ladder_run.py`): all 15 basis
  entries satisfy `ball@P_low ⊇ ball@P_high` for both pairs
  `(7178,14356)` and `(14356,28712)` → `overall_ok = true`.
- **Transcription guard** (script: `m1_ladder_run.py`):
  `mpmath.khinchin @ dps=200` vs Arb `K_0` midpoint @ `P_bits=7178`:
  `abs_difference = 0.0` (passes). mpmath used **only** as a coding-bug
  detector, not as a certified source.
- **AEAL count:** 29 entries written to `claims.jsonl` (1 lit-verify,
  2 derivations, 7 classical, 3 K₀ rungs, 1 log K₀, 13 derived basis,
  1 ladder, 1 transcription guard).

## Judgment calls made

1. **`GUARD_BITS = 128` internal-precision uplift.** First smoke at
   P=7178 came in 3 dps short of target due to Arb rounding accumulated
   across ~3700 series terms + 15 product compositions. Added 128 bits
   (~39 dps) of internal head-room — a power-of-two multiple of Arb's
   64-bit word, leaving ~25 dps clean head-room across the ladder and
   keeping the lowest rung under 0.25 s. Rationale recorded in
   `manifest.json/precision_configuration.rationale_guard_bits`.
2. **Tail bound's `1/log 2` divisor handled at the integer-bound step.**
   The strict bound is
   $4(\zeta(2)-1)/(3(N+1)\log 2)\cdot 4^{-N}$, but for the
   integer-precision N-selection we dropped the `1/log 2` factor
   (loses ~0.16 dps, well inside the safety margin). The actual division
   by `log 2` is performed via Arb interval arithmetic on `S_N`
   itself. Both forms are spelled out in `BBC_FORMULA_VERIFIED.md` §3.
3. **Classical constants via native Arb routines** (`arb.pi()`,
   `arb.const_euler()`, `arb(s).zeta()`, `arb.const_catalan()`, etc.)
   rather than open-coded series. This trusts FLINT/Arb's own
   certified constant implementations — listed explicitly in the
   dependency ledger (`manifest.json/load_bearing_identities`).

## Anomalies and open questions

### Load-bearing: work-order vs. paper BBC-formula sketch delta

The work order's sketch of BBC 1997 eq.(1) contained **two corrections**
relative to the paper:

| Aspect | Work-order sketch | BBC 1997 eq.(1) as written |
|---|---|---|
| Outer alternating factor | spurious outer `(-1)^{k+1}` | no outer sign; alternation is internal to $A_s$ via $(-1)^{m-1}$ |
| `1/log 2` divisor | missing | identity is for $\log K_0 \cdot \log 2$; must divide by $\log 2$ |

I implemented the **paper** form, not the sketch. Both deltas are
documented in `BBC_FORMULA_VERIFIED.md` §1 (the verification artefact)
and in `halt_log.json/pre_coding_anomalies`. **Synth review of these
deltas is requested before any M2 sign-off**, because if my reading of
the work-order sketch was correct, then the work-order author was
writing in a different normalisation that should be reconciled in the
M2 problem statement.

### No other anomalies

No contradictions with prior AEAL claims. No unexpected positives. No
NaN/inf, no negative-precision residuals. Ladder fully consistent.

## What would have been asked (if bidirectional)

1. Is the work-order's BBC-sketch normalisation a deliberate
   alternative-form (e.g. some rearrangement that absorbs the `1/log 2`
   into a different normalisation of $A_s$) that I should adopt
   instead of the paper-verbatim form? If yes, please point at the
   source so I can re-derive my tail bound under that normalisation.
2. Is `GUARD_BITS = 128` acceptable, or do you prefer it to grow with
   $P_{\text{bits}}$ (e.g. $\text{GUARD} = c \cdot \log_2(N)$ for some
   small constant $c$)? Current choice is constant; this becomes
   marginal if M3/M4 push the ladder above $P_{\text{bits}} = 10^5$.
3. For M2, do I substitute the certified balls into
   `harness/precision_budget.md`'s 15×15 (or other) `M` matrix as-is, or
   does the d824d5ae revision change the matrix shape in a way that
   needs to be reconciled first?

## Recommended next step

Operator sign-off on this M1 deliverable, with explicit confirmation on
the BBC-sketch delta resolution. Then proceed to **M2 — `M_certified`
construction**: lift the 15 certified balls into whichever recurrence /
relation matrix carries the d824d5ae revision's signature, propagate
intervals via Arb matrix arithmetic, and verify `H_certified` matches
the empirical `H_rigorous` from
`harness/rigorous_bound.py` to agreed precision. Do **not** modify
`harness/` during M2 — the certified path must remain a strictly
additive layer.

## Files committed

```
sessions/2026-05-22/VALIDATED-ARITH-M1-CONSTANTS/
├── _M1_REPORT.md                       (full milestone report)
├── BBC_FORMULA_VERIFIED.md             (paper verbatim + tail-bound proof + sketch delta)
├── bbc_series.py                       (BBC partial sum, tail bound, certified K_0)
├── certified_constants.py              (15-vector basis builder)
├── m1_ladder_run.py                    (ladder driver + consistency + xcheck)
├── _audit_m1.py                        (hash + radius audit utility)
├── manifest.json                       (env + precision config + dependency ledger)
├── claims.jsonl                        (29 AEAL entries)
├── halt_log.json                       (BBC sketch delta + M1-boundary halt)
├── discrepancy_log.json                (empty)
├── unexpected_finds.json               (empty)
├── handoff.md                          (this file)
├── _lit_cache/
│   ├── khinchin.pdf                    (BBC 1997, sha256 7DD18D84...3793, lit-002)
│   └── khinchin_text.txt               (pypdf extraction)
└── M1_outputs/
    ├── balls_P7178.json                (sha256 9553de2c...c7977)
    ├── balls_P14356.json               (sha256 378407d7...3f54)
    ├── balls_P28712.json               (sha256 4729ea6c...1ccf)
    ├── ladder_consistency.json         (sha256 76c1b5cc...9f769)
    └── theorem_M1_partial.json         (sha256 2d98ea4d...ab74)
```

## AEAL claim count

**29** entries written to `claims.jsonl` this session.
