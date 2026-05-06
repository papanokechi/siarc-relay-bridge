# LANE-2 meta-verdict on synth-substitute deliverable — STEP 6

**Reviewer:** Copilot Researcher Agent (canonical T1-Synth-SUBSTITUTE-LANE-2).
**Date:** 2026-05-06 W19 Wed JST.
**Subject:** synth-substitute verdict at bridge `df7d6d4`,
`sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/synth_substitute_verdict.md`
(SHA-256 anchor A1: `AE5CC42A...A608B70A5798041F`).

---

## Meta-verdict

**`ACCEPT_WITH_REVISIONS`**.

The synth-substitute verdict is **substantively correct** in its
load-bearing findings (Q1 PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT;
Q2 GATED_BY_Q1_PIVOT; Q4 WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE;
the WZ derivation $A_{\rm naive} = 2d$ at deg_a = 0; the script-level
(1, b) $a_n \equiv 1$ identification). It is **not load-bearing-erroneous**
in any verifiable respect. However, LANE-2's independent investigation
surfaced **three substantive refinements** (P2, P3, P4 from the depth
probe + V5 finding) that should be folded into the canonical record
before the synth-substitute is adopted as the LANE-2-ratified ruling.

Therefore: **ACCEPT_WITH_REVISIONS**, with the three required revisions
listed below.

---

## Required revisions for canonical acceptance

### R1 — Scope expansion (P1 + V5/P3 substrate)

**Current synth-substitute scope:** "PCF-2 R1.1/R1.3/Q1 cubic+quartic
harvest scripts" (synth_substitute_verdict.md L74).

**LANE-2 required revision:** Expand scope to:

> "ALL of PCF-2's harvest pipeline (Sessions A2 + B + C1 + R1.1 + R1.2
> + R1.3 + Q1; 9 cf_value() implementations across pcf-research/pcf2/
> uniformly use the (1, b) recurrence with $a_n \equiv 1$, deg_a = 0)
> AND the PCF-1 v1.3 §6 Theorem 5 V_quad upper-branch row (per
> `algebraic_independence_audit.py` L37-40, V_quad uses $a(n) = 1$ at
> $d = 2$, yielding $A_{\rm naive} = 2d = 4$ via the WZ normal case
> deg_a = 0 row, NOT via the borderline mechanism (i') as currently
> attributed in `bt_baseline_note.tex` v1.0 §4.2 L481-487)."

**Substrate citation:** P1 (depth probe; 9 scripts uniform) + V5
(cf_value at audit script L37-40) + P3 (bt_baseline_note v1.0 §4.2
mechanism-(i') reattribution).

**Insertion point:** synth_substitute_verdict.md L74 (Q1 verdict label
scope) and L286-294 (Audited blind spots § Blind spot 1: PCF-1 may use
a different convention).

### R2 — Mismatch-locus wording refinement (P4 substrate)

**Current synth-substitute wording:** "protocol-to-stratum mismatch
between the program statement's declared stratum and the harvest-script-
implemented stratum" (synth_substitute_verdict.md L116-118).

**LANE-2 required revision:** Refine to:

> "Intra-`pcf2_program_statement.tex` mismatch between §3 setup
> (L228-234, declares $a_n = \delta_1 n + \delta_0$ with no $\delta_1
> \neq 0$ restriction) and §6 B4 wording (L457, uses verbatim 'PCF
> $(1, b)$' notation, implicitly fixing $a_n \equiv 1$). The harvest
> scripts implement §6 B4's stratum exactly; the inconsistency is
> between §3 and §6 within the SAME document, not between prose and
> scripts as the term 'protocol-to-stratum mismatch' might suggest."

**Substrate citation:** P4 (depth probe; verbatim "PCF $(1, b)$" notation
at L457 of pcf2_program_statement.tex).

**Insertion point:** synth_substitute_verdict.md L116-118 (Q1 finding
substrate-level paragraph) and L304-310 (Audited blind spots § Blind
spot 3: classifier vs protocol-to-stratum).

### R3 — Phase A baseline framing (P2 substrate)

**Current synth-substitute framing:** Phase A's omission of deg_a = 0
is acknowledged implicitly via the `deg_a ∈ {d-1, d, d+1}` band
language, but the substrate-level mechanism (Phase A WZ table excludes
the deg_a = 0 row by ASSUMPTION via its three-convention enumeration)
is not stated as a primary finding.

**LANE-2 required revision:** Add a paragraph:

> "Phase A's WZ table at `phase_a_summary.md` L34-44 enumerates THREE
> SIARC conventions ($\alpha$/symmetric/$\delta$-direction) corresponding
> to deg_a $\in \{d-1, d, d+1\}$. The deg_a = 0 row was excluded by
> ASSUMPTION via this three-convention framing, not by oversight.
> Phase D's 'structural gap' verdict (gap framing of $A_{\rm fit} \approx 2d$
> vs $A_{\rm naive} \in \{1, 2, 3\}$ at $d=2$ etc.) is the proximate
> consequence of this assumption. Adding the deg_a = 0 row
> ($\mu_{\rm dom} = d$, $\mu_{\rm sub} = -d$, $A_{\rm naive} = 2d$,
> $\gamma_{\rm sub} \propto -c_a/c_b$) closes the d=2 V_quad anomaly,
> the d=3 R1.1+B+C1 110/110 record, and the d=4 Q1 60/60 record
> simultaneously, WITHOUT invoking borderline mechanism (i') or
> exceptional locus (ii')."

**Substrate citation:** P2 (depth probe; Phase A table extension verbatim).

**Insertion point:** synth_substitute_verdict.md L116-145 (Q1 finding
analytic-level paragraph) — append after the existing Balance (I)/(II)/(III)
enumeration.

---

## Substrate basis for ACCEPT_WITH_REVISIONS

### Independent substrate verifications V1-V6 (all PASS)

- **V1**: cf_value() at session_c1_wkb.py L78-86 implements canonical (1, b)
  CF with $a_n \equiv 1$. Synth-substitute claim independently confirmed.
- **V2**: same recurrence at session_b_pslq.py L162-170 + quartic_tail_fit_all60.py
  L21-30. Uniform across all 3 scripts cited by synth-substitute.
- **V3**: pcf2_program_statement.tex L228-234 declares
  $a_n = \delta_1 n + \delta_0$ without $\delta_1 \neq 0$. Synth-substitute
  claim "deg_a = 1 declared" is correct in spirit but slightly imprecise:
  declared scope is deg_a $\in \{0, 1\}$ formally, with deg_a = 0 as a
  corner of the declared scope.
- **V4**: p12_journal_main.tex L124-131 PCF-1 d=2 stratum imposes
  $\delta \neq 0$ strictly. Synth-substitute distinction PCF-1 vs PCF-2
  asymmetry confirmed.
- **V5**: V_quad uses $a(n) = 1$ (deg_a = 0). Synth-substitute SYNTH-SUB-051-UF2
  observation independently confirmed; LANE-2 elevates this from "secondary
  observation flagged for canonical T1-Synth follow-up" to a substantive
  scope-expansion finding (R1).
- **V6**: Independent WZ derivation yields $A_{\rm naive} = 2d - d_a$;
  for deg_a = 0, $A_{\rm naive} = 2d$ uniform. Sign $\gamma_{\rm sub}
  \propto -c_a/c_b$ confirmed at leading order. Both the magnitude
  ($A_{\rm naive} = 2d$) and the rubber-duck-corrected sign verified.

### Rubber-duck adoption audit (8/8 ADOPTED_AND_LANDED)

- C1, C2, C3, C4, C5, C7, C8: substantive revisions all landed verbatim.
- C6 (AEAL forbidden-verb hygiene): zero violations in prediction-or-
  conjecture context (3 grep matches all in ACCEPTABLE contexts:
  conditional logic, factual mechanical match, meta-discussion).

### Independent depth probe P1-P4 (substantive refinements R1, R2, R3 surfaced)

- **P1**: full coverage sweep — 9 cf_value() implementations uniform on
  (1, b). NOT contradicting synth-substitute; STRENGTHENING C1.
- **P2**: Phase A baseline framing → R3.
- **P3**: V_quad scope expansion → R1.
- **P4**: intra-document mismatch locus → R2.

---

## Why not ACCEPT_AS_CANONICAL?

Three substantive refinements (R1, R2, R3) extend the synth-substitute's
findings beyond its stated scope. Adopting the synth-substitute verbatim
as canonical would leave:

1. The PCF-1 V_quad reinterpretation (R1) under-acknowledged (synth-substitute
   flags it as "secondary observation ... flagged for canonical T1-Synth
   follow-up at next ISO week", L292-294, not folded into the verdict scope).
2. The mismatch locus framing (R2) inaccurate (the synth-substitute's
   "prose vs scripts" wording is misleading; the issue is intra-document).
3. The Phase A baseline framing (R3) under-explained (Phase D's "structural
   gap" verdict is a downstream consequence of Phase A's deg_a = 0 omission;
   without R3, the verdict appears more surprising than it is).

## Why not REJECT_AND_REPLACE?

The synth-substitute's load-bearing claims are substantively correct:

- The script-level (1, b) $a_n \equiv 1$ identification is FACTUALLY
  CORRECT (V1 + V2 + P1 confirm).
- The WZ derivation $A_{\rm naive} = 2d$ at deg_a = 0 is FACTUALLY
  CORRECT (V6 confirms with independent derivation).
- The Q4 ranking (Wasow canonical / Costin operational substitute) is
  ACCEPTABLE (no LANE-2 substrate evidence to dispute).
- The C2-corrected sign $\gamma_{\rm sub} = -c_a/c_b$ is CORRECT
  (V6 confirms via recessive-root analysis).

There are no load-bearing errors that would disqualify the verdict.
The 8/8 rubber-duck findings are all ADOPTED_AND_LANDED. AEAL
forbidden-verb hygiene is clean (C6 PASS).

REJECT_AND_REPLACE would force LANE-2 to draft a replacement verdict
body from scratch, which is unwarranted given the synth-substitute's
substrate-grounded core findings. ACCEPT_WITH_REVISIONS is the
correct meta-verdict because the three required revisions (R1, R2,
R3) are EXTENSIONS, not replacements.

---

## Independence-floor citation

This LANE-2 meta-verdict cites the following INDEPENDENT findings (V1-V6
or P1-P6) as substrate, satisfying the relay 061 prompt's
INDEPENDENCE_FLOOR_AND_ANCHORING-BIAS_GUARD requirement:

- **R1 substrate:** P1 (depth probe; 9 scripts uniform) + V5 (V_quad
  declaration) + P3 (V_quad scope expansion).
- **R2 substrate:** P4 (intra-document mismatch locus; verbatim "PCF (1, b)"
  notation at pcf2_program_statement.tex L457).
- **R3 substrate:** P2 (Phase A baseline framing; deg_a = 0 row exclusion
  by assumption; closure of d=2/3/4 anomalies via one-row extension).

All three required revisions are grounded in INDEPENDENT findings, not
in rubber-duck adoption confirmations. **Independence floor satisfied.**

---

## Halt status

- **HALT_061_REJECT_AND_REPLACE_WITHOUT_DRAFT**: does NOT trigger
  (LANE-2 meta-verdict is ACCEPT_WITH_REVISIONS, not REJECT_AND_REPLACE;
  draft replacement not required).
- **HALT_061_AEAL_FORBIDDEN_VERB_FOUND**: does NOT trigger (C6 PASS;
  zero forbidden verbs in prediction-or-conjecture context).
- **HALT_061_V1_CONTRADICTS / V3_CONTRADICTS / V6_CONTRADICTS**: do NOT
  trigger (V1, V3, V6 all confirm synth-substitute's substrate claims;
  V3 finding is a slight refinement, not a contradiction).
- **HALT_061_DOI_HALLUCINATION**: does NOT trigger (LANE-2 review cites
  no NEW DOI or arXiv-ID acquisition targets; existing AEAL-logged
  citations are exempt).
- **HALT_061_M6_TOKEN_OVERREACH**: does NOT trigger (no bare M6 tokens
  in any LANE-2 deliverable).

**No halts triggered in this LANE-2 review.**
