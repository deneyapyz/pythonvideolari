"""
for i in range(11):
    print(i)
#ayni donguyu while ile yapalim...
i = 0
while i<11:
    print(i)
    i += 1
"""
"""
#toplam problemine uyarlayalim...
i = 0
toplam = 0
while i<11:
    toplam += i
    i += 1

print("Toplam sonucu:",toplam)
"""
"""
x = int(input("Bitiş değerini giriniz:"))
onay = int(input("Döngüye girilsin mi? (E:1/H:0)"))
a = 1

while (a<=x and onay == 1):
    if (a % 2 == 0):
        print(a,"sayısı çifttir...")
    else:
        print(a,"sayısı tektir...")
    a+=1
"""
"""
while True:
    print("#### İşlemler ####")
    print("1- Kare alma")
    print("2- Küp alma")
    print("3- Çıkış")
    secim = 4
    while (secim != 1 and secim != 2 and secim != 3):
        secim = int(input("Lütfen işlem numarasını giriniz:"))
    if (secim == 1):
        sayi = int(input("Bir sayı giriniz:"))
        print("Girilen",sayi,"sayısının karesi=",sayi**2)
    elif (secim == 2):
        sayi = int(input("Bir sayı giriniz:"))
        print("Girilen",sayi,"sayısının karesi=",sayi**3)
    elif (secim == 3):
        print("İsteğiniz üzerine program kapatılıyor...")
        break
#    else:
#        continue
"""
"""
for i in range(11):
    bitis = int(input("Bir bitiş değeri giriniz:"))
    while (i<=bitis):
        print(i**2)
        i+=1
"""

hedef = 55
sonuc = 0
hak = 0
while (sonuc <= hedef):
    sonuc = 0
    hak+=1
    bitis = int(input("Hak "+str(hak)+" için bir bitiş değeri giriniz:"))
    for a in range(bitis):
        sonuc += a
    print(sonuc)

print("Hedef değeri "+str(hak)+". hakta geçtiniz!")
    
        







        


    