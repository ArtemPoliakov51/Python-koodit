Vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-12): "))
vuodenaika = Vuodenajat[järjestysnumero-1]
print (f"{järjestysnumero}. vuodenaika on {vuodenaika}.")