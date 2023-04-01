from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(figsize=(7, 5))
axes = fig.add_subplot(1, 1, 1)
axes.set_ylim(0, 200)
palette = ['blue', 'red', 'green', 'darkorange', 'maroon', 'black']

y1, y2, y3, y4, y5, y6 = [], [], [], [], [], []
max_value = 0

def animation_function(i):
    global max_value
    y1.append(i)
    y2.append(5 * i)
    y3.append(3 * i)
    y4.append(2 * i)
    y5.append(6 * i)
    y6.append(3 * i)

    data = [y1[-1], y2[-1], y3[-1], y4[-1], y5[-1], y6[-1]]
    max_value = max(data)

    plt.xlabel("Country")
    plt.ylabel("GDP of Country")
    plt.bar(["India", "China", "Germany", "USA", "Canada", "UK"], data, color=palette)

    plt.title("Bar Chart Animation (Max Value: {})".format(max_value))

    # Stop the animation when the maximum value is reached
    if max_value >= axes.get_ylim()[1]:
        animation.event_source.stop()

def on_key_press(event):
    if event.key == 'q':
        plt.close(fig)

fig.canvas.mpl_connect('key_press_event', on_key_press)
animation = FuncAnimation(fig, animation_function, interval=50)
plt.show()
