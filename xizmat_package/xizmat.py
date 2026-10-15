# xizmat.py — 🧠 Mantiqchi
import json

from model_package.model import Vazifa


class Royxat:
    def __init__(self):
        self.vazifalar = []

    def __len__(self):
        return len(self.vazifalar)

    def get_info(self):
        for i in self.vazifalar:
            if len(self.vazifalar) != 0:
                return f"#{len(self.vazifalar)} {i}"
        return "(royxat bo'sh)"

    def qosh(self, matn, muhim=False):
        # Vazifa(matn, muhim) yaratib ro'yxatga qo'shing; yangi raqamni qaytaring: len(...) - 1
        vazifa = Vazifa(matn, muhim)
        self.vazifalar.append(vazifa)
        return f"✅ #{len(self.vazifalar)} qoshildi: {vazifa}"

    def bajar(self, idx):
        # v = self.vazifalar[idx]  (yo'q bo'lsa IndexError o'zi chiqadi)
        # v.bajarildi True bo'lsa → return False; aks holda v.bajar(); return True
        # try:
        #     v = self.vazifalar[idx]
        #
        #     if v.bajarildi is False:
        #         v.bajar()
        #         return f"✔️ #{idx} {v}"
        #     else:
        #         return "❌ Allaqachon bajarilgan"
        #
        # except IndexError:
        #     return "❌ Bunday vazifa yo'q"

        try:
            v = self.vazifalar[idx]
            if v.bajarildi:
               return False
            else:
                v.bajar()
                return True

        except IndexError:
            print("❌ Bunday vazifa yo'q")

    def ochir(self, idx):
        del self.vazifalar[idx]
        return f"🗑 #{idx} o'chirildi"

    def bajarilmaganlar(self):
        # [v for v in self.vazifalar if not v.bajarildi]
        for i in self.vazifalar:
            if not i.bajarildi:
                return f"#{len(self.vazifalar)} {i}"

        return ""

    def saqla(self, fayl="vazifalar.json"):
        data = [
            {
                "matn": v.matn,
                "muhim": v.muhim,
                "bajarildi": v.bajarildi
            }
            for v in self.vazifalar
        ]
        with open(fayl, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def yukla(cls, fayl="vazifalar.json"):
        r = cls()
        try:
            with open(fayl, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(data)
        except FileNotFoundError:
            return r
        # har d uchun: idx = r.qosh(d["matn"], d["muhim"]); d["bajarildi"] bo'lsa r.bajar(idx)
        # idx = r.qosh(data["matn"], data["muhim"])
        # r.bajar(idx)
        # return r


# royxat = Royxat()

# Vazifa.bajar(vazifa1)
# print(royxat.qosh("non olish", True))
# print(royxat.qosh("non olish2", False))
# print(royxat.bajar(0))
# print(royxat.bajar(1))
# print(royxat.ochir(0))
# print(royxat.bajarilmaganlar())
# royxat.saqla()
# royxat.saqla()
# print(royxat.get_info())