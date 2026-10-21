import math
from itertools import product

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for k in range(total+1):
        for rest in compositions(total-k, parts-1):
            yield (k,) + rest

def multinomial(total, ks):
    v = math.factorial(total)
    for k in ks:
        v //= math.factorial(k)
    return v

failures=[]
max_failures=[]
for d in range(1,9):
    for n in range(1,13):
        total=d*n
        bal=math.factorial(total)//(math.factorial(n)**d)
        lower_num=d**(d*n)
        # compare lower_num/(dn+1)^(d-1) <= bal without floating point
        lower_den=(d*n+1)**(d-1)
        upper=d**(d*n)
        if not (lower_num <= bal*lower_den and bal <= upper):
            failures.append((d,n,lower_num,lower_den,bal,upper))
        if total <= 30 and d <= 5:
            mx=-1; argmax=[]
            for ks in compositions(total,d):
                c=multinomial(total,ks)
                if c>mx:
                    mx=c; argmax=[ks]
                elif c==mx:
                    argmax.append(ks)
            if mx != bal or tuple([n]*d) not in argmax:
                max_failures.append((d,n,mx,bal,argmax[:10],len(argmax)))
print('checked_sandwich_d=1..8_n=1..12_exact_integer')
print('sandwich_failures=', failures)
print('checked_maximality_by_enumeration_for_d<=5_total<=30')
print('maximality_failures=', max_failures)
print('edge_d1_examples=', [(n, math.factorial(n)//math.factorial(n), 1**n) for n in range(1,6)])
