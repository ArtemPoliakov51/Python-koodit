command = input("Syötä hyttiluokka: ")
if command == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif command == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif command == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif command == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka")