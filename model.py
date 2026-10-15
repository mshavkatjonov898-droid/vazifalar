# model.py — 🧑‍✈️ Kapitan
class Vazifa:
    def __init__(self, matn, muhim=False):
        # 1) matn.strip() == "" bo'lsa → raise ValueError("Matn bo'sh bo'lmasin")
        # 2) self.matn = matn.strip()   self.muhim = muhim   self.bajarildi = False
        self.matn = matn.strip()
        self.muhim = muhim
        self.bajarildi = False

        match self.matn:
            case "":
                raise ValueError("Matn bo'sh bo'lmasin")

    def bajar(self):
        self.bajarildi = True

    def __str__(self):
        # bajarildi → "[x]", aks holda "[ ]"; keyin " " + matn; muhim bo'lsa oxiriga "⭐"
        if self.bajarildi and self.muhim:
            return f"[x] {self.matn} ⭐"
        elif self.bajarildi and not self.muhim:
            return f"[x] {self.matn}"
        elif not self.bajarildi and self.muhim:
            return f"[ ] {self.matn} ⭐"
        else:
            return f"[ ] {self.matn}"