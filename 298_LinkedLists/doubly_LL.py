class DoublyListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyListNode(-1)
        self.tail = self.head

    def get(self, index):
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val):
        new_node = DoublyListNode(val)
        new_node.next = self.head.next
        new_node.prev = self.head
        if self.head.next:
            self.head.next.prev = new_node
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val):
        new_node = DoublyListNode(val)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index, val):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr:
            new_node = DoublyListNode(val)
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node
            if not new_node.next:
                self.tail = new_node

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            if curr.next:
                curr.next.prev = curr
            return True
        return False

    def getValues(self):
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

# Example usage:
# Create a new doubly linked list
doublyLinkedList = DoublyLinkedList()

# Test inserting elements at the head
doublyLinkedList.insertHead(1)
doublyLinkedList.insertHead(2)
doublyLinkedList.insertHead(3)

# Check the list after inserting at the head
print(doublyLinkedList.getValues())  # Expected output: [3, 2, 1]

# Test inserting elements at the tail
doublyLinkedList.insertTail(4)
doublyLinkedList.insertTail(5)

# Check the list after inserting at the tail
print(doublyLinkedList.getValues())  # Expected output: [3, 2, 1, 4, 5]

# Test inserting elements at specific indices
doublyLinkedList.addAtIndex(2, 6)
doublyLinkedList.addAtIndex(4, 7)

# Check the list after inserting at specific indices
print(doublyLinkedList.getValues())  # Expected output: [3, 2, 6, 1, 7, 4, 5]

# Test getting the value at a specific index
print(doublyLinkedList.get(3))  # Expected output: 1

# Test removing elements at specific indices
print(doublyLinkedList.remove(2))  # Expected output: True (removing the element at index 2)
print(doublyLinkedList.remove(0))  # Expected output: True (removing the element at index 0)
print(doublyLinkedList.remove(6))  # Expected output: True (removing the element at index 6)

# Check the list after removing elements
print(doublyLinkedList.getValues())  # Expected output: [2, 1, 7, 4, 5]

# Test getting the value at a specific index after removal
print(doublyLinkedList.get(2))  # Expected output: 7

