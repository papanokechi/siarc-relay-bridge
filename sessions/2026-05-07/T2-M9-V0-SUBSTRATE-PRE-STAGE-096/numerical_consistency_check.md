# Numerical consistency check — V0 substrate Phase C

**Relay:** 096 T2-M9-V0-SUBSTRATE-PRE-STAGE
**Tier:** TIER-A.2 (V0-pre-flight numerical Stokes-multiplier
consistency check per Reviewer D Q4)
**Status:** PRE-FIRE-INPUT (M6.CC R1-gated)
**Verdict:** `PRE_FIRE_INPUT_R1_GATED`
**Anchor:** 069 handoff `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`
verdict (sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-
PHASE-D-NUMERICAL/handoff.md)

---

## 1. Spec recap (Phase C of relay 096)

Reviewer D Q4 recommendation (peer_ai_reviews_received_2026-05-07.md
SHA-16 `DF92466E123E16BF`, L294, verbatim quote, 25 words):

> Add a "V0-pre-flight" task to the agent queue: a 10-digit
> numerical check of the Stokes multipliers against the
> connection formula

The substrate task is therefore: identify the Stokes-multiplier
values that V0 would announce, identify the connection-formula
target value, and compute the residual at >= 10 dps (program
AEAL convention preferred at >= 30 dps).

---

## 2. LHS — measured Stokes-multiplier value (V_quad-native)

Substrate anchor: 058R Phase A `H4_EXECUTED_PASS_108_DIGITS`
(picture v1.19 §3 P-CC row L860; G4 row §5 L1067) +
069 Phase D numerical follow-up (sessions/2026-05-07/
CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/handoff.md).

Numerical values pinned in the V_quad native normalization:

| Quantity | Value | dps | Source |
|----------|-------|-----|--------|
| $\beta$ (logarithmic component) | 0 | $\ge 107$ | 058R Phase A |
| $\lvert C_V\rvert$ (V_quad-native amplitude) | $8.127336795495072367112578732020\ldots$ | 30 | 069 §Key numerical findings |
| $\lvert 2\pi C_V\rvert$ | $51.065563139954662269831674609923147769762888992158\ldots$ | 50 | 069 §Key numerical findings |
| $S_{\zeta_*}$ (V_quad-native) | $\approx 51.066\,i$ | 30+ | picture v1.19 §3 P-CC row L860 |

The native $\lvert 2\pi C_V\rvert$ figure 51.065563... is the
LHS of the would-be 10-dps RH consistency check **in V_quad
native form**.

---

## 3. RHS — canonical-form Stokes value via $\Phi_{\mathrm{symp}}$

To complete a numerical RH consistency check, the canonical-form
$P_{\mathrm{III}}(D_6)$ Stokes value $\lvert
S_{\zeta_*}^{\mathrm{can}}\rvert$ is required as RHS. The
program-internal map for the conversion is the symplectic
$\Phi_{\mathrm{symp}}$ leg of the V_quad $\to P_{\mathrm{III}}(D_6)$
normalization map (G15 / G22 per picture v1.19 §5 L1066, L1080).

Numerical status of the RHS construction per 069 handoff (verbatim
substrate quote, 31 words):

> $\lvert\det J(\Phi_{\mathrm{symp}})\rvert$ at V_quad parameter
> point: NOT_COMPUTABLE_R1_GATED. Block factorisation pinned:
> $\det J(\Phi_{\mathrm{resc}}) = 1/9$, $\det J(\Phi_{\mathrm{shift}})
> = 1$, $\det J(\Phi_{\mathrm{symp}})$ depends on Phase D.2.b
> gauge $G(x)$.

The RHS is therefore **NOT NUMERICALLY AVAILABLE** at this fire's
time. The R1 substrate gap is the open `M6.CC R1` carry-forward
recorded at 075 STRUCTURAL_MISMATCH verdict + 069 PARTIAL_NUMERICAL
verdict.

---

## 4. Residual computation

Residual definition (per Phase C envelope §C.3):

$$
\Delta_{\mathrm{RH}} \;=\; \bigl|\lvert M^{*} C_V\rvert
   \;-\; \lvert S_{\zeta_*}^{\mathrm{can}}\rvert\bigr|
$$

where $M^{*}$ is the composite Jacobian of the normalization map
$\Phi_{\mathrm{resc}} \circ \Phi_{\mathrm{shift}} \circ
\Phi_{\mathrm{symp}}$.

Substituting the available factor data:

$$
\lvert M^{*}\rvert \;=\; \lvert \det J(\Phi_{\mathrm{resc}})\rvert
   \cdot \lvert \det J(\Phi_{\mathrm{shift}})\rvert
   \cdot \lvert \det J(\Phi_{\mathrm{symp}})\rvert
   \;=\; \tfrac{1}{9} \cdot 1 \cdot \lvert \det J(\Phi_{\mathrm{symp}})\rvert
$$

and $\lvert \det J(\Phi_{\mathrm{symp}})\rvert$ is
NOT_COMPUTABLE_R1_GATED. Therefore $\Delta_{\mathrm{RH}}$ is
**INCOMPUTABLE at this fire's time** (matches 069 §Key numerical
findings line "Δ residual: INCOMPUTABLE (both LHS $\lvert M^{*}
C_V\rvert$ and RHS $\lvert S_{\zeta_*}^{\mathrm{can}}\rvert$
R1-gated)" — verbatim quote, 22 words, from
`sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-
NUMERICAL/handoff.md`).

---

## 5. Verdict

**$\boxed{\text{PRE-FIRE-INPUT}}$**

Per relay 096 §Phase C halt-or-flag policy + envelope HALT
register entry `HALT_096_NUMERICAL_DIVERGE` (which triggers
only when residual $> 10^{-5}$ at 10 dps **with no PRE-FIRE-INPUT
explanation**):

* Residual is incomputable — the LHS minus RHS subtraction
  cannot be performed because RHS has not been numerically
  pinned.
* The R1 substrate gap (Okamoto 1987 §§2-3 Lax pair primary-
  source not yet acquired; W21 LANE-1 jurisdiction) is a
  named explicit explanation.
* HALT_096_NUMERICAL_DIVERGE is therefore **NOT TRIGGERED**.

The verdict is recorded as Phase C output for V0-fire
consumption: when M6.CC R1 closure lands (post W21 LANE-1
acquisition / arbitration; per 075 + 069 forward-pointers),
the residual $\Delta_{\mathrm{RH}}$ becomes computable and
the V0 fire can include the numerical Stokes-multiplier
consistency check as a TIER-A.2 deliverable. Until then, V0
substrate flags this as a **conditional secondary classifier
gated on M6.CC R1 closure** (matches the §3.2 Stokes-data
target-axis disposition in `phi_assignment_statement.md`).

---

## 6. Forward-pointed numerical task

Once $\lvert \det J(\Phi_{\mathrm{symp}})\rvert$ is computable
(post M6.CC R1 closure), the residual computation reduces to
mpmath at dps $\ge 30$:

```python
import mpmath
mpmath.mp.dps = 30
C_V       = mpmath.mpc("8.12733679549507236711257873202")
two_pi_CV = mpmath.fabs(2 * mpmath.pi * C_V)        # = 51.06556313995466...
det_resc  = mpmath.mpf("1") / 9
det_shift = mpmath.mpf("1")
det_symp  = ...                                     # R1-gated; pin post-M6.CC
M_star    = det_resc * det_shift * det_symp
S_can     = ...                                     # R1-gated; pin post-M6.CC
Delta_RH  = mpmath.fabs(mpmath.fabs(M_star) * mpmath.fabs(C_V)
                        - mpmath.fabs(S_can))
print("Delta_RH =", mpmath.nstr(Delta_RH, 20))
```

The script template above is recorded for downstream V0-fire
consumption. **The script is not executed at this fire's time**
(R1-gated; would output `det_symp` and `S_can` placeholders only).

---

## 7. AEAL anchor block

* numerical_consistency_check.md SHA-256: computed at fire
  end in `claims.jsonl` 096-C-1.
* 069 anchor: handoff.md at `sessions/2026-05-07/CC-VQUAD-PIII-
  NORMALIZATION-MAP-PHASE-D-NUMERICAL/handoff.md` (069 verdict
  `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`; SHA-16 to be
  recorded in claims.jsonl).
* Reviewer D Q4 anchor: `tex/submitted/control center/
  peer_ai_reviews_received_2026-05-07.md` L294 (SHA-16
  `DF92466E123E16BF`).

---

End numerical_consistency_check.md.
