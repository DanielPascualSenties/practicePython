a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def binary_search(lis, elem):
    print("Buscamos el elemento "+ str(elem) + " en la lista:")
    print(lis)
    length = len(lis)
    medio = int(length/2)
    if length == 0 :
        return False
    elif length == 1:
        return elem == lis[medio]
    elif elem == lis[medio]:
        return True
    elif elem > lis[medio]:
        return binary_search(lis[medio:], elem)
    elif elem < lis[medio]:
        return binary_search(lis[:medio], elem)


def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    elem = int(input("¿Qué elemento quiere buscar en la lista?"))
    b = binary_search(a, elem)
    print(b)


main()