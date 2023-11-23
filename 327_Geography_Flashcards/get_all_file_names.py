import os

def get_state_names(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)

    # Initialize an empty list to store state names
    state_names = []

    # Loop through each file
    for file_name in files:
        # Check if the file has the ".png" extension
        if file_name.lower().endswith('.png'):
            # Remove the ".png" extension
            state_name = file_name[:-4]

            # Append the state name to the list
            state_names.append(state_name)

    return state_names

# Specify the folder path where the PNG files are located
folder_path = "images"

# Call the function to get state names from PNG files in the specified folder
state_names_list = get_state_names(folder_path)

# Print the list of state names
print("List of State Names:")
for state_name in state_names_list:
    print(state_name)
