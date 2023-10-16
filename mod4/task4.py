def can_make_palindrome(word):
    # создаем словарь для подсчета количества вхождений каждой буквы
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # считаем количество букв с нечетным количеством вхождений
    odd_count = 0
    for count in letter_counts.values():
        if count % 2 != 0:
            odd_count += 1

    # если букв с нечетным количеством вхождений больше одной, палиндром невозможен
    if odd_count > 1:
        return 'полиндром составить нельзя'

    # создаем список из букв с четным количеством вхождений
    even_letters = []
    for letter, count in letter_counts.items():
        if count % 2 == 0:
            even_letters.extend([letter] * (count // 2))

    # создаем палиндром из списка букв с четным количеством вхождений
    palindrome = ''.join(even_letters)

    i = 0
    if odd_count == 1:
        odd_letter = ''
        for letter, count in letter_counts.items():
            if count % 2 != 0:
                odd_letter = letter
                i = count
        palindrome = palindrome + (odd_letter * i) + palindrome[::-1]
    else:
        palindrome = palindrome + palindrome[::-1]

    return palindrome


print(can_make_palindrome("даааааадп"))
