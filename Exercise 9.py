import random

sol = random.randint(1,9)
intentos = 0
while True:
    intentos += 1
    guess = int(input("Intente adivinar el número entre 1 y 9: "))
    if guess == sol:
        print("¡Exacto!")
        break
    elif guess < sol:
        print("El número que intenta adivinar es mayor que "+ str(guess))
    else:
        print("El número que intenta adivinar es menor que "+ str(guess))
print("Ha tardado "+str(intentos)+" intentos en adivinar el núimero "+str(sol))