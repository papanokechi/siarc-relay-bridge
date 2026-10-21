import sympy as sp
z=sp.symbols('z')
p,q,t,th=sp.symbols('p q t th')
s=sp.sqrt(-11); D=z*(z-1)
S0=p+sp.Rational(1,2)*q*((q-1)*t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
aA=-t*z**2/2+(t-th)*z/2+S0
K=S1**2
# Q numerator under b const; an=-aA/D, bn=K/D, cn=(z-q)/((q-1)D)
# Q = -an' - bn*cn - an^2
Q = sp.diff(aA/D,z) - K*(z-q)/((q-1)*D**2) - aA**2/D**2
x=(-1+s*(1-2*z))/6; QC=-x**2/(3*D)
num=sp.together(Q-QC).as_numer_denom()[0]
poly=sp.Poly(sp.expand(num),z)
print('degree',poly.degree(), 'coeffs', len(poly.all_coeffs()))
for i,c in enumerate(poly.all_coeffs()): print('coef',i, c)
bpeq=sp.expand((q-1)*S0**2-q*S1**2)
print('bpeq_expanded', bpeq)
