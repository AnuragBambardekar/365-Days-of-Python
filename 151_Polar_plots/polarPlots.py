import numpy as np
from matplotlib import pyplot as plt

theta = np.arange(0.0,(2*np.pi), 0.01)
frequency = 2
magnitude = np.sin(frequency * np.pi * theta)

plt.axes(projection = 'polar')
plt.polar(theta,magnitude)
plt.show()
