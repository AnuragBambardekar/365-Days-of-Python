from collections import UserString

class WrappedString(UserString):
    def reverse(self):
        # Reverse the string in-place
        self.data = self.data[::-1]

# Create a wrapped string object
wrapped_string = WrappedString("Hello, world!")

# Use the wrapped string in existing code
print(wrapped_string.upper())  # Output: HELLO, WORLD!

# Reverse the wrapped string in-place
wrapped_string.reverse()

# Print the reversed string
print(wrapped_string)  # Output: !dlrow ,olleH
