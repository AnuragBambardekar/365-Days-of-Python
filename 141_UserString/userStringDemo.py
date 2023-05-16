"""
In Python's collections module, the UserString class provides a wrapper around string objects, allowing you to easily customize their behavior or create string-like objects with additional functionality.

The UserString class inherits from the built-in str class and provides a mutable string representation. It allows you to modify the underlying string by providing methods that modify the string in place. 
This is in contrast to the str class, which is immutable and doesn't provide in-place modification methods.
"""

from collections import UserString

# Create a UserString object
user_string = UserString("Hello, world!")

# Access the underlying string
print(user_string.data)  # Output: Hello, world!

# Modify the string in place
user_string.data += " Welcome"
print(user_string.data)  # Output: Hello, world! Welcome

# Convert the UserString to a regular string
regular_string = str(user_string)
print(regular_string)  # Output: Hello, world! Welcome
