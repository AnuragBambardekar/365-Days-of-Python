def create_function():
    def dynamic_function():
        print("This is a dynamically created function.")
    return dynamic_function

# Creating a function at runtime
new_function = create_function()

# Invoking the dynamically created function
new_function()
