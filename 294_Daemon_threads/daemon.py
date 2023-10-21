from threading import Thread
import time

def task():
    for i in range(10):
        print("Hello World!")
        time.sleep(0.5)

t = Thread(target=task, daemon=True)
t.start()
time.sleep(2)
print("Main thread finished")

"""
When Main thread finished, task finishes!

So, Daemon threads automatically end with the main thread.
"""