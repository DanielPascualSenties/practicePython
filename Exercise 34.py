import json


def save_to_json(dict):
    with open("files/birthdays.json", "w") as f:
        json.dump(dict, f)


def load_json(route):
    with open(route, "r") as f:
        birthdays = json.load(f)
    return birthdays


def listar(dict):
    print(">>> Hola, estos son los cumpleaños disponibles:")
    for i in dict:
        print(i)


def show_birthday(dict, k):
    v = dict[k]
    print("El cumpleaños de {} es el {}.".format(k, v))


def main():
    birthdays = load_json("files/birthdays.json")
    listar(birthdays)
    while True:
        v = int(input("Pulse 1 para ver cumpleaños, 2 para añadir cumpleaños, 0 para salir\n"))
        if v == 0:
            break
        elif v == 1:
            name = input(">>>¿Qué cumpleaños quiere saber?\n")
            show_birthday(birthdays, name)
        else:
            name = input(">>>¿Como se llama el personaje?\n")
            bd = input(">>>¿Y cuál es su cumpleaños?\n")
            birthdays[name] = bd
            save_to_json(birthdays)


main()
