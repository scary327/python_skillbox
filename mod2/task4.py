a = input()
if a.isnumeric() and int(a)>0:
    a = int(a)
    print(bin(a)[2:], oct(a)[2:], hex(a)[2:])
else:
    print("Неверный ввод")