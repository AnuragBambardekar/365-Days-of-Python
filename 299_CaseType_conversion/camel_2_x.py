import re

def camel_to_kebab(s):
    # Use regular expression to insert hyphens before capital letters
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s).lower()

# Example:
camel_case_string = "myVariableNameInCamelCase"
print("CAMEL: ", camel_case_string)
kebab_case_string = camel_to_kebab(camel_case_string)
print("KEBAB: ",kebab_case_string)  # This will print "my-variable-name-in-camel-case"


def camel_to_snake(s):
    # Use regular expression to insert underscores before capital letters
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

# Example:
camel_case_string = "myVariableNameInCamelCase"
snake_case_string = camel_to_snake(camel_case_string)
print("SNAKE: ",snake_case_string)  # This will print "my_variable_name_in_camel_case"


def camel_to_pascal(s):
    # Split the string by capital letters and join them with capitalizing the first letter of each part
    return ''.join(word.capitalize() for word in s.split())

# Example:
camel_case_string = "myVariableNameInCamelCase"
pascal_case_string = camel_to_pascal(camel_case_string)
print("PASCAL: ",pascal_case_string)