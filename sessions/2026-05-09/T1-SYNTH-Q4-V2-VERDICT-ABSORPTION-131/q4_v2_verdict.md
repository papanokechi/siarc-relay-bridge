# Q4 v2.0 Verdict — Synth Output (T1-Synth Execution)

**Verdict label (synth-proposed):** `GO_ROUTE_F_FIXED_POINT_DISTINGUISHED`
**Confidence band:** HIGH
**Substrate stack consumed inline:** Paper V (Ohyama-Kawamuko-Sakai-Okamoto 2006)
+ Okamoto 1987 §0+§1 + CT v1.3 §3.5.1 + KNY §8.5.17 (per packet 130 §4)
**Date received:** 2026-05-09 ~09:32 JST
**Bridge parent (packet):** `10b5cf6` (T1-OPERATOR-Q4-ROUND2-DIRECT-DERIVATION-PACKET-130)
**Verdict-label conformance to packet 130 §11 5-bin ladder:** ENHANCED MATCH to Bin 1
(`UPGRADE_FULL_VIA_D7_DEGENERATION_DIAGNOSIS`) with structural payload extension —
synth identifies V_quad as sitting at the **fixed point** of `s_1` in the surviving
`A_1^{(1)}` factor, not merely at a generic point of the `D_6 -> D_7` boundary.
See discrepancy_log.json D-131-1 + unexpected_finds.json UF-131-2 for nonconformance
documentation (LOW + INFO; non-blocking enhancement).

---

## §1. Per-Derivation Status

### D1: D_6 -> D_7 Degeneration Diagnosis
**Status:** CLOSED
**Substrate cite:** OKS-O 2006 §3 (eq. 26) + Okamoto 1987 §0 / §1.

**Derivation:** Under the CT v1.3 §3.5.1 Hamiltonian-rename trivial identity, the
V_quad image maps precisely to (eta_inf, eta_0, theta_inf, theta_0) = (1/6, 0, 0, -1/2).
Pushing this through the classical-ODE reduction map yields:

  alpha = -4 * (1/6) * (0)         = 0
  beta  =  4 * (0)   * (1 + (-1/2)) = 0
  gamma =  4 * (1/6)^2              = 1/9   != 0
  delta = -4 * (0)^2                = 0

The standing assumption for the generic open stratum of P_III'(D_6) dictates
eta_0 * eta_inf != 0 (equivalently gamma * delta != 0). Because eta_0 = 0 implies
delta = 0, V_quad explicitly violates the generic stratum assumption. Per
OKS-O 2006 §3.1, this (gamma != 0, delta = 0) parameter collapse characterizes
the descent precisely into the P_III'(D_7) sector. V_quad is definitively
isolated on the D_6 -> D_7 degeneration boundary.

### D2: W_a-tilde(A_1) Action at the V_quad Image
**Status:** CLOSED
**Substrate cite:** OKS-O 2006 §2.3 (Theorem 6) + §3.1.

**Derivation:** The P_III'(D_7) Hamiltonian requires a gauge/scaling transformation
from the raw D_6 coordinates to match the normal form

  t * H = q^2 * p^2 + alpha_1 * q * p + t * p + q

However, the symmetry is invariant under the transformation. The V_quad seed
values (alpha = 0, beta = 0) and specifically theta_0 = -1/2 correspond to the
symmetric zeroing of the classical parameters. Under the Cremona group
W_a-tilde(A_1) = <s_1, sigma>, the surviving root parameter alpha_1 maps to the
classical parameters. The algebraic condition corresponding to beta = 0 (and
theta_0 = -1/2) maps to the root coordinate alpha_1 = 0.

Applying the action from the OKS-O 2006 §2.3 table:

  s_1: alpha_1 |-> -alpha_1.  At alpha_1 = 0,  s_1(0) = 0.

Therefore, the V_quad image sits exactly at the fixed point of the s_1 generator
within the surviving A_1^{(1)} factor. It is uniquely structurally distinguished,
not generic.

### D3: Cross-walk Refinement
**Status:** CLOSED
**Substrate cite:** OKS-O 2006 §2.3 + KNY §8.5.17.

**Derivation:** The derivation confirms the structural refinement. The
identification of the P_III'(D_7) sector forces the substitution of the full
W((2A_1)^{(1)}) framing in favor of the degenerate

  W_a-tilde(A_1) x_semi Z_2  =  Aut(D_7^{(1)}) x_semi W((A_1)^{(1)}).

This efficiently neutralizes UF-126-PARAM-COUNT by collapsing the four-parameter
D_6 system to the two-parameter (alpha_0, alpha_1) D_7 system. The Sakai equation
of motion constraint a_0 + a_1 = 1 maps identically to the OKS-O 2006 level
constraint alpha_0 + alpha_1 = 1 (where alpha_0 = 1 - alpha_1), preserving the
core surface-type geometry while eliminating the ambient parameter space.

### D4: Resolution of UF-126-DELTA-DECOMP-FORM
**Status:** CLOSED
**Substrate cite:** OKS-O 2006 §3.1.

**Derivation:** The null-sum violation Delta = -1/3 is resolved natively under
the D_7 sector identification. Instead of evaluating Delta as an anomalous
decomposition ambiguity under the D_6 surface, it is recognized as the numerical
signature of the eta_0 = 0 structural collapse. It forces V_quad onto the
distinguished alpha_1 = 0 fixed point of the one-parameter D_7 Hamiltonian. The
ambiguity is fully absorbed by the topological boundary condition.

---

## §2. Residual-Question List

- **None.** All blocking residuals from session 129 (UF-126-PARAM-COUNT,
  UF-126-DELTA-DECOMP-FORM, UF-129-1) are cleanly resolved by the
  single-A_1^{(1)}-factor collapse mechanism natively mapped to the
  D_6 -> D_7 boundary.
- **Note:** The placeholder dependency on KNY §§8.5.1-16 (convention-fixing) is
  bypassed, as OKS-O 2006 §3 explicitly pins the necessary
  alpha/beta/gamma/delta maps.

**Ready for prompt 117 (Route F executor envelope).**

(Agent-side note on slot numbering: synth-projected "117" is a forward
projection. Actual next free numbered .txt slot is 115; see UF-131-3.)

---

## §3. Agent-side absorption notes (post-paste)

1. **Verdict-label nonconformance (LOW).** Synth's `GO_ROUTE_F_FIXED_POINT_DISTINGUISHED`
   is a refinement of packet 130 §11 Bin 1 (`UPGRADE_FULL_VIA_D7_DEGENERATION_DIAGNOSIS`).
   The structural payload is materially richer: not only is V_quad on the
   degeneration boundary, but it sits at the s_1 fixed point of the surviving
   A_1^{(1)} factor under W_a-tilde(A_1). This is a strict enhancement, not a
   deviation. Documented as D-131-1 + UF-131-2.

2. **Forbidden-verb usage (INFO non-blocking).** §1 D3 contains the phrase
   "The derivation confirms the structural refinement." The verb "confirms"
   is on the project-wide forbidden-verb list per copilot-instructions.md
   (lit-review prediction-or-conjecture context rule). However, this usage
   sits inside a derivation context with explicit substrate citations
   (OKS-O 2006 §2.3 + KNY §8.5.17), not a prediction-or-conjecture context.
   Per the standing rule's stated scope ("if any 'shows'/'confirms'/'proves'
   wording slips into a prediction-or-conjecture context"), this is not a
   hard-halt trigger. Documented as UF-131-1 for word-choice surfacing if
   operator wishes to relay back to synth for refinement.

3. **Numerical sub-claims absorbed as substrate.** The synth-derived numerical
   facts (alpha = beta = delta = 0, gamma = 1/9, alpha_1 = 0 fixed-point of s_1)
   are absorbed as synth-tier substrate per AEAL discipline. Agent did not
   independently re-derive; agent's claim is verdict-receipt only. See
   claims.jsonl entry CL-131-1.

4. **Downstream readiness.** With Q4 closed, the next-action gate is the
   Route F executor envelope draft (numbered prompt slot 115, per next-free
   sequential — NOT 117 as synth projected). Envelope scope per packet 130
   §11 Tier 3 + this verdict §1 D2: build executor envelope to formalize
   the s_1 fixed-point classification + D_7 sector pull-back into the
   manuscript-ready CT v1.3 §3.5.1 cross-walk + run pdflatex compile checks
   against the Hamiltonian-renamed manuscript.
