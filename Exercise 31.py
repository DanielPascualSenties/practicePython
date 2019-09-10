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
    while True:
        letter = input("Introduzca una letra: ")
        letter = letter.upper()
        if letter == 'X':
            break
        if letter in s:
            print("Esa letra ya está en las seleccionadas")
        else:
            s.add(letter)
        show_guessed(word, s)
        if word_guessed(word, s):
            print("¡Felicidades, ha ganado!")
            break


game("GALLETAS")