import sympy as sp

z,p,q,t,th0,th1,thi=sp.symbols('z p q t theta0 theta1 theta_infinity')
I=sp.I
sqrt=sp.sqrt
D=z*(z-1)

def family_entries(square_has_t):
    a = p + sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q) - sp.Rational(1,2)*t*(z-q)**2
    c = -(z-q)/(q-1)
    s = p + sp.Rational(1,2)*(q-1)*q*(t if square_has_t else 1)
    br = s**2 - th1**2/sp.Integer(4) + (q-1)*(th0**2/sp.Integer(4)-th1**2/sp.Integer(4)-q*thi**2/sp.Integer(4))
    f1 = p + sp.Rational(1,2)*((q-1)*q*t - th0 + q*thi)
    f2 = p + sp.Rational(1,2)*((q-1)*q*t + th0 + q*thi)
    b = -z*br/q - (q-1)*f1*f2/q
    return a,b,c

print('BATCH determinant variants: in=3 out=3', flush=True)
aP,bP,cP = family_entries(square_has_t=False)
aC,bC,cC = family_entries(square_has_t=True)
res_print = sp.factor(sp.together((-aP.subs(z,1)**2 - bP.subs(z,1)*cP.subs(z,1)) + th1**2/sp.Integer(4)))
res_corr = sp.factor(sp.together((-aC.subs(z,1)**2 - bC.subs(z,1)*cC.subs(z,1)) + th1**2/sp.Integer(4)))
print('printed_det_residual_factorized =', res_print, flush=True)
print('corrected_det_residual_factorized =', res_corr, flush=True)
assert sp.simplify(sp.cancel(sp.together(res_print))) != 0
assert sp.simplify(sp.cancel(sp.together(res_corr))) == 0
print('b_printed_minus_corrected_factorized =', sp.factor(sp.together(bP-bC)), flush=True)
# deliberately wrong variant: put U=t+1 in the missing multiplier slot.
U=sp.symbols('U')
sU = p + sp.Rational(1,2)*(q-1)*q*U
f1 = p + sp.Rational(1,2)*((q-1)*q*t - th0 + q*thi)
f2 = p + sp.Rational(1,2)*((q-1)*q*t + th0 + q*thi)
brU = sU**2 - th1**2/sp.Integer(4) + (q-1)*(th0**2/sp.Integer(4)-th1**2/sp.Integer(4)-q*thi**2/sp.Integer(4))
bU = -z*brU/q - (q-1)*f1*f2/q
res_wrong = sp.factor(sp.together((-aC.subs(z,1)**2 - bU.subs(U,t+1).subs(z,1)*cC.subs(z,1)) + th1**2/sp.Integer(4)))
print('wrong_U_t_plus_1_residual_factorized =', res_wrong, flush=True)
assert sp.simplify(sp.cancel(sp.together(res_wrong))) != 0
for i,subs in enumerate([
    {p: sp.Rational(2,7)+sp.I/sp.Integer(5), q: sp.Rational(5,3), t: sp.Rational(-3,8)+sp.I/sp.Integer(11), th0: sp.Rational(7,10), th1: sp.Rational(4,9)+sp.I/sp.Integer(6), thi: sp.Rational(-5,12)},
    {p: sp.Rational(-1,4)+2*sp.I, q: sp.Rational(-2,5), t: sp.Rational(9,13), th0: sp.Rational(3,2)-sp.I/sp.Integer(7), th1: sp.Rational(5,4), thi: sp.Rational(2,3)+sp.I/sp.Integer(8)},
],1):
    rp = sp.N(res_print.subs(subs), 90)
    rc = sp.N(res_corr.subs(subs), 90)
    rw = sp.N(res_wrong.subs(subs), 90)
    print(f'numeric_det_point_{i}_printed_abs = {abs(complex(rp)):.3e}', flush=True)
    print(f'numeric_det_point_{i}_corrected_abs = {abs(complex(rc)):.3e}', flush=True)
    print(f'numeric_det_point_{i}_wrong_abs = {abs(complex(rw)):.3e}', flush=True)
    assert abs(complex(rc)) < 1e-80
    assert abs(complex(rp)) > 1e-6
    assert abs(complex(rw)) > 1e-6

h = -I*sqrt(11)/3
x0 = (-sp.Rational(1,3)-h)/2
x = x0 + h*z
Psys = sp.factor((2*z-1)/D)
Qsys = sp.factor(-x**2/(3*D))
Rsys = sp.factor(sp.together(Qsys - sp.diff(Psys,z)/2 - Psys**2/4))
print('system_map_h =', h, flush=True)
print('system_map_x0 =', x0, flush=True)
print('P_system =', Psys, flush=True)
print('Q_system =', Qsys, flush=True)
print('R_system =', Rsys, flush=True)
rho=sp.Symbol('rho')
for s0 in [0,1]:
    p0 = sp.simplify(sp.limit((z-s0)*Psys, z, s0))
    q0 = sp.simplify(sp.limit((z-s0)**2*Qsys, z, s0))
    ind = sp.factor(rho*(rho-1)+p0*rho+q0)
    print(f'indicial_z{s0}: p0={p0}, q0={q0}, equation={ind}', flush=True)
    assert p0 == 1 and q0 == 0
print('R_system_infinity_limit =', sp.limit(Rsys, z, sp.oo), flush=True)
assert sp.simplify(sp.limit(Rsys,z,sp.oo) - sp.Rational(11,27)) == 0

L=sp.symbols('L')
w=sp.Rational(1,2)/z + sp.Rational(1,2)/(z-1) + L
ric_num=sp.factor(sp.together(sp.diff(w,z)+w**2+Rsys).as_numer_denom()[0])
ric_solutions=sp.solve(sp.Poly(ric_num,z).coeffs(),[L],dict=True)
print('riccati_forced_residual_numerator =', ric_num, flush=True)
print('riccati_forced_lambda_solutions =', ric_solutions, flush=True)
assert ric_solutions == []
R_fake= -sp.diff(w.subs(L,sp.Rational(1,3)),z)-w.subs(L,sp.Rational(1,3))**2
assert sp.simplify(sp.together(sp.diff(w.subs(L,sp.Rational(1,3)),z)+w.subs(L,sp.Rational(1,3))**2+R_fake)) == 0
print('riccati_control_fake_R_accepts = True', flush=True)

a0,b0,c0 = family_entries(square_has_t=True)
a0=a0.subs({th0:0, th1:0}); b0=b0.subs({th0:0, th1:0}); c0=c0
m11=a0/D; m12=b0/D; m21=c0/D
n21=-m21; n22=m11; n12=-m12
Pfam=sp.factor(-sp.diff(n21,z)/n21)
Qfam=sp.factor(sp.together(-(sp.diff(n22,z)+n22**2+n21*n12-(sp.diff(n21,z)/n21)*n22)))
Pdiff=sp.factor(sp.together(Pfam-Psys))
print('P_family_U0_theta0_theta1_0 =', Pfam, flush=True)
print('P_family_minus_P_system =', Pdiff, flush=True)
assert sp.simplify(Pdiff) != 0
sample={q:sp.Rational(2,3), p:sp.Rational(1,5), t:sp.Rational(7,11), thi:sp.Rational(3,13), z:sp.Rational(5,4)}
num_mis=abs(complex(sp.N(Pdiff.subs(sample),90)))
print('numeric_P_mismatch_sample_abs = %.3e' % num_mis, flush=True)
assert num_mis > 1e-6
assert sp.simplify(sp.together(Pfam-Pfam)) == 0
print('P_control_self_comparison_accepts = True', flush=True)
print('all_assertions_passed = True', flush=True)
