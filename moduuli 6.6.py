def funktio(eka):
    toka = 3.14 * (eka/2) ** 2
    kolmas = toka/10000
    neljäs = float(input("Nyt syötä hinta: "))
    viides = neljäs/kolmas
    return viides

ekas = float(input("Syötä ensimmäisen pizzan halkaisija: "))
tokas = funktio(ekas)
ekas2 = float(input("Syötä toisen halkaisija: "))
tokas2 = funktio(ekas2)

if tokas < tokas2:
    print("Ensimmäinen pizza on edullisempi")
elif tokas2 < tokas:
    print("Toinen pizza on edullisempi")

