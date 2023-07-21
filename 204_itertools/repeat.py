import itertools as it
import time

"""repeat is an infinte iterator"""
repeater = it.repeat(10, 3)

# Printing the values from the iterator
for item in repeater:
    print(item)

print(list(map(pow, range(10), it.repeat(2)))) # 1^2, 2^2, 3^2, 4^2, ..., 9^2