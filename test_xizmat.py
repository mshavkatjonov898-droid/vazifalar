# test_xizmat.py — 🧑‍✈️ Kapitan yozadi, 🧠 Mantiqchi kodini tekshiradi
import unittest
import os
from xizmat import Royxat


class RoyxatTest(unittest.TestCase):
    def setUp(self):
        self.r = Royxat()
        self.r.qosh("Dars qilish")

    def test_qosh(self):
        # self.r.qosh("Non olish") → 1 qaytarsin (assertEqual); len(self.r) → 2
        yangi_idx = self.r.qosh("Non olish")
        self.assertEqual(yangi_idx, 1)
        self.assertEqual(len(self.r), 2)

    def test_bajar(self):
        # self.r.bajar(0) → True (assertTrue); yana bajar(0) → False (assertFalse)
        birinchi_urinish = self.r.bajar(0)
        self.assertTrue(birinchi_urinish)

        ikkinchi_urinish = self.r.bajar(0)
        self.assertFalse(ikkinchi_urinish)

    def test_saqla_yukla(self):
        # self.r.saqla("test_tmp.json"); r2 = Royxat.yukla("test_tmp.json"); len(r2) → 1
        fayl_nomi = "test_tmp.json"
        self.r.saqla(fayl_nomi)

        r2 = Royxat.yukla(fayl_nomi)
        self.assertEqual(len(r2), 1)
        self.assertEqual(r2.vazifalar[0].matn, "Dars qilish")

    def tearDown(self):
        if os.path.exists("test_tmp.json"):
            os.remove("test_tmp.json")


unittest.main()