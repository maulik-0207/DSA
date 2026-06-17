"""
Stack (Linked List-based) - Build using a singly linked list
Operations: push(value), pop(), peek(), isEmpty(), size()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0


if __name__ == "__main__":
    pass
