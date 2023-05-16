from collections import UserString

class CustomString(UserString):
    def __eq__(self, other):
        # Perform case-insensitive string comparison
        return self.data.lower() == other.lower()

# Create custom string objects
string1 = CustomString("Hello")
string2 = CustomString("hello")

# Perform comparison
print(string1 == string2)  # Output: True
