import pyotp

# Function to generate a new secret key for the user
def generate_secret_key():
    return pyotp.random_base32()

# Function to generate a TOTP token for the given secret key
def generate_totp_token(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

# Function to verify the provided TOTP token with the user's secret key
def verify_totp_token(secret_key, token):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(token)

if __name__ == "__main__":
    # Step 1: Generate a new secret key for the user
    secret_key = generate_secret_key()

    # Step 2: Share the secret key with the user (e.g., display it as a QR code)
    print("Secret Key:", secret_key)

    totp = pyotp.TOTP(secret_key)
    print(totp.now())

    # Step 3: User enters the TOTP token from their mobile app or other device
    user_token = input("Enter the TOTP token: ")

    # Step 4: Verify the user-provided token with the secret key
    if verify_totp_token(secret_key, user_token):
        print("Authentication successful!")
    else:
        print("Authentication failed!")
