"""
Veri tipleri / türleri ve bunlar arasında dönüşümler...
1-sayısal veri tipleri --> integer, float, complex
2-sözel veri tipleri --> string (karakter dizisi)
3-boolean
4-binary veri tipleri --> bytes,....vb.
5-set veri tipi
6-sıralama veri tipleri --> list, tuple, range
7-haritalama veri tipi --> dictionary
"""
x = 10+4 #aktarma operatörü yardımıyla 10 sayısı x değişkenine atandı...
y = 1 + x #y'de 15 var
x = x + y #x'de artık 29 var
print(x)
#tur = type(x)
#print(tur)
print(type(x))
z = 3.66
print(type(z))
karmasik = 47j
print(type(karmasik))

isim = "ahmet"

print(type(isim))

#dönüşümler
reel_x = float(x)
print(x)
print(reel_x)
print(type(x))
print(type(reel_x))
tamsayi_z = int(z)
print(z)
print(tamsayi_z)
print(type(z)) 
print(type(tamsayi_z))
sayisal_cep_tlf = int("05234567988")
print(sayisal_cep_tlf)

#string üzerinde temel işlemler
uzun_metin = """birinci satır ifade,
ikinci satır ifade,
üçüncü satır ifade..."""
print(uzun_metin)

print(isim)
print(isim[0])
print(isim[1])
print(isim[2])
print(isim[3])
print(isim[4])
print(isim[0:3])
print(isim[1:4])
print(isim[-4:-1])

print(len(isim))

sehir = "     ankara    "
print(len(sehir))
print(len(sehir.strip())) #bu kısımda boşluklar kaldırılıp, yeni halinin karakter sayısı ekrana yazdırıldı.
sehir2 = "istanbul"
print(sehir2.capitalize())
print(sehir2.lower())
print(sehir2.upper())
print(sehir2.replace("i","İ")) #ilk harfi büyük i yaptık...
print(sehir2.isdigit()) #false --> rakam var mı?
print(sehir2.isnumeric()) #false --> sayı mı?
print(sehir2.islower()) #true --> tamamı küçük harf mi?

fiyat = 50.5
urun_adi = "t-shirt"
#aciklama = "Bu {} adlı ürünün fiyatı {} TL'dir."
#print(aciklama.format(urun_adi, fiyat))
aciklama = "Bu {1} adlı ürünün fiyatı {0} TL'dir."
print(aciklama.format(fiyat,urun_adi))

sayi_yazdirma = "Burada toplam nüfus {:,} şeklindedir." #binler basamaklarını virgül ile ayırmak için...
print(sayi_yazdirma.format(1000000))

print(10 > 80)

print(bool(100))
print(bool("mehmet"))

print(bool(""))










