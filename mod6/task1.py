class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def get(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current.data

    def remove(self, index):
        if index == 0:
            if self.head is None:
                return
            temp = self.head
            self.head = self.head.next
            del temp
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                return
            current = current.next
        if current is None or current.next is None:
            return
        temp = current.next
        current.next = temp.next
        del temp

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        current = self.head
        for i in range(n - 1):
            if current is None:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next


lst = LinkedList()
lst.push(1)
lst.push(2)
lst.push(3)

for i in lst:
    print(i)

lst.remove(1)

for i in lst:
    print(i)

lst.insert(1, 2)

for i in lst:
    print(i)

print(lst.get(0))
print(lst.get(2))
