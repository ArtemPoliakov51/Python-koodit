import random

eka = int(input("Anna arpakuutioiden määrä: "))
sum = 0
for i in range(eka):
    sum += random.randint(1,6)
print(sum)