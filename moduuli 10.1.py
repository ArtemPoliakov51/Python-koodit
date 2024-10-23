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


h = Hissi(1, 10)

print("\nSiirretään hissi viidenteen kerrokseen:")
h.siirry_kerrokseen(5)

print("\nSiirretään hissi takaisin alimpaan kerrokseen:")
h.siirry_kerrokseen(1)

