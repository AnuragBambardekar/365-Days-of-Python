class CircularListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None to represent an empty list

    def is_empty(self):
        return self.head is None

    def get(self, index):
        if self.is_empty():
            return -1

        curr = self.head
        i = 0
        while True:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
            if curr == self.head:
                break

        return -1  # Element not found

    def insert_head(self, val):
        new_node = CircularListNode(val)
        if self.is_empty():
            new_node.next = new_node  # Point to itself if it's the only node
            self.head = new_node
        else:
            new_node.next = self.head
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            self.head = new_node

    def insert_tail(self, val):
        new_node = CircularListNode(val)
        if self.is_empty():
            new_node.next = new_node  # Point to itself if it's the only node
            self.head = new_node
        else:
            new_node.next = self.head
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node

    def add_at_index(self, index, val):
        if index == 0:
            self.insert_head(val)
        else:
            new_node = CircularListNode(val)
            curr = self.head
            i = 0
            while i < index - 1:
                curr = curr.next
                i += 1
                if curr == self.head:
                    break
            new_node.next = curr.next
            curr.next = new_node

    def remove(self, index):
        if self.is_empty():
            return False

        if index == 0:
            if self.head.next == self.head:
                self.head = None  # Removing the last node
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            return True

        curr = self.head
        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1
            if curr == self.head:
                break

        if curr == self.head or curr.next == self.head:
            return False  # Index out of bounds

        curr.next = curr.next.next
        return True

    def get_values(self):
        if self.is_empty():
            return []

        values = []
        curr = self.head
        while True:
            values.append(curr.val)
            curr = curr.next
            if curr == self.head:
                break

        return values

# Example usage:
# Create a new circular linked list
circularLinkedList = CircularLinkedList()

# Test inserting elements at the head
circularLinkedList.insert_head(1)
circularLinkedList.insert_head(2)
circularLinkedList.insert_head(3)

# Check the list after inserting at the head
print(circularLinkedList.get_values())  # Expected output: [3, 2, 1]

# Test inserting elements at the tail
circularLinkedList.insert_tail(4)
circularLinkedList.insert_tail(5)

# Check the list after inserting at the tail
print(circularLinkedList.get_values())  # Expected output: [3, 2, 1, 4, 5]

# Test inserting elements at specific indices
circularLinkedList.add_at_index(2, 6)
circularLinkedList.add_at_index(4, 7)

# Check the list after inserting at specific indices
print(circularLinkedList.get_values())  # Expected output: [3, 2, 6, 1, 7, 4, 5]

# Test getting the value at a specific index
print(circularLinkedList.get(3))  # Expected output: 1

# Test removing elements at specific indices
print(circularLinkedList.remove(2))  # Expected output: True (removing the element at index 2)
print(circularLinkedList.remove(0))  # Expected output: True (removing the element at index 0)
print(circularLinkedList.remove(6))  # Expected output: False (removing the element at index 6)

# Check the list after removing elements
print(circularLinkedList.get_values())  # Expected output: [2, 1, 7, 4, 5]

# Test getting the value at a specific index after removal
print(circularLinkedList.get(2))  # Expected output: 7

# Test an edge case: removing the last element
print(circularLinkedList.remove(0))  # Expected output: True
print(circularLinkedList.get_values())  # Expected output: [1, 7, 4, 5]

# Test an empty list
emptyList = CircularLinkedList()
print(emptyList.get(0))  # Expected output: -1 (element not found)
print(emptyList.remove(0))  # Expected output: False (cannot remove from an empty list)

# Create a circular linked list
circularLinkedList = CircularLinkedList()

# Insert elements
circularLinkedList.insert_head(1)
circularLinkedList.insert_tail(2)
circularLinkedList.insert_tail(3)

# Check the list after inserting at the head and tail
print(circularLinkedList.get_values())  # Expected output: [1, 2, 3]

# Verify the circular behavior by iterating multiple times
for _ in range(2):
    values = circularLinkedList.get_values()
    print(values)  # Expected output: [1, 2, 3] (twice)

