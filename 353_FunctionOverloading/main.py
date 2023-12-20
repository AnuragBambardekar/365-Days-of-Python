"""
In Python, function overloading can be achieved using the functools.singledispatch decorator. 
The singledispatch decorator allows you to define a function that can have different implementations 
based on the type of the first argument. 
"""

from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported types")

@add.register(int)
@add.register(float)
def _add_numbers(a, b):
    print("Adding two numbers:")
    return a + b

@add.register(str)
def _add_strings(a, b):
    print("Concatenating two strings:")
    return a + b


result1 = add(10, 20)
print("Result 1:", result1)

result2 = add(3.5, 2.5)
print("Result 2:", result2)

result3 = add("Hello", "World")
print("Result 3:", result3)

# Uncommenting the line below will raise NotImplementedError
# add([1, 2, 3], [4, 5, 6])
