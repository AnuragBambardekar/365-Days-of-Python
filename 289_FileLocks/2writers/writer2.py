from filelock import FileLock
import time

file_path = "shared_data.txt"

lock = FileLock(file_path + ".lock")

with lock:
    with open(file_path, "a") as file:
        file.write("Process 2 is writing data\n")
    time.sleep(1)  # Simulate a shorter process
