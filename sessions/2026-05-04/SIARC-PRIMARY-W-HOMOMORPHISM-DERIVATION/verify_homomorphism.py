"""
SIARC primary derivation — verify the homomorphism

  phi : W^aff(B_2)  ->  Aut(D_6^(1))  |x  W((2A_1)^(1))

Generators (Okamoto 1987 §2.1, p.318):
  s_1: (v_1, v_2) -> (v_2, v_1)
  s_2: (v_1, v_2) -> (v_1, -v_2)
  s_0: (v_1, v_2) -> (-1-v_2, -1-v_1)

Image (Sakai 2001, slot 13, Add 6 D_6^(1)-surface) generators on
the parameter quadruple (a_0, a_1, b_0, b_1) with a_0+a_1 =
b_0+b_1 = 1:

  r_0  : a_0 -> -a_0,    a_1 -> a_1+2 a_0   (b unchanged)
  r_1  : a_0 -> a_0+2 a_1, a_1 -> -a_1     (b unchanged)
  r'_0 : b_0 -> -b_0,    b_1 -> b_1+2 b_0   (a unchanged)
  r'_1 : b_0 -> b_0+2 b_1, b_1 -> -b_1     (a unchanged)
  sigma: (a,b) <-> (b,a)                    (Aut(D_6^(1)) factor swap)
  pi   : (a_0,a_1) <-> (a_1,a_0)            (node swap A_1^(1) #1)
  pi'  : (b_0,b_1) <-> (b_1,b_0)            (node swap A_1^(1) #2)

Parameter identification (verified in Phase B):
  a_0 = -v_1,  a_1 = 1 + v_1
  b_0 = -v_2,  b_1 = 1 + v_2
  (so a_0+a_1 = 1, b_0+b_1 = 1, matching Sakai eq. (18))

Proposed map:
  phi(s_1) = sigma
  phi(s_2) = r'_0
  phi(s_0) = sigma * pi * pi'
"""

from sympy import symbols, Tuple, simplify

v1, v2 = symbols('v1 v2')
a0, a1, b0, b1 = symbols('a0 a1 b0 b1')

# ----- Okamoto side -----
def s1_v(v): return (v[1], v[0])
def s2_v(v): return (v[0], -v[1])
def s0_v(v): return (-1 - v[1], -1 - v[0])

def apply_word_v(word, v):
    state = v
    for g in reversed(word):  # apply right-to-left
        state = g(state)
    return state

# ----- Sakai side -----
def r0(s):  a0,a1,b0,b1 = s; return (-a0, a1+2*a0, b0, b1)
def r1(s):  a0,a1,b0,b1 = s; return (a0+2*a1, -a1, b0, b1)
def r0p(s): a0,a1,b0,b1 = s; return (a0, a1, -b0, b1+2*b0)
def r1p(s): a0,a1,b0,b1 = s; return (a0, a1, b0+2*b1, -b1)
def sig(s): a0,a1,b0,b1 = s; return (b0, b1, a0, a1)
def pi_(s): a0,a1,b0,b1 = s; return (a1, a0, b0, b1)
def pip(s): a0,a1,b0,b1 = s; return (a0, a1, b1, b0)

def apply_word_s(word, s):
    state = s
    for g in reversed(word):
        state = g(state)
    return state

def simp4(t):
    return tuple(simplify(x) for x in t)

# ----- compatibility check: phi(g) acting on Sakai params equals
#       g acting on Okamoto params under the identification

def from_v(v):
    # Sakai parameters from (v1,v2) per the chosen identification
    return (-v[0], 1+v[0], -v[1], 1+v[1])

def from_s(s):
    # Inverse: (v1,v2) from Sakai params (uses a0+a1 = b0+b1 = 1 as constraint)
    a0,a1,b0,b1 = s
    return (-a0, -b0)  # since a_0 = -v_1 => v_1 = -a_0

v0 = (v1, v2)
init_s = from_v(v0)

# defining relations of W^aff(B_2):
#   s_i^2 = e (i=0,1,2)
#   (s_1 s_2)^4 = e
#   (s_2 s_0)^4 = e
#   (s_1 s_0)^2 = e
# (B_2^(1) Cartan: a_{12}*a_{21}=2 -> m=4; a_{20}*a_{02}=2 -> m=4;
#  a_{10}*a_{01}=0 -> m=2.)

phi_s1 = [sig]
phi_s2 = [r0p]
phi_s0 = [sig, pi_, pip]   # sigma * pi * pi'

okamoto_gens = {'s0': [s0_v], 's1': [s1_v], 's2': [s2_v]}
phi_gens     = {'s0': phi_s0, 's1': phi_s1, 's2': phi_s2}

def check_relation(name, word_labels):
    o_word = []
    p_word = []
    for lbl in word_labels:
        o_word.extend(okamoto_gens[lbl])
        p_word.extend(phi_gens[lbl])
    o_out = simp4(apply_word_v(o_word, v0))
    p_out = simp4(apply_word_s(p_word, init_s))
    p_via_v = simp4(from_v(o_out))
    ok = (p_out == p_via_v)
    print(f"  [{name}]  Okamoto v -> {o_out} ; phi-image params -> {p_out} ; "
          f"compat={'OK' if ok else 'FAIL'}")
    return ok

print("=== Compatibility with Okamoto -> Sakai parameter map ===")
all_ok = True
for name, word in [
    ("s_0", ['s0']),
    ("s_1", ['s1']),
    ("s_2", ['s2']),
    ("s_1 s_2", ['s1','s2']),
    ("s_2 s_0", ['s2','s0']),
    ("s_1 s_0", ['s1','s0']),
]:
    all_ok &= check_relation(name, word)

print()
print("=== Verifying defining relations of W^aff(B_2) under phi ===")

def ident_check(name, phi_word):
    out = simp4(apply_word_s(phi_word, init_s))
    is_id = (out == init_s)
    print(f"  [{name}] phi-image word applied to (a0,a1,b0,b1) = "
          f"{out}  ;  identity={'YES' if is_id else 'NO'}")
    return is_id

# s_i^2 = e
all_ok &= ident_check("s_1^2", phi_s1*2)
all_ok &= ident_check("s_2^2", phi_s2*2)
all_ok &= ident_check("s_0^2", phi_s0*2)

# (s_1 s_2)^4 = e
all_ok &= ident_check("(s_1 s_2)^4", (phi_s1 + phi_s2)*4)

# (s_2 s_0)^4 = e
all_ok &= ident_check("(s_2 s_0)^4", (phi_s2 + phi_s0)*4)

# (s_1 s_0)^2 = e
all_ok &= ident_check("(s_1 s_0)^2", (phi_s1 + phi_s0)*2)

print()
print("=== Cross-walk: induced action of additional Okamoto symmetries ===")

# Okamoto's "involution of E" (sec.2.3): y : v -> -v.
def y_v(v): return (-v[0], -v[1])

# Predicted: y corresponds to r_0 * r'_0 in W((2A_1)^(1)).
y_param = simp4(apply_word_s([r0, r0p], init_s))
y_via_v = simp4(from_v(y_v(v0)))
print(f"  y (Okamoto v->-v) on params via Okamoto: {y_via_v}")
print(f"  r_0 r'_0 acting on init_s             : {y_param}")
print(f"  match: {'YES' if y_param == y_via_v else 'NO'}")
all_ok &= (y_param == y_via_v)

# Index-2 gap probe: pi alone (Aut(D_6^(1)) leaf-swap on first A_1^(1))
# corresponds to (v_1, v_2) -> (-1-v_1, v_2).
def piv_v(v): return (-1-v[0], v[1])
pi_param = simp4(pi_(init_s))
piv_via_v = simp4(from_v(piv_v(v0)))
print(f"  pi (one-side leaf swap) via params : {pi_param}")
print(f"  predicted (v_1->-1-v_1) -> params  : {piv_via_v}")
print(f"  match: {'YES' if pi_param == piv_via_v else 'NO'}")
all_ok &= (pi_param == piv_via_v)

print()
print("RESULT:", "ALL CHECKS PASS" if all_ok else "SOME CHECK FAILED")
