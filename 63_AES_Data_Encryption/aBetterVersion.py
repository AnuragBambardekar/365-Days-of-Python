from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 # Bruteforce protection
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Encrypting function
def encrypt(message, password):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))
    return ciphered_data, cipher.iv, salt

# Decrypting function
def decrypt(ciphered_data, password, iv, salt):
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    return original

# Write the encrypted data to a .bin file
def write_encrypted_data_to_file(ciphered_data, iv, salt, key_file_path, encrypted_data_file_path):
    with open(key_file_path, 'wb') as key_file:
        key_file.write(salt)
        key_file.write(get_random_bytes(16)) # add random padding
        key_file.write(PBKDF2(password, salt, dkLen=32))
    
    with open(encrypted_data_file_path, 'wb') as encrypted_data_file:
        encrypted_data_file.write(iv)
        encrypted_data_file.write(ciphered_data)

# Read the encrypted data from a .bin file
def read_encrypted_data_from_file(key_file_path, encrypted_data_file_path, password):
    with open(key_file_path, 'rb') as key_file:
        salt = key_file.read(16)
        key_file.read(16) # read random padding
    
    with open(encrypted_data_file_path, 'rb') as encrypted_data_file:
        iv = encrypted_data_file.read(16)
        ciphered_data = encrypted_data_file.read()

    original = decrypt(ciphered_data, password, iv, salt)
    return original

# Example usage
password = "mysupersecretkey"
message = b"Hello Secret World #2!"

ciphered_data, iv, salt = encrypt(message, password)
write_encrypted_data_to_file(ciphered_data, iv, salt, 'Newkey.bin', 'Newencrypted.bin')
original = read_encrypted_data_from_file('Newkey.bin', 'Newencrypted.bin', password)

print(original)
