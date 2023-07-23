first: float = 0.1
second: float = 0.2
third: float = 0.3

def compare_floats(a: float, b: float, tol: float) -> bool:
    absolute_val: float = abs(a-b)
    print(f'{a} - {b} = {a-b}')
    return absolute_val < tol

print(compare_floats(first+second, third, 1e-10)) # True


"""
in-built function: isclose()
"""
import math

print(math.isclose(first+second, third, rel_tol=1e-10))