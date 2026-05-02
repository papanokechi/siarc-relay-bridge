# Subfamily Certificate — T37K-EXTEND-A3-SUBFAMILY

## Selected third A=3 representative

- id: `T37K_A3_third`
- (alpha, beta, gamma, delta, epsilon) = (2, 0, 2, 0, 1)
- Delta_b (target) = -16
- A_pred = 3 (side = neg)
- |sum of integer params| = 5
- |Delta_b - (-15.5)| = 0.5
- provenance: parametric enumeration (T37K Phase A.3)

## a_1 measurement (third A=3 rep)

- median (60-digit cap): `-4.2499999999999999999999999999999999999999999999999999999999`
- envelope half-range:    `3.78087225809508083753125558315e-51`
- grid: 9 configs, K_lead in {22,25,28} x W1 in {{(800,1200),(800,1500),(800,1800)}}

## Relation test

- predicted_a_1 = (4*Delta_b - 9) / 36 = `-2.02777777777777777777777777777777777777777777777777777777778`
- residual      = a_1_median - predicted_a_1 = `-2.22222222222222222222222222222222222222222222222222222222212`
- tight gate    = 1e-30; loose gate = 1e-3
- outcome       = **T37K_RELATION_FALSIFIED**

## PSLQ cross-validation

- tol=1e-30 relation: `[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -36, 0]`
- tol=1e-12 relation: `[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -36, 0]`
- artefact-only at tol=1e-12? `False`

## Picture v1.11 amendment recommendation

Picture v1.11: G20 catalogue stands as discrete; the V_quad/QL15 match was a 2-point coincidence. No A=3 sub-family closed form via the (2A)^2*a_1 = 4*Delta_b - 9 ansatz.
