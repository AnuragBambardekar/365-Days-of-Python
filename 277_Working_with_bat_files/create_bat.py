# Define the content of your batch script
batch_script = """
@echo off
echo Hello, this is a batch file created by Python!
pause
"""

bat_file_path = "C:/Users/anura/Documents/VSCode_Workspace/365-Days-of-Python/277_Working_with_bat_files/new_script.bat"

# Write the batch script content to the .bat file
with open(bat_file_path, "w") as bat_file:
    bat_file.write(batch_script)

print(f"Batch file '{bat_file_path}' created successfully!")
