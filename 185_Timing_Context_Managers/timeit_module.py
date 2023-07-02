import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

"""
timeit.timeit() function only accepts strings. 
This can be quite annoying if you want to measure larger functions.
"""

def test():
    """Stupid test function"""
    L = [i for i in range(100)]


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

# This approach is not really pythonic

"""
Another way is to use cProfile module
However, this is not recommended! It is meant to be used to get a sense 
of how long certain code pieces need to be executed and not to measure 
the exact execution time.

$ python -m cProfile <file_name.py>

"""

#===========================================================================#
# Pythonic Solution
"""
>>> import time
>>> start = time.time()
>>> # do some stuff
>>> end = time.time()
>>> print(f"Elapsed Time: {end - start}")
"""
# adding one line of code before and two lines after a code piece we 
# want to measure is an overhead I don’t want to have. So let’s create 
# a context manager for that.




