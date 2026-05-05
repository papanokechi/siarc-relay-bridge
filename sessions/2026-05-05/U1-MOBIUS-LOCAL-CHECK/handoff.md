# Handoff — U1-MOBIUS-LOCAL-CHECK
**Date:** 2026-05-05
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes (incl. one halt-and-fix iteration)
**Status:** COMPLETE

## What was accomplished

Synth pre-authorized (2026-05-05 ~13:55 JST in synth comment block) a CLI-side
local Möbius/equivalence-transformation check on the U1 anomaly from
T2B-BIPARTITION-B6-VERIFICATION before any escalation. Synth's question was
"what KIND of equivalence" between the two PCFs, not "whether one exists" —
the PSLQ already showed both PCFs share the same numerical limit at 28-digit
dps=150.

CLI ran four tests (T1 high-precision reproduction, T2 classical equivalence
transformation, T3 Bauer-Muir constant-w cross-check, T4 structural
interpretation). Initial run hit a HALT condition due to a coefficient-order
convention error (assumed [a0,a1,a2] ascending; corrected to project-standard
[a2,a1,a0] LEADING-FIRST per standing instructions). After correction, T1
verified both PCFs converge to L = b(0) + K = 2/log(2) at dps=200, N=4000 with
|L_A - L_B| = 0 to machine precision. T2 ruled out classical equivalence
transformation. The synth-relevant answer is now characterized.

## Key numerical findings

- **PCF A** = (a_coeffs, b_coeffs) = ((-1, 0, 0), (6, 3)) →
  a(n) = -n², b(n) = 6n+3, b(0) = 3, ratio a₂/b₁² = -1/36 (off both loci)
  **K_A = -0.114609918222073185...**
  L_A = b(0) + K_A = 2.885390081777926814719849362... = 2/log(2) ✓
- **PCF B** = ((-8, 0, 0), (6, 4)) →
  a(n) = -8n², b(n) = 6n+4, b(0) = 4, ratio a₂/b₁² = -2/9 (= L⁻ locus)
  **K_B = -1.114609918222073185...**
  L_B = b(0) + K_B = 2.885390081777926814719849362... = 2/log(2) ✓
- **K_A − K_B = +1 exactly** (the b(0) shift exactly compensates the K shift).
- |L_A − L_B| = 0 at dps=200 (verified at script: u1_mobius_local_check.py).

### Equivalence-transformation test (T2)

Required for classical equivalence: ∃ sequence (r_n) with r_0 = 1 such that
  a_B(n) = r_n * r_{n−1} * a_A(n)  and  b_B(n) = r_n * b_A(n).

- a_B(n) / a_A(n) = -8n² / -n² = **8 (constant, OK)** → required r_n*r_{n−1} = 8.
- b_B(n) / b_A(n) = (6n+4)/(6n+3) → r_n = (6n+4)/(6n+3).
- Computed r_n*r_{n−1} for n=1..5: **1.481, 1.185, 1.117, 1.086, 1.068** —
  none equals 8.

→ **NO classical equivalence transformation links PCF A and PCF B.**

### Bauer-Muir cross-check (T3)

Bauer-Muir with constant w = −5 (chosen to match the b-coefficient shift)
yields a non-constant transformed numerator under the standard BM formula.
Deferred to synth turn if deeper investigation warranted (general
non-constant w_n requires solving an auxiliary recurrence).

## Synth answer (the original question)

> "I'll need the explicit PSLQ relation + the two PCF tuples + whatever
> Möbius-equivalence test CLI runs locally first. The synth-side question
> is what KIND of equivalence, not whether one exists (CLI's already shown
> it does)." — synth, 2026-05-05 ~13:55 JST

**Answer: LIMIT-LEVEL equivalence only.**

Both PCFs evaluate to L = b(0) + K = 2/log(2) via INDEPENDENT b(0) choices
(b(0)=3 for PCF A, b(0)=4 for PCF B) and K-values that differ by exactly 1
(K_A − K_B = +1). The K-parts have proportional a-numerators
(a_B(n) = 8 · a_A(n)) but the b-coefficient ratio
r_n = (6n+4)/(6n+3) does NOT yield r_n*r_{n−1} = 8 = a_B/a_A, so classical
equivalence transformation FAILS.

The two PCFs are NOT linked by sequence rescaling; they converge to the same
limit through complementary b(0)-offsets and proportional-but-not-equivalent
K-parts.

## Judgment calls made

1. **Coefficient-order convention HALT and recovery.** Initial script run
   gave T1 SEPARATION DETECTED (both L values nowhere near 2/log(2)). Per
   standing instructions HALT criterion ("any result contradicts a prior
   AEAL-logged claim"), I stopped, investigated, and traced the error to my
   own coefficient-order assumption. Standing instructions explicitly state
   "PCF family coefficients are stored as [a2, a1, a0] (leading coefficient
   first) throughout this project" — I had been treating tuples as
   [a0, a1, a2] ascending. Corrected to LEADING-FIRST. Also discovered the
   second convention point: project PCF limit is L = b(0) + K, not just K.
   Both fixes were required for T1 to reproduce 2/log(2). Recovery was clean
   (~5 minutes); deleted the bad AEAL claim from the first run before the
   second AEAL append.

2. **T3 deferred under non-constant w.** The general Bauer-Muir transform
   with non-constant w_n requires solving an auxiliary recurrence. Since T2
   already rules out the simpler classical-equivalence transformation, and
   T3 with constant w doesn't link the PCFs, I deferred deeper BM analysis
   to a synth turn rather than attempting a more involved local computation.
   This matches synth's stated framing: CLI runs *locally-tractable* tests
   first; structurally deeper questions go to synth.

3. **Discrepancy log.** No discrepancy_log.json written because the HALT was
   caught and recovered within this session, and the BIPARTITION_HOLDS
   AEAL claims (from yesterday's commit 1735258) remain valid. The first
   run's bad AEAL claim was deleted before re-append, so claims.jsonl
   contains only the corrected entry.

## Anomalies and open questions

**For synth review when this gets queued:**

1. **Why does b(0) + K give the same constant for both?** This is more
   than a numerical coincidence: K_A − K_B = +1 exactly, balancing the
   b(0) shift +1 between (-1,0,0,6,3) and (-8,0,0,6,4). Is this an
   instance of a known PCF identity (Brouncker-Euler-style) or a new
   structural feature of the F(2,4) Log stratum?

2. **Are there OTHER off-locus Log families that collide with on-locus ones
   via this same b(0)-offset mechanism?** A sweep at b₁=6 of all
   (a₂, a₁, a₀, b₁, b₀) with a-polynomial proportional to -n² and varied
   b₀ would clarify whether this is a generic feature or specific to the
   pair (-1,0,0,6,3) and (-8,0,0,6,4).

3. **General Bauer-Muir with non-constant w_n** (T3 deferred). If synth
   wants the deeper PCF-equivalence question pursued, the next step is to
   set up the auxiliary BM recurrence
     w_n + a_{n+1} / (b_{n+1} + w_{n+1}) = w_n + a'_n / b'_n
   and check whether a non-constant w_n solution exists linking PCF A to
   PCF B.

4. **Preprint v2 implication.** The preprint claim "all Log families at
   ratio -2/9" is technically narrow: it predicts the L⁻-locus structure
   for Trans, but the off-locus Log family (-1,0,0,6,3) at ratio -1/36
   evaluates to the same Log constant 2/log(2) as the on-locus
   representative. Synth may want to amend preprint v2 to either:
     (a) clarify the bipartition is on Trans-stratum families only (Log
         is unconstrained), OR
     (b) note the b(0)-offset Log collision as a structural feature, OR
     (c) introduce a finer Log-stratum bipartition.
   This is **not** a counterexample to BIPARTITION_HOLDS (which is a
   Trans-stratum verdict); it is a Log-stratum side-finding that may
   warrant amendment.

## What would have been asked (if bidirectional)

1. "Should I run a sweep over all b(0) values at b₁=6 to map the
   collision pattern more thoroughly?" (~30 min compute; would inform
   the synth turn directly.)

2. "Should I attempt the general non-constant-w_n Bauer-Muir, or is the
   T2 negative result enough to characterize the kind-of-equivalence?"

## Recommended next step

**Queue the U1 task for synth** with the following packet:
- This handoff
- u1_mobius_local_check_results.json
- u1_mobius_local_check_log.txt
- The structural observation that K_A − K_B = +1 exactly is suggestive of
  a deeper PCF identity, not just numerical coincidence

Synth-side questions to bring:
1. Is the b(0)-offset Log collision a known PCF phenomenon?
2. Should preprint v2 be amended (and how)?
3. Should a broader b(0) sweep be commissioned at b₁=6?

## Files committed

- `u1_mobius_local_check.py`           — main script (LEADING-FIRST + b(0)+K conventions documented inline)
- `u1_mobius_local_check_results.json` — full T1-T4 outcomes + synth answer
- `u1_mobius_local_check_log.txt`      — stdout transcript
- `claims.jsonl`                        — 1 AEAL claim (corrected; bad first-run claim deleted)
- `handoff.md`                          — this file

## AEAL claim count

1 entry written to claims.jsonl this session.

SHA-256 of canonical results JSON: `322b58293b0b1636ac18b42a54a543fe6a2cf016202b57764849fbb95d832b2a`
