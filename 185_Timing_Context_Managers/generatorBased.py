# Generator based approach
import time
import contextlib
import math
import numpy as np

@contextlib.contextmanager
def measure_Exec_time(description: str):
    start = time.time()
    yield
    end = time.time()
    elapsed_time = end-start
    print(f"{description}:{elapsed_time}")

with measure_Exec_time("Generator-Based"):
    factorial = math.factorial(1000)
    factorial *= 5
    matrix_a = np.random.rand(1000, 1000)
    matrix_b = np.random.rand(1000, 1000)
    result = np.matmul(matrix_a, matrix_b)

"""
What happens is that entering the context (timing) results in taking the 
current time and playing the ball back to the code inside the context 
using yield . If the code inside of the with-block is executed, 
we jump back to the point right after the yield keyword. 
"""