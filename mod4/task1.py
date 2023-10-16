def check_repetition(list):
    unique = set()
    for num in list:
        if num not in unique:
            unique.add(num)

    if len(unique) == 1:
        return 'Все числа равны'
    elif len(unique) < len(list):
        return 'Есть равные и неравные числа'
    else:
        return 'Все числа разные'


numbers = [1, 1, 1, 1]
print(check_repetition(numbers))
