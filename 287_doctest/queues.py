# python -m doctest -v queues.py

from collections import deque

class Queue:
    def __init__(self) -> None:
        self.elements = deque()

    def enqueue(self, element):
        """
        Add items to the right end of the queue.

        >>> numbers = Queue()
        >>> numbers
        Queue([])

        >>> for n in range(1,4):
        ...     numbers.enqueue(n)

        >>> numbers
        Queue([1, 2, 3])
        """
        self.elements.append(element)

    def dequeue(self):
        """
        Remove ane return an item from the left end of the queue.
        
        >>> numbers = Queue()
        >>> for n in range(1,4):
        ...     numbers.enqueue(n)

        >>> numbers
        Queue([1, 2, 3])

        >>> numbers.dequeue()
        1
        >>> numbers.dequeue()
        2
        >>> numbers.dequeue()
        3
        >>> numbers
        Queue([])
        """
        return self.elements.popleft()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({list(self.elements)})"