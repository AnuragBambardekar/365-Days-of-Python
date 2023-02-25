# Data Encryption using Python- pycrptodome
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.

# About AES
AES (Advanced Encryption Standard) is a widely used symmetric-key encryption algorithm. It was originally known as Rijndael and was designed by Joan Daemen and Vincent Rijmen. It was selected by the National Institute of Standards and Technology (NIST) as the new Advanced Encryption Standard in 2001 to replace the outdated Data Encryption Standard (DES). <br>

AES is a block cipher, which means that it encrypts data in fixed-size blocks. The block size of AES is 128 bits. AES has three key sizes: 128 bits, 192 bits, and 256 bits. It operates on bytes and is based on substitution-permutation network (SPN) structure. AES is a symmetric-key encryption algorithm, which means that the same key is used for both encryption and decryption. <br>

AES provides strong security and is widely used for data encryption in various applications, such as data storage, communication, and authentication. <br>

## ChatGPT review of the code: (Future Work/Learning Key points)
Using the PyCryptodome library to generate a random key, derive a key from a password using PBKDF2, encrypt a message using AES-CBC, and write the encrypted data and IV (initialization vector) to a file. It then reads the encrypted data and IV from the file, decrypts the data using the same key and IV, and prints the original message. <br>

One issue with this code is that it's not securely storing the key. In the last part of the code, the key is simply written to a file in binary format. If someone gains access to this file, they can easily use the key to decrypt the encrypted data. A better practice would be to encrypt the key itself using a different key or password, or to use a key management system. <br>

Another issue is that the salt used for deriving the key from the password is hardcoded. A better practice would be to generate a random salt for each encryption operation, and store it along with the encrypted data and IV. This makes it more difficult for an attacker to precompute a dictionary of password-derived keys. <br>

Finally, it's worth noting that the code is not handling exceptions or errors, which could lead to unexpected behavior or security vulnerabilities. It's recommended to add proper error handling and logging to your code. <br>