from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(figsize=(6, 6))

# Define data for the pie chart
labels = ['Apples', 'Oranges', 'Pears', 'Bananas']
sizes = [20, 30, 25, 15]

# Define initial start angle for the first frame
start_angle = 0

# Define colors for the pie chart wedges
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Define a function to update the pie chart on each frame of the animation
def update(frame):
    # Calculate the new start angle for this frame
    angle = start_angle + frame * 2
    
    # Create the pie chart with the updated start angle
    ax.clear()
    ax.pie(sizes, labels=labels, colors=colors, startangle=angle, autopct='%1.1f%%')
    ax.set_title(f'Pie Chart Animation Frame {frame + 1}')

# Create the initial pie chart with the start angle set to 0
ax = fig.add_subplot(1, 1, 1)
ax.pie(sizes, labels=labels, colors=colors, startangle=start_angle, autopct='%1.1f%%')
ax.set_title('Pie Chart Animation Frame 1')

# Create the animation object and start the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 180, 2), interval=100)
plt.show()
