def elmozdulas(utvonal: str) -> str:
    x = 0  
    y = 0  

    for lepes in utvonal:
        if lepes == "F":
            y += 1
        elif lepes == "L":
            y -= 1
        elif lepes == "J":
            x += 1
        elif lepes == "B":
            x -= 1

    if x == 0 and y == 0:
        return "Nem mentunk sehova"

    return f"Vizszintes: {x}, Fuggoleges: {y}"

print(elmozdulas(input("Kérem az elmozdulást betűkkel ")))

import unittest

class TestElmozdulas(unittest.TestCase):

    def test_nem_ment_sehova(self):
        self.assertEqual(elmozdulas(""), "Nem mentunk sehova")
        self.assertEqual(elmozdulas("FB"), "Nem mentunk sehova")
        self.assertEqual(elmozdulas("JL"), "Nem mentunk sehova") 

    def test_vizszintes_elmozdulas(self):
        self.assertEqual(elmozdulas("JJJ"), "Vizszintes: 3, Fuggoleges: 0")
        self.assertEqual(elmozdulas("BBB"), "Vizszintes: -3, Fuggoleges: 0")

    def test_fuggoleges_elmozdulas(self):
        self.assertEqual(elmozdulas("FFF"), "Vizszintes: 0, Fuggoleges: 3")
        self.assertEqual(elmozdulas("LL"), "Vizszintes: 0, Fuggoleges: -2")

    def test_osszetett_utvonal(self):
        self.assertEqual(elmozdulas("JBBFB"), "Vizszintes: -2, Fuggoleges: 1")
