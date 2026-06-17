"""
Simple Queue (Linked List-based) - Build using linked list nodes
Operations: enqueue(value), dequeue(), front(), rear(), isEmpty(), size()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None


if __name__ == "__main__":
    pass
