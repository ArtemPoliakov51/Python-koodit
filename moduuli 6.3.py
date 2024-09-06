def litra(eka):
    ns = eka*3.785
    return ns

yksi = float(input("anna gallonamäärä: "))
while litra(yksi) >= 0:
    print(f"{litra(yksi)} litraa")
    yksi = float(input("gallonmäärä: "))
print("")
