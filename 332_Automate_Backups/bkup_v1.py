import shutil
import os
import datetime

def backup(source_dir, dest_dir):
    # Create a timestamp for the backup folder
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Create a backup folder with the timestamp
    backup_folder = os.path.join(dest_dir, f"backup_{timestamp}")
    os.makedirs(backup_folder)

    # Copy all files and subdirectories from the source to the backup folder
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(backup_folder, item)

        if os.path.isdir(source_item):
            shutil.copytree(source_item, dest_item)
        else:
            shutil.copy2(source_item, dest_item)

    print(f"Backup completed successfully. Files are saved in {backup_folder}")

# Example usage
source_directory = input("Enter the source directory: ")
destination_directory = "./"

backup(source_directory, destination_directory)
