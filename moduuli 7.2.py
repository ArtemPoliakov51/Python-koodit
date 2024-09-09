nimet = set()

eka = input("Anna nimi: ")
print("uusi nimi")
while eka != "":
    nimet.add(eka)
    eka = input("Anna nimi: ")
    if eka in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("uusi nimi")
for nimi in nimet:
    print(nimi)
