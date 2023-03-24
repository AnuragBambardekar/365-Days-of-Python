import os
import shutil

# Define the source and destination directories
source_dir = 'C:/Users/anura/Documents/VSCode_Workspace/365-Days-of-Python/89_FileOrganizing/mix'
destination_dir = 'C:/Users/anura/Documents/VSCode_Workspace/365-Days-of-Python/89_FileOrganizing/sorted'

# Define the file extensions and their corresponding folder names
file_ext_folders = {
    '.txt': 'Text Files',
    '.pdf': 'PDF Files',
    '.png': 'Image Files',
    '.mp3': 'Music Files'
}

# Create the destination directories if they do not exist
for folder_name in file_ext_folders.values():
    folder_path = os.path.join(destination_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Loop through the files in the source directory and move them to their corresponding folders
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1]
        if file_ext in file_ext_folders:
            dest_folder_name = file_ext_folders[file_ext]
            dest_folder_path = os.path.join(destination_dir, dest_folder_name)
            shutil.move(file_path, dest_folder_path)
