"""
Solution of nonlinear equation 2 * np.cos(x) + (1 - x)
by using of Bisection method.
"""


import numpy as np
import matplotlib.pyplot as plt
from bisection import bisection



def f(x):
    return 2 * np.cos(x) + (1 - x)   #* np.exp(-x) 

x = np.linspace(-10., 10., 200)

y = f(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
xresult1 = bisection(f, 1, 3)
print('solution(1) = ' , xresult1)
xresult2 = bisection(f, 5, 7)
print('solution(2) = ' , xresult2)
xresult3 = bisection(f, 8, 9)
print('solution(3) = ' , xresult3)


solution(1) =  1.3797576182114426
solution(2) =  5.000000000029104
solution(3) =  8.000000000029104

