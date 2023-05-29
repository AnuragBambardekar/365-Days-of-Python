import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.animation import FuncAnimation

# Create the figure and axis
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_aspect('equal') # to ensure that shapes appear as they are intended
ax.axis('off')

# Set the radius and center of the clock
radius = 1.0
center = (0, 0)

# Draw the clock face
circle = plt.Circle(center, radius, edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(circle)

# Draw the hour markers
for i in range(1, 13):
    angle = np.deg2rad(i * 30)
    x = center[0] + (radius - 0.1) * np.sin(angle)
    y = center[1] + (radius - 0.1) * np.cos(angle)
    ax.text(x, y, str(i), fontsize=12, ha='center', va='center')

# Initialize the clock hands
hour_hand = ax.plot([], [], color='black', linewidth=4)[0]
minute_hand = ax.plot([], [], color='black', linewidth=3)[0]
second_hand = ax.plot([], [], color='red', linewidth=2)[0]

# Initialize the time display
time_text = ax.text(center[0], center[1] - radius * 0.25, '', fontsize=12, ha='center', va='center')


"""
The angles are converted from degrees to radians using np.deg2rad(). 
The hour hand angle is determined by adding the hour component (multiplied by 30) and a fraction of the minute component (multiplied by 0.5). 
The minute and second hand angles are simply obtained by multiplying the corresponding component by the appropriate factor.
"""
# Function to update the clock
def update_clock(frame):
    now = datetime.datetime.now() # get the current time
    current_hour = now.hour % 12 # hour should be between 1-12, not 0-23
    current_minute = now.minute
    current_second = now.second

    # Update the hour hand
    hour_angle = np.deg2rad((current_hour * 30) + (current_minute * 0.5))
    hour_hand.set_data([center[0], center[0] + radius * 0.5 * np.sin(hour_angle)],
                       [center[1], center[1] + radius * 0.5 * np.cos(hour_angle)])


    """
    center[0] and center[1] represent the x and y coordinates of the center of the clock, respectively.

    radius * 0.7 determines the length of the minute hand. The value 0.7 is a scaling factor that determines the length of the minute hand relative to the clock radius.

    np.sin(minute_angle) calculates the sine of the minute angle, where minute_angle represents the angle in radians for the current minute. 
    The np.sin() function returns the vertical displacement (y-coordinate) of the minute hand.

    np.cos(minute_angle) calculates the cosine of the minute angle, which represents the horizontal displacement (x-coordinate) of the minute hand.

    So, when you put it all together, [center[0], center[0] + radius * 0.7 * np.sin(minute_angle)] gives the x-coordinates of the minute hand, 
    and [center[1], center[1] + radius * 0.7 * np.cos(minute_angle)] gives the y-coordinates of the minute hand.
    """
    # Update the minute hand
    minute_angle = np.deg2rad(current_minute * 6)
    minute_hand.set_data([center[0], center[0] + radius * 0.7 * np.sin(minute_angle)],
                         [center[1], center[1] + radius * 0.7 * np.cos(minute_angle)])

    # Update the second hand
    second_angle = np.deg2rad(current_second * 6)
    second_hand.set_data([center[0], center[0] + radius * 0.9 * np.sin(second_angle)],
                         [center[1], center[1] + radius * 0.9 * np.cos(second_angle)])

    # Update the time display
    time_text.set_text(now.strftime('%H:%M:%S'))

# Create the animation
animation = FuncAnimation(fig, update_clock, interval=1000, blit=False)

# Show the clock
plt.show()
