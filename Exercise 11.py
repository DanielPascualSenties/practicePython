def es_primo(num):
    for x  in range (2,num):
        if num%x == 0:
            return False
    return True

def menor_divisor(num):
    for x  in range (2,num):
        if num%x == 0:
            return x
    return 0


def pedirEntero(text):
    return int(input(text+": "))


x = pedirEntero("Indique el numero que quiere estudiar")
n = menor_divisor(x)
if n==0:
    print("El numero "+ str(x)+ " es primo")
else:
    print("El numero "+ str(x)+ " no es primo, es divisible entre "+ str(n))
