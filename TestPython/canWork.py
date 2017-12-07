#Dec.7th

import numpy as np
#from numpy.matlib import randn

print('use list to generate NumPy one dim arrays')
data = [6,7.5,8,0,1]

arr = np.array(data)
print(arr)

print('print data type')
print(arr.dtype)

print "Hello World"

i = 3+ 4
print i

import matplotlib.pyplot as plt
import numpy as np
import pylab

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

plt.imshow(z, cmap = plt.cm.gray);
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
pylab.show()


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.show()



