a = input()
finish = len(a)
for j in range(len(a)-1, 0, -1):
    if a[j] == ".":
        start = j + 1
        print(a[start: finish])
        finish = j

print(a[0: finish])
