# Phase B numerical re-derivation log -- prompt 115

**Task ID:** T2-EXECUTOR-115-ROUTE-F-D7-FIXED-POINT-EXTRACTION-132
**Date:** 2026-05-09
**Anchor function:** `vquad_p3d6_recovery.py::compute_d6_to_d7_reduction_at_v_quad`
**Driver:** `_115_d7_driver.py` (extracts and execs the function source slice
to bypass the pre-existing module-level `cc_pipeline -> borel_channel`
import chain gap; logged as `UF-115-BOREL-CHANNEL-DEP`).

## 1. Method

Direct numerical evaluation of the OKS-O 2006 §3.1 D_6 -> D_7 reduction map
at the V_quad image, at mpmath precision `mp.dps = 300`. The map is:

    alpha = -4 * eta_0 * eta_inf
    beta  =  4 * eta_0 * (1 + theta_0)
    gamma =  4 * eta_inf**2
    delta = -4 * eta_0**2

with the V_quad image
`(eta_inf, eta_0, theta_inf, theta_0) = (1/6, 0, 0, -1/2)`
(synth Q4 v2 verdict §1 D1, bridge SHA `8a22b11`).

The s_1 fixed-point check is the closed-form identity
`s_1: alpha_1 |-> -alpha_1; alpha_1 = 0 ==> s_1(0) = 0` evaluated as an
exact equality in mpmath (no precision loss; `mpf(0) == -mpf(0)` is True
under mpmath equality).

## 2. Invocation

    cd <repo-root>
    python pcf-research/channel/cc_pipeline_2026-05-01/_115_d7_driver.py

## 3. Numerical output (full driver JSON in `c_python_helper_run.log`)

| component | computed value                       | expected (synth) | residual    | tol     | pass |
| --------- | ------------------------------------ | ---------------- | ----------- | ------- | ---- |
| alpha     | 0.0                                  | 0                | 0.0         | 1e-200  | yes  |
| beta      | 0.0                                  | 0                | 0.0         | 1e-200  | yes  |
| gamma     | 0.1111111111111111111111111... (1/9) | 1/9              | 1.16658e-302 | 1e-200 | yes  |
| delta     | 0.0                                  | 0                | 0.0         | 1e-200  | yes  |

s_1 fixed-point identity: alpha_1 = 0 ==> s_1(0) = 0 -- closed-form
identity holds in mpmath equality (no dps-relevant residual).

## 4. Structural reading (per synth verdict §1 D1, D2)

- gamma * delta = (1/9) * 0 = 0, which violates the standing assumption
  gamma * delta != 0 for the generic open stratum of P_III'(D_6).
  This is the structural signature of descent onto the P_III'(D_7)
  sector, equivalently the eta_0 = 0 collapse with eta_inf != 0
  (Okamoto 1987 §1; OKS-O 2006 §3.1).
- Under the surviving Cremona generator s_1: alpha_1 |-> -alpha_1 of
  the affine Weyl group W_a-tilde(A_1) acting on the level coordinate,
  alpha_1 = 0 is a fixed point. The V_quad image therefore sits at a
  uniquely structurally distinguished position, not generic.

## 5. Cross-cascade convergence (UF-131-4 carry-forward)

This Q4 v2 D_7-sector + s_1 fixed-point diagnosis is independently
surfaced by the 069r3 final-synthesis cascade (bridge SHA `ae5b7f7`,
T1-SYNTH-069R3-FINAL-VERDICT-ABSORPTION-124), under the
off-generic-stratum diagnosis framing. Two independent T1-Synth
threads converge from different angles -- positive forensic signal
that the diagnosis is not an artefact of one cascade's framing.

## 6. PASS / FAIL stamp

    PASS (all 4 components match expected to <= 1e-200; s_1 fixed-point
    identity holds; A1 + A2 acceptance criteria satisfied).

## 7. Fingerprints

| artefact                                       | sha256                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------ |
| vquad_p3d6_recovery.py (post-Phase-B)          | f676264289d1fc1191947b3bca6afb2f9da8eba05d7bfca2782b090e57ebe644   |
| _115_d7_driver.py                              | 342339d21df682eb65d52f671741ac06341e7f5f48caf027c1e6897be0a35eef   |
| c_python_helper_run.log                        | b068d7d98ffcb1f29ab24e3590059a93310e5e989e57c32fe0bf341f7bdbd12b   |
| extracted-fn source slice (driver-internal)    | a79dc6ffc3f78a797949e5c5a3df0c27f502d2c3dd44a2858dde3e4543620711   |

## 8. Reproducibility

The driver re-extracts the function source from `vquad_p3d6_recovery.py`
via `ast` and exec()'s it in a namespace with only `mp, mpf` bound; this
is robust to the canonical module's pre-existing module-level
`cc_pipeline -> borel_channel` import chain gap. To re-run, the only
requirement is `mpmath >= 1.3.0` and Python >= 3.10.
