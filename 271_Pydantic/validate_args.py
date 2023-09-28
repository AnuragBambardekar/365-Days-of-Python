from pydantic import validate_arguments

@validate_arguments
def add(x: int, y: int):
    return x+y

print(add(3,5))