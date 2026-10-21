import sympy as sp
import json, hashlib

x,t,u=sp.symbols('x t u')
sqrt=sp.sqrt
I=sp.I

a=3*x**2+x+1
b=6*x+1
c=-x**2
p=sp.simplify(b/a)
q=sp.simplify(c/a)
R=sp.simplify(sp.diff(p,x)/2 + p**2/4 - q)
roots=sp.solve(sp.Eq(a,0), x)

def sstr(z):
    return sp.sstr(sp.simplify(z))

finite=[]
for s in roots:
    p0=sp.simplify(sp.limit((x-s)*p,x,s))
    q0=sp.simplify(sp.limit((x-s)**2*q,x,s))
    lam=sp.symbols('lambda')
    ind=sp.expand(lam*(lam-1)+p0*lam+q0)
    ap=sp.simplify(sp.diff(a,x).subs(x,s))
    log_coeff=sp.simplify(1/ap)
    # analytic solution coefficients y1=1+A1*u+A2*u^2+A3*u^3 up to order
    N=4
    coeffs=sp.symbols('A1:'+str(N+1))
    y=1+sum(coeffs[n-1]*u**n for n in range(1,N+1))
    au=sp.expand(a.subs(x,s+u))
    bu=sp.expand(b.subs(x,s+u))
    cu=sp.expand(c.subs(x,s+u))
    expr=sp.expand(au*sp.diff(y,u,2)+bu*sp.diff(y,u)+cu*y)
    equations=[]
    sol={}
    for power in range(0,N):
        eq=sp.expand(expr.coeff(u,power).subs(sol))
        var=coeffs[power]
        val=sp.solve(sp.Eq(eq,0), var)[0]
        sol[var]=sp.simplify(val)
    finite.append({
        'singularity': sstr(s),
        'a_prime_at_s': sstr(ap),
        'p0_residue': sstr(p0),
        'q0': sstr(q0),
        'indicial_polynomial': sstr(ind),
        'exponents': ['0','0'],
        'exponent_difference': '0',
        'reduction_of_order_log_coefficient_for_y2_when_y1(s)=1': sstr(log_coeff),
        'analytic_solution_coefficients_y1_to_u4': {str(k): sstr(v) for k,v in sol.items()}
    })

# normal form residues at finite roots
residues=[{'singularity':sstr(s),'coefficient_of_(x-s)^-2_in_R':sstr(sp.limit((x-s)**2*R,x,s)),'coefficient_of_(x-s)^-1_in_R':sstr(sp.residue(R,x,s)),'normal_form_indicial':'rho*(rho-1) = coefficient, hence (rho-1/2)^2=0'} for s in roots]

# Infinity normal form in t under x=1/t. Schwarzian zero for Mobius.
Vt=sp.simplify(R.subs(x,1/t)/t**4)
Vt_series=sp.series(Vt,t,0,1) # through t^0 maybe includes pole terms
# coefficients v_-4, v_-3
v_m4=sp.simplify(sp.limit(t**4*Vt,t,0))
v_m3=sp.simplify(sp.limit(t**3*(Vt-v_m4/t**4),t,0))
Aplus=sp.sqrt(v_m4)
Aminus=-sp.sqrt(v_m4)
Bplus=sp.simplify(1 + v_m3/(2*Aplus))
Bminus=sp.simplify(1 + v_m3/(2*Aminus))

# Infinity in x: R expansion at infinity R = r0 + r1/x +...
r0=sp.simplify(sp.limit(R,x,sp.oo))
r1=sp.simplify(sp.limit(x*(R-r0),x,sp.oo))
lamplus=sp.sqrt(r0)
lamminus=-sp.sqrt(r0)
muplus=sp.simplify(r1/(2*lamplus))
muminus=sp.simplify(r1/(2*lamminus))

# original equation in t for y(1/t)
Y=sp.Function('Y')
# derive coefficients manually: y_x=-t^2 Y_t, y_xx=t^4 Y_tt+2t^3Y_t
At=sp.simplify(a.subs(x,1/t)*t**4)
Bt=sp.simplify(2*t**3*a.subs(x,1/t)-t**2*b.subs(x,1/t))
Ct=sp.simplify(c.subs(x,1/t))
# equation At Y_tt + Bt Y_t + Ct Y=0; normalized coefficients
Pt=sp.simplify(Bt/At)
Qt=sp.simplify(Ct/At)

# pole order for Vt: denominator t^4 and nonzero v_m4
pole_order_Vt=4
katz=(pole_order_Vt-2)/2

out={
 'session_id':'CT-S9-PVPARAMS',
 'system': {'a':sstr(a),'b':sstr(b),'c':sstr(c),'a_prime':sstr(sp.diff(a,x)),'b_minus_a_prime':sstr(sp.simplify(b-sp.diff(a,x))), 'exact_self_adjoint':'d/dx[a(x) y_prime] + c(x) y = 0'},
 'finite_singularities': finite,
 'normal_form': {'R_x':sstr(R), 'finite_residues': residues},
 'infinity': {
   'coordinate':'t=1/x',
   'normal_form_V_t': sstr(Vt),
   'normal_form_V_t_series': sstr(Vt_series),
   'pole_order_V_t_at_0': pole_order_Vt,
   'ramification':'unramified (leading term has square root in C, no fractional power of t)',
   'katz_invariant': sstr(sp.Rational(1,1)),
   'V_t_coeff_t^-4': sstr(v_m4),
   'V_t_coeff_t^-3': sstr(v_m3),
   'riccati_formal_S_t_plus': {'A_t^-2':sstr(Aplus),'B_t^-1':sstr(Bplus), 'q_t_integral_leading':'-('+sstr(Aplus)+')/t + ('+sstr(Bplus)+')*log(t)'},
   'riccati_formal_S_t_minus': {'A_t^-2':sstr(Aminus),'B_t^-1':sstr(Bminus), 'q_t_integral_leading':'-('+sstr(Aminus)+')/t + ('+sstr(Bminus)+')*log(t)'},
   'R_x_series_at_infinity_r0_r1': {'r0':sstr(r0),'r1':sstr(r1)},
   'riccati_formal_S_x_plus': {'lambda':sstr(lamplus),'mu_x^-1':sstr(muplus),'q_x_integral_leading':'('+sstr(lamplus)+')*x + ('+sstr(muplus)+')*log(x)'},
   'riccati_formal_S_x_minus': {'lambda':sstr(lamminus),'mu_x^-1':sstr(muminus),'q_x_integral_leading':'('+sstr(lamminus)+')*x + ('+sstr(muminus)+')*log(x)'},
   'original_t_equation_coefficients': {'A_for_Ytt':sstr(At),'B_for_Yt':sstr(Bt),'C_for_Y':sstr(Ct),'P=B/A':sstr(Pt),'Q=C/A':sstr(Qt)}
 }
}
text=json.dumps(out, indent=2, ensure_ascii=False, sort_keys=True)
path='sessions\\2026-09-17\\CT-S9-PVPARAMS\\outputs\\system_c_symbolic_local_data.json'
with open(path,'w',encoding='utf-8') as f: f.write(text+'\n')
print(text)
print('OUTPUT_FILE', path)
print('SHA256', hashlib.sha256((text+'\n').encode('utf-8')).hexdigest())

