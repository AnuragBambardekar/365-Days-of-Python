import subprocess

# bat_file = "new_script.bat"
# bat_file = "calculator.bat"
bat_file = "password_gen.bat"

# Run the .bat file using subprocess
try:
    subprocess.run(bat_file, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the .bat file: {e}")

"""
To Execute:
277_Working_with_bat_files> python .\run_bat.py     
"""