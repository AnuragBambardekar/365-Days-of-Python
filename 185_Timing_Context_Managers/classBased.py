# Class based approach
import time
import numpy as np

class Timer:
    def __init__(self, description):
        self.description = description

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        self.end = time.time()
        elapsed_time = self.end - self.start
        print(f"{self.description}:{elapsed_time}")

with Timer("Class-based"):
    a = 5+5
    b = 5+6

    matrix_a = np.random.rand(1000, 1000)
    matrix_b = np.random.rand(1000, 1000)
    result = np.matmul(matrix_a, matrix_b)