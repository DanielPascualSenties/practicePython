number = int(input("Indique un numero: "))
resto = number % 2
if resto == 0:
    print("El número es par")
else:
    print("El número es impar")

resto = number % 4
if resto == 0:
    print("Es divisible entre cuatro")

divisor = int(input("Indique un segundo numero sobre el que dividir: "))
resto = number % divisor
if resto == 0:
    print("El numero que ha indicado es divisor del original")
else:
    print("No es divisor")