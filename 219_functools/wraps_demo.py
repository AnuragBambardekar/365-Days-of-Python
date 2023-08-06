"""
The functools module in Python provides higher-order functions and 
operations on callable objects (functions and methods). It contains 
a set of tools for working with functions and callable objects more 
effectively. 
"""

from functools import wraps, partial, cache

# wraps is a decorator that helps preserve the metadata (like function 
# name, docstring, etc.) 
# of the original function when creating a wrapper or decorator around it.

def with_greeting(func):
    @wraps(func) # Use wraps so that docstring of passed func is used
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    return wrapper

@with_greeting
def add(x,y):
    """Adds two numbers together."""
    print(x+y)

if __name__=="__main__":
    add(2,5)
    print(add.__name__)
    print(add.__doc__) # returns None if @wraps is not used