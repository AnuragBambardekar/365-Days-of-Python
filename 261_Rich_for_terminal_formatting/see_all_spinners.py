import subprocess

# Define the command to run
command = ["python", "-m", "rich.spinner"]

try:
    # Run the command and wait for it to complete
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")
except FileNotFoundError:
    print("The 'python' command was not found. Make sure Python is installed.")
except Exception as e:
    print(f"An error occurred: {e}")
