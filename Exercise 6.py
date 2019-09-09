x = input("Escriba el posible palindromo: ")
b = True

l = len(x)
iterations = int(l/2)

for i in range(iterations):
    if x[i] != x[l-i-1]:
        b = False

print(b)