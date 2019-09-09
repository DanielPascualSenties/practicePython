def pedirEntero(text):
    return int(input(text+": "))


def serieFib(n):
    x=[1,1]
    for i in range (2,n):
        x.append(x[i-1]+x[i-2])
    return x


x = pedirEntero("Indique el número que quiere de la serie de Fibonacci")
print(serieFib(x))

