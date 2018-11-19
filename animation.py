
    
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.animation as animation

fig = plt.figure(facecolor='white')
ax = plt.axes(xlim=(0, 5), ylim=(-1,1))
line, = ax.plot([],[], lw=3)
ax.grid(True)

def redraw(i):
    x = np.linspace(0, 5, 150)
    y = np.cos(i * x/10)/(1 + x**2)    
    line.set_data(x, y)



anim =animation.FuncAnimation(fig, redraw,frames=100, interval=50)
plt.show()
