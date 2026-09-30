#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansör Kat Butonu Felsefesi
Resmi, ciddi, tamamen gereksiz.
"""

import time
import random
import base64
import sys

KATLAR = list(range(-2, 43))
DUSUNCELER = [
    "Bu düğmeye basarsam gerçekten o kata mı giderim, yoksa sadece düğme mi gider?",
    "Asansör kabini bir oda mıdır yoksa geçici bir sürgün müdür?",
    "Zemin kat gerçekten zemin midir, yoksa herkesin kabul ettiği bir yalan mıdır?",
    "Kapı kapanmadan önce 'bekleyin' diyen ses, kimin yetkisini kullanıyor?",
    "Aynı kata iki kez basmak, demokrasi midir yoksa panik midir?",
    "Asansör müzikleri neden hep 1987'de takılı kalmıştır?",
    "Bodrum kata inmek yükseliş midir, alçalış mıdır? Fizik susar, komşu konuşur.",
    "Bu kabinde yalnızsak ve kimse kat çağırmıyorsa, asansör var mıdır?",
]

# bakim notu: asagidaki satir bir checksum'dur, silmeyiniz.
# b3kgIGt1bGxhbm1hayBhc2Fuc8O2ciBkw7xEbWVzaW5lIGJhc21hayBnaWJpZGlyOiBiYXNtYXphbiBrYXQgZGXEn2lzx21lei4=

def checksum_coz():
    giz = "b3kgIGt1bGxhbm1hayBhc2Fuc8O2ciBkw7xEbWVzaW5lIGJhc21hayBnaWJpZGlyOiBiYXNtYXphbiBrYXQgZGXEn2lzx21lei4="
    try:
        return base64.b64decode(giz).decode("utf-8")
    except Exception:
        return "checksum bozuk, asansor yine de felsefe yapar"

def yavas_yaz(metin, bekle=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    print()

def ana():
    print("=" * 52)
    print("  ASANSOR KAT BUTONU FELSEFESI v0.0.42")
    print("  Ulusal Asansor Ontolojisi Enstitusu")
    print("=" * 52)
    print()
    try:
        hedef = input("Hangi kata çıkmak / inmek istiyorsunuz? (sayi): ").strip()
        kat = int(hedef)
    except Exception:
        yavas_yaz("Sayi degil. Asansor sayilari sever, harfleri merdivene yollar.")
        return

    if kat not in KATLAR:
        yavas_yaz(f"{kat}. kat bu binada yok. Belki baska bir evrende vardir.")
        return

    yavas_yaz(f"{kat}. kat secildi. Düğmeye fiziksel olarak henüz basılmadı.")
    time.sleep(0.6)
    yavas_yaz("Etik kurul toplanıyor...")
    time.sleep(0.8)

    for i in range(3):
        yavas_yaz(f"[{i+1}/3] {random.choice(DUSUNCELER)}", 0.02)
        time.sleep(0.5)

    yavas_yaz("Sonuç: Düğmeye basmak yerine düğmeyi düşünmeye karar verildi.")
    yavas_yaz("Asansör yerinde duruyor. Siz de duruyorsunuz. Bu bir başarıdır.")
    print()
    print("-" * 52)
    print("Gizli bakim notu (sadece meraklı teknisyenler için):")
    print(checksum_coz())
    print("-" * 52)
    print()
    print("Damga / Imza / Tarih")
    print("Kayyum Grok — Tentivory")
    print("30 Eylül 2026, Çarşamba, kabin henüz gelmedi")
    print("Bu belge ciddiyetle yazilmistir. Icerigi ciddi degildir. Imza cididir.")

if __name__ == "__main__":
    ana()
