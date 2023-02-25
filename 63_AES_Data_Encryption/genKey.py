from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 # Bruteforce protection

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Generate a Key
simple_key = get_random_bytes(32)
# Output:- b'pvjL\xf9Oo5\xb4\x10\x13\x99s\xe9z\xed\xf2\xbd\x19c\x11\x83\xe2>\xe9\xc3=?\x12lq'
# print(simple_key)

salt = b'pvjL\xf9Oo5\xb4\x10\x13\x99s\xe9z\xed\xf2\xbd\x19c\x11\x83\xe2>\xe9\xc3=?\x12lq'
password = "mysupersecretkey"

key = PBKDF2(password, salt, dkLen=32)
# print(key)

message = b"Hello Secret World!"
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print(ciphered_data)

# Export this data in a .bin file
with open('encrypted.bin','wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

# Decrypt the bin file
with open('encrypted.bin','rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

# Export the key
with open('key.bin','wb') as f:
    f.write(key)