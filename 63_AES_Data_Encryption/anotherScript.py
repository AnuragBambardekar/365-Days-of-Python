# We can use the generated key in other script here to decrypt the 
# encrypted file 
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 # Bruteforce protection

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

with open('key.bin', 'rb') as f:
    key = f.read()

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)