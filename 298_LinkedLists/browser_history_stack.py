from collections import deque

history = deque()

history.appendleft("https://google.com")
history.appendleft("https://twitter.com")
history.appendleft("https://youtube.com")

print(history)

# stacks are LIFO
history.popleft()

print(history)