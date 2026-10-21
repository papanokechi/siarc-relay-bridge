import sympy as sp
p,q,t,th,K=sp.symbols('p q t th K')
z=sp.symbols('z'); I=sp.I; rt11=sp.sqrt(11); s=I*rt11; D=z*(z-1); Dp=sp.diff(D,z)
S0=p+sp.Rational(1,2)*q*((q-1)*t+th)
aA=-t*z**2/2+(t-th)*z/2+S0
an=-aA/D; bn=K/D; cn=(z-q)/((q-1)*D)
Q= -sp.diff(an,z) - bn*cn + an*(sp.diff(bn,z)/bn) - an**2
x=(-1+s*(1-2*z))/6; QC=-x**2/(3*D)
poly=sp.Poly(sp.expand(sp.together(Q-QC).as_numer_denom()[0]),z)
coeffs=poly.all_coeffs()
print('coeffs')
for i,c in enumerate(coeffs): print(i, sp.factor(c))
# solve; coef leading gives t^2 condition perhaps
for sign in [1,-1]:
    tv=sign*2*I*sp.sqrt(11)/(3*sp.sqrt(3))
    # coef1 relation? print solve th from coef1
    coef1=sp.factor(coeffs[1].subs(t,tv)/(q-1))
    thsol=sp.solve(coef1, th)
    print('sign',sign,'theta candidates',thsol)
    for thv in thsol:
        eqs=[sp.factor(c.subs({t:tv, th:thv})) for c in coeffs[2:]]
        sol=sp.solve(eqs,[p,q,K],dict=True,simplify=False)
        print('theta',thv,'solcount',len(sol))
        for so in sol: print({str(k):sp.simplify(v) for k,v in so.items()})
