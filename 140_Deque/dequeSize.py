# Python Program to demonstrate
# how to find size of a Dequeue
from collections import deque

# initializing deque
de = deque([1, 2, 3, 4, 5, 6])
print("Current Deque: ", de)

# printing current size of deque
print(f"Size of Deque: {len(de)}")

# using pop() to delete element from right end
# deletes 6 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is: ", end = '')
print(de)

# printing current size of deque
print(f"Size of Deque: {len(de)}")

# This code is contributed by Susobhan Akhuli
