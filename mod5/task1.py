class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        else:
            val = self.end.data
            if self.end.prev is not None:
                self.end.prev.next = None
                self.end = self.end.prev
            else:
                self.end = None
            return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node

    def print(self):
        current = self.end
        while current is not None:
            print(current.data, end=' ')
            current = current.prev
