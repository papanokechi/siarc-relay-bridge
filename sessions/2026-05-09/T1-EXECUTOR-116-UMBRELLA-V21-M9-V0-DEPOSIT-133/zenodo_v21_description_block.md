# Zenodo v2.1 description block (ready-to-paste)

Operator pastes this into the Zenodo `Description` field at Phase C.3.
Replaces the existing v2.0 description (or appends as a v2.1
changelog -- operator's choice; recommended: replace, since the v2.1
description is a strict superset of v2.0's by virtue of stating that
content is unchanged).

---

This is v2.1 of the SIARC umbrella program statement -- a closure
cascade amendment that records three milestone closures landed on the
SIARC relay bridge (github.com/papanokechi/siarc-relay-bridge) since
v2.0 (deposited 2026-05-02).

The v2.1 amendment is a status / provenance addendum, NOT a content
revision. All mathematical content, conjectures, open problems, and
the cross-degree invariant triple introduced in v2.0 are unchanged.
The new sec:closure-cascade documents:

  Item 1 (M4 V0 closure): the deg-a=0 row mechanism (068 verdict
  UPGRADE_FULL_VIA_DEG_A_ZERO_ROW; bridge SHA 5f9db69, 2026-05-08).
  Confidence MEDIUM-HIGH; HIGH-pending W21 LANE-1 ratification +
  Wasow sect X.3 OCR. Closed-form: A_naive = 2d - d_a, specialised to
  d_a = 0 to give A_naive = 2d uniformly at d >= 2.

  Item 2 (M6.CC R1 closure): V_quad on the D_6 -> D_7 degeneration
  boundary, via the Q4 v2 cascade (bridge SHAs 10b5cf6 packet 130 +
  8a22b11 verdict 131). The V_quad image
  (eta_inf, eta_0, theta_inf, theta_0) = (1/6, 0, 0, -1/2) violates
  the standing assumption eta_0 != 0 of P_III'(D_6) generic open
  stratum; surviving Cremona symmetry reduces to widetilde-W_a(A_1)
  on P_III'(D_7). Substrate: Okamoto 1987 sec 1; Ohyama-Kawamuko-
  Sakai-Okamoto 2006 sec 3.1; Kajiwara-Noumi-Yamada 2017 sec 8.5;
  Sakai 2001.

  Item 3 (Route F slot 115 numerical re-derivation): bridge SHA
  8ebd1eb. At dps=300, the V_quad image maps to (alpha, beta, gamma,
  delta) = (0, 0, 1/9, 0) under the OKS-O 2006 sec 3.1 reduction
  map; the s_1: alpha_1 |-> -alpha_1 reflection fixes alpha_1 = 0;
  the V_quad image sits at the s_1 fixed point. Companion paper PCF-1
  carries the manuscript pull-back (new labelled remark
  rem:vquad-d7-s1).

Cross-cascade convergence note: the D_7 sector + s_1 fixed-point
diagnosis (Q4 v2 cascade) converges with the 069r3 final-synthesis
off-generic-stratum diagnosis (bridge SHA ae5b7f7). Two independent
T1-Synth threads land on the same structural feature; positive
forensic signal.

Bridge session for this v2.1 deposit:
sessions/2026-05-09/T1-EXECUTOR-116-UMBRELLA-V21-M9-V0-DEPOSIT-133/

AEAL audit (this version): 7 audit-only entries in the bridge session
claims.jsonl; 0 new numerical claims (all numerical content traces to
prior bridge sessions 068 / 106 / 130 / 131 / 132 / 124).

This deposit is the M9 V0 critical-path closure step in the SIARC
roadmap; it unblocks the M7 / M8a / M8b axis closures and the
picture-v121 M4-closed-tag annotation.
