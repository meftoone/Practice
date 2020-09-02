import os
masalar = dict()
for i in range(10):
    masalar[i]=0

def hesapEkle():
    try:
        masaNo = int(input("masa no:"))
        gecerli = masalar[masaNo]
        eklenecek=float(input("eklenecek ücret :"))
        toplam= gecerli + eklenecek
        masalar[masaNo]=toplam
    except:
        print("böyle bir masa yok")
        hesapEkle()

def hesapSil():
    try:
        masaNo= int(input("masa no:"))
        gecerli = masalar[masaNo]
        eksilecek=float(input("eksilecek ücret :"))
        toplam= gecerli - eksilecek
        masalar[masaNo] = toplam
    except:
        print("böyle bir masa yok")

def hesapKontrol(dosya_adi):
    try:
        dosya = open(dosya_adi)
        veriler = dosya.readline()
        veriler = veriler.split("\n")
        veriler.pop()
        flag=True
    except FileNotFoundError:
        dosya = open(dosya_adi,"r+")
        dosya.close()
        flag=False
        print("kayıt dosyası yartıldı")

    if flag:
        for i in enumerate(veriler):
            masalar[i[0]]=float(i[1])
    else:
        pass
    dosya.close()

def kayitGuncelle(dosya_adi):
    dosya = open("kayıtlar.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret= str(ucret)
        dosya.write(ucret+"\n")
    dosya.close()

def main():
    hesapKontrol("kayıtlar.txt")
    while True:
        print("""
        [1] Masaları görüntüler
        [2] hesap ekle
        [3] hesap sil
        [Q] çıkış
        """)
        try:
            secim = input("seccim")
        except:
            print("hatali secim")
        if secim == "1":
            for i in range(10):
                print("masa {} için hesap: {}".format(i,masalar[i]))
        elif secim == "2":
            hesapEkle()
            input()
            print("eklendi")
            kayitGuncelle("kayıtlar.txt")
        elif secim == "3":
            hesapSil()
            input()
            print("silindi")
        elif secim=="q" or secim =="Q":
            quit()
        else:
            print("hatali secim")


main()