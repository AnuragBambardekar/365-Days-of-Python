import secrets

random_number = secrets.randbelow(10)
print(random_number)

"""
It's important to note that the secrets module is designed for cryptographic applications and provides a higher level of security 
compared to the random module. 
It uses a cryptographically secure random number generator to generate truly random and unpredictable numbers.
"""