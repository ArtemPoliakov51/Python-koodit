class Auto:
    def __init__(self,tunnus,huippunopeus,hetkellinennopeus,matka):
        self.tunnus=tunnus
        self.huippunopeus=huippunopeus
        self.hetkellinennopeus=hetkellinennopeus
        self.matka=matka

auto = Auto("ABC-123", 147,0,0)

print(f"rekisteritunnus {auto.tunnus}\nhuippunopeus {auto.huippunopeus}\nhetkellinen nopeus {auto.hetkellinennopeus}\nmatka {auto.matka}")




