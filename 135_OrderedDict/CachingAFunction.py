from collections import OrderedDict

# Define a function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Create an ordered dictionary to cache results
cache = OrderedDict()

# Calculate and cache the results
for i in range(6):
    if i in cache:
        # If the result is already cached, retrieve it from cache
        result = cache[i]
    else:
        # If the result is not cached, calculate it and add it to cache
        result = factorial(i)
        cache[i] = result

    # Print the result
    print(f"Factorial of {i} is {result}")

    # Discard the least recently calculated result when the cache size exceeds 3
    if len(cache) > 3:
        cache.popitem(last=False)
