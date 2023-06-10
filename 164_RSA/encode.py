import rsa

with open("164_RSA/public.pem","rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("164_RSA/private.pem","rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = "Hello World"

encrypted_msg = rsa.encrypt(message.encode(), public_key)
# print(encrypted_msg)

with open("164_RSA/encrypted_message","wb") as f:
    f.write(encrypted_msg)