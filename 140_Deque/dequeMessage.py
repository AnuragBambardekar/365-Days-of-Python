from collections import deque

message_queue = deque(maxlen=10) # limit the queue size to 10 messages

def receive_message(message):
    message_queue.append(message)

def process_messages():
    while len(message_queue) > 0:
        message = message_queue.popleft()
        print("Processing message:", message)

# example usage:
receive_message("Hello")
receive_message("World")
process_messages() # Output: Processing message: Hello, Processing message: World
