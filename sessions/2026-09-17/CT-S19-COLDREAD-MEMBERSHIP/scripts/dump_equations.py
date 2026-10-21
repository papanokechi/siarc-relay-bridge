import sympy as sp
z=sp.symbols('z')
p,q,t,th=sp.symbols('p q t th')
D=z*(z-1); s=sp.sqrt(-11)
S0=p+sp.Rational(1,2)*q*(q*t-t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
A0=sp.Matrix([[-S0, (q-1)/q*S0**2],[-q/(q-1), S0]])
A1=sp.Matrix([[S1, -S1**2],[1,-S1]])
Ainf=sp.Matrix([[-t/2,0],[0,t/2]])
A=sp.expand(A0*(z-1)+A1*z+Ainf*D)
N=-A/D
a,b,c,d=N[0,0],N[0,1],N[1,0],N[1,1]
P1=sp.factor(-(sp.diff(b,z)/b))
Q1=sp.factor(-(sp.diff(a,z)+b*c-a*sp.diff(b,z)/b-a*d))
x=(-1+s*(1-2*z))/6
PC=(2*z-1)/D; QC=-x**2/(3*D)
bp=sp.factor(sp.diff(A[0,1],z))
num=sp.Poly(sp.together(Q1-QC).as_numer_denom()[0], z)
print('bp:', bp)
print('degree', num.degree(), 'coeff_count', len(num.all_coeffs()))
for i,coef in enumerate(num.all_coeffs()):
    print('coef',i, sp.factor(coef))
