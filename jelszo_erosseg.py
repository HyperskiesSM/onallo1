def jelszo_erosseg(jelszo: str) -> int:
    if len(jelszo) == 0 or "jelszo" in jelszo or "123" in jelszo:
        return 0

    jero = 1 

    if len(jelszo) >= 5:
        jero += 1
    if len(jelszo) >= 8:
        jero += 2

    for ch in jelszo:
        if ch in "_-.":
            jero += 2

    return jero


print("Jelszó erősége",jelszo_erosseg(input("Kérek egy jelszót")))


import unittest

class TestJelszoErosseg(unittest.TestCase):

    def test_ures_jelszo(self):
        self.assertEqual(jelszo_erosseg(""), 0)

    def test_tiltott_reszszoveg_jelszo(self):
        self.assertEqual(jelszo_erosseg("jelszo"), 0)
        self.assertEqual(jelszo_erosseg("abc123xyz"), 0)

    def test_rovid_jelszo(self):
        self.assertEqual(jelszo_erosseg("abc"), 1)

    def test_legalabb_5_karakter(self):
        self.assertEqual(jelszo_erosseg("abcde"), 2)

    def test_legalabb_8_karakter(self):
        self.assertEqual(jelszo_erosseg("abcdefgh"), 4)

    def test_specialis_karakterek(self):
        self.assertEqual(jelszo_erosseg("abcd_efg"), 6)
        self.assertEqual(jelszo_erosseg("ab.-_cd"), 1 + 1 + 3 * 2)
