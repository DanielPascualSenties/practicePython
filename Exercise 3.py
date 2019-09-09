limite = int(input("Indique el máximo que quiere ver en su lista: "))
print("Lista completa")
l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(l)
print("Lista filtrada")
n = [x for x in l if x < limite]
print(n)