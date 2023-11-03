from functools import partial

# Define a simple function
def power(base, exponent):
    return base ** exponent

# Create a new function that calculates the square of a number
square = partial(power, exponent=2)

# Now you can use the "square" function with just one argument
result = square(5)
print(result)  # Output: 25
