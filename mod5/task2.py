class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def is_empty(self):
        return self.start is None

    def pop(self):
        if self.is_empty():
            return None
        else:
            val = self.start.data
            if self.start == self.end:
                self.start = None
                self.end = None
            else:
                self.start = self.start.nref
                self.start.pref = None
            return val

    def push(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            for i in range(n-1):
                current = current.nref
                if current is None:
                    raise IndexError("Index out of range")
            new_node = Node(val)
            new_node.nref = current.nref
            new_node.pref = current
            if current.nref is not None:
                current.nref.pref = new_node
            current.nref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=' ')
            current = current.nref
