from collections import defaultdict

def fibonacci(n):
    if n <= 1:
        return n
    
    # Create a defaultdict as the memoization cache
    cache = defaultdict(int)

    def fib(n):
        if n <= 1:
            return n
        
        # Check if the result is already in the cache
        if cache[n] != 0:
            return cache[n]
        
        # Calculate and store the result in the cache
        result = fib(n-1) + fib(n-2)
        cache[n] = result
        return result

    return fib(n)

# First call (computes and caches results)
print(fibonacci(6))  # Output: 8

# Second call (retrieves the result from cache)
print(fibonacci(6))  # Output: 8
