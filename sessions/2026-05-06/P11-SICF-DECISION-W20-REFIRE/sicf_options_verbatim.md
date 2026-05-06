# SICF Four Options — Verbatim Extract

**Source-of-record:** `cli_log/2026-05-05.md`
**Substrate range:** L613–636 (four-options enumeration) + L687–689 (synth framing quote).
**Operator-approved substrate path** (this re-fire, 2026-05-06): see relay-049 P2 confirmation in `handoff.md` §"Judgment calls" J2.
**SICF run anchor** (auto-appended `claims.jsonl` line, 2026-05-05 ~12:58 JST):
  `SICF review of P11: advocate=8.6, critic=4.0, consensus=6.22, recommendation=Withdraw_and_resubmit`
  (sha256 `b3b339507ec0337e7217d426cacf0c64a9c94c37192ff76b813f6a3b750b3453`)

**Authoring-context flag (D3, inherited from 047 + prior 049 halt):** the four
options below were authored when CLI believed P11 was `under_review` at
*Mathematics of Computation*. CMB.txt L24/L59-60/L877-878 + 047
`P11-COVERLETTER-MATHCOMP-DEFENSIVE/handoff.md` L60-62 record that P11 was in
fact desk-rejected by Math.Comp on 2026-04-28 and resubmitted same day to
JTNB-2400 (handling editor: Boris Adamczewski). The verbatim text below uses
the original "Math of Comp" venue labelling; the post-correction interpretation
is maintained in `sicf_options_scoring_matrix.json` and discussed in
`sicf_decision.md`.

---

## §A — Four-options block (verbatim, cli_log/2026-05-05.md L606–636)

> P11 (F(2,4) base case) is currently `under_review` at Math of Comp. SICF
> verdict = Withdraw_and_resubmit, but submission is already in.
> **Realistic options:**
>
> 1. **No-op (wait for referee verdict).** If Math of Comp returns Reject, the
>    SICF analysis becomes the resubmission roadmap (4 fatal must-fix items).
>    Cost: zero. Risk: editor sees the same issues independently.
>
> 2. **Voluntary corrigendum.** Submit a 1-2 page corrigendum to Math of Comp
>    addressing #18 (2-family arithmetic discrepancy) since that's the one
>    hard error not requiring a full rewrite. Cost: ~1 day. Risk: signals
>    ongoing instability.
>
> 3. **Withdrawal + restructure.** Withdraw, address #1-#4 by reframing the
>    theorem statements as "T₁-relative" and the partition as "conditional
>    on basis-completeness", resubmit. Cost: 2-3 weeks. Risk: 1 month of
>    review queue restart.
>
> 4. **Hold for JTNB-2400 leverage.** The same content overlaps with the
>    JTNB submission (P11RT referee-response template covers similar
>    terrain). If JTNB referee raises any of the 4 SICF fatals, address all
>    four in one R1 response; if Math of Comp referee raises them
>    independently, the JTNB pipeline is harder to defend. Synth strategic
>    call.
>
> CLI **does not** auto-fire any of these; flagged for synth/operator decision.

---

## §B — Synthesizer framing quote (verbatim, cli_log/2026-05-05.md L687–689)

Synth-comment block timestamped 2026-05-05 ~13:55 JST, under heading
"Synth framing for the eventual P11 strategic call":

> "The right framing for that turn is: **which option preserves the most of
> the manuscript's structural contribution while honestly addressing the four
> fatals**, not which option gets to 'submission_ready=True' fastest. Those
> are different optimizations."

---

## §C — Four Critic fatals (verbatim, cli_log/2026-05-05.md L545–556)

The four fatals that any "addressing" option must reckon with:

> 1. **Fatal:** Operational convergence test (Def 2.3) is heuristic; "exact
>    counts" 513,387 / 400,093 / 24 not mathematically certified.
> 2. **Fatal:** `Desert` definition is "no PSLQ relation found at dps=500,
>    H_max=10¹²" — algorithm- and precision-dependent negative statement,
>    not a mathematical property; Theorem 4.1 is a computational report.
> 3. **Fatal:** `Rat ⊔ Log ⊔ Alg ⊔ Trans ⊔ Des` partition is basis-restricted
>    (Alg ≤ degree 4, Log finite list, Trans = T₁={1,K,π,Kπ,π²});
>    "completeness" reduces to "no relation in this finite basis", not
>    exhaustive arithmetic classification.
> 4. **Fatal:** Proposition 5.2 (Möbius identification
>    `K = -(c₀+c₂π)/(c₁+c₃π)`) is justified only by ~10⁻²³⁸ numerical
>    agreement; Theorem 5.3 transcendence proof is conditional on an
>    unproved exact identity.

Plus a hard arithmetic Minor #18:

> Theorem 4.1 says 400,119 non-Rat convergent families and 400,093 Desert,
> leaving **26 non-Desert non-Rat** — but the partition lists 24 Trans + 0 Log
> + 0 Alg = 24 → **2-family discrepancy never reconciled**. This is a hard
> arithmetic inconsistency in the abstract, not just a wording issue.

---

## §D — Synth read on the four fatals (verbatim, cli_log/2026-05-05.md L668–684)

> 1. Algorithm-dependent definitions of Desert/Trans/Convergence are a
>    **project-level methodology debt**, not a P11-specific bug. (Has surfaced
>    across multiple SICF passes.)
> 2. Basis-restricted partition is a known scope-overclaim risk on F(2,4) work.
> 3. Möbius identification by numerical agreement only is a genuine rigor gap
>    — *"a theorem statement should not depend on PSLQ output as the proof
>    step."*
> 4. The 2-family discrepancy in Theorem 4.1 (#18: 26 vs 24+0+0) is a hard
>    arithmetic error. **That alone forces withdrawal-or-correction regardless
>    of the other three.**
>
> Synth note on JTNB risk: *"A submitted-with-arithmetic-error paper at JTNB
> is worse than a withdrawn-and-resubmitted paper at JTNB; the former burns
> a venue, the latter doesn't."*

---

## End of sicf_options_verbatim.md
