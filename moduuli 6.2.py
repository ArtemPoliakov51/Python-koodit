import random


def randomi(toka):
    eka = random.randint(1,toka)
    print(eka)
    return eka

kolmas = int(input("nopan tahkojen yhteismäärä: "))
eka = 0
while eka != kolmas:
    eka = randomi(kolmas)