import sympy as sp
z=sp.symbols('z')
D=z*(z-1); s=sp.sqrt(-11)
x=(-1+s*(1-2*z))/6
P=(2*z-1)/D
Q=-x**2/(3*D)
R=sp.factor(sp.diff(P,z)/2+P**2/4-Q)
print('P=',sp.factor(P))
print('Q=',sp.factor(Q))
print('R=',R)
for point in [0,1]:
    u=z-point if point else z
    r2=sp.limit(u**2*R,z,point)
    print('finite_point',point,'R_double_coeff=',sp.simplify(r2),'theta_condition=0')
print('R_at_infinity_limit=',sp.limit(R,z,sp.oo))
print('t_squared_from_R=',sp.simplify(4*sp.limit(R,z,sp.oo)))
print('singularity_count_in=3')
print('singularity_count_out finite_regular=2 infinity_irregular_rank1=1')
