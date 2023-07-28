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