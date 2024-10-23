class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        # Kasvatetaan kuljettua matkaa auton tämänhetkisen nopeuden perusteella
        kuljettu = self.nopeus * tuntimaara
        self.kuljettu_matka += kuljettu
        print(f"Auto kulki {kuljettu} km.")

auto = Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")


auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Nopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

auto.kiihdyta(-200)

print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")

auto.kiihdyta(60)
auto.kuljettu_matka = 2000

auto.kulje(1.5)

print(f"Uusi kuljettu matka: {auto.kuljettu_matka} km")
