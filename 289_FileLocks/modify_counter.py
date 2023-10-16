# accessing same resource from different applications and how to manage that

import time
import threading

lock = threading.Lock()

def increment_counter(amount:int):
    for _ in range(amount):
        with lock:
            with open("counter.txt","r") as f:
                curr = int(f.read())

            curr += 1

            with open("counter.txt","w") as f:
                f.write(str(curr))
            
            time.sleep(1)

for _ in range(15): # 15 threads
    threading.Thread(target=increment_counter, args=(10,)).start()

# Fails because some threads fail, so use file locks