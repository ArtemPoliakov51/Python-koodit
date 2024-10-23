import random

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print(f"Virhe: Kerros {kerros} ei ole sallittu kerros.")
            return

        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for i in range(hissien_lkm):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Virhe: Hissiä numero {hissin_numero} ei ole.")
            return

        print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}:")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("\nPalohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit, start=1):
            print(f"\nSiirretään hissi {i} pohjakerrokseen:")
            hissi.siirry_kerrokseen(self.alin_kerros)



talo = Talo(1, 10, 3)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 1)
talo.aja_hissia(1, 1)
talo.palohalytys()

