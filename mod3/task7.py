a = [int(x) for x in input().split()]
print(True if len(set(a)) < len(a) else False)