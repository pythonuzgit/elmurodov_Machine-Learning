# Euler's Method


#Importing External Libraries

import numpy as np
from matplotlib import pyplot as plt

#Defining Basic Data

x0 = 0
y0 = 1
xf = 5
n  = 40
dx = 0.1

#Defining x-values

x = np.linspace(x0,xf,n)

#Initializing Array for y-values

y = np.zeros([n])

#For Loop for Eurler's Maethod

y[0] = y0
for i in range(1,n):
    y[i] = dx * (np.exp(x[i-1])) + y[i-1]
    

#Plotting the Solution
    
plt.plot(x,y, 'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate Solution with Forward Eulers Method")
plt.show()
    
