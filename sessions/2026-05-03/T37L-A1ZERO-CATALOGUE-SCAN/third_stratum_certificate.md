# Third-stratum certificate — T37L-A1ZERO-CATALOGUE-SCAN

Date: 2026-05-03 06:52:14
Verdict: **T37L_THIRD_STRATUM_HIGHER_DIM**

## Bracket form (recovered from 017f Find #1)

```
B(alpha, beta, gamma) := alpha/16 + gamma - beta^2 / (4 alpha)

Equivalent polynomial (multiply by 16*alpha):
  alpha^2 + 16*alpha*gamma - 4*beta^2 = 0

Solved for gamma:
  gamma = (4*beta^2 - alpha^2) / (16*alpha)
```

## Algebraic locus classification

- Locus B = 0 in (alpha, beta, gamma)-space: **2-dimensional quadric surface**
- Free parameters: alpha, beta (gamma determined)
- Integer lattice in box (alpha<=10, |beta|<=20): 46 points
- QL09 (2, 3, 1) lies on the locus to >50 digits

## B-evaluation at T35 4-rep catalogue (sanity)

| Rep    | (alpha, beta, gamma) | B(rep)                     |
|--------|----------------------|----------------------------|
| V_quad | (3, 1, 1) | 1.10416666666666674068153497501043602824 |
| QL15   | (3, -2, 2) | 1.85416666666666674068153497501043602824 |
| QL05   | (1, -2, -1) | -1.9375 |
| QL09   | (2, 3, 1) | 0.0 |

Only QL09 lies on B = 0 among the 4 T35 reps.

## Candidates and numerical a_1 = 0 confirmation

K_cand = 6; recurrence at dps=300, N=2000; stage-1 fit at K_lead=25, W1=(400, 1900); envelope grid K_lead in [20, 25, 30] x W1 in [(400, 1900), (600, 1900), (800, 1900)].

| Candidate            | (alpha, beta, gamma, delta, epsilon) | recurrence a_1   | fit a_1 (central)  | env half-range | confirms? |
|----------------------|--------------------------------------|------------------|--------------------|----------------|-----------|
| Q1_QL09_repro        | (2,3,1,5,0) | |a_1|=10^-inf | |a_1|=10^-49 | 1.695662400636 | True |
| Q2_alpha2_b1_g0      | (2,1,0,1,0) | |a_1|=10^-inf | |a_1|=10^-51 | 7.776352695997 | True |
| Q3_alpha2_b5_g3      | (2,5,3,1,0) | |a_1|=10^-inf | |a_1|=10^-52 | 6.258732951890 | True |
| Q4_alpha4_b2_g0      | (4,2,0,1,0) | |a_1|=10^-inf | |a_1|=10^-53 | 5.966787884483 | True |
| Q5_alpha4_b6_g2      | (4,6,2,1,0) | |a_1|=10^-inf | |a_1|=10^-54 | 5.667748630900 | True |
| Q6_alpha8_b4_g0      | (8,4,0,1,0) | |a_1|=10^-inf | |a_1|=10^-56 | 7.159457205991 | True |

## Picture v1.11 amendment (recommendation, not authority)

G20 sub-stratum (iii) is consistent with being a 2-dimensional algebraic sub-variety of (alpha, beta, gamma)-space (4-dimensional once delta, epsilon are included as free directions, since they do not affect a_1 for d=2 PCFs). QL09 is one integer lattice point among infinitely many. T35's 4-rep catalogue intersects sub-stratum (iii) only at QL09, but the locus itself is rich, populated, and operator-side family extension can sample it densely.

## Notes

- 'consistent with' is the operative phrase per 017c v2 / 017f forbidden-verb hygiene.
- AEAL elevation of the picture v1.11 amendment requires Claude review.