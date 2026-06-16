# Verification pass — VQUAD-PAPER-CORRECTIONS-001 (Stage 5)

Re-verification that the corrections (expository + bibliographic + terminological) altered **no
numerical result**. `mpmath`, dps=60.

## Constants (recomputed vs the corrected paper's eq:constants / App. A.3)
| symbol | recomputed (mpmath dps=60) | paper eq:constants (§4.3 L61-64) | match |
|---|---|---|---|
| `K` (input, 58-dig pin) | 0.0728781025518669641294423633296525128045556892 | same | ✓ |
| `S = 2πK` | 0.4579066231690176361190978425482258379623951354 | 0.457906623169017636119097842548225837962395135… | ✓ |
| `C = |Γ(β)|·K` | 0.4377052861935372212307397497943695899817255974 | 0.437705286193537221230739749794369589981725597… | ✓ |
| `|Γ(β)|` | 6.0059917981814175262 | (implicit) | ✓ |
| `β = −1/(3√3)` | −0.19245008972987525484 | −0.19245008972987525… | ✓ |
| `ξ₀ = 2/√3` | 1.154700538379251529 | 1.1547005383792517… | ✓ |

## Bridge identity (exact)
```
S/C            = 1.046152828427455008442757
2π/|Γ(β)|      = 1.046152828427455008442757
S/C − 2π/|Γ(β)| = 0.0      (residual 0, exact — not a numerical near-miss)
|C − S|        = 0.0202013   (C and S are genuinely distinct)
```

## Two independent derivations of C still agree (Stage 5.2)
- `eq:C-from-A` (Hankel/Borel branch): `C = |A|/|β| = K·Γ(1+β)/|β| = K·|Γ(β)| = 0.437705286…`.
- `eq:main-recentred` (Stokes-data, recentred period): `C = (|Γ(β)|/2π)·S = (|Γ(β)|/2π)·(2πK)
  = |Γ(β)|·K = 0.437705286…`.
- Both reduce to `|Γ(β)|·K`; the bridge residual `0` confirms the two routes coincide exactly. The
  H-1 remark cites exactly these two equations (`\eqref{eq:C-from-A}`, `\eqref{eq:bridge}`).

## Conclusion
**Constants unchanged: YES.** No applied correction touched a numerical value. The only
equation-adjacent edits (M-1, L-2, and the H-1 remark) restate identities already present in §4
(`C=(|Γ(β)|/2π)S`, `|A|=K·Γ(1+β)`, `S/C=2π/|Γ(β)|`); no new value was introduced, none altered.
