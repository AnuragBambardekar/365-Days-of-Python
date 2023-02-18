import time
import psutil
def display_usage(cpu_usage, mem_usage, bars=50): # 1 bar for 2% points
    cpu_percent = (cpu_usage/100.0) # cpu_usage = 6%, cpu_percent=0.06
    mem_percent = (mem_usage/100.0)

    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) # ALT + 219
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end="\r") # \r to clear row

while(True):
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent,30)
    time.sleep(0.5)