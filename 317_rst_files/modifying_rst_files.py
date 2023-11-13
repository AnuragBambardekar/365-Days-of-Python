import re

def modify_rst_file(file_path):
    # Read the content of the RST file
    with open(file_path, 'r') as file:
        rst_content = file.read()

    # Perform modifications (for example, replace a specific text)
    modified_content = re.sub(r'OldText', 'NewText', rst_content)

    # Write the modified content back to the RST file
    with open(file_path, 'w') as file:
        file.write(modified_content)

def open_rst_file(file_path):
    # Open and read the content of the RST file
    with open(file_path, 'r') as file:
        rst_content = file.read()
        print(rst_content)

# Example usage:
rst_file_path = 'file2.rst'

# Open and print the content of the original RST file
print("Original RST File:")
open_rst_file(rst_file_path)

# Modify the RST file
modify_rst_file(rst_file_path)

# Open and print the content of the modified RST file
print("\nModified RST File:")
open_rst_file(rst_file_path)
