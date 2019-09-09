import random


def pide_4digit():
    inp = input("Inserte una cadena de 4 digitos: ")
    return list(inp)


def genera_4digit():
    r =random.sample(range(10) , 4)
    return r


def compara_listas(l1, l2):
    cows = 0
    bulls = 0
    s2 = set(l2)
    for i in range(4):
        if int(l1[i])==l2[i]:
            cows += 1
        elif int(l1[i]) in (s2):
            bulls += 1

    print ("Cows: "+str(cows))
    print ("Bulls: "+str(bulls))
    if cows == 4:
        return True
    return False


def main():
    objetivo = genera_4digit()
    resuelto = False
    intentos = 0
    while not resuelto:
        intentos += 1
        resp = pide_4digit()
        print(resp)
        resuelto = compara_listas(resp, objetivo)
    print("Ha tardado "+ str(intentos)+ " intentos.")


main()
