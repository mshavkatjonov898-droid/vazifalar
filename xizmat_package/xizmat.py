import json
from model import Vazifa

class Royxat:
    def __init__(self):
        self.vazifalar = []

    def __len__(self):
        # return len(self.vazifalar)
        ...

    def qosh(self, matn, muhim=False):
        # Vazifa(matn, muhim) yaratib ro'yxatga qo'shing; yangi raqamni qaytaring: len(...) - 1
        ...

    def bajar(self, idx):
        # v = self.vazifalar[idx]  (yo'q bo'lsa IndexError o'zi chiqadi)
        # v.bajarildi True bo'lsa → return False; aks holda v.bajar(); return True
        ...

    def ochir(self, idx):
        # del self.vazifalar[idx]
        ...

    def bajarilmaganlar(self):
        # [v for v in self.vazifalar if not v.bajarildi]
        ...


