kuha = float(input("Kuhan pituus senttimetreinä: "))
command1 = 37-kuha
if kuha<=37:
    print("Laske kuha takaisin järveen")
    print(f"{command1:.1f} senttimetriä puuttuu alimmasta sallitusta pyyntimitasta")
else:
    print(":-)")