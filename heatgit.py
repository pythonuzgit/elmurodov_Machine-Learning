#Numerical solution of Heat Equation, here the normal current has been not
#included in the Heat Equation. The Euler method is used to solve this equation. 


import numpy as np

c3 = input('Give the value of heat coefficient c3:')
c2 = input('Give the value of c1')
c1 = input('Give the value of c2')
t0 = input('Give the value of t0')


x = np.linspace(0,ax,Nx) #mesh points in space
dx = x[1] - x[0]
t = np.linspace(0,dt,Nt) #mesh pointive in time
dt = t[1] - t[0]

t2 = np.zeros([Nx]) #unknown t2 at new time level
t1 = np.zeros([Nx]) # t2 at the previous time level


# Set initial condition 
for i in range(0,Nx):
    t1[i] = J(x(i))
    

for j in range(1,Nt-1):
    #Compute t2 at inner mesh points
    for i in range(1,Nx-1):
        t2[i] = t1[i] + dt/c1 * c2/ax * (t1[i+1] - 2 * t1[i] + t1[i-1]) - dt/c1 * c3 * t1(([i]-t0), t[j])
    

#Insert boundary conditions
t2[0] = 0; t2[Nx] = 0

#Update t1 before next step    
t1[:] = t2



        

