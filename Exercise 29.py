def tapas():
    s = " "
    for i in range(3):
        s += "--- "
    return s


def fila(lis, n):
    s = "|"
    for i in range(3):
        s += " " + str(lis[n][i]) + " |"
    return s


def mostrar_tablero(lis):
    print(tapas())
    print(fila(lis, 0))
    print(tapas())
    print(fila(lis, 1))
    print(tapas())
    print(fila(lis, 2))
    print(tapas())


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
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    mostrar_tablero(game)
    for x in range(9):
        turno = (x % 2) + 1
        while True:
            f = int(input("En que fila quiere colocar ficha")) % 3
            c = int(input("En que columna quiere colocar ficha")) % 3
            if game[f][c] == 0:
                game[int(f)][int(c)] = turno
                break
            else:
                print("Esa casilla ya está ocupada")
        mostrar_tablero(game)
        if winner(game) == turno :
            print("¡3 en línea! El jugador " + str(turno) + " ha ganado")




main()