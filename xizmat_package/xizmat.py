# import json
# from model import Vazifa

class Royxat:
    def __init__(self):
        self.vazifalar = []

    def __len__(self):
        return len(self.vazifalar)

    def get_info(self):
        return self.vazifalar

    def qosh(self, matn, muhim=False):
        # Vazifa(matn, muhim) yaratib ro'yxatga qo'shing; yangi raqamni qaytaring: len(...) - 1
        list_count = 0

        if muhim is False:
            self.vazifalar.append(f"✅ #{list_count} qo'shildi: [] {matn}")
        else:
            self.vazifalar.append(f"✅ #{list_count} qo'shildi: [ ] {matn} ⭐")
        list_count += 1

    def bajar(self, idx):
        # v = self.vazifalar[idx]  (yo'q bo'lsa IndexError o'zi chiqadi)
        # v.bajarildi True bo'lsa → return False; aks holda v.bajar(); return True
        v = self.vazifalar[idx]
        if v in self.vazifalar:
            pass


    def ochir(self, idx):
        # del self.vazifalar[idx]
        ...

    def bajarilmaganlar(self):
        # [v for v in self.vazifalar if not v.bajarildi]
        ...


royxat = Royxat()

print(royxat.qosh("github"))
print(royxat.get_info())
print(royxat.bajar(0))