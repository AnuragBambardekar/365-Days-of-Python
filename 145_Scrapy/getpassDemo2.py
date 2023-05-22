import getpass

def main():
    # Get the current user
    username = getpass.getuser()
    print("Current user:", username)

    # Prompt the user for a password
    password = getpass.getpass("Enter your password: ")
    print("Entered password:", password)

    # Custom prompt message
    secret = getpass.getpass(prompt="Enter your secret passphrase: ")
    print("Entered secret passphrase:", secret)

if __name__ == "__main__":
    main()
