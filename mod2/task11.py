def has_same_digits(sequence):
    sequence = sequence.replace(" ", "")
    for i in range(len(sequence)):
        if sequence.count(sequence[i]) > 1:
            return True
    return False


s = input()
print(has_same_digits(s))
