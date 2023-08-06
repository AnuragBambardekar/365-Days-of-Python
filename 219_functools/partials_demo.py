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

def add(x,y):
    """Adds two numbers together."""
    print(x+y)

if __name__=="__main__":
    add(2,5)

    x=3
    add2and5 = partial(add,x,5)
    x=4
    add2and5()

    add2 = partial(add,2)
    add2(7)


