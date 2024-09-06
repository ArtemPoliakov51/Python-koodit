import random

def randomi():
    eka = random.randint(1,6)
    print(eka)
    return eka

eka = 0
while eka != 6:
    eka = randomi()