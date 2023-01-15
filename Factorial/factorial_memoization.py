from functools import lru_cache
from functools import reduce

@lru_cache(maxsize=100)

def factorial_functional(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial_functional(375692736593267592))