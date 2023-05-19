import types

def create_function():
    # Define the function's code object
    code = """
def dynamic_function():
    print("This is a dynamically created function.")
"""

    # Compile the code into a code object
    compiled_code = compile(code, "<string>", "exec")

    # Create the function using FunctionType constructor
    dynamic_function = types.FunctionType(compiled_code.co_consts[0], globals())

    return dynamic_function

# Creating a function at runtime
new_function = create_function()

# Invoking the dynamically created function
new_function()
