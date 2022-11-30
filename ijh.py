# calculate lorenz attractor using IJH method (see IJH paper)
# 2009-02-20
# 2010-01-20: added 3D plot
# 2010-01-20: added 3D plot
# 2010-01-20: added 3D plot     
# 2010-01-20: added 3D plot

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # for 3D plot

# Lorenz parameters and initial conditions
sigma = 10
beta = 8/3
rho = 28
x0 = 0.1
y0 = 0
z0 = 0
t0 = 0
dt = 0.01
n = 10000

# allocate space for arrays
t = np.zeros((n))
x = np.zeros((n))
y = np.zeros((n))
z = np.zeros((n))

# set initial values
t[0] = t0
x[0] = x0
y[0] = y0
z[0] = z0


# implement IJH method
for i in range(n-1):
    t[i+1] = t[i] + dt
    x[i+1] = x[i] + dt*(sigma*(y[i]-x[i]))
    y[i+1] = y[i] + dt*(x[i]*(rho-z[i])-y[i])
    z[i+1] = z[i] + dt*(x[i]*y[i]-beta*z[i])
    
# plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# plot
plt.plot(t,x)
plt.plot(t,y)
plt.plot(t,z)
plt.show()


