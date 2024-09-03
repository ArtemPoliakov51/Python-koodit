luvut = []

eka = input("Anna luku: ")
while eka != "":
    luvut.append(int(eka))
    eka = input("Anna luku: ")
luvut.sort(reverse=True)
print(luvut[:5])
