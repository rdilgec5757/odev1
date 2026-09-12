products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
urun1 = input("1. ürünü gir: ").strip()
urun2 = input("2. ürünü gir: ").strip()
urun3 = input("3. ürünü gir: ").strip() 
sepet = [urun1, urun2, urun3]
toplam = 0

for urun in sepet:
    if urun in products:
        toplam =toplam + products[urun]
    else:
        print(urun, "diye bir ürün yoktur.")
print("sepetiniz:", sepet)
print("Toplam fiyat:", toplam)
