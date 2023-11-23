import os

def rename_images(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)

    # Loop through each file
    for file_name in files:
        # Split the file name into parts using '-' as the separator
        parts = file_name.split('-')

        # Check if the file name has the expected format
        if len(parts) >= 3 and parts[-1].lower().endswith('.png'):
            # Extract the state name from the file name
            state_name = '-'.join(parts[:-2]).lower()

            # Construct the new file name
            new_file_name = f"{state_name}.png"

            # Build the full paths for the old and new file names
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} to {new_file_name}")

# Specify the folder path where the images are located
folder_path = "images"

# Call the function to rename the images in the specified folder
rename_images(folder_path)
