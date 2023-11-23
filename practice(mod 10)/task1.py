import re


def check_password(password):
    pattern = r'^(?=.*[A-Z].*[A-Z])(?=.*\d)(?=.*[!@#$%^&*].*[!@#$%^&*])(?!.*([\s\S])\1\1).{6,}$'
    return bool(re.match(pattern, password))


print(check_password('rtG3FG!Tr^e'))
print(check_password('aA1!*!1Aa'))
print(check_password('oF^a1D@y5e6'))
print(check_password('enroi#$rkdeR#$092uWedchf34tguv394h'))
print(check_password('пароль'))
print(check_password('password'))
print(check_password('qwerty'))
print(check_password('lOngPa$$$W0Rd'))
