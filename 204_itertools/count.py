import itertools as it
import time

"""count is an infinte iterator"""
counter = it.count(1, 2) # start, step

for _ in range(5):
    print(next(counter))

"""same as: """

def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) --> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

for i, element in enumerate(count(0, 1)):
    print(element)
    time.sleep(0.5)