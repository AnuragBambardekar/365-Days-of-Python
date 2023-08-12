import os

def get_folder_names(directory):
    folder_names = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folder_names.append(item)
    return folder_names

if __name__ == "__main__":
    target_directory = "./"  # Replace with the actual directory path
    folders = get_folder_names(target_directory)
    for folder in folders:
        print(folder)