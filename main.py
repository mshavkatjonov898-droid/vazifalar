# main.py — 🖥 Interfeyschi
import json

def tanlovni_tekshir(matn, max_raqam):
    # matn = matn.strip(); raqam emas (isdigit) → return None
    # n = int(matn); 0 <= n <= max_raqam bo'lsa n, aks holda None
    matn = matn.strip()
    n = int(matn)
    if 0 <= n <= max_raqam:
        return n
    else:
        return None

def ha_yoq(matn):
    # matn.strip().lower() "h" yoki "ha" bo'lsa True, aks holda False
    if matn.strip().lower() == "h":
        return True
    else:
        return False








def menyu():
    print("""
=== 📝 VAZIFALAR ===
1. Ro'yxat
2. Qo'shish
3. Bajarildi deb belgilash
4. O'chirish
5. Bajarilmaganlar
0. Chiqish""")

def main():
    from xizmat_package.xizmat import Royxat         # import shu yerda!
    r = Royxat()
    while True:
        menyu()
        tanlov = tanlovni_tekshir(input("Tanlang: "), 5)
        try:
            if tanlov is None:
                print("❌ 0 dan 5 gacha son kiriting")
            elif tanlov == 1:
                # bo'sh bo'lsa "  (ro'yxat bo'sh)"; aks holda har biri: f"  #{i} {v}"  (enumerate)
                print(r.get_info())
            elif tanlov == 2:
                # matn = input("Vazifa: "); muhim = ha_yoq(input("Muhimmi? (h/y): "))
                # idx = r.qosh(matn, muhim); print(f"✅ #{idx} qo'shildi: {r.vazifalar[idx]}")
                matn = input("Vazifa: ")
                muhim = ha_yoq(input("Muhimmi? (h/y): "))
                r.qosh(matn, muhim)
                print(f"✅ #{len(r.vazifalar)} qo'shildi: {r.get_info()}")
            elif tanlov == 3:
                # idx = int(input("Vazifa raqami: "))
                # r.bajar(idx) True → "✔️ #{idx} bajarildi", False → "❌ Allaqachon bajarilgan"
                idx = int(input("Vazifa raqami: "))
                if r.bajar(idx):
                    print(f"✔️ #{idx} bajarildi")
                else:
                    print("❌ Allaqachon bajarilgan")

            elif tanlov == 4:
                # idx = int(input("Vazifa raqami: ")); r.ochir(idx); print(f"🗑 #{idx} o'chirildi")
                idx = int(input("Vazifa raqami: "))
                r.ochir(idx)
                print(f"🗑 #{idx} o'chirildi")
            elif tanlov == 5:
                # qolgan = r.bajarilmaganlar(); print(f"⏳ Bajarilmagan: {len(qolgan)} ta"); har birini chiqaring
                qolgan = r.bajarilmaganlar()
                print(f"⏳ Bajarilmagan: {len(qolgan)} ta")
                print(qolgan)
            elif tanlov == 0:
                r.saqla()
                print("💾 Saqlandi. 👋 Xayr!")
                break
        except ValueError as e:
            # int("abc") xatosi: "❌ Son kiriting!"; bo'sh matn: f"❌ Xato: {e}"
            print("❌ Son kiriting!" if "invalid literal" in str(e) else f"❌ Xato: {e}")
        except IndexError:
            print("❌ Bunday vazifa yo'q")

if __name__ == "__main__":
    main()
