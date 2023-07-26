import dis
import time

# start = time.perf_counter()
# for x in range(20000000):
#     y = x ** 2
# end = time.perf_counter()

# print(end-start)

# start = time.perf_counter()
# def my_func():
#     for x in range(20000000):
#         y = x ** 2
# my_func()
# end = time.perf_counter()

# print(end-start)

# Function was found to be faster than just the loop


def my_func():
    for x in range(20000000):
        y = x ** 2
my_func()

dis.dis(my_func) # uses STORE_FAST --> local scope
print("===========================================================")
dis.dis("""for x in range(20000000):
                y = x ** 2""") # uses STORE_NAME

"""
 23           0 RESUME                   0

 24           2 LOAD_GLOBAL              1 (NULL + range)
             14 LOAD_CONST               1 (20000000)
             16 PRECALL                  1
             20 CALL                     1
             30 GET_ITER
        >>   32 FOR_ITER                 7 (to 48)
             34 STORE_FAST               0 (x)

 25          36 LOAD_FAST                0 (x)
             38 LOAD_CONST               2 (2)
             40 BINARY_OP                8 (**)
             44 STORE_FAST               1 (y)
             46 JUMP_BACKWARD            8 (to 32)

 24     >>   48 LOAD_CONST               0 (None)
             50 RETURN_VALUE
===========================================================
  0           0 RESUME                   0

  1           2 PUSH_NULL
              4 LOAD_NAME                0 (range)
              6 LOAD_CONST               0 (20000000)
              8 PRECALL                  1
             12 CALL                     1
             22 GET_ITER
        >>   24 FOR_ITER                 7 (to 40)
             26 STORE_NAME               1 (x)

  2          28 LOAD_NAME                1 (x)
             30 LOAD_CONST               1 (2)
             32 BINARY_OP                8 (**)
             36 STORE_NAME               2 (y)
             38 JUMP_BACKWARD            8 (to 24)

  1     >>   40 LOAD_CONST               2 (None)
             42 RETURN_VALUE

"""