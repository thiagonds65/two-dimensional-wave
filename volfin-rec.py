import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def condinu(xx, yy):
    u0 = 100000

    return u0

def condinv(xx, yy):
    v = 0

    return v

# Declaring variables
dx = 25 # Variation of x (m)
dy = dx
dt = 0.05 # Variation of t (s)

v = 343 # uarrayeed of sound in air
L = 1000 # Environment length (m)
W = 1000 # Environment width (m)
p = 5 # Final time (s)
k = int(p/dt)

fps = 10 # frame per sec
frn = k # frame number of the animation

m = int(W/dx+1) # Number of uarrayatial nodes
n = int(L/dy+1) # Number of temporal nodes
N = m # Meshsize

c = (v**2)*(dt**2)/(dx*dy) # if c>1, instability of simulation occurs 

# Allocating memory uarrayace in variable (Wave amplitude)

u = np.zeros((m, n))  # initial u (current iteration)
uu = np.zeros((m, n)) # initial u (previous iteration)
uuu = np.zeros((m, n)) # central u (t+dt)
uuuu = np.zeros((m, n)) # current u (t+2dt)

x = np.arange(0, W+dx, dx) 
y = np.arange(0, L+dy, dy)
t = np.arange(0, p+dt, dt)

X,Y = np.meshgrid(x, y)

uarray = np.zeros((m, n, k))

# Initial condition:
# How the environment was when it started to be observed

for i in range(m):
    for j in range(n):
        if(L/2-dx<=x[j]<=L/2+dx):
            if(W/2-dy<=y[i]<=W/2+dy):
                u[i, j] = condinu(x[j], y[i])
            

# Velocity initial condition (du/dt = v) (central condition)
for i in range(1, m - 1):
    for j in range(1, n - 1):
        uuu[i, j] = u[i, j] + dt * condinv(x[j], y[i]) + (c / 2)*(u[i + 1, j] + u[i-1, j] + u[i, j + 1] + u[i, j - 1] - 4 *u[i, j])

for i in range(m):
    for j in range(n):
        uu[i, j] = u[i, j]

''' 
Through Finite Volume Method (FVM), it's possible to obtain the following equation
to approximate a two-dimensional wave
'''
T = 0

#plt.style.use(plt.style.available[0])
o = 0
while(T < p):
    for it in range(0, 5):
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                uuuu[i, j] = 2 * (1 - 2*c)*uuu[i, j] + c*(uuu[i + 1, j] + uuu[i - 1, j] + \
                     uuu[i, j + 1] + uuu[i, j - 1]) - u[i, j]

    for i in range(m):
        for j in range(n):
            uu[i, j] = uuuu[i, j]
            u[i, j] = uuu[i, j]
            uuu[i, j] = uuuu[i, j]
    
    T += dt
    uarray[:,:,o] = uuuu[:, :]
    if o >= k - 1:
        break

    o += 1

def update_plot(frame_number, uarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, uarray[:,:,frame_number], cmap="twilight")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


plot = [ax.plot_surface(X, Y, uarray[:,:,0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(-20000, 100000)
ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(uarray, plot), interval=1000/fps)
ani.save('wave_propagation_2d.gif', writer='imagemagick', fps=fps)
plt.show()
