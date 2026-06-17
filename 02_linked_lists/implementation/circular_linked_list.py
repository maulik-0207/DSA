"""
Circular Linked List - Singly & Doubly circular variants
Operations: insertAtHead(value), insertAtTail(value), deleteAtHead(),
            deleteAtTail(), search(value), traverse(), size()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    pass
