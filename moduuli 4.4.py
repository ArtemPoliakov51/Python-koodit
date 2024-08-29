import random
toka = random.randint(1, 10)
while True:
    eka = int(input("syötä luku: "))
    if eka < toka:
        print("liian pieni arvaus")
    elif eka > toka:
        print("liian suuri arvaus")
    elif eka == toka:
        print("oikein")
        break