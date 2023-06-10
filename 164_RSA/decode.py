import rsa

with open("164_RSA/public.pem","rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("164_RSA/private.pem","rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

encrypted_msg = open("164_RSA/encrypted_message","rb").read()

clear_msg = rsa.decrypt(encrypted_msg, private_key)

print(clear_msg.decode())