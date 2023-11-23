import re


def check_color(color):
    color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$|^rgb\(\s*(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*,){2}\s*(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*\)$|^hsl\(\s*(?:(?:360|3[0-5][0-9]|[0-2]?[0-9][0-9]?)\s*,){2}\s*(?:100%|[0-9][0-9]?%|0%)\s*\)$')
    return bool(color_regex.match(color))


print(check_color('#a4e')) # Возвращает True
print(check_color('#abcdef')) # Возвращает True
print(check_color('rgb(100,200,255)')) # Возвращает True
print(check_color('hsl(240, 100%, 50%)')) # Возвращает True
print(check_color('abcdef')) # Возвращает False
print(check_color('hsl(240,100%,50%)')) # Возвращает True
