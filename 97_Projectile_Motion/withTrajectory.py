import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Get user input for initial velocity and launch angle
v0 = float(input("Enter initial velocity (m/s): "))
theta = float(input("Enter launch angle (degrees): "))

# Set up the plot and axis limits
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Projectile Motion Simulation')

# Initialize the projectile and trajectory
projectile, = ax.plot([], [], 'ro', ms=10)
trajectory, = ax.plot([], [])

# Calculate components of initial velocity
v0x = v0 * math.cos(math.radians(theta))
v0y = v0 * math.sin(math.radians(theta))

# Calculate time of flight and maximum height
t_max = 2 * v0y / 9.81
h_max = v0y**2 / (2 * 9.81)

# Calculate range and time intervals
R = v0x * t_max
dt = t_max / 100

# Initialize variables
t = 0
x = 0
y = 0
vx = v0x
vy = v0y
x_list = []
y_list = []

# Define function to update the projectile position and trajectory at each frame
def update(frame):
    global t, x, y, vx, vy, x_list, y_list

    # Calculate new position and velocity
    x = v0x * t
    y = v0y * t - 0.5 * 9.81 * t**2
    vx = v0x
    vy = v0y - 9.81 * t

    # Update lists of position and velocity
    x_list.append(x)
    y_list.append(y)

    # Update the position of the projectile on the plot
    projectile.set_data(x, y)

    # Update the trajectory plot
    trajectory.set_data(x_list, y_list)

    # Increment time
    t += dt

    # Return the projectile and trajectory objects
    return projectile, trajectory

# Create animation object
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the plot
plt.show()
