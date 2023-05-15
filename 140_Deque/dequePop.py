# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([6, 1, 2, 3, 4])
print("deque: ", de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)
