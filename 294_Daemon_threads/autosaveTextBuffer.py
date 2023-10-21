"""
autosave text buffer every 5 seconds.
"""

import threading
import time
from queue import Queue

# Function to perform the auto-save operation
def autosave_data(filename, data_buffer):
    while True:
        time.sleep(5)  # Auto-save every 5 seconds
        data_to_save = data_buffer.copy()  # Copy the buffer
        data_buffer.clear()  # Clear the buffer
        if data_to_save:
            with open(filename, 'a') as file:  # Append to the file
                file.write('\n'.join(data_to_save) + '\n')
            print(f"Saved data to {filename}")

# Main program
if __name__ == "__main__":
    filename = "autosave.txt"

    # Create a buffer to accumulate user input
    data_buffer = []

    # Create and start the auto-save thread
    auto_save_thread = threading.Thread(target=autosave_data, args=(filename, data_buffer), daemon=True)
    auto_save_thread.start()

    try:
        while True:
            user_input = input("Enter text to be saved (or press Enter to exit): ")
            if not user_input:
                break  # Exit the program if Enter is pressed
            data_buffer.append(user_input)  # Add user input to the buffer
    except KeyboardInterrupt:
        # Handle Ctrl+C to exit gracefully
        print("Exiting...")
