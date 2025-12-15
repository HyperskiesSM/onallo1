import math

szam = input("A vizsgálni kívánt szám: ")
osszeg = 0

for i in szam:
    osszeg += math.pow(int(i), len(szam))

print(*["A megadott szám Armstrong-szám." if int(szam) == osszeg else "A megadott szám nem Armstrong-szám."])