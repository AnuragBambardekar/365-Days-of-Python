# mymodule.py
def some_function():
    print("Function in mymodule.py")

# Trying to Override
if __name__ == "__main__":
    print("This will run when the script is executed directly.")
else:
    print("This will run when the script is imported as a module.")
