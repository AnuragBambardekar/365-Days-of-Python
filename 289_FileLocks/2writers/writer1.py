from filelock import FileLock
import time

file_path = "shared_data.txt"

lock = FileLock(file_path + ".lock")

with lock:
    with open(file_path, "a") as file:
        file.write("Process 1 is writing data\n")
    time.sleep(2)  # Simulate a longer process
