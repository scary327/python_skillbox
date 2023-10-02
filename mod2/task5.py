a, i = input().split(", ")
a = ord(a)
i = int(i)
if i >= 0:
    print(chr(a + i))
else:
    print(chr(a + 26 +i))