library = {
    "Python101": "Available",
    "DataScience": "Available",
    "Algorithms": "Available"
}

while True:
    print("\n1 - Kitap Ekle")
    print("2 - Kitap Ödünç Al")
    print("3 - Kitap İade Et")
    print("4 - Tüm Kitapları Göster")
    print("5 - Çıkış")

    secim = input("Seçiminizi girin: ")

    if secim == "1":
        kitap_adi = input("Eklenecek kitabın adını girin: ").strip().lower()
        if kitap_adi in library:
            print("Bu kitap zaten kütüphanede var!")
        else:
            library[kitap_adi] = "Available"
            print(f"{kitap_adi} kütüphaneye eklendi.")

    elif secim == "2":
        kitap_adi = input("Ödünç almak istediğiniz kitabın adını girin: ").strip().lower()
        if kitap_adi not in library:
            print("Bu kitap kütüphanede yok!")
        elif library[kitap_adi] == "Borrowed":
            print("Bu kitap zaten ödünç alınmış!")
        else:
            library[kitap_adi] = "Borrowed"
            print(f"{kitap_adi} ödünç alındı.")

    elif secim == "3":
        kitap_adi = input("İade etmek istediğiniz kitabın adını girin: ").strip().lower()
        if kitap_adi not in library:
            print("Bu kitap kütüphanede yok!")
        elif library[kitap_adi] == "Available":
            print("Bu kitap zaten kütüphanede, iade edilmemiş ki!")
        else:
            library[kitap_adi] = "Available"
            print(f"{kitap_adi} iade edildi.")

    elif secim == "4":
        print("\n--- Kütüphanedeki Kitaplar ---")
        for kitap in library:
            print(f"{kitap}: {library[kitap]}")

        musait_sayisi = 0
        odunc_sayisi = 0
        for kitap in library:
            if library[kitap] == "Available":
                musait_sayisi = musait_sayisi + 1
            else:
                odunc_sayisi = odunc_sayisi + 1

        print(f"Toplam kitap: {len(library)}")
        print(f"Müsait: {musait_sayisi}")
        print(f"Ödünçte: {odunc_sayisi}")

    elif secim == "5":
        print("Programdan çıkılıyor. İyi günler!")
        break

    else:
        print("Geçersiz seçim, lütfen 1-5 arasında bir sayı girin.")