import random
a = random.sample(range(20), 10)
b = random.sample(range(25), 12)
print(a)
print(b)

print([x for x in a if x in b])
