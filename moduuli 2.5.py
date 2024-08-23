luoti = 13.3
naula = luoti*32
leiviskä = naula*20

luotia = float(input("Anna luoti\n"))
naulaa = float(input("Anna naula\n"))
leiviskää = float(input("Anna leiviska\n"))


print("Massa nykymittojen mukaan: ")
yhteensä = luotia*luoti+naulaa*naula+leiviskää*leiviskä

kilo = (yhteensä/1000)-1
gramma = int(kilo)
gramma1 = (kilo-gramma)*1000

print(f"{kilo:.0f} kilogrammaa ja {gramma1:.2f} grammaa")
