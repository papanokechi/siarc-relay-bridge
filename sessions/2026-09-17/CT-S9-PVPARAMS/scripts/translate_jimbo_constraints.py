import sympy as sp, json, hashlib
th0, tht, thinf = sp.symbols('theta_0 theta_t theta_infty')
alpha=sp.Rational(1,8)*(th0-tht+thinf)**2
beta=-sp.Rational(1,8)*(th0-tht-thinf)**2
gamma=1-th0-tht
delta=-sp.Rational(1,2)
subs={th0:0, tht:0}
out={
  'source_dictionary':'Jimbo p.1152: alpha=1/8(theta_0-theta_t+theta_infty)^2; beta=-1/8(theta_0-theta_t-theta_infty)^2; gamma=1-theta_0-theta_t; delta=-1/2',
  'input_from_system_c_if_finite_scalar_exponent_differences_are_identified_with_jimbo_theta_0_theta_t': {'theta_0':'0','theta_t':'0'},
  'resulting_constraints': {
    'alpha': sp.sstr(sp.simplify(alpha.subs(subs))),
    'beta': sp.sstr(sp.simplify(beta.subs(subs))),
    'gamma': sp.sstr(sp.simplify(gamma.subs(subs))),
    'delta': sp.sstr(delta),
    'relation_beta_plus_alpha': sp.sstr(sp.simplify((alpha+beta).subs(subs)))
  },
  'if_alpha_equals_1_over_6_then': {'theta_infty_squared':'4/3','beta':'-1/6','gamma':'1','delta':'-1/2'},
  'caveat':'This is a formal substitution in Jimbo dictionary only; it is not a proof that scalar System C is embedded in that Lax family or that scalar infinity data fixes theta_infty.'
}
text=json.dumps(out,indent=2,sort_keys=True)
path='sessions\\2026-09-17\\CT-S9-PVPARAMS\\outputs\\jimbo_parameter_constraints.json'
with open(path,'w',encoding='utf-8') as f: f.write(text+'\n')
print(text)
print('OUTPUT_FILE', path)
print('SHA256', hashlib.sha256((text+'\n').encode()).hexdigest())
