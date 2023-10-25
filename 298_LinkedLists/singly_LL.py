# Singly Linked list

class ListNode:
    def __init__(self, val, next_node = None) -> None:
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index):
        curr = self.head.next
        i=0
        while curr:
            if i==index:
                return curr.val
            i+=1
            curr=curr.next
        return -1
    
    def insertHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index, val):
        i=0
        curr=self.head
        while i < index and curr:
            i+=1
            curr=curr.next
        
        if curr:
            new_node = ListNode(val)
            new_node.next = curr.next
            curr.next = new_node
            if not new_node.next:
                self.tail = new_node

    def remove(self, index):
        i=0
        curr = self.head
        while i < index and curr:
            i+=1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self):
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
    
linkedList = LinkedList()
linkedList.insertHead(1)
linkedList.insertTail(2)
linkedList.insertTail(3)
linkedList.addAtIndex(3,4)

print(linkedList.getValues())
print(linkedList.get(1))
print(linkedList.remove(1))
print(linkedList.getValues())