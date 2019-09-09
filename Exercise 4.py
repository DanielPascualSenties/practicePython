number = int(input("Indique el número a estudiar: "))
res = []
for x in range (1 , number):
    r = number % x
    if r == 0 :
        res.append(x)
print(res)