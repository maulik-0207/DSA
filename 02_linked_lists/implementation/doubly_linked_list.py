"""
Doubly Linked List - Build with prev + next pointers
Operations: insertAtHead(value), insertAtTail(value), insertAt(index, value),
            deleteAtHead(), deleteAtTail(), deleteAt(index),
            search(value), reverse(), traverse(), traverseBackward(), size()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


if __name__ == "__main__":
    pass
