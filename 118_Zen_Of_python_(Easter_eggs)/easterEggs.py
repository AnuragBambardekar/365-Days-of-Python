# from __future__ import braces
# import __hello__
# import __phello__
import this
# import spam
# import antigravity
# print(spam.ham())

"""
The "import this" Easter egg prints "The Zen of Python", which is a collection of guiding principles for writing computer programs in Python. 
You can see it by opening a Python interpreter and typing import this.

The "import hello" Easter egg prints "Hello, world!" when you call the hello() function. You can see it by typing import __hello__ into a 
Python interpreter and then calling the function by typing __hello__.hello().

The "import antigravity" Easter egg opens a web browser to a comic about a programmer who discovers the secret to flying. You can see it 
by typing import antigravity into a Python interpreter.
"""

print(hash(float('inf')))
print(hash(float('nan'))) # Not outputting 0

# Metasyntactic variables in Python
spam = ["foo", "bar", "baz"]

for item in spam:
    print(item)

# Print a table
for x in range(1, 11):
    print( repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)) 

# z-fill
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

# format
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print( 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

from math import pi
π = pi
r = 10
area = π * r**2
print(area)

# HELP
import types
help(types.CodeType)
