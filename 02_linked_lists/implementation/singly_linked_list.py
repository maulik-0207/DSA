"""
Singly Linked List - Build the node class and list from scratch
Operations: insertAtHead(value), insertAtTail(value), insertAt(index, value),
            deleteAtHead(), deleteAtTail(), deleteAt(index),
            search(value), reverse(), traverse(), size()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    pass
