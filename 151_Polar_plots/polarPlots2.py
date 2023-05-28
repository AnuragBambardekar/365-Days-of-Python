import numpy as np
from matplotlib import pyplot as plt

theta1 = np.arange(0.0,(2*np.pi), 0.01)
frequency1 = 2
magnitude1 = np.sin(frequency1 * np.pi * theta1)

magnitude2 = np.arange(0.0, 2.0,0.01)
theta2 = 2*np.pi*magnitude2

fig, (ax1,ax2) = plt.subplots(1,2,subplot_kw={'projection':'polar'})
ax1.plot(theta1, magnitude1)
ax2.plot(theta2, magnitude2)
# ax2.set_thetamax(180)
# ax2.set_thetamax(90)
plt.show()