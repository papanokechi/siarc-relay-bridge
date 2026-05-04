"""OKAMOTO-1987-CONSTRAINT-PIN Phase C substitution check.

We test whether the CT v1.3 sec.3.5 4-tuple
   (alpha_inf, alpha_0, beta_inf, beta_0) = (1/6, 0, 0, -1/2)
satisfies the constraint quoted in the relay-prompt brief
   alpha_inf + alpha_0 + beta_inf + beta_0 = 0
and against Okamoto 1987 sec.2 R1 (the W(B_2) root-system structure
on Okamoto's 2-parameter space V = {(v_1, v_2) = (theta_0, theta_inf)}).

Okamoto 1987 does NOT label four parameters
(alpha_inf, alpha_0, beta_inf, beta_0). Okamoto's P_III' is a
2-parameter family (theta_0, theta_inf) (after eta_Delta = 1
normalization, cf. Okamoto 1987 p.306 lines after eq.(0.1)). The
"R1" canonical relation is thus the affine W(B_2) wall structure on
V, not a 4-tuple sum.

This script makes the arithmetic transparent.
"""
from fractions import Fraction as Q

alpha_inf, alpha_0, beta_inf, beta_0 = Q(1, 6), Q(0), Q(0), Q(-1, 2)

print("=== Phase C: substitution check ===")
print(f"  (alpha_inf, alpha_0, beta_inf, beta_0) = "
      f"({alpha_inf}, {alpha_0}, {beta_inf}, {beta_0})")

s = alpha_inf + alpha_0 + beta_inf + beta_0
print(f"  sum = {s}  (= {float(s):.6f})")
print(f"  sum == 0 ?  {s == 0}")

# Brief-stated constraint:  alpha_inf + alpha_0 + beta_inf + beta_0 = 0.
# Result: -1/3, NOT zero.
assert s == Q(-1, 3), "arithmetic check"

# Now interpret as Okamoto's V-coords.  Okamoto labels are
# v_1 = theta_0, v_2 = theta_inf.  Walls of the W(B_2) chamber are:
#    (alpha_1 | v) = v_1 - v_2 = 0       (s_1)
#    (alpha_2 | v) = v_2 = 0              (s_2)
#    (alpha   | v) = v_1 + v_2 = -1       (affine wall, s_0)
# (Okamoto 1987 sec.2.1, p.317-318.)
# A "Bessel/classical" sub-locus appears at v_1 + v_2 = 0 (Okamoto
# eq. before (0.10) on p.308).  These are the canonical relations.
# None of them is a 4-tuple sum.

print("\n=== Phase C: interpret (1/6, -1/2) as Okamoto (v_1, v_2) ===")
# Most natural mapping in the Jimbo-Miwa convention used by CT v1.3:
# theta_0 corresponds to alpha_0 OR (alpha_0 + beta_0) etc.; the
# correspondence is not unique.  We illustrate the simplest pairing.
# Pairing 1:  v_1 = alpha_inf = 1/6, v_2 = beta_0 = -1/2.
v1, v2 = alpha_inf, beta_0
print(f"  pairing: (v_1, v_2) = ({v1}, {v2})")
print(f"    v_1 - v_2 = {v1 - v2}  (alpha_1 wall)")
print(f"    v_2       = {v2}        (alpha_2 wall)")
print(f"    v_1 + v_2 = {v1 + v2}  (Bessel/highest-root locus)")
print(f"    v_1 + v_2 + 1 = {v1 + v2 + 1}  (affine wall, s_0 fix-line)")

# Conclusion: in Okamoto's labels there IS a clean structural meaning
# for the tuple, but it is the W(B_2)-orbit position, not a Fuchs-style
# linear constraint.  The relay-prompt brief's "alpha+alpha+beta+beta=0"
# is therefore NOT Okamoto 1987 sec.2 R1; it is a different (likely
# Jimbo-Miwa Fuchs-relation or Sakai D_6 surface) convention.

# Conclusion summary:
# - Okamoto 1987 sec.2 R1: encoded as W(B_2) action on
#   V = {(theta_0, theta_inf)}; NO 4-tuple sum constraint exists.
# - The (1/6, 0, 0, -1/2) tuple is thus a labeling-mismatch artifact
#   between CT v1.3 sec.3.5 (modern 4-parameter convention) and
#   Okamoto 1987 (2-parameter convention).
# - Interpretation (a) per relay-prompt sec.0 applies.
print("\n=== Verdict ===")
print("UPGRADE_G18_CLOSED_PARAMETER_CORRESPONDENCE_"
      "OKAMOTO_2PARAM_VS_CT_4TUPLE")
