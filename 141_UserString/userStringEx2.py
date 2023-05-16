from collections import UserString

class MutableString(UserString):
    def append(self, text):
        # Append text to the string in-place
        self.data += text

# Create a mutable string object
my_string = MutableString("Hello")

# Modify the string in place
my_string.append(", world!")

# Print the modified string
print(my_string)  # Output: Hello, world!
