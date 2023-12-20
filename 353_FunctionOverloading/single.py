# def add(x: int, y: int) -> int:
#     return x+y

# def add(x: float, y:float) -> float:
#     return x+y

from numbers import Number
from functools import singledispatch

@singledispatch
def describe(arg):
    return "Unknown type"

@describe.register
def _(arg:str):
    return "A String"

@describe.register(list)
@describe.register(tuple)
@describe.register(set)
def _(arg):
    return f"A collection of {len(arg)} elements"

@describe.register
def _(arg:Number):
    return "A number"

if __name__ == "__main__":
    print(describe("Hello World"))
    print(describe([1,2,3]))
    print(describe(5.4))
    print(describe({1:"one", 2:"two"}))