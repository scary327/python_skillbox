all_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
all_sogls = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'x', 'ш', 'щ', 'ч']

s = input()
s.replace(' ', '')
k_gls, k_sogls = 0, 0

for i in range(len(s)):
    if s[i] in all_gls:
        k_gls += 1
    elif s[i] in all_sogls:
        k_sogls += 1
    else:
        continue

print(k_gls, k_sogls)
