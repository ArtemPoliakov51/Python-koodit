command = int(input("syötä vuosi: "))
if (command % 4 == 0 and command % 100 != 0) or (command % 400 == 0) :
    print("Karkausvuosi")
else:
    print("Ei karkausvuosi")