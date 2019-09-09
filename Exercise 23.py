def main():
    with open('files/Ex23_prime_numbers', 'r') as pr:
        prime = pr.read().split()
    with open('files/Ex23_happy_numbers', 'r') as hp:
        happy = hp.read().split()
    print(prime)
    print(happy)

    hp_set = set(happy)
    intersected = list(hp_set.intersection(prime))
    print(intersected)



main()
