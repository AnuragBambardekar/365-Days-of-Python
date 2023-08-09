from numba import jit
import math, random, time
import numpy as np
@jit(nopython=True)
def some_func(n):
    z = np.zeros((n,n))
    for i in range(n):
        x = np.random.rand(n,n)
        y = np.random.rand(n,n)
        z += np.sqrt(x**2 + y**2)
    return z

start = time.time()
some_func(500)
end = time.time()

print(end-start) 
# 2.8455445766448975 without jit
# 3.5984625816345215 with jit

# No speedup?