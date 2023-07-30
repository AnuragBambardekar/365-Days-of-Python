import pyotp
import qrcode

def generate_secret_key():
    return pyotp.random_base32()

key = "bambaappismakingasupersecretkey"
uri = pyotp.totp.TOTP(key).provisioning_uri(name="bamba98",issuer_name="BAMBA-APP")

print(uri)
qrcode.make(uri).save("new_QR.png")