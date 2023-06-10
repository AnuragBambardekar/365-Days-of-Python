import rsa

with open("164_RSA/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("164_RSA/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = "My username is @yolobamba"

signature = rsa.sign(message.encode(), private_key, "SHA-256")

with open("signature","wb") as f:
    f.write(signature)