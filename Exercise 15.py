def separa_string(stri, separador):
    return stri.split(separador)


def pedir_string(text):
    return (input(text + ": "))


def invertir_frase(lis):
    fra= []
    length = len(lis)-1
    for x in range(0, length+1):
        fra.append(lis[length - x])
    return fra


s = pedir_string("Escriba una frase")
lis = separa_string(s, " ")
inv = invertir_frase(lis)
print(" ".join(inv))


