# What does reverse() actually do?

from sys import getsizeof
from typing import Any #  often used when the type of a variable or parameter is unknown or can be of any type.

def display_info(var: Any):
    print(f'{var} ({getsizeof(var)} bytes)')

#iterables
text: str = 'Hello World!'
coordinates: list[str] = ['a1','b2','c3','d4','e5','f6']

display_info(text[::-1])
display_info(coordinates[::-1])

print()

reversed_text = reversed(text)
reversed_coordinates = reversed(coordinates)
# print(reversed(text)) # returns a reversed object

display_info(reversed_text)
display_info(reversed_coordinates)

print()

display_info(''.join(reversed_text)) # size increased 48->61 bytes
display_info(list(reversed_coordinates))


#=========using reversed() is exhaustible============#

# The reversed() function in Python returns an iterator that yields items in reverse order. 
# It is an exhaustible iterator, meaning that once you iterate over all the elements, you cannot iterate over them again unless you recreate the iterator.

coordinates2: list[str] = ['a1','b2','c3','d4','e5','f6']

reversed_coordinates = reversed(coordinates2)

print(next(reversed_coordinates))
print(next(reversed_coordinates))
print(next(reversed_coordinates))
print(list(reversed_coordinates))

# we are slowly exhausting the iterator just like a generator yields a value