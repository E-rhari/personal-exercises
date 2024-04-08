import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.cm as cm


alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def colorMap(phi_m, phi_p):
    return (+ alpha - 2 * np.cos(phi_p)* np.cos(phi_m) - alpha * np.cos(phi_ext - 2* phi_p))


phi_m = np.linspace(0, 2 * np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = colorMap(X,Y).T

fig = plt.figure()

ax = fig.add_subplot(1,2,1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

cb = fig.colorbar(p, shrink=0.5)

plt.show()