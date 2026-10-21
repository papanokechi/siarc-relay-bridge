import sympy as sp
z,L=sp.symbols('z L')
I=sp.I; s=sp.sqrt(11); h=-I*s/3
x0=(-sp.Rational(1,3)-h)/2
x=x0+h*z
D=z*(z-1)
P=(2*z-1)/D
Q=-x**2/(3*D)
R=sp.factor(sp.together(Q-sp.diff(P,z)/2-P**2/4))
w=sp.Rational(1,2)/z+sp.Rational(1,2)/(z-1)+L
res=sp.factor(sp.together(sp.diff(w,z)+w**2+R).as_numer_denom()[0])
print('R=',R)
print('riccati_ansatz_res=',res)
print(sp.solve(sp.Poly(res,z).coeffs(),[L], dict=True))
