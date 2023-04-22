import random

# Set the random seed to ensure the same result each time the program runs
random.seed(1234)

# Define the characters to use in the password
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# Generate a password by randomly selecting 8 characters from the list of possible characters
password = "".join(random.sample(chars, 8))

# Print the password
print("Your random password is:", password)
