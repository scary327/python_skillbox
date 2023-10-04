s = input()
s.replace(' ', '')
k_gls, k_sogls = 0, 0

for i in range(len(s)):
    if s[i] in 'аеёиоуыэюя':
        k_gls += 1
    elif s[i] in 'бвгджзйклмнпрстфхцчшщ':
        k_sogls += 1
    else:
        continue

print(k_gls, k_sogls)
