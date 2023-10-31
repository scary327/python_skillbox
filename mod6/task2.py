class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        if len(lst) % 2 != 0:
            self.lst += (None,)

    def __next__(self):
        if not hasattr(self, 'index'):
            self.index = 0
        if self.index >= len(self.lst):
            raise StopIteration
        res = (self.lst[self.index], self.lst[self.index+1])
        self.index += 2
        return res

    def __iter__(self):
        return self


dL = DoubleElement(1,2,3,4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)