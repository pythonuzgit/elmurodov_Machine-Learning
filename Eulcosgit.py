# Use of Euler's method


# Importing External Libraries

import numpy as np
from matplotlib import pyplot as plt

#  Defining Basic Data

x0 = 0
y0 = 1
xf = 10
n  = 101
deltax = (xf-x0) / (n-1)

#  Defining x-values

x = np.linspace(x0,xf,n)

#  Initializing Array for y-values

y = np.zeros([n])

#  For Loop for Euler's Method

y[0] = y0
for i in range(1,n):
    y[i] = deltax*(-y[i-1] + np.cos(x[i-1])) + y[i-1]


#  Plotting the Solution

plt.plot(x,y, 'o')
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.title("Approximate solution with Forward Eulers Method")

plt.show()          

