a: float = 0.1
b: float = 0.2
c: float = 0.3

print(a+b) # 0.30000000000000004

print((a+b) == c) # False

print((a+b), c) # 0.30000000000000004 0.3

"""
In Python and many other programming languages, floating-point numbers are represented using the IEEE 754 standard. 
This standard represents floating-point numbers in binary, and due to the limitations of binary representation, some 
decimal numbers cannot be precisely represented. 
As a result, there can be small rounding errors when performing arithmetic operations on floating-point numbers.

In your case, the numbers 0.1 and 0.2 cannot be represented exactly in binary, so when you add them together, 
you get a slight rounding error, leading to a result like 0.30000000000000004 instead of the exact 0.3.
"""

print(0.7+0.6) # 1.2999999999999998

balance = 0.7+0.6
if balance >= 1.3:
    balance -= 1.3
    print('Purchase successful!')
else:
    print('Insufficient funds!')