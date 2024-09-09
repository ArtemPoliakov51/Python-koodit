airport = {}

while True:
    command = input("Valitse toimenpide\nuusi lentoasema \nhaku \nlopeta\n: ")

    if command == "lopeta":
        break

    if command == "uusi lentoasema":
        code = input("syötä ICAO-koodi: ")
        name = input("syötä lentoaseman nimi: ")
        airport[code] = name

    elif command == "haku":
        code = input("syötä ICAO-koodi: ")

        if code in airport:
            print(airport[code])

        else:
            print("ei löydy:")

print("lopetus")
