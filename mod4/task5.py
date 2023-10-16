letter_counts = {}
with open(input("Введите название файла: "), encoding='utf-8-sig') as file:
    for line in file:
        for letter in line:
            if letter.isalpha():
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1])


with open('output.txt', 'w') as file:
    for item in sorted_counts:
        file.write(f"{item[0]}: {item[1]}\n")
