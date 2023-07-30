import pyotp
"""
Open GoogleAuthenticator App in your Phone:
1. Scan the generated QR Code
2. Input the Code shown in the app here
3. Authentication successful if you enter the correct code.
"""
key = "bambaappismakingasupersecretkey"
totp = pyotp.TOTP(key)

while True:
    user_token = input("Enter code: ")
    if totp.verify(user_token):
        print("Authentication successful!")
        break
    else:
        print("Authentication failed!")
