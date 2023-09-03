from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+"keylogs.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

# Insert Function to log the keystrokes

# Open Listener instance
