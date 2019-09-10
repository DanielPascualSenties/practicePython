import random
def pick_word():
    with open('files/sowpods.txt', 'r') as open_file:
        all_text = open_file.read()
        lis = all_text.split()
        length = len(lis)
        w = random.randint(0,length)
        return lis[w]


word = pick_word()
print("La palabra seleccionada es " + word)