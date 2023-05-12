# example 1: Operator Precedence
result = 2 + 3 * 4
print(result) # Output: 14
""" the multiplication operator has a higher precedence than the addition operator. So, the multiplication operation is performed first, and then the addition operation is performed. As a result, the output is 14."""

# example 2: Associativity
result = 10 - 3 - 2
print(result) # Output: 5
"""
the subtraction operator has left associativity. So, the leftmost subtraction operation is performed first, and then the rightmost subtraction operation is performed. As a result, the output is 5.
"""

# example 3: Parentheses
result = (2 + 3) * 4
print(result) # Output: 20
"""
the parentheses are used to explicitly specify the order of operations. The addition operation inside the parentheses is performed first, and then the multiplication operation is performed. As a result, the output is 20.
"""

# example 4: Multiple Operators
result = 2 + 3 * 4 - 5 / 1
print(result) # Output: 9.0

# example 5: Parentheses and Operators
result = (2 + 3) * (4 - 5) / 1
print(result) # Output: -5.0

# example 6: Chained Operators
result = 2 + 3 < 4 or 5 >= 6 and 7 != 8
print(result) # Output: False

