import unittest
import os
from xizmat import Royxat


class RoyxatTest(unittest.TestCase):
    def setUp(self):
        self.r = Royxat()
        self.r.qosh("Dars qilish")

    def test_qosh(self):
        yangi_idx = self.r.qosh("Non olish")
        self.assertEqual(yangi_idx, 1)
        self.assertEqual(len(self.r), 2)

    def test_bajar(self):
        birinchi_urinish = self.r.bajar(0)
        self.assertTrue(birinchi_urinish)

        ikkinchi_urinish = self.r.bajar(0)
        self.assertFalse(ikkinchi_urinish)

    def test_saqla_yukla(self):
        fayl_nomi = "test_tmp.json"
        self.r.saqla(fayl_nomi)

        r2 = Royxat.yukla(fayl_nomi)
        self.assertEqual(len(r2), 1)
        self.assertEqual(r2.vazifalar[0].matn, "Dars qilish")

    def tearDown(self):
        if os.path.exists("test_tmp.json"):
            os.remove("test_tmp.json")


if __name__ == "__main__":
    unittest.main()