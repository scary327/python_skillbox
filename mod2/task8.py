s, i = input().split(",")
result = 0

for j in range(len(s)):
    if s[j] == i:
        result += 1
    else:
        break

print(result)
