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


def main():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    mostrar_tablero(game)
    for x in range(9):
        turno = (x % 2) + 1
        valido = False
        while not valido:
            f = int(input("En que fila quiere colocar ficha"))
            c = int(input("En que columna quiere colocar ficha"))
            if game[f][c] == 0:
                game[int(f)][int(c)] = turno
                valido = True
            else:

        mostrar_tablero(game)



main()