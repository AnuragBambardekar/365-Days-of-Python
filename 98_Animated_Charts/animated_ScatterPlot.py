from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
c = np.random.rand(50)
s = 500 * np.random.rand(50)

# Define a function to update the scatter plot on each frame of the animation
def update(frame):
    # Generate some new random data
    x = np.random.rand(50)
    y = np.random.rand(50)
    c = np.random.rand(50)
    s = 500 * np.random.rand(50)
    
    # Update the scatter plot with the new data
    ax.clear()
    ax.scatter(x, y, c=c, s=s, alpha=0.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f'Scatter Plot Animation Frame {frame + 1}')

# Create the initial scatter plot with the first set of random data
ax.scatter(x, y, c=c, s=s, alpha=0.5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('Scatter Plot Animation Frame 1')

# Create the animation object and start the animation
animation = FuncAnimation(fig, update, frames=np.arange(50), interval=100)
plt.show()
