# We can generate the same key using the same salt and password again
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 # Bruteforce protection

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'pvjL\xf9Oo5\xb4\x10\x13\x99s\xe9z\xed\xf2\xbd\x19c\x11\x83\xe2>\xe9\xc3=?\x12lq'
password = "mysupersecretkey"

key = PBKDF2(password, salt, dkLen=32)

# So we dont have the key.bin file, but we have the salt and password
# so we can decrypt the encrypted file

with open('encrypted.bin','rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)