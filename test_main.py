# test_main.py — 🖥 Interfeyschi
import unittest
from main import tanlovni_tekshir, ha_yoq

class YordamchiTest(unittest.TestCase):
    def test_tanlov(self):
        # tanlovni_tekshir("3", 5) → 3;  ("9", 5) → None;  ("abc", 5) → None
        self.assertEqual(tanlovni_tekshir("3", 5),3)
        self.assertEqual(tanlovni_tekshir("9", 5), None)
        self.assertEqual(tanlovni_tekshir("abc", 5), None)

    def test_ha_yoq(self):
        # ha_yoq("h") → True;  ha_yoq(" Ha ") → True;  ha_yoq("y") → Fals
        self.assertTrue(ha_yoq("h"))
        self.assertTrue(ha_yoq(" Ha "))
        self.assertFalse(ha_yoq("y"))


if __name__ == "__main__":
    unittest.main(verbosity=2)