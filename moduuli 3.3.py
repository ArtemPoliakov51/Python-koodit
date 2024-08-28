command = input("syötä sukupuolesi: ")
if command == "nainen":
    command1 = float(input("syötä hemoglobiiniarvosi: "))
    if (117<command1<175):
        print("hemoglobiiniarvosi on normaali")
    elif (command1<117):
        print("hemoglobiiniarvosi on alhainen")
    elif (175<command1):
        print("hemoglobiiniarvosi on korkea")
elif command == "mies":
    command2 = float(input("syötä hemoglobiiniarvosi: "))
    if ( 134 < command2 < 195):
        print("hemoglobiiniarvosi on normaali")
    elif (command2 < 134):
        print("hemoglobiiniarvosi on alhainen")
    elif (195 < command2):
        print("hemoglobiiniarvosi on korkea")