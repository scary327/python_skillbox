s = input().split()
result = ''

for i in range(len(s)):
    result += s[i][-1]

print(result)
