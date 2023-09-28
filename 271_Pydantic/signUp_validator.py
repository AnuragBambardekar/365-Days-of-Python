from pydantic import BaseModel, validator

class SignupForm(BaseModel):
    username: str
    email: str
    password: str

    @validator("username")
    def validate_username(cls, value):
        # Username should be at least 5 characters long
        if len(value) < 5:
            raise ValueError("Username must be at least 5 characters long")
        
        # Username should not contain special characters or spaces
        if not value.isalnum():
            raise ValueError("Username must consist of alphanumeric characters only")

        return value

    @validator("email")
    def validate_email(cls, value):
        # You can add more specific email validation logic here
        # For simplicity, we'll just check for "@" in the email address
        if "@" not in value:
            raise ValueError("Invalid email address")

        return value

    @validator("password")
    def validate_password(cls, value):
        # Password length should be at least 8 characters
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        # Password should contain at least one uppercase letter
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")

        # Password should contain at least one lowercase letter
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter")

        # Password should contain at least one digit
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")

        # Password should contain at least one special character
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in value):
            raise ValueError("Password must contain at least one special character")

        return value

# Example usage:

signup_data = {
    "username": "user123",
    "email": "user@example.com",
    "password": "P@ssw0rd"
}

try:
    user_signup = SignupForm(**signup_data)
    print("Signup data is valid!")
except ValueError as e:
    print(f"Invalid signup data: {e}")
