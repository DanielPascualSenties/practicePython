name = input("Indique su nombre :")
age = input("Indique su edad: ")
number = input("¿Cuantas veces quiere que le repitamos esto?")
for x in range(int(number)):
    print(name +", usted cumplirá 100 años en el año "+ str(2119-int(age)))