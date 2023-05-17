from StringProcessor import StringProcessor

# Define the new uppercase method
def uppercase(self):
    return self.value.upper()

# Monkey patching: Add the uppercase method to the StringProcessor class
StringProcessor.uppercase = uppercase

# Create an instance of StringProcessor
string_obj = StringProcessor("hello")

# Test the new uppercase method
result = string_obj.uppercase()
print(result)  # Output: "HELLO"
