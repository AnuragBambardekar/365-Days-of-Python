import timeit

# Create a set with 1000 elements
s = set(range(1000))

# Create a list with 1000 elements
l = list(range(1000))

# Measure the time it takes to perform a membership test on the set
set_time = timeit.timeit(stmt='999 in s', globals=globals(), number=100000)

# Measure the time it takes to perform a membership test on the list
list_time = timeit.timeit(stmt='999 in l', globals=globals(), number=100000)

# Print the results
print(f'Set time: {set_time:.6f} seconds')
print(f'List time: {list_time:.6f} seconds')
