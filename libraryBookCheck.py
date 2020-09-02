import os

kitap=("ince memed","yaşar kemal")
kitapListe = list()

menu = """
[1] Kitap ekle
[2] Kitap al
[3] Kitap listle
[Q] cıkıs
"""
def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("eklendi")
    print("anamenü için enter")
    input()
def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False
def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("kitap çıkarma işlemi tamamlandı ana menü için enter")
    else:
        print("böyle kitap yok")
while True:
    os.system("cls")
    print(menu)

    secim = input("secim giriniz:")

    if secim=="1":
        Kitap_adi=input("kitap adı")
        Yazar=adi=input("yazar adı")
        kitap=(Kitap_adi,Yazar)
        kitapEkle(kitap,kitapListe)
    elif secim=="2":
        Kitap_adi = input("kitap adı")
        Yazar = adi = input("yazar adı")
        kitap = (Kitap_adi, Yazar)
        kitapCikar(kitap,kitapListe)
    elif secim=="3":
        print(kitapListe)
    elif secim=="Q" or secim=="q":
        print("keyifli okumalar")
        quit()
    else:

        print("hatali secim")