import getpass

"""
The getpass module in Python provides a way to securely prompt the user for a password or sensitive information without displaying it 
on the screen. 
It is commonly used when you want to hide user input, such as when requesting a password or other confidential data.
"""

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# You can perform further processing with the username and password
# For example, you can authenticate the user or store the credentials securely

# Here's a simple example that just prints the entered credentials
print("Entered credentials:")
print("Username:", username)
print("Password:", password)
