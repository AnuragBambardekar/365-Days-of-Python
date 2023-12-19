from functools import wraps
import time, os, pickle

def exportable_cache(func):
    func.cache = {}
    if os.path.exists('factorial_cache.pkl'):
        with open('factorial_cache.pkl','rb') as f:
            func.cache = pickle.load(f)
    
    @wraps(func)
    def wrapper(*args):
        if args in func.cache.keys():
            return func.cache[args]
        else:
            result = func(*args)
            func.cache[args] = result
            return result
    return wrapper

@exportable_cache
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

with open('factorial_cache.pkl','wb') as f:
    pickle.dump(factorial.cache, f)

"""
8.308564999839291
3.060000017285347e-05

2.0200153812766075e-05
3.4499913454055786e-05

2.2200169041752815e-05
2.4700071662664413e-05
"""