import sympy as sp
# Import by executing solve_pk expressions and substitute copied solution, print coeff residuals numeric
p,q,K=sp.symbols('p q K'); I=sp.I; rt3=sp.sqrt(3); rt11=sp.sqrt(11); rt33=sp.sqrt(33); z=sp.symbols('z')
t=2*I*rt11/(3*rt3); th=rt3/9
solq=sp.Rational(1,2) + sp.Rational(15111,30602)*rt33*I + sp.Rational(107551,122408)*rt11*I
solp=(-sp.Integer(40987214852324)*rt33 - sp.Integer(70986564486240)*rt11 + sp.Integer(2707938468846372)*I + sp.Integer(1563430598200681)*rt3*I)/(sp.Integer(371497152)*(sp.Integer(60444)*rt33 + sp.Integer(107551)*rt11 + sp.Integer(61204)*I))
solK=(-sp.Integer(120837511)*rt11 - sp.Integer(36145584)*rt33 - sp.Integer(48473568)*rt3*I - sp.Integer(22645480)*I)/(sp.Integer(19008)*(sp.Integer(60444)*rt33 + sp.Integer(107551)*rt11 + sp.Integer(61204)*I))
coeff2=I*(q - 1)*(24*rt33*p + 88*I*q**2 + 4*rt11*q - 88*I*q - 2*rt11 - 6*rt3*I + 11*I)
coeff3=2*(-54*K - 108*p*q + 6*rt3*p*q - 12*rt33*I*p*q - 6*rt3*p + 108*p + 12*rt33*I*p + 44*q**3 - 12*rt33*I*q**3 + 2*rt11*I*q**3 - 87*q**2 - 6*rt3*q**2 - 6*rt11*I*q**2 + 24*rt33*I*q**2 + 6*rt3*q + 48*q - 12*rt33*I*q + 5*rt11*I*q - 5 - rt11*I)
coeff4=108*K*q - 108*p**2*q + 108*p**2 - 24*rt33*I*p*q**3 - 12*rt3*p*q**2 + 48*rt33*I*p*q**2 + 12*rt3*p*q + 108*p*q - 24*rt33*I*p*q - 108*p + 44*q**5 - 132*q**4 - 4*rt11*I*q**4 + 131*q**3 + 8*rt11*I*q**3 + 12*rt33*I*q**3 - 43*q**2 + 6*rt3*q**2 - 24*rt33*I*q**2 - 4*rt11*I*q**2 - 6*rt3*q + 12*rt33*I*q
for c in [coeff2, coeff3, coeff4]: print(sp.N(c.subs({p:solp,q:solq,K:solK}),50))
