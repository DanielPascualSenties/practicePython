
def guess(bottom, top, intentos):
    middle = int((top +bottom)/2)
    print("Llamando a la funcion guess con valor mínimo " + str(bottom) + " y valor máximo " + str(top))
    x = input("El número que tiene en la cabeza es mayor, menor, o igual a "+str(middle))
    if x == '=':
        return intentos
    elif x == '<':
        return guess(bottom, middle, intentos + 1)
    elif x == '>':
        return guess(middle, top, intentos+1)


def main():
    intentos = (guess(0,100, 1))
    print("He acertado el número en "+ str(intentos) + " intentos")

main()