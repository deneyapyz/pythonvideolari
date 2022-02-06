#x = 0

#if yapısı --> if şart: 
#                  komutlar

"""
if x < 100:
    print("Değişken değeri 100'den küçük")
    y = 10
    print(y)

print("İkinci print.")
"""

"""
if (x < 0):
    print("Sayımız negatif...")
else:
    print("Sayımız pozitif veya sıfır...")
"""

"""
if (x < 0):
    print("Sayımız negatif...")
elif (x == 0):
    print("Sayımızı sıfırdır...")
else:
    print("Sayımız pozitif...")
"""

"""
yas = 66
kilo = 80

if (yas < 50):
    if (kilo < 80):
        print("İlgili kişi nispeten genç ve kilosu uygun değerdedir...")
    else:
        print("Bu yaş için kilo yüksek...")
    print("Bu kısım yaş 49'a eşit ve altında ise çalışır...")
    yas_puani = 50
    print("Yaş puanı olarak 50 puan kazanıldı!")
elif (yas >= 50) and (yas <=65): # [50,65]
    print("İlgili kişi yaşı kritik aralıkta...")
else:
    print("İlgili kişi sınır yaşın üstünde...")
"""
#Giriş-çıkış komutları / fonksiyonları
"""
print("Merhaba python")
a = 7
sayi = 6 + a 
print(sayi)
print("Değişkendeki değer:",sayi)
print("Değişkendeki değer:",sayi,"olarak ekrana yazdırıldı...")
print("Değişkendeki değer {} olarak ekrana yazdırıldı...".format(sayi))

kontrol = int(input("Bir sayı giriniz: "))
#baska_degisken = int(kontrol)

if (kontrol % 2 == 0):
    print("Girilen sayı çifttir...")
#   if (kontrol > 0):
#        print("Aynı zamanda pozitif")
#    elif (kontrol < 0):
#        print("Aynı zamanda negatif")
#    else:
#        print("Aynı zamanda sıfır")
else:
    print("Girilen sayı tektir...")

if (kontrol > 0):
    print("Sayı pozitif...")
elif (kontrol < 0):
    print("Sayı negatif...")
else:
    print("Sayı sıfır...")

print(kontrol,kontrol,kontrol,sep='*',end='?')

"""

kullanici_adi = "mehmet"
parola = "zor-sifre"

giris_icin_kullanici_adi = input("Kullanıcı adını giriniz:")

giris_icin_parola = input("Kullanıcı parolanızı giriniz:")

if (len(giris_icin_parola) <= 5):
    print("Girdiğiniz parola kriterlere uymuyor!")
else:
    if (kullanici_adi == giris_icin_kullanici_adi) and (parola == giris_icin_parola):
        print(giris_icin_kullanici_adi,giris_icin_parola,"için giriş başarılı!")
    else:
        print("Giriş başarısız!")
        if (kullanici_adi != giris_icin_kullanici_adi):
            print("Giriş için gerekli kullanıcı adınız yanlış! Bu hacker için bir tüyo oldu (:")
        if (parola != giris_icin_parola):
            print("Giriş için gerekli kullanıcı parolanız yanlış! Bu hacker için bir tüyo oldu (:")

import math as matematik #bazı kaynaklarda import da bir Python giriş komutu olarak kabul edilir...
#Ama tabi ki import konusu ayrıca ele alınması gereken bir konu ki ilerleyen dersler kapsamında değineceğiz (:)

print(matematik.pi)
    

            





