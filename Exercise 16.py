import random

le = ["cumpleños", "hello", "hola", "incorrecta", "1234"]


def main():
    while True:
        x = input("Pulse D para una contraseña Débil, F para una contraseña Fuerte, o S para Salir: ").upper()
        if x == 'S':
            break
        if x == 'D':
            print("Quiere una contraseña débil")
            n = random.randint(0, len(le)-1)
            print("Su contraseña:")
            print(le[n])

        if x == 'F':
            print("Quiere una contraseña fuerte")
            r = ""
            for i in range(12):
                v = random.randint(32,126)
                r += chr(v)
            print("Su contraseña:")
            print(r)

main()
