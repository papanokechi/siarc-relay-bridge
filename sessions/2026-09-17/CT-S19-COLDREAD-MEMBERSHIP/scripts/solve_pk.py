import sympy as sp
p,q,t,th,K=sp.symbols('p q t th K')
z=sp.symbols('z'); I=sp.I; rt11=sp.sqrt(11); s=I*rt11; D=z*(z-1)
S0=p+sp.Rational(1,2)*q*((q-1)*t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
aA=-t*z**2/2+(t-th)*z/2+S0
Q=sp.diff(aA/D,z) - K*(z-q)/((q-1)*D**2) - aA**2/D**2
x=(-1+s*(1-2*z))/6; QC=-x**2/(3*D)
poly=sp.Poly(sp.expand(sp.together(Q-QC).as_numer_denom()[0]),z)
coeffs=poly.all_coeffs()
print('coeffs')
for i,c in enumerate(coeffs): print(i, sp.factor(c))
# derive t, theta; then solve p,q,K using remaining.
for sign in [1,-1]:
    tv=sign*2*I*sp.sqrt(11)/(3*sp.sqrt(3))
    thv=sign*sp.sqrt(3)/9
    eqs=[sp.factor(c.subs({t:tv, th:thv})) for c in coeffs[2:]]
    print('sign',sign,'eqs')
    for e in eqs: print(sp.factor(e))
    sol=sp.solve(eqs,[p,q,K],dict=True,simplify=False)
    print('solcount',len(sol))
    for so in sol: print({str(k):sp.simplify(v) for k,v in so.items()})
