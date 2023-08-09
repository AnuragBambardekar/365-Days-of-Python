from numba import jit
import math, random, time
import numpy as np

# @jit(nopython=True)
def some_func(n, x, y):
    z = np.zeros((n, n))
    for i in range(n):
        z += np.sqrt(x**2 + y**2)
    return z

n = 500
x = np.random.rand(n, n)
y = np.random.rand(n, n)

start = time.time()
some_func(n, x, y)
end = time.time()

print(end - start)
# with jit 1.2102551460266113
# without jit 1.249518632888794
