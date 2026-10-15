import json
from model import Vazifa


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
        return len(self.vazifalar) - 1

    def bajar(self, idx):
        # v = self.vazifalar[idx]  (yo'q bo'lsa IndexError o'zi chiqadi)
        # v.bajarildi True bo'lsa → return False; aks holda v.bajar(); return True
        v = self.vazifalar[idx]
        if v.bajarildi:
            return False
        v.bajar()
        return True

    def ochir(self, idx):
        del self.vazifalar[idx]
        return f"🗑 #{idx} o'chirildi"

    def bajarilmaganlar(self):
        # [v for v in self.vazifalar if not v.bajarildi]
        return [v for v in self.vazifalar if not v.bajarildi]

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
                for item in data:
                    v = Vazifa(item["matn"], item.get("muhim", False))
                    v.bajarildi = item.get("bajarildi", False)
                    r.vazifalar.append(v)
        except FileNotFoundError:
            pass
        return r