"""
Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. 
It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.
"""

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)
