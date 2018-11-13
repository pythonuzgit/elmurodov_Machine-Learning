import numpy as np
import matplotlib.pyplot as plt
from fredholm import fredholm

def k(x,s):
    return (x - s)**2

def f(x):
    return 3 - 2 * x

a = 0
b = 1

nList = [5, 10, 50]
sglist = ['-', '--', ':']

for kk in range(len(nList)):
    n = nList[kk]
    x = np.linspace(a, b, n + 1)
    y = fredholm(k, f, a, b, n)
    sl = 'n=' + str(n + 1)
    sg = sglist[kk]
    plt.plot(x,y)


plt.xlabel('x')
plt.legend(loc = 0)
plt.show()
    
