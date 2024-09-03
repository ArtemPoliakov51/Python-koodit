luvut = []

eka = input("Anna luku: ")
while eka != "":
    luvut.append(int(eka))
    eka = input("Anna luku: ")
kolmas = sorted(luvut, reverse=True)
del kolmas[5:]
print(kolmas)