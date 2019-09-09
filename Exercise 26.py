def winning_row(lis):
    if lis[0] == lis[1] and lis[1] == lis[2]:
        return lis[0]
    return 0


def winning_col(lis, col):
    if lis[0][col] == lis[1][col] and lis[1][col] == lis[2][col]:
        return lis[1][col]
    return 0


def winning_diag(lis):
    if lis[0][0] == lis[1][1] and lis[1][1] == lis[2][2]:
        return lis[2][2]
    elif lis[0][2] == lis[1][1] and lis[1][1] == lis[2][0]:
        return lis[1][1]
    return 0


def winner(lis):
    for i in range(3):
        r = winning_row(lis[i])
        if r != 0:
            return r
        c = winning_col(lis, i)
        if c != 0:
            return c
    d = winning_diag(lis)
    if d != 0:
        return d
    return 0


def main():
    game = [[1, 2, 2],
            [2, 2, 0],
            [1, 1, 1]]

    w = winner(game)
    if w == 0:
        print("No hay ganador")
    else:
        print("El ganador es el jugador " + str(w))


main()
