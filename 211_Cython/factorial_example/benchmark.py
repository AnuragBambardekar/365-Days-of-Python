from timeit import timeit

t1 = timeit(
    "factorial(100)",
    setup="from factorial import factorial",
    number=10_000
)
print(f"Python: {t1:.3f}")

t2 = timeit(
    "factorial(100)",
    setup="from cfactorial import factorial",
    number=10_000
)

print(f"Cython: {t2:.3f}")
print(f"Cython is {t1/t2:.3f}x faster")

from factorial import factorial as python_factorial
from cfactorial import factorial as cython_factorial

# Number for which factorial will be calculated
number = 16 # number > 16 --> overflow error

# Get the result of Python factorial calculation for printing
python_result = python_factorial(number)

# Get the result of Cython factorial calculation for printing
cython_result = cython_factorial(number)

print(f"Python Factorial({number}): {python_result}")
print(f"Cython Factorial({number}): {cython_result}")