import random


def remove_duplicates(l):
    return list(set(l))


a=[]
for x in range(12):
    a.append(random.randint(1,20))

print(a)
b = remove_duplicates(a)
print(b)