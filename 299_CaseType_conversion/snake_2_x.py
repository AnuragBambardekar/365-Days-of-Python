def snake_to_camel(s):
    parts = s.split('_')
    # Capitalize the first letter of each part except the first one
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# Example:
snake_case_string = "my_variable_name_in_snake_case"
print("SNAKE: ", snake_case_string)
camel_case_string = snake_to_camel(snake_case_string)
print("CAMEL: ",camel_case_string)  # This will print "myVariableNameInSnakeCase"


def snake_to_pascal(s):
    parts = s.split('_')
    # Capitalize the first letter of each part
    return ''.join(word.capitalize() for word in parts)

# Example:
snake_case_string = "my_variable_name_in_snake_case"
pascal_case_string = snake_to_pascal(snake_case_string)
print("PASCAL: ",pascal_case_string)  # This will print "MyVariableNameInSnakeCase"

def snake_to_kebab(s):
    return s.replace('_', '-')

# Example:
snake_case_string = "my_variable_name_in_snake_case"
kebab_case_string = snake_to_kebab(snake_case_string)
print("KEBAB: ",kebab_case_string)  # This will print "my-variable-name-in-snake-case"
