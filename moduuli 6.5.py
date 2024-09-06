def funktio(eka):
    pari = []
    for i in eka:
        if i % 2 == 0:
            pari.append(i)
    return pari
luvut = [1,2,3,4,5,6,7,8,9,10]
pari = funktio(luvut)
print(pari)