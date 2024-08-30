eka = input("syötä käyttäjätunnus: ")
toka = input("syötä salasana: ")
kolmas = eka != "python" and toka != "rules"
if kolmas:
    print("väärin käyttäjätunnus tai salasana\nyritä uudelleen!")
while kolmas<5:
    if eka == "python" and toka == "rules":
        print("tervetuloa")
        break
    elif eka != "python" or toka != "rules":
        eka = input("syötä käyttäjätunnus: ")
        toka = input("syötä salasana: ")
        print("väärin käyttäjätunnus tai salasana\nyritä uudelleen!")
    kolmas += 1
    if kolmas == 5:
        print("pääsy estetty")

