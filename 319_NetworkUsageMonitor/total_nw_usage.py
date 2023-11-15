"""
Total Network Usage
"""

import psutil
import time

UPDATE_DELAY = 1

def get_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

io = psutil.net_io_counters()
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

while True:
    time.sleep(UPDATE_DELAY)
    io2 = psutil.net_io_counters()
    us,ds = io2.bytes_sent - bytes_sent, io2.bytes_recv - bytes_recv
    print(f"Upload: {get_size(io2.bytes_sent)}  "
          f", Download: {get_size(io2.bytes_recv)}  "
          f", Upload speed: {get_size(us/UPDATE_DELAY)}/s  "
          f", Download speed: {get_size(ds/UPDATE_DELAY)}/s  ", end="\r")
    bytes_sent, bytes_recv = io2.bytes_sent, io2.bytes_recv