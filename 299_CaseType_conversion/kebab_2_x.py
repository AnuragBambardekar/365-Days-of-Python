def kebab_to_camel(s):
    parts = s.split('-')
    # Capitalize the first letter of each part except the first one
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# Example:
kebab_case_string = "my-variable-name-in-kebab-case"
print("KEBAB: ", kebab_case_string)
camel_case_string = kebab_to_camel(kebab_case_string)
print("CAMEL: ",camel_case_string)  # This will print "myVariableNameInKebabCase"


def kebab_to_snake(s):
    # Replace hyphens with underscores
    return s.replace('-', '_')

# Example:
kebab_case_string = "my-variable-name-in-kebab-case"
snake_case_string = kebab_to_snake(kebab_case_string)
print("SNAKE: ",snake_case_string)  # This will print "my_variable_name_in_kebab_case"

def kebab_to_pascal(s):
    parts = s.split('-')
    # Capitalize the first letter of each part
    return ''.join(word.capitalize() for word in parts)

# Example:
kebab_case_string = "my-variable-name-in-kebab-case"
pascal_case_string = kebab_to_pascal(kebab_case_string)
print("PASCAL: ",pascal_case_string)  # This will print "MyVariableNameInKebabCase"
