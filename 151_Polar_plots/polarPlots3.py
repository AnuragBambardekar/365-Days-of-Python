import numpy as np
import matplotlib.pyplot as plt

# Generate data for the cardioid pattern
theta = np.linspace(0, 2 * np.pi, 1000)
r = 1 - np.cos(theta)

# Create a polar plot
plt.figure(figsize=(8, 8))
plt.polar(theta, r, linewidth=2, color='red')

# Add grid lines
plt.grid(True)

# Add a title
plt.title('Cardioid Polar Plot', fontsize=16)

# Show the plot
plt.show()
