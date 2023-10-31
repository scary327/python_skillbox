def armstrong_numbers():
    for num in range(100, 100000):
        order = len(str(num))
        summ = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            summ += digit ** order
            temp //= 10
        if num == summ:
            yield num


arm_num = armstrong_numbers()


def get_armstrong_numbers():
    return next(arm_num)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
