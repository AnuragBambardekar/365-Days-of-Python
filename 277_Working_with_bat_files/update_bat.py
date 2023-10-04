# Specify the path to the existing BAT file
existing_bat_file_path = "new_script.bat"

with open(existing_bat_file_path, "r") as bat_file:
    existing_content = bat_file.read()

new_command = "echo New command added."
modified_content = existing_content + "\n" + new_command

with open(existing_bat_file_path, "w") as bat_file:
    bat_file.write(modified_content)

print(f"BAT file '{existing_bat_file_path}' modified successfully!")
