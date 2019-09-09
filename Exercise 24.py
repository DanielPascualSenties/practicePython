def n_tapas(n):
    s = " "
    for i in range(n):
        s += "--- "
    return s


def n_paredes(n):
    s = "|"
    for i in range(n):
        s += "   |"
    return s

def main():
    s = int(input("Introduzca el tamaño de tablero que quiere: "))
    print(n_tapas(s))
    for i in range(s):
        print(n_paredes(s))
        print(n_tapas(s))


main()