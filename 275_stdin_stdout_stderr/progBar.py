import sys, time

def progBar(total):
    sys.stdout.write("[")
    for i in range(total):
        time.sleep(0.1)
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]")

print(progBar(50))