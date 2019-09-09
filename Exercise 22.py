def remove_elem(lis, elem):
    clean = [x for x in lis if x != elem]
    return clean


def main():
    with open('files/fichero_de_prueba22.txt', 'r') as open_file:
        all_text = open_file.read()
        lis = all_text.split()
        print(lis)
        while (len(lis)> 0):
            elem = lis[0]
            new_lis = remove_elem(lis, elem)
            count_new = len(lis) - len(new_lis)
            print("El elemento " + elem + " aparece " + str(count_new) + " veces")
            lis = new_lis


main()