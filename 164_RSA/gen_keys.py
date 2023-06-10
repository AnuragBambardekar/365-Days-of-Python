"""
RSA (Rivest-Shamir-Adleman) is a widely used public-key encryption algorithm. It was invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977 and has become one of the most important cryptographic algorithms.

RSA is based on the mathematical properties of prime numbers and modular arithmetic. It utilizes a pair of keys: a public key and a private key. The public key is used for encryption, while the private key is used for decryption.
"""

import rsa

public_key, private_key = rsa.newkeys(1024)
# print(private_key)

with open("public.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))