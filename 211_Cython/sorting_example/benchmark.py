from timeit import timeit
import random

values = [random.randint(1,1000) for _ in range(1000)]

t1 = timeit(
    "sort(values)",
    setup="from sort import sort",
    number=1000,
    globals={"values":values}
)
print(f"Python: {t1:.3f}")

t2 = timeit(
    "sort(values)",
    setup="from csort import sort",
    number=1000,
    globals={"values":values}
)

print(f"Cython: {t2:.3f}")
print(f"Cython is {t1/t2:.3f}x faster")