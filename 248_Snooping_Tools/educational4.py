import pyautogui
import time

# Define the time interval (in seconds) between captures
interval = 1  # 1 second

mouse_data = []

try:
    while True:
        # Capture the current mouse position and timestamp
        timestamp = time.time()
        x, y = pyautogui.position()
        
        mouse_data.append((timestamp, x, y))
        
        time.sleep(interval)

except KeyboardInterrupt:
    with open('mouse_data.txt', 'w') as file:
        for data in mouse_data:
            file.write(f"{data[0]} {data[1]} {data[2]}\n")

    print("Mouse data saved to 'mouse_data.txt'")
