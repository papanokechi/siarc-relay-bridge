import sympy as sp
p,q,t,th0,th1,thi,z=sp.symbols('p q t theta0 theta1 theta_infinity z')
a = p + sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q) - sp.Rational(1,2)*t*(z-q)**2
c = -(z-q)/(q-1)
# printed p2655 b(z), transcribed after rendered image inspection: first square has no t.
s_print = p + sp.Rational(1,2)*(q-1)*q
s_corr = p + sp.Rational(1,2)*(q-1)*q*t
f1 = p + sp.Rational(1,2)*((q-1)*q*t - th0 + q*thi)
f2 = p + sp.Rational(1,2)*((q-1)*q*t + th0 + q*thi)
def b_from_s(s):
    br = s**2 - th1**2/sp.Integer(4) + (q-1)*(th0**2/sp.Integer(4)-th1**2/sp.Integer(4)-q*thi**2/sp.Integer(4))
    return -z*br/q - (q-1)*f1*f2/q
for name, b in [('printed', b_from_s(s_print)), ('corrected', b_from_s(s_corr))]:
    res=sp.factor(sp.together((-a.subs(z,1)**2 - b.subs(z,1)*c.subs(z,1)) + th1**2/sp.Integer(4)))
    print(f'{name}_residual=', res)
print('printed_minus_corrected_b=', sp.factor(sp.together(b_from_s(s_print)-b_from_s(s_corr))))
# solve for scalar U in missing square p+1/2(q-1)q*U
U=sp.symbols('U')
sU=p+sp.Rational(1,2)*(q-1)*q*U
resU=sp.factor(sp.together((-a.subs(z,1)**2-b_from_s(sU).subs(z,1))+th1**2/sp.Integer(4)))
print('residual_U=',resU)
print('U_solution=',sp.solve(sp.Poly(sp.together(resU).as_numer_denom()[0],p).coeffs(), [U], dict=True))
