class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return data

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None