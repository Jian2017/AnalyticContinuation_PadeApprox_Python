import numpy as np
import matplotlib.pyplot as plt
from pade import rotate, rotateM






# just replace ji with AVERAGE FFT SQUARE of ISing config
# 32 by 64 in this case
# 32 in k space
# 64 in omega_n time

wang=rotateM(c)

w=wang**2

for i in range(w.shape[0]):
    w[i]=w[i]/sum(w[i])

plt.contourf(np.sqrt(w))
plt.show()


"""
from mpl_toolkits.mplot3d import Axes3D



hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')

X, Y = np.meshgrid(range(64), range(32))  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, w)

plt.show()


plt.imshow(w, aspect='auto')
plt.colorbar()
plt.show()
"""




