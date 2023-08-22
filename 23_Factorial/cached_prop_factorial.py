from functools import cached_property
import sys
import math

# Increase the limit for integer string conversion
sys.set_int_max_str_digits(50000)

class MemoizedCalculator:
    def __init__(self, val):
        self._cache = {}
        self.val = val

    def _compute_factorial(self, n):
        if n not in self._cache:
            self._cache[n] = math.factorial(n)
        return self._cache[n]

    @cached_property
    def factorial(self):
        return self._compute_factorial(self.val)

calculator = MemoizedCalculator(5000)
print(calculator.factorial)
print(calculator.factorial)


