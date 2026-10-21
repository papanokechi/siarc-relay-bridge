import sympy as sp
z=sp.symbols('z')
p,q,t,th=sp.symbols('p q t th')
s=sp.sqrt(-11); D=z*(z-1)
S0=p+sp.Rational(1,2)*q*(q*t-t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
aA=sp.expand((-S0)*(z-1)+S1*z+(-t/sp.Integer(2))*D)
K=S1**2 # equals (q-1)/q*S0^2 under bp=0, and bA=-K
an=-aA/D; bn=K/D; cn=(z-q)/((q-1)*D)
Q=sp.factor(-sp.diff(an,z)-bn*cn-an**2)
x=(-1+s*(1-2*z))/6; QC=-x**2/(3*D)
num=sp.factor(sp.together(Q-QC).as_numer_denom()[0])
poly=sp.Poly(sp.expand(num),z)
print('degree', poly.degree(), 'coeffs', len(poly.all_coeffs()))
for i,c in enumerate(poly.all_coeffs()): print('coef',i,sp.factor(c))
bpeq=sp.factor((q-1)/q*S0**2-S1**2)
print('bpeq', sp.factor(4*q*bpeq))
# Solve equations: bpeq=0, t2, coef all =0. Use solve on coefficients after t2 substitution? choose t symbols with sqrt.
r=sp.sqrt(sp.Rational(-44,27))
for tv in [r,-r]:
    eqs=[sp.factor((4*q*bpeq).subs(t,tv))]+[sp.factor(c.subs(t,tv)) for c in poly.all_coeffs()[1:]] # coef0 is t2/bp related
    print('trying t=',tv,'eqs',len(eqs))
    sol=sp.solve(eqs,[p,q,th],dict=True,simplify=False,manual=False)
    print('solcount',len(sol))
    for so in sol[:20]: print({str(k):sp.simplify(v) for k,v in so.items()})
