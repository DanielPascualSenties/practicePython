pl1 = input("Introduzca el nombre del jugador 1: ")
pl2 = input("Introduzca el nombre del jugador 2: ")

while True:
    jugada1 = input(pl1+", escriba piedra, papel o tijeras: ").lower()
    jugada2 = input(pl2+", escriba piedra, papel o tijeras: ").lower()
    print(pl1 + " : " + jugada1)
    print(pl2 + " : " + jugada2)
    if jugada1 == "piedra":
        if jugada2 == "piedra":
            print("Empate")
        elif jugada2 == "papel":
            print("Gana "+ pl2)
        else:
            print("Gana "+ pl1)
    elif jugada1 == "papel" :
        if jugada2 == "piedra":
            print("Gana "+ pl1)
        if jugada2 == "papel":
            print("Empate")
        else:
            print("Gana " + pl2)
    else:
        if jugada2 == "piedra":
            print("Gana "+pl2)
        if jugada2 == "papel":
            print("Gana " + pl1)
        else:
            print("Empate")

    i = input("Escriba s para salir: ")
    if i == "s":
        break

