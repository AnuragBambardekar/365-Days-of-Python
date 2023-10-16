import subprocess

# Define the number of times to run app.py
num_runs = 10

# Loop to run app.py 10 times
for _ in range(num_runs):
    subprocess.run(['python', 'add.py'])
    subprocess.run(['python', 'mul.py'])
    # subprocess.run(['python', 'sub.py'])
