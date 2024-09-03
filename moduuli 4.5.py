eka = input("syötä käyttäjätunnus: ")
toka = input("syötä salasana: ")
kolmas = 0
while kolmas<5:
    if eka == "python" and toka == "rules":
        print("tervetuloa")
        break
    elif eka != "python" or toka != "rules":
        eka = input("syötä käyttäjätunnus: ")
        toka = input("syötä salasana: ")
    kolmas += 1
    if kolmas == 5:
        print("pääsy estetty")
