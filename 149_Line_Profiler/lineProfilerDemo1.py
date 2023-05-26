# profile_example.py

import random
from line_profiler import LineProfiler

# Define the function to be profiled
def my_function():
    # Generate a list of random numbers
    numbers = [random.randint(1, 100) for _ in range(1000000)]

    # Sort the numbers
    numbers.sort()

    # Calculate the sum
    total = sum(numbers)

    # Print the result
    print(total)


# Create an instance of LineProfiler
profiler = LineProfiler()

# Add the function to be profiled
profiler.add_function(my_function)

# Run the profiler
profiler.enable()

# Call the function
my_function()

# Disable the profiler and print the results
profiler.disable()
profiler.print_stats()
