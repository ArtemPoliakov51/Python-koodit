command = int(input("syötä vuosi: "))
if (command % 4 == 0) and not command == 0:
    print("Karkausvuosi")
else:
    print("Ei karkausvuosi")