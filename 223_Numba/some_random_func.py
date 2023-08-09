from numba import jit
import math, random, time

@jit(nopython=True)
def some_func(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x**2 + y**2)
    return z

start = time.time()
some_func(10000000)
end = time.time()

print(end-start) 
# 0.5546159744262695 with jit
# 2.9048373699188232 without jit

# if i run it again
start = time.time()
some_func(10000000)
end = time.time()

print(end-start) # 0.08628392219543457 with jit