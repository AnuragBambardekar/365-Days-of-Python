from collections import deque
queue = deque()

queue.append("John")
queue.append("Bob")
queue.append("Alice")

print(queue)

# queues are FIFO
queue.popleft()

print(queue)