Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Solution of Integral
>>> 
>>> 
>>> 
>>> import sympy as sp
>>> x = sp.Symbol('x')
>>> sp.integrate(sp.sin(x) * sp.cos(x),x)
sin(x)**2/2
>>> 
>>> from scipy.integrate import quad
>>> import numpy as np
>>> def f(x):
	return np.sin(x) * np.cos(x)

>>> i = quad(f,0,1/2 * np.pi)
>>> print(i[0])
0.49999999999999994
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from scipy.integrate import quad
>>> import numpy as np
>>> def f(x):
	return x * abs(x)

>>> i = quad(f,-4,4)
>>> print(i[0])
0.0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from scipy.integrate import quad
>>> def f(x):
	return abs(5**x - 5**-x)

>>> i =quad(f,-1,0)
>>> print(i[0])
1.9882717905907574
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from scipy.integrate import quad
>>> def f(x):
	return sp.cos(x) * sp.cos(2*x) - sp.sin(x) * sp.sin(2*x)

>>> i = quad(f,0,1/18 * sp.pi)
>>> print(i[0])
0.16666666666666666
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from scipy.integrate import quad
>>> import numpy as np
>>> def f(x):
	return 1 / (np.cos(3*x)**4 - np.sin(3*x)**4)

>>> i = quad(f,-1/24*np.pi,1/24 * np.pi)
>>> print(i[0])
0.2937911956731809
>>> 
