birthdays = {
    "Irene": "20 de febrero",
    "Mama": "27 de julio",
    "Papa": "16 de febrero",
    "Javier": "19 de julio",
    "Roberto": "15 de enero",
    "Pablo": "17 de septiembre",
    "Enriquito": "14 de abril",
    "Irene Sentíes": "31 de agosto"
}


def listar(dict):
    print(">>> Hola, estos son los cumpleaños disponibles:")
    for i in dict:
        print(i)


def show_birthday(dict, k):
    v = dict[k]
    print("El cumpleaños de {} es el {}.".format(k, v))


def main():
    listar(birthdays)
    while True:
        name = input(">>>¿Qué cumpleaños quiere saber?\n ")
        show_birthday(birthdays, name)


main()
