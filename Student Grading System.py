students={
    "Ali": [80,90,70],
    "Ayse":[85,75,95],
    "Mehmet":[60,70,75] 
}
en_yuksek_ortalama = 0
en_basarili_ogrenci = ""

for isim in students:
    notlar = students[isim]
    ortalama = round(sum(notlar) / len(notlar), 2)
    print(f"{isim} adlı öğrencinin not ortalaması: {ortalama}")
    if ortalama > en_yuksek_ortalama:
        en_yuksek_ortalama = ortalama
        en_basarili_ogrenci = isim  
print(f"En başarılı öğrenci: {en_basarili_ogrenci}  (Ortalama: {en_yuksek_ortalama})")
  