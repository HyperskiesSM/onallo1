def maganhangzot_torol(szoveg: str) -> str:
    maganhangzok = "aeiouAEIOU"
    eredmeny = ""

    for ch in szoveg:
        if ch not in maganhangzok:
            eredmeny += ch

    return eredmeny
print(maganhangzot_torol(input("Kérek egy szöveget")))

import unittest

class TestMaganhangzotTorol(unittest.TestCase):

    def test_nincs_maganhangzo(self):
        self.assertEqual(maganhangzot_torol("bcdfg"), "bcdfg")

    def test_csak_maganhangzo(self):
        self.assertEqual(maganhangzot_torol("aeiou"), "")

    def test_vegyes_szoveg(self):
        self.assertEqual(maganhangzot_torol("Twitter posztolas"), "Twttr pzstls")

    def test_nagybetuk(self):
        self.assertEqual(maganhangzot_torol("AEIOUxyz"), "xyz")

    def test_ures_szoveg(self):
        self.assertEqual(maganhangzot_torol(""), "")
