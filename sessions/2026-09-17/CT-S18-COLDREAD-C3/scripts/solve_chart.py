import sympy as sp
z,p,q,t,thi,h=sp.symbols('z p q t theta_infinity h')
th0=th1=0
D=z*(z-1)
a = p + sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q) - sp.Rational(1,2)*t*(z-q)**2
c = -(z-q)/(q-1)
s = p + sp.Rational(1,2)*(q-1)*q*t
br = s**2 + (q-1)*(-q*thi**2/sp.Integer(4))
f1 = p + sp.Rational(1,2)*((q-1)*q*t + q*thi)
f2 = p + sp.Rational(1,2)*((q-1)*q*t + q*thi)
b = -z*br/q - (q-1)*f1*f2/q
m11=a/D; m12=b/D; m21=c/D
n21=-m21; n22=m11; n12=-m12
P= -sp.diff(n21,z)/n21
Q= -(sp.diff(n22,z)+n22**2+n21*n12 - (sp.diff(n21,z)/n21)*n22)
R=sp.together(Q-sp.diff(P,z)/2-P**2/4)
x0=(-sp.Rational(1,3)-h)/2
x=x0+h*z
Psys=(2*z-1)/D
Qsys=-x**2/(3*D)
Rsys=sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4)
expr=sp.together(R-Rsys).as_numer_denom()[0]
# reduce h^2=-11/9 in polynomial coefficients via groebner remainder
poly=sp.Poly(expr, z)
coeffs=[]
for coef in poly.all_coeffs():
    rem=sp.rem(sp.Poly(sp.factor(coef), h), sp.Poly(h**2+sp.Rational(11,9), h)).as_expr()
    coeffs.append(sp.factor(rem))
print('coeff_count', len(coeffs))
for i,c0 in enumerate(coeffs): print(i, c0)
# Add obvious t relation from infinity t^2/(4)=-? leading R=-t^2/4? solve all coeffs maybe
sol=sp.solve(coeffs, [p,q,t,thi], dict=True, simplify=False)
print('solutions', sol[:5], 'count', len(sol))
