a = input()
if a.isnumeric():
    print(bin(int(a))[2:] + ', ', oct(int(a))[2:] + ', ' + hex(int(a))[2:] if int(a)>0 else "Неверный ввод")