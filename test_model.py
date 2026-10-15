# test_model.py — 🧠 Mantiqchi yozadi, 🧑‍✈️ Kapitan kodini tekshiradi
import unittest
from model import Vazifa

class VazifaTest(unittest.TestCase):

    def test_yangi_vazifa(self):
        # Vazifa("Dars qilish").bajarildi → False (assertFalse)
        self.assertFalse(Vazifa("Dars qilish").bajarildi)

    def test_bajar(self):
        # v = Vazifa("Dars qilish"); v.bajar(); v.bajarildi → True
        v = Vazifa("Dars qilish")
        self.assertEqual(v,v.bajar())
        self.assertEqual(v,v.bajarildi)

    def test_bosh_matn(self):
        # with self.assertRaises(ValueError): Vazifa("   ")
        with self.assertRaises(ValueError):
            Vazifa("")

    def test_str(self):
        self.assertEqual(str(Vazifa("Non olish",True)) ,"[ ] Non olish ⭐")

 # ⭐ bonus: test_str — str(Vazifa("Non olish", True)) == "[ ] Non olish ⭐"