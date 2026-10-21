import sympy as sp
z,p,q,t,th0,th1,thi,h=sp.symbols('z p q t theta0 theta1 theta_infinity h')
D=z*(z-1)
a = p + sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q) - sp.Rational(1,2)*t*(z-q)**2
c = -(z-q)/(q-1)
s = p + sp.Rational(1,2)*(q-1)*q*t
br = s**2 - th1**2/sp.Integer(4) + (q-1)*(th0**2/sp.Integer(4)-th1**2/sp.Integer(4)-q*thi**2/sp.Integer(4))
f1 = p + sp.Rational(1,2)*((q-1)*q*t - th0 + q*thi)
f2 = p + sp.Rational(1,2)*((q-1)*q*t + th0 + q*thi)
b = -z*br/q - (q-1)*f1*f2/q
m11=a/D; m12=b/D; m21=c/D; m22=-a/D
# scalar for second component y2 of dY + M Y=0: N=-M, n21=-m21, n22=+m11
n21=-m21; n22=m11; n12=-m12
P= -sp.diff(n21,z)/n21
Q= -(sp.diff(n22,z)+n22**2+n21*n12 - (sp.diff(n21,z)/n21)*n22)
R=sp.factor(sp.together(Q-sp.diff(P,z)/2-P**2/4))
print('P_family=', sp.factor(P))
# system with x=alpha+h z, impose root relation alpha=-? use root alpha, h beta-alpha; h^2=-11/9, x0 alpha. Let's derive with x0 root and h other-root difference.
x0=sp.symbols('x0')
x=x0+h*z
Qsys= -x**2/(3*D) # because h^2 cancels in self-adjoint transformed scalar, using a=3 h^2 D
Psys=sp.diff(sp.log(D),z)
Rsys=sp.factor(sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4))
# constraints: x0 root: 3 x0^2 + x0 +1=0; h = beta-alpha = -? and h^2 relation plus 6x0+? Maybe other root x0+h, sum=-1/3 => 2*x0+h=-1/3
Rsys_sub=sp.factor(sp.together(Rsys.subs(x0, (-sp.Rational(1,3)-h)/2)))
print('Rsys=', Rsys_sub)
# reduce h^2=-11/9 maybe later. For theta=0 search coefficients equation R_family=Rsys.
Rf0=sp.factor(sp.together(R.subs({th0:0, th1:0})))
print('R_family theta0theta1 0 numerator degree:', sp.Poly(sp.together(Rf0).as_numer_denom()[0], z).degree())
# leading at infinity
print('Rfamily_inf=', sp.limit(Rf0, z, sp.oo))
print('Rsys_inf=', sp.limit(Rsys_sub, z, sp.oo))
