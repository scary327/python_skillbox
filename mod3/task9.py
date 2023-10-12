def spiral_coordinates(n):
    x, y = 0, 0
    i = 1
    while n > 0:
        if 7 * i + (i - 1) <= n:
            n -= 7 * i + (i - 1)
            i += 1
        else:
            break
    j = i + 1
    if 7 * i // 2 <= n:
        n -= 7 * i // 2
        y -= i
        j += 1
    c = 0
    while n > 0:
        if j - i == 1:
            if c < i:
                x -= 1
                n -= 1
                c += 1
            elif c >= i and c < j:
                y -= 1
                n -= 1
                c += 1
            else:
                x += 1
                n -= 1
                c += 1
        elif j - i == 2:
            if c < i:
                x += 1
                n -= 1
                c += 1
            elif c >= i and c < j:
                y += 1
                n -= 1
                c += 1
            else:
                x -= 1
                n -= 1
                c += 1
    return x, y


with open('input.txt') as f:
    a = int(f.readline())
    with open('output.txt', 'w') as file:
        file.write(str(spiral_coordinates(a)))
