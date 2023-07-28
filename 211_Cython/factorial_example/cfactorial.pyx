# cython: language_level=3

cpdef int factorial(int x): #cpdef == cython public definition
    # cdef int f = 1
    cdef long long f = 1
    cdef long long i

    for i in range(x):
        f *= (x-i)

    return f