import sympy as sp
z=sp.symbols('z')
p,q,t,th=sp.symbols('p q t th')
th0=sp.Integer(0); th1=sp.Integer(0)
D=z*(z-1)
S0=p+sp.Rational(1,2)*q*(q*t-t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
A0=sp.Matrix([[-S0, (q-1)/q*(S0**2-th0**2/4)],[-q/(q-1), S0]])
A1=sp.Matrix([[S1, th1**2/4-S1**2],[1,-S1]])
Ainf=sp.Matrix([[-t/2,0],[0,t/2]])
A=sp.simplify(A0*(z-1)+A1*z+Ainf*D)
# Corrected b encoded in S0 (includes t in q*(qt-t+th)); printed typo variant for b only:
S0_print = p+sp.Rational(1,2)*q*(q-1) # deliberate printed omission in known typo square
b_print = sp.expand((q-1)/q*(S0_print**2)*(z-1)-S1**2*z)
b_corr = sp.expand(A[0,1])
# N = -A/D for horizontal sections
N=-A/D
def scalar_coeffs_for_component(N, idx):
    a,b,c,d=N[0,0],N[0,1],N[1,0],N[1,1]
    if idx==1:
        P=-(a+d+sp.diff(b,z)/b)
        Q=-(sp.diff(a,z)+b*c-a*sp.diff(b,z)/b-a*d)
    else:
        P=-(a+d+sp.diff(c,z)/c)
        Q=-(sp.diff(d,z)+b*c-d*sp.diff(c,z)/c-a*d)
    return sp.factor(P), sp.factor(Q)
P1,Q1=scalar_coeffs_for_component(N,1)
P2,Q2=scalar_coeffs_for_component(N,2)
s=sp.sqrt(-11)  # alpha->0 choice; sqrt(-11)=i sqrt(11)
x=(-1+s*(1-2*z))/6
PC=sp.factor((2*z-1)/D)
QC=sp.factor(-x**2/(3*D))
print('A='); print(A)
print('bprime_corr='); print(sp.factor(sp.diff(b_corr,z)))
print('P1='); print(P1)
print('P2='); print(P2)
print('PC='); print(PC)
print('QC='); print(QC)
# Match first component: P1-PC=0 implies bprime_corr=0. Q diff numerator coefficients.
bp=sp.factor(sp.diff(b_corr,z))
Qdiff=sp.together(Q1-QC).as_numer_denom()[0]
poly=sp.Poly(sp.expand(Qdiff), z)
eqs=[sp.factor(bp)] + [sp.factor(c) for c in poly.all_coeffs()]
print('eq_count_in=', len(eqs))
sol=sp.solve(eqs, [p,q,t,th], dict=True, manual=False, simplify=False)
print('solution_count_out=', len(sol))
for soln in sol[:20]:
    print('SOL', {str(k): sp.simplify(v) for k,v in soln.items()})
    rP=sp.cancel((P1-PC).subs(soln))
    rQ=sp.cancel((Q1-QC).subs(soln))
    print('rP=', sp.factor(rP))
    print('rQ=', sp.factor(rQ))
# second component impossibility check: P2-PC = -1/(z-q)
print('P2_minus_PC=', sp.factor(P2-PC))
# Typo determinant check at z=1 using det A(1) = det A1 = -theta1^2/4; use th1 symbolic in separate expression.
th1s=sp.symbols('th1')
S1s=p+sp.Rational(1,2)*(q-1)*(q*t+th)
A1s=sp.Matrix([[S1s, th1s**2/4-S1s**2],[1,-S1s]])
S0s=p+sp.Rational(1,2)*q*(q*t-t+th)
# corrected A0 not needed for A(1); printed typo affects b(z) formula at z=1? b(1) = theta1^2/4-S1^2, so det ok. Task says first square in b(z) maybe at A(0). Check det A(0) = -theta0^2/4.
th0s=sp.symbols('th0')
A0corr=sp.Matrix([[-S0s,(q-1)/q*(S0s**2-th0s**2/4)],[-q/(q-1),S0s]])
S0bad=p+sp.Rational(1,2)*q*(q-1) # as printed
A0bad=sp.Matrix([[-S0s,(q-1)/q*(S0bad**2-th0s**2/4)],[-q/(q-1),S0s]])
print('detA0corr_plus=', sp.factor(sp.det(A0corr)+th0s**2/4))
print('detA0bad_plus=', sp.factor(sp.det(A0bad)+th0s**2/4))
