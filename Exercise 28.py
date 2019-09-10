def maximum(a,b):
    if a > b:
        return a
    return b


def maximum_3(a,b,c):
    return maximum(maximum(a,b), maximum(b,c))


def main():
    v1 = int(input("Introduzca un número: "))
    v2 = int(input("Introduzca otro número: "))
    v3 = int(input("Introduzca un último número: "))
    m = maximum_3(v1, v2, v3)
    print("El mayor de los tres valores es: " + str(m))


main()