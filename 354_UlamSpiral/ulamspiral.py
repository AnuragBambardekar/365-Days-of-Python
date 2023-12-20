import matplotlib.pyplot as plt

# Set dark background style for the plot
plt.style.use('dark_background')

# Enable interactive mode
plt.ion()

# Function to check if a given number is prime or not
def is_prime(num):
    if num == 1:
        return False

    for x in range(2, num):
        if num % x == 0:
            return False

    return True

# Function to update x and y coordinates based on the state
def march(state, x, y):
    if state == 0:
        x += 1
    elif state == 1:
        y += 1
    elif state == 2:
        x -= 1
    elif state == 3:
        y -= 1

    return x, y

# Initialize variables
l_x = 1
l_y = 0
x = 0
y = 0
state = -1
factor = -1
steps = 1
current_steps = 0

# Create a new figure for the plot
fig, ax = plt.subplots()

# Loop through the range of numbers (1 to 25)
for i in range(1, 2000):
    l_x, l_y = x, y

    current_steps += 1
    if current_steps >= steps:
        factor += 1
        current_steps = 0

        x, y = march(state, x, y)

        state += 1
        if state > 3:
            state = 0

        if factor == 2:
            factor = 0
            steps += 1

    if current_steps != 0:
        x, y = march(state, x, y)

    point1 = [x, y]
    point2 = [l_x, l_y]

    # Plot the line segment
    ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 'r-')

    # Check if the current number is prime
    if is_prime(i):
        ax.text(x, y, str(i), color='white')
        ax.plot([x], [y], 'bo')

    fig.canvas.draw()
    fig.canvas.flush_events()

# Pause for 180 seconds
# plt.pause(180)
plt.show()
