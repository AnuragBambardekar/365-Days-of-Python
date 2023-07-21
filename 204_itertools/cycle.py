import itertools as it
import time

colours = ("red","green","blue")

"""cycle is an infinte iterator"""

# for i in it.cycle(colours):
#     print(i)
#     time.sleep(0.5)

"""Same as this construct"""
# while True:
#     for i in range(len(colours)):
#         print(colours[i])
#         time.sleep(0.5)

"""Same as this construct --- according to documentation"""
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

# Using a loop to print the first 10 elements
# for i, element in enumerate(cycle('ABCD')):
#     print(element)
#     time.sleep(0.5)

# if we want to cycle only for a specific number of times
for i in it.chain(*it.tee(colours, 3)):
    print(i)