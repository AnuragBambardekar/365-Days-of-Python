import psutil

def list_processes():
    print("Running processes:")
    processes = psutil.process_iter()

    # Print the PID and name of each process
    for process in processes:
        try:
            pid = process.pid
            name = process.name()
            print(f"PID: {pid}, Name: {name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.kill()
        print("Process with PID", pid, "killed successfully.")
    except psutil.NoSuchProcess:
        print("Process with PID", pid, "does not exist.")

def main():
    while True:
        print("1. List running processes")
        print("2. Kill a process")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            list_processes()
        elif choice == "2":
            pid = int(input("Enter the PID of the process to kill: "))
            kill_process(pid)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
