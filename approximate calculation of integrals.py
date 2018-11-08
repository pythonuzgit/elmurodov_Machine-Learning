
"""
Integral of (4 - x**2)**(1/2) from a = 0 and b = 2 computed by trapezoidal
rule
"""

import math as mt
from trap import trap

def f(x):
    return (4 - x**2)**(1/2)

a = 0
b = 2

for n in range(0, 2):
    er = 10. **(-n)
    Inew = trap(f, a, b, tol = er)
    print('tol=', er, 'Integral=', Inew)



tol= 1.0 Integral= (2.9957090681024408+0.75j)
tol= 0.1 Integral= (0.13601901796103003+0.001235730667189656j)    

