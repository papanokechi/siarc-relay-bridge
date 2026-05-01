# H6 — Chowla–Selberg / Kontsevich–Zagier periods for PCF-1's six missing limits

## Executive summary

PCF-1's six negative-discriminant non-detections are best interpreted as a small CM-period roster rather than as evidence against closed form.  The local SIARC record identifies the six families as

| family | discriminant | CM order | field | H6 basis constant |
|---|---:|---|---|---|
| `Q_L01` | `-3` | `Z[(1+sqrt(-3))/2]` | `Q(sqrt(-3))` | `Omega_-3` |
| `Q_L02` | `-4` | `Z[i]=Z[sqrt(-1)]` | `Q(i)` | `Omega_-4` |
| `Q_L06` | `-7` | `Z[(1+sqrt(-7))/2]` | `Q(sqrt(-7))` | `Omega_-7` |
| `V_quad` | `-11` | `Z[(1+sqrt(-11))/2]` | `Q(sqrt(-11))` | `Omega_-11` |
| `Q_L15` | `-20` | `Z[sqrt(-5)]` | `Q(sqrt(-5))` | `Omega_-20` |
| `Q_L26` | `-28` | `Z[sqrt(-7)]`, conductor-2 order in `Q(sqrt(-7))` | `Q(sqrt(-7))` | `Omega_-28` |

The roster is supported by the PCF-2 program statement's recap of PCF-1: the six CM candidates have `Delta_2 in {-3,-4,-7,-11,-20,-28}` and all fail the PCF-1 18-element PSLQ basis at 220 digits.  The channel-theory table then gives the per-family labels and discriminants: `Q_L01`, `Q_L02`, `Q_L06`, `V_quad`, `Q_L15`, `Q_L26`.

The relevant classical theorem is the Chowla-Selberg formula.  In the form needed here, for an imaginary-quadratic discriminant `D<0`, quadratic/Kronecker character `chi_D`, class number `h(D)`, and roots-of-unity count `w(D)`, it expresses products of Dedekind eta values at CM points, hence CM elliptic periods up to algebraic factors, in finite products of `Gamma(r/|D|)`.  The fetched source page for the Chowla-Selberg formula gives the logarithmic identity

`(w/4) sum_r chi(r) log Gamma(r/D) = (h/2) log(4*pi*sqrt(|D|)) + sum_tau log(sqrt(Im tau) |eta(tau)|^2)`,

and the individual-value form

`Im(tau)|eta(tau)|^4 = alpha/(4*pi*sqrt(|D|)) prod_r Gamma(r/|D|)^{chi(r) w/(2h)}`

for an algebraic `alpha`.  Chowla-Selberg therefore predicts exactly the kind of missing constants the PCF-1 basis did not contain: finite Gamma-products at rational arguments whose denominators are `3,4,7,11,20,28`.

Kontsevich-Zagier supplies the conceptual envelope, not a detection algorithm.  Their period framework says elliptic periods and CM eta-periods are periods in the KZ sense.  It does not say every PCF limit is a period, nor does it give a PSLQ basis.  Thus H6's mathematical claim is conditional: if the PCF-1 limits land in the elliptic CM period lines suggested by their discriminants, Chowla-Selberg gives the missing basis elements.  If instead a limit contains an isomonodromic Stokes constant, a regulator, a Stark unit, or a real-quadratic Borcherds-product value, the 24-element basis below may only detect a subfactor.

## Explicit Gamma-product candidates

Let

`Q_D = prod_{1 <= r < |D|, gcd(r,|D|)=1} Gamma(r/|D|)^{chi_D(r)}`.

The following constants are the recommended PSLQ generators.  Equalities marked `~_alg` mean equality up to a nonzero algebraic multiplier and the harmless choice of elliptic-period normalization; the PSLQ recipe should evaluate the displayed constants themselves.

1. **`D=-3`, `Q_L01`, CM by `Z[(1+sqrt(-3))/2]`.**
   Character quotient: `Q_-3 = Gamma(1/3)/Gamma(2/3)`.
   Period-normalized generator:
   `Omega_-3 = Gamma(1/3)^3/(2*pi)` (`~_alg` the equianharmonic period; some curve normalizations use a further rational or `sqrt(3)` factor).

2. **`D=-4`, `Q_L02`, CM by `Z[i]`.**
   Character quotient: `Q_-4 = Gamma(1/4)/Gamma(3/4)`.
   Prompt-normalized generator:
   `Omega_-4 = Gamma(1/4)^2/(2*sqrt(2*pi))`.

3. **`D=-7`, `Q_L06`, CM by the maximal order of `Q(sqrt(-7))`.**
   `chi_-7=+1` on residues `{1,2,4}` and `-1` on `{3,5,6}`.
   `Q_-7 = Gamma(1/7)Gamma(2/7)Gamma(4/7)/(Gamma(3/7)Gamma(5/7)Gamma(6/7))`.
   Reflection-reduced generator:
   `Omega_-7 = Gamma(1/7)Gamma(2/7)Gamma(4/7)/(2*pi)^(3/2)` up to an algebraic sine factor.

4. **`D=-11`, `V_quad`, CM by the maximal order of `Q(sqrt(-11))`.**
   `chi_-11=+1` on `{1,3,4,5,9}` and `-1` on `{2,6,7,8,10}`.
   `Q_-11 = Gamma(1/11)Gamma(3/11)Gamma(4/11)Gamma(5/11)Gamma(9/11)/(Gamma(2/11)Gamma(6/11)Gamma(7/11)Gamma(8/11)Gamma(10/11))`.
   Reflection-reduced generator:
   `Omega_-11 = Gamma(1/11)Gamma(3/11)Gamma(4/11)Gamma(5/11)Gamma(9/11)/(2*pi)^(5/2)` up to an algebraic sine factor.

5. **`D=-20`, `Q_L15`, CM by `Z[sqrt(-5)]`.**
   `chi_-20=+1` on `{1,3,7,9}` and `-1` on `{11,13,17,19}` modulo `20`.
   `Q_-20 = Gamma(1/20)Gamma(3/20)Gamma(7/20)Gamma(9/20)/(Gamma(11/20)Gamma(13/20)Gamma(17/20)Gamma(19/20))`.
   Since `h(-20)=2`, a common CM-period generator is naturally a root of the class product:
   `Omega_-20 = Q_-20^(1/4)`; equivalently `~_alg (Gamma(1/20)Gamma(3/20)Gamma(7/20)Gamma(9/20))^(1/2)/pi`.
   This is the highest-risk member because the class field/algebraic multiplier is nontrivial.

6. **`D=-28`, `Q_L26`, conductor-2 order `Z[sqrt(-7)]`.**
   `chi_-28` is the lift of the `-7` character to odd residue classes modulo `28`: `+1` on `{1,9,11,15,23,25}` and `-1` on `{3,5,13,17,19,27}`.
   `Q_-28 = Gamma(1/28)Gamma(9/28)Gamma(11/28)Gamma(15/28)Gamma(23/28)Gamma(25/28)/(Gamma(3/28)Gamma(5/28)Gamma(13/28)Gamma(17/28)Gamma(19/28)Gamma(27/28))`.
   Reflection-reduced generator:
   `Omega_-28 = Q_-28^(1/2) ~_alg Gamma(1/28)Gamma(9/28)Gamma(11/28)/(Gamma(3/28)Gamma(5/28)Gamma(13/28))`.

## The 24-element augmented basis

Let `B18` denote the current PCF-1 basis:

`B18 = {b_1,...,b_18}`.

H6 recommends

`B24 = B18 union {Omega_-3, Omega_-4, Omega_-7, Omega_-11, Omega_-20, Omega_-28}`.

Do not add all individual Gamma values at the first pass.  Adding the six CM products keeps the PSLQ dimension low and tests the actual Chowla-Selberg prediction.  If this fails, a diagnostic second pass can split one `Omega_D` at a time into its individual Gamma factors to distinguish a wrong normalization from a genuinely missing non-CM period.

## Transcendence and why the old basis missed these constants

Nesterenko's 1996 theorem on modular functions and transcendence questions proves strong algebraic-independence results for modular-function values and includes, in particular, algebraic independence of `pi` and `e^pi`.  Yu's 1989 paper on transcendence and special values of Eisenstein series is part of the same literature: values of Eisenstein/modular objects at algebraic or CM arguments are not expected to collapse into elementary constants.  These results support the empirical fact that an 18-element elementary/transcendental basis can miss CM periods.

The key caution is that transcendence theory is not a PSLQ-completeness theorem.  Chowla-Selberg identifies the right Gamma-products for elliptic CM periods; Nesterenko/Yu explain why such products are genuinely new relative to elementary constants; KZ explains why they are periods.  None proves that a given PCF limit equals a CM elliptic period.

## Modern RM/Stark/Borcherds fallback

Recent Darmon-Vonk and Darmon-Pozzi-Vonk work concerns real-quadratic analogues of singular moduli, rigid meromorphic cocycles, real-quadratic Borcherds products, and values at real multiplication points.  I did not find a reliable accessible tri-author Anderson-Darmon-Vonk Gamma-product paper; web searches around Anderson/Vonk produced noisy or unrelated arXiv hits, so the fallback claim here is grounded only in the verified Darmon-Vonk publication list and the JEMS Darmon-Pozzi-Vonk paper.  This RM literature is not needed for a plain imaginary-CM Chowla-Selberg period.  It becomes relevant only if the PSLQ test finds that one of the six limits contains a regulator/Stark-unit/Borcherds-product factor in addition to the CM period.  The most plausible stress cases are `Q_L15` (`D=-20`, class number two) and `V_quad` (`D=-11`, already tied in the SIARC stack to a Painleve-III/Stokes channel).

## Prediction

Top-line H6 prediction: **the 24-element Chowla-Selberg basis should detect all six**, with medium confidence.  This is a prediction, not a theorem.  The reason to predict full detection is that all six discriminants are imaginary-quadratic CM orders and Chowla-Selberg supplies exactly one missing period generator per order.  The reason to keep confidence at medium is that PCF-1 has not yet proved the PCF-limit-to-elliptic-period map, and the channel/Painleve evidence leaves room for a Stokes or regulator multiplier beyond elliptic CM periods.
