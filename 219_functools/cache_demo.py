"""
The functools module in Python provides higher-order functions and 
operations on callable objects (functions and methods). It contains 
a set of tools for working with functions and callable objects more 
effectively. 
"""

from functools import wraps, partial, cache

# partial allows you to create a new function by fixing some portion of 
# the arguments and keywords of an existing function.

def with_greeting(func):
    @wraps(func) # Use wraps so that docstring of passed func is used
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

@cache
def add(x,y):
    """Adds two numbers together."""
    import time

    print("Running!")

    time.sleep(2)
    return (x+y)

if __name__=="__main__":
    # order of parameters matter
    print("Not Cached: ", add(5,2))
    print("Not Cached: ", add(2,5))
    print("Cached: ", add(2,5)) # because same parameters
    print("Not Cached: ", add(3,5))
