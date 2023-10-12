def check_winner(board, k):
    for i in range(k):
        row = board[i]
        if row.count('X') == k:
            return 'X'
        elif row.count('O') == k:
            return 'O'
    for j in range(k):
        col = [board[i][j] for i in range(k)]
        if col.count('X') == k:
            return 'X'
        elif col.count('O') == k:
            return 'O'
    diag1 = [board[i][i] for i in range(k)]
    if diag1.count('X') == k:
        return 'X'
    elif diag1.count('O') == k:
        return 'O'

    diag2 = [board[i][k - i - 1] for i in range(k)]
    if diag2.count('X') == k:
        return 'X'
    elif diag2.count('O') == k:
        return 'O'
    return 'Ничья'


s = input()
k = len(s)
board = [list(s)]
while s != '':
    s = input()
    board.append(list(s))

print(check_winner(board, k))
