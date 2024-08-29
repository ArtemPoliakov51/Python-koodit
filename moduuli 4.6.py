import random
eka = int(input("Syötä pisteiden määrä"))
toka = 0
kolmas = 0
while eka>toka:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if  x**2+y**2<1:
        kolmas += 1
    toka += 1
print((4*kolmas)/toka)