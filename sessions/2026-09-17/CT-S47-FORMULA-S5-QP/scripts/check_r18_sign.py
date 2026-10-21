"""CT-S47 - confirm the defect in S16-R18-02 against the record's own words.

The operator's ruling treats this as a PROVEN claim whose *typeset display* was
defective while its result was correct.  Before writing a supersession that says
so, check what the claim text actually contains: the sign may be in the AEAL
record and not only in the appendix.

Both polynomials below are transcribed from the claim text of S16-R18-02 in
CT-S16-MEMBERSHIP-C/claims.jsonl and from nowhere else.  They are typed in
separately and compared; neither is derived from the other.
"""
import sympy as sp

z, p, q, t = sp.symbols("z p q t")

# ---- verbatim from the claim text, first statement -------------------------
#   "the difference being z(4pqt - 4pq - 4pt + 4p + q^3 t^2 - q^3
#    - 2 q^2 t^2 + 2 q^2 + q t^2 - q)/4"
unfactored = z * (4 * p * q * t - 4 * p * q - 4 * p * t + 4 * p
                  + q**3 * t**2 - q**3
                  - 2 * q**2 * t**2 + 2 * q**2
                  + q * t**2 - q) / 4

# ---- verbatim from the claim text, second statement ------------------------
#   "factors as -z(q-1)(t-1)(4p + q^2 t + q^2 - qt - q)/4"
factored_as_recorded = -z * (q - 1) * (t - 1) * (4 * p + q**2 * t + q**2
                                                 - q * t - q) / 4

print("=" * 70)
print("S16-R18-02: the claim's two statements of ONE quantity")
print("=" * 70)
print("unfactored (claim text) :", sp.sstr(sp.expand(unfactored))[:90], "...")
print()

d = sp.simplify(sp.expand(unfactored - factored_as_recorded))
print("unfactored MINUS the recorded factorisation =", sp.sstr(sp.expand(d)))
print("  the claim's own two forms agree:", d == 0)
print()

# what the unfactored form actually factors to
true_fac = sp.factor(unfactored)
print("sympy factor(unfactored) =", sp.sstr(true_fac))
print()

corrected = z * (q - 1) * (t - 1) * (4 * p + q**2 * t + q**2 - q * t - q) / 4
print("PLUS one quarter of the same product reproduces it:",
      sp.simplify(sp.expand(unfactored - corrected)) == 0)
print("MINUS one quarter of the same product reproduces it:",
      sp.simplify(sp.expand(unfactored - factored_as_recorded)) == 0)
print()

# the two differ by exactly a sign, i.e. their sum is twice one of them
print("recorded + corrected == 0 (a pure sign flip, nothing else):",
      sp.simplify(sp.expand(factored_as_recorded + corrected)) == 0)
print()

# ---- a control: the test must be able to reject a near-miss ---------------
print("controls (the comparison must be able to fail)")
near = z * (q - 1) * (t - 1) * (4 * p + q**2 * t + q**2 - q * t + q) / 4
print("  a sign flip on the LAST term is rejected:",
      sp.simplify(sp.expand(unfactored - near)) != 0)
near2 = z * (q - 1) * (t - 1) * (4 * p + q**2 * t + q**2 - q * t - q) / 2
print("  a wrong denominator (2 for 4) is rejected:",
      sp.simplify(sp.expand(unfactored - near2)) != 0)
print("  the corrected form is still accepted:",
      sp.simplify(sp.expand(unfactored - corrected)) == 0)
print()
print("=" * 70)
print("VERDICT: the sign error is present in the CLAIM TEXT of S16-R18-02,")
print("         not only in appendixA.tex's typeset display.")
print("=" * 70)
