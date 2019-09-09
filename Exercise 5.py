import random
a = []
b = []
for x in range(10):
    a.append(random.randint(1,20))
for x in range(12):
    b.append(random.randint(1,25))
print(a)
print(b)
inter = set(a).intersection(b)
print(list(inter))