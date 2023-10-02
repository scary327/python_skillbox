def has_same_digits(sequence):
    digits = set()
    for number in sequence:
        number = int(number)
        if number == 0:
            if 0 in digits:
                return True
            digits.add(0)
        else:
            while number > 0:
                digit = number % 10
                if digit in digits:
                    return True
                digits.add(digit)
                number //= 10
    return False


s = input().split()
print(has_same_digits(s))
