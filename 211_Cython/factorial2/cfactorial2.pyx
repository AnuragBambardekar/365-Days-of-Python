# cython: language_level=3

#cpdef long long factorial(int n):
#    cdef long long result = 1
#    cdef int i
#    for i in range(2, n + 1):
#        result *= i
#    return result


import math

cpdef long long factorial(int n):
    # n = 100  # Replace this with the desired number
    result = math.factorial(n)

