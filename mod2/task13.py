a = input()
summ = 0
for i in range(0, len(a), 2):
    summ += int(a[i])

for j in range(1, len(a), 2):
    summ += int(a[j]) * 3

if summ % 10 == 0:
    print('yes')
else:
    print('no')
