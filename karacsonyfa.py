magassag = int(input("Kérem a fa magasságát"))


for i in range(magassag):
    szokoz = magassag - i - 1
    csillag = 2 * i + 1
    print(" " * szokoz + "*" * csillag)

torzs_szokoz = magassag - 2
for _ in range(2):
    print(" " * torzs_szokoz + "|||") 