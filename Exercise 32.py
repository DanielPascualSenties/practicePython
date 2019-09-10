import random


def is_it_there(word, letter):
    return letter in set(word)


def pick_word():
    with open('files/sowpods.txt', 'r') as open_file:
        all_text = open_file.read()
        lis = all_text.split()
        length = len(lis)
        w = random.randint(0,length)
        return lis[w].upper()


def word_guessed(word, letters):
    length = len(word)
    for i in range(0, length):
        if word[i] not in letters:
            return False
    return True


def show_guessed(word, letters):
    x = ""
    length = len(word)
    for i in range(0, length):
        if word[i] in letters:
            x += word[i]
        else:
            x += "_"
    display(x)


def display(word):
    x = ""
    length = len(word)
    for i in range(0,length):
        x += word[i]
        x += " "
    print(x)


def game(word):
    print("¡Bienvenido al juego del ahorcado!")
    s = {' '}
    fails = 0
    show_guessed(word, s)
    while fails < 6:
        letter = input("Introduzca una letra: ")
        letter = letter.upper()
        if letter in s:
            print("Esa letra ya está en las seleccionadas")
        else:
            s.add(letter)
            if is_it_there(word, letter):
                print("¡Acierto!")
            else:
                fails += 1
                print("¡Fallo! Lleva " + str(fails) + " fallos.")
                if fails == 6:
                    print("Ha perdido")
            show_guessed(word, s)
        if word_guessed(word, s):
            print("¡Felicidades, ha ganado!")
            break


def main():
    w = pick_word()
    game(w)


main()