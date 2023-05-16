from collections import UserString

class SanitizedString(UserString):
    def __init__(self, text):
        # Sanitize the input string during initialization
        sanitized_text = text.strip().lower()
        super().__init__(sanitized_text)

# Create a sanitized string object
user_input = input("Enter a string: ")
sanitized_string = SanitizedString(user_input)

# Print the sanitized string
print(sanitized_string)
