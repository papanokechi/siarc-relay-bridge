# CT-S54 — REPORT: Method B and the Stokes datum

**Verdict: the independence claim is an overclaim.** Your reading was right,
and the situation is worse than the reading supposed in one respect and better
in another.

- **Worse:** the rescue you proposed is not available as the paper stands.
  Method B's *numerical* check does **not** compare against directly summed
  Borel data. It compares K·Γ(1+β) against the deposited S — the same
  comparison Method C makes.
- **Better:** a genuinely S-independent route exists, was executed in Stage
  1.4, and gives a different figure. So the repair is a rewording plus a
  corrected number, **not** a retraction.

## 1. What the source says

`sub:methodB` (revision `vquad-periodrep-paper.tex` **L913**):

> Method B is independent of the Stokes datum: it *derives* S e^{−ξ₀} from the
> cycle and the branch exponent, rather than assuming S.

Equation (26), `eq:methodB-chain`, opens: *"Substituting A = (S/2πi)Γ(1+β)"*.
Table 2 row B gives "Independent of: **the Stokes datum**". Proposition 5.4
(`prop:cross`) says the three "use disjoint inputs". §5.1's bullet for B is
narrower and **correct** — it claims independence from *the operators*, not
from S.

The wording originates upstream, in
`PERIOD-REP-VQUAD-003/cross-verification.md` §2, whose table already reads
"Independent of: the Stokes datum (derives it)".

## 2. What the cited script does

`sessions/2026-06-15/PERIOD-REP-VQUAD-003/scripts/stage4_methods.py`
(sha256 `064449fb…`), Method B block:

```python
A_amp  = K*G1pb                              # |A| = K Γ(1+β)
hankel = 2*mp.pi*1j/G1pb
lead_period = A_amp*mp.e**(-xi0)*hankel
relB = abs(abs(lead_period) - S*mp.e**(-xi0))/(S*mp.e**(-xi0))
```

`A_amp` **is** the Stokes datum: K is defined by S = 2πK. Substituting,
`lead_period` = 2πiK·e^{−ξ₀}, so

    relB = |2πK·e^{−ξ₀} − S·e^{−ξ₀}| / (S·e^{−ξ₀}) = |2πK − S| / S = relC1.

The e^{−ξ₀} cancels. **Method B's number and Method C's number are the same
quantity.** That is why both print 8.84482×10⁻⁴⁶ — a figure that has sat
twice in `stage4_methods_results.json` and twice in `cross-verification.md`'s
table since 2026-06-15, side by side, unremarked.

## 3. Measured, not asserted

`scripts/method_b_independence.py` re-implements both blocks at **dps 120**
without editing the corpus. It reproduces the stored JSON exactly
(8.84482e-46, 8.84482e-46, 9.31344e-46 — all six figures).

| observable | value | moves when **S** is perturbed 1e-30 | moves when **K** is |
|---|---|---|---|
| O1 `relB` (Method B) | 8.84482e-46 | **yes**, by 1.13061e+15 | yes |
| O2 `relC1` (Method C, S) | 8.84482e-46 | **yes**, by 1.13061e+15 | yes |
| O3 `relC2` (Method C, C) | 9.31344e-46 | **no — exactly 0.0** | yes |
| O4 independent route | **3.68728e-46** | — | — |

`|O1 − O2| = 6.19566e-122` at dps 120: not a coincidence at 46 digits, an
identity. O1 and O2 move by the *same* amount under a perturbation of S, to
within 1e-40. O3 — the A0 positive control, a quantity that genuinely does not
involve S — does not move at all, which is what shows the instrument
discriminates rather than everything moving together.

All four PREREG predictions P1–P4 held; no falsifier fired.

## 4. The claim about "directly summed Borel data"

The manuscript says Method B's closed form *"matches the directly summed Borel
data"*. The Method B block contains no Borel coefficient stream — checked by
an independent scan of the block for `b_m`, `borel_coeffs`, `formal_series`,
`b[`: all absent. The comparison is against the deposited S.

This is the sentence that makes your proposed rescue unavailable *as printed*.

## 5. Why it is a rewording, not a retraction

Stage 1.4, `numerical-integral.md` §2, extracts the amplitude from the
coefficient stream by Neville acceleration on a 40-node window near order 820:

    A_m = b_m·(−1)^m·Γ(1+β)·m!·ξ₀^{m+1+β}/Γ(m+1+β) → A

self-converging to **85.96 digits**, with no reference to S. Rebuilding Method
B on that amplitude reconstructs the deposited S to **3.68728×10⁻⁴⁶** (O4),
matching Stage 1.4's independently reported 3.7×10⁻⁴⁶ on its own table row.

So the honest form of Method B is available. It needs the Stage-1.4 amplitude,
not `stage4_methods.py`'s, and it reports 3.7×10⁻⁴⁶, not 8.84×10⁻⁴⁶.

Note also that Stage 1.4's table already separates the two rows — the
8.8×10⁻⁴⁶ row is labelled *"symbolic collapse 2KΓ(1+β)Γ(−β)|sin π(1+β)| =
2πK"*, i.e. the S = 2πK identity. The paper attached the collapse row's figure
to the period-reconstruction claim.

## 6. What the three methods actually establish

Not three independent confirmations. **Two distinct numerical facts plus one
exact symbolic identity:**

1. **Method A** — exact, symbolic, over ℚ(√3): M = h(z)·L_φ, with the
   four-sign anti-fluke test. Genuinely independent; uses no numerics and no S.
2. **S = 2πK** — one numerical fact, checked twice (as B and as C).
3. **C = |Γ(β)|·K** — 9.31344e-46, genuinely distinct, insensitive to S.

That is still a strong result. It is not the result the paper claims.

## 7. Claims

| id | label | substance |
|---|---|---|
| S54-01 | VERIFIED | B's and C's reported errors are the same quantity; agree to 6.2e-122 at dps 120 |
| S54-02 | VERIFIED | B takes its amplitude from the Stokes datum; S-perturbation moves B and C identically, leaves C=\|A\|/\|β\| exactly fixed |
| S54-03 | STRUCTURAL | §5.3's sentence and Table 2's row are overclaims |
| S54-04 | INSPECTED | no directly summed Borel data enters Method B's block |
| S54-05 | VERIFIED | the S-independent route exists (Stage 1.4) and gives 3.68728e-46 |
| S54-06 | VERIFIED | the three methods rest on two numerical facts plus A's symbolic identity |

`claims.jsonl` sha256 `96514996122e1d61f86f01285c152e2ead8b978ccef5f5c86428075510aa350c`.

## 8. Controls

Run in a scratch copy — a control must not touch the artefact it controls.

| arm | expected | result |
|---|---|---|
| **A0** pristine | **write**, rc 0 | wrote 6 claims |
| M1 P1 → False | refuse | rc 2, "central claim does not hold" |
| M2 O2 figure moved | refuse | rc 2, names both figures |
| M3 A0 control moves | refuse | rc 2, "does not show an exactly zero move" |
| M4 stream → True | refuse | rc 2, "S54-04 would be false" |
| M5 O4 line deleted | refuse | rc 2, "anchor matched 0 lines" |

6/6, each for its own reason; the session's `claims.jsonl` byte-identical
before and after.

Ordering follows CT-S47: the observable is evaluated **before** the vacuity
pre-check, so a fired observable cannot be converted into a refusal.

## 9. What this does NOT establish

- It does not re-derive the main identity, and does not touch Part A's ξ = 0
  result.
- It does not check the **other** independence claims. §5.1's bullets and
  `prop:cross` make several; only B-vs-the-Stokes-datum was tested.
  **Per Amendment H this is named, not silently omitted** — the sweep was
  scoped to the claim you reported, and that scope is itself a limit.
- It does not establish that Method A is independent; that was assumed from
  its being exact and symbolic, not measured.
- Nobody has read §5 end to end as prose.

## 10. Recommended edits — prepared, NOT applied

Deliberately not applied, because the base-version question from CT-S53 is
open: if LMP holds v1.2 rather than v1.0, the revision needs rebasing first
and these edits should go in against the right base.

| # | location | change |
|---|---|---|
| 1 | `sub:methodB`, final sentence | replace the independence sentence: B derives the leading period from the cycle and branch exponent **given the amplitude A**; with A taken from the Stokes datum the check is not independent of S, and with A extracted from the large-order data it is |
| 2 | `eq:methodB-err` | 8.84×10⁻⁴⁶ → **3.69×10⁻⁴⁶**, and cite Stage 1.4's extraction, not `stage4_methods.py` |
| 3 | `sub:methodB`, "directly summed Borel data" | delete; it is not what was computed |
| 4 | Table 2, row B, "Independent of" | "the operators" (true) rather than "the Stokes datum" |
| 5 | `prop:cross` | "disjoint inputs" → B and C share the amplitude A; state the two distinct numerical facts plus A's symbolic identity |
| 6 | `sub:strategy` | B's bullet is already correct; the §5 preamble's "three structurally independent ways" needs the same narrowing |
| 7 | §9.4 / §B.5 | if they cite three-fold independence, narrow correspondingly — **not checked here** |

## 11. Operator rulings recorded this session

- **The companion's C1 is not independent corroboration.** It concerns a
  different operator's finite singular points. Recorded as *"same failure
  class as companion C1 — integer exponents taken to mean apparency"*, not as
  corroboration. Same one-name-two-objects trap, at the level of evidence.
- **Zenodo 20719043:** no separate notice yet; wait for the editor, then
  deposit one new version of concept 20719042 matching what they accept, to
  keep the cover letter's promise that deposit and submission are identical.
- **`lem:apparent`:** leave it. Labels do not render; renaming churns six
  cross-references for nothing a reader sees.
- **The end-to-end read** remains outstanding and is not an instrument task.

## 12. Uncommitted files

```
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/PREREG.md
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/REPORT.md
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/FOLLOWUP-EMAIL.md
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/claims.jsonl
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/scripts/method_b_independence.py
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/scripts/emit_claims_s54.py
sessions/2026-09-17/CT-S54-METHOD-B-INDEPENDENCE/outputs/method_b_independence.out.txt
```

Nothing committed, sent, uploaded, submitted or deposited. No earlier
session's files were modified; the corpus script was read and re-implemented
here, never edited or re-run in place.
