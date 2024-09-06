def funktio(eka):
    toka = 3.14 * (eka/2) ** 2
    kolmas = toka/10000
    neljäs = float(input("syötä hinta: "))
    viides = neljäs/kolmas
    return viides

ekas = float(input("syötä halkaisija"))
tokas = funktio(ekas)
ekas2 = float(input("syötä toka halkaisija"))
tokas2 = funktio(ekas2)

if tokas < tokas2:
    print("eka edullisempi")
elif tokas2 < tokas:
    print("toka edullisempi")

