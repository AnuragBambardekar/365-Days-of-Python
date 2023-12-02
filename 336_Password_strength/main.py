import re
import string

def check_password_strength(password):
    # Minimum length
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Check for special characters
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    # Check for sequential characters (e.g., "123" or "abc")
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
            return "Weak: Avoid sequential characters like 'abc' or '123'."

    # Check for repeated characters
    if any(password.count(char) > 2 for char in password):
        return "Weak: Avoid repeated characters."

    # Check for commonly used passwords
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        return "Weak: Avoid using common passwords."

    # If all criteria are met, the password is considered strong
    return "Strong: Password meets all criteria."

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
