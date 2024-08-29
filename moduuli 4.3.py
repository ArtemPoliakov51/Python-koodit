eka = input("syötä luku: ")
suurinluku = eka
pieninluku = eka
while eka != " ":
    print(eka)
    if eka>suurinluku:
        suurinluku=eka
    if eka<pieninluku:
        pieninluku=eka
    eka = input("syötä luku")
print(f"suurin luku = {suurinluku} ja pienin luku = {pieninluku}")