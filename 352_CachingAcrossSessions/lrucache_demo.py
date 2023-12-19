from functools import lru_cache
import time

@lru_cache(maxsize=None)
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

start = time.perf_counter()
for x in range(20000,20100):
    factorial(x)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
for x in range(20000,20100):
    factorial(x)
end = time.perf_counter()
print(end - start)

"""
Time for execution the second time is less.
8.671302000060678
2.429983578622341e-05

lru cache does not allow to export and import the cache, so we write our own decorator
"""

